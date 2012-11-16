#!/bin/bash

DT=`date +%Y-%d-%m_%H:%M`
REPORT_FILE="Report_Disk_Utilization_"$DT".txt"

echo "Disk quota for ALCA_MUONALIGN group:" >> $REPORT_FILE
fs lq /afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN >> $REPORT_FILE
