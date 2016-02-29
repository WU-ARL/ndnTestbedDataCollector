#!/bin/bash

if [ $# -eq 2 ]
then
  NODENAME=$1
  PREFIX=$2
else
  echo "Usage:   $0 nodename prefix"
  echo "Example: $0 WU /ndn/edu/wustl"
  exit 0
fi
CPU_TYPE=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getCpuMemCfg.sh  | grep -m 1 model | cut -d ':' -f 2`
NUM_CPUS=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getCpuMemCfg.sh  | grep "processor" | wc -l`
TOT_MEM=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getMemUsage.sh | cut -d ' ' -f 1`

#echo "$NODENAME"
NAME_AND_SPEC=`echo "$NODENAME:  $NUM_CPUS cpus of type $CPU_TYPE ;  total mem $TOT_MEM "`


echo ""
echo "$NAME_AND_SPEC"
echo "        	  SYSTEM 	    NFD   	    NFD      	      NFD          "
echo "UTC Time 	 FREE_MEM 	 PROC_SIZE 	 PIT_ENTRIES 	 NAME_TREE_ENTRIES "
COUNT=0
while (true)
do
  DATE=`date +%s`
  FREE_MEM=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getMemUsage.sh | cut -d ' ' -f 2`
  NFD_PROC_SIZE=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getNfdProcSize.sh`
  NFD_PIT_ENTRIES=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getPitEntries.sh`
  NFD_NAME_TREE_ENTRIES=`/home/jdd/WU-ARL/ndn-ops/NOC/nfdDataCollection/build/nfdDataCollectorCmd -i $PREFIX -y getNameTreeEntries.sh`
  echo "$DATE 	 $FREE_MEM 	 $NFD_PROC_SIZE 	 $NFD_PIT_ENTRIES 		 $NFD_NAME_TREE_ENTRIES"

  COUNT=$(($COUNT+1))
  if [ $COUNT -ge 8 ] 
  then
    COUNT=0
    echo ""
    echo "$NAME_AND_SPEC"
    echo "        	  SYSTEM 	    NFD   	    NFD      	      NFD          "
    echo "UTC Time 	 FREE_MEM 	 PROC_SIZE 	 PIT_ENTRIES 	 NAME_TREE_ENTRIES "
    #echo "UTC Time 	 PROC_SIZE 	 PIT_ENTRIES 	 NAME_TREE_ENTRIES"
  fi
sleep 10
done

