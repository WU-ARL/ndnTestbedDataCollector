#!/bin/bash


PREFIX="/ndn/edu/ucla/remap"
echo "REMAP"
echo "UTC Time 	 PROC_SIZE 	 PIT_ENTRIES 	 NAME_TREE_ENTRIES"
COUNT=0
while (true)
do
  DATE=`date +%s`
  NFD_PROC_SIZE=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getNfdProcSize.sh`
  NFD_PIT_ENTRIES=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getPitEntries.sh`
  NFD_NAME_TREE_ENTRIES=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getNameTreeEntries.sh`
  echo "$DATE 	 $NFD_PROC_SIZE 	 $NFD_PIT_ENTRIES 		 $NFD_NAME_TREE_ENTRIES"

  COUNT=$(($COUNT+1))
  if [ $COUNT -ge 8 ] 
  then
    COUNT=0
    echo "REMAP"
    echo "UTC Time 	 PROC_SIZE 	 PIT_ENTRIES 	 NAME_TREE_ENTRIES"
  fi
sleep 10
done

