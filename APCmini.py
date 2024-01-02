import os
import sys
from RuleSet import MidiRuleSet, MidiButtonRule, MidiSliderRule, Message, map_1d_to_2d, map_2d_to_1d

from mido import Message as MidoMessage
import mido
import time
import time

class APCMatrix:
    pass

class APCmini:
    def __init__(self):
        self.slider_start = Message(channel=1, data1=2, data2=0, message=3)
        self.slider_end = Message(channel=1, data1=49, data2=0, message=7)
        self.matrix_start = Message(channel=1, data1=0, data2=0, message=144)
        self.matrix_end = Message(channel=1, data1=0, data2=0, message=128)
        
#with mido.open_input('APC MINI 0') as inport:
#    for message in inport:
#        msg = Message.from_raw_message(3706881)
#        print(f"{message.bytes()} | {msg}")


def print_diagonal_line():
    width = 10  # Width of the line
    height = 5  # Height of the line

    for i in range(height):
        for j in range(width):
            if i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        time.sleep(0.1)  # Delay between each line

print_diagonal_line()




k = 0
colors = [1,3]


def effect1(outport):
    
        
    time.sleep(0.1)

with mido.open_output('APC MINI 1') as outport:
    for _ in range(10000):
            
        effect1(outport)
                
            
            
    
outport.close()