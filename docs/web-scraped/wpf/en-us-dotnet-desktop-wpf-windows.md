# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/

Title: Windows in WPF overview - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/

Markdown Content:
Users interact with Windows Presentation Foundation (WPF) applications through windows. The primary purpose of a window is to host content that visualizes data and enables users to interact with data. WPF applications provide their own windows by using the [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) class. This article introduces [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) before covering the fundamentals of creating and managing windows in applications.

Important

This article uses XAML generated from a **C#** project. If you're using **Visual Basic**, the XAML may look slightly different. These differences are typically present on `x:Class` attribute values. C# includes the root namespace for the project while Visual Basic doesn't.

The project templates for C# create an `App` type contained in the _app.xaml_ file. In Visual Basic, the type is named `Application` and the file is named `Application.xaml`.

In WPF, a window is encapsulated by the [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) class that you use to do the following:

*   Display a window.
*   Configure the size, position, and appearance of a window.
*   Host application-specific content.
*   Manage the lifetime of a window.

The following figure illustrates the constituent parts of a window:

![Image 1: Screenshot that shows parts of a WPF window.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/index/window-parts.png)

A window is divided into two areas: the non-client area and client area.

The _non-client area_ of a window is implemented by WPF and includes the parts of a window that are common to most windows, including the following:

*   A title bar (1-5).
*   An icon (1).
*   Title (2).
*   Minimize (3), Maximize (4), and Close (5) buttons.
*   System menu (6) with menu items. Appears when clicking on the icon (1).
*   Border (7).

The _client area_ of a window is the area within a window's non-client area and is used by developers to add application-specific content, such as menu bars, tool bars, and controls.

*   Client area (8).
*   Resize grip (9). This is a control added to the Client area (8).

The implementation of a typical window includes both appearance and behavior, where _appearance_ defines how a window looks to users and _behavior_ defines the way a window functions as users interact with it. In WPF, you can implement the appearance and behavior of a window using either code or XAML markup.

In general, however, the appearance of a window is implemented using XAML markup, and its behavior is implemented using code-behind, as shown in the following example.

```
<Window x:Class="WindowsOverview.Window1"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:WindowsOverview"
        >

    <!-- Client area containing the content of the window -->

</Window>
```

The following code is the code-behind for the XAML.

```
using System.Windows;

namespace WindowsOverview
{
    public partial class Window1 : Window
    {
        public Window1()
        {
            InitializeComponent();
        }
    }
}
```

To enable a XAML markup file and code-behind file to work together, the following are required:

*   In markup, the `Window` element must include the `x:Class` attribute. When the application is built, the existence of `x:Class` attribute causes Microsoft build engine (MSBuild) to generate a `partial` class that derives from [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) with the name that is specified by the `x:Class` attribute. This requires the addition of an XML namespace declaration for the XAML schema (`xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"`). The generated `partial` class implements the `InitializeComponent` method, which is called to register the events and set the properties that are implemented in markup.

*   In code-behind, the class must be a `partial` class with the same name that is specified by the `x:Class` attribute in markup, and it must derive from [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window). This allows the code-behind file to be associated with the `partial` class that is generated for the markup file when the application is built, for more information, see [Compile a WPF Application](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/building-a-wpf-application-wpf).

*   In code-behind, the [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) class must implement a constructor that calls the `InitializeComponent` method. `InitializeComponent` is implemented by the markup file's generated `partial` class to register events and set properties that are defined in markup.

Note

When you add a new [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) to your project by using Visual Studio, the [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) is implemented using both markup and code-behind, and includes the necessary configuration to create the association between the markup and code-behind files as described here.

With this configuration in place, you can focus on defining the appearance of the window in XAML markup and implementing its behavior in code-behind. The following example shows a window with a button that defines an event handler for the [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.buttonbase.click#system-windows-controls-primitives-buttonbase-click) event. This is implemented in the XAML and the handler is implemented in code-behind.

```
<Window x:Class="WindowsOverview.Window1"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:WindowsOverview"
        >

    <!-- Client area containing the content of the window -->

    <Button Click="Button_Click">Click This Button</Button>

</Window>
```

The following code is the code-behind for the XAML.

```
using System.Windows;

namespace WindowsOverview
{
    public partial class Window1 : Window
    {
        public Window1()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Button was clicked.");
        }
    }
}
```

How you implement your window determines how it's configured for MSBuild. For a window that is defined using both XAML markup and code-behind:

*   XAML markup files are configured as MSBuild `Page` items.
*   Code-behind files are configured as MSBuild `Compile` items.

.NET SDK projects automatically import the correct `Page` and `Compile` items for you, and you don't need to declare these. When the project is configured for WPF, the XAML markup files are automatically imported as `Page` items, and the corresponding code-behind file is imported as `Compile`.

MSBuild projects won't automatically import the types and you must declare them yourself:

```
<Project>
    ...
    <Page Include="MarkupAndCodeBehindWindow.xaml" />
    <Compile Include=" MarkupAndCodeBehindWindow.xaml.cs" />
    ...
</Project>
```

For information about building WPF applications, see [Compile a WPF Application](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/building-a-wpf-application-wpf).

As with any class, a window has a lifetime that begins when it's first instantiated, after which it's opened, activated/deactivated, and eventually closed.

To open a window, you first create an instance of it, which is demonstrated in the following example:

```
using System.Windows;

namespace WindowsOverview
{
    public partial class App : Application
    {
        private void Application_Startup(object sender, StartupEventArgs e)
        {
            // Create the window
            Window1 window = new Window1();

            // Open the window
            window.Show();
        }
    }
}
```

In this example `Window1` is instantiated when the application starts, which occurs when the [Startup](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.startup#system-windows-application-startup) event is raised. For more information about the startup window, see [How to get or set the main application window](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-get-set-main-application-window).

When a window is instantiated, a reference to it's automatically added to a [list of windows](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.windows) that is managed by the [Application](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application) object. The first window to be instantiated is automatically set by [Application](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application) as the [main application window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.mainwindow).

The window is finally opened by calling the [Show](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.show) method as shown in the following image:

![Image 2: WPF Window with a single button inside with the text 'Click me'.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/index/window-with-button.png)

A window that is opened by calling [Show](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.show) is a _modeless_ window, and the application doesn't prevent users from interacting with other windows in the application. Opening a window with [ShowDialog](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showdialog) opens a window as _modal_ and restricts user interaction to the specific window. For more information, see [Dialog Boxes Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/dialog-boxes-overview).

When [Show](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.show) is called, a window does initialization work before it's shown to establish infrastructure that allows it to receive user input. When the window is initialized, the [SourceInitialized](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.sourceinitialized#system-windows-window-sourceinitialized) event is raised and the window is shown.

For more information, see [How to open a window or dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-window-dialog-box).

The previous example used the `Startup` event to run code that displayed the initial application window. As a shortcut, instead use [StartupUri](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.startupuri) to specify the path to a XAML file in your application. The application automatically creates and displays the window specified by that property.

```
<Application x:Class="WindowsOverview.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="clr-namespace:WindowsOverview"
             StartupUri="ClippedWindow.xaml">
    <Application.Resources>
         
    </Application.Resources>
</Application>
```

A window that is opened by using the [Show](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.show) method doesn't have an implicit relationship with the window that created it. Users can interact with either window independently of the other, which means that either window can do the following:

*   Cover the other (unless one of the windows has its [Topmost](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.topmost) property set to `true`).
*   Be minimized, maximized, and restored without affecting the other.

Some windows require a relationship with the window that opens them. For example, an Integrated Development Environment (IDE) application may open property windows and tool windows whose typical behavior is to cover the window that creates them. Furthermore, such windows should always close, minimize, maximize, and restore in concert with the window that created them. Such a relationship can be established by making one window _own_ another, and is achieved by setting the [Owner](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.owner) property of the _owned window_ with a reference to the _owner window_. This is shown in the following example.

```
private void Button_Click(object sender, RoutedEventArgs e)
{
    // Create a window and make the current window its owner
    var ownedWindow = new ChildWindow1();
    ownedWindow.Owner = this;
    ownedWindow.Show();
}
```

After ownership is established:

*   The owned window can reference its owner window by inspecting the value of its [Owner](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.owner) property.
*   The owner window can discover all the windows it owns by inspecting the value of its [OwnedWindows](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.ownedwindows) property.

When a window is first opened, it becomes the active window. The _active window_ is the window that is currently capturing user input, such as key strokes and mouse clicks. When a window becomes active, it raises the [Activated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activated#system-windows-window-activated) event.

After a window becomes active, a user can activate another window in the same application, or activate another application. When that happens, the currently active window becomes deactivated and raises the [Deactivated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.deactivated#system-windows-window-deactivated) event. Likewise, when the user selects a currently deactivated window, the window becomes active again and [Activated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activated#system-windows-window-activated) is raised.

One common reason to handle [Activated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activated#system-windows-window-activated) and [Deactivated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.deactivated#system-windows-window-deactivated) is to enable and disable functionality that can only run when a window is active. For example, some windows display interactive content that requires constant user input or attention, including games and video players. The following example is a simplified video player that demonstrates how to handle [Activated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activated#system-windows-window-activated) and [Deactivated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.deactivated#system-windows-window-deactivated) to implement this behavior.

```
<Window x:Class="WindowsOverview.CustomMediaPlayerWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Activated="Window_Activated"
        Deactivated="Window_Deactivated"
        Title="CustomMediaPlayerWindow" Height="450" Width="800">
    <Grid>
        <MediaElement x:Name="mediaElement" Stretch="Fill"
                      LoadedBehavior="Manual" Source="numbers.mp4" />
    </Grid>
</Window>
```

The following code is the code-behind for the XAML.

```
using System;
using System.Windows;

namespace WindowsOverview
{
    public partial class CustomMediaPlayerWindow : Window
    {
        public CustomMediaPlayerWindow() =>
            InitializeComponent();

        private void Window_Activated(object sender, EventArgs e)
        {
            // Continue playing media if window is activated
            mediaElement.Play();
        }

        private void Window_Deactivated(object sender, EventArgs e)
        {
            // Pause playing if media is being played and window is deactivated
            mediaElement.Pause();
        }
    }
}
```

Other types of applications may still run code in the background when a window is deactivated. For example, a mail client may continue polling the mail server while the user is using other applications. Applications like these often provide different or extra behavior while the main window is deactivated. For a mail program, this may mean both adding the new mail item to the inbox and adding a notification icon to the system tray. A notification icon need only be displayed when the mail window isn't active, which is determined by inspecting the [IsActive](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.isactive) property.

If a background task completes, a window may want to notify the user more urgently by calling [Activate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activate) method. If the user is interacting with another application activated when [Activate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activate) is called, the window's taskbar button flashes. However, if a user is interacting with the current application, calling [Activate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activate) will bring the window to the foreground.

There are scenarios where windows shouldn't be activated when shown, such as conversation windows of a chat application or notification windows of an email application.

If your application has a window that shouldn't be activated when shown, you can set its [ShowActivated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showactivated) property to `false` before calling the [Show](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.show) method for the first time. As a consequence:

*   The window isn't activated.
*   The window's [Activated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activated#system-windows-window-activated) event isn't raised.
*   The currently activated window remains activated.

The window will become activated, however, as soon as the user activates it by clicking either the client or non-client area. In this case:

*   The window is activated.
*   The window's [Activated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activated#system-windows-window-activated) event is raised.
*   The previously activated window is deactivated.
*   The window's [Deactivated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.deactivated#system-windows-window-deactivated) and [Activated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.activated#system-windows-window-activated) events are then raised as expected in response to user actions.

The life of a window starts coming to an end when a user closes it. Once a window is closed, it can't be reopened. A window can be closed by using elements in the non-client area, including the following:

*   The **Close** item of the **System** menu.
*   Pressing ALT + F4.
*   Pressing the **Close** button.
*   Pressing ESC when a button has the [IsCancel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button.iscancel) property set to `true` on a modal window.

You can provide more mechanisms to the client area to close a window, the more common of which include the following:

*   An **Exit** item in the **File** menu, typically for main application windows.
*   A **Close** item in the **File** menu, typically on a secondary application window.
*   A **Cancel** button, typically on a modal dialog box.
*   A **Close** button, typically on a modeless dialog box.

To close a window in response to one of these custom mechanisms, you need to call the [Close](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.close) method. The following example implements the ability to close a window by choosing **Exit** from a **File** menu.

```
<Window x:Class="WindowsOverview.ClosingWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="ClosingWindow" Height="450" Width="800">
    <StackPanel>
        <Menu>
            <MenuItem Header="_File">
                <MenuItem Header="E_xit" Click="fileExitMenuItem_Click" />
            </MenuItem>
        </Menu>
    </StackPanel>
</Window>
```

The following code is the code-behind for the XAML.

```
using System.Windows;

namespace WindowsOverview
{
    public partial class ClosingWindow : Window
    {
        public ClosingWindow() =>
            InitializeComponent();

        private void fileExitMenuItem_Click(object sender, RoutedEventArgs e)
        {
            // Close the current window
            this.Close();
        }
    }
}
```

Note

An application can be configured to shut down automatically when either the main application window closes (see [MainWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.mainwindow)) or the last window closes. For more information, see [ShutdownMode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.shutdownmode).

While a window can be explicitly closed through mechanisms provided in the non-client and client areas, a window can also be implicitly closed as a result of behavior in other parts of the application or Windows, including the following:

*   A user logs off or shuts down Windows.
*   A window's [Owner](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.owner) closes.
*   The main application window is closed and [ShutdownMode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.shutdownmode) is [OnMainWindowClose](https://learn.microsoft.com/en-us/dotnet/api/system.windows.shutdownmode#system-windows-shutdownmode-onmainwindowclose).
*   [Shutdown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.shutdown) is called.

Important

A window can't be reopened after it's closed.

When a window closes, it raises two events: [Closing](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closing#system-windows-window-closing) and [Closed](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closed#system-windows-window-closed).

[Closing](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closing#system-windows-window-closing) is raised before the window closes, and it provides a mechanism by which window closure can be prevented. One common reason to prevent window closure is if window content contains modified data. In this situation, the [Closing](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closing#system-windows-window-closing) event can be handled to determine whether data is dirty and, if so, to ask the user whether to either continue closing the window without saving the data or to cancel window closure. The following example shows the key aspects of handling [Closing](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closing#system-windows-window-closing).

```
<Window x:Class="WindowsOverview.DataWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="DataWindow" Height="450" Width="800"
        Closing="Window_Closing">
    <Grid>
        <TextBox x:Name="documentTextBox" TextChanged="documentTextBox_TextChanged" />
    </Grid>
</Window>
```

The following code is the code-behind for the XAML.

```
using System.Windows;
using System.Windows.Controls;

namespace WindowsOverview
{
    public partial class DataWindow : Window
    {
        private bool _isDataDirty;

        public DataWindow() =>
            InitializeComponent();

        private void documentTextBox_TextChanged(object sender, TextChangedEventArgs e) =>
            _isDataDirty = true;

        private void Window_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            // If data is dirty, prompt user and ask for a response
            if (_isDataDirty)
            {
                var result = MessageBox.Show("Document has changed. Close without saving?",
                                             "Question",
                                             MessageBoxButton.YesNo);

                // User doesn't want to close, cancel closure
                if (result == MessageBoxResult.No)
                    e.Cancel = true;
            }
        }
    }
}
```

The [Closing](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closing#system-windows-window-closing) event handler is passed a [CancelEventArgs](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.canceleventargs), which implements the [Cancel](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.canceleventargs.cancel) property that you set to `true` to prevent a window from closing.

If [Closing](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closing#system-windows-window-closing) isn't handled, or it's handled but not canceled, the window will close. Just before a window actually closes, [Closed](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.closed#system-windows-window-closed) is raised. At this point, a window can't be prevented from closing.

The following illustration shows the sequence of the principal events in the lifetime of a window:

![Image 3: Diagram that shows events in a window's lifetime.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/index/window-lifetime-events.png)

The following illustration shows the sequence of the principal events in the lifetime of a window that is shown without activation ([ShowActivated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showactivated) is set to `false` before the window is shown):

![Image 4: Diagram that shows events in a window's lifetime without activation.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/index/window-lifetime-no-activation.png)

While a window is open, it has a location in the x and y dimensions relative to the desktop. This location can be determined by inspecting the [Left](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.left) and [Top](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.top) properties, respectively. Set these properties to change the location of the window.

You can also specify the initial location of a [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) when it first appears by setting the [WindowStartupLocation](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstartuplocation) property with one of the following [WindowStartupLocation](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstartuplocation) enumeration values:

*   [CenterOwner](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstartuplocation#system-windows-windowstartuplocation-centerowner) (default)
*   [CenterScreen](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstartuplocation#system-windows-windowstartuplocation-centerscreen)
*   [Manual](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstartuplocation#system-windows-windowstartuplocation-manual)

If the startup location is specified as [Manual](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstartuplocation#system-windows-windowstartuplocation-manual), and the [Left](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.left) and [Top](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.top) properties have not been set, [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) will ask the operating system for a location to appear in.

Besides having an x and y location, a window also has a location in the z dimension, which determines its vertical position with respect to other windows. This is known as the window's z-order, and there are two types: **normal** z-order and **topmost** z-order. The location of a window in the _normal z-order_ is determined by whether it's currently active or not. By default, a window is located in the normal z-order. The location of a window in the _topmost z-order_ is also determined by whether it's currently active or not. Furthermore, windows in the topmost z-order are always located above windows in the normal z-order. A window is located in the topmost z-order by setting its [Topmost](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.topmost) property to `true`.

Within each z-order type, the currently active window appears above all other windows in the same z-order.

Besides having a desktop location, a window has a size that is determined by several properties, including the various width and height properties and [SizeToContent](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.sizetocontent).

[MinWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.minwidth), [Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.width), and [MaxWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxwidth) are used to manage the range of widths that a window can have during its lifetime.

```
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    MinWidth="300" Width="400" MaxWidth="500">
</Window>
```

Window height is managed by [MinHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.minheight), [Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.height), and [MaxHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxheight).

```
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    MinHeight="300" Height="400" MaxHeight="500">
</Window>
```

Because the various width values and height values each specify a range, it's possible for the width and height of a resizable window to be anywhere within the specified range for the respective dimension. To detect its current width and height, inspect [ActualWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.actualwidth) and [ActualHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.actualheight), respectively.

If you'd like the width and height of your window to have a size that fits to the size of the window's content, you can use the [SizeToContent](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.sizetocontent) property, which has the following values:

*   [SizeToContent.Manual](https://learn.microsoft.com/en-us/dotnet/api/system.windows.sizetocontent#system-windows-sizetocontent-manual)

 No effect (default).
*   [SizeToContent.Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.sizetocontent#system-windows-sizetocontent-width)

 Fit to content width, which has the same effect as setting both [MinWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.minwidth) and [MaxWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxwidth) to the width of the content.
*   [SizeToContent.Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.sizetocontent#system-windows-sizetocontent-height)

 Fit to content height, which has the same effect as setting both [MinHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.minheight) and [MaxHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxheight) to the height of the content.
*   [SizeToContent.WidthAndHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.sizetocontent#system-windows-sizetocontent-widthandheight)

 Fit to content width and height, which has the same effect as setting both [MinHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.minheight) and [MaxHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxheight) to the height of the content, and setting both [MinWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.minwidth) and [MaxWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxwidth) to the width of the content.

The following example shows a window that automatically sizes to fit its content, both vertically and horizontally, when first shown.

```
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    SizeToContent="WidthAndHeight">
</Window>
```

The following example shows how to set the [SizeToContent](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.sizetocontent) property in code to specify how a window resizes to fit its content .

```
// Manually alter window height and width
this.SizeToContent = SizeToContent.Manual;

// Automatically resize width relative to content
this.SizeToContent = SizeToContent.Width;

// Automatically resize height relative to content
this.SizeToContent = SizeToContent.Height;

// Automatically resize height and width relative to content
this.SizeToContent = SizeToContent.WidthAndHeight;
```

Essentially, the various sizes properties of a window combine to define the range of width and height for a resizable window. To ensure a valid range is maintained, [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) evaluates the values of the size properties using the following orders of precedence.

**For Height Properties:**

1.   [FrameworkElement.MinHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.minheight)
2.   [FrameworkElement.MaxHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxheight)
3.   [SizeToContent.Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.sizetocontent#system-windows-sizetocontent-height) / [SizeToContent.WidthAndHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.sizetocontent#system-windows-sizetocontent-widthandheight)
4.   [FrameworkElement.Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.height)

**For Width Properties:**

1.   [FrameworkElement.MinWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.minwidth)
2.   [FrameworkElement.MaxWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxwidth)
3.   [SizeToContent.Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.sizetocontent#system-windows-sizetocontent-width) / [SizeToContent.WidthAndHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.sizetocontent#system-windows-sizetocontent-widthandheight)
4.   [FrameworkElement.Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.width)

The order of precedence can also determine the size of a window when it's maximized, which is managed with the [WindowState](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstate) property.

During the lifetime of a resizable window, it can have three states: normal, minimized, and maximized. A window with a _normal_ state is the default state of a window. A window with this state allows a user to move and resize it by using a resize grip or the border, if it's resizable.

A window with a _minimized_ state collapses to its task bar button if [ShowInTaskbar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showintaskbar) is set to `true`; otherwise, it collapses to the smallest possible size it can be and moves itself to the bottom-left corner of the desktop. Neither type of minimized window can be resized using a border or resize grip, although a minimized window that isn't shown in the task bar can be dragged around the desktop.

A window with a _maximized_ state expands to the maximum size it can be, which will only be as large as its [MaxWidth](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxwidth), [MaxHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxheight), and [SizeToContent](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.sizetocontent) properties dictate. Like a minimized window, a maximized window can't be resized by using a resize grip or by dragging the border.

Note

The values of the [Top](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.top), [Left](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.left), [Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.width), and [Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.height) properties of a window always represent the values for the normal state, even when the window is currently maximized or minimized.

The state of a window can be configured by setting its [WindowState](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstate) property, which can have one of the following [WindowState](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstate) enumeration values:

*   [Normal](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstate#system-windows-windowstate-normal) (default)
*   [Maximized](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstate#system-windows-windowstate-maximized)
*   [Minimized](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstate#system-windows-windowstate-minimized)

The following example shows how to create a window that is shown as maximized when it opens.

```
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    WindowState="Maximized">
</Window>
```

In general, you should set [WindowState](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstate) to configure the initial state of a window. Once a _resizable_ window is shown, users can press the minimize, maximize, and restore buttons on the window's title bar to change the window state.

You change the appearance of the client area of a window by adding window-specific content to it, such as buttons, labels, and text boxes. To configure the non-client area, [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) provides several properties, which include [Icon](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.icon) to set a window's icon and [Title](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.title) to set its title.

You can also change the appearance and behavior of non-client area border by configuring a window's resize mode, window style, and whether it appears as a button in the desktop task bar.

Depending on the [WindowStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstyle) property, you can control if, and how, users resize the window. The window style affects the following:

*   Allow or disallow resizing by dragging the window border with the mouse.
*   Whether the **Minimize**, **Maximize**, and **Close** buttons appear on the non-client area.
*   Whether the **Minimize**, **Maximize**, and **Close** buttons are enabled.

You can configure how a window resizes by setting its [ResizeMode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.resizemode) property, which can be one of the following [ResizeMode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resizemode) enumeration values:

*   [NoResize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resizemode#system-windows-resizemode-noresize)
*   [CanMinimize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resizemode#system-windows-resizemode-canminimize)
*   [CanResize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resizemode#system-windows-resizemode-canresize) (default)
*   [CanResizeWithGrip](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resizemode#system-windows-resizemode-canresizewithgrip)

As with [WindowStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstyle), the resize mode of a window is unlikely to change during its lifetime, which means that you'll most likely set it from XAML markup.

```
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    ResizeMode="CanResizeWithGrip">
</Window>
```

Note that you can detect whether a window is maximized, minimized, or restored by inspecting the [WindowState](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstate) property.

The border that is exposed from the non-client area of a window is suitable for most applications. However, there are circumstances where different types of borders are needed, or no borders are needed at all, depending on the type of window.

To control what type of border a window gets, you set its [WindowStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstyle) property with one of the following values of the [WindowStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstyle) enumeration:

*   [None](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstyle#system-windows-windowstyle-none)
*   [SingleBorderWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstyle#system-windows-windowstyle-singleborderwindow) (default)
*   [ThreeDBorderWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstyle#system-windows-windowstyle-threedborderwindow)
*   [ToolWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstyle#system-windows-windowstyle-toolwindow)

The effect of applying a window style is illustrated in the following image:

![Image 5: Screenshot that shows how WindowStyle affects a window in WPF.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/index/window-styles.png)

Notice that the image above doesn't show any noticeable difference between `SingleBorderWindow` and `ThreeDBorderWindow`. Back in Windows XP, `ThreeDBorderWindow` did affect how the window was drawn, adding a 3D border to the client area. Starting with Windows 7, the differences between the two styles are minimal.

You can set [WindowStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstyle) using either XAML markup or code. Because it's unlikely to change during the lifetime of a window, you'll most likely configure it using XAML markup.

```
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    WindowStyle="ToolWindow">
</Window>
```

There are also situations where the border styles that [WindowStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstyle) allows you to have aren't sufficient. For example, you may want to create an application with a non-rectangular border, like Microsoft Windows Media Player uses.

For example, consider the speech bubble window shown in the following image:

![Image 6: Screenshot of a WPF window that has a clipped area and custom shape.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/media/index/window-transparent.png)

This type of window can be created by setting the [WindowStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstyle) property to [None](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstyle#system-windows-windowstyle-none), and by using special support that [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) has for transparency.

```
<Window x:Class="WindowsOverview.ClippedWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="ClippedWindow" SizeToContent="WidthAndHeight"
        WindowStyle="None" AllowsTransparency="True" Background="Transparent">
    <Grid Margin="20">
        <Grid.RowDefinitions>
            <RowDefinition Height="*"/>
            <RowDefinition Height="20"/>
        </Grid.RowDefinitions>

        <Rectangle Stroke="#FF000000" RadiusX="10" RadiusY="10"/>
        <Path Fill="White" Stretch="Fill" Stroke="#FF000000" HorizontalAlignment="Left" Margin="15,-5.597,0,-0.003" Width="30" Grid.Row="1" Data="M22.166642,154.45381 L29.999666,187.66699 40.791059,154.54395"/>
        <Rectangle Fill="White" RadiusX="10" RadiusY="10" Margin="1"/>
        
        <TextBlock HorizontalAlignment="Left" VerticalAlignment="Center" FontSize="25" Text="Greetings!" TextWrapping="Wrap" Margin="5,5,50,5"/>
        <Button HorizontalAlignment="Right" VerticalAlignment="Top" Background="Transparent" BorderBrush="{x:Null}" Foreground="Red" Content="❌" FontSize="15" />

        <Grid.Effect>
            <DropShadowEffect BlurRadius="10" ShadowDepth="3" Color="LightBlue"/>
        </Grid.Effect>
    </Grid>
</Window>
```

This combination of values instructs the window to render transparent. In this state, the window's non-client area adornment buttons can't be used and you need to provide your own.

The default appearance of a window includes a taskbar button. Some types of windows don't have a task bar button, such as message boxes, [dialog boxes](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/dialog-boxes-overview), or windows with the [WindowStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.windowstyle) property set to [ToolWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.windowstyle#system-windows-windowstyle-toolwindow). You can control whether the task bar button for a window is shown by setting the [ShowInTaskbar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.showintaskbar) property, which is `true` by default.

```
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    ShowInTaskbar="False">
</Window>
```

[NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow) is a window that is designed to host navigable content.

Dialog boxes are windows that are often used to gather information from a user to complete a function. For example, when a user wants to open a file, the **Open File** dialog box is displayed by an application to get the file name from the user. For more information, see [Dialog Boxes Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/dialog-boxes-overview).

*   [Dialog boxes overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/dialog-boxes-overview)
*   [How to open a window or dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-window-dialog-box)
*   [How to open a common dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-common-system-dialog-box)
*   [How to open a message box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-open-message-box)
*   [How to close a window or dialog box](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/how-to-close-window-dialog-box)
*   [System.Windows.Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window)
*   [System.Windows.MessageBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.messagebox)
*   [System.Windows.Navigation.NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow)
*   [System.Windows.Application](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application)
