# Source: https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html

Title: Terminal.Gui v2 - What's New | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html

Markdown Content:
This document provides an in-depth overview of the new features, improvements, and architectural changes in Terminal.Gui v2 compared to v1.

**For migration guidance**, see the [v1 To v2 Migration Guide](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html).

Table of Contents[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#table-of-contents)
----------------------------------------------------------------------------------------------

* [Overview](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#overview)
* [Architectural Overhaul](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#architectural-overhaul)
* [Instance-Based Application Model](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#instance-based-application-model)
* [IRunnable Architecture](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#irunnable-architecture)
* [Modern Look & Feel](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#modern-look--feel)
* [Simplified API](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#simplified-api)
* [View Improvements](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#view-improvements)
* [New and Improved Views](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#new-and-improved-views)
* [Enhanced Input Handling](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#enhanced-input-handling)
* [Configuration and Persistence](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#configuration-and-persistence)
* [Debugging and Performance](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#debugging-and-performance)
* [Additional Features](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#additional-features)

* * *

Overview[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#overview)
----------------------------------------------------------------------------

Terminal.Gui v2 represents a fundamental redesign of the library's architecture, API, and capabilities. Key improvements include:

* **Instance-Based Application Model** - Move from static singletons to [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) instances
* **IRunnable Architecture** - Interface-based pattern for type-safe, runnable views
* **Proper Resource Management** - Full IDisposable pattern with automatic cleanup
* **Built-in Scrolling** - Every view supports scrolling inherently
* **24-bit TrueColor** - Full color spectrum by default
* **Enhanced Input** - Modern keyboard and mouse APIs
* **Improved Layout** - Simplified with adornments (Margin, Border, Padding)
* **Better Navigation** - Decoupled focus and tab navigation
* **Configuration System** - Persistent themes and settings
* **Logging and Metrics** - Built-in debugging and performance tracking

* * *

Architectural Overhaul[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#architectural-overhaul)
--------------------------------------------------------------------------------------------------------

### Design Philosophy[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#design-philosophy)

Terminal.Gui v2 was designed with these core principles:

1. **Separation of Concerns** - Layout, focus, input, and drawing are cleanly decoupled
2. **Performance** - Reduced overhead in rendering and event handling
3. **Modern .NET Practices** - Standard patterns like `EventHandler<T>` and `IDisposable`
4. **Testability** - Views can be tested in isolation without global state
5. **Accessibility** - Improved keyboard navigation and visual feedback

### Result[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#result)

* Thousands of lines of redundant or complex code removed
* More modular and maintainable codebase
* Better performance and predictability
* Easier to extend and customize

* * *

Instance-Based Application Model[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#instance-based-application-model)
----------------------------------------------------------------------------------------------------------------------------

See the [Application Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/application.html) for complete details.

v2 introduces an instance-based architecture that eliminates global state and enables multiple application contexts.

### Key Features[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#key-features)

**IApplication Interface:**

* [Application.Create()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.Create.html) returns an [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) instance
* Multiple applications can coexist (useful for testing)
* Each instance manages its own driver, session stack, and resources

**View.App Property:**

* Every view has an [App](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.App.html#Terminal_Gui_ViewBase_View_App) property referencing its [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) context
* Views access application services through [App](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.App.html#Terminal_Gui_ViewBase_View_App) (driver, session management, etc.)
* Eliminates static dependencies, improving testability

**Session Management:**

* [Session Stack](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.SessionStack.html#Terminal_Gui_App_IApplication_SessionStack) tracks all running sessions as a stack
* [Top Runnable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.TopRunnable.html#Terminal_Gui_App_IApplication_TopRunnable) property references the currently active session
* [Begin()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.Begin.html) and [End()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.End.html) methods manage session lifecycle

### Example[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#example)

```
// Instance-based pattern (recommended)
IApplication app = Application.Create ().Init ();
Window window = new () { Title = "My App" };
app.Run (window);
window.Dispose ();
app.Dispose ();

// With using statement for automatic disposal
using (IApplication app = Application.Create ().Init ())
{
    Window window = new () { Title = "My App" };
    app.Run (window);
    window.Dispose ();
} // app.Dispose() called automatically

// Access from within a view
public class MyView : View
{
    public void DoWork ()
    {
        App?.Driver.Move (0, 0);
        App?.TopRunnableView?.SetNeedsDraw ();
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Benefits[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#benefits)

* **Testability** - Mock [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) for unit tests
* **No Global State** - Multiple contexts can coexist
* **Clear Ownership** - Views explicitly know their context
* **Proper Cleanup** - IDisposable ensures resources are released

### Resource Management[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#resource-management)

v2 implements full `IDisposable` pattern:

```
// Recommended: using statement
using (IApplication app = Application.Create ().Init ())
{
    app.Run<MyDialog> ();
    MyResult? result = app.GetResult<MyResult> ();
}

// Ensures:
// - Input thread stopped cleanly
// - Driver resources released
// - No thread leaks in tests
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")
**Important Changes:**

* [Shutdown()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.Shutdown.html) method is obsolete - use `Dispose()` instead
* Always dispose applications (especially in tests)
* Input thread runs at ~50 polls/second (20ms throttle) until disposed

* * *

IRunnable Architecture[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#irunnable-architecture)
--------------------------------------------------------------------------------------------------------

See the [Application Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/application.html) for complete details.

v2 introduces [IRunnable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IRunnable.html) - an interface-based pattern for runnable views with type-safe results.

### Key Features[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#key-features-1)

**Interface-Based:**

* Implement [IRunnable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IRunnable.html) without inheriting from `Runnable`
* Any view can be runnable
* Decouples runnability from view hierarchy

**Type-Safe Results:**

* Generic `TResult` parameter provides compile-time type safety
* `null` indicates cancellation/non-acceptance
* Results extracted before disposal in lifecycle events

**Lifecycle Events (CWP-Compliant):**

* `IsRunningChanging` - Cancellable, before stack change
* `IsRunningChanged` - Non-cancellable, after stack change
* `IsModalChanging` - Cancellable, before modal state change
* `IsModalChanged` - Non-cancellable, after modal state change

### Example[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#example-1)

```
public class FileDialog : Runnable<string?>
{
    private TextField _pathField;
    
    public FileDialog ()
    {
        Title = "Select File";
        _pathField = new () { Width = Dim.Fill () };
        Add (_pathField);
        
        Button okButton = new () { Text = "OK", IsDefault = true };
        okButton.Accepting += (s, e) =>
        {
            Result = _pathField.Text;
            Application.RequestStop ();
        };
        AddButton (okButton);
    }
    
    protected override bool OnIsRunningChanging (bool oldValue, bool newValue)
    {
        if (!newValue)  // Stopping - extract result before disposal
        {
            Result = _pathField?.Text;
            
            // Optionally cancel stop
            if (HasUnsavedChanges ())
            {
                return true; // Cancel
            }
        }
        return base.OnIsRunningChanging (oldValue, newValue);
    }
}

// Use with fluent API
using (IApplication app = Application.Create ().Init ())
{
    app.Run<FileDialog> ();
    string? path = app.GetResult<string> ();
    
    if (path is { })
    {
        OpenFile (path);
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Fluent API[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#fluent-api)

v2 enables elegant method chaining:

```
// Concise and readable
using (IApplication app = Application.Create ().Init ())
{
    app.Run<ColorPickerDialog> ();
    Color? result = app.GetResult<Color> ();
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")
**Key Methods:**

* [Init()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.Init.html) - Returns [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) for chaining
* [Run()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.Run.html) - Creates and runs runnable, returns [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html)
* [GetResult()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.GetResult.html) - Extract typed result after run
* `Dispose()` - Release all resources

### Disposal Semantics[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#disposal-semantics)

**"Whoever creates it, owns it":**

| Method | Creator | Owner | Disposal |
| --- | --- | --- | --- |
| [Run()](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.Run.html) | Framework | Framework | Automatic when returns |
| `Run(IRunnable)` | Caller | Caller | Manual by caller |

```
// Framework ownership - automatic disposal
app.Run<MyDialog> (); // Dialog disposed automatically

// Caller ownership - manual disposal
MyDialog dialog = new ();
app.Run (dialog);
dialog.Dispose (); // Caller must dispose
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Benefits[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#benefits-1)

* **Type Safety** - No casting, compile-time checking
* **Clean Lifecycle** - CWP-compliant events
* **Automatic Disposal** - Framework manages created runnables
* **Flexible** - Works with any View, not just Toplevel

* * *

Modern Look & Feel[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#modern-look--feel)
-----------------------------------------------------------------------------------------------

### 24-bit True Color Support[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#24-bit-truecolor-support)

See the [Drawing Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/drawing.html) for complete details.

v2 provides full 24-bit color support by default:

* **Implementation**: [Attribute](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Attribute.html) class handles RGB values
* **Fallback**: Automatic 16-color mode for older terminals
* **Driver Support**: `IDriver.SupportsTrueColor` detection
* **Usage**: Direct RGB input via [Color](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Color.html) struct

```
// 24-bit RGB color
Color customColor = new (0xFF, 0x99, 0x00);

// Or use named colors (ANSI-compliant)
Color color = Color.Yellow; // Was "Brown" in v1
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Enhanced Borders and Adornments[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#enhanced-borders-and-adornments)

See the [Layout Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/layout.html) for complete details.

v2 introduces a comprehensive [Adornment](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Adornment.html) system:

* **[Margin](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Margin.html)** - Transparent spacing outside the border
* **[Border](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Border.html)** - Visual frame with title, multiple styles
* **[Padding](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Padding.html)** - Spacing inside the border

**Border Features:**

* Multiple [LineStyle](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.LineStyle.html) options: Single, Double, Heavy, Rounded, Dashed, Dotted
* Automatic line intersection handling via [LineCanvas](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.LineCanvas.html)
* Configurable thickness per side via [Thickness](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Thickness.html)
* Title display with alignment options

```
view.BorderStyle = LineStyle.Double;
view.Border.Thickness = new (1);
view.Title = "My View";

view.Margin.Thickness = new (2);
view.Padding.Thickness = new (1);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### User Configurable Themes[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#user-configurable-themes)

See the [Configuration Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/config.html) and [Scheme Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/scheme.html) for details.

v2 adds comprehensive theme support:

* **ConfigurationManager**: Loads/saves color schemes from files
* **Schemes**: Applied per-view or globally via [Scheme](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Scheme.html)
* **Text Styles**: [TextStyle](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.TextStyle.html) supports Bold, Italic, Underline, Strikethrough, Blink, Reverse, Faint
* **User Customization**: End-users can personalize without code changes

```
// Apply a theme
ConfigurationManager.Themes.Theme = "Dark";

// Customize text style
view.Scheme.Normal = new (
    Color.White, 
    Color.Black, 
    TextStyle.Bold | TextStyle.Underline
);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Line Canvas[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#linecanvas)

See the [Drawing Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/drawing.html) for complete details.

[LineCanvas](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.LineCanvas.html) provides sophisticated line drawing:

* Auto-joining lines at intersections
* Multiple line styles (Single, Double, Heavy, etc.)
* Automatic glyph selection for corners and T-junctions
* Used by [Border](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Border.html), [Line](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Line.html), and custom views

```
// Line view uses LineCanvas
Line line = new () { Orientation = Orientation.Horizontal };
line.LineStyle = LineStyle.Double;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Gradients[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#gradients)

See the [Drawing Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/drawing.html) for details.

v2 adds gradient support:

* [Gradient](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Gradient.html) - Color transitions
* [GradientFill](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.GradientFill.html) - Fill patterns
* Uses TrueColor for smooth effects
* Apply to borders, backgrounds, or custom elements

```
Gradient gradient = new (Color.Blue, Color.Cyan);
view.BackgroundGradient = new (gradient, Orientation.Vertical);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

* * *

Simplified API[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#simplified-api)
----------------------------------------------------------------------------------------

### Consistency and Reduction[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#consistency-and-reduction)

v2 consolidates redundant APIs:

* **Centralized Navigation**: [ApplicationNavigation](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.ApplicationNavigation.html) replaces scattered focus methods
* **Standard Events**: All events use `EventHandler<T>` pattern
* **Consistent Naming**: Methods follow .NET conventions (e.g., `OnHasFocusChanged`)
* **Reduced Surface**: Fewer but more powerful APIs

**Example:**

```
// v1 - Multiple scattered methods
View.MostFocused
View.EnsureFocus ()
View.FocusNext ()

// v2 - Centralized
Application.Navigation.GetFocused ()
view.SetFocus ()
view.AdvanceFocus ()
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Modern .NET Standards[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#modern-net-standards)

* Events: `EventHandler<EventArgs>` instead of custom delegates
* Properties: Consistent get/set patterns
* Disposal: IDisposable throughout
* Nullability: Enabled in core library files

### Performance Optimizations[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#performance-optimizations)

v2 reduces overhead through:

* Smarter [Needs Draw](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.NeedsDraw.html#Terminal_Gui_ViewBase_View_NeedsDraw) system (only draw what changed)
* Reduced allocations in hot paths (event handling, rendering)
* Optimized layout calculations
* Efficient input processing

**Result**: Snappier UIs, especially with many views or frequent updates

* * *

View Improvements[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#view-improvements)
----------------------------------------------------------------------------------------------

### Deterministic Lifetime Management[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#deterministic-lifetime-management)

v2 clarifies view ownership:

* Explicit disposal rules enforced by unit tests
* `Application.Run` manages `Runnable` lifecycle
* SubViews disposed automatically with SuperView
* Clear documentation of ownership semantics

### Built-in Scrolling[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#built-in-scrolling)

See the [Scrolling Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/scrolling.html) for complete details.

Every [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html) supports scrolling inherently:

* **[Viewport](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html)** - Visible rectangle (can have non-zero location)
* **[GetContentSize](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html)** - Returns total content size
* **[SetContentSize](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html)** - Sets scrollable content size
* **ScrollVertical/ScrollHorizontal** - Helper methods

**No need for ScrollView wrapper!**

```
// Enable scrolling
view.SetContentSize (new (100, 100));

// Scroll by changing Viewport location
view.ScrollVertical (5);
view.ScrollHorizontal (3);

// Built-in scrollbars with automatic visibility
view.ViewportSettings |= ViewportSettingsFlags.HasVerticalScrollBar;
view.ViewportSettings |= ViewportSettingsFlags.HasHorizontalScrollBar;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Enhanced Scroll Bar[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#enhanced-scrollbar)

v2 replaces `ScrollBarView` with [ScrollBar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ScrollBar.html):

* Cleaner implementation
* Automatic show/hide via [ScrollBarVisibilityMode](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ScrollBarVisibilityMode.html)
* Proportional sizing with `ScrollSlider`
* Integrated with View's scrolling system
* Simple to enable via [ViewportSettingsFlags](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.ViewportSettingsFlags.html)
* Accessible via [View.VerticalScrollBar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html) / [View.HorizontalScrollBar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html)

### Advanced Layout Features[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#advanced-layout-features)

See the [Layout Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/layout.html) and [DimAuto Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/dimauto.html) for details.

**[Auto](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Dim.Auto.html):**

* Automatically sizes views based on content or subviews
* Reduces manual layout calculations
* Supports multiple styles (Text, Content, Position)

**[Anchor End](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Pos.AnchorEnd.html):**

* Anchor to right or bottom of SuperView
* Enables flexible, responsive layouts

**[Pos.Align](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Pos.html):**

* Align multiple views (Left, Center, Right)
* Simplifies creating aligned layouts

```
// Auto-size based on text
label.Width = Dim.Auto ();
label.Height = Dim.Auto ();

// Anchor to bottom-right
button.X = Pos.AnchorEnd (10);
button.Y = Pos.AnchorEnd (2);

// Center align
label1.X = Pos.Center ();
label2.X = Pos.Center ();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### View Arrangement[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#view-arrangement)

See the [Arrangement Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/arrangement.html) for complete details.

[View.Arrangement](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html) enables interactive UI:

* **[ViewArrangement.Movable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.ViewArrangement.html)** - Drag with mouse or move with keyboard
* **[ViewArrangement.Resizable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.ViewArrangement.html)** - Resize edges with mouse or keyboard
* **[ViewArrangement.Overlapped](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.ViewArrangement.html)** - Z-order management for overlapping views

**Arrangement Key**: Press `Ctrl+F5` (configurable via `Application.DefaultKeyBindings` for `Command.Arrange`) to enter arrange mode

```
// Movable and resizable window
window.Arrangement = ViewArrangement.Movable | ViewArrangement.Resizable;

// Overlapped windows
container.Arrangement = ViewArrangement.Overlapped;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Enhanced Navigation[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#enhanced-navigation)

See the [Navigation Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/navigation.html) for complete details.

v2 decouples navigation concepts:

* **[CanFocus](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html)** - Whether view can receive focus (defaults to `false` in v2)
* **[TabStop](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html)** - [TabBehavior](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.TabBehavior.html) enum (TabStop, TabGroup, NoStop)
* **[ApplicationNavigation](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.ApplicationNavigation.html)** - Centralized navigation logic

**Navigation Keys (Configurable):**

* `Tab` / `Shift+Tab` - Next/previous TabStop
* `F6` / `Shift+F6` - Next/previous TabGroup
* Arrow keys - Same as Tab navigation

```
// Configure navigation keys via Application.DefaultKeyBindings
Application.DefaultKeyBindings[Command.NextTabStop] = Bind.All (Key.Tab);
Application.DefaultKeyBindings[Command.PreviousTabStop] = Bind.All (Key.Tab.WithShift);
Application.DefaultKeyBindings[Command.NextTabGroup] = Bind.All (Key.F6);
Application.DefaultKeyBindings[Command.PreviousTabGroup] = Bind.All (Key.F6.WithShift);

// Set tab behavior
view.CanFocus = true;
view.TabStop = TabBehavior.TabStop; // Normal tab navigation
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

* * *

New and Improved Views[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#new-and-improved-views)
--------------------------------------------------------------------------------------------------------

See the [Views Overview](https://gui-cs.github.io/Terminal.Gui/docs/views.html) for a complete catalog.

### New Views in v2[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#new-views-in-v2)

* **[Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Bar.html)** - Foundation for StatusBar, MenuBar, PopoverMenu
* **[CharMap](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.CharMap.html)** - Scrollable Unicode character map with UCD support
* **[ColorPicker](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ColorPicker.html)** - TrueColor selection with multiple color models
* **[DatePicker](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.DatePicker.html)** - Calendar-based date selection
* **[FlagSelector](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FlagSelector.html)** - Non-mutually-exclusive flag selection
* **[GraphView](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.GraphView.html)** - Data visualization (bar, scatter, line graphs)
* **[Line](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Line.html)** - Single lines with LineCanvas integration
* **[NumericUpDown](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.NumericUpDown-1.html)** - Type-safe numeric input
* **[OptionSelector](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.OptionSelector.html)** - Mutually-exclusive option selection
* **[Shortcut](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Shortcut.html)** - Command display with key bindings
* **[LinearRange](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.LinearRange.html)** - Sophisticated range selection control
* **[SpinnerView](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.SpinnerView.html)** - Animated progress indicators

### Significantly Improved Views[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#significantly-improved-views)

* **[FileDialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FileDialog.html)** - TreeView navigation, Unicode icons, search, history
* **[ScrollBar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ScrollBar.html)** - Clean implementation with auto-show
* **[StatusBar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.StatusBar.html)** - Rebuilt on Bar infrastructure
* **[TableView](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TableView.html)** - Generic collections, checkboxes, tree structures, custom rendering
* **[MenuBar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBar.html)** / **[PopoverMenu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.PopoverMenu.html)** - Redesigned menu system

* * *

Enhanced Input Handling[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#enhanced-input-handling)
----------------------------------------------------------------------------------------------------------

### Keyboard API[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#keyboard-api)

See the [Keyboard Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html) and [Command Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/command.html) for details.

**[Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Key.html) Class:**

* Replaces v1's `KeyEvent` struct
* High-level abstraction over raw key codes
* Properties for modifiers and key type
* Platform-independent

```
// Check keys
if (key == Key.Enter) { }
if (key == Key.C.WithCtrl) { }

// Modifiers
if (key.Shift) { }
if (key.Ctrl) { }
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")
**Key Bindings:**

* Map keys to [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html) enums
* Scopes: Application, Focused, HotKey
* Views declare supported commands via [View.AddCommand](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html)

```
// Add command handler
view.AddCommand (Command.Accept, HandleAccept);

// Bind key to command
view.KeyBindings.Add (Key.Enter, Command.Accept);

private bool HandleAccept ()
{
    // Handle command
    return true; // Handled
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")
**Configurable Keys** (via `Application.DefaultKeyBindings`):

* `Command.Quit` - Close app (default: Esc)
* `Command.Arrange` - Arrange mode (default: Ctrl+F5)
* Navigation commands (`Command.NextTabStop`, `Command.NextTabGroup`, etc.)

### Mouse API[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#mouse-api)

See the [Mouse Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html) for complete details.

**[MouseEventArgs](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Mouse.html):**

* Replaces v1's `MouseEventEventArgs`
* Cleaner structure for mouse data
* [MouseFlags](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.MouseFlags.html) for button states

**Granular Events:**

* [View.MouseClick](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html) - High-level click events
* Double-click support
* Mouse movement tracking
* Viewport-relative coordinates (not screen-relative)

**Highlight and Repeat on Hold:**

* [View.MouseHighlightStates](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html) - Allows views to provide visual feedback on hover/click.
* [View.MouseState](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html) - Indicates whether the mouse is pressed, hovered, or outside.
* [View.MouseHoldRepeat](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.html) - Enables or disables whether mouse click events will be repeated when the user holds the mouse down

Configuration and Persistence[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#configuration-and-persistence)
----------------------------------------------------------------------------------------------------------------------

See the [Configuration Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/config.html) for complete details.

### Configuration Manager[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#configurationmanager)

[ConfigurationManager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationManager.html) provides:

* JSON-based persistence
* Theme management
* Key binding customization
* View property persistence
* [SettingsScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.SettingsScope.html) - User, Application, Machine levels
* [ConfigLocations](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html) - Where to search for configs

```
// Enable configuration
ConfigurationManager.Enable (ConfigLocations.All);

// Load a theme
ConfigurationManager.Themes.Theme = "Dark";

// Save current configuration
ConfigurationManager.Save ();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")
**User Customization:**

* End-users can personalize themes, colors, text styles
* Key bindings can be remapped
* No code changes required
* JSON files easily editable

* * *

Debugging and Performance[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#debugging-and-performance)
--------------------------------------------------------------------------------------------------------------

See the [Logging Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/logging.html) for complete details.

### Logging System[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#logging-system)

[Logging](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Logging.html) integrates with Microsoft.Extensions.Logging:

* Multi-level logging (Trace, Debug, Info, Warning, Error)
* Internal operation tracking (rendering, input, layout)
* Works with standard .NET logging frameworks (Serilog, NLog, etc.)

```
// Configure logging
Logging.ConfigureLogging ("myapp.log", LogLevel.Debug);

// Use in code
Logging.Debug ("Rendering view {ViewId}", view.Id);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

### Metrics[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#metrics)

`Logging.Meter` provides performance metrics:

* Frame rate tracking
* Redraw times
* Iteration timing
* Input processing overhead

**Tools**: Use `dotnet-counters` or other metrics tools to monitor

```
dotnet counters monitor --name MyApp Terminal.Gui
```

[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html# "Copy")

* * *

Additional Features[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#additional-features)
--------------------------------------------------------------------------------------------------

### Sixel Image Support[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#sixel-image-support)

v2 supports the Sixel protocol for rendering images:

* [SixelEncoder](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.SixelEncoder.html) - Encode images as Sixel data
* [SixelSupportDetector](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.SixelSupportDetector.html) - Detect terminal support
* [SixelToRender](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.SixelToRender.html) - Render Sixel images
* Compatible terminals: Windows Terminal, xterm, others

**Use Cases**: Image previews, graphics in terminal apps

### AOT Support[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#aot-support)

v2 ensures compatibility with Ahead-of-Time compilation:

* Avoid reflection patterns problematic for AOT
* Source generators for JSON serialization via SourceGenerationContext
* Single-file deployment support
* Faster startup, reduced runtime overhead

**Example**: See `Examples/NativeAot` for AOT deployment

### Enhanced Unicode Support[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#enhanced-unicode-support)

* Correctly manages wide characters (CJK scripts)
* [TextFormatter](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Text.TextFormatter.html) accounts for Unicode width
* Fixes v1 layout issues with wide characters
* International application support

* * *

Conclusion[](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html#conclusion)
--------------------------------------------------------------------------------

Terminal.Gui v2 represents a comprehensive modernization:

**Architecture:**

* Instance-based application model
* IRunnable architecture with type-safe results
* Proper resource management (IDisposable)
* Decoupled concerns (layout, focus, input)

**Features:**

* 24-bit TrueColor
* Built-in scrolling
* Enhanced adornments (Margin, Border, Padding)
* Modern keyboard and mouse APIs
* Configuration and themes
* Logging and metrics

**API:**

* Simplified and consistent
* Modern .NET patterns
* Better performance
* Improved testability

**Views:**

* Many new views (CharMap, ColorPicker, GraphView, etc.)
* Significantly improved existing views
* Easier to create custom views

v2 provides a robust foundation for building sophisticated, maintainable, and user-friendly terminal applications. The architectural improvements, combined with new features and enhanced APIs, enable developers to create modern terminal UIs that feel responsive and polished.

For detailed migration guidance, see the [v1 To v2 Migration Guide](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html).
