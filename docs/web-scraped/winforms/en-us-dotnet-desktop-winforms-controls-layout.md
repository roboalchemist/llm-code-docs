# Source: https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/layout

Title: Control layout options - Windows Forms

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/layout

Markdown Content:
Control placement in Windows Forms is determined not only by the control, but also by the parent of the control. This article describes the different settings provided by controls and the different types of parent containers that affect layout.

The position a control appears on a parent is determined by the value of the [Location](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.location#system-windows-forms-control-location) property relative to the top-left of the parent surface. The top-left position coordinate of a control in the parent is `(x0,y0)`. The size of the control is determined by the [Size](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.size#system-windows-forms-control-size) property and represents the width and height of the control.

![Image 1: Location of the control relative to the container](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/location+container.png)

When a control is added to a parent that enforces automatic placement, the position and size of the control is changed. In this case, the position and size of the control might not be manually adjusted, depending on the type of parent.

The [MaximumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.maximumsize) and [MinimumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.minimumsize) properties help set the minimum and maximum space a control can use.

There are two control properties that help with precise placement of controls: [Margin](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.margin) and [Padding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.padding).

The [Margin](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.margin) property defines the space around the control that keeps other controls a specified distance from the control's borders.

The [Padding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.padding) property defines the space in the interior of a control that keeps the control's content (for example, the value of its [Text](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.text) property) a specified distance from the control's borders.

The following figure shows the [Margin](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.margin) and [Padding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.padding) properties on a control.

![Image 2: Padding and Margin properties for Windows Forms Controls](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/margin-padding.png)

The Visual Studio Designer respects these properties when you're positioning and resizing controls. Snaplines appear as guides to help you remain outside the specified margin of a control. For example, Visual Studio displays the snapline when you drag a control next to another control:

![Image 3: Animated image demonstrating the snaplines with margin properties for Windows Forms .NET in Visual Studio](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/margins.gif)

Controls can be automatically placed within their parent. Some parent containers force placement while others respect control settings that guide placement. There are two properties on a control that help automatic placement and size within a parent: [Dock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.dock) and [Anchor](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.anchor#system-windows-forms-control-anchor).

Drawing order can affect automatic placement. The order in which a control is drawn determined by the control's index in the parent's [Controls](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.controls#system-windows-forms-control-controls) collection. This index is known as the **Z-order**. Each control is drawn in the reverse order they appear in the collection. Meaning, the collection is a first-in-last-drawn and last-in-first-drawn collection.

The [MinimumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.minimumsize) and [MaximumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.maximumsize) properties help set the minimum and maximum space a control can use.

The `Dock` property sets which border of the control is aligned to the corresponding side of the parent, and how the control is resized within the parent.

![Image 4: Windows form with buttons with dock settings.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/dock-modes.png)

When a control is docked, the container determines the space it should occupy and resizes and positions the control. The width and height of the control are still respected based on the docking style. For example, if the control is docked to the top, the [Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.height#system-windows-forms-control-height) of the control is respected but the [Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.width#system-windows-forms-control-width) is automatically adjusted. If a control is docked to the left, the [Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.width#system-windows-forms-control-width) of the control is respected but the [Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.height#system-windows-forms-control-height) is automatically adjusted.

The [Location](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.location#system-windows-forms-control-location) of the control can't be manually set as docking a control automatically sets the position.

The **Z-order** of the control does affect docking. As docked controls are laid out, they use what space is available to them. For example, if a control is drawn first and docked to the top, it takes up the entire width of the container. If a next control is docked to the left, it has less vertical space available to it.

![Image 5: Windows form with buttons docked to the left and top with top being bigger.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/dock-top-then-left.png)

If the control's **Z-order** is reversed, the control that is docked to the left now has more initial space available. The control uses the entire height of the container. The control that is docked to the top has less horizontal space available to it.

![Image 6: Windows form with buttons docked to the left and top with left being bigger.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/dock-left-then-top.png)

As the container grows and shrinks, the controls docked to the container are repositioned and resized to maintain their applicable positions and sizes.

![Image 7: Animation showing how A Windows Form with buttons docked in all positions is resized.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/dock-resize.gif)

If multiple controls are docked to the same side of the container, they're stacked according to their **Z-order**.

![Image 8: Windows form with two buttons docked to the left.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/dock-left-left.png)

Anchoring a control allows you to tie the control to one or more sides of the parent container. As the container changes in size, anchored child controls maintain their distance to the anchored side.

A control can be anchored to one or more sides, without restriction. The anchor is set with the [Anchor](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.anchor#system-windows-forms-control-anchor) property.

![Image 9: Animation showing how A Windows Form with buttons anchored in all positions is resized.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/anchor-resize.gif)

The [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize#system-windows-forms-control-autosize) property enables a control to change its size, if necessary, to fit the size specified by the [PreferredSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.preferredsize#system-windows-forms-control-preferredsize) property. You adjust the sizing behavior for specific controls by setting the `AutoSizeMode` property.

Only some controls support the [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property. In addition, some controls that support the [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property also supports the `AutoSizeMode` property.

| Always true behavior | Description |
| --- | --- |
| Automatic sizing is a run-time feature. | This means it never grows or shrinks a control and then has no further effect. |
| If a control changes size, the value of its [Location](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.location) property always remains constant. | When a control's contents cause it to grow, the control grows toward the right and downward. Controls don't grow to the left. |
| The [Dock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.dock) and [Anchor](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.anchor) properties are honored when [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) is `true`. | The value of the control's [Location](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.location) property is adjusted to the correct value. The [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.label) control is the exception to this rule. When you set the value of a docked [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.label) control's [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property to `true`, the [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.label) control won't stretch. |
| A control's [MaximumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.maximumsize) and [MinimumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.minimumsize) properties are always honored, regardless of the value of its [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property. | The [MaximumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.maximumsize) and [MinimumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.minimumsize) properties aren't affected by the [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property. |
| There's no minimum size set by default. | This means that if a control is set to shrink under [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) and it has no contents, the value of its [Size](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.size) property is `(0x,0y)`. In this case, your control shrinks to a point, and it will not be readily visible. |
| If a control doesn't implement the [GetPreferredSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.getpreferredsize) method, the [GetPreferredSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.getpreferredsize) method returns last value assigned to the [Size](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.size) property. | This means that setting [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) to `true` has no effect. |
| A control in a [TableLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel) cell always shrinks to fit in the cell until its [MinimumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.minimumsize) is reached. | This size is enforced as a maximum size. This isn't the case when the cell is part of an [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.sizetype#system-windows-forms-sizetype-autosize) row or column. |

The [AutoSizeMode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.autosizemode) property provides more fine-grained control over the default [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) behavior. The `AutoSizeMode` property specifies how a control sizes itself to its content. The content, for example, could be the text for a [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.button) control or the child controls for a container.

The following list shows the `AutoSizeMode` values and its behavior.

* [AutoSizeMode.GrowAndShrink](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.autosizemode#system-windows-forms-autosizemode-growandshrink)

The control grows or shrinks to encompass its contents.

The [MinimumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.minimumsize) and [MaximumSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.maximumsize) values are honored, but the current value of the [Size](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.size) property is ignored.

This is the same behavior as controls with the [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property and no `AutoSizeMode` property.

* [AutoSizeMode.GrowOnly](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.autosizemode#system-windows-forms-autosizemode-growonly)

The control grows as much as necessary to encompass its contents, but it will not shrink smaller than the value specified by its [Size](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.size) property.

This is the default value for `AutoSizeMode`.

The following table describes the level of auto sizing support by control:

| Control | `AutoSize` supported | `AutoSizeMode` supported |
| --- | --- | --- |
| [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.button) | ✔️ | ✔️ |
| [CheckedListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.checkedlistbox) | ✔️ | ✔️ |
| [FlowLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.flowlayoutpanel) | ✔️ | ✔️ |
| [Form](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form) | ✔️ | ✔️ |
| [GroupBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.groupbox) | ✔️ | ✔️ |
| [Panel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.panel) | ✔️ | ✔️ |
| [TableLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel) | ✔️ | ✔️ |
| [CheckBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.checkbox) | ✔️ | ❌ |
| [DomainUpDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.domainupdown) | ✔️ | ❌ |
| [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.label) | ✔️ | ❌ |
| [LinkLabel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.linklabel) | ✔️ | ❌ |
| [MaskedTextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.maskedtextbox) | ✔️ | ❌ |
| [NumericUpDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.numericupdown) | ✔️ | ❌ |
| [RadioButton](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.radiobutton) | ✔️ | ❌ |
| [TextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox) | ✔️ | ❌ |
| [TrackBar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.trackbar) | ✔️ | ❌ |
| [CheckedListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.checkedlistbox) | ❌ | ❌ |
| [ComboBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.combobox) | ❌ | ❌ |
| [DataGridView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.datagridview) | ❌ | ❌ |
| [DateTimePicker](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.datetimepicker) | ❌ | ❌ |
| [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.listbox) | ❌ | ❌ |
| [ListView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.listview) | ❌ | ❌ |
| [MaskedTextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.maskedtextbox) | ❌ | ❌ |
| [MonthCalendar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.monthcalendar) | ❌ | ❌ |
| [ProgressBar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.progressbar) | ❌ | ❌ |
| [PropertyGrid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.propertygrid) | ❌ | ❌ |
| [RichTextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.richtextbox) | ❌ | ❌ |
| [SplitContainer](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.splitcontainer) | ❌ | ❌ |
| [TabControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tabcontrol) | ❌ | ❌ |
| [TabPage](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tabpage) | ❌ | ❌ |
| [TreeView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.treeview) | ❌ | ❌ |
| [WebBrowser](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.webbrowser) | ❌ | ❌ |
| [ScrollBar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.scrollbar) | ❌ | ❌ |

The following table describes the sizing behavior of a control at design time, based on the value of its [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) and `AutoSizeMode` properties.

Override the [SelectionRules](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.design.controldesigner.selectionrules) property to determine whether a given control is in a user-resizable state. In the following table, "can't resize" means [Moveable](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.design.selectionrules#system-windows-forms-design-selectionrules-moveable) only, "can resize" means [AllSizeable](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.design.selectionrules#system-windows-forms-design-selectionrules-allsizeable) and [Moveable](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.design.selectionrules#system-windows-forms-design-selectionrules-moveable).

| `AutoSize` setting | `AutoSizeMode` setting | Behavior |
| --- | --- | --- |
| `true` | Property not available. | The user can't resize the control at design time, except for the following controls: - [TextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox) - [MaskedTextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.maskedtextbox) - [RichTextBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.richtextbox) - [TrackBar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.trackbar) |
| `true` | [GrowAndShrink](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.autosizemode#system-windows-forms-autosizemode-growandshrink) | The user can't resize the control at design time. |
| `true` | [GrowOnly](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.autosizemode#system-windows-forms-autosizemode-growonly) | The user can resize the control at design time. When the [Size](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.size) property is set, the user can only increase the size of the control. |
| `false` or `AutoSize` is hidden | Not applicable. | User can resize the control at design time. |

Note

To maximize productivity, the Windows Forms Designer in Visual Studio shadows the [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property for the [Form](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form) class. At design time, the form behaves as though the [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property is set to `false`, regardless of its actual setting. At runtime, no special accommodation is made, and the [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property is applied as specified by the property setting.

The [Form](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form) is the main object of Windows Forms. A Windows Forms application usually has a form displayed at all times. Forms contain controls and respect the [Location](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.location#system-windows-forms-control-location) and [Size](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.size#system-windows-forms-control-size) properties of the control for manual placement. Forms also respond to the [Dock](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/layout#dock) property for automatic placement.

Most of the time a form has grips on the edges that allow the user to resize the form. The [Anchor](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.anchor#system-windows-forms-control-anchor) property of a control lets the control grow and shrink as the form is resized.

The [Panel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.panel) control is similar to a form in that it simply groups controls together. It supports the same manual and automatic placement styles that a form does. For more information, see the [Container: Form](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/layout#container-form) section.

A panel blends in seamlessly with the parent, and it does cut off any area of a control that falls out of bounds of the panel. If a control falls outside the bounds of the panel and [AutoScroll](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form.autoscroll#system-windows-forms-form-autoscroll) is set to `true`, scroll bars appear and the user can scroll the panel.

Unlike the [group box](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/layout#container-group-box) control, a panel doesn't have a caption and border.

![Image 10: A Windows Form with a panel and group box.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/panel-groupbox.png)

The image above has a panel with the [BorderStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.panel.borderstyle) property set to demonstrate the bounds of the panel.

The [GroupBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.groupbox) control provides an identifiable grouping for other controls. Typically, you use a group box to subdivide a form by function. For example, you may have a form representing personal information and the fields related to an address would be grouped together. At design time, it's easy to move the group box around along with its contained controls.

The group box supports the same manual and automatic placement styles that a form does. For more information, see the [Container: Form](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/layout#container-form) section. A group box also cuts off any portion of a control that falls out of bounds of the panel.

Unlike the [panel](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/layout#container-panel) control, a group box doesn't have the capability to scroll content and display scroll bars.

![Image 11: A Windows Form with a panel and group box.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/panel-groupbox.png)

The [FlowLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.flowlayoutpanel) control arranges its contents in a horizontal or vertical flow direction. You can wrap the control's contents from one row to the next, or from one column to the next. Alternately, you can clip instead of wrap its contents.

You can specify the flow direction by setting the value of the [FlowDirection](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.flowlayoutpanel.flowdirection) property. The [FlowLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.flowlayoutpanel) control correctly reverses its flow direction in Right-to-Left (RTL) layouts. You can also specify whether the [FlowLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.flowlayoutpanel) control's contents are wrapped or clipped by setting the value of the [WrapContents](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.flowlayoutpanel.wrapcontents) property.

The [FlowLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.flowlayoutpanel) control automatically sizes to its contents when you set the [AutoSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.autosize) property to `true`. It also provides a `FlowBreak` property to its child controls. Setting the value of the `FlowBreak` property to `true` causes the [FlowLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.flowlayoutpanel) control to stop laying out controls in the current flow direction and wrap to the next row or column.

![Image 12: A Windows Form with two flow panel controls.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/flow.png)

The image above has two `FlowLayoutPanel` controls with the [BorderStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.panel.borderstyle#system-windows-forms-panel-borderstyle) property set to demonstrate the bounds of the control.

The [TableLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel) control arranges its contents in a grid. Because the layout is done both at design time and run time, it can change dynamically as the application environment changes. This gives the controls in the panel the ability to resize proportionally, so they can respond to changes such as the parent control resizing or text length changing because of localization.

Any Windows Forms control can be a child of the [TableLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel) control, including other instances of [TableLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel). This allows you to construct sophisticated layouts that adapt to changes at run time.

You can also control the direction of expansion (horizontal or vertical) after the [TableLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel) control is full of child controls. By default, the [TableLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel) control expands downward by adding rows.

You can control the size and style of the rows and columns by using the [RowStyles](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel.rowstyles) and [ColumnStyles](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel.columnstyles) properties. You can set the properties of rows or columns individually.

The [TableLayoutPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel) control adds the following properties to its child controls: `Cell`, `Column`, `Row`, `ColumnSpan`, and `RowSpan`.

![Image 13: A Windows Form with table layout control.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/table.png)

The image above has a table with the [CellBorderStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tablelayoutpanel.cellborderstyle#system-windows-forms-tablelayoutpanel-cellborderstyle) property set to demonstrate the bounds of each cell.

The Windows Forms [SplitContainer](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.splitcontainer) control can be thought of as a composite control; it's two panels separated by a movable bar. When the mouse pointer is over the bar, the pointer changes shape to show that the bar is movable.

With the [SplitContainer](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.splitcontainer) control, you can create complex user interfaces; often, a selection in one panel determines what objects are shown in the other panel. This arrangement is effective for displaying and browsing information. Having two panels lets you aggregate information in areas, and the bar, or "splitter," makes it easy for users to resize the panels.

![Image 14: A Windows Form with a nested split container.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/splitcontainer.png)

The image above has a split container to create a left and right pane. The right pane contains a second split container with the [Orientation](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.splitcontainer.orientation#system-windows-forms-splitcontainer-orientation) set to [Vertical](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.orientation#system-windows-forms-orientation-vertical). The [BorderStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.splitcontainer.borderstyle#system-windows-forms-splitcontainer-borderstyle) property is set to demonstrate the bounds of each panel.

The [TabControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tabcontrol) displays multiple tabs, like dividers in a notebook or labels in a set of folders in a filing cabinet. The tabs can contain pictures and other controls. Use the tab control to produce the kind of multiple-page dialog box that appears many places in the Windows operating system, such as the Control Panel and Display Properties. Additionally, the [TabControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tabcontrol) can be used to create property pages, which are used to set a group of related properties.

The most important property of the [TabControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tabcontrol) is [TabPages](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tabcontrol.tabpages), which contains the individual tabs. Each individual tab is a [TabPage](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.tabpage) object.

![Image 15: A Windows Form with a tab control with two tab pages.](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/media/layout/tabcontrol.png)
