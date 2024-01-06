from xml.dom import minidom
import xml.etree.ElementTree as ET
import os

class XMLCreator:
    def __init__(self):
        self.rule_sets = []

    def to_xml_element(self):
        midi_settings = ET.Element('MidiSettings')
        
        for rule_set in self.rule_sets:
            midi_settings.append(rule_set.to_xml_element())
            
        return midi_settings
        
        
    def add_rule_set(self, rule_set):
        self.rule_sets.append(rule_set)
    
        
    def to_pretty_xml_string(self):
        midisettings_element = self.to_xml_element()
        xml_string = ET.tostring(midisettings_element, encoding="utf-8").decode("utf-8")
        pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
        return pretty_xml
    
    def save(self, path):
        path = os.path.abspath(path)
        with open(path, 'w') as f:
            f.write(self.to_pretty_xml_string())