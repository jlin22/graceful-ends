from parse import *

files = ["1-1-1", "2-1-1", "3-1-1", "2-2-1", "4-1-1", "3-2-1", "2-2-2", \
"5-1-1", "4-2-1", "3-3-1", "3-2-2", "6-1-1", "5-2-1", "4-3-1", "4-2-2", "3-3-2"]

for fn in files:
    f = open(fn+'points', 'a')
    temp = open(fn+"temp", 'r')
    data = temp.read()
    data = data.split() 
    for i in range(len(data)):
        data[i] = float(data[i])
    f.write(" "+str(data[0]/data[1]))
    f.close()
