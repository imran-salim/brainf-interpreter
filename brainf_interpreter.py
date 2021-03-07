import sys
import re

# commands
MV_RIGHT = '>'
MV_LEFT = '<'
INC = '+'
DEC = '-'
OUT = '.'
IN = ','
JMP_PAST = '['
JMP_BACK = ']'
CMD_SET = [MV_RIGHT,MV_LEFT,INC,DEC,OUT,IN,JMP_PAST,JMP_BACK]

# line break
#BR = 10

# memory
# each cell is 1 byte
tape = ['_'] * 30000
TAPE_START = 0
TAPE_END = len(tape)-1
head = TAPE_START

# check if tape head is going to move off the tape
#def head_is_moving_off_tape(curr_pos):
#    if curr_pos == TAPE_START: # and '<' occurs, then return TAPE_END
#        return TAPE_END:
#    elif curr_pos == TAPE_END: # and '>' occurs, then return TAPE_START
#        return TAPE_START

def interpret_brainf():
    # check if file is a brainf*** file
    filename = list(sys.argv)[1]
    if (filename == ''):
        sys.exit('brainf programs have the filename extension ".b" or ".bf". Please provide a brainf program.')
    if not (re.search('.+\.b', filename) or re.search('.+\.bf', filename)):
        sys.exit('brainf programs have the filename extension ".b" or ".bf". Please provide a brainf program.')

    program = open(filename)
    cmds = []

    # extract brainf*** commands from the file
    for line in program:
        ln = ''.join(line.split())
        for c in ln:
            if c in CMD_SET:
                cmds.append(c)
                #print(c)
        #print(ln)
    
    program.close()
    return cmds

brainf_code = interpret_brainf()
for cmd in brainf_code:
    print(cmd)
