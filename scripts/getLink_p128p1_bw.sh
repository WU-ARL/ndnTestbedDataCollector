#!/bin/bash
TIME=`date +%s.%N`

FIELDS=`ifconfig p128p1 | grep "RX bytes" | cut -d ':' -f 2,3`

RX_BYTES=`echo $FIELDS | cut -d ' ' -f 1`
TX_BYTES=`echo $FIELDS | cut -d ':' -f 2 | cut -d ' ' -f 1`

echo "$TIME $RX_BYTES $TX_BYTES"



