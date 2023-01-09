import os

videos = [
    {
        'title': 'HTML Basics',
        'input': 'inputs/HTML_Basics.mp4',
        'output': 'outputs/HTML_Basics.mp4'
    }
]

print("-----------------------------------------")
print("Found " + str(len(videos)) + " videos to convert.")
print("Starting batch process! Hold tight...")
print("-----------------------------------------")


for vid in videos:
    print("Converting " + vid['title'])
    os.system('sh process-video.sh ' + vid['input'] + ' ' + vid['output'] + ' ' + '"' + vid['title'] + '"')