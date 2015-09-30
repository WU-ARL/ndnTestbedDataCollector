#!/bin/bash
DATE=`date`
TIME=`date +%s.%N`
LOAD=`w | head -1`
#TOP=`top -n 1 | grep "PID\|nfd" | grep -v nfdstat`
#TOP=`top -n 1 | grep "nfd" | grep -v nfdstat`
PS=`ps alx | grep "PID\|nfd" | grep "PID\|config" | grep -v grep`
#echo "PID   USER PR NI VIRT  RES SHR S  %CPU  %MEM  TIME+   COMMAND"
echo ""
echo "$DATE"
echo "TIME $TIME"
echo ""
#echo "$TOP"
echo '> ps alx | grep "PID\|nfd" | grep "PID\|config" | grep -v grep'
echo ""
echo "$PS"
echo ""
echo "> w | head -1"
echo "$LOAD"

MEMINFO=`grep "MemTotal\|MemFree" /proc/meminfo`
CPUINFO=`grep "processor\|model name" /proc/cpuinfo`

echo ""
echo "$CPUINFO"
echo "$MEMINFO"

nfd-status -v
