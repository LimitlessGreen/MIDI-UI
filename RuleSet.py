import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from RuleSet import MidiRuleBase, Message, MidiRuleSet, MidiButtonRule, MidiSliderRule, XMLCreator
from rich import print








if __name__ == "__main__":
    # Erstellen eines XML-Elements
    midi_settings = XMLCreator()
    
    # Erstelle ein Regelset
    ruleset = MidiRuleSet("Test")
    
    # Füge das Regelset zum XML-Element hinzu
    midi_settings.add_rule_set(ruleset)

    # Erstelle eine Regel
    slider_rule = MidiSliderRule(name="Fader 2", use_backtrack=False, 
                                 slider_message=Message.from_dmxc_message(channel=1, data1=2, data2=0, message=176),
                                 minimum_backtrack=Message.from_dmxc_message(channel=1, data1=49, data2=0, message=176), 
                                 maximum_backtrack=Message.from_dmxc_message(channel=1, data1=49, data2=0, message=176))
    
    button_rule = MidiButtonRule(name="Button 1", use_backtrack=False, threshold=0, is_toggle=False,
                                 enable_message=Message.from_dmxc_message(channel=1, data1=2, data2=0, message=176),
                                 enabled_backtrack=Message.from_dmxc_message(channel=1, data1=49, data2=0, message=176),
                                 disable_message=Message.from_dmxc_message(channel=1, data1=49, data2=0, message=176),
                                 disabled_backtrack=Message.from_dmxc_message(channel=1, data1=49, data2=0, message=176))

    # Füge die Regel zum Regelset hinzu
    ruleset.add_rule(slider_rule)
    ruleset.add_rule(button_rule)

    # Gib das Regelset als XML-String aus
    print(midi_settings.to_pretty_xml_string())
