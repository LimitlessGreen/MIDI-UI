from . import MidiRuleBase
import xml.etree.ElementTree as ET

class MidiSliderRule(MidiRuleBase):
    def __init__(self, name, use_backtrack, slider_message:int, minimum_backtrack:int, maximum_backtrack:int):
        self.name = name
        self.use_backtrack = use_backtrack
        self.slider_message = slider_message
        self.minimum_backtrack = minimum_backtrack
        self.maximum_backtrack = maximum_backtrack

    def to_xml_element(self):
        rule_element = ET.Element("Rule", Name=self.name, UseBacktrack=str(self.use_backtrack).lower(),
                                  SliderMessage=str(self.slider_message), MinimumBacktrack=str(self.minimum_backtrack),
                                  MaximumBacktrack=str(self.maximum_backtrack))

        type_element = ET.SubElement(rule_element, "Type")
        type_element.text = "Lumos.GUI.MIDI.SliderRule"

        return rule_element