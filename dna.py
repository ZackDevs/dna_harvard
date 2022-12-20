# https://cs50.harvard.edu/x/2020/psets/6/dna/

from sys import argv
from os.path import exists, join, dirname
from csv import reader
def start():
    # In the prompt they ask for in line files 
    # if len(argv) < 3:
    #   return print("Usage: python3 main.py databases/<something>.csv sequences/<file>.txt")
    # database = argv[1]
    # sequence = argv[2]

    database = input()
    sequence = input()
    
    if not exists(join(dirname(__file__),database)):
        return print("Error: That file doesn't exist.")
    if not database.endswith(".csv"):
        return print("Error: Please provide a .cvs file.")
    s = ""
    with open(join(dirname(__file__),sequence)) as f:
        s = f.read()
    read = ""
    with open(join(dirname(__file__),database)) as f:
        read = list(reader(f))
    datasets = read[0][1:]
    data = []
    for i in datasets:
        strs_counter = 1
        while s.count(i*strs_counter):
            strs_counter+=1
        data += [str(strs_counter-1)]
    x = list(filter(lambda x: x[1:] == data, read))
    print("No match" if not len(x) else x[0][0])
start()