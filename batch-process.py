import os

videos = [
    {
        'title': 'Intro to HTML',
        'input': 'input.mkv',
        'output': '1-introToHTML.mp4'
    },
    {
        'title': 'A HTML Template',
        'input': 'input.mkv',
        'output': '2-HTMLTemplate.mp4'
    },
    {
        'title': 'Lists In HTML',
        'input': 'input.mkv',
        'output': '3-introToHTML.mp4'
    },
]

print("-----------------------------------------")
print("Found " + str(len(videos)) + " videos to convert.")
print("Starting batch process! Hold tight...")
print("-----------------------------------------")


for vid in videos:
    print("Converting " + vid['title'])
    os.system('sh process-video.sh ' + vid['input'] + ' ' + vid['output'] + ' ' + '"' + vid['title'] + '"')