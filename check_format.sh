#!/bin/bash

for file in *; do 
	if [[ $file != *.txt ]]
	then 
		echo "$file is not a .txt"
	else 
		if [[ $file == *.txt ]]
		then
			echo "$file is a .txt"
		fi
	fi
done;
