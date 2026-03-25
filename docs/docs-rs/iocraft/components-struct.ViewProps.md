iocraft::components
# Struct ViewProps 
Source 

```
#[non_exhaustive]pub struct ViewProps<'a> {}
```

## Fields (Non-exhaustive)§
§`children: Vec<AnyElement<'a>>`

The elements to render inside of the view.
§`border_style: BorderStyle`

The style of the border. By default, the view will have no border.
§`border_color: Option<Color>`

The color of the border.
§`border_edges: Option<Edges>`

The edges to render the border on. By default, the border will be rendered on all edges.
§`background_color: Option<Color>`

The color of the background.
§`display: Display`

Sets the display mode for the element. Defaults to [`Display::Flex`].

See the MDN documentation for display.
§`width: Size`

Sets the width of the element.
§`height: Size`

Sets the height of the element.
§`min_width: Size`

Sets the minimum width of the element.
§`min_height: Size`

Sets the minimum height of the element.
§`max_width: Size`

Sets the maximum width of the element.
§`max_height: Size`

Sets the maximum height of the element.
§`gap: Gap`

Defines the gaps in between rows or columns of flex items.

See the MDN documentation for gap.
§`column_gap: Gap`

Defines the gaps in between columns of flex items.

See the MDN documentation for column-gap.
§`row_gap: Gap`

Defines the gaps in between rows of flex items.

See the MDN documentation for row-gap.
§`padding: Padding`

Defines the area to reserve around the element’s content, but inside the border.

See the MDN documentation for padding.
§`padding_top: Padding`

Defines the area to reserve above the element’s content, but inside the border.

See the MDN documentation for padding.
§`padding_right: Padding`

Defines the area to reserve to the right of the element’s content, but inside the border.

See the MDN documentation for padding.
§`padding_bottom: Padding`

Defines the area to reserve below the element’s content, but inside the border.

See the MDN documentation for padding.
§`padding_left: Padding`

Defines the area to reserve to the left of the element’s content, but inside the border.

See the MDN documentation for padding.
§`position: Position`

Controls how the element is layed out and whether it will be controlled by the flexbox.
§`inset: Inset`

Sets the position of a positioned element.

See the MDN documentation for inset.
§`top: Inset`

Sets the vertical position of a positioned element.

See the MDN documentation for top.
§`right: Inset`

Sets the horizontal position of a positioned element.

See the MDN documentation for right.
§`bottom: Inset`

Sets the vertical position of a positioned element.

See the MDN documentation for bottom.
§`left: Inset`

Sets the horizontal position of a positioned element.

See the MDN documentation for left.
§`margin: Margin`

Defines the area to reserve around the element’s content, but outside the border.

See the MDN documentation for margin.
§`margin_top: Margin`

Defines the area to reserve above the element’s content, but outside the border.

See the MDN documentation for margin.
§`margin_right: Margin`

Defines the area to reserve to the right of the element’s content, but outside the border.

See the MDN documentation for margin.
§`margin_bottom: Margin`

Defines the area to reserve below the element’s content, but outside the border.

See the MDN documentation for margin.
§`margin_left: Margin`

Defines the area to reserve to the left of the element’s content, but outside the border.

See the MDN documentation for margin.
§`flex_direction: FlexDirection`

Defines how items are placed along the main axis of a flex container.

See the MDN documentation for flex-direction.
§`flex_wrap: FlexWrap`

Defines whether items are forced onto one line or can wrap into multiple lines.

See the MDN documentation for flex-wrap.
§`flex_basis: FlexBasis`

Sets the initial main size of a flex item.

See the MDN documentation for flex-basis.
§`flex_grow: f32`

Sets the flex grow factor, which specifies how much free space should be assigned
to the item’s main size.

See the MDN documentation for flex-grow.
§`flex_shrink: Option<f32>`

Sets the flex shrink factor, which specifies how the item should shrink when the
container doesn’t have enough room for all flex items.

See the MDN documentation for flex-shrink.
§`align_items: Option<AlignItems>`

Controls the alignment of items along the cross axis of a flex container.

See the MDN documentation for align-items.
§`align_content: Option<AlignContent>`

Controls the distribution of space between and around items along a flex container’s cross axis.

See the MDN documentation for align-content.
§`justify_content: Option<JustifyContent>`

Controls the distribution of space between and around items along a flex container’s main axis.

See the MDN documentation for justify-content.
§`overflow: Option<Overflow>`

Defines the behavior when content does not fit within the element’s padding box.

See the MDN documentation for overflow.
§`overflow_x: Option<Overflow>`

Defines the behavior when content does not fit within the element’s padding box in the horizontal direction.

See the MDN documentation for overflow.
§`overflow_y: Option<Overflow>`

Defines the behavior when content does not fit within the element’s padding box in the vertical direction.

See the MDN documentation for overflow.

## Implementations§