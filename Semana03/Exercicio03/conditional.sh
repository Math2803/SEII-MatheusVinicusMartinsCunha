#!/bin/bash

if [ ${1,,} = matheus ]; then
	echo "Welcome Boss"
elif [ ${1,,} = help ]; then
	echo "Just enter your username"
else
	echo "I don't know who you are."
fi
