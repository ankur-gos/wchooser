# loader.py
"""
    Load some string stuff
"""

'''
    read one line from the file
'''


def read_line(filename):
    with open(filename, 'r') as f:
        return f.readline()


'''
    read numLines from the file 
    or until EOF reached
'''


def read_lines(filename, num_lines):
    lines = []
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            if counter > num_lines:
                break
            if line == '':
                break
            lines.append(line)
            counter += 1
    return lines

'''
    read numLines from start line
'''


def read_lines_from(filename, num_lines, start):
    lines = []
    scount = 0
    lcount = 0
    with open(filename, 'r') as f:
        for line in f:
            if scount < start:
                scount += 1
                continue
            if lcount > num_lines:
                break
            if line == '':
                break
            lines.append(line)
            lcount += 1
    return lines

