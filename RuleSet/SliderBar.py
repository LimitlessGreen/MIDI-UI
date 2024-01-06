from enum import Enum
from .MidiSlider import MidiSlider

class BarOrientations(Enum):
    left_to_right = 0
    right_to_left = 1

class SliderBar:
    def __init__(self, start_address:int, end_address:int, orientation:BarOrientations = BarOrientations.left_to_right):
        self.start_address = start_address
        self.end_address = end_address
        self._total_elements = end_address - start_address + 1
        self._orientation = orientation
        self.sliders = self._create_sliders()
        
    @property
    def total_elements(self):
        return self._total_elements
        
    @property
    def orientation(self):
        return self._orientation
    
    @orientation.setter
    def orientation(self, orientation:BarOrientations):
        '''
        Set the orientation of the vector.
        Not really needed, but it's nice to have for unittests.
        '''
        self._orientation = orientation
        self.sliders = self._create_buttons()
        
    def _create_sliders(self):
        '''
        Create a vector of sliders, where 0 is left.
        But respecting the original given orientation.
        For example: The Function for a grid with left_to_right orientation would be:
        index_1d = column
        '''
        sliders = []
        
        if self.orientation == BarOrientations.left_to_right:
            mapping = lambda column: column
        elif self.orientation == BarOrientations.right_to_left:
            mapping = lambda column: self._total_elements - 1 - column
        else:
            raise ValueError(f"Orientation '{self.orientation}' not found")
        
        for column in range(self._total_elements):
            index_1d = mapping(column)
            address = self.start_address + index_1d
            slider = MidiSlider(control=address, name=f"Fader({column+1})")
            sliders.append(slider)
            
        return sliders
    
    def get_output_rules(self):
        rules = []
        for slider in self.sliders:
            rules += slider.get_output_rules()
        return rules
