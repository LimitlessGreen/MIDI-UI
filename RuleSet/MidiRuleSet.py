from xml.dom import minidom
import xml.etree.ElementTree as ET


class MidiRuleSet:
    def __init__(self, name):
        self.name = name
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def to_xml_element(self):
        ruleset_element = ET.Element("RuleSet", Name=self.name)

        for rule in self.rules:
            ruleset_element.append(rule.to_xml_element())

        return ruleset_element

    def to_pretty_xml_string(self):
        ruleset_element = self.to_xml_element()
        xml_string = ET.tostring(ruleset_element, encoding="utf-8").decode("utf-8")
        pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
        return pretty_xml