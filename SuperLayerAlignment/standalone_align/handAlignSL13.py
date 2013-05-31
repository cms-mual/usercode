#! /usr/bin/env python

import os,sys

#ffxml = "initialMuonAlignment_DT-Aug11_CSC-Aug12.xml"

#f = open("res_st1234f.txt", "rb")
#f = open("res_st1234_dumpfidgt.txt", "rb")
#f = open("res_st1234_dumpfidgttn.txt", "rb")

#sfx = ".sl13"
#sfx = ".sl13xphiz"


#ffxml = "initialMuonAlignment_DT-Aug11_CSC-Aug12.xml"
#f = open("res_st1234_dumpfidgttn.txt", "rb")
#sfx = ".sl13xphiz"

ffxml = "initialMuonAlignment_DT-Aug11_CSC-Aug12.sl13xphiz.xml"
f = open("res_st1234_dumpfidgttn_c1.txt","rb")
sfx = ".sl13xphiz2"

do_sl2 = False


labels = [item for item in f.readline().strip().split() if item]

# dictionary of data with column names as keys and columns are stored as lists 
dd = {}

for line in f:
  line = line.strip()
  if line:
    lineList = [item for item in line.split() if item]
    for i, item in enumerate(lineList):
      dd.setdefault(labels[i], []).append(item)

f.close()

xml_str = """
"""

# avg distances between SL13 in four stations
Ds = [23.68,  23.61, 23.60, 23.66]
# SL1&3 distances from the center of chamber
D1s = [11.75 ,11.75, 9.95, 9.95]
D3s = [11.94, 11.86, 13.65, 13.74]

print "dphiz SL13:"

for i in range(len(dd['wheel'])):
  wheel   = dd['wheel'][i]
  station = dd['station'][i]
  sector  = dd['sector'][i]

  idx = int(station)-1
  db = float(dd['db'][i])*Ds[idx]/23.5
  cor_sl1 =-db * D1s[idx]/Ds[idx]/1000.
  cor_sl3 = db * D3s[idx]/Ds[idx]/1000.
  
  #dphiz2 = float(dd['dphizsl2'][i])
  dphiz2 = float(dd['phiz_010111'][i]) - float(dd['phiz_100011'][i])
  cor_sl2 = - dphiz2/1000.
  
  print wheel, station, sector, cor_sl1, cor_sl3
  xml_str += """<operation>
  <DTSuperLayer wheel=\"%(wheel)s\" station=\"%(station)s\" sector=\"%(sector)s\" superlayer="1" />
  <rotatelocal axisx="0." axisy="0." axisz="1." angle="%(cor_sl1).10f" />
</operation>

<operation>
  <DTSuperLayer wheel=\"%(wheel)s\" station=\"%(station)s\" sector=\"%(sector)s\" superlayer="3" />
  <rotatelocal axisx="0." axisy="0." axisz="1." angle="%(cor_sl3).10f" />
</operation>

""" % vars()

  if do_sl2 and station != "4":
    xml_str += """<operation>
  <DTSuperLayer wheel=\"%(wheel)s\" station=\"%(station)s\" sector=\"%(sector)s\" superlayer="2" />
  <rotatelocal axisx="0." axisy="0." axisz="1." angle="%(cor_sl2).10f" />
</operation>

""" % vars()


print "dx SL13:"

for i in range(len(dd['wheel'])):
  wheel   = dd['wheel'][i]
  station = dd['station'][i]
  sector  = dd['sector'][i]

  er = float(dd['edai'][i])
  if er>0.5:
    print "not aligning dx13 in Wh%s St%s Sec%s as error = %f > 0.5mm" % (wheel, station, sector, er)
    continue

  idx = int(station)-1
  dai = float(dd['dai'][i])*Ds[idx]/23.5
  cor_sl1 = dai * D1s[idx]/Ds[idx]/10.
  cor_sl3 =-dai * D3s[idx]/Ds[idx]/10.
  
  print wheel, station, sector, float(dd['dai'][i]), cor_sl1, cor_sl3
  xml_str += """<operation>
  <DTSuperLayer wheel=\"%(wheel)s\" station=\"%(station)s\" sector=\"%(sector)s\" superlayer="1" />
  <movelocal x="%(cor_sl1).8f" y="0." z="0." />
</operation>

<operation>
  <DTSuperLayer wheel=\"%(wheel)s\" station=\"%(station)s\" sector=\"%(sector)s\" superlayer="3" />
  <movelocal x="%(cor_sl3).8f" y="0." z="0." />
</operation>

""" % vars()


#print xml_str

xml_str += "</MuonAlignment>"


ff = open(ffxml+sfx,mode="w")
print >>ff, xml_str
ff.close()

os.system('grep -v "</MuonAlignment>" %s > %s' % (ffxml, ffxml+".tmp"))
os.system('cat %s %s > %s' % (ffxml+".tmp", ffxml+sfx, ffxml+sfx+".xml") )
os.system('rm %s %s' % (ffxml+".tmp", ffxml+sfx) )
