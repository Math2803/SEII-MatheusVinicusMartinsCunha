#!/bin/bash

MY_LIST=(ONE TWO THREE FOUR)

for item in ${MY_LIST[@]}; do 
	echo -n $item | wc -c; 
	done
