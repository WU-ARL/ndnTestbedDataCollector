#!/bin/bash
DATE=`date`

#MemTotal:        2048076 kB
#MemFree:          234396 kB

MEMINFO=`grep "MemTotal\|MemFree" /proc/meminfo`
CPUINFO=`grep "processor\|model name" /proc/cpuinfo`

MEMTOTAL=`grep MemTotal /proc/meminfo | awk '{ print $2 };' `
MEMFREE=`grep MemFree /proc/meminfo | awk '{ print $2 };' `

#echo ""
#echo "$DATE"
#echo ""
#echo "$CPUINFO"
echo "$MEMTOTAL $MEMFREE" 
