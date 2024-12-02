
Assumptions:

q0 is always the start state

Line 1: a two element list consisting of the Name of machine followed by a number k - where k is the number of tapes in this machin

• Transitions: will have 2 +3k items in its list: – State name
– k characters from Γ that must match the cells under the heads – The new state on a match
– k characters from Γ that are the replacement characters
– k characters from {L, R, S} representing how each head moves


The inputs to your program should include:
• The name of the file describing the machine
• The input string to run
• A ”termination” flag that will stop execution under some circumstance such as if the
depth of the configuration tree exceeds a limit, or the total number of transitions
simulated exceeds some number.
• You may have some other flags which activate some debugging or expanded tracing
option that help you follow what your code is doing.
You may want to design it so that you can enter multiple strings one after another.
