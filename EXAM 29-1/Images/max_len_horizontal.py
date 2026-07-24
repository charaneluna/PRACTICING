"""
Write a function that takes as input the string representing name of a png file and returns an integer.
The image is black with some white horizontal segments that never intersect. The function has to return
the number of pixels of the longest white segment in the image. An example is the image in image02.png,
for which the function should return the value 33.

"""

import images

def func1(png_file):
    image=images.load(png_file)
    white=(255,255,255)

    max_len=0

    for row in range(len(image)):
        current=0
        for col in range(len(image[0])):
            if image[row][col]==white:
                current+=1
                if current>max_len:
                    max_len=current
            else:
                current=0

    return max_len
                