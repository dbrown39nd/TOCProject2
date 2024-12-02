from src.tape import Tape
from typing import List


class TuringMachine():
    
    
    def __init__(self, name: str, tapes: list[Tape], delta: list[list[str]], qstart: str, qaccept: str, qreject: str):
        
        self.tapes = tapes
        self.delta = delta # Transition function of format [q0, [0, 1], q1, [a,b], [R,R]]
        self.qaccept = qaccept
        self.qreject = qreject
        self.current_state = qstart
        
        # Loop through delta and determine Q.
        self.Q = set()
        for t in delta:
            if t[0] not in self.Q:
                self.Q.add(t[0])
            if t[2] not in self.Q:
                self.Q.add(t[2])
                
   
    
    
    def execute(self):
        current_state = self.current_state
        transitions = self.delta # Going to need to iterate through transitions to find the transition we need to take. 
        
       
        inputs = []
        for tape in self.tapes:
            inputs.append(tape.get_head())
        
        for transition in transitions: 

            if transition[0] == current_state and transition[1] == inputs:
                self._take_transition(transition)
        
        # read head from each tape. 


        
    def _take_transition(self, transition: list[str]):
        print(transition)
        self.current_state = transition[2] # update current state
        #update each tape
        for index, new_char in enumerate(transition[3]):
            self.tapes[index].update_tape(new_char)
            self.tapes[index].move_tape(transition[4][index])
            
        
        
    def __str__(self):
        

        machine_str = f"Current State: {self.current_state}\n"
        for tape in self.tapes:
            machine_str += tape.toString()
            machine_str += "\n"
        return machine_str
            
    
    
    
    
    