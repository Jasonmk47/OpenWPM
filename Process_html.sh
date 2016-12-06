#!/bin/bash
FILES=/home/jason/Desktop/NYT/analysis/saved_sources/*
for f in $FILES
do
	echo "Processing $f:"
	FILENAME=`basename $f .html`
	FILENAME=$(echo "$FILENAME" | sed 's/\.[^.]*$//')
	FILENAME="$FILENAME"""
	python extract_words.py $f > "/home/jason/Desktop/NYT/analysis/sources/$FILENAME""_text.txt"
	grep . "/home/jason/Desktop/NYT/analysis/sources/$FILENAME""_text.txt" > "/home/jason/Desktop/NYT/analysis/sources/$FILENAME"".txt"
	rm "/home/jason/Desktop/NYT/analysis/sources/$FILENAME""_text.txt"

done