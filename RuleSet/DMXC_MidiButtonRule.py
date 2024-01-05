from . import MidiRuleBase
import xml.etree.ElementTree as ET

class MidiButtonRule(MidiRuleBase):
    def __init__(self, name, use_backtrack, threshold, is_toggle, enable_message:int, enabled_backtrack:int,
                 disable_message:int, disabled_backtrack:int):
        self.name = name
        self.use_backtrack = use_backtrack
        self.threshold = threshold
        self.is_toggle = is_toggle
        self.enable_message = enable_message
        self.enabled_backtrack = enabled_backtrack
        self.disable_message = disable_message
        self.disabled_backtrack = disabled_backtrack

    def to_xml_element(self):
        rule_element = ET.Element("Rule", Name=self.name, UseBacktrack=str(self.use_backtrack).lower(),
                                  Threshold=str(self.threshold), IsToggle=str(self.is_toggle).lower(),
                                  EnableMessage=str(self.enable_message), EnabledBacktrack=str(self.enabled_backtrack),
                                  DisableMessage=str(self.disable_message), DisabledBacktrack=str(self.disabled_backtrack))

        type_element = ET.SubElement(rule_element, "Type")
        type_element.text = "Lumos.GUI.MIDI.ButtonRule"

        return rule_element