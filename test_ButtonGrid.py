import unittest
from RuleSet import ButtonGrid, GridOrientations

class TestButtonGrid(unittest.TestCase):
    def setUp(self):
        # Define test parameters
        start_address = 0
        end_address = 63
        width = 8
        colors = {'red': 1, 'green': 2, 'blue': 3}
        orientation = GridOrientations.bottom_left_to_top_right
        
        # Create a ButtonGrid instance for testing
        self.button_grid = ButtonGrid(start_address, end_address, width, colors, orientation)
    
    def test_create_buttons(self):
        # Check if the number of buttons is correct
        self.assertEqual(len(self.button_grid.buttons), 64)
        
        # Check if the buttons are created with the correct addresses and names
        self.assertEqual(self.button_grid.buttons[0].note, 56)
        self.assertEqual(self.button_grid.buttons[0].name, "B(1,1)")
        self.assertEqual(self.button_grid.buttons[63].note, 7)
        self.assertEqual(self.button_grid.buttons[63].name, "B(8,8)")
        
    def test_get_button(self):
        # Check if the get_button method returns the correct button
        button = self.button_grid.get_button(0, 0)
        self.assertEqual(button.note, 56)
        self.assertEqual(button.name, "B(1,1)")
        
        button = self.button_grid.get_button(7, 7)
        self.assertEqual(button.note, 7)
        self.assertEqual(button.name, "B(8,8)")
        
    def test_getitem(self):
        # Check if the __getitem__ method returns the correct button
        button = self.button_grid[0, 0]
        self.assertEqual(button.note, 56)
        self.assertEqual(button.name, "B(1,1)")
        
        button = self.button_grid[7, 7]
        self.assertEqual(button.note, 7)
        self.assertEqual(button.name, "B(8,8)")
        
    def test_orientation_bottom_left_to_top_right(self):
        # Set the orientation to bottom_left_to_top_right
        self.button_grid.orientation = GridOrientations.bottom_left_to_top_right
        
        # Check if the get_button method returns the correct button for each coordinate
        button = self.button_grid.get_button(0, 0)
        self.assertEqual(button.note, 56)
        self.assertEqual(button.name, "B(1,1)")
        
        button = self.button_grid.get_button(7, 7)
        self.assertEqual(button.note, 7)
        self.assertEqual(button.name, "B(8,8)")
        
    def test_orientation_top_left_to_bottom_right(self):
        # Set the orientation to top_left_to_bottom_right
        self.button_grid.orientation = GridOrientations.top_left_to_bottom_right
        
        # Check if the get_button method returns the correct button for each coordinate
        button = self.button_grid.get_button(0, 0)
        self.assertEqual(button.note, 0)
        self.assertEqual(button.name, "B(1,1)")
        
        button = self.button_grid.get_button(7, 7)
        self.assertEqual(button.note, 63)
        self.assertEqual(button.name, "B(8,8)")
        
    def test_orientation_bottom_right_to_top_left(self):
        # Set the orientation to bottom_right_to_top_left
        self.button_grid.orientation = GridOrientations.bottom_right_to_top_left
        
        # Check if the get_button method returns the correct button for each coordinate
        button = self.button_grid.get_button(0, 0)
        self.assertEqual(button.note, 63)
        self.assertEqual(button.name, "B(1,1)")
        
        button = self.button_grid.get_button(7, 7)
        self.assertEqual(button.note, 0)
        self.assertEqual(button.name, "B(8,8)")
        
    def test_orientation_top_right_to_bottom_left(self):
        # Set the orientation to top_right_to_bottom_left
        self.button_grid.orientation = GridOrientations.top_right_to_bottom_left
        
        # Check if the get_button method returns the correct button for each coordinate
        button = self.button_grid.get_button(0, 0)
        self.assertEqual(button.note, 7)
        self.assertEqual(button.name, "B(1,1)")
        
        button = self.button_grid.get_button(7, 7)
        self.assertEqual(button.note, 56)
        self.assertEqual(button.name, "B(8,8)")

if __name__ == '__main__':
    unittest.main()