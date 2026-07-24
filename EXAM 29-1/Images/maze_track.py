"""
func7: 15 marks

Define the function func7(file_png_in, file_png_out)
which receives two strings:
- file_png_in: the name of a PNG file to read
- file_png_out: the name of a PNG file to save

The image represents a maze on a black background (0,0,0) with walls as white pixels (255,255,255).

You are given:
- a starting point S, represented by a colored pixel (e.g., red)
- an ending point E, represented by a colored pixel (e.g., green)

Rules:
1. You can move in four directions: up, down, left, right (no diagonals)
2. You cannot move through walls (white pixels)
3. You cannot revisit the same point
4. Your goal is to find the **shortest path** from S to E

Once you find the path:
- Fill it with a new color (e.g., blue `(0,0,255)`)

You can assume:
- There is always at least one valid path
- The maze is small enough to process with standard algorithms
- Walls completely block movement; black pixels are free space

The function does not return anything, but saves the modified image to file_png_out.
"""

import images

def func7(file_png_in, file_png_out):
    image=images.load(file_png_in)
    black=(0,0,0)
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    white=(255,255,255)
    path=[]
    visited=[]
    
    for row in range(len(image)):  #get the start point
        for col in range(len(image[0])):
            if image[row][col]==red:
                S=(row,col)
                path.append(S)
                visited.append(S)

    for row in range(len(image)):    #get the end point
        for col in range(len(image[0])):
            if image[row][col]==green:
                E=(row,col)

    row,col = path.pop()
    while (row,col)!=E:         # follow a path
        if col+1<len(image[0]):
            if image[row][col+1]!=white and (row,col+1) not in visited and image[row][col+1]==black:
                path.append((row,col+1))
                visited.append((row,col+1))

        if row+1<len(image):
            if image[row+1][col]!=white and (row+1,col) not in visited and image[row+1][col]==black:
                path.append((row+1,col))                    
                visited.append((row+1,col))

        if col-1<len(image[0]) and col-1>=0: 
            if image[row][col-1]!=white and (row,col-1) not in visited and image[row][col-1]==black:
                path.append((row,col-1))
                visited.append((row,col-1))

        if row-1>=0 and row-1<len(image):
            if image[row-1][col]!=white and (row-1,col) not in visited and image[row-1][col]==black:
                path.append((row-1,col))
                visited.append((row-1,col))

        row,col = path.pop()

    if image[row][col]==E:      # add the end point to the path 
        path.append(E)
        visited.append(E)
      
    for element in visited[1:len(visited)-1] :       #color the path-start/end points
        row,col=element
        image[row][col]=blue
    
    images.save(image,file_png_out)        # save the image to a file
    

        


