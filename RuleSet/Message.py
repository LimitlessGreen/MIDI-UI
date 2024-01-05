from mido import Message as MidoMessage


class Message(MidoMessage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    @classmethod

    def from_raw_message(cls, raw_message):

        data2, data1, message_type, channel = cls.extract_midi_values_from_number(raw_message)
        

        return cls.from_bytes([message_type, data1, data2])
    

    @classmethod

    def from_dmxc_message(cls, channel, data1, data2, message):

        return cls.from_bytes([message, data1, data2])
    

    @property

    def raw(self):

        # data2, data1, message_type, channel

        midi_values = [self.data2, self.data1, self.message, self.dmxc_channel]

        number = self.convert_midi_values_to_number(midi_values)
        

        return number
    

    @property

    def data1(self):

        return self.bytes()[1]
    

    @property

    def data2(self):

        return self.bytes()[2]
    

    @property

    def message(self):

        return self.bytes()[0]
    

    @property

    def dmxc_channel(self):

        '''DMX Control uses Channels beginning with 1, not 0'''

        return self.channel + 1
    

    #@property

    #def mido(self):

    #    return MidoMessage.from_bytes([self.message, self.data1, self.data2])
    

    #def __repr__(self):

    #    return f"Message(channel={self.channel}, data1={self.data1}, data2={self.data2}, message={self.message})"
    

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

    messages =[

        Message.from_raw_message(84381697),

        Message.from_raw_message(84381697),

        Message.from_raw_message(495617),   

    ]
    

    for message in messages:    

        print(f"{message.raw} | {message}")