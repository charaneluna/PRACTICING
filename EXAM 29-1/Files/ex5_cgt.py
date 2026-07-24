"""
funcY: 6 marks

Define the function 
    funcY(input_filename, output_filename)
which receives the following arguments:
- input_filename: the path to a text file containing a sequence of integers,
    one integer per line
- output_filename: the path to a file in which you must write a sequence of integers
The function must read the integers from the input file and group them into
consecutive blocks of strictly increasing values.
For each block, write in the output file a single integer equal to:
- the length of the block multiplied by the maximum value in the block
The values must be written in the order in which the blocks appear in the input file.
The function must also return the sum of all the integers that start a new block.

Example: the file funcY/in_1.txt contains the sequence
    3
    5
    7
    2
    4
    1
    2
    3
The function must write in the output file
    21
    8
    9

write the values in the output file and return 6.

"""

def func6(input_filename, output_filename):
    block_max,block_size,block_start=seq_operator(input_filename)
    with open(output_filename,'w') as fout:
        for i in range(len(block_max)):
            fout.write(str(block_max[i]*block_size[i])+'\n')
    return sum(block_start)

def seq_reader(input_filename):
    with open(input_filename,'r') as fin:
        seq=[]

        for line in fin:
            number=int(line.strip())
            seq.append(number)
    return seq

def seq_operator(input_filename):
    seq=seq_reader(input_filename)
    block=[]
    block_start=[]
    block_size=[]
    block_max=[]

    block.append(seq[0])
    for nbr in seq[1:]:
        if nbr>block[-1]:
            block.append(nbr)
        elif nbr<=block[-1]:
            block_start.append(block[0])
            block_size.append(len(block))
            block_max.append(block[-1])
            block=[nbr]              
    block_start.append(block[0])
    block_size.append(len(block))
    block_max.append(block[-1])

    return block_max,block_size,block_start
