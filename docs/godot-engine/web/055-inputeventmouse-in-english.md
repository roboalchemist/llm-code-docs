# InputEventMouse in English

# InputEventMouse

Inherits:InputEventWithModifiers<InputEventFromWindow<InputEvent<Resource<RefCounted<Object
Inherited By:InputEventMouseButton,InputEventMouseMotion
Base input event type for mouse events.

## Description

Stores general information about mouse events.

## Tutorials

- Using InputEvent
Using InputEvent

## Properties

| BitField[MouseButtonMask] | button_mask | 0 |
|---|---|---|
| Vector2 | global_position | Vector2(0,0) |
| Vector2 | position | Vector2(0,0) |

BitField[MouseButtonMask]
button_mask
Vector2
global_position
Vector2(0,0)
Vector2
position
Vector2(0,0)

## Property Descriptions

BitField[MouseButtonMask]button_mask=0🔗

- voidset_button_mask(value:BitField[MouseButtonMask])
voidset_button_mask(value:BitField[MouseButtonMask])
- BitField[MouseButtonMask]get_button_mask()
BitField[MouseButtonMask]get_button_mask()
The mouse button mask identifier, one of or a bitwise combination of theMouseButtonbutton masks.
Vector2global_position=Vector2(0,0)🔗
- voidset_global_position(value:Vector2)
voidset_global_position(value:Vector2)
- Vector2get_global_position()
Vector2get_global_position()
When received inNode._input()orNode._unhandled_input(), returns the mouse's position in the rootViewportusing the coordinate system of the rootViewport.
When received inControl._gui_input(), returns the mouse's position in theCanvasLayerthat theControlis in using the coordinate system of theCanvasLayer.
Vector2position=Vector2(0,0)🔗
- voidset_position(value:Vector2)
voidset_position(value:Vector2)
- Vector2get_position()
Vector2get_position()
When received inNode._input()orNode._unhandled_input(), returns the mouse's position in theViewportthisNodeis in using the coordinate system of thisViewport.
When received inControl._gui_input(), returns the mouse's position in theControlusing the local coordinate system of theControl.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
