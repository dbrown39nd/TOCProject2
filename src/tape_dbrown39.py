

class Tape:
    def __init__(self, input: list, name: str):
        self.name = name # eg: T1, T2...
        self.input = input
        self.length = len(input)
        self.head = 0 # initialize head to start

        self.alphabet = set("*")
        for let in input:
            if let not in self.alphabet:
                self.alphabet.add(let)

    def update_tape(self, char):
        self.input[self.head] = char
        
    def get_head(self):
        return self.input[self.head]
    
    def move_tape(self, dir: str):
        if dir == "L":
            if self.head > 0:
                self.head -= 1
                return True
            # Don't move the head if it's already at the leftmost position
            return False
        if dir == "R":
            self.head += 1
            if self.head >= self.length:
                self.input.append("_")
                self.length += 1
            return True
        if dir == "S":
            return True
        return False
            

    
    def toString(self):
        # First line: the tape contents
        
        tape_str = self.name + ": " + str(self.input) + '\n'
        pointer_offset = len(self.name) + 2 + 1 + (self.head * 5)
        tape_str += ' ' * pointer_offset + ' ^'
        return tape_str
            
    