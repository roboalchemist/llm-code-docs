# Source: https://gui-cs.github.io/Terminal.Gui/

Title: Terminal.Gui - Cross Platform Terminal UI Toolkit for .NET | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/

Markdown Content:

1. [Deep Dives](https://gui-cs.github.io/Terminal.Gui/docs/index.html)

Terminal.Gui is a cross-platform UI toolkit for building sophisticated terminal UI (TUI) applications on Windows, macOS, and Linux/Unix.

[![Image 1: Sample app](https://gui-cs.github.io/Terminal.Gui/images/sample.gif)](https://gui-cs.github.io/Terminal.Gui/images/sample.gif)

Quick Start[](https://gui-cs.github.io/Terminal.Gui/#quick-start)
-----------------------------------------------------------------

Install the [Terminal.Gui.Templates](https://github.com/gui-cs/Terminal.Gui.templates), create a new TUI app, and run it:

```
dotnet new install Terminal.Gui.Templates
dotnet new tui-simple -n myproj
cd myproj
dotnet run
```

[](https://gui-cs.github.io/Terminal.Gui/# "Copy")
Simple Example[](https://gui-cs.github.io/Terminal.Gui/#simple-example)
-----------------------------------------------------------------------

```
using Terminal.Gui.App;
using Terminal.Gui.ViewBase;
using Terminal.Gui.Views;

using IApplication app = Application.Create ();
app.Init ();

using Window window = new () { Title = "Hello World (Esc to quit)" };
Label label = new ()
{
    Text = "Hello, Terminal.Gui v2!",
    X = Pos.Center (),
    Y = Pos.Center ()
};
window.Add (label);

app.Run (window);
```

[](https://gui-cs.github.io/Terminal.Gui/# "Copy")
See the [Examples](https://github.com/gui-cs/Terminal.Gui/tree/v2_develop/Examples) directory for more.

Build Powerful Terminal Applications[](https://gui-cs.github.io/Terminal.Gui/#build-powerful-terminal-applications)
-------------------------------------------------------------------------------------------------------------------

Terminal.Gui enables building sophisticated console applications with modern UIs:

* **Rich Forms and Dialogs** - Text fields, buttons, checkboxes, radio buttons, and data validation
* **Interactive Data Views** - Tables, lists, and trees with sorting, filtering, and in-place editing
* **Visualizations** - Charts, graphs, progress indicators, and color pickers with TrueColor support
* **Text Editors** - Full-featured text editing with clipboard, undo/redo, and Unicode support
* **File Management** - File and directory browsers with search and filtering
* **Wizards and Multi-Step Processes** - Guided workflows with navigation and validation
* **System Monitoring Tools** - Real-time dashboards with scrollable, resizable views
* **Configuration UIs** - Settings editors with persistent themes and user preferences
* **Cross-Platform CLI Tools** - Consistent experience on Windows, macOS, and Linux
* **Server Management Interfaces** - SSH-compatible UIs for remote administration

Key Features[](https://gui-cs.github.io/Terminal.Gui/#key-features)
-------------------------------------------------------------------

* **[Dozens of Built-in Views](https://gui-cs.github.io/Terminal.Gui/docs/views.html)** - Rich set of controls for building complex user interfaces

* **[Cross Platform](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html)** - Windows, Mac, and Linux with terminal drivers that work on color and monochrome terminals, including over SSH

* **[Powerful Layout Engine](https://gui-cs.github.io/Terminal.Gui/docs/layout.html)** - Relative positioning, automatic sizing, and dynamic terminal UIs

* **[Keyboard](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html) and [Mouse](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html) Input** - Complete input handling with simple event-based API

* **[Configuration System](https://gui-cs.github.io/Terminal.Gui/docs/config.html)** - Machine, user, and app-level settings with themes and key bindings

* **[Clipboard Support](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Clipboard.html)** - Cut, Copy, and Paste across platforms

* **[Multi-tasking](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html)** - Event processing, idle handlers, timers, and thread-safe classes

* **[Reactive Extensions](https://github.com/dotnet/reactive)** - MVVM pattern support with ReactiveUI data bindings

Installing[](https://gui-cs.github.io/Terminal.Gui/#installing)
---------------------------------------------------------------

### v2 Alpha (Recommended for new projects)[](https://gui-cs.github.io/Terminal.Gui/#v2-alpha-recommended-for-new-projects)

```
dotnet add package Terminal.Gui --version "2.0.0-alpha.*"
```

[](https://gui-cs.github.io/Terminal.Gui/# "Copy")

### v2 Develop (Latest)[](https://gui-cs.github.io/Terminal.Gui/#v2-develop-latest)

```
dotnet add package Terminal.Gui --version "2.0.0-develop.*"
```

[](https://gui-cs.github.io/Terminal.Gui/# "Copy")
Or use the [Terminal.Gui.Templates](https://github.com/gui-cs/Terminal.Gui.templates):

```
dotnet new install Terminal.Gui.Templates
```

[](https://gui-cs.github.io/Terminal.Gui/# "Copy")
Documentation[](https://gui-cs.github.io/Terminal.Gui/#documentation)
---------------------------------------------------------------------

* **[Getting Started](https://gui-cs.github.io/Terminal.Gui/docs/getting-started.html)** - Create your first Terminal.Gui application
* **[What's New in v2](https://gui-cs.github.io/Terminal.Gui/docs/newinv2.html)** - New features and architectural improvements
* **[Migrating from v1](https://gui-cs.github.io/Terminal.Gui/docs/migratingfromv1.html)** - Complete migration guide
* **[Views Overview](https://gui-cs.github.io/Terminal.Gui/docs/views.html)** - All built-in views and controls
* **[Deep Dives](https://gui-cs.github.io/Terminal.Gui/docs/index.html)** - Comprehensive guides and deep dives
* **[API Reference](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.html)** - Complete API documentation

Contributing[](https://gui-cs.github.io/Terminal.Gui/#contributing)
-------------------------------------------------------------------

Contributions welcome! See [CONTRIBUTING.md](https://github.com/gui-cs/Terminal.Gui/blob/v2_develop/CONTRIBUTING.md).

History[](https://gui-cs.github.io/Terminal.Gui/#history)
---------------------------------------------------------

See [gui-cs](https://github.com/gui-cs/) for project history and origins.
