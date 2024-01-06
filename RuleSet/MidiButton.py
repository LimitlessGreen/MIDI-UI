from . import MidiButtonRule, Message

class MidiButton:
    def __init__(self, note: int, channel:int = 0, on_velocity:int=127, off_velocity:int=127, name:str = None, color:dict = None):
        self.note = note
        self.channel = channel
        self.on_velocity = on_velocity
        self.off_velocity = off_velocity
        self.name = name
        self.color = color
        

    @property
    def msg_press(self):
        return Message('note_on', note=self.note, channel=self.channel, velocity=self.on_velocity)
    
    @property
    def msg_release(self):
        return Message('note_off', note=self.note, channel=self.channel, velocity=self.off_velocity)
    
    def msg_color(self, color:str):
        if color not in self.color:
            raise ValueError(f"Color '{color}' not found in {list(self.color.keys())}")
        return Message('note_on', note=self.note, channel=self.channel, velocity=self.color[color])
    
    @property
    def addresses_colors(self):
        return self.color
       
    def get_output_rules(self, is_toggle = False):
        output = []
        
        if self.color is None:
            return None
        
        for color in self.color:
            if color == 'off': continue
            rule = MidiButtonRule(name=f"{self.name}_{color}", 
                                  use_backtrack=True, 
                                  threshold=126, 
                                  is_toggle=is_toggle, 
                                  enable_message=self.msg_color(color).raw, 
                                  enabled_backtrack=self.msg_color(color).raw, 
                                  disable_message=self.msg_color('off').raw, 
                                  disabled_backtrack=self.msg_color('off').raw)
            output.append(rule)
            
        return output
    
    def get_input_rule(self, is_toggle = False):
       
        rule = MidiButtonRule(name=f"{self.name}", 
                                use_backtrack=False, 
                                threshold=126, 
                                is_toggle=is_toggle, 
                                enable_message=self.msg_press.raw, 
                                enabled_backtrack=0, 
                                disable_message=self.msg_release.raw, 
                                disabled_backtrack=0)            
        return rule

    def __repr__(self):
        return f"MidiButton(note={self.note}, channel={self.channel}, on_velocity={self.on_velocity}, off_velocity={self.off_velocity}, name='{self.name}', color={self.color})"