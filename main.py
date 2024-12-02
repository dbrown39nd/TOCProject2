#!/usr/bin/env python3
from src.tape import Tape
from src.TuringMachine import TuringMachine
import sys 
import csv


def parse_transition(transition_str: str) -> list:
    
    transition_str = transition_str[1:-1].strip()
    transition_str = transition_str.replace(' ', '')
    
    output = [] 
    s = ""
    s_list = []
    in_list = False
    skip = False
    for index, char in enumerate(transition_str):
        if skip:
            skip = False
            continue
        if not in_list:
            if char != ",":
                s += char
            if char == ",":
                output.append(s)
                s = "" # reset temp var
                continue
        
        if char == "[":
           in_list = True
           continue
        if char == "]":
           in_list = False
           output.append(s_list)
           s_list = []
           s = ""
           skip = True
           continue
       
        if in_list:
            if char == ",": continue
            s_list.append(char)

        
    
    return output

def parse_input(input_file) -> bool:
    """ 
    Takes in the input file and yields a list of tapes and a list for the transition function. 
    
    """
    
    num_tapes = 0
    machine_name = "" 
    tapes = [] # list of Tape Objects
    delta = [] 
    with open(input_file, "r") as f :
       for index, line in enumerate(f):
            line = line.strip()
            if index == 0: #first line
               line = line.strip("[]").split(',')
               num_tapes = int(line[-1]) # Reset num_tapes
               machine_name=line[0] # Reset Machine Name
               delta = [] # Reset delta
               for i in range(num_tapes):
                   line = f.readline().strip().strip("[]").split(',') #convert to list
                   tapes.append(Tape(line, f"T{i+1}"))
                   index += 1 
            else:

                delta.append(parse_transition(line))
    
    
        
    # Create a TuringMachine object and return that. 
    tm = TuringMachine(name=machine_name, tapes=tapes, delta=delta, qstart="q0", qaccept="qaccept", qreject="qreject")
    
    return tm
               



def main(input_file: str) -> bool:
    
    tm = parse_input(input_file=input_file)
    tm.execute()
    print(tm)
    tm.execute()
    print(tm)
    tm.execute()
    print(tm)
    return True


if __name__=="__main__":
    """ May need to change it to have the user enter the input string from the command line. Maybe not though, seems less efficient."""
    args = sys.argv[1:]
    if len(args) != 2: 
        print("Usage: ./main.py -i input.csv")
    if(args[0] == "-i"):
        main(args[1])
        
    
    