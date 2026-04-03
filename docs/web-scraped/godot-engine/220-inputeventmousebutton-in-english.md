# InputEventMouseButton in English

# InputEventMouseButton

Inherits:InputEventMouse<InputEventWithModifiers<InputEventFromWindow<InputEvent<Resource<RefCounted<Object
Represents a mouse button being pressed or released.

## Description

Stores information about mouse click events. SeeNode._input().
Note:On Wear OS devices, rotary input is mapped to@GlobalScope.MOUSE_BUTTON_WHEEL_UPand@GlobalScope.MOUSE_BUTTON_WHEEL_DOWN. This can be changed to@GlobalScope.MOUSE_BUTTON_WHEEL_LEFTand@GlobalScope.MOUSE_BUTTON_WHEEL_RIGHTwith theProjectSettings.input_devices/pointing/android/rotary_input_scroll_axissetting.

## Tutorials

- Using InputEvent
Using InputEvent
- Mouse and input coordinates
Mouse and input coordinates

## Properties

| MouseButton | button_index | 0 |
|---|---|---|
| bool | canceled | false |
| bool | double_click | false |
| float | factor | 1.0 |
| bool | pressed | false |

MouseButton
button_index
bool
canceled
false
bool
double_click
false
float
factor
bool
pressed
false

## Property Descriptions

MouseButtonbutton_index=0🔗

- voidset_button_index(value:MouseButton)
voidset_button_index(value:MouseButton)
- MouseButtonget_button_index()
MouseButtonget_button_index()
The mouse button identifier, one of theMouseButtonbutton or button wheel constants.
boolcanceled=false🔗
- voidset_canceled(value:bool)
voidset_canceled(value:bool)
- boolis_canceled()
boolis_canceled()
Iftrue, the mouse button event has been canceled.
booldouble_click=false🔗
- voidset_double_click(value:bool)
voidset_double_click(value:bool)
- boolis_double_click()
boolis_double_click()
Iftrue, the mouse button's state is a double-click.
floatfactor=1.0🔗
- voidset_factor(value:float)
voidset_factor(value:float)
- floatget_factor()
floatget_factor()
The amount (or delta) of the event. When used for high-precision scroll events, this indicates the scroll amount (vertical or horizontal). This is only supported on some platforms; the reported sensitivity varies depending on the platform. May be0if not supported.
boolpressed=false🔗
- voidset_pressed(value:bool)
voidset_pressed(value:bool)
- boolis_pressed()
boolis_pressed()
Iftrue, the mouse button's state is pressed. Iffalse, the mouse button's state is released.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
