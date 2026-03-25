# Source: https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html

Title: Migrating From v1 To v2 | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html

Markdown Content:
This document provides a comprehensive guide for migrating applications from Terminal.Gui v1 to v2.

For detailed breaking change documentation, check out this Discussion: [https://github.com/gui-cs/Terminal.Gui/discussions/2448](https://github.com/gui-cs/Terminal.Gui/discussions/2448)

Table of Contents[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#table-of-contents)
------------------------------------------------------------------------------------------------------

* [Overview of Major Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#overview-of-major-changes)
* [Application Architecture](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#application-architecture)
* [View Construction and Initialization](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#view-construction-and-initialization)
* [Layout System Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#layout-system-changes)
* [Color and Attribute Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#color-and-attribute-changes)
* [Type Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#type-changes)
* [Unicode and Text](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#unicode-and-text)
* [Keyboard API](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#keyboard-api)
* [Mouse API](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#mouse-api)
* [Navigation Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#navigation-changes)
* [Scrolling Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#scrolling-changes)
* [Adornments](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#adornments)
* [Event Pattern Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#event-pattern-changes)
* [Cursor Management](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#cursor-management)
* [View-Specific Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#view-specific-changes)
* [Disposal and Resource Management](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#disposal-and-resource-management)
* [API Terminology Changes](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#api-terminology-changes)

* * *

Overview of Major Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#overview-of-major-changes)
----------------------------------------------------------------------------------------------------------------------

Terminal.Gui v2 represents a major architectural evolution with these key improvements:

1. **Instance-Based Application Model** - Move from static [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html) to [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) instances
2. **IRunnable Architecture** - Interface-based runnable pattern with type-safe results
3. **Simplified Layout** - Removed Absolute/Computed distinction, improved adornments
4. **24-bit TrueColor** - Full color support by default
5. **Enhanced Input** - Better keyboard and mouse APIs
6. **Built-in Scrolling** - All views support scrolling inherently
7. **Fluent API** - Method chaining for elegant code
8. **Proper Disposal** - IDisposable pattern throughout

* * *

Application Architecture[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#application-architecture)
--------------------------------------------------------------------------------------------------------------------

### Instance-Based Application Model[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#instance-based-application-model)

**v1 Pattern (Static):**

```
// v1 - static Application
Application.Init();
var top = Application.Top;
top.Add(myView);
Application.Run();
Application.Shutdown();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2 Recommended Pattern (Instance-Based):**

```
// v2 - instance-based with using statement
using (var app = Application.Create().Init())
{
    var top = new Window();
    top.Add(myView);
    app.Run(top);
    top.Dispose();
} // app.Dispose() called automatically
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2 Legacy Pattern (Still Works):**

```
// v2 - legacy static (marked obsolete but functional)
Application.Init();
var top = new Window();
top.Add(myView);
Application.Run(top);
top.Dispose();
Application.Shutdown(); // Obsolete - use Dispose() instead
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### IRunnable Architecture[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#irunnable-architecture)

v2 introduces [IRunnable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IRunnable.html) for type-safe, runnable views:

```
// Create a dialog that returns a typed result
public class FileDialog : Runnable<string>
{
    // Implementation
}

// Use it
using (var app = Application.Create().Init())
{
    app.Run<FileDialog>();
    string? result = app.GetResult<string>();
    
    if (result is { })
    {
        OpenFile(result);
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**Key Benefits:**

* Type-safe results (no casting)
* Automatic disposal of framework-created runnables
* CWP-compliant lifecycle events
* Works with any View (not just Toplevel)

### Disposal and Resource Management[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#disposal-and-resource-management)

v2 requires explicit disposal:

```
// ❌ v1 - Application.Shutdown() disposed everything
Application.Init();
var top = new Window();
Application.Run(top);
Application.Shutdown(); // Disposed top automatically

// ✅ v2 - Dispose views explicitly
using (var app = Application.Create().Init())
{
    var top = new Window();
    app.Run(top);
    top.Dispose(); // Must dispose
}

// ✅ v2 - Framework-created runnables disposed automatically
using (var app = Application.Create().Init())
{
    app.Run<ColorPickerDialog>();
    var result = app.GetResult<Color>();
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**Disposal Rules:**

* "Whoever creates it, owns it"
* `Run<TRunnable>()`: Framework creates → Framework disposes
* `Run(IRunnable)`: Caller creates → Caller disposes
* Always dispose [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) (use `using` statement)

### View.App Property[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#viewapp-property)

Views now have an `App` property for accessing the application context:

```
// ❌ v1 - Direct static reference
Application.Driver.Move(x, y);

// ✅ v2 - Use View.App
App?.Driver.Move(x, y);

// ✅ v2 - Dependency injection
public class MyView : View
{
    private readonly IApplication _app;
    
    public MyView(IApplication app)
    {
        _app = app;
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

* * *

View Construction and Initialization[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#view-construction-and-initialization)
--------------------------------------------------------------------------------------------------------------------------------------------

### Constructors → Initializers[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#constructors--initializers)

**v1:**

```
var myView = new View(new Rect(10, 10, 40, 10));
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
var myView = new View 
{ 
    X = 10, 
    Y = 10, 
    Width = 40, 
    Height = 10 
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Initialization Pattern[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#initialization-pattern)

v2 uses `ISupportInitializeNotification`:

```
// v1 - No explicit initialization
var view = new View();
Application.Run(view);

// v2 - Automatic initialization via BeginInit/EndInit
var view = new View();
// BeginInit() called automatically when added to SuperView
// EndInit() called automatically
// Initialized event raised after EndInit()
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

* * *

Layout System Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#layout-system-changes)
--------------------------------------------------------------------------------------------------------------

### Removed Layout Style Distinction[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#removed-layoutstyle-distinction)

v1 had `Absolute` and `Computed` layout styles. v2 removed this distinction.

**v1:**

```
view.LayoutStyle = LayoutStyle.Computed;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// No LayoutStyle - all layout is declarative via Pos/Dim
view.X = Pos.Center();
view.Y = Pos.Center();
view.Width = Dim.Percent(50);
view.Height = Dim.Fill();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Frame vs Bounds[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#frame-vs-bounds)

**v1:**

* `Frame` - Position/size in SuperView coordinates
* `Bounds` - Always `{0, 0, Width, Height}` (location always empty)

**v2:**

* `Frame` - Position/size in SuperView coordinates (same as v1)
* `Viewport` - Visible area in content coordinates (replaces Bounds)
  * **Important**: `Viewport.Location` can now be non-zero for scrolling

```
// ❌ v1
var size = view.Bounds.Size;
Debug.Assert(view.Bounds.Location == Point.Empty); // Always true

// ✅ v2
var visibleArea = view.Viewport;
var contentSize = view.GetContentSize();

// Viewport.Location can be non-zero when scrolled
view.ScrollVertical(10);
Debug.Assert(view.Viewport.Location.Y == 10);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Pos and Dim API Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#pos-and-dim-api-changes)

| v1 | v2 |
| --- | --- |
| `Pos.At(x)` | `Pos.Absolute(x)` |
| `Dim.Sized(width)` | `Dim.Absolute(width)` |
| `Pos.Anchor()` | `Pos.GetAnchor()` |
| `Dim.Anchor()` | `Dim.GetAnchor()` |

```
// ❌ v1
view.X = Pos.At(10);
view.Width = Dim.Sized(20);

// ✅ v2
view.X = Pos.Absolute(10);
view.Width = Dim.Absolute(20);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### View.Auto Size Removed[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#viewautosize-removed)

**v1:**

```
view.AutoSize = true;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
view.Width = Dim.Auto();
view.Height = Dim.Auto();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
See [Dim.Auto Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/dimauto.html) for details.

* * *

Adornments[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#adornments)
----------------------------------------------------------------------------------------

v2 adds `Border`, `Margin`, and `Padding` as built-in adornments.

**v1:**

```
// Custom border drawing
view.Border = new Border { /* ... */ };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// Built-in Border adornment
view.BorderStyle = LineStyle.Single;
view.Border.Thickness = new Thickness(1);
view.Title = "My View";

// Built-in Margin and Padding
view.Margin.Thickness = new Thickness(2);
view.Padding.Thickness = new Thickness(1);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
See [Layout Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/layout.html) for complete details.

* * *

Color and Attribute Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#color-and-attribute-changes)
--------------------------------------------------------------------------------------------------------------------------

### 24-bit True Color Default[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#24-bit-truecolor-default)

v2 uses 24-bit color by default.

```
// v1 - Limited color palette
var color = Color.Brown;

// v2 - ANSI-compliant names + TrueColor
var color = Color.Yellow; // Brown renamed
var customColor = new Color(0xFF, 0x99, 0x00); // 24-bit RGB
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Attribute.Make Removed[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#attributemake-removed)

**v1:**

```
var attr = Attribute.Make(Color.BrightMagenta, Color.Blue);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
var attr = new Attribute(Color.BrightMagenta, Color.Blue);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Color Name Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#color-name-changes)

| v1 | v2 |
| --- | --- |
| `Color.Brown` | `Color.Yellow` |

* * *

Type Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#type-changes)
--------------------------------------------------------------------------------------------

### Low-Level Types[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#low-level-types)

| v1 | v2 |
| --- | --- |
| `Rect` | `Rectangle` |
| `Point` | `Point` |
| `Size` | `Size` |

```
// ❌ v1
Rect rect = new Rect(0, 0, 10, 10);

// ✅ v2
Rectangle rect = new Rectangle(0, 0, 10, 10);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

* * *

Unicode and Text[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#unicode-and-text)
----------------------------------------------------------------------------------------------------

### NStack.ustring Removed[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#nstackustring-removed)

**v1:**

```
using NStack;
ustring text = "Hello";
var width = text.Sum(c => Rune.ColumnWidth(c));
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
using System.Text;
string text = "Hello";
var width = text.GetColumns(); // Extension method
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Rune Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#rune-changes)

**v1:**

```
// Implicit cast
myView.AddRune(col, row, '▄');

// Width
var width = Rune.ColumnWidth(rune);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// Explicit constructor
myView.AddRune(col, row, new Rune('▄'));

// Width
var width = rune.GetColumns();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
See [Unicode](https://gui-cs.github.io/Terminal.GuiV2Docs/docs/overview.html#unicode) for details.

* * *

Keyboard API[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#keyboard-api)
--------------------------------------------------------------------------------------------

v2 has a completely redesigned keyboard API.

### Key Class[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#key-class)

**v1:**

```
KeyEvent keyEvent;
if (keyEvent.KeyCode == KeyCode.Enter) { }
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
Key key;
if (key == Key.Enter) { }

// Modifiers
if (key.Shift) { }
if (key.Ctrl) { }

// With modifiers
Key ctrlC = Key.C.WithCtrl;
Key shiftF1 = Key.F1.WithShift;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Key Bindings[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#key-bindings)

**v1:**

```
// Override OnKeyPress
protected override bool OnKeyPress(KeyEvent keyEvent)
{
    if (keyEvent.KeyCode == KeyCode.Enter)
    {
        // Handle
        return true;
    }
    return base.OnKeyPress(keyEvent);
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// Use KeyBindings + Commands
AddCommand(Command.Accept, HandleAccept);
KeyBindings.Add(Key.Enter, Command.Accept);

private bool HandleAccept()
{
    // Handle
    return true;
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Application-Wide Keys[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#application-wide-keys)

**v1:**

```
// Hard-coded Ctrl+Q
if (keyEvent.Key == Key.CtrlMask | Key.Q)
{
    Application.RequestStop();
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// Configurable quit key
if (key == Application.GetDefaultKey (Command.Quit))
{
    Application.RequestStop ();
}

// Change the quit key via DefaultKeyBindings
Application.DefaultKeyBindings[Command.Quit] = Bind.All (Key.Esc);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Navigation Keys[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#navigation-keys)

v2 has consistent, configurable navigation keys:

| Key | Purpose |
| --- | --- |
| `Tab` | Next TabStop |
| `Shift+Tab` | Previous TabStop |
| `F6` | Next TabGroup |
| `Shift+F6` | Previous TabGroup |

```
// Configurable via Application.DefaultKeyBindings
Application.GetDefaultKey (Command.NextTabStop);    // Key.Tab
Application.GetDefaultKey (Command.PreviousTabStop); // Key.Tab.WithShift
Application.GetDefaultKey (Command.NextTabGroup);    // Key.F6
Application.GetDefaultKey (Command.PreviousTabGroup); // Key.F6.WithShift
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
See [Keyboard Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html) for complete details.

* * *

Mouse API[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#mouse-api)
--------------------------------------------------------------------------------------

### Mouse Event Event Args → Mouse Event Args[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#mouseeventeventargs--mouseeventargs)

**v1:**

```
void HandleMouse(MouseEventEventArgs args) { }
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
void HandleMouse(object? sender, MouseEventArgs args) { }
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Mouse Coordinates[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#mouse-coordinates)

**v1:**

* Mouse coordinates were screen-relative

**v2:**

* Mouse coordinates are now **Viewport-relative**

```
// v2 - Viewport-relative coordinates
view.MouseEvent += (s, e) =>
{
    // e.Position is relative to view's Viewport
    var x = e.Position.X; // 0 = left edge of viewport
    var y = e.Position.Y; // 0 = top edge of viewport
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Mouse Click Handling[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#mouse-click-handling)

**v1:**

```
// v1 - MouseClick event
view.MouseClick += (mouseEvent) =>
{
    // Handle click
    DoSomething();
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// v2 - Use MouseBindings + Commands + Activating event
view.MouseBindings.Add(MouseFlags.Button1Clicked, Command.Activate);
view.Activating += (s, e) =>
{
    // Handle selection (called when Button1Clicked)
    DoSomething();
};

// Alternative: Use MouseEvent for low-level handling
view.MouseEvent += (s, e) =>
{
    if (e.Flags.HasFlag(MouseFlags.Button1Clicked))
    {
        DoSomething();
        e.Handled = true;
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**Key Changes:**

* `View.MouseClick` event has been **removed**
* Use `MouseBindings` to map mouse events to [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html)s
* Default mouse bindings invoke [Activate](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html#Terminal_Gui_Input_Command_Activate) which raises the [Activating](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Activating.html) event
* For custom behavior, override `OnActivating` or subscribe to the [Activating](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Activating.html) event
* For low-level mouse handling, use `MouseEvent` directly

**Migration Pattern:**

```
// ❌ v1 - OnMouseClick override
protected override bool OnMouseClick(MouseEventArgs mouseEvent)
{
    if (mouseEvent.Flags.HasFlag(MouseFlags.Button1Clicked))
    {
        PerformAction();
        return true;
    }
    return base.OnMouseClick(mouseEvent);
}

// ✅ v2 - OnActivating override
protected override bool OnActivating(CommandEventArgs args)
{
    if (args.Context is CommandContext { Binding.MouseEventArgs: { } mouseArgs })
    {
        // Access mouse position and flags via context
        if (mouseArgs.Flags.HasFlag(MouseFlags.Button1Clicked))
        {
            PerformAction();
            return true;
        }
    }
    return base.OnActivating(args);
}

// ✅ v2 - Activating event (simpler)
view.Activating += (s, e) =>
{
    PerformAction();
    e.Handled = true;
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**Accessing Mouse Position in Activating Event:**

```
view.Activating += (s, e) =>
{
    // Extract mouse event args from command context
    if (e.Context is CommandContext { Binding.MouseEventArgs: { } mouseArgs })
    {
        Point position = mouseArgs.Position;
        MouseFlags flags = mouseArgs.Flags;
        
        // Use position and flags for custom logic
        HandleClick(position, flags);
        e.Handled = true;
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Mouse State and Highlighting[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#mouse-state-and-highlighting)

v2 adds enhanced mouse state tracking:

```
// Configure which mouse states trigger highlighting
view.HighlightStates = MouseState.In | MouseState.Pressed;

// React to mouse state changes
view.MouseStateChanged += (s, e) =>
{
    switch (e.Value)
    {
        case MouseState.In:
            // Mouse entered view
            break;
        case MouseState.Pressed:
            // Mouse button pressed in view
            break;
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
See [Mouse Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html) for complete details.

* * *

Navigation Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#navigation-changes)
--------------------------------------------------------------------------------------------------------

### Focus Properties[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#focus-properties)

**v1:**

```
view.CanFocus = true; // Default was true
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
view.CanFocus = true; // Default is FALSE - must opt-in
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**Important:** In v2, [Can Focus](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.CanFocus.html#Terminal_Gui_ViewBase_View_CanFocus) defaults to `false`. Views that want focus must explicitly set it.

### Focus Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#focus-changes)

**v1:**

```
// HasFocus was read-only
bool hasFocus = view.HasFocus;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// HasFocus can be set
view.HasFocus = true; // Equivalent to SetFocus()
view.HasFocus = false; // Equivalent to SuperView.AdvanceFocus()
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Tab Stop Behavior[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#tabstop-behavior)

**v1:**

```
view.TabStop = true; // Boolean
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
view.TabStop = TabBehavior.TabStop; // Enum with more options

// Options:
// - NoStop: Focusable but not via Tab
// - TabStop: Normal tab navigation
// - TabGroup: Advance via F6
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Navigation Events[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#navigation-events)

**v1:**

```
view.Enter += (s, e) => { }; // Gained focus
view.Leave += (s, e) => { }; // Lost focus
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
view.HasFocusChanging += (s, e) => 
{ 
    // Before focus changes (cancellable)
    if (preventFocusChange)
        e.Cancel = true;
};

view.HasFocusChanged += (s, e) => 
{ 
    // After focus changed
    if (e.Value)
        Console.WriteLine("Gained focus");
    else
        Console.WriteLine("Lost focus");
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
See [Navigation Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/navigation.html) for complete details.

* * *

### Scroll View Removed[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#scrollview-removed)

**v1:**

```
var scrollView = new ScrollView
{
    ContentSize = new Size(100, 100),
    ShowHorizontalScrollIndicator = true,
    ShowVerticalScrollIndicator = true
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// Built-in scrolling on every View
var view = new View();
view.SetContentSize(new Size(100, 100));

// Built-in scrollbars with automatic visibility
view.ViewportSettings |= ViewportSettingsFlags.HasVerticalScrollBar;
view.ViewportSettings |= ViewportSettingsFlags.HasHorizontalScrollBar;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Scrolling API[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#scrolling-api)

**v2:**

```
// Set content larger than viewport
view.SetContentSize(new Size(100, 100));

// Scroll by changing Viewport location
view.Viewport = view.Viewport with { Location = new Point(10, 10) };

// Or use helper methods
view.ScrollVertical(5);
view.ScrollHorizontal(3);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
See [Scrolling Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/scrolling.html) for complete details.

* * *

Event Pattern Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#event-pattern-changes)
--------------------------------------------------------------------------------------------------------------

v2 standardizes all events to use `object sender, EventArgs args` pattern.

### Button.Clicked → Button.Accepting[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#buttonclicked--buttonaccepting)

**v1:**

```
button.Clicked += () => { /* do something */ };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
button.Accepting += (s, e) => { /* do something */ };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Event Signatures[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#event-signatures)

**v1:**

```
// Various patterns
event Action SomeEvent;
event Action<T> OtherEvent;
event Action<T1, T2> ThirdEvent;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
// Consistent pattern
event EventHandler<EventArgs>? SomeEvent;
event EventHandler<T>? OtherEvent;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

* * *

Cursor Management[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#cursor-management)
------------------------------------------------------------------------------------------------------

Terminal.Gui v2 introduces a completely redesigned cursor system that separates the **Terminal Cursor** (visible indicator) from the **Draw Cursor** (internal rendering position).

### Key Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#key-changes)

**v1 Pattern (PositionCursor Override):**

```
// v1 - Override PositionCursor method
public override void PositionCursor ()
{
    if (!HasFocus) return;
    
    var col = _cursorPosition - _scrollOffset;
    if (col < 0 || col >= Frame.Width) return;
    
    Move (col, 0);  // This was confusing - affected both cursors
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2 Pattern (Cursor Property):**

```
// v2 - Set Cursor property in OnDrawContent
protected override void OnDrawContent (Rectangle viewport)
{
    // ... drawing code ...
    
    if (HasFocus)
    {
        int col = _cursorPosition - _scrollOffset;
        
        if (col >= 0 && col < viewport.Width)
        {
            // Convert to screen coordinates and set cursor
            Point screenPos = ViewportToScreen (new Point (col, 0));
            Cursor = new Cursor 
            { 
                Position = screenPos,
                Style = CursorStyle.BlinkingBar 
            };
        }
        else
        {
            // Hide cursor when outside viewport
            Cursor = new Cursor { Position = null };
        }
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Cursor Class[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#cursor-class)

v2 uses an immutable `Cursor` record class:

```
// Immutable cursor with screen coordinates
Cursor = new Cursor
{
    Position = screenPos,        // Point? - null = hidden
    Style = CursorStyle.BlinkingBar  // ANSI-based styles
};

// Update position keeping same style
Cursor = Cursor with { Position = newScreenPos };

// Hide cursor
Cursor = new Cursor { Position = null };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Cursor Style Enum[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#cursorstyle-enum)

v2 uses ANSI/VT terminal standards instead of Windows-based styles:

```
// v2 - ANSI DECSCUSR-based styles
public enum CursorStyle
{
    Default = 0,           // Usually BlinkingBlock
    BlinkingBlock = 1,     // █ (blinking)
    SteadyBlock = 2,       // █ (steady)
    BlinkingUnderline = 3, // _ (blinking)
    SteadyUnderline = 4,   // _ (steady)
    BlinkingBar = 5,       // | (blinking) - common for text editors
    SteadyBar = 6,         // | (steady)
    Hidden = -1            // No visible cursor
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Coordinate Systems[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#coordinate-systems)

**CRITICAL**: `Cursor.Position` must ALWAYS be in screen-absolute coordinates.

```
// v2 - Always convert to screen coordinates
Point contentPos = new Point (col, row);        // Your internal coordinates
Point screenPos = ContentToScreen (contentPos); // Convert to screen
Cursor = new Cursor { Position = screenPos, Style = CursorStyle.BlinkingBar };

// Or from viewport coordinates
Point viewportPos = new Point (col, row);
Point screenPos = ViewportToScreen (viewportPos);
Cursor = new Cursor { Position = screenPos, Style = CursorStyle.BlinkingBar };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Efficient Cursor Updates[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#efficient-cursor-updates)

When cursor moves without content changes, use `SetCursorNeedsUpdate()`:

```
// v2 - Signal cursor update without full redraw
private void MoveCursorRight ()
{
    _cursorPosition++;
    
    int viewportCol = _cursorPosition - _scrollOffset;
    if (viewportCol >= 0 && viewportCol < Viewport.Width)
    {
        Point screenPos = ViewportToScreen (new Point (viewportCol, 0));
        Cursor = Cursor with { Position = screenPos };
        SetCursorNeedsUpdate (); // Efficient - no redraw
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Critical: Move() vs Cursor[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#critical-move-vs-cursor)

**v1 Confusion:**

* `Move()` affected both Draw Cursor and positioning for Terminal Cursor

**v2 Clarity:**

* `Move()` ONLY affects **Draw Cursor** (where next character renders)
* `Cursor` property ONLY affects **Terminal Cursor** (visible indicator)

```
// ❌ WRONG in v2 - Don't use Move() for cursor positioning
Move (cursorCol, cursorRow);  // This is for drawing, not Terminal Cursor

// ✅ CORRECT in v2 - Use Cursor property
Point screenPos = ViewportToScreen (new Point (cursorCol, cursorRow));
Cursor = new Cursor { Position = screenPos, Style = CursorStyle.BlinkingBar };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Migration Checklist[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#migration-checklist)

When migrating cursor code from v1 to v2:

1. ✅ Remove `PositionCursor()` override
2. ✅ Move cursor logic to `OnDrawContent()` or event handlers
3. ✅ Convert coordinates to screen space using `ViewportToScreen()` or `ContentToScreen()`
4. ✅ Set `Cursor` property instead of calling `Move()`
5. ✅ Use `CursorStyle` enum for cursor appearance
6. ✅ Use `SetCursorNeedsUpdate()` for position-only changes
7. ✅ Set `Cursor.Position = null` to hide cursor

See [Cursor Management](https://gui-cs.github.io/Terminal.Gui/docs/cursor.html) for comprehensive documentation and examples.

* * *

View-Specific Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#view-specific-changes)
--------------------------------------------------------------------------------------------------------------

### List View[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#listview)

**v1:**

```
var listView = new ListView(items);
listView.SelectedChanged += () => { };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
var listView = new ListView();
listView.SetSource(items);
listView.SelectedItemChanged += (s, e) => { };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Text View[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#textview)

**v1:**

```
var textView = new TextView
{
    Text = "Initial text"
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
var textView = new TextView
{
    Text = "Initial text"
};
// Same API, but better performance
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

### Button[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#button)

**v1:**

```
var button = new Button("Click Me");
button.Clicked += () => { };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")
**v2:**

```
var button = new Button { Text = "Click Me" };
button.Accepting += (s, e) => { };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

* * *

Disposal and Resource Management[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#disposal-and-resource-management-1)
--------------------------------------------------------------------------------------------------------------------------------------

v2 implements `IDisposable` throughout the API.

### Disposal Rules[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#disposal-rules)

1. **Whoever creates it, owns it** - If you create a View, you must dispose it
2. **Framework-created instances** - The framework disposes what it creates
3. **Always use `using` statements** - For [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) instances

```
// ✅ Correct disposal pattern
using (var app = Application.Create().Init())
{
    var window = new Window();
    try
    {
        app.Run(window);
    }
    finally
    {
        window.Dispose();
    }
}

// ✅ Framework disposes what it creates
using (var app = Application.Create().Init())
{
    app.Run<MyDialog>(); // Framework creates and disposes MyDialog
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html# "Copy")

* * *

API Terminology Changes[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#api-terminology-changes)
------------------------------------------------------------------------------------------------------------------

| v1 | v2 | Notes |
| --- | --- | --- |
| `Application.Top` | `app.TopRunnable` | Property on IApplication instance |
| `Application.MainLoop` | `app.MainLoop` | Property on IApplication instance |
| `Application.Driver` | `app.Driver` | Property on IApplication instance |
| `Bounds` | `Viewport` | Viewport can have non-zero location for scrolling |
| `Rect` | `Rectangle` | Standard .NET type |
| `MouseClick` event | [Activating](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Activating.html) event | Via Command.Activate |
| `Enter`/`Leave` events | `HasFocusChanged` event | Unified focus event |
| `Button.Clicked` | `Button.Accepting` | Consistent with Command pattern |
| `AutoSize` | `Dim.Auto()` | Part of layout system |
| `LayoutStyle` | Removed | All layout is now declarative |

* * *

Summary[](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html#summary)
----------------------------------------------------------------------------------

v2 represents a significant evolution of Terminal.Gui with:

* **Better Architecture** - Instance-based, testable, maintainable
* **Modern APIs** - Standard .NET patterns throughout
* **Enhanced Capabilities** - TrueColor, built-in scrolling, better input
* **Improved Developer Experience** - Fluent API, better documentation

While migration requires some effort, the result is a more robust, performant, and maintainable codebase. Start by updating your application lifecycle to use `Application.Create()`, then address layout and input changes incrementally.

For more details, see:

* [Application Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/application.html)
* [Keyboard Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html)
* [Mouse Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html)
* [Layout Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/layout.html)
* [Navigation Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/navigation.html)
* [What's New in v2](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html)
