# Source: https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Clipboard.html

Title: Class Clipboard | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Clipboard.html

Markdown Content:
Terminal.Gui v2
Deep Dives
API Reference
Source

Terminal.Gui
Terminal.Gui.App
Application
ApplicationMainLoop<TInputRecord>
ApplicationModelUsage
ApplicationNavigation
ApplicationPopover
CWPEventHelper
CWPPropertyHelper
CWPWorkflowHelper
CancelEventArgs<T>
Clipboard
Properties
Methods
ClipboardBase
EventArgs<T>
GlobalResources
IApplication
IApplicationMainLoop<TInputRecord>
IClipboard
IKeyboard
IMainLoopCoordinator
IMouse
IMouseGrabHandler
IPopover
IPopoverView
IRunnable
IRunnable<TResult>
ITimedEvents
LogarithmicTimeout
Logging
NotInitializedException
PopoverImpl
Popover<TView, TResult>
ResultEventArgs<T>
SessionToken
SessionTokenEventArgs
SmoothAcceleratingTimeout
TimedEvents
Timeout
TimeoutEventArgs
ValueChangedEventArgs<T>
ValueChangingEventArgs<T>
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
Terminal.Gui.App
Class Clipboard
NamespaceTerminal.Gui.App
AssemblyTerminal.Gui.dll

Provides cut, copy, and paste support for the OS clipboard.

[Obsolete("Use IApplication.Clipboard instead. The static Clipboard class will be removed in a future release.")]
public static class Clipboard
Inheritance
object Clipboard
Remarks

DEPRECATED: This static class is obsolete. Use Clipboard instead.

On Windows, the Clipboard class uses the Windows Clipboard APIs via P/Invoke.

On Linux, when not running under Windows Subsystem for Linux (WSL), the Clipboard class uses the xclip command line tool. If xclip is not installed, the clipboard will not work.

On Linux, when running under Windows Subsystem for Linux (WSL), the Clipboard class launches Windows' powershell.exe via WSL interop and uses the "Set-Clipboard" and "Get-Clipboard" Powershell CmdLets.

On the Mac, the Clipboard class uses the MacO OS X pbcopy and pbpaste command line tools and the Mac clipboard APIs vai P/Invoke.

Properties
Contents

Gets (copies from) or sets (pastes to) the contents of the OS clipboard.

IsSupported

Returns true if the environmental dependencies are in place to interact with the OS clipboard.

Methods
TryGetClipboardData(out string)

Gets the OS clipboard data if possible.

TrySetClipboardData(string)

Sets the OS clipboard data if possible.

Edit this page
IN THIS ARTICLE
Remarks
Properties
Methods
Terminal.Gui - Part of the gui-cs Organization
