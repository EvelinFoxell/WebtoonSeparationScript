# Webtoon Separation Script

This is a little python script that crops an image that is 800px wide and longer 
than 1280px into chunks of 800x1280px or whatever is left in the last image so
that you can upload them to Webtoon.

## Installation

### Requirements
Python3
PIP3
Pillow image library

### Instructions

In the terminal/commandline run the following:

    python WebtoonSeparationScript.py <path to your imaga>

E.g. for a mac with python 2 and 3 installed:

   python3 WebtoonSeparationScript.py chapter1.png

### Output

The scripts creates a folder named `croppedImages_<filename of the image>` which in the example above would be `croppedImages_chapter1`.


## Important notes
* This script only supports png files
* Make sure to not use the only existing copy of your image when cropping. This script does not affect the supplied image, this is just good advice as a precaution.
