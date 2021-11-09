#!/bin/bash
directory="learning_bash_scripting"

# bash check if directory exists
if [ -d $directory ]; then
	echo "Directory exists"
else 
	echo "Directory does not exists"
fi 
