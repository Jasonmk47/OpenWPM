#!/bin/bash
FILES=/home/jason/Desktop/NYT/analysis/sources/*
for f in $FILES
do
	echo "Processing $f:"
	python extract_words.py $f
done