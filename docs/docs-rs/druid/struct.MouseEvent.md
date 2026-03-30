druid

# Struct MouseEvent

Source

```
pub struct MouseEvent {
    pub pos: Point,
    pub window_pos: Point,
    pub buttons: MouseButtons,
    pub mods: Modifiers,
    pub count: u8,
    pub focus: bool,
    pub button: MouseButton,
    pub wheel_delta: Vec2,
}
```

## Fields§

§`pos: Point`

The position of the mouse in the coordinate space of the receiver.
§`window_pos: Point`

The position of the mouse in the coordinate space of the window.
§`buttons: MouseButtons`

Mouse buttons being held down during a move or after a click event.
Thus it will contain the `button` that triggered a mouse-down event,
and it will not contain the `button` that triggered a mouse-up event.
§`mods: Modifiers`

Keyboard modifiers at the time of the event.
§`count: u8`

The number of mouse clicks associated with this event. This will always
be `0` for a mouse-up and mouse-move events.
§`focus: bool`

Focus is `true` on macOS when the mouse-down event (or its companion mouse-up event)
with `MouseButton::Left` was the event that caused the window to gain focus.

This is primarily used in relation to text selection.
If there is some text selected in some text widget and it receives a click
with `focus` set to `true` then the widget should gain focus (i.e. start blinking a cursor)
but it should not change the text selection. Text selection should only be changed
when the click has `focus` set to `false`.
§`button: MouseButton`

The button that was pressed down in the case of mouse-down,
or the button that was released in the case of mouse-up.
This will always be `MouseButton::None` in the case of mouse-move.
§`wheel_delta: Vec2`

The wheel movement.

The polarity is the amount to be added to the scroll position,
in other words the opposite of the direction the content should
move on scrolling. This polarity is consistent with the
deltaX and deltaY values in a web WheelEvent.

## Trait Implementations§
