#!/usr/bin/env python3
from src.tape_dbrown39 import Tape
from src.TuringMachine_dbrown39 import TuringMachine
import os 
import csv
import json

#GLOBALS:
PASS_COUNT = 0
FAIL_COUNT = 0


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

def parse_input(input_file: str, output_file: str) -> bool:
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
    tm = TuringMachine(name=machine_name, tapes=tapes, delta=delta, qstart="q0", qaccept="qaccept", qreject="qreject", output_file=output_file)
    return tm
               



def main(input_file: str) -> bool:
    global PASS_COUNT
    global FAIL_COUNT
    
    test_num = input_file.split('/')[-1].split('.')[0].split('_')[0]
    tm = parse_input(input_file=input_file, output_file=f"output/{test_num}_dbrown39.txt")
    result = tm.execute(max_iterations=100)
    with open("check_dbrown39.json", "r") as f:
        check = json.load(f)
    
    # check the result to verify if it's correct 
    if result.lower() == check[test_num]:
        print(f"{test_num} passed!")
        PASS_COUNT += 1
    else:
        print(f"{test_num} failed")
        FAIL_COUNT += 1
    
    


if __name__=="__main__":
    
    INPUT_PATH = "input"

    for file in sorted(os.listdir(INPUT_PATH)): #run in order
        if file.endswith(".csv"):
            print("="*2 + f"{file}" + "="*2)
            main(input_file=f"{INPUT_PATH}/{file}")
            print()
    
    if FAIL_COUNT == 0:
        print(f"{PASS_COUNT}/{PASS_COUNT} tests passed!")
    else:
        print(f"{FAIL_COUNT}/{FAIL_COUNT + PASS_COUNT} tests failed.")