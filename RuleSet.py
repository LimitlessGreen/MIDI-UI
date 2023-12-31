import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from RuleSet import MidiRuleBase, Message, MidiRuleSet, MidiButtonRule, MidiSliderRule
from rich import print








if __name__ == "__main__":
    # Erstelle ein Regelset
    ruleset = MidiRuleSet("Test")

    # Erstelle eine Regel
    slider_rule = MidiSliderRule(name="Fader 2", use_backtrack=False, 
                                 slider_message=Message(channel=1, data1=2, data2=0, message=3),
                                 minimum_backtrack=Message(channel=1, data1=49, data2=0, message=176), 
                                 maximum_backtrack=Message(channel=1, data1=49, data2=0, message=7))
    
    button_rule = MidiButtonRule(name="Button 1", use_backtrack=False, threshold=0, is_toggle=False,
                                 enable_message=Message(channel=1, data1=2, data2=0, message=3),
                                 enabled_backtrack=Message(channel=1, data1=49, data2=0, message=176),
                                 disable_message=Message(channel=1, data1=49, data2=0, message=7),
                                 disabled_backtrack=Message(channel=1, data1=49, data2=0, message=7))

    # Füge die Regel zum Regelset hinzu
    ruleset.add_rule(slider_rule)
    ruleset.add_rule(button_rule)

    # Gib das Regelset als XML-String aus
    print(ruleset.to_pretty_xml_string())
