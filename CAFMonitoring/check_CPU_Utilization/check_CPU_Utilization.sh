#!/bin/bash

SCRIPT_PATH="/afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/CAFMonitoring/UserCode/MuonAlignment/CAFMonitoring/check_CPU_Utilization"
SCRIPT_NAME="script.py"

DIR=`pwd`
DT=`date +%Y-%d-%m_%H:%M`
NEWDIR="Report_CPU_Utilization_"$DT
mkdir $NEWDIR
cd $NEWDIR

cp $SCRIPT_PATH/$SCRIPT_NAME ./
python $SCRIPT_NAME --group CMSALCA

rm -rf error*.txt

cd $DIR
