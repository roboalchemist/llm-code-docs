druid

# Struct ViewContext

Source

```
pub struct ViewContext {
    pub window_origin: Point,
    pub last_mouse_position: Option<Point>,
    pub clip: Rect,
}
```

## Fields§

§`window_origin: Point`

The origin of this widget relative to the window.

This is written from the perspective of the Widget and not the Pod.
For the Pod this is its parent’s window origin.
§`last_mouse_position: Option<Point>`

The last position the cursor was at, relative to the widget.
§`clip: Rect`

The visible area, this widget is contained in, relative to the widget.

The area may be larger than the widget’s `paint_rect`.

## Trait Implementations§
