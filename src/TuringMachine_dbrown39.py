from src.tape_dbrown39 import Tape
class TuringMachine():
    """ Turing Machine Class"""
    def __init__(self, name: str, tapes: list[Tape], delta: list[list[str]], qstart: str, qaccept: str, qreject: str, output_file: str):
        self.name = name
        self.tapes = tapes
        self.delta = delta
        self.qaccept = qaccept
        self.qreject = qreject
        self.current_state = qstart
        self.previous_state = ""
        self.current_transition = ""
        self.iterations = 0
        self.count = 0
        self.output_file = output_file

        self.Q = set()
        for t in delta:
            self.Q.update([t[0], t[2]])
    
    def _check_input(self, transition_input: list[str], tape_input: list[str]) -> bool:
        """ Check if the tape input matches the transition"""
        if len(transition_input) != len(tape_input):
            return False
        
        return all((t1 == "*" or 
                    t2 == "*" or 
                    t1 == t2 or 
                    (t1 == "_" and t2 == "_")) 
                for t1, t2 in zip(transition_input, tape_input))
    
    def execute(self, max_iterations=100) -> str:
        """ Recursive execution function, max iterations is a safety net. Executes the Turing Machine """
        if self.iterations == 0:
            with open(self.output_file, "w") as f:
                f.write(f"Machine: {self.name}\n")
                f.write(f"Number of Tapes: {len(self.tapes)}\n")
                f.write(f"Start State: {self.current_state}\n")
                f.write(f"Accept State: {self.qaccept}\n")
                f.write(f"Reject State: {self.qreject}\n")
                f.write("\n")
        
        if self.iterations >= max_iterations:
            return "Reject"
            
        inputs = [tape.get_head() for tape in self.tapes]

        
        for transition in self.delta:
            if transition[0] == self.current_state and self._check_input(transition[1], inputs):
                self._take_transition(transition)
                
                if self.current_state == self.qaccept:
                    return "Accept"
                if self.current_state == self.qreject:
                    return "Reject"
                    
                self.iterations += 1
                return self.execute(max_iterations)
        
        self.count += 1
        return "Reject"
    
    def _take_transition(self, transition: list[str]):
        """ internal method used in execute(), takes a transition and applies it to the tape"""
        self.count += 1
        
        # apply transition
        self.current_transition = transition
        self.previous_state = self.current_state
        self.current_state = transition[2]
        
        # Track if all movements were successful
        movements_successful = True
        
        # Apply the moves and track if they all succeeded
        for index, (new_char, direction) in enumerate(zip(transition[3], transition[4])):
            self.tapes[index].update_tape(new_char)
            if not self.tapes[index].move_tape(direction):
                movements_successful = False
        
        # If we're in qcheck and couldn't move all heads left, we should accept
        # (assuming all symbols matched up to this point)
        if self.current_state == "qcheck" and not movements_successful:
            self.current_state = "qaccept"
    
    def _format_output(self, transition=None) -> str:
        """ Neatly print to output_file current configuration of the Turing Machine """
        machine_str = "+" + "-"*25 + f"T{self.count}" + "-"*25 + "+\n"
        machine_str += f"Current State: {self.current_state}\n"
        
        # Add current tape positions
        for tape in self.tapes:
            machine_str += tape.toString() + "\n"
            
        if transition:
            machine_str += f"Transition: {transition}\n"
            machine_str += f"New State: {transition[2]}\n"
            
        if self.current_state == self.qaccept:
            machine_str += "Accept!\n"
        if self.current_state == self.qreject:
            machine_str += "Reject!\n"

        with open(self.output_file, "a") as f:
            f.write(machine_str + "\n")
            
        return machine_str