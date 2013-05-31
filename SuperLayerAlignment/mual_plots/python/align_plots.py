import os, inspect, gc, csv, re, ctypes, array
import ROOT
from ROOT import (gROOT,
                  TCanvas, TGraphErrors, TStyle, TH1F,
                  kBlue, kRed, kGreen, kYellow)

execfile('tdrStyle.py')

class corrections_plotter:
    FLOAT_RE = re.compile(r'^(\-?\d+\.\d*|\d*\.\d+)$')
    INT_RE = re.compile(r'^-?\d+$')
    index_shift = {'wheel':2 , 'station':-1 , 'sector':-1}
    n_items = {'wheel':5, 'station':4, 'sector':14}
    f_colors = [kBlue, kRed, kGreen, kYellow]
    def __init__(self):
        self.data = []
        self.sign_conventions = {}
        self.canvas = TCanvas()
        self.hps = []
        self.frames = []
        self.framess = []
        self.file_list = []
        self.title = "Title"
        self.all_plots  = True
        self.plot_range = (0,0,0,0)
        self.scm = [] #sign convention mapping
        #define sign convention mapping
        self.scm.append(["x_100000", "signx"])
        self.scm.append(["x_100001", "signx"])
        self.scm.append(["x_100011", "signx"])
        self.scm.append(["x_100111", "signx"])
        self.scm.append(["x_101000", "signx"])
        self.scm.append(["x_111000", "signx"])
        self.scm.append(["y_100000", "signy"])
        self.scm.append(["y_010001", "signy"])
        self.scm.append(["y_010011", "signy"])
        self.scm.append(["y_010111", "signy"])
        self.scm.append(["y_011000", "signy"])
        self.scm.append(["y_111000", "signy"])
        self.scm.append(["z_101000", "signz"])
        self.scm.append(["z_011000", "signz"])
        self.scm.append(["z_111000", "signz"])
        self.scm.append(["phix_100111", "signy", "signz"])
        self.scm.append(["phix_010111", "signy", "signz"])
        self.scm.append(["phiy_100011", "signx", "signz"])
        self.scm.append(["phiy_000011", "signx", "signz"])
        self.scm.append(["phiy_100111", "signx", "signz"])
        self.scm.append(["phiy_010011", "signx", "signz"])
        self.scm.append(["phiy_010111", "signx", "signz"])
        self.scm.append(["phiz_100011", "signx", "signy"])
        self.scm.append(["phiz_010001", "signx", "signy"])
        self.scm.append(["phiz_000011", "signx", "signy"])
        self.scm.append(["phiz_100111", "signx", "signy"])
        self.scm.append(["phiz_010011", "signx", "signy"])
        self.scm.append(["phiz_010111", "signx", "signy"])
        self.scm.append(["db", "signx", "signy"])
        self.scm.append(["dai", "signx"])
        self.scm.append(["dphizsl2", "signx", "signy"])

        self.x_var = ""
        self.y_var = ""
        self.xo_var = ""
        self.yo_var = ""

    def setPlotRange(self, x_min, y_min, x_max, y_max):
        self.plot_range = (x_min, y_min, x_max, y_max)
        self.all_plots = False

    def setPlotAll(self, b = True):
        self.all_plots = b

    def getCanvas(self):
        return self.canvas

    def createCanvas(self):
        #create canvas and set style
        self.canvas = TCanvas("c1",self.title,200,10,700,500)
        self.canvas.SetGrid(True)
        style = gROOT.GetStyle("tdrStyle")
        style.SetOptTitle(1)
        style.SetTitleBorderSize(0)
        style.SetTitleFontSize(0.08)
        style.SetPadTopMargin(0.07)
        style.SetPadBottomMargin(0.13)
        style.SetPadLeftMargin(0.15)
        style.SetPadRightMargin(0.02)
        style.cd()
        
    def readFile(self, f_name, sign_conv = False):
        file_ = open(f_name, 'r')

        temp_suffix = '.temp'
        #create temporary files with excess whitespace removed
        temp_file = open(f_name + temp_suffix, 'w')
        line = file_.readline()
        while(line != ""):
            temp_file.write(re.sub(r' +', r' ', line))
            line = file_.readline()
        temp_file.close()
        file_.close()
        file_ = open(f_name + temp_suffix, 'r')

        csv_ = csv.reader(file_, delimiter=' ', quotechar='"')

        labels = []
        types = []
        file_cols = {}
        count = 0
        
        row = csv_.next() #get first row
        for label in row:
            labels.append(label) #store labels
            file_cols[label] = [] #create dictionary entries

        row = csv_.next() #get second row
        for item in row:
            types.append(self.getType(item)) #determine types for each column
        try:
            while(True): #store data by column
                for i in range(0,len(row)):
                    exec("val =%s(row[i])" % types[i]) #perform type casting
                    file_cols[labels[i]].append(val) #store data in column
                    count+=1
                row = csv_.next() #get next row
        except (StopIteration):
            file_.close()
            os.remove(f_name + temp_suffix)
        if(sign_conv):
            self.sign_conventions = file_cols
        else:
            self.data.append(file_cols)

    #identifies the type of the data
    def getType(self, s):
        if self.FLOAT_RE.match(s):
            value_type = 'float'
        elif self.INT_RE.match(s):
            value_type = 'int'
        else:
            value_type = ''
        return value_type

    #applies sign conventions
    def applySC(self):
        for f_n in range(0,len(self.data)):
            for i in self.scm:
                if(len(i) == 2):
                    self.data[f_n][i[0]] = [a*b for a, b in zip(self.data[f_n][i[0]], self.sign_conventions[i[1]])]
                elif(len(i) == 3):
                    self.data[f_n][i[0]] = [a*b*c for a, b, c in zip(self.data[f_n][i[0]], self.sign_conventions[i[1]], self.sign_conventions[i[2]])]

    #formats data for use in TGraphErrors and passes to plotGrid
    def plot(self, f, x_var, y_var, xo_var, yo_var):
        self.x_var = x_var
        self.y_var = y_var
        self.xo_var = xo_var
        self.yo_var = yo_var
        self.file_list = f
        
        var = [x_var, y_var, 'e'+x_var, 'e'+y_var, xo_var, yo_var]
        include = [1, 1, 1, 1, 1, 1]
        is_include = [0, 0, 0, 0, 1, 1]
        for f_n in f:
            for i in range(0,len(var)):
                if (not var[i] in self.data[f_n].keys()):
                    include[i] = 0
                if (not var[i] in self.index_shift.keys()):
                    is_include[i] = 0
        if((not include[0]) or (not include[1])):
           print "Warning: Nothing is being plotted!"
        
        #create structure
        #d is an array of 4 2d arrays
        #each 2d array represents a variable (x,y,ex,ey) each entry of the 2d array is an array of values pertaining to that variable
        #len(d) = 4
        #len(d[0]) = number of plots in x direction
        #len(d[0][0]) = number of plots in y direction
        #len(d[0][0][0]) = number of data points in each plot
        d = []
        for i in range(0, len(self.data)):
            d.append([])
        for f_n in f:
            for i in range(0,4):
                d[f_n].append([])
                for j in range(0,self.n_items[xo_var]):
                    d[f_n][i].append([])
                    for k in range(0,self.n_items[yo_var]):
                        d[f_n][i][j].append([])


        #fill structure
        for f_n in f:
            for i in range(0,len(self.data[f_n]['label'])): #iterate over rows
                val = []
                for j in range(0,len(var)): #iterate over names of variables to be collected
                    if (include[j]): #check if variable exists
                        if(is_include[j]): #add index shift if necessary
                            val.append(self.data[f_n][var[j]][i] + self.index_shift[var[j]])
                        else:
                            val.append(self.data[f_n][var[j]][i])
                    else: #if not put zero in place
                        val.append(0)
                i_x = int(val[4])
                i_y = int(val[5])
                for ii in range(0,4): #iterate over first 4 variables [x,y,ex,ey]
                    d[f_n][ii][i_x][i_y].append(val[ii])
                #determine y max and min
                try:
                    x_max = max(x_max, val[0])
                    x_min = min(x_min, val[0])
                    y_max = max(y_max, val[1])
                    y_min = min(y_min, val[1])
                except(Exception):
                    x_max = val[0]
                    x_min = val[0]
                    y_max = val[1]
                    y_min = val[1]

        #set min and max to +-10%
        xx_min = int(x_min)
        xx_max = int(x_max)
        if(xx_min == x_min and xx_max == x_max):
            xx_min = x_min - 1
            xx_max = x_max + 1
        else:
            xx_max = x_max + (x_max-x_min)*.1
            xx_min = x_min - (x_max-x_min)*.1

        yy_min = int(y_min)
        yy_max = int(y_max)
        if(yy_min == y_min and yy_max == y_max):
            yy_min = y_min - 1
            yy_max = y_max + 1
        else:
            yy_max = y_max + (y_max-y_min)*.1
            yy_min = y_min - (y_max-y_min)*.1

        bounds = (xx_min, yy_min, xx_max, yy_max)
        
        self.plotGrid(bounds, d)

    #generates a grid of plots
    def plotGrid(self, bounds, d):

        w, h = self.n_items[self.xo_var], self.n_items[self.yo_var]

        x_min, y_min, x_max, y_max = bounds
        
        if(self.all_plots):
            self.plot_range = (
            0-self.index_shift[self.xo_var],
            0-self.index_shift[self.yo_var],
            (w-1)-self.index_shift[self.xo_var], 
            (h-1)-self.index_shift[self.yo_var])
            rx_max, ry_max, rx_min, ry_min = (w,h,0,0)
        else:
            rx_min, ry_min, rx_max, ry_max = self.plot_range
            rx_min = min(max(rx_min + self.index_shift[self.xo_var], 0), w)
            ry_min = min(max(ry_min + self.index_shift[self.yo_var], 0), h)
            rx_max = max(min(rx_max + self.index_shift[self.xo_var] + 1, w), 0)
            ry_max = max(min(ry_max + self.index_shift[self.yo_var] + 1, h), 0)
            
        self.canvas.Divide(rx_max-rx_min,ry_max-ry_min)

        print self.file_list
        
        self.hps = []
        self.frames = []
        for f_n in range(0, len(self.data)):
            self.hps.append([])
            for i in range(rx_min, rx_max):
                self.hps[f_n].append([])
        for i in range(rx_min, rx_max):
            self.frames.append([])
            self.framess.append([])
            for j in range(ry_min, ry_max):
                self.canvas.cd(i + j*(rx_max-rx_min) + 1)
                self.frames[i].append(self.canvas.DrawFrame(x_min, y_min, x_max, y_max))
                self.frames[i][j].SetTitle("%s:%d, %s:%d" % (self.xo_var,
                                                                   i - self.index_shift[self.xo_var],
                                                                   self.yo_var,
                                                                   j - self.index_shift[self.yo_var]))
                self.frames[i][j].GetXaxis().SetTitle(self.x_var)
                self.frames[i][j].GetYaxis().SetTitle(self.y_var)
                self.frames[i][j].GetXaxis().SetTitleSize(.07)
                self.frames[i][j].GetYaxis().SetTitleSize(.06)
                self.frames[i][j].GetXaxis().CenterTitle(True)
                self.frames[i][j].GetYaxis().CenterTitle(True)
                for f_n in self.file_list:
                    n = min(len(d[f_n][0][i][j]), len(d[f_n][1][i][j]), len(d[f_n][2][i][j]), len(d[f_n][3][i][j]))
                    self.hps[f_n][i].append(TGraphErrors(n, array.array("d", d[f_n][0][i][j]),
                                                         array.array("d", d[f_n][1][i][j]),
                                                         array.array("d", d[f_n][2][i][j]),
                                                         array.array("d", d[f_n][3][i][j])))
                    self.hps[f_n][i][j].SetMarkerColor(self.f_colors[f_n])
                    self.hps[f_n][i][j].SetMarkerStyle(7)
                    self.hps[f_n][i][j].SetFillStyle(0)
                    self.hps[f_n][i][j].SetMaximum(y_max)
                    self.hps[f_n][i][j].SetMinimum(y_min)
                    self.canvas.cd(i + j*(rx_max-rx_min) + 1)
                    self.hps[f_n][i][j].Draw("P")
                #self.canvas.cd(i + j*(rx_max-rx_min) + 1)
                self.padRefresh()

    def padRefresh(self):
        self.canvas.Modified()
        self.canvas.GetFrame().SetBorderSize(12);
        self.canvas.Update()
       
    def tca(self, array):
        n = len(array)
        if (not n == 0):
            t = type(array[0])
            if (t == int):
                ct = ctypes.c_int
            elif (t == float):
                ct = ctypes.c_float
            elif (t == long):
                ct = ctypes.c_long
        C_ARRAY = ct * n
        c_array = C_ARRAY()

        i = 0
        for c in c_array:
            c = ct(array[i])
            i+=1
        return c_array

def printCArray(carray):
    s = "["
    for i in carray:
        s += str(i)
        s += ","
    s = s[:-1]
    s += "]"
    print s
