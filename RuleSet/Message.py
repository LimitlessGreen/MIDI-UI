class Message:
    def __init__(self, channel, data1, data2, message):
        self.channel = channel
        self.data1 = data1
        self.data2 = data2
        self.message = message
        
        
    @classmethod
    def from_raw_message(cls, raw_message):
        data2, data1, message_type, channel = cls.extract_midi_values_from_number(raw_message)
        
        return cls(channel, data1, data2, message_type)
    
    @property
    def raw(self):
        midi_values = [self.data2, self.data1, self.message, self.channel]
        number = self.convert_midi_values_to_number(midi_values)
        
        return number
    
    @staticmethod
    def extract_midi_values_from_number(number):
        # Wandele die Dezimalzahl in eine hexadezimale Zeichenkette um
        hex_string = format(number, '08X')  # Hier wird festgelegt, dass 8 Zeichen (32 Bits) genutzt werden sollen

        # Teile die hexadezimale Zeichenkette in Zweiergruppen auf
        hex_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

        # Konvertiere die Zweiergruppen in Dezimalzahlen, einschließlich führender Nullen
        midi_values = [int(pair, 16) for pair in hex_pairs]

        return midi_values

    @staticmethod
    def convert_midi_values_to_number(midi_values):
        # Konvertiere die Dezimalzahlen in hexadezimale Zeichenketten
        hex_pairs = [format(value, '02X') for value in midi_values]

        # Verbinde die hexadezimalen Zeichenketten zu einer Zeichenkette
        hex_string = ''.join(hex_pairs)

        # Wandele die hexadezimale Zeichenkette in eine Dezimalzahl um
        number = int(hex_string, 16)

        return number
    
if __name__ == "__main__":
    message1 = Message(channel=100, data1=2, data2=3, message=4)
    
    print(message1.raw)
    
    message2 = Message.from_raw_message(message1.raw)
    
    print(message2.raw)