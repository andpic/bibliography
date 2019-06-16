#!/bin/bash

make

if [ ! -f biblist.pdf ]; then
   exit -1 
fi
