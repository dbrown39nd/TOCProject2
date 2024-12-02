from src.tape import Tape
from typing import List

class TuringMachine():
    def __init__(self, name: str, tapes: list[Tape], delta: list[list[str]], qstart: str, qaccept: str, qreject: str):
        self.tapes = tapes
        self.delta = delta
        self.qaccept = qaccept
        self.qreject = qreject
        self.current_state = qstart
        self.previous_state = ""
        self.current_transition = ""
        self.iterations = 0
        self.count = 0
        
        self.Q = set()
        for t in delta:
            self.Q.update([t[0], t[2]])
    
    def _check_input(self, transition_input: list[str], tape_input: list[str]) -> bool:
        if len(transition_input) != len(tape_input):
            return False
        
        return all(t1 == "*" or t2 == "*" or t1 == t2 
                  for t1, t2 in zip(transition_input, tape_input))
    
    def execute(self, max_iterations=100) -> str:
        if self.iterations >= max_iterations:
            return "Reject"
            
        inputs = [tape.get_head() for tape in self.tapes]
        
        for transition in self.delta:
            if transition[0] == self.current_state and self._check_input(transition[1], inputs):
                self._take_transition(transition)
                print(self)
                
                if self.current_state == self.qaccept:
                    return "Accept"
                if self.current_state == self.qreject:
                    return "Reject"
                    
                self.iterations += 1
                return self.execute(max_iterations)
        
        self.count += 1
        return "Reject"
    
    def _take_transition(self, transition: list[str]):
        self.current_transition = transition
        self.previous_state = self.current_state
        self.current_state = transition[2]
        self.count += 1
        
        
        # Print state before applying transition
        machine_str = self._format_output(before_transition=True)
        print(machine_str)
        
        # Apply transition
        for index, (new_char, direction) in enumerate(zip(transition[3], transition[4])):
            self.tapes[index].update_tape(new_char)
            self.tapes[index].move_tape(direction)
    
    def _format_output(self, before_transition=False) -> str:
        machine_str = "+" + "-"*38 + f"T{self.count}"+ "-"*38 + "+\n"
        machine_str += f"Start State: {self.previous_state if self.previous_state else self.current_state}\n"
        
        # add tapes with current position
        for tape in self.tapes:
            machine_str += tape.toString() + "\n"
            
        if not before_transition:
            machine_str += "Transition Taken: " + str(self.current_transition) + "\n"
            machine_str += f"Current State: {self.current_state}\n"
            
            if self.current_state == self.qaccept:
                machine_str += "Accept!\n"
            if self.current_state == self.qreject:
                machine_str += "Reject!\n"
                
        machine_str += "+" + "-"*80 + "+"
        return machine_str
    
    def __str__(self):
        return self._format_output()