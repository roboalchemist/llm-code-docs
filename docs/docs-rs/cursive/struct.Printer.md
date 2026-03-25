cursive
# Struct Printer 
Source 

```
pub struct Printer<'a, 'b> {
    pub offset: XY<usize>,
    pub output_size: XY<usize>,
    pub size: XY<usize>,
    pub content_offset: XY<usize>,
    pub focused: bool,
    pub enabled: bool,
    pub theme: &'a Theme,
    /* private fields */
}
```

## Fields§
§`offset: XY<usize>`

Offset into the window this printer should start drawing at.

A print request at `x` will really print at `x + offset`.
§`output_size: XY<usize>`

Size of the area we are allowed to draw on.

Anything outside of this should be discarded.

The view being drawn can ignore this, but anything further than that
will be ignored.
§`size: XY<usize>`

Size allocated to the view.

This should be the same value as the one given in the last call to
`View::layout`.
§`content_offset: XY<usize>`

Offset into the view for this printer.

The view being drawn can ignore this, but anything to the top-left of
this will actually be ignored, so it can be used to skip this part.

A print request `x`, will really print at `x - content_offset`.
§`focused: bool`

Whether the view to draw is currently focused or not.
§`enabled: bool`

Whether the view to draw is currently enabled or not.
§`theme: &'a Theme`

Currently used theme

## Implementations§