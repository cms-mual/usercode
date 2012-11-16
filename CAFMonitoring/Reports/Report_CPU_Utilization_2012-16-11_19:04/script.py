#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
Created on 2010-03-01
@author: Rapolas Kaselis <rapolas.kaselis@cern.ch>

Collects users statistics about submitted jobs to CAF.

Usage: python script.py [options]

Options:
    -p <period in weeks>, --period <period in weeks>    How many weeks to go back
    -g <groupname>, --group <groupname>                 For which group statistics should be counted

Examples:
    python script.py                                    Gets the information for all three groups, and for three different periods: 1week, 1month and 3months
    python script.py -p 4                               Gets the information for all three groups for 4weeks (1month)
    python script.py --period 1 --group CMSALCA         Gets the information for group CMSALCA and for one week
    python script.py --p 1 -g CMSALCA                   Gets the information for group CMSALCA and for one week

Group names: CMSALCA, CMSCOMM, CMSPHYS; It can be either uppercase or lowercase or mixed
'''

import os, sys, getopt, commands, re
from sets import Set
from datetime import date

BHPART = "bhpart"

def detectCPUs():
    """
    Detects the number of CPUs are on a system.
    """
    # Linux, Unix, MacOS
    if hasattr(os, "sysconf"):
        if os.sysconf_names.has_key("SC_NPROCESSORS_ONLN"):
            #Linux, Unix
            ncpus = os.sysconf("SC_NPROCESSORS_ONLN")
            if isinstace(ncpus, int) and ncpus > 0:
                return ncpus
            else:
                return int(os.popen2("sysctl -n hw.ncpu")[1].read())
    # Windows
    if os.environ.has_key("NUMBER_OF_PROCESSORS"):
        ncpus = int(os.environ["NUMBER_OF_PROCESSORS"])
        if ncpus > 0:
            return ncpus
    
    # default, incase something went wrong
    return 1    

def which(program):
    '''
    Checks, if given program exists and is executable
    on current system
    '''
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath = os.path.split(program)[0]

    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ['PATH'].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None

def createBhpartFile():
    if which("bhpart"):
        command = "bhpart -r CMSCAF"
        if os.path.exists(BHPART):
            os.remove(BHPART)
        try:
            file = open(BHPART, "w")
            file.write(commands.getoutput(command))
        finally:
            file.close()
    else:
        print "No bhpart command was found on this system"

def readBhpartFile():
    """
    Reads contents of bhpart file
    """
    createBhpartFile()
    try:
        try:
            file = open(BHPART, "r")
            info = file.readlines()
        except:
            print "File was not found, can not continue!"
            sys.exit(2)
    finally:
        file.close()
    return info

class Base(object):
    def __init__(self, name):
        self.name = name
        self.jobs = 0
        self.cpu = 0.0
        self.wall = 0

    def getEfficiency(self):
        self.wall = self.getWallTime()
        self.cpu = self.getCpuTime()
        if self.wall > 0:
            return self.cpu * 100.0 / self.wall
        return 0.0

    def __repr__(self): return self.name
    def __str__(self): return self.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return self.name == other.name

class Group(Base):
    bhpart = readBhpartFile()
    total = 0
    nogroup = 0
    failedsubmission = 0

    def getTotalUsers(groups):
        total = 0
        for g in groups:
            for sub in g.subs:
                total += len(sub.users)
        return total
    getTotalUsers = staticmethod(getTotalUsers)
       

    def getTotalEfficiency(groups):
        wall = 0
        cpu = 0.0
        for g in groups:
            wall += g.getWallTime()
            cpu += g.getCpuTime()
        if wall > 0.0:
            return cpu * 100.0 / wall
        return 0.0
    getTotalEfficiency = staticmethod(getTotalEfficiency)

    def getUniqueUsers(groups):
        s = Set()
        for g in groups:
            for u in g.getUnique():
                s.add(u)
        return len(s)
    getUniqueUsers = staticmethod(getUniqueUsers)

    def getActiveUsers(groups):
        s = Set()
        for g in groups:
            for u in g.getActive():
                s.add(u.name)
        return len(s)
    getActiveUsers = staticmethod(getActiveUsers)
    
    def getActive(self):
        s = Set()
        for sub in self.subs:
            for u in sub.getActive():
                s.add(u)
        l = list(s)
        l.sort()
        return l

    def getUnique(self):
        s = Set()
        for sub in self.subs:
            for u in sub.getUnique():
                s.add(u)
        return s

    def getTotal(self):
        total = 0
        for sub in self.subs:
            total += len(sub.users)
        return total

    def __init__(self, name):
        super(Group, self).__init__(name)
        self.subs = []
        self.__initialize()

    def __initialize(self):
        p = "%s" % self.name[3:]
        for line in Group.bhpart:
            if line.startswith(p):
                name = line.split()[0]
                subgroup = Sub(name, self)
                self.subs.append(subgroup)
        self.subs.sort()

    def getJobs(self):
        jobs = 0
        for sub in self.subs:
            jobs += sub.getJobs()
        return jobs
    
    def getWallTime(self):
        wall = 0
        for sub in self.subs:
            wall += sub.getWallTime()
        return wall

    def getCpuTime(self):
        cpu = 0.0
        for sub in self.subs:
            cpu += sub.getCpuTime()
        return cpu

class Sub(Base):
    def __init__(self, name, group):
        super(Sub, self).__init__(name)
        self.group = group
        self.users = []
        self.__initialize()

    def __initialize(self):
        p = "CMSCAF/u_%s/%s/" % (self.group.name, self.name)
        found = False
        for line in Group.bhpart:
            if line.find(p) != -1 or found:
                found = True
                if line == "\n":
                    break;
                try: username = line.split()[0]
                except: print line
                if not username.isupper():
                    user = User(username)
                    self.users.append(user)

    def getWallTime(self):
        wall = 0
        for user in self.users:
            wall += user.wall
        return wall

    def getCpuTime(self):
        cpu = 0.0
        for user in self.users:
            cpu += user.cpu
        return cpu
    
    def getActive(self):
        s = Set()
        for u in self.users:
            if u.isActive():
                s.add(u)
        return s

    def getActiveUsers(self):
        l = []
        for u in self.users:
            if u.isActive():
                l.append(u)

        l.sort()
        l.reverse()
        return l

    def getUnique(self):
        s = Set()
        for u in self.users:
            s.add(u.name)
        return s
        
    def getNonActiveUsers(self):
        nonActive = []
        for user in self.users:
            if not user.isActive():
                nonActive.append(user.name)
        nonActive.sort()
        return nonActive
        
    def getJobs(self):
        jobs = 0
        for user in self.users:
            jobs += user.jobs
        return jobs
    def __cmp__(self, other):
        if self.name < other.name: return -1
        if self.name == other.name: return 0
        if self.name > other.name: return 1

class User(Base):
    def __init__(self, name):
        super(User, self).__init__(name)

    def isActive(self): return self.jobs > 0

    def getEfficiency(self):
        if self.wall > 0:
            return self.cpu * 100.0 / self.wall
        return 0.0

    def __cmp__(self, other):
        if self.wall < other.wall: return -1
        if self.wall == other.wall: return 0
        if self.wall > other.wall: return 1

class Parser:
    def __init__(self, groups):
        self.groups = groups
        self.periods = []
        self.interested = []

    def getInfo(self):
        filesToParse = self.__getFilesList()

        p = re.compile("^\d+\.\d{6,6}$")
        tmp = 0
        printer = Printer(self.groups, self.interested)
        for p1 in self.periods:
            printer.period = p1
            try:
                errors = open("errors_%s.txt" % p1, "w")
                for p2 in range(tmp, p1):
                    file = filesToParse.pop()
                    content = self.__getContent(file)
                  
                    for l in content.split("\n"):
                        Group.total += 1
                        line = [f.strip() for f in l.split() if f]
                        try: wall = int(line[2]) - int(line[10])
                        except:
                            Group.failedsubmission += 1
                            errors.write("Error in conversion: %s\n" % l)
                            continue

                        cputimes = []
                        for value in line:
                            if p.match(value): cputimes.append(value)

                        cpu = -1
                        if len(cputimes) == 2:
                            try: cpu = float(cputimes[0]) + float(cputimes[1])
                            except: cpu = -1

                        if cpu == -1:
                            Group.failedsubmission += 1
                            errors.write("Failed to get cpu times: %s\n" % (l))
                            continue

                        groupstr = line[-4]
                        if groupstr == "-1" or groupstr.isdigit():
                            groupstr = line[-5]
                            if groupstr == "-1" or groupstr.isdigit():
                                Group.nogroup += 1
                                errors.write("No group info %s\n" % l)
                                continue

                        parts = [part for part in groupstr.split("/") if part]

                        if len(parts) < 3:
                            errors.write("Error extracting information: %s\n" % l)
                            Group.nogroup += 1
                            print "whoops"
                            continue

                        group = self.__getGroup(parts[0][2:])
                        if not group:
                            Group.nogroup += 1
                            errors.write("No group was found: %s\n" % l)
                            continue

                        sub = self.__getSubgroup(parts[1])
                        if not sub:
                            Group.nogroup += 1
                            errors.write("No subgroup was found: %s\n" % l)
                            continue

                        user = self.__getUser(parts[2], sub)
                        if not user:
                            user = User(parts[2])
                            sub.users.append(user)
                            print "User %s was not found in group %s" % (user.name, sub.name)
                            print "Added not according by bhpart"

                        user.jobs += 1
                        user.wall += wall
                        user.cpu += cpu
                        
            finally:            
                errors.close()
                
            printer.output()

            print "done"
            tmp = p1

    def __getUser(self, name, subgroup):
        for u in subgroup.users:
            if u == name:
                return u

    def __getSubgroup(self, name):
        for g in self.groups:
            for s in g.subs:
                if s == name:
                    return s

    def __getGroup(self, name):
        for g in self.groups:
            if g == name:
                return g

    def __getContent(self, filename):
        pwd = os.getcwd()
        dir = ""
        content = ""
        if not (os.name == 'nt'):
            dir = "/afs/cern.ch/project/lsf/7.0/mnt/batch/work/batch/acct/"
            os.chdir(dir)
        zcat = "zcat %s" % (filename)
        grep = "grep cmscaf"
        tr = "tr -d '\"'"
        command = "%s | %s | %s" % (zcat, grep, tr)
        content = commands.getoutput(command)
        os.chdir(pwd)
        return content

    def __getFilesList(self):
        s = Set()
        pwd = os.getcwd()
        dir = ""
        if not (os.name == 'nt'):
            dir = "/afs/cern.ch/project/lsf/7.0/mnt/batch/work/batch/acct/"
            os.chdir(dir)
        lsf = "lsb.acct.%s.gz"
        week = int(date.today().strftime("%W"))
        year = int(date.today().strftime("%Y"))
        self.periods.sort()
        weeksNumber = self.periods[-1]
        while len(s) < weeksNumber:
            found = False
            while not found:
                week -= 1
                if week < 0:
                    week = 53
                    year -= 1

                name = lsf % ("%s%s" % (year, week))
                if week < 10:
                    name = lsf % ("%s0%s" % (year, week))
                found = os.path.exists(name)

            if name not in s:
                s.add(name)
        os.chdir(pwd)
        l = list(s)
        l.sort()
        return l

class Printer:
    def __init__(self, groups, interested):
        self.groups = groups
        self.interested = interested
        self.period = 0

    def output(self):
        try:
            self.__file = open(self.__getfilename(), "w")
            self.__outputHeader()
            self.__outputTable()
            for g in self.groups:
                if g in self.interested:
                    self.__outputGroup(g)
            self.__createPdfs()
        finally:
            self.__file.close()

    def __createPdfs(self):
        file = self.__getfilename()
        temp = "temp.ps"
        createps = "enscript --word-wrap -p %s -t %s --header='$n|%%W|Page $%% of $='  %s" % (temp, file, file)
        createpdf = "ps2pdf %s %s.pdf" % (temp, file)
        os.system(createps)
        os.system(createpdf)
        os.remove(temp)

    def __outputTable(self):
        self.__file.write("\n%s\n" % ("-" * 52))
        
        line = "|"
        for g in self.groups:
            line += " %s |" % (g.name)
        self.__file.write("| %s %s\n" % (" ".ljust(18), line))
        self.__file.write("%s\n" % ("-" * 52))
        
        line = "|"
        for g in self.groups:
            line += " %s |" % (str(len(g.getActive())).center(7))
        self.__file.write("| %s %s\n" % ("Active users".ljust(18), line))
#        self.__file.write("%s\n" % ("-" * 52))
        
        line = "|"
        for g in self.groups:
            line += " %s |" % (str(len(g.getUnique())).center(7))
        self.__file.write("| %s %s\n" % ("Total unique users".ljust(18), line))
#        self.__file.write("%s\n" % ("-" * 52))
        
        line = "|"
        for g in self.groups:
            line += " %s |" % (str(g.getTotal()).center(7))
        self.__file.write("| %s %s\n" % ("Total users".ljust(18), line))
#        self.__file.write("%s\n" % ("-" * 52))
        
        line = "|"
        for g in self.groups:
            eff = "%.2f%%" % g.getEfficiency()
            line += " %s |" % (eff.center(7))
        self.__file.write("| %s %s\n" % ("Efficiency".ljust(18), line))
        self.__file.write("%s\n\n" % ("-" * 52))
        
    def __outputGroup(self, group):
        self.__file.write("%s\n" % ("~" * 80))
#        self.__file.write("%s\n" % (group.name))
        for sub in group.subs:
            self.__outputSubgroup(sub)

    def __outputSubgroup(self, sub):
        self.__file.write("%s\n" % (sub.name))
        self.__file.write("%s %s %s %s %s\n" % ("USER".ljust(10), "WALL".ljust(12), "CPU".ljust(12), "#JOBS".ljust(8), "EFFICIENCY"))
        self.__file.write("%s\n" % ("-" * 68))

        active = sub.getActiveUsers()
        passive = sub.getNonActiveUsers()
        for u in active:
            uwall = "%s" % u.wall
            ucpu = "%.2f" % u.cpu
            ujobs = "%s" % u.jobs
            ueff = "%.2f%%" % u.getEfficiency()
            self.__file.write("%s %s %s %s %s\n" % (u.name.ljust(10), uwall.ljust(12), ucpu.ljust(12), ujobs.ljust(8), ueff))
            
        self.__file.write("%s\n" % ("-" * 68))
        wall = "%s" % sub.getWallTime()
        cpu = "%.2f" % sub.getCpuTime()
        jobs = "%s" % sub.getJobs()
        if sub.getEfficiency() > 0: eff =  "%.2f%%" % sub.getEfficiency()
        else: eff = "N/A"
        self.__file.write("%s %s %s %s %s\n\n" % ("TOTALS".ljust(10), wall.ljust(12), cpu.ljust(12), jobs.ljust(8), eff ))

        
        self.__file.write("Users, who were not active:\n")
        self.__file.write("%s\n\n" % ("; ".join(passive)))
        self.__file.write("%s\n" % (">" * 10))
        
    def __outputHeader(self):
        self.__file.write("\n%s\n" % (80 * "*"))
        self.__file.write("There was %s jobs in total.\n" % (Group.total))
        self.__file.write("%s (%.2f%%) jobs were without group information.\n" % (Group.nogroup, Group.nogroup*100.0/Group.total))
        self.__file.write("%s (%.2f%%) jobs failed at submission time.\n" % (Group.failedsubmission, Group.failedsubmission*100.0/Group.total))
        total = Group.getTotalUsers(self.groups)
        active = Group.getActiveUsers(self.groups)
        self.__file.write("Total active users: %s (%.2f%%).\n" % (active, active * 100.0 / total))
        unique = Group.getUniqueUsers(self.groups)
        self.__file.write("Total unique users: %s.\n" % unique)
        self.__file.write("Total users: %s.\n" % (total))
        eff = Group.getTotalEfficiency(self.groups)
        self.__file.write("Total efficiency of all groups: %.2f%%.\n" % (eff))
        self.__file.write("%s\n" % ("*" * 80))

    def __getfilename(self):
        today = date.today().strftime("%b%-e").lower()
        if self.period == 1:
            file = "%s_1_week" % (today)
        elif self.period == 4:
            file = "%s_1_month" % (today)
        elif self.period % 4 == 0:
            file = "%s_%s_months" % (today, self.period / 4)
        else:
            file = "%s_%s_weeks" % (today, self.period)
        return file
            
            
def usage():
    print __doc__
    sys.exit(1)

def getargs(opts):
    group = None
    period = 0
    for opt, arg in opts:
        if opt not in ("-p", "--period", "-g", "--group"):
            print "Unknown parameters given: %s" % (opt)
            usage()
            
        
        
        if opt in ("-p", "--period"):
            if not arg.isdigit():
                print "Period parameter should be integer"
                usage()
            else:
                period = int(arg)
            
            
        if opt in ("-g", "--group"):
            if arg.upper() not in ["CMSALCA", "CMSCOMM", "CMSPHYS"]:
                print "Unknown group given: %s" % (arg)
                print "Group has to be one of these: CMSALCA, CMSPHYS or CMSCOMM"
                usage()
            else:
                group = arg.upper()
                
    return group, period
    
def main(argv):
    """
    Extracts args and after checking continues
    """
    groupsnames = ["CMSALCA", "CMSCOMM", "CMSPHYS"]
    periods = [1, 4, 12]
    groups = []
    
    for g in groupsnames:
        groups.append(Group(g))
    os.remove(BHPART)
    
    parser = Parser(groups)
    
    if len(argv) % 2:
        usage()
    else:
        try:
            opts = getopt.getopt(argv, "p:g:", ["period=", "group="])[0]
        except getopt.GetoptError:
            usage()
    
    group, period = getargs(opts)
    if group:
        groups = [group]
    if period: periods = [period]

    parser.interested = groups
    parser.periods = periods
    print "Getting information for %s, for %s " % (groups, periods)
        
    
    parser.getInfo()
    
if __name__ == '__main__':
    if os.environ.has_key("SHELL"):
        shell = os.environ["SHELL"]
        os.environ["SHELL"] = "/bin/bash"

    main(sys.argv[1:])
    
    
    if os.environ.has_key("SHELL") and shell:
        os.environ["SHELL"] = shell
