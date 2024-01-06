from . import MidiSliderRule, Message

class MidiSlider:
    def __init__(self, control: int, channel:int = 0, min_value:int=0, max_value:int=127, name:str = None):
        self.control = control
        self.channel = channel
        self.min_value = min_value
        self.max_value = max_value
        self.name = name

    def get_msg_change(self, value):
        return Message('control_change', control=self.control, channel=self.channel, value=value)
    
    @property
    def msg_min(self):
        return Message('control_change', control=self.control, channel=self.channel, value=self.min_value)
    
    @property
    def msg_max(self):
        return Message('control_change', control=self.control, channel=self.channel, value=self.max_value)
        

    def get_input_rule(self):
        rule = MidiSliderRule(name=f"{self.name}", 
                              use_backtrack=False, 
                              slider_message=self.msg_max.raw, 
                              minimum_backtrack=self.msg_min.raw, 
                              maximum_backtrack=self.msg_max.raw)
        return rule

    def __repr__(self):
        return f"MidiSlider(name={self.name}, control_change={self.control}, channel={self.channel}, min_value={self.min_value}, max_value={self.max_value})"