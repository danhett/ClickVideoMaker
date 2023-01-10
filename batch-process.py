import os


videos = [
    {
        'title': 'A HTML Template',
        'input': 'inputs/html/A_HTML_Template.mp4',
        'output': 'outputs/html/A_HTML_Template.mp4'
    },
    {
        'title': 'Checkpoint - HTML Recap',
        'input': 'inputs/html/Checkpoint_HTML_Recap.mp4',
        'output': 'outputs/html/Checkpoint_HTML_Recap.mp4'
    },
    {
        'title': 'Common HTML Problems',
        'input': 'inputs/html/Common_HTML_Problems.mp4',
        'output': 'outputs/html/Common_HTML_Problems.mp4'
    },
    {
        'title': 'Exercise - Your First Page',
        'input': 'inputs/html/Exercise_Your_First_Page.mp4',
        'output': 'outputs/html/Exercise_Your_First_Page.mp4'
    },
    {
        'title': 'External Links in HTML',
        'input': 'inputs/html/External_Links_In_HTML.mp4',
        'output': 'outputs/html/External_Links_In_HTML.mp4'
    },
    {
        'title': 'HTML Basics',
        'input': 'inputs/html/HTML_Basics.mp4',
        'output': 'outputs/html/HTML_Basics.mp4'
    },
    {
        'title': 'HTML Comments',
        'input': 'inputs/html/HTML_Comments.mp4',
        'output': 'outputs/html/HTML_Comments.mp4'
    },
    {
        'title': 'Images in HTML',
        'input': 'inputs/html/Images_In_HTML.mp4',
        'output': 'outputs/html/Images_In_HTML.mp4'
    },
    {
        'title': 'Lists in HTML',
        'input': 'inputs/html/Lists_In_HTML.mp4',
        'output': 'outputs/html/Lists_In_HTML.mp4'
    },
    {
        'title': 'Local links in HTML',
        'input': 'inputs/html/Local_Links_In_HTML.mp4',
        'output': 'outputs/html/Local_Links_In_HTML.mp4'
    },
    {
        'title': 'Text and Headings',
        'input': 'inputs/html/Text_And_Headings_In_HTML.mp4',
        'output': 'outputs/html/Text_And_Headings_In_HTML.mp4'
    },
    {
        'title': 'Where Your Site Lives',
        'input': 'inputs/html/Where_Does_My_Site_Live.mp4',
        'output': 'outputs/html/Where_Does_My_Site_Live.mp4'
    },
    {
        'title': 'Better HTML for Styling',
        'input': 'inputs/css/Better_HTML_For_Styling.mp4',
        'output': 'outputs/css/Better_HTML_For_Styling.mp4'
    },
    {
        'title': 'Borders and Backgrounds',
        'input': 'inputs/css/Borders_And_Backgrounds.mp4',
        'output': 'outputs/css/Borders_And_Backgrounds.mp4'
    },
    {
        'title': 'Changing the Colour',
        'input': 'inputs/css/Changing_The_Colour.mp4',
        'output': 'outputs/css/Changing_The_Colour.mp4'
    },
    {
        'title': 'Changing the Font',
        'input': 'inputs/css/Changing_The_Font.mp4',
        'output': 'outputs/css/Changing_The_Font.mp4'
    },
    {
        'title': 'Common CSS Problems',
        'input': 'inputs/css/Common_CSS_Problems.mp4',
        'output': 'outputs/css/Common_CSS_Problems.mp4'
    },
    {
        'title': 'Margins and Padding',
        'input': 'inputs/css/Margins_And_Padding.mp4',
        'output': 'outputs/css/Margins_And_Padding.mp4'
    },
    {
        'title': 'More about Colour',
        'input': 'inputs/css/More_About_Colour.mp4',
        'output': 'outputs/css/More_About_Colour.mp4'
    },
    {
        'title': 'Styling Whole Websites',
        'input': 'inputs/css/Styling_Whole_Sites.mp4',
        'output': 'outputs/css/Styling_Whole_Sites.mp4'
    },
    {
        'title': 'What CSS Changes',
        'input': 'inputs/css/What_Can_We_Change_With_CSS.mp4',
        'output': 'outputs/css/What_Can_We_Change_With_CSS.mp4'
    }
]


print("-----------------------------------------")
print("Found " + str(len(videos)) + " videos to convert.")
print("Starting batch process! Hold tight...")
print("-----------------------------------------")


for vid in videos:
    print("Converting " + vid['title'])
    
    # convert the full videos into branded assets
    #os.system('sh process-video.sh ' + vid['input'] + ' ' + vid['output'] + ' ' + '"' + vid['title'] + '"')
    
    # quickly crunch the videos down without adding graphics
    os.system('sh compress-raw-video.sh ' + vid['input'] + ' ' + vid['output'])