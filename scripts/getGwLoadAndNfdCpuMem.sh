#!/bin/bash


#LOAD3=`w | grep "load average" | cut -d ','  -f 4-6 | cut -d ':' -f 2 | cut -d ',' --output-delimiter=' ' -f 1-3`
LOAD3=`w | grep "load average" | awk -F: '{print $NF}' | cut -d ',' --output-delimiter=' ' -f 1-3`
#NFD_PID=`ps aux | grep nfd | grep config | tr -s ' ' | cut -d ' ' -f 2`
#NFD_PID=`ps aux | grep nfd | grep config | tr -s ' ' | cut -d ' ' -f 2`
#PS=`ps -p $NFD_PID -o comm,%cpu,%mem`


NFD_CPU_MEM_PERCENTS=` ps aux | sed -n '/\/usr\/bin\/nfd /s/ \+/ /gp' | cut -d ' ' -f 3,4`
#echo "$PS"
echo "$LOAD3 $NFD_CPU_MEM_PERCENTS"
