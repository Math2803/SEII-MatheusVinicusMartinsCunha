#!/bin/bash

case ${1,,} in
	matheus | administrador)
		echo "Hello Boss"
		;;
	help)
		echo "Just enter your username!"
		;;
	*)
		echo "I dont't know who you are"
esac
