# InputEventMIDI

# InputEventMIDI
Inherits:InputEvent<Resource<RefCounted<Object
Represents a MIDI message from a MIDI device, such as a musical keyboard.

## Description
InputEventMIDI stores information about messages fromMIDI(Musical Instrument Digital Interface) devices. These may include musical keyboards, synthesizers, and drum machines.
MIDI messages can be received over a 5-pin MIDI connector or over USB. If your device supports both be sure to check the settings in the device to see which output it is using.
By default, Godot does not detect MIDI devices. You need to callOS.open_midi_inputs(), first. You can check which devices are detected withOS.get_connected_midi_inputs(), and close the connection withOS.close_midi_inputs().
```
func _ready():
    OS.open_midi_inputs()
    print(OS.get_connected_midi_inputs())

func _input(input_event):
    if input_event is InputEventMIDI:
        _print_midi_info(input_event)

func _print_midi_info(midi_event):
    print(midi_event)
    print("Channel ", midi_event.channel)
    print("Message ", midi_event.message)
    print("Pitch ", midi_event.pitch)
    print("Velocity ", midi_event.velocity)
    print("Instrument ", midi_event.instrument)
    print("Pressure ", midi_event.pressure)
    print("Controller number: ", midi_event.controller_number)
    print("Controller value: ", midi_event.controller_value)
```
```
public override void _Ready()
{
    OS.OpenMidiInputs();
    GD.Print(OS.GetConnectedMidiInputs());
}

public override void _Input(InputEvent inputEvent)
{
    if (inputEvent is InputEventMidi midiEvent)
    {
        PrintMIDIInfo(midiEvent);
    }
}

private void PrintMIDIInfo(InputEventMidi midiEvent)
{
    GD.Print(midiEvent);
    GD.Print($"Channel {midiEvent.Channel}");
    GD.Print($"Message {midiEvent.Message}");
    GD.Print($"Pitch {midiEvent.Pitch}");
    GD.Print($"Velocity {midiEvent.Velocity}");
    GD.Print($"Instrument {midiEvent.Instrument}");
    GD.Print($"Pressure {midiEvent.Pressure}");
    GD.Print($"Controller number: {midiEvent.ControllerNumber}");
    GD.Print($"Controller value: {midiEvent.ControllerValue}");
}
```
Note:Godot does not support MIDI output, so there is no way to emit MIDI messages from Godot. Only MIDI input is supported.
Note:On the Web platform, using MIDI input requires a browser permission to be granted first. This permission request is performed when callingOS.open_midi_inputs(). MIDI input will not work until the user accepts the permission request.

## Tutorials
- MIDI Message Status Byte List
MIDI Message Status Byte List
- Wikipedia General MIDI Instrument List
Wikipedia General MIDI Instrument List
- Wikipedia Piano Key Frequencies List
Wikipedia Piano Key Frequencies List

## Properties

| int | channel | 0 |
|---|---|---|
| int | controller_number | 0 |
| int | controller_value | 0 |
| int | instrument | 0 |
| MIDIMessage | message | 0 |
| int | pitch | 0 |
| int | pressure | 0 |
| int | velocity | 0 |

channel
controller_number
controller_value
instrument
MIDIMessage
message
pitch
pressure
velocity

## Property Descriptions
intchannel=0🔗
- voidset_channel(value:int)
voidset_channel(value:int)
- intget_channel()
intget_channel()
The MIDI channel of this message, ranging from0to15. MIDI channel9is reserved for percussion instruments.
intcontroller_number=0🔗
- voidset_controller_number(value:int)
voidset_controller_number(value:int)
- intget_controller_number()
intget_controller_number()
The unique number of the controller, ifmessageis@GlobalScope.MIDI_MESSAGE_CONTROL_CHANGE, otherwise this is0. This value can be used to identify sliders for volume, balance, and panning, as well as switches and pedals on the MIDI device. See theGeneral MIDI specificationfor a small list.
intcontroller_value=0🔗
- voidset_controller_value(value:int)
voidset_controller_value(value:int)
- intget_controller_value()
intget_controller_value()
The value applied to the controller. Ifmessageis@GlobalScope.MIDI_MESSAGE_CONTROL_CHANGE, this value ranges from0to127, otherwise it is0. See alsocontroller_value.
intinstrument=0🔗
- voidset_instrument(value:int)
voidset_instrument(value:int)
- intget_instrument()
intget_instrument()
The instrument (also calledprogramorpreset) used on this MIDI message. This value ranges from0to127.
To see what each value means, refer to theGeneral MIDI's instrument list. Keep in mind that the list is off by 1 because it does not begin from 0. A value of0corresponds to the acoustic grand piano.
MIDIMessagemessage=0🔗
- voidset_message(value:MIDIMessage)
voidset_message(value:MIDIMessage)
- MIDIMessageget_message()
MIDIMessageget_message()
Represents the type of MIDI message (see theMIDIMessageenum).
For more information, see theMIDI message status byte list chart.
intpitch=0🔗
- voidset_pitch(value:int)
voidset_pitch(value:int)
- intget_pitch()
intget_pitch()
The pitch index number of this MIDI message. This value ranges from0to127.
On a piano, themiddle Cis60, followed by aC-sharp(61), then aD(62), and so on. Each octave is split in offsets of 12. See the "MIDI note number" column of thepiano key frequency charta full list.
intpressure=0🔗
- voidset_pressure(value:int)
voidset_pressure(value:int)
- intget_pressure()
intget_pressure()
The strength of the key being pressed. This value ranges from0to127.
Note:For many devices, this value is always0. Other devices such as musical keyboards may simulate pressure by changing thevelocity, instead.
intvelocity=0🔗
- voidset_velocity(value:int)
voidset_velocity(value:int)
- intget_velocity()
intget_velocity()
The velocity of the MIDI message. This value ranges from0to127. For a musical keyboard, this corresponds to how quickly the key was pressed, and is rarely above110in practice.
Note:Some MIDI devices may send a@GlobalScope.MIDI_MESSAGE_NOTE_ONmessage with0velocity and expect it to be treated the same as a@GlobalScope.MIDI_MESSAGE_NOTE_OFFmessage. If necessary, this can be handled with a few lines of code:
```
func _input(event):
    if event is InputEventMIDI:
        if event.message == MIDI_MESSAGE_NOTE_ON and event.velocity > 0:
            print("Note pressed!")
```

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.