from . import MidiButton
from enum import Enum

class GridOrientations(Enum):
    bottom_left_to_top_right = 0
    top_left_to_bottom_right = 1
    bottom_right_to_top_left = 2
    top_right_to_bottom_left = 3
    

class ButtonGrid:
    def __init__(self, start_address:int, end_address:int, width:int, colors:dict, orientation:GridOrientations = GridOrientations.bottom_left_to_top_right):
        self.start_address = start_address
        self.end_address = end_address
        self.total_elements = end_address - start_address + 1
        self.width = width
        self.height = self.total_elements // width
        self.colors = colors
        self._orientation = orientation
        self.buttons = self._create_buttons()
        
    @property
    def orientation(self):
        return self._orientation
    
    @orientation.setter
    def orientation(self, orientation:GridOrientations):
        '''
        Set the orientation of the grid.
        Not really needed, but it's nice to have for unittests.
        '''
        self._orientation = orientation
        self.buttons = self._create_buttons()      
        
    def _create_buttons(self):
        '''
        Create a matrix of buttons, where (0,0) is top left.
        But respecting the original given orientation.
        For example: The Function for a grid with bottom_left_to_top_right orientation would be:
        index_1d = (height - 1 - row) * width + column
        '''
        buttons = []
        
        if self.orientation == GridOrientations.bottom_left_to_top_right:
            mapping = lambda row, column: (self.height - 1 - row) * self.width + column
        elif self.orientation == GridOrientations.top_left_to_bottom_right:
            mapping = lambda row, column: row * self.width + column
        elif self.orientation == GridOrientations.bottom_right_to_top_left:
            mapping = lambda row, column: (self.height - 1 - row) * self.width + (self.width - 1 - column)
        elif self.orientation == GridOrientations.top_right_to_bottom_left:
            mapping = lambda row, column: row * self.width + (self.width - 1 - column)
        else:
            raise ValueError(f"Orientation '{self.orientation}' not found")
        
        for row in range(self.height):
            for column in range(self.width):
                index_1d = mapping(row, column)
                address = self.start_address + index_1d
                button = MidiButton(note=address, color=self.colors, name=f"Button {row+1},{column+1}")
                buttons.append(button)
                
        return buttons
                
    @orientation.setter
    def orientation(self, orientation:GridOrientations):
        '''
        Set the orientation of the grid.
        Not really needed, but it's nice to have for unittests.
        '''
        self._orientation = orientation
        self.buttons = self._create_buttons()      
        
    
    def get_button(self, x: int, y: int) -> MidiButton:
        '''
        Get the button at the specified x and y coordinates.
        '''
        index = x + y * self.width
        return self.buttons[index]

    def __getitem__(self, coordinates):
        x, y = coordinates
        return self.get_button(x, y)



