#!/bin/bash


DISKUSAGEROOT=`df -h / | grep -v Filesystem| awk '{print $5}' | awk -F% '{print $1}'`
DISKUSAGEBOOT=`df -h /boot | grep -v Filesystem| awk '{print $5}' | awk -F% '{print $1}'`
DISKUSAGE2=`echo "$DISKUSAGEROOT $DISKUSAGEBOOT"`
#LOAD3=`w | grep "load average" | awk -F: '{print $NF}' | cut -d ',' --output-delimiter=' ' -f 1-3`

echo " $DISKUSAGE2 "
