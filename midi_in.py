import mido
from mido import Message



with mido.open_input('APC MINI 0', virtual=False) as inport:
    for message in inport:
        print(f"{message} | {message.bytes()}")