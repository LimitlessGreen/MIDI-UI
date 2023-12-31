from . import MidiRuleBase, Message
import xml.etree.ElementTree as ET

class MidiSliderRule(MidiRuleBase):
    def __init__(self, name, use_backtrack, slider_message:Message, minimum_backtrack:Message, maximum_backtrack:Message):
        self.name = name
        self.use_backtrack = use_backtrack
        self.slider_message = slider_message
        self.minimum_backtrack = minimum_backtrack
        self.maximum_backtrack = maximum_backtrack

    def to_xml_element(self):
        rule_element = ET.Element("Rule", Name=self.name, UseBacktrack=str(self.use_backtrack).lower(),
                                  SliderMessage=str(self.slider_message.raw), MinimumBacktrack=str(self.minimum_backtrack.raw),
                                  MaximumBacktrack=str(self.maximum_backtrack.raw))

        type_element = ET.SubElement(rule_element, "Type")
        type_element.text = "Lumos.GUI.MIDI.SliderRule"

        return rule_element