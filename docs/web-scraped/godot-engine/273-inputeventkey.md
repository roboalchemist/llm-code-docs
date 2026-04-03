# InputEventKey

# InputEventKey
Inherits:InputEventWithModifiers<InputEventFromWindow<InputEvent<Resource<RefCounted<Object
Represents a key on a keyboard being pressed or released.

## Description
An input event for keys on a keyboard. Supports key presses, key releases andechoevents. It can also be received inNode._unhandled_key_input().
Note:Events received from the keyboard usually have all properties set. Event mappings should have only one of thekeycode,physical_keycodeorunicodeset.
When events are compared, properties are checked in the following priority -keycode,physical_keycodeandunicode. Events with the first matching value will be considered equal.

## Tutorials
- Using InputEvent
Using InputEvent

## Properties

| bool | echo | false |
|---|---|---|
| Key | key_label | 0 |
| Key | keycode | 0 |
| KeyLocation | location | 0 |
| Key | physical_keycode | 0 |
| bool | pressed | false |
| int | unicode | 0 |

bool
echo
false
key_label
keycode
KeyLocation
location
physical_keycode
bool
pressed
false
unicode

## Methods

| String | as_text_key_label()const |
|---|---|
| String | as_text_keycode()const |
| String | as_text_location()const |
| String | as_text_physical_keycode()const |
| Key | get_key_label_with_modifiers()const |
| Key | get_keycode_with_modifiers()const |
| Key | get_physical_keycode_with_modifiers()const |

String
as_text_key_label()const
String
as_text_keycode()const
String
as_text_location()const
String
as_text_physical_keycode()const
get_key_label_with_modifiers()const
get_keycode_with_modifiers()const
get_physical_keycode_with_modifiers()const

## Property Descriptions
boolecho=false🔗
- voidset_echo(value:bool)
voidset_echo(value:bool)
- boolis_echo()
boolis_echo()
Iftrue, the key was already pressed before this event. An echo event is a repeated key event sent when the user is holding down the key.
Note:The rate at which echo events are sent is typically around 20 events per second (after holding down the key for roughly half a second). However, the key repeat delay/speed can be changed by the user or disabled entirely in the operating system settings. To ensure your project works correctly on all configurations, do not assume the user has a specific key repeat configuration in your project's behavior.
Keykey_label=0🔗
- voidset_key_label(value:Key)
voidset_key_label(value:Key)
- Keyget_key_label()
Keyget_key_label()
Represents the localized label printed on the key in the current keyboard layout, which corresponds to one of theKeyconstants or any valid Unicode character. Key labels are meant for key prompts.
For keyboard layouts with a single label on the key, it is equivalent tokeycode.
To get a human-readable representation of theInputEventKey, useOS.get_keycode_string(event.key_label)whereeventis theInputEventKey.
```
+-----+ +-----+
| Q   | | Q   | - "Q" - keycode
|   Й | |  ض | - "Й" and "ض" - key_label
+-----+ +-----+
```
Keykeycode=0🔗
- voidset_keycode(value:Key)
voidset_keycode(value:Key)
- Keyget_keycode()
Keyget_keycode()
Latin label printed on the key in the current keyboard layout, which corresponds to one of theKeyconstants. Key codes are meant for shortcuts expressed with a standard Latin keyboard, such asCtrl+Sfor a "Save" shortcut.
To get a human-readable representation of theInputEventKey, useOS.get_keycode_string(event.keycode)whereeventis theInputEventKey.
```
+-----+ +-----+
| Q   | | Q   | - "Q" - keycode
|   Й | |  ض | - "Й" and "ض" - key_label
+-----+ +-----+
```
KeyLocationlocation=0🔗
- voidset_location(value:KeyLocation)
voidset_location(value:KeyLocation)
- KeyLocationget_location()
KeyLocationget_location()
Represents the location of a key which has both left and right versions, such asShiftorAlt.
Keyphysical_keycode=0🔗
- voidset_physical_keycode(value:Key)
voidset_physical_keycode(value:Key)
- Keyget_physical_keycode()
Keyget_physical_keycode()
Represents the physical location of a key on the 101/102-key US QWERTY keyboard, which corresponds to one of theKeyconstants. Physical key codes meant for game input, such as WASD movement, where only the location of the keys is important.
To get a human-readable representation of theInputEventKey, useOS.get_keycode_string()in combination withDisplayServer.keyboard_get_keycode_from_physical()orDisplayServer.keyboard_get_label_from_physical():
```
func _input(event):
    if event is InputEventKey:
        var keycode = DisplayServer.keyboard_get_keycode_from_physical(event.physical_keycode)
        var label = DisplayServer.keyboard_get_label_from_physical(event.physical_keycode)
        print(OS.get_keycode_string(keycode))
        print(OS.get_keycode_string(label))
```
```
public override void _Input(InputEvent @event)
{
    if (@event is InputEventKey inputEventKey)
    {
        var keycode = DisplayServer.KeyboardGetKeycodeFromPhysical(inputEventKey.PhysicalKeycode);
        var label = DisplayServer.KeyboardGetLabelFromPhysical(inputEventKey.PhysicalKeycode);
        GD.Print(OS.GetKeycodeString(keycode));
        GD.Print(OS.GetKeycodeString(label));
    }
}
```
boolpressed=false🔗
- voidset_pressed(value:bool)
voidset_pressed(value:bool)
- boolis_pressed()
boolis_pressed()
Iftrue, the key's state is pressed. Iffalse, the key's state is released.
intunicode=0🔗
- voidset_unicode(value:int)
voidset_unicode(value:int)
- intget_unicode()
intget_unicode()
The key Unicode character code (when relevant), shifted by modifier keys. Unicode character codes for composite characters and complex scripts may not be available unless IME input mode is active. SeeWindow.set_ime_active()for more information. Unicode character codes are meant for text input.
Note:This property is set by the engine only for a pressed event. If the event is sent by an IME or a virtual keyboard, no corresponding key released event is sent.

## Method Descriptions
Stringas_text_key_label()const🔗
Returns aStringrepresentation of the event'skey_labeland modifiers.
Stringas_text_keycode()const🔗
Returns aStringrepresentation of the event'skeycodeand modifiers.
Stringas_text_location()const🔗
Returns aStringrepresentation of the event'slocation. This will be a blank string if the event is not specific to a location.
Stringas_text_physical_keycode()const🔗
Returns aStringrepresentation of the event'sphysical_keycodeand modifiers.
Keyget_key_label_with_modifiers()const🔗
Returns the localized key label combined with modifier keys such asShiftorAlt. See alsoInputEventWithModifiers.
To get a human-readable representation of theInputEventKeywith modifiers, useOS.get_keycode_string(event.get_key_label_with_modifiers())whereeventis theInputEventKey.
Keyget_keycode_with_modifiers()const🔗
Returns the Latin keycode combined with modifier keys such asShiftorAlt. See alsoInputEventWithModifiers.
To get a human-readable representation of theInputEventKeywith modifiers, useOS.get_keycode_string(event.get_keycode_with_modifiers())whereeventis theInputEventKey.
Keyget_physical_keycode_with_modifiers()const🔗
Returns the physical keycode combined with modifier keys such asShiftorAlt. See alsoInputEventWithModifiers.
To get a human-readable representation of theInputEventKeywith modifiers, useOS.get_keycode_string(event.get_physical_keycode_with_modifiers())whereeventis theInputEventKey.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.