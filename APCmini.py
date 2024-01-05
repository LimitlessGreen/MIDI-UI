import os
import sys

from RuleSet import (
    XMLCreator,
    MidiRuleSet,
    MidiButtonRule,
    MidiSliderRule,
    ButtonGrid,
    MidiButton,
    MidiColors,
    Message,
    map_1d_to_2d,
    map_2d_to_1d,
    Orientations
)

from mido import Message as Message
import mido
import time

class APCMatrix:
    pass

class APCmini:
    def __init__(self):
        
        self.board = {
            'grid': {
                'start': 0,
                'end': 63,
                'width': 8,
                'channel': 0,
                'orientation': 'bottom_left_to_top_right',
                'colors': {
                    'off': 0,
                    'green': 1,
                    'green_blink': 2,
                    'red': 3,
                    'red_blink': 4,
                    'yellow': 5,
                    'yellow_blink': 6
                },                
            },
            'slider': {
                'start': 48,
                'end': 56,
                'channel': 0,
            },
            'bar_down': {
                'start': 64,
                'end': 71,
                'channel': 0,
                'colors': {
                    'off': 0,
                    'red': 1,
                    'red_blink': 2,
                },
                'names': ['up', 'down', 'left', 'right', 'volume', 'pan', 'send', 'device']
            },
            'bar_right': {
                'start': 82,
                'end': 87,
                'channel': 0,
                'colors': {
                    'off': 0,
                    'green': 1,
                    'green_blink': 2,
                },
                'names': ['stop', 'play', 'record', 'mute', 'select', 'custom1', 'custom2']
            },
            'shift': 98,
        }
        
        self.grid = None
        self.slider = None
        self.bar_down = None
        self.bar_right = None
        self.shift = None
        self.parse_board()
        

    def parse_board(self):
        '''
        Parse the board dictionary into a usable format.
        '''
        self.grid = ButtonGrid(
            start_address=self.board['grid']['start'],
            end_address=self.board['grid']['end'],
            width=self.board['grid']['width'],
            colors=self.board['grid']['colors'],
            orientation=Orientations[self.board['grid']['orientation']]
        )
        
        self.slider = MidiButton(
            note=self.board['slider']['start'],
            channel=self.board['slider']['channel'],
            name='slider'
        )
        
        self.bar_down = [MidiButton(
            note=self.board['bar_down']['start'] + i,
            channel=self.board['bar_down']['channel'],
            name=self.board['bar_down']['names'][i],
            color=self.board['bar_down']['colors']
        ) for i in range(len(self.board['bar_down']['names']))]
        
        self.bar_right = [MidiButton(
            note=self.board['bar_right']['start'] + i,
            channel=self.board['bar_right']['channel'],
            name=self.board['bar_right']['names'][i],
            color=self.board['bar_right']['colors']
        ) for i in range(len(self.board['bar_right']['names']))]
        
        self.shift = MidiButton(
            note=self.board['shift'],
            channel=0,
            name='shift'
        )
        
    def _get_rule_set(self):
        '''
        Get the rule set for the APCmini.
        '''
        rules_out = MidiRuleSet(name='OUT APCmini')
        rules_in = MidiRuleSet(name='IN APCmini')
        
        # Grid
        for button in self.grid.buttons:
            rules_out.add_rules(button.get_output_rules(is_toggle=False))
            rules_in.add_rule(button.get_input_rule(is_toggle=False))
            
        # Slider
        pass
    
        # Bar down
        for button in self.bar_down:
            rules_out.add_rules(button.get_output_rules(is_toggle=False))
            rules_in.add_rule(button.get_input_rule(is_toggle=False))
            
        # Bar right
        for button in self.bar_right:
            rules_out.add_rules(button.get_output_rules(is_toggle=False))
            rules_in.add_rule(button.get_input_rule(is_toggle=False))
            
        # Shift
        rules_out.add_rules(self.shift.get_output_rules(is_toggle=False))
        
        return rules_out, rules_in
    
    def get_dmxc_config(self):
        '''
        Get the DMXC config for the APCmini.
        '''
        output_rules, input_rules = self._get_rule_set()
        
        xml = XMLCreator()
        xml.add_rule_set(output_rules)
        xml.add_rule_set(input_rules)
        
        return xml
    
    def export_rules(self, path:str):
        '''
        Export the rules to a file.
        '''
        pass
    
    
    
apc_mini = APCmini()
print(apc_mini.get_dmxc_config().to_pretty_xml_string())
        
        
        
            
            
       
        
        