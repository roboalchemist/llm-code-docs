# Source: https://gui-cs.github.io/Terminal.Gui/docs/mouse.html

Title: Mouse Deep Dive | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/mouse.html

Published Time: Fri, 13 Mar 2026 23:38:23 GMT

Markdown Content:
> **Quick Start:** Jump to [Quick Reference](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#quick-reference) for a condensed overview of the mouse pipeline and common patterns.

Table of Contents[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#table-of-contents)
--------------------------------------------------------------------------------------------

* [Quick Reference](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#quick-reference)
* [Tenets for Mouse Handling](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#tenets-for-mouse-handling)
* [Mouse Behavior - End User's Perspective](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-behavior---end-users-perspective)
* [Mouse APIs](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-apis)
* [Mouse Bindings](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-bindings)
* [Mouse Events](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-events)
* [Mouse State and Mouse Grab](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-state-and-mouse-grab)
* [Mouse Coordinate Systems](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-coordinate-systems)
* [Complete Mouse Event Pipeline](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#complete-mouse-event-pipeline)
* [Best Practices](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#best-practices)
* [Testing Mouse Input](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#testing-mouse-input)
* [Limitations and Considerations](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#limitations-and-considerations)

Quick Reference[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#quick-reference)
----------------------------------------------------------------------------------------

### The Pipeline (TL;DR)[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#the-pipeline-tldr)

```
ANSI Input ? AnsiMouseParser ? MouseInterpreter ? ApplicationMouse ? View ? Commands
   (1-based)     (0-based screen)   (click synthesis)   (routing)  (viewport)  (Activate/Accept)
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Pipeline Stages[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#pipeline-stages)

| Stage | Input | Output | Key Transformation |
| --- | --- | --- | --- |
| **ANSI** | User clicks | `ESC[<0;10;5M` | Hardware ? ANSI escape sequence |
| **Parser** | ANSI string | `Mouse{Pressed, Screen(9,4)}` | 1-based ? 0-based, Button code ? MouseFlags |
| **Interpreter** | Press/Release | `Mouse{Clicked, Screen(9,4)}` | Press+Release ? Clicked, Timing ? DoubleClicked |
| **ApplicationMouse** | Screen coords | `Mouse{Clicked, Viewport(2,1)}` | Screen ? Viewport, Find view, Handle grab |
| **View** | Viewport coords | Command invocation | Clicked ? Command.Activate, MouseState updates |
| **Commands** | Command | Event | Activate ? Activating, Accept ? Accepting |

### Coordinate Systems[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#coordinate-systems)

| Level | Origin | Example |
| --- | --- | --- |
| **ANSI** | 1-based, (1,1) = top-left | `ESC[<0;10;5M` |
| **Screen** | 0-based, (0,0) = top-left of terminal | `ScreenPosition = (9,4)` |
| **Viewport** | 0-based, relative to view's content area | `Position = (2,1)` |

### Common Patterns[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#common-patterns)

**Handle mouse clicks:**

```
view.Activating += (s, e) =>
{
    if (e.Context?.Binding is MouseBinding { MouseEvent: { } mouse })
    {
        Point position = mouse.Position;  // Viewport-relative
        HandleClick(position);
        e.Handled = true;
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**Enable visual feedback and auto-grab:**

```
view.MouseHighlightStates = MouseState.In | MouseState.Pressed;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**Continuous button press (scrollbar arrows, spin buttons):**

```
view.MouseHoldRepeat = MouseFlags.LeftButtonReleased;
view.Activating += (s, e) => { DoRepeatAction(); e.Handled = true; };
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
Tenets for Mouse Handling[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#tenets-for-mouse-handling)
------------------------------------------------------------------------------------------------------------

Tenets higher in the list have precedence over tenets lower in the list.

* **Keyboard Required; Mouse Optional** - Terminal users expect full functionality without a mouse. We strive to ensure anything that can be done with the keyboard is also possible with the mouse, and avoid mouse-only features.

* **Be Consistent With the User's Platform** - Users choose their platform and Terminal.Gui apps should respond to mouse input consistent with platform conventions. For example, on Windows: right-click shows context menus, double-click activates items, mouse wheel scrolls content.

Mouse Behavior - End User's Perspective[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-behavior---end-users-perspective)
---------------------------------------------------------------------------------------------------------------------------------------

### Button Behavior[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#button-behavior)

| Scenario | Visual State | `Command.Accept` Count | Notes |
| --- | --- | --- | --- |
| **Single click** (press + release inside) | Pressed ? Released | **1** on release | Standard click behavior |
| **Hold** (MouseHoldRepeat = false) | Pressed ? stays ? Released | **1** on release | Normal push-button |
| **Hold** (MouseHoldRepeat = true) | Same visual | **~10+** (timer ~500ms initial, ~50ms intervals) + **1 final** on release | Scrollbar arrow behavior |
| **Drag outside ? release outside** | Pressed ? Released | **0** (canceled) | Standard click cancellation |
| **Double-click** (MouseHoldRepeat = false) | Press?Release?Press?Release | **2** (one per release) | Two separate accepts |
| **Double-click** (MouseHoldRepeat = true) | Same cycle | **2** (one per release) | Each press/release fires Accept |

**Key Point for MouseHoldRepeat:** When enabled, the view responds to **Press and Release events only**. Each press starts the timer (which fires Accept repeatedly), and each release fires one final Accept (if released inside).

### List View Behavior[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#listview-behavior)

| Scenario | Selection State | `Command.Activate` Count | `Command.Accept` Count | Notes |
| --- | --- | --- | --- | --- |
| **Single click** | Item selected on click | **1** | **0** | Selection happens immediately |
| **Double-click** | Selected on first click | **1** (first click) | **1** (second click) | Standard file browser behavior |
| **Enter key** | No change (already selected) | **0** | **1** | Keyboard equivalent of double-click |

Mouse APIs[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-apis)
------------------------------------------------------------------------------

Terminal.Gui provides these APIs for handling mouse input:

* **Mouse Bindings** - Declarative approach using [Mouse Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.MouseBindings.html) to map mouse events to commands. **Recommended for most scenarios.**

* **Mouse Events** - Direct event handling via `MouseEvent` for complex scenarios like drag-and-drop.

* **Mouse State** - [Mouse State](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.MouseState.html) property provides current interaction state for visual feedback.

* **Mouse** class - Platform-independent abstraction ([Mouse](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Mouse.html)) for mouse events.

Mouse Bindings[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-bindings)
--------------------------------------------------------------------------------------

Mouse Bindings is the **recommended** way to handle mouse input. Views call `AddCommand` to declare command support, then use [Mouse Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.MouseBindings.html) to map mouse events to commands:

```
public class MyView : View
{
    public MyView()
    {
        AddCommand (Command.ScrollUp, () => ScrollVertical (-1));
        MouseBindings.Add (MouseFlags.WheelUp, Command.ScrollUp);
        
        AddCommand (Command.ScrollDown, () => ScrollVertical (1));
        MouseBindings.Add (MouseFlags.WheelDown, Command.ScrollDown);
        
        // Mouse clicks invoke Command.Activate by default
        AddCommand (Command.Activate, () => {
            SelectItem();
            return true;
        });
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Default Mouse Bindings[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#default-mouse-bindings)

All views have these default bindings:

```
MouseBindings.Add (MouseFlags.LeftButtonPressed, Command.Activate);
MouseBindings.Add (MouseFlags.LeftButtonPressed | MouseFlags.Ctrl, Command.Context);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
When a mouse event occurs matching a binding, the bound command is invoked, which raises the corresponding event (e.g., [Activate](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html#Terminal_Gui_Input_Command_Activate) ? [Activating](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Activating.html) event).

### Common Binding Patterns[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#common-binding-patterns)

* **Click Events**: `MouseFlags.LeftButtonPressed` for selection/interaction
* **Context Menu**: `MouseFlags.RightButtonPressed` or `LeftButtonPressed | Ctrl`
* **Scroll Events**: `MouseFlags.WheelUp` / `WheelDown`
* **Drag Operations**: `MouseFlags.LeftButtonPressed` + mouse move tracking

Mouse Events[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-events)
----------------------------------------------------------------------------------

### Mouse Event Processing Flow[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-event-processing-flow)

Mouse events are processed using the [Cancellable Work Pattern](https://gui-cs.github.io/Terminal.Gui/docs/cancellable-work-pattern.html):

1. **Driver Level**: Captures platform-specific events ? converts to `Mouse`
2. **Application Level**: `IMouse.RaiseMouseEvent` determines target view and routes event
3. **View Level**: `View.NewMouseEvent()` processes:
    *Pre-condition validation (enabled, visible, wants event type)
    *   Low-level `MouseEvent` (raises `OnMouseEvent()` and `MouseEvent` event)
    *Mouse grab handling (if `MouseHighlightStates` or `MouseHoldRepeat` set)
    *   Command invocation via [Mouse Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.MouseBindings.html)

### Handling Mouse Events Directly[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#handling-mouse-events-directly)

For scenarios requiring direct event handling (drag-and-drop, custom gestures):

```
public class CustomView : View
{
    public CustomView()
    {
        MouseEvent += OnMouseEventHandler;
    }
    
    private void OnMouseEventHandler(object sender, Mouse e)
    {
        if (e.Flags.HasFlag(MouseFlags.LeftButtonPressed))
        {
            // Handle drag start
            e.Handled = true;
        }
    }
    
    // Alternative: Override the virtual method
    protected override bool OnMouseEvent(Mouse mouse)
    {
        if (mouse.Flags.HasFlag(MouseFlags.LeftButtonPressed))
        {
            return true; // Handled
        }
        return base.OnMouseEvent(mouse);
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Handling Mouse Clicks[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#handling-mouse-clicks)

**Recommended pattern** - Use [Activating](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Activating.html) event with command context:

```
public class ClickableView : View
{
    public ClickableView()
    {
            Activating += OnActivating;
        }

        private void OnActivating(object sender, CommandEventArgs e)
        {
            if (e.Context?.Binding is MouseBinding { MouseEvent: { } mouse })
            {
                Point clickPosition = mouse.Position; // Viewport-relative

                if (mouse.Flags.HasFlag(MouseFlags.LeftButtonPressed))
                {
                    HandleLeftClick(clickPosition);
                }
                else if (mouse.Flags.HasFlag(MouseFlags.RightButtonPressed))
                {
                    ShowContextMenu(clickPosition);
                }

                e.Handled = true;
            }
        }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
For custom button handling:

```
// Clear defaults and add custom bindings
MouseBindings.Clear();
MouseBindings.Add(MouseFlags.LeftButtonPressed, Command.Activate);
MouseBindings.Add(MouseFlags.RightButtonPressed, Command.Context);

AddCommand(Command.Context, HandleContextMenu);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
Mouse State and Mouse Grab[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-state-and-mouse-grab)
--------------------------------------------------------------------------------------------------------------

### Mouse State[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-state)

The [Mouse State](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.MouseState.html) property tracks the current mouse interaction state:

* **None** - No mouse interaction
* **In** - Mouse over the view's viewport
* **Pressed** - Mouse button pressed while over view
* **PressedOutside** - Button pressed inside but mouse moved outside

Configure which states trigger highlighting:

```
view.MouseHighlightStates = MouseState.In | MouseState.Pressed;

view.MouseStateChanged += (sender, e) => 
{
    switch (e.Value)
    {
        case MouseState.In:
            // Hover appearance
            break;
        case MouseState.Pressed:
            // Pressed appearance
            break;
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Mouse Grab[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-grab)

Views with `MouseHighlightStates` or `MouseHoldRepeat` enabled **automatically grab the mouse** when a button is pressed. For manual grab control, use the `IMouseGrabHandler` interface via [App](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.App.html#Terminal_Gui_ViewBase_View_App)`.Mouse`.

**Grab Lifecycle:**

1. **Press inside** ? Call `GrabMouse(view)` (auto or manual), fires `GrabbingMouse` (cancellable) then `GrabbedMouse`
2. **During grab** ? ALL mouse events routed exclusively to grabbed view with viewport-relative coordinates
3. **Move outside** ? `MouseState |= PressedOutside` (unless `MouseHoldRepeat`)
4. **Release/Click** ? Call `UngrabMouse()`, fires `UnGrabbingMouse` (cancellable) then `UnGrabbedMouse`

**Grabbed View Receives:**

* ALL mouse events (even outside viewport)
* Coordinates converted to viewport-relative (`mouse.Position`)
* `mouse.View` set to grabbed view

**Auto-ungrab occurs when:**

* Button released (via clicked event)
* View disposed (uses `WeakReference<View>` internally)
* Application ends

**Manual Grab Example (for custom drag operations):**

```
protected override bool OnMouseEvent(Mouse mouse)
{
    if (mouse.Flags.HasFlag(MouseFlags.Button1Pressed))
    {
        App?.Mouse.GrabMouse(this);
        _isDragging = true;
        return true;
    }

    if (_isDragging && mouse.Flags.HasFlag(MouseFlags.Button1Released))
    {
        App?.Mouse.UngrabMouse();
        _isDragging = false;
        return true;
    }

    if (_isDragging)
    {
        // mouse.Position is viewport-relative during grab
        UpdateDragPosition(mouse.Position);
        return true;
    }

    return false;
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**Preventing Grab Theft (for complex drag operations):**

```
// Subscribe to prevent other views from stealing the grab during drag
App.Mouse.GrabbingMouse += (sender, e) =>
{
    if (_isDragging && !ReferenceEquals(e.View, this))
    {
        e.Cancel = true; // Prevent other views from grabbing
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Continuous Button Press[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#continuous-button-press)

When `MouseHoldRepeat` is set, the [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) receives repeated events while the button is held:

```
view.MouseHoldRepeat = MouseFlags.LeftButtonReleased;

view.Activating += (s, e) =>
{
    // Called repeatedly while held (~500ms initial, ~50ms intervals)
    DoRepeatAction();
    e.Handled = true;
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
Mouse Coordinate Systems[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-coordinate-systems)
----------------------------------------------------------------------------------------------------------

Mouse coordinates in Terminal.Gui use multiple coordinate systems:

* **Screen Coordinates** - Relative to terminal (0,0 = top-left) - `Mouse.ScreenPosition`
* **Viewport Coordinates** - Relative to view's content area (0,0 = top-left of viewport) - `Mouse.Position`

When handling mouse events in views, use `Position` for viewport-relative coordinates:

```
view.MouseEvent += (s, e) =>
{
    // e.Position is viewport-relative
    if (e.Position.X < 10 && e.Position.Y < 5)
    {
        // Click in top-left corner of viewport
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Coordinate Conversion Methods[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#coordinate-conversion-methods)

Views provide methods to convert between coordinate systems:

```
// Screen ? Viewport
Point viewportPos = view.ScreenToViewport(screenPos);
Point screenPos = view.ViewportToScreen(viewportPos);

// Screen ? Content  
Point contentPos = view.ScreenToContent(screenPos);
Point screenPos = view.ContentToScreen(contentPos);

// Screen ? Frame
Point framePos = view.ScreenToFrame(screenPos);
Rectangle screenRect = view.FrameToScreen();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
Complete Mouse Event Pipeline[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#complete-mouse-event-pipeline)
--------------------------------------------------------------------------------------------------------------------

This section documents the complete flow from raw terminal input to View command execution.

### Stage 1: Terminal Input (ANSI Escape Sequences)[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#stage-1-terminal-input-ansi-escape-sequences)

**Input Format:** SGR Extended Mouse Mode (`ESC[<button;x;yM/m`)

**Example - Single click at column 10, row 5:**

```
Press:   ESC[<0;10;5M    (button=0, x=10, y=5, 'M'=press)
Release: ESC[<0;10;5m    (button=0, x=10, y=5, 'm'=release)
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**Key Points:**

* Coordinates are **1-based** in ANSI (top-left = 1,1)
* `M` terminator = press, `m` terminator = release
* Button codes: 0=left, 1=middle, 2=right, 64/65=wheel
* Modifiers in button code (8=Alt, 16=Ctrl, 4=Shift)

### Stage 2: ANSI Parsing (Ansi Mouse Parser)[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#stage-2-ansi-parsing-ansimouseparser)

**Location:**`Terminal.Gui/Drivers/AnsiHandling/AnsiMouseParser.cs`

**Responsibilities:**

1. Parse ANSI sequence: `\u001b\[<(\d+);(\d+);(\d+)(M|m)`
2. Extract button, x, y, terminator
3. Convert to **0-based** coordinates (subtract 1)
4. Map button code + terminator to [Mouse Flags](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.MouseFlags.html)
5. Extract modifiers
6. Create `Mouse` instance

**Output:**`Mouse { Timestamp=now, ScreenPosition=(9,4), Flags=LeftButtonPressed }`

### Stage 3: Click Synthesis (Mouse Interpreter)[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#stage-3-click-synthesis-mouseinterpreter)

**Location:**`Terminal.Gui/Drivers/MouseInterpreter.cs`

**Responsibilities:**

1. Track press/release pairs ? generate click events
2. Detect multi-clicks (double/triple) based on:
    *Time between clicks (500ms threshold)
    *   Position proximity
    *   Same button

3. Emit synthetic events:
    *Press+Release ? `LeftButtonClicked`
    *   Second click within threshold ? `LeftButtonDoubleClicked`
    *   Third click ? `LeftButtonTripleClicked`

**Key Behavior:**

* Press and Release events pass through immediately
* Click events synthesized immediately after release
* Multi-click detection tracks timing/position/button
* Modifier keys (Shift, Ctrl, Alt) are preserved in synthetic click events

**Output:** Stream of `Mouse` events including synthesized clicks

### Stage 4: Application Routing (Application Mouse)[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#stage-4-application-routing-applicationmouse)

**Location:**`Terminal.Gui/App/Mouse/ApplicationMouse.cs`

**Entry:**`IMouse.RaiseMouseEvent(Mouse mouse)`

**Processing:**

#### 4.1: Find Target View[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#41-find-target-view)

```
List<View?> viewsUnderMouse = App.TopRunnableView.GetViewsUnderLocation(
    mouse.ScreenPosition, 
    ViewportSettingsFlags.TransparentMouse
);
View? deepestView = viewsUnderMouse?.LastOrDefault();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

#### 4.2: Popover Dismissal[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#42-popover-dismissal)

```
if (mouse.IsPressed && 
    App.Popover?.GetActivePopover() is {} popover &&
    !View.IsInHierarchy(popover, deepestView, true))
{
    ApplicationPopover.HideWithQuitCommand(popover);
    RaiseMouseEvent(mouse); // Recurse to handle event below popover
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**Re-show Guard:** When a popover is dismissed, `ApplicationMouse` records the dismissed popover in `DismissedByMousePress` and wraps the recursive `RaiseMouseEvent` call with an `_isDismissRecursing` flag. `ApplicationPopover.Show` checks this guard and silently returns if the caller is trying to re-show the same popover that was just dismissed. This prevents views beneath the popover (e.g., a `DropDownList` toggle button or a `MenuBarItem`) from re-opening the popover during the recursed press event or during the subsequent release/click events in the same mouse interaction cycle (press → release → click). The guard is cleared when the next fresh press event arrives or when the click cycle completes.

#### 4.3: Mouse Grab Handling[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#43-mouse-grab-handling)

```
// If a view has grabbed the mouse, route events exclusively to that view
// HandleMouseGrab converts coordinates to the grabbed view's viewport
// and delivers the event directly, returning true to stop further processing
if (HandleMouseGrab(deepestViewUnderMouse, mouse))
    return; // Grabbed view received the event
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

#### 4.4: Convert to View Coordinates[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#44-convert-to-view-coordinates)

```
Point viewportLocation = deepestView.ScreenToViewport(mouse.ScreenPosition);
Mouse viewMouseEvent = new() {
    Position = viewportLocation,      // Viewport-relative!
    Flags = mouse.Flags,
    ScreenPosition = mouse.ScreenPosition,
    View = deepestView
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

#### 4.5: Raise Mouse Enter/Leave[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#45-raise-mouseenterleave)

```
RaiseMouseEnterLeaveEvents(mouse.ScreenPosition, viewsUnderMouse);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

#### 4.6: Send to View[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#46-send-to-view)

```
deepestView.NewMouseEvent(viewMouseEvent);
// If not handled, propagate to SuperView
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Stage 5: View Processing (View.New Mouse Event)[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#stage-5-view-processing-viewnewmouseevent)

**Location:**`Terminal.Gui/ViewBase/View.Mouse.cs`

**Entry:**`View.NewMouseEvent(Mouse mouse)`

#### 5.1: Pre-conditions[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#51-pre-conditions)

```
if (!Enabled) return false;
if (!CanBeVisible(this)) return false;
if (!MousePositionTracking && mouse.Flags == MouseFlags.PositionReport) 
    return false;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

#### 5.2: Low-Level Mouse Event[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#52-low-level-mouseevent)

```
if (RaiseMouseEvent(mouse) || mouse.Handled)
    return true;  // View handled via OnMouseEvent or subscriber
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

#### 5.3: Mouse Grab Handling[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#53-mouse-grab-handling)

**Conditions:**`MouseHighlightStates != None` OR `MouseHoldRepeat.HasValue`

**On Pressed:**

```
if (!App.Mouse.IsGrabbed(this))
{
    // GrabbingMouse event fires first (can be cancelled)
    // If not cancelled, GrabbedMouse event fires
    App.Mouse.GrabMouse(this);
}
if (!HasFocus && CanFocus) SetFocus();

if (mouse.Position in Viewport)
    MouseState |= MouseState.Pressed;
else if (!MouseHoldRepeat)
    MouseState |= MouseState.PressedOutside;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**On Released:**

```
MouseState &= ~MouseState.Pressed;
MouseState &= ~MouseState.PressedOutside;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**On Clicked:**

```
if (App.Mouse.IsGrabbed(this))
{
    // UnGrabbingMouse event fires first (can be cancelled)
    // If not cancelled, UnGrabbedMouse event fires
    // MouseEnter/Leave events update for views under current mouse position
    App.Mouse.UngrabMouse();
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

#### 5.4: Invoke Commands via Mouse Bindings[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#54-invoke-commands-via-mousebindings)

```
if (MouseBindings.TryGet(mouse.Flags, out binding))
{
    binding.MouseEventArgs = mouse;
    InvokeCommands(binding.Commands, binding);
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**Default Bindings:**

* `LeftButtonPressed` ? `Command.Activate`
* `LeftButtonPressed | Ctrl` ? `Command.Context`

#### 5.5: Command Execution[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#55-command-execution)

See [Command Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/command.html) for details.

**Example - LeftButtonPressed ? Command.Activate:**

```
InvokeCommand(Command.Activate, context):
    OnActivating(args) || args.Cancel  // Subclass override
    Activating?.Invoke(this, args)     // Event subscribers
    if (!args.Cancel && CanFocus) SetFocus();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Driver Architecture[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#driver-architecture)

**Platform-Specific Input:**

* **Windows**: `WindowsInputProcessor` - `ReadConsoleInput()` ? direct `Mouse` conversion
* **Unix/ANSI**: ANSI escape sequence parsing pipeline

**Input Processing:**

```
Platform API ? InputProcessorImpl ? AnsiResponseParser ? MouseInterpreter ? Application
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
This ensures consistent mouse behavior across platforms while maintaining platform-specific optimizations.

Best Practices[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#best-practices)
--------------------------------------------------------------------------------------

* **Use Mouse Bindings and Commands** for simple interactions - integrates with keyboard bindings
* **Use [Activating](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Activating.html) event** to handle clicks - provides mouse position via CommandContext
* **Access mouse details via CommandContext:**

```
if (e.Context?.Binding is MouseBinding { MouseEvent: { } mouse })
{
    Point pos = mouse.Position;  // Viewport-relative
    MouseFlags flags = mouse.Flags;
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

* **Handle MouseEvent directly** only for complex scenarios (drag-and-drop, custom gestures)
* **Use `MouseHighlightStates`** for automatic grab and visual feedback
* **Use `MouseHoldRepeat`** for repeating actions (scroll buttons, spinners)
* **Respect platform conventions** - right-click for menus, double-click for default actions
* **Provide keyboard alternatives** - essential for accessibility
* **Test with different terminals** - mouse support varies

Testing Mouse Input[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#testing-mouse-input)
------------------------------------------------------------------------------------------------

> **For comprehensive documentation,** see **[Input Injection](https://gui-cs.github.io/Terminal.Gui/docs/input-injection.html)**.

Terminal.Gui provides sophisticated input injection for testing without hardware:

### Quick Test Example (Using Helper Methods)[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#quick-test-example-using-helper-methods)

**Recommended approach** - Use helper methods for cleaner test code:

```
using IApplication app = Application.Create();
app.Init(DriverRegistry.Names.ANSI);

// Inject a left click - simple and clear
app.InjectSequence(InputInjectionExtensions.LeftButtonClick(new Point(10, 5)));

// Inject a right click
app.InjectSequence(InputInjectionExtensions.RightButtonClick(new Point(10, 5)));

// Inject a double-click
app.InjectSequence(InputInjectionExtensions.LeftButtonDoubleClick(new Point(10, 5)));
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**Alternative approach** - Manual event creation for advanced scenarios:

```
VirtualTimeProvider time = new();
using IApplication app = Application.Create(time);
app.Init(DriverRegistry.Names.ANSI);

// Inject click manually
app.InjectMouse(new() { 
    ScreenPosition = new(10, 5), 
    Flags = MouseFlags.LeftButtonPressed 
});
app.InjectMouse(new() { 
    ScreenPosition = new(10, 5), 
    Flags = MouseFlags.LeftButtonReleased 
});
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Testing Double-Click with Virtual Time[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#testing-double-click-with-virtual-time)

**Using helper method** (recommended):

```
using IApplication app = Application.Create();
app.Init(DriverRegistry.Names.ANSI);

// One line for a complete double-click
app.InjectSequence(InputInjectionExtensions.LeftButtonDoubleClick(new Point(10, 5)));
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
**Manual approach** (for custom timing control):

```
VirtualTimeProvider time = new();
time.SetTime(new DateTime(2025, 1, 1, 12, 0, 0));
using IApplication app = Application.Create(time);
app.Init(DriverRegistry.Names.ANSI);

// First click
app.InjectMouse(new() { 
    ScreenPosition = new(10, 5), 
    Flags = MouseFlags.LeftButtonPressed,
    Timestamp = time.Now 
});
time.Advance(TimeSpan.FromMilliseconds(50));
app.InjectMouse(new() { 
    ScreenPosition = new(10, 5), 
    Flags = MouseFlags.LeftButtonReleased,
    Timestamp = time.Now 
});

// Second click within threshold
time.Advance(TimeSpan.FromMilliseconds(250));
app.InjectMouse(new() { 
    ScreenPosition = new(10, 5), 
    Flags = MouseFlags.LeftButtonPressed,
    Timestamp = time.Now 
});
time.Advance(TimeSpan.FromMilliseconds(50));
app.InjectMouse(new() { 
    ScreenPosition = new(10, 5), 
    Flags = MouseFlags.LeftButtonReleased,
    Timestamp = time.Now 
});
// Double-click detected!
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")

### Mouse Click Helper Methods[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-click-helper-methods)

Terminal.Gui provides three helper methods in `InputInjectionExtensions` to simplify common mouse click patterns:

* **`LeftButtonClick(Point p)`** - Single left click (Press + Release)
* **`RightButtonClick(Point p)`** - Single right click (Press + Release)
* **`LeftButtonDoubleClick(Point p)`** - Double left click (two complete click sequences)

**Benefits:**

* Reduces boilerplate from 2-4 lines to 1 line
* Built-in appropriate delays for reliable click detection
* Clearer test intent
* Fewer errors from mismatched Press/Release pairs

### Key Testing Features[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#key-testing-features)

* **Virtual Time Control** - Deterministic multi-click timing
* **Helper Methods** - `InputInjectionExtensions.LeftButtonClick()`, etc. for simplified injection
* **Single-Call Injection** - `app.InjectMouse(mouse)` handles everything
* **No Real Delays** - Tests run instantly with virtual time
* **Two Modes** - Direct (fast) and Pipeline (full ANSI encoding)

**Learn More:** See **[Input Injection](https://gui-cs.github.io/Terminal.Gui/docs/input-injection.html)** for complete documentation.

Limitations and Considerations[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#limitations-and-considerations)
----------------------------------------------------------------------------------------------------------------------

* **Terminal Support** - Not all terminals support mouse input; always provide keyboard alternatives
* **Mouse Wheel** - Support varies between platforms and terminals
* **Mouse Buttons** - Some terminals may not support all buttons or modifier keys
* **Coordinate Precision** - Limited to character cell boundaries; no sub-character precision
* **Performance** - Excessive mouse move tracking can impact performance; use Enter/Leave events when appropriate
* **Accessibility** - Mouse-only features exclude keyboard-only users

Global Mouse Handling[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#global-mouse-handling)
----------------------------------------------------------------------------------------------------

Handle mouse events application-wide before views process them:

```
App.Mouse.MouseEvent += (sender, e) => 
{
    // Application-wide handling
    if (e.Flags.HasFlag(MouseFlags.RightButtonClicked))
    {
        ShowGlobalContextMenu(e.Position);
        e.Handled = true;
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
Mouse Enter/Leave Events[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-enterleave-events)
---------------------------------------------------------------------------------------------------------

Views can respond when the mouse enters or exits:

```
view.MouseEnter += (sender, e) => 
{
    UpdateTooltip("Hovering");
};

view.MouseLeave += (sender, e) => 
{
    HideTooltip();
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
These events work with [Mouse State](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.MouseState.html) to enable hover effects and visual feedback.

See Also[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#see-also)
--------------------------------------------------------------------------

* [Command System](https://gui-cs.github.io/Terminal.Gui/docs/command.html) - Understanding how commands work with mouse events
* [Input Injection](https://gui-cs.github.io/Terminal.Gui/docs/input-injection.html) - Complete testing documentation
* [View Layout](https://gui-cs.github.io/Terminal.Gui/docs/layout.html) - Understanding coordinate systems and layout
* [Cancellable Work Pattern](https://gui-cs.github.io/Terminal.Gui/docs/cancellable-work-pattern.html) - Event processing pattern
* `IMouseGrabHandler` - API reference for mouse grab handling
* `IMouse` - API reference for the mouse interface

Mouse Tracing[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html#mouse-tracing)
------------------------------------------------------------------------------------

For debugging mouse event flow, use the `Trace` class from the `Terminal.Gui.Tracing` namespace:

```
using Terminal.Gui.Tracing;

Trace.MouseEnabled = true;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html# "Copy")
When enabled, mouse events are logged via `Logging.Trace` showing the flow from Driver → Application → View. Enable via:

* **Code**: `Trace.MouseEnabled = true;`
* **Config**: `"Trace.MouseEnabled": true`
* **UICatalog**: Logging menu → Mouse Trace

See [Logging - View Event Tracing](https://gui-cs.github.io/Terminal.Gui/docs/logging.html#view-event-tracing) for more details.
