"""
func4: 12 marks

Define the function func4(file_png_in)
which receives a string as argument, representing the name of a PNG file.
The image contains flowers and candles on a black background.

A flower is made up of 9 identical pixels arranged as follows (C = color, . = black):

.C.C.
..C..
CCCCC
..C..
.C.C.

A candle is made up of 6 identical pixels arranged as follows:

..C..
..C..
..C..
..C..
.CCC.

The function returns a pair with the number of flowers and candles
found in the image of the input file, as a tuple FLOWERS, CANDLES.
"""


import images

def func4(file_png_in):
    image=images.load(file_png_in)
    black=(0,0,0)
    flowers=0
    candles=0

    for row in range(len(image)):
        for col in range(len(image[0])):
            if image[row][col]!=black:
                c = image[row][col]
                if 0<=row-2<len(image) and row+2<len(image) and col+4<len(image[0]):    #flowers count
                    if image[row][col]== image[row][col+1]== image[row][col+2]== image[row][col+3]== image[row][col+4]== image[row-2][col+1]== image[row-2][col+3]== image[row-1][col+2] ==image[row+1][col+2]== image[row+2][col+1]== image[row+2][col+3]== c:
                        flowers+=1
                if row+4<len(image) and 0<=col-1<len(image[0]) and col+1<len(image[0]): #candles count
                    if image[row][col] == image[row+1][col] == image[row+2][col] == image[row+3][col] == image[row+4][col] == image[row+4][col-1] == image[row+4][col+1] == c:
                        candles+=1
    return (flowers,candles)