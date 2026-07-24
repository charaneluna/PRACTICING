"""

Write a function that takes the string representing a png file's name and returns an integer as input. The
image is black with some white vertical segmentes, never intersecting. The function has to return the
number of pixels of the longest white segment in the image. An example is the image in image06.png,
for which the function should return the value 33.


"""
import images
def func1(png_file):
    black=(0,0,0)
    white=(255,255,255)
    image=images.load(png_file)


    max_len=0
    for col in range(len(image[0])):
        current_max=0
        for row in range(len(image)):
            if image[row][col]==white:
                current_max+=1
                if current_max>max_len:
                    max_len=current_max
            else:
                current_max=0

    return max_len
            