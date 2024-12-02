#!/usr/bin/env python3
from src.tape import Tape
from src.TuringMachine import TuringMachine
import sys 
import csv


def parse_transition(transition_str: str) -> list:
    
    content = transition_str.strip('[]').split(',')
    content = [item.strip() for item in content]
    
    result = []
    current_sublist = []
    in_sublist = False
    
    for item in content:
        if '[' in item:
            in_sublist = True
            current_sublist = [item.strip('[ ')]
        elif ']' in item:
            current_sublist.append(item.strip(' ]'))
            result.append(current_sublist)
            current_sublist = []
            in_sublist = False
        elif in_sublist:
            current_sublist.append(item)
        else:
            result.append(item)
            
    return result
    

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
               print(f'Machine Name: {machine_name} Number of Tapes: {num_tapes}')
               for i in range(num_tapes):
                   line = f.readline().strip().strip("[]").split(',') #convert to list
                   tapes.append(Tape(line, f"T{i+1}"))
                   index += 1 
            else:
                delta.append(parse_transition(line))
    
    
    
    for tape in tapes:
        print(tape)
        
    for t in delta:
        print(t)
        
    # Create a TuringMachine object and return that. 
    return tapes, delta
               



def main(input_file: str) -> bool:
    
    parse_input(input_file=input_file)
    return True


if __name__=="__main__":
    """ May need to change it to have the user enter the input string from the command line. Maybe not though, seems less efficient."""
    args = sys.argv[1:]
    if len(args) != 2: 
        print("Usage: ./main.py -f input.txt")
    if(args[0] == "-f"):
        main(args[1])
        
    
    