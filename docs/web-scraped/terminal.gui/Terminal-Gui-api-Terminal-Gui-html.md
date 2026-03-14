# Source: https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.html

Title: Namespace Terminal.Gui | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.html

Markdown Content:
Terminal.Gui v2
Deep Dives
API Reference
Source

Terminal.Gui
Bind
IAcceptTarget
PlatformKeyBinding
TraceCategory
Terminal.Gui.App
Terminal.Gui.Configuration
Terminal.Gui.Drawing
Terminal.Gui.Drivers
Terminal.Gui.FileServices
Terminal.Gui.Input
Terminal.Gui.Resources
Terminal.Gui.Testing
Terminal.Gui.Text
Terminal.Gui.Time
Terminal.Gui.Tracing
Terminal.Gui.ViewBase
Terminal.Gui.Views
API Reference
Namespace Terminal.Gui
Classes
Bind

Provides ergonomic factory methods for creating PlatformKeyBinding instances.

PlatformKeyBinding

Defines the keys for a single command, optionally varying by platform. Keys are additive — for example, on Linux both All and Linux keys apply.

Interfaces
IAcceptTarget

Interface for views that handle Accept as terminal destinations. Views implementing this interface can bubble their Accept commands up to their SuperView or be treated as the default accept target depending on IsDefault.

Enums
TraceCategory

Categories of trace events that can be independently enabled or disabled.

IN THIS ARTICLE
Classes
Interfaces
Enums
Terminal.Gui - Part of the gui-cs Organization
