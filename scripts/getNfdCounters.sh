#!/bin/bash

#RESULTS=`nfd-status -v | grep Pit | cut -d'=' -f 2`
RESULTS=`nfd-status -v `
NFD_PITENTRIES=`echo "$RESULTS" | grep Pit | cut -d'=' -f 2`
NFD_NAMETREEENTRIES=`echo "$RESULTS" | grep NameTreeEntries | cut -d'=' -f 2`
NFD_UPTIME=`echo "$RESULTS" | grep uptime | cut -d'=' -f 2`
NFD_FIBENTRIES=`echo "$RESULTS" | grep Fib | cut -d'=' -f 2`
NFD_MEASUREMENTENTRIES=`echo "$RESULTS" | grep Measurements | cut -d'=' -f 2`
echo "pit:$NFD_PITENTRIES nametree:$NFD_NAMETREEENTRIES uptime:$NFD_UPTIME fib:$NFD_FIBENTRIES measurements:$NFD_MEASUREMENTENTRIES"

