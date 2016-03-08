#!/bin/bash

FACE_IP="128.196.203.36"

FIELDS=`nfd-status -f | grep persistent | grep $FACE_IP | cut -d '=' -f 6,7 | cut -d '{' -f 2,3 | cut -d ' ' -f 1-6`
FIELDS_IN=`echo $FIELDS | cut -d '}' -f 1`
FIELDS_OUT=`echo $FIELDS | cut -d '{' -f 2 | cut -d '}' -f 1`
#echo "FIELDS = $FIELDS"
#echo "FIELDS_IN = $FIELDS_IN"
#echo "FIELDS_OUT = $FIELDS_OUT"

IN_INTERESTS_CNT=`echo $FIELDS_IN | cut -d 'i' -f 1`
#IN_DATA_CNT=`echo $FIELDS | cut -d 'i' -f 2 | cut -d 'd' -f 1 `
IN_DATA_CNT=`echo $FIELDS_IN | cut -d ' ' -f 2 | cut -d 'd' -f 1 `
#IN_BYTES=`echo $FIELDS | cut -d 'i' -f 2 | cut -d 'd' -f 2 | cut -d 'B' -f 1 `
IN_BYTES=`echo $FIELDS_IN | cut -d ' ' -f 3 | cut -d 'B' -f 1 `
IN_BITS=`echo "$IN_BYTES * 8" | bc`
OUT_INTERESTS_CNT=`echo $FIELDS_OUT | cut -d 'i' -f 1`
OUT_DATA_CNT=`echo $FIELDS_OUT | cut -d ' ' -f 2 | cut -d 'd' -f 1 `
OUT_BYTES=`echo $FIELDS_OUT | cut -d ' ' -f 3 | cut -d 'B' -f 1 `
OUT_BITS=`echo "$OUT_BYTES * 8" | bc`

#echo "IN_INTERESTS_CNT = $IN_INTERESTS_CNT"
#echo "IN_DATA_CNT = $IN_DATA_CNT"
#echo "IN_BYTES = $IN_BYTES"
#echo "OUT_INTERESTS_CNT = $OUT_INTERESTS_CNT"
#echo "OUT_DATA_CNT = $OUT_DATA_CNT"
#echo "OUT_BYTES = $OUT_BYTES"
#echo "$IN_INTERESTS_CNT $IN_DATA_CNT $IN_BYTES $OUT_INTERESTS_CNT $OUT_DATA_CNT $OUT_BYTES"
echo "IN_I:$IN_INTERESTS_CNT IN_D:$IN_DATA_CNT IN_B:$IN_BITS OUT_I:$OUT_INTERESTS_CNT OUT_D:$OUT_DATA_CNT OUT_B:$OUT_BITS"

