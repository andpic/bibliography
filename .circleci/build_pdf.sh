#!/bin/bash

make

if [ ! -f bibliography.pdf ]; then
   exit -1 
fi
