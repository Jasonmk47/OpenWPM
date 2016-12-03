#!/bin/bash
FILES=/home/jason/Desktop/NYT/analysis/saved_sources/*
for f in $FILES
do
	echo "Processing $f:"
	FILENAME=`basename $f .html`
	FILENAME=$(echo "$FILENAME" | sed 's/\.[^.]*$//')
	FILENAME="$FILENAME""_text.txt"
	python extract_words.py $f > "/home/jason/Desktop/NYT/analysis/sources/$FILENAME"
	
done