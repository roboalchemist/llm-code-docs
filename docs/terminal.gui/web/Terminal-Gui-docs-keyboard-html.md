# Source: https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html

Title: Keyboard Deep Dive | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html

Published Time: Fri, 13 Mar 2026 23:38:23 GMT

Markdown Content:
See Also[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#see-also)
-----------------------------------------------------------------------------

* [Cancellable Work Pattern](https://gui-cs.github.io/Terminal.Gui/docs/cancellable-work-pattern.html)
* [Command Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/command.html)
* [Mouse Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html)
* [Lexicon & Taxonomy](https://gui-cs.github.io/Terminal.Gui/docs/lexicon.html)

Tenets for Terminal.Gui Keyboard Handling (Unless you know better ones...)[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#tenets-for-terminalgui-keyboard-handling-unless-you-know-better-ones)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tenets higher in the list have precedence over tenets lower in the list.

* **Users Have Control** - _Terminal.Gui_ provides default key bindings consistent with these tenets, but those defaults are configurable by the user. For example, [Configuration Manager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationManager.html) allows users to redefine key bindings for the system, a user, or an application.

* **More Editor than Command Line** - Once a _Terminal.Gui_ app starts, the user is no longer using the command line. Users expect keyboard idioms in TUI apps to be consistent with GUI apps (such as VS Code, Vim, and Emacs). For example, in almost all GUI apps, `Ctrl+V` is `Paste`. But the Linux shells often use `Shift+Insert`. _Terminal.Gui_ binds `Ctrl+V` by default.

* **Be Consistent With the User's Platform** - Users get to choose the platform they run _Terminal.Gui_ apps on and those apps should respond to keyboard input in a way that is consistent with the platform. For example, on Windows to erase a word to the left, users press `Ctrl+Backspace`. But on Linux, `Ctrl+W` is used.

* **The Source of Truth is Wikipedia** - We use this [Wikipedia article](https://en.wikipedia.org/wiki/Table_of_keyboard_shortcuts) as our guide for default key bindings.

* **If It's Hot, It Works** - If a [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) with a [Hot Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.HotKey.html#Terminal_Gui_ViewBase_View_HotKey) is visible, and the HotKey is visible, the user should be able to press that HotKey and whatever behavior is defined for it should work. For example, in v1, when a Modal view was active, the HotKeys on [Menu Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBar.html) continued to show "hot". In v2 we strive to ensure this doesn't happen.

Keyboard APIs[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#keyboard-apis)
---------------------------------------------------------------------------------------

_Terminal.Gui_ provides the following APIs for handling keyboard input:

* **Key** - [Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Key.html) provides a platform-independent abstraction for common keyboard operations. It is used for processing keyboard input and raising keyboard events. This class provides a high-level abstraction with helper methods and properties for common keyboard operations. Use this class instead of the low-level `KeyCode` enum when possible. `Key` also carries rich metadata:
  * `EventType` — `KeyEventType.Press` (default), `KeyEventType.Repeat`, or `KeyEventType.Release`. Defaults to `Press` so existing code is unaffected. Does not participate in equality.
  * `ModifierKey` — identifies standalone modifier key events (e.g. `ModifierKey.LeftShift`, `ModifierKey.RightCtrl`). Defaults to `ModifierKey.None`.
  * `IsModifierOnly` — `true` when `ModifierKey != ModifierKey.None`, indicating a standalone modifier key press/release with no accompanying character key.
  * `ShiftedKeyCode` — the key code that would be produced with the current modifier state (e.g. Shift+2 on US layout → `(KeyCode)'@'`). Reported by the kitty keyboard protocol when alternate key reporting is enabled (flag 4). Defaults to `KeyCode.Null`. Does not participate in equality.
  * `BaseLayoutKeyCode` — the key code corresponding to the physical key in the standard (US) keyboard layout, regardless of the active input language or modifier state. Reported by the kitty keyboard protocol when alternate key reporting is enabled (flag 4). Defaults to `KeyCode.Null`. Does not participate in equality.

* **Key Bindings** - Key Bindings provide a declarative method for handling keyboard input in [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) implementations. The View calls `AddCommand()`(Terminal.Gui.Command,System.Func{System.Nullable{System.Boolean}}) to declare it supports a particular command and then uses [Key Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.KeyBindings.html) to indicate which key presses will invoke the command.
* **Key Events** - The Key Bindings API is rich enough to support the vast majority of use-cases. However, in some cases subscribing directly to key events is needed (e.g. when capturing arbitrary typing by a user). Use `KeyDown` and `KeyUp` events in these cases.

Each of these APIs are described more fully below.

### **[Key Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.KeyBindings.html)**[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#key-bindings)

Key Bindings is the preferred way of handling keyboard input in [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) implementations. The View calls `AddCommand()`(Terminal.Gui.Command,System.Func{System.Nullable{System.Boolean}}) to declare it supports a particular command and then uses [Key Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.KeyBindings.html) to indicate which key presses will invoke the command. For example, if a [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) wants to respond to the user pressing the up arrow key to scroll up it would do this

```
public MyView : View
{
  AddCommand (Command.ScrollUp, () => ScrollVertical (-1));
  KeyBindings.Add (Key.CursorUp, Command.ScrollUp);
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
The `Character Map` Scenario includes a View called `CharMap` that is a good example of the Key Bindings API.

The [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html) enum lists generic operations that are implemented by views. For example [Accept](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html#Terminal_Gui_Input_Command_Accept) in a [Button](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Button.html) results in the [Accepting](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Accepting.html) event firing while in `TableView` it is bound to `CellActivated`. Not all commands are implemented by all views (e.g. you cannot scroll in a [Button](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Button.html)). Use the `GetSupportedCommands()` method to determine which commands are implemented by a [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html).

The default key for activating a button is `Space`. You can change this using `KeyBindings.ReplaceKey()`:

```
var btn = new Button () { Title = "Press me" };
btn.KeyBindings.ReplaceKey (btn.KeyBindings.GetKeyFromCommands (Command.Accept));
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
Key Bindings can be added at the [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html) or [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) level.

For **Application-scoped Key Bindings** there are two categories of Application-scoped Key Bindings:

1. **Application Command Key Bindings** - Bindings for [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html)s supported by [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html). For example, `Application.GetDefaultKey (Command.Quit)`, which is bound to `Command.Quit` in `Application.DefaultKeyBindings` and results in [Request Stop(IRunnable?)](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.RequestStop.html#Terminal_Gui_App_Application_RequestStop_Terminal_Gui_App_IRunnable_) being called.
2. **Application Key Bindings** - Bindings for [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html)s supported on arbitrary [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)s that are meant to be invoked regardless of which part of the application is visible/active.

Use `Application.Keyboard.KeyBindings` to add or modify Application-scoped Key Bindings. For backward compatibility, `Application.KeyBindings` also provides access to the same key bindings.

**View-scoped Key Bindings** also have two categories:

1. **HotKey Bindings** - These bind to [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html)s that will be invoked regardless of whether the [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) has focus or not. The most common use-case for `HotKey` bindings is [Hot Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.HotKey.html#Terminal_Gui_ViewBase_View_HotKey). For example, a [Button](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Button.html) with a `Title` of `_OK`, the user can press `Alt-O` and the button will be accepted regardless of whether it has focus or not. Add and modify HotKey bindings with `HotKeyBindings`.
2. **Focused Bindings** - These bind to [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html)s that will be invoked only when the [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) has focus. Focused Key Bindings are the easiest way to enable a [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) to support responding to key events. Add and modify Focused bindings with [Key Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.KeyBindings.html).

**Application-Scoped** Key Bindings

### Hot Key[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#hotkey)

A **HotKey** is a key press that selects a visible UI item. For selecting items across [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)s (e.g. a [Button](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Button.html) in a [Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Dialog.html)) the key press must have the `Alt` modifier. For selecting items within a [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) that are not [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)s themselves, the key press can be key without the `Alt` modifier. For example, in a [Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Dialog.html), a [Button](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Button.html) with the text of "_Text" can be selected with `Alt+T`. Or, in a `Menu` with "_File _Edit", `Alt+F` will select (show) the Strings.menuFile menu. If the Strings.menuFile menu has a sub-menu of Strings.cmdNew `Alt+N` or `N` will ONLY select the Strings.cmdNew sub-menu if the Strings.menuFile menu is already opened.

By default, the `Text` of a [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) is used to determine the [Hot Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.HotKey.html#Terminal_Gui_ViewBase_View_HotKey) by looking for the first occurrence of the `HotKeySpecifier` (which is underscore (`_`) by default). The character following the underscore is the [Hot Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.HotKey.html#Terminal_Gui_ViewBase_View_HotKey). If the `HotKeySpecifier` is not found in `Text`, the first character of `Text` is used as the [Hot Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.HotKey.html#Terminal_Gui_ViewBase_View_HotKey). The `Text` of a [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) can be changed at runtime, and the [Hot Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.HotKey.html#Terminal_Gui_ViewBase_View_HotKey) will be updated accordingly. @"Terminal.Gui.View.HotKey" is `virtual` enabling this behavior to be customized.

### **Shortcut**[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#shortcut)

A **Shortcut** is an opinionated (visually & API) [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) for displaying a command, help text, key key press that invokes a [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html).

The [Command](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Command.html) can be invoked even if the [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) that defines them is not focused or visible (but the [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) must be enabled). [Shortcut](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Shortcut.html)s can be any key press; `Key.A`, `Key.A.WithCtrl`, `Key.A.WithCtrl.WithAlt`, `Key.Del`, and `Key.F1`, are all valid.

[Shortcut](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Shortcut.html)s are used to define application-wide actions or actions that are not visible (e.g. `Copy`).

[MenuBar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBar.html), [PopoverMenu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.PopoverMenu.html), and [StatusBar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.StatusBar.html) support [Shortcut](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Shortcut.html)s.

### **Key Events**[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#key-events)

Keyboard events are retrieved from [Drivers](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html) each iteration of the [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html)[Main Loop](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html). The driver raises `IDriver.KeyDown` for press/repeat events and `IDriver.KeyUp` for release events.

[Raise Key Down Event(Key)](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.RaiseKeyDownEvent.html#Terminal_Gui_App_Application_RaiseKeyDownEvent_Terminal_Gui_Input_Key_) raises `Application.KeyDown` and then calls `NewKeyDownEvent()` on all runnable [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)s. If no [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) handles the key event, any Application-scoped key bindings will be invoked. Application-scoped key bindings are managed through `Application.Keyboard.KeyBindings`.

`Application.Keyboard.KeyUp` fires for key release events. It routes through the focused view hierarchy via `View.NewKeyUpEvent()` → `View.OnKeyUp()` → `View.KeyUp`. Key bindings are not invoked for key-up events.

##### Note

`KeyUp` events are only raised when the driver provides release information. The ANSI driver reports key releases when the terminal supports the [kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) with event type reporting (flag 2). Terminals that do not support kitty, or drivers that do not implement key-up (e.g. Windows, DotNet), simply never raise `KeyUp`.

If a view is enabled, the `NewKeyDownEvent()` method will do the following:

1. If the view has a subview that has focus, 'NewKeyDown' on the focused view will be called. This is recursive. If the most-focused view handles the key press, processing stops.
2. If there is no most-focused sub-view, or a most-focused sub-view does not handle the key press, `OnKeyDown()` will be called. If the view handles the key press, processing stops.
3. If `OnKeyDown()` does not handle the event. `KeyDown` will be raised.
4. If the view does not handle the key down event, any bindings for the key will be invoked (see the [Key Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.KeyBindings.html) property). If the key is bound and any of it's command handlers return true, processing stops.
5. If the key is not bound, or the bound command handlers do not return true, `OnKeyDownNotHandled()` is called.

**Application Key Handling**[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#application-key-handling)
-----------------------------------------------------------------------------------------------------------------

To define application key handling logic for an entire application in cases where the methods listed above are not suitable, use the `Application.KeyDown` event.

**Key Down/Up Events**[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#key-downup-events)
----------------------------------------------------------------------------------------------------

_Terminal.Gui_ supports both key down and key up events:

* `KeyDown` — raised for press and repeat events. This is the primary keyboard event used by most code.
* `KeyUp` — raised for release events. Only available when the driver supports it (currently the ANSI driver with kitty keyboard protocol).

Both events carry a [Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Key.html) whose `EventType` property indicates `Press`, `Repeat`, or `Release`. The `EventType` defaults to `Press` and does not affect equality, so existing code that compares keys is unaffected.

**Kitty Keyboard Protocol**[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#kitty-keyboard-protocol)
---------------------------------------------------------------------------------------------------------------

Terminal.Gui uses the [kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) to enable enhanced keyboard capabilities when running under a supporting terminal (e.g. Windows Terminal, kitty, WezTerm, foot, Ghostty). The protocol is opt-in: the ANSI driver negotiates it at startup and falls back to legacy parsing when unsupported.

### Flags and Capabilities[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#flags-and-capabilities)

The protocol defines progressive enhancement flags, represented by the [Kitty Keyboard Flags](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drivers.KittyKeyboardFlags.html) enum:

| Flag | Value | Description |
| --- | --- | --- |
| `DisambiguateEscapeCodes` | 1 | Encodes keys unambiguously as CSI u sequences instead of legacy escape sequences. |
| `ReportEventTypes` | 2 | Reports press, repeat, and release events. Enables `KeyUp` and repeat `KeyDown` events. |
| `ReportAlternateKeys` | 4 | Reports shifted and base-layout key codes alongside the primary key code. |
| `ReportAllKeysAsEscapeCodes` | 8 | Reports standalone modifier key events (e.g. pressing Shift alone). |
| `ReportAssociatedText` | 16 | Reports the text generated by a key event (not yet implemented). |

Terminal.Gui currently requests flags 1 through 8 (value `15`) from the terminal. The terminal may grant a subset of these based on its capabilities.

### Alternate Key Reporting (Flag 4)[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#alternate-key-reporting-flag-4)

When the terminal supports flag 4 (`ReportAlternateKeys`), key events include additional information in two `Key` properties:

* **`ShiftedKeyCode`** — The key code produced by applying the current modifier state. For example, pressing Shift+`2` on a US keyboard reports `ShiftedKeyCode = (KeyCode)'@'`. This is useful for responding to the actual character a user sees rather than the unshifted base key.

* **`BaseLayoutKeyCode`** — The key code for the physical key in the standard US layout, regardless of the active keyboard language. For example, on a French AZERTY keyboard, pressing the physical "A" key (which types "Q" on AZERTY) would report `BaseLayoutKeyCode = (KeyCode)'a'`. This enables keyboard shortcuts that work by physical position rather than by label.

Both default to `KeyCode.Null` when the terminal does not report alternate keys (or doesn't support flag 4). Neither property participates in equality comparisons — two `Key` instances are equal if their `KeyCode` matches, regardless of alternate key data.

#### Kitty CSI u Format[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#kitty-csi-u-format)

The kitty protocol encodes key events as:

```
CSI code:shifted:base ; modifiers:eventtype u
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
For example, pressing Shift+`a` might produce `\x1b[97:65:97;2u` meaning:

* `97` — primary key code (lowercase `a`)
* `65` — shifted key code (uppercase `A`)
* `97` — base layout key code (lowercase `a` in US layout)
* `2` — modifier (Shift)

#### Example Usage[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#example-usage)

**NOTE:** Developers are encouraged to use `KeyBinding` for most keyboard input handling. These examples show direct use of `KeyDown` for scenarios where `KeyBinding` is not suitable (e.g. arbitrary text input) and demonstrate how to access alternate key data when available.

```
// Respond to physical key position regardless of keyboard layout
view.KeyDown += (s, key) =>
{
    if (key.BaseLayoutKeyCode != KeyCode.Null)
    {
        // Use the US-layout key for positional shortcuts (e.g. WASD)
        switch (key.BaseLayoutKeyCode)
        {
            case (KeyCode)'w': MoveUp (); break;
            case (KeyCode)'a': MoveLeft (); break;
            case (KeyCode)'s': MoveDown (); break;
            case (KeyCode)'d': MoveRight (); break;
        }
    }
};

// Respond to the shifted character
view.KeyDown += (s, key) =>
{
    if (key.ShiftedKeyCode != KeyCode.Null)
    {
        // ShiftedKeyCode tells you what character the shift state actually produces
        Debug.WriteLine ($"Shifted key: {key.ShiftedKeyCode}");
    }
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
General input model
-------------------

* The driver generates `KeyDown` events (for press and repeat) and `KeyUp` events (for release, when supported).

* [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) implementations subscribe to driver `KeyDown`/`KeyUp` events and forward them to the most-focused `Runnable` view using `View.NewKeyDownEvent` or `View.NewKeyUpEvent` respectively.

* The base ([View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)) implementation of `NewKeyDownEvent` follows a pattern of "Before", "During", and "After" processing:

  * **Before**
    * If `Enabled == false` that view should _never_ see keyboard (or mouse input).
    * `NewKeyDownEvent` is called on the most-focused SubView (if any) that has focus. If that call returns true, the method returns.
    * Calls `OnKeyDown`.

  * **During**
    * Assuming `OnKeyDown` call returns false (indicating the key wasn't handled) any commands bound to the key will be invoked.

  * **After**
    * Assuming no keybinding was found or all invoked commands were not handled:
      * `OnKeyDownNotHandled` is called to process the key.
      * `KeyDownNotHandled` is raised.

* Subclasses of [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) can (rarely) override `OnKeyDown` (or subscribe to `KeyDown`) to see keys before they are processed

* Subclasses of [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) can (often) override `OnKeyDownNotHandled` to do key processing for keys that were not previously handled. [Text Field](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TextField.html) and [Text View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TextView.html) are examples.

Application[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#application)
-----------------------------------------------------------------------------------

* Implements support for `KeyBindingScope.Application`.
* Keyboard functionality is now encapsulated in the [IKeyboard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IKeyboard.html) interface, accessed via `Application.Keyboard`.
* `Application.Keyboard` provides access to [Key Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.KeyBindings.html), key binding configuration (via `Application.DefaultKeyBindings` for commands like `Command.Quit`, `Command.Arrange`, and navigation commands), and keyboard event handling.
* For backward compatibility, [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html) still exposes static properties/methods that delegate to `Application.Keyboard` (e.g., `IApplication.KeyBindings`, `IApplication.RaiseKeyDownEvent`).
* Exposes cancelable `KeyDown` events (via `Handled = true`). The `RaiseKeyDownEvent` method is public and can be used to simulate keyboard input, although it is preferred to use `InputInjector` for testing.
* The [IKeyboard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IKeyboard.html) interface enables testability with isolated keyboard instances that don't depend on static Application state.

View[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#view)
---------------------------------------------------------------------

* Implements support for [Key Bindings](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.KeyBindings.html) and `HotKeyBindings`.
* Exposes cancelable non-virtual method for a new key event: `NewKeyDownEvent`.
* Exposes cancelable virtual methods for a new key event: `OnKeyDown`. This method is called by `NewKeyDownEvent` and can be overridden to handle keyboard input.

IKeyboard Architecture[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#ikeyboard-architecture)
---------------------------------------------------------------------------------------------------------

The [IKeyboard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IKeyboard.html) interface provides a decoupled, testable architecture for keyboard handling in Terminal.Gui. This design allows for:

### Key Features[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#key-features)

1. **Decoupled State** - All keyboard-related state (key bindings, navigation keys, events) is encapsulated in [IKeyboard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IKeyboard.html), separate from the static [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html) class.

2. **Dependency Injection** - The `Keyboard` implementation receives an [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) reference, enabling it to interact with application state without static dependencies.

3. **Testability** - Unit tests can create isolated [IKeyboard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IKeyboard.html) instances with mock [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) references, enabling parallel test execution without interference.

4. **Backward Compatibility** - All existing [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html) keyboard APIs (e.g., `Application.KeyBindings`, `Application.RaiseKeyDownEvent`) remain available and delegate to `Application.Keyboard`. Application-level command keys are configured via `Application.DefaultKeyBindings`.

### Usage Examples[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#usage-examples)

**Accessing keyboard functionality:**

```
App.Keyboard.KeyBindings.Add(Key.F1, Command.HotKey);
App.Keyboard.RaiseKeyDownEvent(Key.Enter);
Application.DefaultKeyBindings[Command.Quit] = Bind.All (Key.Q.WithCtrl);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
**Testing with isolated keyboard instances:**

```
// Create independent keyboard instances for parallel tests
var keyboard1 = new ApplicationKeyboard ();
keyboard1.KeyBindings.Add (Key.Q.WithCtrl, Command.Quit);

var keyboard2 = new ApplicationKeyboard ();
keyboard2.KeyBindings.Add (Key.X.WithCtrl, Command.Quit);

// keyboard1 and keyboard2 maintain completely separate KeyBindings
Assert.True (keyboard1.KeyBindings.TryGet (Key.Q.WithCtrl, out _));
Assert.True (keyboard2.KeyBindings.TryGet (Key.X.WithCtrl, out _));
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
**Accessing application context from views:**

```
public class MyView : View
{
    protected override bool OnKeyDown(Key key)
    {
        // Use View.App instead of static Application
        if (key == Key.F1)
        {
            App?.Keyboard?.KeyBindings.Add(Key.F2, Command.Accept);
            return true;
        }
        return base.OnKeyDown(key);
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")

### Architecture Benefits[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#architecture-benefits)

* **Parallel Testing**: Multiple test methods can create and use separate [IKeyboard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IKeyboard.html) instances simultaneously without state interference.
* **Dependency Inversion**: `Keyboard` depends on [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) interface rather than static [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html) class.
* **Cleaner Code**: Keyboard functionality is organized in a dedicated interface rather than scattered across [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html) partial classes.
* **Mockability**: Tests can provide mock [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) implementations to test keyboard behavior in isolation.

### Implementation Details[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#implementation-details)

The `Keyboard` class implements [IKeyboard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IKeyboard.html) and maintains:

* **KeyBindings**: Application-scoped key binding dictionary
* **Navigation Keys**: Configured via Application.DefaultKeyBindings dictionary (Quit, Arrange, NextTabStop, PreviousTabStop, NextTabGroup, PreviousTabGroup, Refresh, Suspend)
* **Events**: `KeyDown` and `KeyUp` events for application-level keyboard monitoring
* **Command Implementations**: Handlers for Application-scoped commands (Quit, Suspend, Navigation, Refresh, Arrange)

The [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) implementations create and manage the [IKeyboard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IKeyboard.html) instance, setting its `IApplication` property to `this` to provide the necessary [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html) reference.

Testing Keyboard Input[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#testing-keyboard-input)
---------------------------------------------------------------------------------------------------------

> **For comprehensive documentation on testing,** see **[Input Injection](https://gui-cs.github.io/Terminal.Gui/docs/input-injection.html)**.

Terminal.Gui provides a sophisticated input injection system for testing keyboard behavior without requiring actual keyboard hardware. Here's a quick overview:

### Quick Test Example[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#quick-test-example)

```
// Create application with virtual time for deterministic testing
VirtualTimeProvider time = new();
using IApplication app = Application.Create(time);
app.Init(DriverRegistry.Names.ANSI);

// Subscribe to key events
app.Keyboard.KeyDown += (s, e) => Console.WriteLine($"Key: {e}");

// Inject keys
app.InjectKey(Key.A);
app.InjectKey(Key.Enter);
app.InjectKey(Key.Esc);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")

### Testing Key Commands[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#testing-key-commands)

```
VirtualTimeProvider time = new();
using IApplication app = Application.Create(time);
app.Init(DriverRegistry.Names.ANSI);

Button button = new() { Text = "_Click Me" };
bool acceptingCalled = false;
button.Accepting += (s, e) => acceptingCalled = true;

IRunnable runnable = new Runnable();
(runnable as View)?.Add(button);
app.Begin(runnable);

// Inject hotkey (Alt+C)
app.InjectKey(Key.C.WithAlt);

Assert.True(acceptingCalled);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")

### Testing Escape Sequences with Pipeline Mode[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#testing-escape-sequences-with-pipeline-mode)

```
// Pipeline mode tests full ANSI encoding/decoding
VirtualTimeProvider time = new();
using IApplication app = Application.Create(time);
app.Init(DriverRegistry.Names.ANSI);

IInputInjector injector = app.GetInputInjector();
InputInjectionOptions options = new() { Mode = InputInjectionMode.Pipeline };

// This encodes Key.F1 ? "\x1b[OP", injects chars, parses back to Key.F1
injector.InjectKey(Key.F1, options);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")

### Key Testing Features[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#key-testing-features)

* **Virtual Time Control** - Deterministic timing for escape sequence handling
* **Single-Call Injection** - `app.InjectKey(key)` handles everything
* **No Real Delays** - Tests run instantly using virtual time
* **Two Modes** - Direct (default, fast) and Pipeline (full ANSI encoding)
* **Escape Sequence Handling** - Automatic release of stale escapes

**Learn More:** See **[Input Injection](https://gui-cs.github.io/Terminal.Gui/docs/input-injection.html)** for complete documentation including:

* Architecture and design
* Testing patterns and best practices
* Advanced scenarios (modifier keys, function keys, special keys)
* Troubleshooting guide

Configurable Key Bindings[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#configurable-key-bindings)
---------------------------------------------------------------------------------------------------------------

Terminal.Gui uses a layered, platform-aware key binding architecture. All default key bindings are defined declaratively using `PlatformKeyBinding` records and can be overridden via [ConfigurationManager](https://gui-cs.github.io/Terminal.Gui/docs/config.html).

### Three Layers[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#three-layers)

Key bindings are organized in three layers, applied from lowest to highest priority:

1. **`Application.DefaultKeyBindings`** - Application-wide bindings for commands like Quit, Suspend, Arrange, and tab navigation. This is a `[ConfigurationProperty]` and can be overridden via configuration.

2. **`View.DefaultKeyBindings`** - Shared base bindings for all views, covering navigation (cursor keys, Home, End), clipboard (Copy, Cut, Paste), and editing (Undo, Redo, Delete). This is also a `[ConfigurationProperty]`.

3. **Per-view `DefaultKeyBindings`** - View-specific bindings that layer on top of the base. For example, `TextField.DefaultKeyBindings` adds Emacs-style navigation (`Ctrl+B`, `Ctrl+F`), word movement (`Ctrl+CursorLeft`), and kill commands (`Ctrl+K`). These are plain static properties, not configurable via ConfigurationManager.

Each view's constructor calls `ApplyKeyBindings (View.DefaultKeyBindings, <ViewType>.DefaultKeyBindings)` to combine the layers. Only commands that the view actually supports (via `GetSupportedCommands ()`) are bound. Keys already bound by a lower layer are not overwritten by a higher layer.

### Platform-Aware Bindings[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#platform-aware-bindings)

Key bindings can vary by operating system using the `PlatformKeyBinding` record:

```
public record PlatformKeyBinding
{
    public string []? All { get; init; }      // All platforms
    public string []? Windows { get; init; }  // Windows only
    public string []? Linux { get; init; }    // Linux only
    public string []? Macos { get; init; }    // macOS only
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
`All` keys apply on every platform. Platform-specific arrays add additional bindings on that platform. For example, `Undo` is bound to `Ctrl+Z` everywhere, but also to `Ctrl+/` on Linux and macOS:

```
["Undo"] = Bind.AllPlus ("Ctrl+Z", nonWindows: ["Ctrl+/"]),
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
The `Bind` helper class provides factory methods:

| Method | Description |
| --- | --- |
| `Bind.All (...)` | Same keys on all platforms |
| `Bind.AllPlus (key, nonWindows, windows, linux, macos)` | A base key on all platforms, plus platform-specific extras |
| `Bind.NonWindows (...)` | Keys that apply only on Linux and macOS |
| `Bind.Platform (windows, linux, macos)` | Fully platform-specific, no shared keys |

### User Overrides via Configuration[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#user-overrides-via-configuration)

Users can override key bindings for any view type using `View.ViewKeyBindings` in a configuration file. The outer key is the view type name; the inner dictionary maps command names to `PlatformKeyBinding` objects:

```
{
  "View.ViewKeyBindings": {
    "TextField": {
      "Undo": { "All": ["Ctrl+Z"] },
      "CutToEndOfLine": { "All": ["Ctrl+K"] }
    },
    "TextView": {
      "Redo": { "All": ["Ctrl+Shift+Z"], "Windows": ["Ctrl+Y"] }
    }
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
`ViewKeyBindings` overrides are applied last (highest priority), after both `View.DefaultKeyBindings` and per-view `DefaultKeyBindings`.

Application-level defaults can also be overridden:

```
{
  "Application.DefaultKeyBindings": {
    "Quit": { "All": ["Ctrl+Q"] },
    "Suspend": { "Linux": ["Ctrl+Z"], "Macos": ["Ctrl+Z"] }
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")

### Resolution Order[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#resolution-order)

When a view is created, key bindings are resolved in this order:

1. `View.DefaultKeyBindings` (base layer - navigation, clipboard, editing)
2. Per-view `DefaultKeyBindings` (e.g., `TextField.DefaultKeyBindings`)
3. `View.ViewKeyBindings` user overrides (from configuration)

At each layer, only commands supported by the view are bound, and keys already bound by a previous layer are skipped. This means user overrides take effect because they are applied last, after the default layers have established their bindings.

Keyboard Tracing[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#keyboard-tracing)
---------------------------------------------------------------------------------------------

For debugging keyboard event flow, use the `Trace` class from the `Terminal.Gui.Tracing` namespace:

```
using Terminal.Gui.Tracing;

Trace.KeyboardEnabled = true;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html# "Copy")
When enabled, keyboard events are logged via `Logging.Trace` showing the flow from Driver → Application → View. Enable via:

* **Code**: `Trace.KeyboardEnabled = true;`
* **Config**: `"Trace.KeyboardEnabled": true`
* **UICatalog**: Logging menu → Keyboard Trace

See [Logging - View Event Tracing](https://gui-cs.github.io/Terminal.Gui/docs/logging.html#view-event-tracing) for more details.
