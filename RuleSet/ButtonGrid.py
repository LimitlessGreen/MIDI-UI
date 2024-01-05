from . import MidiButton
from enum import Enum

class Orientations(Enum):
    bottom_left_to_top_right = 0
    top_left_to_bottom_right = 1
    bottom_right_to_top_left = 2
    top_right_to_bottom_left = 3
    

class ButtonGrid:
    def __init__(self, start_address:int, end_address:int, width:int, colors:dict, orientation:Orientations = Orientations.bottom_left_to_top_right):
        self.start_address = start_address
        self.end_address = end_address
        self.width = width
        self.height = (end_address - start_address) // width
        self.colors = colors
        self.orientation = orientation
        self.buttons = self._create_buttons()
        
    def _create_buttons(self):
        '''
        Create a matrix of buttons, where (0,0) is top left.
        But respecting the original given orientation.
        '''
        buttons = []
        
        if self.orientation == Orientations.bottom_left_to_top_right:
            for y in range(self.height):
                for x in range(self.width):
                    buttons.append(MidiButton(note=self.start_address + x + (y * self.width), color=self.colors, name=f"B({x},{y})"))
        elif self.orientation == Orientations.top_left_to_bottom_right:
            for y in reversed(range(self.height)):
                for x in range(self.width):
                    buttons.append(MidiButton(note=self.start_address + x + (y * self.width), color=self.colors, name=f"B({x},{y})"))
        elif self.orientation == Orientations.bottom_right_to_top_left:
            for y in range(self.height):
                for x in reversed(range(self.width)):
                    buttons.append(MidiButton(note=self.start_address + x + (y * self.width), color=self.colors, name=f"B({x},{y})"))
        elif self.orientation == Orientations.top_right_to_bottom_left:
            for y in reversed(range(self.height)):
                for x in reversed(range(self.width)):
                    buttons.append(MidiButton(note=self.start_address + x + (y * self.width), color=self.colors, name=f"B({x},{y})"))
        else:
            raise ValueError(f"Orientation '{self.orientation}' not implemented")
            
        return buttons
    
    def get_button(self, x: int, y: int) -> MidiButton:
        '''
        Get the button at the specified x and y coordinates.
        '''
        index = x + y * self.width
        return self.buttons[index]

    def __getitem__(self, coordinates):
        x, y = coordinates
        return self.get_button(x, y)



