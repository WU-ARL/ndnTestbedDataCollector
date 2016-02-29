#!/bin/bash

export LC_ALL=en_US.utf-8

NFD_VSIZE=`ps alx | sed -n '/\/usr\/bin\/nfd /s/ \+/ /gp' | cut -d ' ' -f 7`
echo "$NFD_VSIZE"
#touch /tmp/nfdvsize.log
#echo "$NFD_VSIZE" >> /tmp/nfdvsize.log
