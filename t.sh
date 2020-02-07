#!/bin/bash
filename='found_hdd.txt'
n=0
while read line; do
# reading each line
n=$((n+1))
done< $filename
echo External HDD Found :$n
