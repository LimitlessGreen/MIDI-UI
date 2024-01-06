from xml.dom import minidom
import xml.etree.ElementTree as ET


class MidiRuleSet:
    def __init__(self, name):
        self.name = name
        self.rules = []

    def add_rule(self, rule):
        if rule is None:
            return
        self.rules.append(rule)
        
    def add_rules(self, rules:list):
        if rules is None:
            return
        self.rules.extend(rules)

    def to_xml_element(self):
        ruleset_element = ET.Element("RuleSet", Name=self.name)

        for rule in self.rules:
            ruleset_element.append(rule.to_xml_element())

        return ruleset_element

