import abc


class MidiRuleBase(abc.ABC):
    @abc.abstractmethod
    def to_xml_element(self):
        pass
