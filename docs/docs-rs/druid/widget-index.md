druid

# Module widget

Source

## Modules§

preludeThe types required to implement a `Widget`.

## Structs§

AddedThis `Controller` widget responds to `LifeCycle::WidgetAdded` event
with the provided closure. Pass this and a child widget to `ControllerHost`
to respond to the event when the child widget is added to the widget tree.
This is also available, for convenience, as an `on_added` method
via `WidgetExt`.AlignA widget that aligns its child.AspectRatioBoxA widget that preserves the aspect ratio given to it.ButtonA button with a text label.CheckboxA checkbox that toggles a `bool`.ClickA clickable `Controller` widget. Pass this and a child widget to a
`ControllerHost` to make the child interactive. More conveniently, this is
available as an `on_click` method via `WidgetExt`.ClipBoxA widget exposing a rectangular view into its child, which can be used as a building block for
widgets that scroll their child.ContainerA widget that provides simple visual styling options to a child.ControllerHostA `Widget` that manages a child and a `Controller`.DefaultScopePolicyA default implementation of `ScopePolicy` that takes a function and a transfer.DisabledIfA widget wrapper which disables the child widget if the provided closure return true.EitherA widget that switches between two possible child views.EnvScopeA widget that accepts a closure to update the environment for its child.FlexA container with either horizontal or vertical layout.FlexParamsOptional parameters for an item in a `Flex` container (row or column).IdentityWrapperA wrapper that adds an identity to an otherwise anonymous widget.ImageA widget that renders a bitmap Image.IntrinsicWidthA widget that sizes its child to the child’s maximum intrinsic width.LabelA label that displays static or dynamic text.LensScopeTransferA `ScopeTransfer` that uses a Lens to synchronise between a large internal
state and a small input.LensWrapA wrapper for its widget subtree to have access to a part
of its parent’s data.ListA list widget for a variable-size collection of items.MaybeA widget that switches between two possible child views, for `Data` that
is `Option<T>`.PaddingA widget that just adds padding around its child.PainterA widget that only handles painting.ProgressBarA progress bar, displaying a numeric progress value.RadioA single radio buttonRadioGroupA group of radio buttonsRangeSliderA range slider, allowing interactive update of two numeric values .RawLabelA widget that displays text data.ScopeA widget that allows encapsulation of application state.ScrollA container that scrolls its contents.SizedBoxA widget with predefined size.SliderA slider, allowing interactive update of a numeric value.SpinnerAn animated spinner widget for showing a loading state.SplitA container containing two other widgets, splitting the area either horizontally or vertically.StepperA stepper widget for step-wise increasing and decreasing a value.Svg`svg`A widget that renders a SVGSvgData`svg`Stored parsed SVG tree.SwitchA switch that toggles a `bool`.TabInfoInformation about a tab that may be used by the TabPolicy to
drive the visual presentation and behaviour of its labelTabsA tabs widget.TabsStateThis is the current state of the tabs widget as a whole.
This expands the input data to include a policy that determines how tabs are derived,
and the index of the currently selected tabTextBoxA widget that allows user text input.ValueTextBoxA `TextBox` that uses a `Formatter` to handle formatting and validation
of its data.ViewSwitcherA widget that switches dynamically between multiple children.ViewportRepresents the size and position of a rectangular “viewport” into a larger area.WidgetIdA unique identifier for a single `Widget`.ZStackA container that stacks its children on top of each other.

## Enums§

AxisAn axis in visual space.BackgroundBrushSomething that can be used as the background for a widget.CrossAxisAlignmentThe alignment of the widgets on the container’s cross (or minor) axis.FillStratStrategies for inscribing a rectangle inside another rectangle.KnobStyleThe shape of the slider knobs.LabelTextThe text for a `Label`.LineBreakingOptions for handling lines that are too wide for the label.MainAxisAlignmentArrangement of children on the main axis.TabsEdgeDetermines where the tab bar should be placed relative to the cross axisTabsTransitionDetermines whether the tabs will have a transition animation when a new tab is selected.TextBoxEventEvents sent to a `ValidationDelegate`.

## Traits§

AddTabAddTabs is an extension to TabsPolicy.
If a policy implements AddTab, then the add_tab and with_tab methods will be available on
the Tabs instance.ControllerA trait for types that modify behaviour of a child widget.ListIterThis iterator enables writing List widget for any `Data`.ScopePolicyA policy that controls how a `Scope` will interact with its surrounding
application data. Specifically, how to create an initial State from the
input, and how to synchronise the two using a `ScopeTransfer`.ScopeTransferA `ScopeTransfer` knows how to synchronise input data with its counterpart
within a `Scope`.TabsPolicyA policy that determines how a Tabs instance derives its tabs from its app data.ValidationDelegateA type that can be registered to receive callbacks as the state of a
`ValueTextBox` changes.WidgetThe trait implemented by all widgets.WidgetExtA trait that provides extra methods for combining `Widget`s.WidgetWrapperA trait for widgets that wrap a single child to expose that child for access and mutation
