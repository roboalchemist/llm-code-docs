# InputEventFromWindow

# InputEventFromWindow
Inherits:InputEvent<Resource<RefCounted<Object
Inherited By:InputEventScreenDrag,InputEventScreenTouch,InputEventWithModifiers
Abstract base class forViewport-based input events.

## Description
InputEventFromWindow represents events specifically received by windows. This includes mouse events, keyboard events in focused windows or touch screen actions.

## Properties

| int | window_id | 0 |

window_id

## Property Descriptions
intwindow_id=0🔗
- voidset_window_id(value:int)
voidset_window_id(value:int)
- intget_window_id()
intget_window_id()
The ID of aWindowthat received this event.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.