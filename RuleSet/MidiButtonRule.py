from . import MidiRuleBase, Message
import xml.etree.ElementTree as ET

class MidiButtonRule(MidiRuleBase):
    def __init__(self, name, use_backtrack, threshold, is_toggle, enable_message:Message, enabled_backtrack:Message,
                 disable_message:Message, disabled_backtrack:Message):
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
                                  EnableMessage=str(self.enable_message.raw), EnabledBacktrack=str(self.enabled_backtrack.raw),
                                  DisableMessage=str(self.disable_message.raw), DisabledBacktrack=str(self.disabled_backtrack.raw))

        type_element = ET.SubElement(rule_element, "Type")
        type_element.text = "Lumos.GUI.MIDI.ButtonRule"

        return rule_element