from . import Message

def interpolate_message(message1:Message, message2:Message, value:float):
    data1 = int(message1.data1 + (message2.data1 - message1.data1) * value)
    data2 = int(message1.data2 + (message2.data2 - message1.data2) * value)
    
    return Message(message1.channel, data1, data2, message1.message)

