#! /usr/bin/env python

### Driver script for running custom alignment in all DT chambers: 
#   it runs customAlign6DOF.C or customAlign5DOF.C for every chamber.
# 
# The results are stored in a txt format with many columns (1st line is columns header if 1st station)
# and each row contains results for a chamber.
# 
# The command example is
# ./customAlignDT.py ntuple_file.root stationN
# if stationN == 0, runs over all stations.
#
# But, obviously, it would be faster to run 4 jobs for 4 stations at the same time.
###

import os, sys

stationN = int(sys.argv[2])
ntuple_fname = sys.argv[1]

res_fname = "res_st"+str(stationN)+".txt"
if stationN==1 or stationN==0:
  # outupt the column headers in the 1st line (has to be in sync with the columns printed out by the *.C scripts)
  headers = "label wheel station sector db edb dai edai dphizsl2 edphizsl2 k" + \
    " x_100000 ex_100000" + \
    " x_100001 ex_100001 phiz_100001 ephiz_100001" + \
    " x_100011 ex_100011 phiy_100011 ephiy_100011 phiz_100011 ephiz_100011" + \
    " x_100111 ex_100111 phix_100111 ephix_100111 phiy_100111 ephiy_100111 phiz_100111 ephiz_100111" + \
    " x_101000 ex_101000 z_101000 ez_101000" + \
    " y_100000 ey_100000" + \
    " y_010001 ey_010001 phiz_010001 ephiz_010001" + \
    " y_010011 ey_010011 phiy_010011 ephiy_010011 phiz_010011 ephiz_010011" + \
    " y_010111 ey_010111 phix_010111 ephix_010111 phiy_010111 ephiy_010111 phiz_010111 ephiz_010111" + \
    " y_011000 ey_011000 z_011000 ez_011000" + \
    " x_111000 ex_111000 y_111000 ey_111000 z_111000 ez_111000" + \
    " phiy_000010 ephiy_000010" + \
    " phiy_000011 ephiy_000011 phiz_000011 ephiz_000011" + \
    " phix_000111 ephix_000111 phiy_000111 ephiy_000111 phiz_000111 ephiz_000111"
  os.system('echo    "%s" > %s' % (headers, res_fname) )
else:
  # just create the empty results file
  os.system('echo -n "" > %s' % res_fname)

#wheel = -1
#station = 2
#sector = 3

stations_range = [stationN]
if stationN == 0:
  stations_range = range(1,5)

for station in stations_range:
  if station<4:
    for wheel in range(-2,3):
      for sector in range(1,13):
        exit_code = os.system("""root.exe -bq <<EEEND
int wh = %(wheel)d, st = %(station)d, sec = %(sector)d;
TString res_fname = \"%(res_fname)s\";
TString fname = \"%(ntuple_fname)s\";
cout<<"wss "<<wh<<" "<<st<<" "<<sec<<endl;
.x customAlign6DOF.C
.q
EEEND""" % vars() )
        print "root.exe done with code ", exit_code

  if station==4:
    for wheel in range(-2,3):
      for sector in range(1,15):
        exit_code = os.system("""root.exe -bq <<EEEND
int wh = %(wheel)d, st = %(station)d, sec = %(sector)d;
TString res_fname = \"%(res_fname)s\";
TString fname = \"%(ntuple_fname)s\";
cout<<"wss "<<wh<<" "<<st<<" "<<sec<<endl;
.x customAlign5DOF.C
.q
EEEND""" % vars() )
        print "root.exe done with code ", exit_code
