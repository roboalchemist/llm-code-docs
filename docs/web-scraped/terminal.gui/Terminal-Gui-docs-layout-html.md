# Source: https://gui-cs.github.io/Terminal.Gui/docs/layout.html

Title: Layout | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/layout.html

Markdown Content:
Terminal.Gui provides a rich system for how [View](https://gui-cs.github.io/Terminal.Gui/docs/View.html) objects are laid out relative to each other. The layout system also defines how coordinates are specified.

See [View Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/View.html), [Arrangement Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/arrangement.html), [Scrolling Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/scrolling.html), and [Drawing Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/drawing.html) for more.

Table of Contents[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#table-of-contents)
---------------------------------------------------------------------------------------------

* [Lexicon & Taxonomy](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#lexicon--taxonomy)
* [Arrangement Modes](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#arrangement-modes)
* [Composition](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#composition)
* [The Content Area](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#the-content-area)
* [The Viewport](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#the-viewport)
* [Layout Engine](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#layout-engine)
  * [Pos](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#pos)
  * [Dim](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#dim)

* [How To](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#how-to)
  * [Stretch a View Between Fixed Elements](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#stretch-a-view-between-fixed-elements)
  * [Align Multiple Views (Like Dialog Buttons)](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#align-multiple-views-like-dialog-buttons)
  * [Center with Auto-Sizing and Constraints (Like Dialog)](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#center-with-auto-sizing-and-constraints-like-dialog)

* * *

Lexicon & Taxonomy[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#lexicon--taxonomy)
----------------------------------------------------------------------------------------------

| Term | Meaning |
| --- | --- |
| **Adornment** | The `Thickness`es that separate the `Frame` from the `Viewport`. There are three Adornments: `Margin`, `Padding`, and `Border`. Adornments are not part of the View's content and are not clipped by the View's `ClipArea`. |
| **Application-Relative** | The dimensions and characteristics of the application. Because only full-screen apps are currently supported, @Terminal.Gui.Application is effectively the same as `Screen` from a layout perspective. _Application-Relative_ currently means an origin (`0, 0`) at the top-left corner of the terminal. @Terminal.Gui.Application.Top is a `View` with a top-left corner fixed at the _Application.Relative_ coordinate of (`0, 0`) and is the size of `Screen`. |
| **Border** | The `Adornment` that resides in the inside of the `Margin`. The Border is where a visual border (drawn using line-drawing glyphs) and the @Terminal.Gui.View.Title are drawn, and where the user can interact with the mouse/keyboard to adjust the Views' [Arrangement](https://gui-cs.github.io/Terminal.Gui/docs/arrangement.html). |
| **Content Area** | Describes the View's total content. The location of the content is always `(0, 0)` and the size is set by @Terminal.Gui.View.SetContentSize* and defaults to the size of the `Viewport`. If the content size is larger than the `Viewport`, scrolling is enabled. |
| **Content-Relative** | A rectangle, with an origin of (`0, 0`) and size, defined by @Terminal.Gui.View.GetContentSize*, where the View's content exists. _Content-Relative_ means a coordinate is relative to the top-left corner of the content, which is always (`0,0`). @Terminal.Gui.View.ContentToScreen* and @Terminal.Gui.View.ScreenToContent* are helper methods for translating coordinates. |
| **Frame** | A `Rectangle` that defines the location and size of the @Terminal.Gui.View. The coordinates are relative to the SuperView of the View (or, in the case of `Application.Top`, the console size). Controlled by @Terminal.Gui.View.X, @Terminal.Gui.View.Y, @Terminal.Gui.View.Width, and @Terminal.Gui.View.Height. |
| **Frame-Relative** | The @Terminal.Gui.View.Frame property of a `View` is a rectangle that describes the current location and size of the view relative to the `Superview`'s content area. _Frame-Relative_ means a coordinate is relative to the top-left corner of the View in question. @Terminal.Gui.View.FrameToScreen*and @Terminal.Gui.View.ScreenToFrame* are helper methods for translating coordinates. |
| **Margin** | The outermost `Adornment`. The outside of the margin is a rectangle the same size as the `Frame`. By default `Margin` is `{0,0,0,0}`. When made thicker, Margins are visually transparent and transparent to mouse events by default. |
| **Overlapped/Overlapping** | Refers to a form [Layout](https://gui-cs.github.io/Terminal.Gui/docs/layout.html) where SubViews of a View are visually arranged such that their Frames overlap. In Overlap view arrangements there is a Z-axis (Z-order) in addition to the X and Y dimension. |
| **Padding** | The `Adornment` resides in the inside of the `Border` and outside of the `Viewport`. `Padding` is `{0, 0, 0, 0}` by default. Padding is not part of the View's content and is not clipped by the View's `Clip`. When enabled, scroll bars reside within `Padding`. |
| **Screen-Relative** | Describes the dimensions and characteristics of the underlying terminal. Currently Terminal.Gui only supports applications that run "full-screen", meaning they fill the entire terminal when running. _Screen-Relative_ means an origin (`0, 0`) at the top-left corner of the terminal. @Terminal.Gui.ConsoleDriver implementations operate exclusively on _Screen-Relative_ coordinates. |
| **Thickness** | A smart `record struct` describing a rectangle where each of the four sides can have a width. Valid width values are >= 0. The inner area of a Thickness is the sum of the widths of the four sides minus the size of the rectangle. |
| **Tiled/Tiling** | Refer to a form of Views that are visually arranged such that they abut each other and do not overlap. In a Tiled view arrangement, Z-ordering only comes into play when a developer intentionally causes views to be aligned such that they overlap. |
| **Viewport** | The `Rectangle` that describes the portion of the View's `Content Area` that is currently visible to the user. If size of the `Content Area` is larger than the `Viewport`, scrolling is enabled and the `Viewport` location determines which portion of the content is visible. |
| **Viewport-Relative** | A _Content-Relative_ rectangle representing the subset of the View's content that is visible to the user: @Terminal.Gui.View.Viewport. _Viewport-Relative_ means a coordinate that is bound by (`0,0`) and the size of the inner-rectangle of the View's `Padding`. The View drawing primitives (e.g. `View.Move`) take _Viewport-Relative_ coordinates. |

Arrangement Modes[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#arrangement-modes)
---------------------------------------------------------------------------------------------

See [Arrangement Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/arrangement.html) for more.

Composition[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#composition)
---------------------------------------------------------------------------------

View Composition Diagram
------------------------

The diagram above shows the structure of a View's composition:

1. **Frame**: The outermost rectangle defining the View's location and size
2. **Margin**: Separates the View from other SubViews
3. **Border**: Contains visual border and title
4. **Padding**: Offsets the Viewport from the Border
5. **Viewport**: The visible portion of the Content Area
6. **Content Area**: Where the View's content is drawn (shown larger than Viewport to illustrate scrolling)

Each layer is defined by a Thickness that specifies the width of each side (top, right, bottom, left). The Content Area is shown as a separate container that the Viewport "looks into" - this illustrates how scrolling works. In this example, the Viewport is positioned at (5,5) relative to the Content Area, showing how scrolling works.

The Content Area[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#the-content-area)
-------------------------------------------------------------------------------------------

**Content Area** refers to the rectangle with a location of `0,0` with the size returned by `GetContentSize()`.

The content area is the area where the view's content is drawn. Content can be any combination of the `Text` property, `SubViews`, and other content drawn by the View. The `GetContentSize()` method gets the size of the content area of the view.

The Content Area size tracks the size of the `Viewport` by default. If the content size is set via `SetContentSize()`, the content area is the provided size. If the content size is larger than the `Viewport`, scrolling is enabled.

The Viewport[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#the-viewport)
-----------------------------------------------------------------------------------

The `Viewport` is a rectangle describing the portion of the **Content Area** that is visible to the user. It is a "portal" into the content. The `Viewport.Location` is relative to the top-left corner of the inner rectangle of `View.Padding`. If `Viewport.Size` is the same as `View.GetContentSize()`, `Viewport.Location` will be `0,0`.

To enable scrolling call `View.SetContentSize()` and then set `Viewport.Location` to positive values. Making `Viewport.Location` positive moves the Viewport down and to the right in the content.

See the [Scrolling Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/scrolling.html) for details on how to enable scrolling.

### Viewport Settings[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#viewport-settings)

The `ViewportSettings` property controls how the Viewport is constrained using [Viewport Settings Flags](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.ViewportSettingsFlags.html). By default, `ViewportSettings` is `None`, which provides sensible constraints for typical scrolling scenarios.

#### Default Behavior (No Flags Set)[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#default-behavior-no-flags-set)

With no flags set, the Viewport is constrained as follows:

* **No negative scrolling**: `Viewport.X` and `Viewport.Y` cannot go below `0`. The user cannot scroll above or to the left of the content origin.
* **Content fills the viewport**: The Viewport is clamped so that `Viewport.X + Viewport.Width <= ContentSize.Width` and `Viewport.Y + Viewport.Height <= ContentSize.Height`. This prevents blank space from appearing when scrolling - the content always fills the visible area.
* **Last row/column always visible**: Even if trying to scroll past the end of content, at least the last row and last column remain visible.

#### Flag Categories[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#flag-categories)

The flags are organized into categories:

**Negative Location Flags** - Allow scrolling before the content origin (0,0):

* `AllowNegativeX` - Permits `Viewport.X < 0` (scroll left of content)
* `AllowNegativeY` - Permits `Viewport.Y < 0` (scroll above content)
* `AllowNegativeLocation` - Combines both X and Y

**Greater Than Content Flags** - Allow scrolling past the last row/column:

* `AllowXGreaterThanContentWidth` - Permits `Viewport.X >= ContentSize.Width`
* `AllowYGreaterThanContentHeight` - Permits `Viewport.Y >= ContentSize.Height`
* `AllowLocationGreaterThanContentSize` - Combines both X and Y

**Blank Space Flags** - Allow blank space to appear when scrolling:

* `AllowXPlusWidthGreaterThanContentWidth` - Permits `Viewport.X + Viewport.Width > ContentSize.Width` (blank space on right)
* `AllowYPlusHeightGreaterThanContentHeight` - Permits `Viewport.Y + Viewport.Height > ContentSize.Height` (blank space on bottom)
* `AllowLocationPlusSizeGreaterThanContentSize` - Combines both X and Y

**Conditional Negative Flags** - Allow negative scrolling only when viewport is larger than content:

* `AllowNegativeXWhenWidthGreaterThanContentWidth` - Useful for centering content smaller than the view
* `AllowNegativeYWhenHeightGreaterThanContentHeight` - Useful for centering content smaller than the view
* `AllowNegativeLocationWhenSizeGreaterThanContentSize` - Combines both X and Y

**Drawing Flags** - Control clipping and clearing behavior:

* `ClipContentOnly` - Clips drawing to the visible content area instead of the entire Viewport
* `ClearContentOnly` - Clears only the visible content area (requires `ClipContentOnly`)
* `Transparent` - The view does not clear its background when drawing
* `TransparentMouse` - Mouse events pass through areas not occupied by SubViews

**ScrollBar Flags** - Enable built-in scrollbars:

* `HasVerticalScrollBar` - Enables the built-in `VerticalScrollBar` with [Scroll Bar Visibility Mode](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ScrollBarVisibilityMode.html).Auto behavior (automatically shown when content exceeds viewport)
* `HasHorizontalScrollBar` - Enables the built-in `HorizontalScrollBar` with [Scroll Bar Visibility Mode](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ScrollBarVisibilityMode.html).Auto behavior (automatically shown when content exceeds viewport)
* `HasScrollBars` - Combines both vertical and horizontal scrollbar flags

Layout Engine[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#layout-engine)
-------------------------------------------------------------------------------------

Terminal.Gui provides a rich system for how views are laid out relative to each other. The position of a view is set by setting the `X` and `Y` properties, which are of time [Pos](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Pos.html). The size is set via `Width` and `Height`, which are of type [Dim](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Dim.html).

The layout system uses virtual properties for categorization without type checking: `ReferencesOtherViews()`, `DependsOnSuperViewContentSize`, `CanContributeToAutoSizing`, `GetMinimumContribution()`, `IsFixed`, and `RequiresTargetLayout`. This enables extensibility.

```
var label1 = new Label () { X = 1, Y = 2, Width = 3, Height = 4, Title = "Absolute")

var label2 = new Label () {
    Title = "Computed",
    X = Pos.Right (otherView),
    Y = Pos.Center (),
    Width = Dim.Fill (),
    Height = Dim.Percent (50)
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html# "Copy")

### Pos[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#pos)

[Pos](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Pos.html) is the type of `View.X` and `View.Y` and supports the following sub-types:

* Absolute position, by passing an integer - `Pos.Absolute()`.
* Percentage of the parent's view size - `Pos.Percent()`
* Anchored from the end of the dimension - `Pos.AnchorEnd()`
* Centered, using `Pos.Center()`
* The `Pos.Left()`, `Pos.Right()`, `Pos.Top()`, and `Pos.Bottom()` tracks the position of another view.
* Aligned (left, right, center, etc...) with other views - `Pos.Align()`
* An arbitrary function - `Pos.Func()`

All [Pos](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Pos.html) coordinates are relative to the SuperView's content area.

[Pos](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Pos.html) values can be combined using addition or subtraction:

```
// Set the X coordinate to 10 characters left from the center
view.X = Pos.Center () - 10;
view.Y = Pos.Percent (20);

anotherView.X = AnchorEnd (10);
anotherView.Width = 9;

myView.X = Pos.X (view);
myView.Y = Pos.Bottom (anotherView) + 5;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html# "Copy")

### Dim[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#dim)

[Dim](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Dim.html) is the type of `View.Width` and `View.Height` and supports the following sub-types:

* Automatic size based on the View's content (either SubViews or Text) - `Dim.Auto()` - See [Dim.Auto Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/dimauto.html).
* Absolute size, by passing an integer - `Dim.Absolute()`.
* Percentage of the SuperView's Content Area - `Dim.Percent()`.
* Fill to the end of the SuperView's Content Area - `Dim.Fill()`. **Note:**`Dim.Fill` does not contribute to a SuperView's `Dim.Auto()` sizing unless `minimumContentDim` is specified. See [Dim.Auto Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/dimauto.html) for details.
* Reference the Width or Height of another view - `Dim.Width()`, `Dim.Height()`.
* An arbitrary function - `Dim.Func()`.

All [Dim](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Dim.html) dimensions are relative to the SuperView's content area.

Like, [Pos](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Pos.html), objects of type [Dim](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Dim.html) can be combined using addition or subtraction, like this:

```
// Set the Width to be 10 characters less than filling 
// the remaining portion of the screen
view.Width = Dim.Fill () - 10;

view.Height = Dim.Percent(20) - 1;

anotherView.Height = Dim.Height (view) + 1;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html# "Copy")
How To[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#how-to)
-----------------------------------------------------------------------

This section provides solutions to common layout scenarios.

### Stretch a View Between Fixed Elements[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#stretch-a-view-between-fixed-elements)

**Scenario:** A label on the left, a text field that stretches to fill available space, and a button anchored to the right:

```
[label][    stretching text field    ][button]
```

[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html# "Copy")

```
Label label = new () { Text = "_Name:" };
Button btn = new () { Text = "_OK", X = Pos.AnchorEnd () };
TextField textField = new ()
{
    X = Pos.Right (label) + 1,
    Width = Dim.Func (() => btn.Frame.X - label.Frame.Width - 1)
};
superView.Add (label, textField, btn);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html# "Copy")

### Align Multiple Views (Like Dialog Buttons)[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#align-multiple-views-like-dialog-buttons)

**Scenario:** Align buttons horizontally using `Pos.Align()`, as [Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Dialog.html) does:

```
Button cancelBtn = new ()
{
    Text = "_Cancel",
    X = Pos.Align (Alignment.End)
};
Button okBtn = new ()
{
    Text = "_OK",
    X = Pos.Align (Alignment.End)
};
superView.Add (cancelBtn, okBtn);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html# "Copy")
The `Pos.Align` method supports different alignments (`Start`, `Center`, `End`, `Fill`) and can add spacing between items via `AlignmentModes`.

### Center with Auto-Sizing and Constraints (Like Dialog)[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html#center-with-auto-sizing-and-constraints-like-dialog)

**Scenario:** A centered view that auto-sizes to its content, with minimum and maximum constraints that account for adornments ([Border](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Border.html), [Margin](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Margin.html), [Padding](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Padding.html)). This is how [Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Dialog.html) positions and sizes itself:

```
Window popup = new ()
{
    X = Pos.Center (),
    Y = Pos.Center (),
    Width = Dim.Auto (
        minimumContentDim: 20,  // Minimum width
        maximumContentDim: Dim.Percent (100) - Dim.Func (_ => popup.GetAdornmentsThickness ().Horizontal)),
    Height = Dim.Auto (
        minimumContentDim: 5,   // Minimum height
        maximumContentDim: Dim.Percent (100) - Dim.Func (_ => popup.GetAdornmentsThickness ().Vertical))
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/layout.html# "Copy")
The key insight is `maximumContentDim` subtracts the adornments thickness from 100% to ensure the view (including its [Border](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Border.html), [Margin](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Margin.html), and [Padding](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Padding.html)) never exceeds the SuperView's bounds.
