class MidiSlider:
    def __init__(self, name, midi, channel, cc, min, max, step, default, label, unit):
        self.name = name
        self.midi = midi
        self.channel = channel
        self.cc = cc
        self.min = min
        self.max = max
        self.step = step
        self.default = default
        self.label = label
        self.unit = unit