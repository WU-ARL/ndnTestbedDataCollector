#!/bin/bash

NFD_PITENTRIES=`nfd-status -v | grep Pit | cut -d'=' -f 2`
echo "$NFD_PITENTRIES"

