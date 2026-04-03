# InputEventWithModifiers in English

# InputEventWithModifiers
Inherits:InputEventFromWindow<InputEvent<Resource<RefCounted<Object
Inherited By:InputEventGesture,InputEventKey,InputEventMouse
Abstract base class for input events affected by modifier keys likeShiftandAlt.

## Description
Stores information about mouse, keyboard, and touch gesture input events. This includes information about which modifier keys are pressed, such asShiftorAlt. SeeNode._input().
Note:Modifier keys are considered modifiers only when used in combination with another key. As a result, their corresponding member variables, such asctrl_pressed, will returnfalseif the key is pressed on its own.

## Tutorials
- Using InputEvent
Using InputEvent

## Properties

| bool | alt_pressed | false |
|---|---|---|
| bool | command_or_control_autoremap | false |
| bool | ctrl_pressed | false |
| bool | meta_pressed | false |
| bool | shift_pressed | false |

bool
alt_pressed
false
bool
command_or_control_autoremap
false
bool
ctrl_pressed
false
bool
meta_pressed
false
bool
shift_pressed
false

## Methods

| BitField[KeyModifierMask] | get_modifiers_mask()const |
|---|---|
| bool | is_command_or_control_pressed()const |

BitField[KeyModifierMask]
get_modifiers_mask()const
bool
is_command_or_control_pressed()const

## Property Descriptions
boolalt_pressed=false🔗
- voidset_alt_pressed(value:bool)
voidset_alt_pressed(value:bool)
- boolis_alt_pressed()
boolis_alt_pressed()
State of theAltmodifier.
boolcommand_or_control_autoremap=false🔗
- voidset_command_or_control_autoremap(value:bool)
voidset_command_or_control_autoremap(value:bool)
- boolis_command_or_control_autoremap()
boolis_command_or_control_autoremap()
Automatically useMeta(Cmd) on macOS andCtrlon other platforms. Iftrue,ctrl_pressedandmeta_pressedcannot be set.
boolctrl_pressed=false🔗
- voidset_ctrl_pressed(value:bool)
voidset_ctrl_pressed(value:bool)
- boolis_ctrl_pressed()
boolis_ctrl_pressed()
State of theCtrlmodifier.
boolmeta_pressed=false🔗
- voidset_meta_pressed(value:bool)
voidset_meta_pressed(value:bool)
- boolis_meta_pressed()
boolis_meta_pressed()
State of theMetamodifier. On Windows and Linux, this represents the Windows key (sometimes called "meta" or "super" on Linux). On macOS, this represents the Command key.
boolshift_pressed=false🔗
- voidset_shift_pressed(value:bool)
voidset_shift_pressed(value:bool)
- boolis_shift_pressed()
boolis_shift_pressed()
State of theShiftmodifier.

## Method Descriptions
BitField[KeyModifierMask]get_modifiers_mask()const🔗
Returns the keycode combination of modifier keys.
boolis_command_or_control_pressed()const🔗
On macOS, returnstrueifMeta(Cmd) is pressed.
On other platforms, returnstrueifCtrlis pressed.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.