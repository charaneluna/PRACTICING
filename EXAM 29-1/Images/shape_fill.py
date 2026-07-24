"""
func6: 12 marks

Define the function func6(file_png_in, file_png_out)
which receives two strings as arguments:
- file_png_in: the name of a PNG file to read
- file_png_out: the name of a PNG file to save

The image contains a black background (0,0,0) and several hollow diamonds.

A hollow diamond is made up of 5 rows of pixels, with the pattern (C = color, . = black):

..C..
.C.C.
C...C
.C.C.
..C..

The function should:
1. Scan the image for all hollow diamonds
2. Fill the **inside black pixels** of each diamond with its color C to make it solid
3. Save the modified image in the file file_png_out

You can assume that diamonds:
- Do not overlap
- Are separated by at least 1 black pixel
- Are all the same size
"""

import images

def func6(file_png_in,file_png_out):
    black=(0,0,0)
    image = images.load(file_png_in)


    for row in range(len(image)):
        for col in range(len(image[0])):
            if image[row][col]!=black:
                c = image[row][col]
                if row+2<len(image) and row-2>=0 and row-2<len(image) and col+4<len(image[0]):
                    if image[row][col] == image[row-1][col+1] == image[row-2][col+2] == image[row-1][col+3] == image[row][col+4] == image[row+1][col+1] == image[row+2][col+2] == image[row+1][col+3] == c:
                        image[row][col+1] = c
                        image[row][col+2] = c
                        image[row][col+3] = c
                        image[row-1][col+2] = c
                        image[row+1][col+2] = c

    images.save(image,file_png_out)

