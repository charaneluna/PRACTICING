"""
Write a function that takes the string representing a png file's name and returns an integer as input.
The image is a black image with some white segments that join vertically and horizontally but never
intersect. The function has to return the number of pixels of the longest white segment in the image.
Examples are the images in image07.png image08.png for which the function should return the values
115 and 148, respectively.

"""

import images

def func1(png_file):
    image=images.load(png_file)
    black=(0,0,0)
    white=(255,255,255)

    