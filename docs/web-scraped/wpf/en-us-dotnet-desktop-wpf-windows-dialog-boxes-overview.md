# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/dialog-boxes-overview

Title: Dialog Boxes Overview - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/dialog-boxes-overview

Markdown Content:
Windows Presentation Foundation (WPF) provides ways for you to design your own dialog boxes. Dialog boxes are windows but with a specific intent and user experience. This article discusses how a dialog box works and what types of dialog boxes you can create and use. Dialog boxes are used to:

*   Display specific information to users.
*   Gather information from users.
*   Both display and gather information.
*   Display an operating system prompt, such as print window.
*   Select a file or folder.

These types of windows are known as _dialog boxes_. A dialog box can be displayed in two ways: modal and modeless.

Displaying a _modal_ dialog box to the user is a technique with which the application interrupts what it was doing until the user closes the dialog box. This generally comes in the form of a prompt or alert. Other windows in the application can't be interacted with until the dialog box is closed. Once the _modal_ dialog box is closed, the application continues. The most common dialog boxes are used to show an open file or save file prompt, displaying the printer dialog, or messaging the user with some status.

A _modeless_ dialog box doesn't prevent a user from activating other windows while it's open. For example, if a user wants to find occurrences of a particular word in a document, a main window will often open a dialog box to ask a user what word they're looking for. Since the application doesn't want to prevent the user from editing the document, the dialog box doesn't need to be modal. A modeless dialog box at least provides a **Close** button to close the dialog box. Other buttons may be provided to run specific functions, such as a **Find Next** button to find the next word in a word search.

With WPF you can create several types of dialog boxes, such as message boxes, common dialog boxes, and custom dialog boxes. This article discusses each, and the [Dialog Box Sample](https://github.com/Microsoft/WPF-Samples/tree/master/Windows/DialogBox) provides matching examples.

A _message box_ is a dialog box that can be used to display textual information and to allow users to make decisions with buttons. The following figure shows a message box that asks a question and provides the user with three buttons to answer the question.

![Image 1: Word processor dialog box asking if you want to save the changes to the document before the application closes.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/dialog-boxes-overview/word-processor-dialog.png)

To create a message box, you use the [MessageBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.messagebox) class. [MessageBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.messagebox) lets you configure the message box text, title, icon, and buttons.

For more information, see [How to open a message box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-message-box).

Windows implements different kinds of reusable dialog boxes that are common to all applications, including dialog boxes for selecting files and printing.

Since these dialog boxes are provided by the operating system, they're shared among all the applications that run on the operating system. These dialog boxes provide a consistent user experience, and are known as _common dialog boxes_. As a user uses a common dialog box in one application, they don't need to learn how to use that dialog box in other applications.

WPF encapsulates the open file, save file, open folder, and print common dialog boxes and exposes them as managed classes for you to use.

![Image 2: A 'Open File' dialog box called from WPF.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/dialog-boxes-overview/open-file-dialog-box.png)

To learn more about common dialog boxes, see the following articles:

*   [How to display a common dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-common-system-dialog-box)
*   [Show the Open File dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-common-system-dialog-box#open-file-dialog-box)
*   [Show the Save File dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-common-system-dialog-box#save-file-dialog-box)
*   [Open Folder dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-common-system-dialog-box#open-folder-dialog-box)
*   [Show the Print dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-common-system-dialog-box#print-dialog-box)

While common dialog boxes are useful, and should be used when possible, they don't support the requirements of domain-specific dialog boxes. In these cases, you need to create your own dialog boxes. As we'll see, a dialog box is a window with special behaviors. [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) implements those behaviors and you use the window to create custom modal and modeless dialog boxes.

There are many design considerations to take into account when you create your own dialog box. Although both an application window and dialog box contain similarities, such as sharing the same base class, a dialog box is used for a specific purpose. Usually a dialog box is required when you need to prompt a user for some sort of information or response. Typically the application will pause while the dialog box (modal) is displayed, restricting access to the rest of the application. Once the dialog box is closed, the application continues. Confining interactions to the dialog box alone, though, isn't a requirement.

When a WPF window is closed, it can't be reopened. Custom dialog boxes are WPF windows and the same rule applies. To learn how to close a window, see [How to close a window or dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-close-window-dialog-box).

When designing a dialog box, follow these suggestions to create a good user experience:

❌ DON'T clutter the dialog window. The dialog experience is for the user to enter some data, or to make a choice.

✔️ DO provide an **OK** button to close the window.

✔️ DO set the **OK** button's [IsDefault](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button.isdefault) property to `true` to allow the user to press the ENTER key to accept and close the window.

✔️ CONSIDER adding a **Cancel** button so that the user can close the window and indicate that they don't want to continue.

✔️ DO set the **Cancel** button's [IsCancel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button.iscancel) property to `true` to allow the user to press the ESC key to close the window.

✔️ DO set the title of the window to accurately describe what the dialog represents, or what the user should do with the dialog.

✔️ DO set minimum width and height values for the window, preventing the user from resizing the window too small.

✔️ CONSIDER disabling the ability to resize the window if [ShowInTaskbar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showintaskbar) is set to `false`. You can disable resizing by setting [ResizeMode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.resizemode) to [NoResize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resizemode#system-windows-resizemode-noresize)

The following code demonstrates this configuration.

```
<Window x:Class="Dialogs.Margins"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Change Margins"
        Closing="Window_Closing"
        MinHeight="200"
        MinWidth="300"
        SizeToContent="WidthAndHeight"
        ResizeMode="NoResize"
        ShowInTaskbar="False"
        WindowStartupLocation="CenterOwner" 
        FocusManager.FocusedElement="{Binding ElementName=leftMarginTextBox}">
    <Grid Margin="10">
        <Grid.Resources>
            <!-- Default settings for controls -->
            <Style TargetType="{x:Type Label}">
                <Setter Property="Margin" Value="0,3,5,5" />
                <Setter Property="Padding" Value="0,0,0,5" />
            </Style>
            <Style TargetType="{x:Type TextBox}">
                <Setter Property="Margin" Value="0,0,0,5" />
            </Style>
            <Style TargetType="{x:Type Button}">
                <Setter Property="Width" Value="70" />
                <Setter Property="Height" Value="25" />
                <Setter Property="Margin" Value="5,0,0,0" />
            </Style>
        </Grid.Resources>

        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="Auto" />
            <ColumnDefinition />
        </Grid.ColumnDefinitions>

        <Grid.RowDefinitions>
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
            <RowDefinition />
        </Grid.RowDefinitions>

        <!-- Left,Top,Right,Bottom margins-->
        <Label Grid.Column="0" Grid.Row="0">Left Margin:</Label>
        <TextBox Name="leftMarginTextBox" Grid.Column="1" Grid.Row="0" />

        <Label Grid.Column="0" Grid.Row="1">Top Margin:</Label>
        <TextBox Name="topMarginTextBox" Grid.Column="1" Grid.Row="1"/>

        <Label Grid.Column="0" Grid.Row="2">Right Margin:</Label>
        <TextBox Name="rightMarginTextBox" Grid.Column="1" Grid.Row="2" />

        <Label Grid.Column="0" Grid.Row="3">Bottom Margin:</Label>
        <TextBox Name="bottomMarginTextBox" Grid.Column="1" Grid.Row="3" />

        <!-- Accept or Cancel -->
        <StackPanel Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="4" Orientation="Horizontal" HorizontalAlignment="Right">
            <Button Name="okButton" Click="okButton_Click" IsDefault="True">OK</Button>
            <Button Name="cancelButton" IsCancel="True">Cancel</Button>
        </StackPanel>
    </Grid >
</Window>
```

The above XAML creates a window that looks similar to the following image:

![Image 3: A dialog box window for WPF that shows left, top, right, bottom text boxes.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/dialog-boxes-overview/example-dialog.png)

The user experience for a dialog box also extends into the menu bar or the button of the window that opens it. When a menu item or button runs a function that requires user interaction through a dialog box before the function can continue, the control should use an ellipsis at the end of its header text:

```
<MenuItem Header="_Margins..." Click="formatMarginsMenuItem_Click" />
<!-- or -->
<Button Content="_Margins..." Click="formatMarginsButton_Click" />
```

When a menu item or button runs a function that displays a dialog box that **doesn't** require user interaction, such as an _About_ dialog box, an ellipsis isn't required.

Menu items are a common way to provide users with application actions that are grouped into related themes. You've probably seen the _File_ menu on many different applications. In a typical application, the _File_ menu item provides ways to save a file, load a file, and print a file. If the action is going to display a modal window, the header typically includes an ellipsis as shown in the following image:

![Image 4: A WPF window that shows menu items with an ellipsis to indicate which item shows a dialog box.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/dialog-boxes-overview/simple-text-editor-menu.png)

Two of the menu items have an ellipsis: `...`. This helps the user identify that when they select those menu items, a modal window is shown, pausing the application until the user closes it.

This design technique is an easy way for you to communicate to your users what they should expect.

You can follow the same principle described in the [Menu items](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/dialog-boxes-overview#menu-items) section. Use an ellipsis on the button text to indicate that when the user presses the button, a modal dialog will appear. In the following image, there are two buttons and it's easy to understand which button displays a dialog box:

![Image 5: A WPF window that shows buttons with an ellipsis to indicate which item shows a dialog box.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/dialog-boxes-overview/simple-text-editor.png)

Opening another window, especially a modal dialog box, is a great way to return status and information to calling code.

When a dialog box is shown by calling [ShowDialog()](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showdialog#system-windows-window-showdialog), the code that opened the dialog box waits until the `ShowDialog` method returns. When the method returns, the code that called it needs to decide whether to continue processing or stop processing. The user generally indicates this by pressing an **OK** or **Cancel** button on the dialog box.

When the **OK** button is pressed, `ShowDialog` should be designed to return `true`, and the **Cancel** button to return `false`. This is achieved by setting the [DialogResult](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.dialogresult#system-windows-window-dialogresult) property when the button is pressed.

```
private void okButton_Click(object sender, RoutedEventArgs e) =>
    DialogResult = true;

private void cancelButton_Click(object sender, RoutedEventArgs e) =>
    DialogResult = false;
```

The [DialogResult](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.dialogresult#system-windows-window-dialogresult) property can only be set if the dialog box was displayed with [ShowDialog()](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showdialog#system-windows-window-showdialog). When the `DialogResult` property is set, the dialog box closes.

If a button's [IsCancel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button.iscancel) property is set to `true`, and the window is opened with [ShowDialog()](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showdialog#system-windows-window-showdialog), the ESC key will close the window and set `DialogResult` to `false`.

For more information about closing dialog boxes, see [How to close a window or dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-close-window-dialog-box).

The [ShowDialog()](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showdialog#system-windows-window-showdialog) returns a boolean value to indicate whether the user accepted or canceled the dialog box. If you're alerting the user to something, but not requiring they make a decision or provide data, you can ignore the response. The response can also be inspected by checking the [DialogResult](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.dialogresult#system-windows-window-dialogresult) property. The following code shows how to process the response:

```
var dialog = new Margins();

// Display the dialog box and read the response
bool? result = dialog.ShowDialog();

if (result == true)
{
    // User accepted the dialog box
    MessageBox.Show("Your request will be processed.");
}
else
{
    // User cancelled the dialog box
    MessageBox.Show("Sorry it didn't work out, we'll try again later.");
}
```

To show a dialog box modeless, call [Show()](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.show#system-windows-window-show). The dialog box should at least provide a **Close** button. Other buttons and interactive elements can be provided to run a specific function, such as a **Find Next** button to find the next word in a word search.

Because a modeless dialog box doesn't block the calling code from continuing, you must provide a different way of returning a result. You can do one of the following:

*   Expose a data object property on the window.
*   Handle the [Window.Closed](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closed#system-windows-window-closed) event in the calling code.
*   Create events on the window that are raised when the user selects an object or presses a specific button.

The following example uses the [Window.Closed](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closed#system-windows-window-closed) event to display a message box to the user when the dialog box closes. The message displayed references a property of the closed dialog box. For more information about closing dialogs boxes, see [How to close a window or dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-close-window-dialog-box).

```
var marginsWindow = new Margins();

marginsWindow.Closed += (sender, eventArgs) =>
{
    MessageBox.Show($"You closed the margins window! It had the title of {marginsWindow.Title}");
};

marginsWindow.Show();
```

*   [Overview of WPF windows](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/)
*   [How to open a window or dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-window-dialog-box)
*   [How to open a common dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-common-system-dialog-box)
*   [How to open a message box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-message-box)
*   [How to close a window or dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-close-window-dialog-box)
*   [Dialog Box Sample](https://github.com/Microsoft/WPF-Samples/tree/master/Windows/DialogBox)
*   [System.Windows.Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window)
*   [System.Windows.MessageBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.messagebox)
