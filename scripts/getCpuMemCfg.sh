#!/bin/bash
DATE=`date`

MEMINFO=`grep "MemTotal\|MemFree" /proc/meminfo`
CPUINFO=`grep "processor\|model name" /proc/cpuinfo`

echo ""
echo "$DATE"
echo ""
echo "$CPUINFO"
echo "$MEMINFO"
