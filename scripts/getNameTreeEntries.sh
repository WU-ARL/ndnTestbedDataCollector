#!/bin/bash

NFD_NAME_TREE_ENTRIES=`nfd-status -v | grep NameTreeEntries | cut -d'=' -f 2`
echo "$NFD_NAME_TREE_ENTRIES"

