import xml.etree.ElementTree as ET

class MidiConverter:
    def __init__(self):
        pass

    def extract_midi_values(self, xml_string):
        # Parse XML
        root = ET.fromstring(xml_string)

        # Erstelle ein leeres Dictionary für die Ergebnisse
        midi_values_dict = {}

        # Iteriere durch alle Regel-Elemente
        for rule in root.findall(".//Rule"):
            name = rule.get("Name")
            slider_message = int(rule.get("SliderMessage"))
            minimum_backtrack = int(rule.get("MinimumBacktrack"))
            maximum_backtrack = int(rule.get("MaximumBacktrack"))

            # Extrahiere MIDI-Werte
            slider_midi_values = self.extract_midi_values_from_number(slider_message)
            min_backtrack_midi_values = self.extract_midi_values_from_number(minimum_backtrack)
            max_backtrack_midi_values = self.extract_midi_values_from_number(maximum_backtrack)

            # Speichere die Ergebnisse im Dictionary
            midi_values_dict[name] = {
                "Slider Message": slider_midi_values,
                "Minimum Backtrack": min_backtrack_midi_values,
                "Maximum Backtrack": max_backtrack_midi_values
            }

        return midi_values_dict

    def extract_midi_values_from_number(self, number):
        # Wandele die Dezimalzahl in eine hexadezimale Zeichenkette um
        hex_string = format(number, '08X')  # Hier wird festgelegt, dass 8 Zeichen (32 Bits) genutzt werden sollen

        # Teile die hexadezimale Zeichenkette in Zweiergruppen auf
        hex_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

        # Konvertiere die Zweiergruppen in Dezimalzahlen, einschließlich führender Nullen
        midi_values = [int(pair, 16) for pair in hex_pairs]

        return midi_values

    def convert_midi_values_to_number(self, midi_values):
        # Konvertiere die Dezimalzahlen in hexadezimale Zeichenketten
        hex_pairs = [format(value, '02X') for value in midi_values]

        # Verbinde die hexadezimalen Zeichenketten zu einer Zeichenkette
        hex_string = ''.join(hex_pairs)

        # Wandele die hexadezimale Zeichenkette in eine Dezimalzahl um
        number = int(hex_string, 16)

        return number

    def convert_midi_values_to_dict(self, midi_values):
        if len(midi_values) < 3:
            raise ValueError("Ungültige Anzahl von MIDI-Werten")

        # Extrahiere Werte
        data2, data1, message_type, channel = midi_values

        # Erstelle ein Dictionary mit den Werten
        midi_dict = {
            "Channel": channel,
            "Data1": data1,
            "Data2": data2,
            "Message": message_type
        }

        return midi_dict

    def convert_dict_to_midi_values(self, midi_dict):
        # Extrahiere Werte
        channel = midi_dict["Channel"]
        data1 = midi_dict["Data1"]
        data2 = midi_dict["Data2"]
        message_type = midi_dict["Message"]

        # Erstelle eine Liste mit den Werten
        midi_values = [data2, data1, message_type, channel]

        return midi_values


# Beispielaufruf mit deinem XML-Beispiel
xml_data = '''
<Root>
    <Rule Name="Fader 2" UseBacktrack="false" SliderMessage="3256321" MinimumBacktrack="3256321" MaximumBacktrack="2133962753">
        <Type>Lumos.GUI.MIDI.SliderRule</Type>
    </Rule>
</Root>
'''

midi_converter = MidiConverter()
midi_values_dict = midi_converter.extract_midi_values(xml_data)

# Gib das erstellte Dictionary aus
print(midi_values_dict)


########

# Beispiel MIDI-Werte
midi_values_example = [0, 49, 176, 1]

# Konvertiere MIDI-Werte zurück zu Dezimalzahl
converted_number = midi_converter.convert_midi_values_to_number(midi_values_example)

# Gib das Ergebnis aus
print("Converted Number:", converted_number)


#######

# Beispiel MIDI-Werte
midi_values_example = [127, 49, 176, 1]

# Konvertiere MIDI-Werte zurück zu einem Dictionary
converted_dict = midi_converter.convert_midi_values_to_dict(midi_values_example)

# Gib das Ergebnis aus
print("Converted Dictionary:", converted_dict)