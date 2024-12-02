

class Tape:
    def __init__(self, input: list, name: str):
        self.name = name # eg: t1, t2...
        self.input = input
        self.length = len(input)
        self.head = 0 # initialize head to start
        
        self.alphabet = set("*")
        for let in input:
            if let not in self.alphabet:
                self.alphabet.add(let)
        
    
    
    def move_tape(self, dir: str):
        if dir == "L":
            self.head -= 1
        if dir == "R":
            self.head += 1
        if dir == "S":
            self.head == self.head # Do nothing

    
    def __str__(self):
        # First line: the tape contents
        
        tape_str = self.name + ": " + str(self.input) + '\n'
        pointer_offset = len(self.name) + 2 + 1 + (self.head * 5)
        tape_str += ' ' * pointer_offset + ' ^'
        return tape_str
            
    