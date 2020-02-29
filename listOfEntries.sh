#!/bin/bash

# listOfNewEntries.sh - Retrieve the keys for the new entries in the
# bibliography.

echo "$(git --no-pager diff ./bibliography.bib | \
    grep '^+@' | \
    sed -e 's/^.*{//g' | \
    sort | \
    tr '\n' ' ')"