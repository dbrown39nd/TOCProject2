from src.tape import Tape
from typing import List


class TuringMachine():
    
    
    def __init__(self, tapes: List[Tape], delta: List[List[str]], qstart: str, qaccept: str, qreject: str):
        
        self.tapes = tapes
        self.delta = delta # Transition function of format [q0, [0, 1], q1, [a,b], [R,R]]
        self.qaccept = qaccept
        self.qreject = qreject
        self.current_state = qstart
        pass
    
    
    
    
    
    def __str__(self):
        
        print(self.current_state)
        to_string = ""
        for tape in self.tapes:
            print(tape)
            
    
    
    
    
    