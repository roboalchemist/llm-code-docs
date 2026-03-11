# Source: https://learn.microsoft.com/en-us/dotnet/desktop/winforms/input-mouse/events

Title: Using mouse events - Windows Forms

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/winforms/input-mouse/events

Markdown Content:
Most Windows Forms programs process mouse input by handling the mouse events. This article provides an overview of the mouse events, including details on when to use each event and the data that is supplied for each event. For more information about events in general, see [Events overview](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/forms/events).

The primary way to respond to mouse input is to handle mouse events. The following table shows the mouse events and describes when they're raised.

| Mouse Event | Description |
| --- | --- |
| [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click) | This event occurs when the mouse button is released, typically before the [MouseUp](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseup#system-windows-forms-control-mouseup) event. The handler for this event receives an argument of type [EventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.eventargs). Handle this event when you only need to determine when a click occurs. |
| [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick) | This event occurs when the user clicks the control with the mouse. The handler for this event receives an argument of type [MouseEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs). Handle this event when you need to get information about the mouse when a click occurs. |
| [DoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.doubleclick#system-windows-forms-control-doubleclick) | This event occurs when the control is double-clicked. The handler for this event receives an argument of type [EventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.eventargs). Handle this event when you only need to determine when a double-click occurs. |
| [MouseDoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedoubleclick#system-windows-forms-control-mousedoubleclick) | This event occurs when the user double-clicks the control with the mouse. The handler for this event receives an argument of type [MouseEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs). Handle this event when you need to get information about the mouse when a double-click occurs. |
| [MouseDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedown#system-windows-forms-control-mousedown) | This event occurs when the mouse pointer is over the control and the user presses a mouse button. The handler for this event receives an argument of type [MouseEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs). |
| [MouseEnter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseenter#system-windows-forms-control-mouseenter) | This event occurs when the mouse pointer enters the border or client area of the control, depending on the type of control. The handler for this event receives an argument of type [EventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.eventargs). |
| [MouseHover](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousehover#system-windows-forms-control-mousehover) | This event occurs when the mouse pointer stops and rests over the control. The handler for this event receives an argument of type [EventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.eventargs). |
| [MouseLeave](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseleave#system-windows-forms-control-mouseleave) | This event occurs when the mouse pointer leaves the border or client area of the control, depending on the type of the control. The handler for this event receives an argument of type [EventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.eventargs). |
| [MouseMove](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousemove#system-windows-forms-control-mousemove) | This event occurs when the mouse pointer moves while it is over a control. The handler for this event receives an argument of type [MouseEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs). |
| [MouseUp](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseup#system-windows-forms-control-mouseup) | This event occurs when the mouse pointer is over the control and the user releases a mouse button. The handler for this event receives an argument of type [MouseEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs). |
| [MouseWheel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousewheel#system-windows-forms-control-mousewheel) | This event occurs when the user rotates the mouse wheel while the control has focus. The handler for this event receives an argument of type [MouseEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs). Use the [MouseEventArgs.Delta](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs.delta) property to determine how far the mouse scrolled. |

A [MouseEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs) is sent to the handlers of mouse events related to clicking a mouse button and tracking mouse movements. [MouseEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.mouseeventargs) provides information about the current state of the mouse, including the location of the mouse pointer in client coordinates, which mouse buttons are pressed, and whether the mouse wheel has scrolled. Several mouse events, such as those that are raised when the mouse pointer has entered or left the bounds of a control, send an [EventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.eventargs) to the event handler with no further information.

If you want to know the current state of the mouse buttons or the location of the mouse pointer, and you want to avoid handling a mouse event, you can also use the [MouseButtons](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousebuttons) and [MousePosition](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseposition) properties of the [Control](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control) class. [MouseButtons](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousebuttons) returns information about which mouse buttons are currently pressed. The [MousePosition](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseposition) returns the screen coordinates of the mouse pointer and is equivalent to the value returned by [Position](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.cursor.position).

Because some mouse location information is in client coordinates and some is in screen coordinates, you might need to convert a point from one coordinate system to the other. You can do this easily by using the [PointToClient](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.pointtoclient) and [PointToScreen](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.pointtoscreen) methods available on the [Control](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control) class.

If you want to handle mouse click events in the proper order, you need to know the order in which click events are raised in Windows Forms controls. All Windows Forms controls raise click events in the same order when any supported mouse button is pressed and released, except where noted in the following list for individual controls. The following list shows the order of events raised for a single mouse-button click:

1. [MouseDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedown#system-windows-forms-control-mousedown) event.
2. [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click) event.
3. [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick) event.
4. [MouseUp](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseup#system-windows-forms-control-mouseup) event.

The following is the order of events raised for a double mouse-button click:

1. [MouseDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedown#system-windows-forms-control-mousedown) event.

2. [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click) event.

3. [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick) event.

4. [MouseUp](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseup#system-windows-forms-control-mouseup) event.

5. [MouseDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedown#system-windows-forms-control-mousedown) event.

6. [DoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.doubleclick#system-windows-forms-control-doubleclick) event.

This can vary, depending on whether the control in question has the [StandardDoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.controlstyles#system-windows-forms-controlstyles-standarddoubleclick) style bit set to `true`. For more information about how to set a [ControlStyles](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.controlstyles) bit, see the [SetStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.setstyle) method.

1. [MouseDoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedoubleclick#system-windows-forms-control-mousedoubleclick) event.

2. [MouseUp](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseup#system-windows-forms-control-mouseup) event.

The following controls don't conform to the standard mouse click event behavior:

* [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.button)

* [CheckBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.checkbox)

* [ComboBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.combobox)

* [RadioButton](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.radiobutton)

Note

For the [ComboBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.combobox) control, the event behavior detailed later occurs if the user clicks on the edit field, the button, or on an item within the list.
    ***Left click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick)
    *   **Right click**: No click events raised
    ***Left double-click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick); [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick)
    *   **Right double-click**: No click events raised

* [TextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox), [RichTextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.richtextbox), [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.listbox), [MaskedTextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.maskedtextbox), and [CheckedListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.checkedlistbox) controls

Note

The event behavior detailed later occurs when the user clicks anywhere within these controls.
    ***Left click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick)
    *   **Right click**: No click events raised
    ***Left double-click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick), [DoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.doubleclick#system-windows-forms-control-doubleclick), [MouseDoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedoubleclick#system-windows-forms-control-mousedoubleclick)
    *   **Right double-click**: No click events raised

* [ListView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.listview) control

Note

The event behavior detailed later occurs only when the user clicks on the items in the [ListView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.listview) control. No events are raised for clicks anywhere else on the control. In addition to the events described later, there are the [BeforeLabelEdit](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.listview.beforelabeledit#system-windows-forms-listview-beforelabeledit) and [AfterLabelEdit](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.listview.afterlabeledit#system-windows-forms-listview-afterlabeledit) events, which might be of interest to you if you want to use validation with the [ListView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.listview) control.
    ***Left click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick)
    *   **Right click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick)
    ***Left double-click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick); [DoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.doubleclick#system-windows-forms-control-doubleclick), [MouseDoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedoubleclick#system-windows-forms-control-mousedoubleclick)
    *   **Right double-click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick); [DoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.doubleclick#system-windows-forms-control-doubleclick), [MouseDoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedoubleclick#system-windows-forms-control-mousedoubleclick)

* [TreeView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview) control

Note

The event behavior detailed later occurs only when the user clicks on the items themselves or to the right of the items in the [TreeView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview) control. No events are raised for clicks anywhere else on the control. In addition to those described later, there are the [BeforeCheck](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview.beforecheck#system-windows-forms-treeview-beforecheck), [BeforeSelect](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview.beforeselect#system-windows-forms-treeview-beforeselect), [BeforeLabelEdit](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview.beforelabeledit#system-windows-forms-treeview-beforelabeledit), [AfterSelect](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview.afterselect#system-windows-forms-treeview-afterselect), [AfterCheck](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview.aftercheck#system-windows-forms-treeview-aftercheck), and [AfterLabelEdit](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview.afterlabeledit#system-windows-forms-treeview-afterlabeledit) events, which may be of interest to you if you want to use validation with the [TreeView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview) control.
    ***Left click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick)
    *   **Right click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick)
    ***Left double-click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick); [DoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.doubleclick#system-windows-forms-control-doubleclick), [MouseDoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedoubleclick#system-windows-forms-control-mousedoubleclick)
    *   **Right double-click**: [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click), [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick); [DoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.doubleclick#system-windows-forms-control-doubleclick), [MouseDoubleClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedoubleclick#system-windows-forms-control-mousedoubleclick)

Toggle controls, such as the controls deriving from the [ButtonBase](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.buttonbase) class, have the following distinctive painting behavior in combination with mouse click events:

1. The user presses the mouse button.

2. The control paints in the pressed state.

3. The [MouseDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mousedown#system-windows-forms-control-mousedown) event is raised.

4. The user releases the mouse button.

5. The control paints in the raised state.

6. The [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click) event is raised.

7. The [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick) event is raised.

8. The [MouseUp](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseup#system-windows-forms-control-mouseup) event is raised.

Note

If the user moves the pointer out of the toggle control while the mouse button is down (such as moving the mouse off the [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.button) control while it's pressed), the toggle control paints in the raised state and only the [MouseUp](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseup#system-windows-forms-control-mouseup) event occurs. The [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.click#system-windows-forms-control-click) or [MouseClick](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.mouseclick#system-windows-forms-control-mouseclick) events won't occur in this situation.

* [Overview of using the mouse](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/input-mouse/overview)
* [Manage mouse pointers](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/input-mouse/how-to-manage-cursor-pointer)
* [How to simulate mouse events](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/input-mouse/how-to-simulate-events)
* [System.Windows.Forms.Control](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control)
