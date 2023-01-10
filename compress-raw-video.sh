#!/bin/sh
# This is a quick ffmpeg helper to quickly convert big
# raw videos into slightly more useful and smaller mp4's. 
# AUTHOR: dan hett (hellodanhett@gmail.com)

inputFile=$1
outputFile=$2

# add the graphics overlay to the main tutorial video and convert it:
echo "Compressing tutorial video..."
ffmpeg -y -i $inputFile $outputFile
