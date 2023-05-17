#!/bin/bash

cd images/

ls -a > ../lser.txt

i = 0

while read p; do echo "Moving $p to $((i++)).jpg";mv $p "$((i++)).jpg";done < ../lser.txt
