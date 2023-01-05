#!/bin/sh
# This is a quick ffmpeg helper to assemble a finished video from a raw input.
# You will need the right images and fonts, these should be supplied with this
# script. You'll also need ffmpeg installed on your system. Set for 1080p.
# AUTHOR: dan hett (hellodanhett@gmail.com)

lessonTitle=$1

# create the title screen video from the graphic:
echo "Creating title screen..."
ffmpeg -loglevel error -loop 1 -i base.png -c:v libx264 -t 9 -pix_fmt yuv420p -vf scale=1920:1080 titleBase.mp4

# next, add some dynamic text to the video to show the title:
echo "Adding lesson title..."
ffmpeg -loglevel error -i titleBase.mp4 -vf 'drawtext=fontfile=Arial.ttf:text='"$lessonTitle"':fontcolor=black:fontsize=96:box=1:boxcolor=black@0.05:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2' -codec:a copy titleNoMusic.mp4

# add the music
echo "Adding music..."
ffmpeg -loglevel error -i titleNoMusic.mp4 -i jingle.mp3 -map 0:v -map 1:a -c:v copy -shortest title.mp4

# add the graphics overlay to the main tutorial video and convert it:
echo "Converting tutorial video..."
ffmpeg -loglevel error -y -i input.mkv -i overlay.png -filter_complex [0]overlay=x=0:y=0[out] -map [out] -map 0:a? tutorial.mp4

# put the two videos together:
echo "Merging videos..."
ffmpeg -loglevel error -i title.mp4 -i tutorial.mp4 \
-filter_complex "[0:v:0] [0:a:0] [1:v:0] [1:a:0] concat=n=2:v=1:a=1 [v] [a]" \
-map "[v]" -map "[a]" -vsync 2 -y DONE.mp4

# clean up the mess
echo "Cleaning up..."
rm title.mp4
rm titleBase.mp4
rm titleNoMusic.mp4
rm tutorial.mp4

echo "Done!"