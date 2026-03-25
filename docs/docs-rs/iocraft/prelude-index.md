iocraft
# Module prelude 
Source 
## Re-exports§
`pub use crate::components::*;``pub use crate::hooks::*;`
## Macros§
elementUsed to declare an element and its properties.
## Structs§
AnyElementA type-erased element that can be created from any `Element`.Canvas`Canvas` is the medium that output is drawn to before being rendered to the terminal or other
destinations.CanvasSubviewMutRepresents a writeable region of a `Canvas`. All coordinates provided to functions of this
type are relative to the region’s top-left corner.CanvasTextStyleDescribes the style of text to be rendered via a `Canvas`.ComponentDrawerProvides information and operations that low level component implementations may need to
utilize during the draw phase.ComponentUpdaterProvides information and operations that low level component implementations may need to
utilize during the update phase.EdgesDefines the edges of an element, e.g. for border styling.ElementAn element is a description of an uninstantiated component, including its key and properties.ElementKeyUsed to identify an element within the scope of its parent. This is used to minimize the number
of times components are destroyed and recreated from render-to-render.FullscreenMouseEventAn event fired when the mouse is moved, clicked, scrolled, etc. in fullscreen mode.HandlerImmutable event handler, which lacks ability to mutate captured variables, but can be cloned.HandlerMut`HandlerMut` is a type representing an optional event handler, commonly used for component properties.HooksA collection of hooks attached to a component.KeyEventAn event fired when a key is pressed.KeyEventStateRepresents extra state about the key event.KeyModifiersRepresents key modifiers (shift, control, alt, etc.).MockTerminalConfigUsed to provide the configuration for a mock terminal which can be used for testing.PercentDefines a type that represents a percentage [0.0-100.0] and is convertible to any of the
libary’s other percent types. As a shorthand, you can express this in the
`element!` macro using the `pct` suffix, e.g. `50pct`.RenderLoopFutureA future that renders an element in a loop, allowing it to be dynamic and interactive.SystemContextThe system context, which is always available to all components.TerminalEventsA stream of terminal events.
## Enums§
AlignContentSets the distribution of space between and around content items
For Flexbox it controls alignment in the cross axis
For Grid it controls alignment in the block axisAlignItemsUsed to control how child nodes are aligned.
For Flexbox it controls alignment in the cross axis
For Grid it controls alignment in the block axisColorRepresents a color.ContextA context that can be passed to components.DisplaySets the layout used for the children of this nodeFlexBasisSets the initial main size of a flex item.FlexDirectionThe direction of the flexbox layout main axis.FlexWrapControls whether flex items are forced onto one line or can wrap onto multiple lines.GapDefines the gaps in between rows or columns of flex items.InsetSets the position of a positioned element.KeyCodeRepresents a key.KeyEventKindRepresents a keyboard event kind.MarginDefines the area to reserve around the element’s content, but outside the border.MouseEventKindA mouse event kind.OverflowHow children overflowing their container should affect layoutPaddingDefines the area to reserve around the element’s content, but inside the border.PositionThe positioning strategy for this item.SizeDefines a width or height of an element.TerminalEventAn event fired by the terminal.WeightA weight which can be applied to text.
## Traits§
Component`Component` defines a component type and the methods required for instantiating and rendering
the component.ElementExtA trait implemented by all element types, providing methods for common operations on them.ElementTypeA trait implemented by all element types to define the properties that can be passed to them.HookA hook is a way to add behavior to a component. Hooks are called at various points in the
update and draw cycle.PropsThis trait makes a struct available for use as component properties.
## Type Aliases§
JustifyContentSets the distribution of space between and around content items
For Flexbox it controls alignment in the main axis
For Grid it controls alignment in the inline axisMeasureFuncThe measure function of the current component, which is invoked to calculate the area that the
component’s content should occupy.
## Attribute Macros§
componentDefines a custom component type.
## Derive Macros§
PropsMakes a struct available for use as component properties.