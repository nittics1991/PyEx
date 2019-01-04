#!/bin/bash

for f in $(find . -type f -name *.py) ; do
	
	echo $PWD/${f:2}
	
	python3 -B -m py_compile $PWD/${f:2}
	
	
done

find . -name __pycache__ |xargs rm -R
