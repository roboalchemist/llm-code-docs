# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/walkthrough-my-first-wpf-desktop-application

Title: Create your first WPF app in Visual Studio 2019 - .NET Framework

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/walkthrough-my-first-wpf-desktop-application

Published Time: Mon, 09 Feb 2026 08:05:35 GMT

Markdown Content:
This article shows you how to develop a Windows Presentation Foundation (WPF) desktop application that includes the elements that are common to most WPF applications: Extensible Application Markup Language (XAML) markup, code-behind, application definitions, controls, layout, data binding, and styles. To develop the application, you'll use Visual Studio.

In this tutorial, you learn how to:

*   Create a WPF project.
*   Use XAML to design the appearance of the application's user interface (UI).
*   Write code to build the application's behavior.
*   Create an application definition to manage the application.
*   Add controls and create the layout to compose the application UI.
*   Create styles for a consistent appearance throughout the application's UI.
*   Bind the UI to data, both to populate the UI from data and to keep the data and UI synchronized.

By the end of the tutorial, you'll have built a standalone Windows application that allows users to view expense reports for selected people. The application is composed of several WPF pages that are hosted in a browser-style window.

Tip

The sample code that is used in this tutorial is available for both Visual Basic and C# at [Tutorial WPF App Sample Code](https://github.com/Microsoft/WPF-Samples/tree/master/Getting%20Started/WalkthroughFirstWPFApp).

You can toggle the code language of the sample code between C# and Visual Basic by using the language selector on top of this page.

*   [Visual Studio 2019](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **.NET desktop development** workload installed.

For more information about installing the latest version of Visual Studio, see [Install Visual Studio](https://learn.microsoft.com/en-us/visualstudio/install/install-visual-studio).

The first step is to create the application infrastructure, which includes an application definition, two pages, and an image.

1.   Create a new WPF Application project in Visual Basic or Visual C# named **`ExpenseIt`**:

    1.   Open Visual Studio and select **Create a new project** under the **Get started** menu.

The **Create a new project** dialog opens.

    2.   In the **Language** dropdown, select either **C#** or **Visual Basic**.

    3.   Select the **WPF App (.NET Framework)** template and then select **Next**.

![Image 1: Create a new project dialog](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/create-new-project-dialog.png)

The **Configure your new project** dialog opens.

    4.   Enter the project name **`ExpenseIt`** and then select **Create**.

![Image 2: Configure a new project dialog](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/configure-new-project-dialog.png)

Visual Studio creates the project and opens the designer for the default application window named **MainWindow.xaml**.

2.   Open _Application.xaml_ (Visual Basic) or _App.xaml_ (C#).

This XAML file defines a WPF application and any application resources. You also use this file to specify the UI, in this case _MainWindow.xaml_, that automatically shows when the application starts.

Your XAML should look like the following in Visual Basic:

```
<Application x:Class="Application"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    StartupUri="MainWindow.xaml">
    <Application.Resources>
        
    </Application.Resources>
</Application>
```

And like the following in C#:

```
<Application x:Class="ExpenseIt.App"
     xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
     StartupUri="MainWindow.xaml">
    <Application.Resources>
         
    </Application.Resources>
</Application>
```
3.   Open _MainWindow.xaml_.

This XAML file is the main window of your application and displays content created in pages. The [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) class defines the properties of a window, such as its title, size, or icon, and handles events, such as closing or hiding.

4.   Change the [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) element to a [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow), as shown in the following XAML:

```
<NavigationWindow x:Class="ExpenseIt.MainWindow"
     xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
     ...
</NavigationWindow>
```

This app navigates to different content depending on the user input. This is why the main [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) needs to be changed to a [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow). [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow) inherits all the properties of [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window). The [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow) element in the XAML file creates an instance of the [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow) class. For more information, see [Navigation overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/navigation-overview).

5.   Remove the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) elements from between the [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow) tags.

6.   Change the following properties in the XAML code for the [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow) element:

    *   Set the [Title](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.title) property to "`ExpenseIt`".

    *   Set the [Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.height) property to 350 pixels.

    *   Set the [Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.width) property to 500 pixels.

Your XAML should look like the following for Visual Basic:

```
<NavigationWindow x:Class="MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="ExpenseIt" Height="350" Width="500">
 
</NavigationWindow>
```

And like the following for C#:

```
<NavigationWindow x:Class="ExpenseIt.MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="ExpenseIt" Height="350" Width="500">
    
</NavigationWindow>
```
7.   Open _MainWindow.xaml.vb_ or _MainWindow.xaml.cs_.

This file is a code-behind file that contains code to handle the events declared in _MainWindow.xaml_. This file contains a partial class for the window defined in XAML.

8.   If you're using C#, change the `MainWindow` class to derive from [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow). (In Visual Basic, this happens automatically when you change the window in XAML.) Your C# code should now look like this:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ExpenseIt
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : NavigationWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }
    }
}
```

In this section, you'll add two pages and an image to the application.

1.   Add a new page to the project, and name it _`ExpenseItHome.xaml`_:

    1.   In **Solution Explorer**, right-click on the **`ExpenseIt`** project node and choose **Add**>**Page**.

    2.   In the **Add New Item** dialog, the **Page (WPF)** template is already selected. Enter the name **`ExpenseItHome`**, and then select **Add**.

This page is the first page that's displayed when the application is launched. It will show a list of people to select from, to show an expense report for.

2.   Open _`ExpenseItHome.xaml`_.

3.   Set the [Title](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.page.title) to "`ExpenseIt - Home`".

4.   Set the `DesignHeight` to 350 pixels and the `DesignWidth` to 500 pixels.

The XAML now appears as follows for Visual Basic:

```
<Page x:Class="ExpenseItHome"
  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
  xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
  mc:Ignorable="d" 
  d:DesignHeight="350" d:DesignWidth="500"
  Title="ExpenseIt - Home">
    <Grid>
        
    </Grid>
</Page>
```

And like the following for C#:

```
<Page x:Class="ExpenseIt.ExpenseItHome"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
      xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
      mc:Ignorable="d" 
      d:DesignHeight="350" d:DesignWidth="500"
    Title="ExpenseIt - Home">

    <Grid>
        
    </Grid>
</Page>
```
5.   Open _MainWindow.xaml_.

6.   Add a [Source](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow.source) property to the [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow) element and set it to "`ExpenseItHome.xaml`".

This sets _`ExpenseItHome.xaml`_ to be the first page opened when the application starts.

Example XAML in Visual Basic:

```
<NavigationWindow x:Class="MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="ExpenseIt" Height="350" Width="500" Source="ExpenseItHome.xaml">
    
</NavigationWindow>
```

And in C#:

```
<NavigationWindow x:Class="ExpenseIt.MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="ExpenseIt" Height="350" Width="500" Source="ExpenseItHome.xaml">
    
</NavigationWindow>
```
Tip

You can also set the **Source** property in the **Miscellaneous** category of the **Properties** window.

![Image 3: Source property in Properties window](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/properties-source.png) 
7.   Add another new WPF page to the project, and name it _ExpenseReportPage.xaml_::

    1.   In **Solution Explorer**, right-click on the **`ExpenseIt`** project node and choose **Add**>**Page**.

    2.   In the **Add New Item** dialog, select the **Page (WPF)** template. Enter the name **ExpenseReportPage**, and then select **Add**.

This page will show the expense report for the person that is selected on the **`ExpenseItHome`** page.

8.   Open _ExpenseReportPage.xaml_.

9.   Set the [Title](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.page.title) to "`ExpenseIt - View Expense`".

10.   Set the `DesignHeight` to 350 pixels and the `DesignWidth` to 500 pixels.

_ExpenseReportPage.xaml_ now looks like the following in Visual Basic:

```
<Page x:Class="ExpenseReportPage"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
      xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
      mc:Ignorable="d" 
      d:DesignHeight="350" d:DesignWidth="500"
      Title="ExpenseIt - View Expense">
    <Grid>
        
    </Grid>
</Page>
```

And like the following in C#:

```
<Page x:Class="ExpenseIt.ExpenseReportPage"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
      xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
      mc:Ignorable="d" 
      d:DesignHeight="350" d:DesignWidth="500"
    Title="ExpenseIt - View Expense">

    <Grid>
        
    </Grid>
</Page>
```
11.   Open _ExpenseItHome.xaml.vb_ and _ExpenseReportPage.xaml.vb_, or _ExpenseItHome.xaml.cs_ and _ExpenseReportPage.xaml.cs_.

When you create a new Page file, Visual Studio automatically creates its _code-behind_ file. These code-behind files handle the logic for responding to user input.

Your code should look like the following for **`ExpenseItHome`**:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ExpenseIt
{
    /// <summary>
    /// Interaction logic for ExpenseItHome.xaml
    /// </summary>
    public partial class ExpenseItHome : Page
    {
        public ExpenseItHome()
        {
            InitializeComponent();
        }
    }
}
```

And like the following for **ExpenseReportPage**:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ExpenseIt
{
    /// <summary>
    /// Interaction logic for ExpenseReportPage.xaml
    /// </summary>
    public partial class ExpenseReportPage : Page
    {
        public ExpenseReportPage()
        {
            InitializeComponent();
        }
    }
}
```
12.   Add an image named _watermark.png_ to the project. You can create your own image, copy the file from the sample code, or get it from the [microsoft/WPF-Samples](https://raw.githubusercontent.com/microsoft/WPF-Samples/master/Getting%20Started/WalkthroughFirstWPFApp/csharp/watermark.png) GitHub repository.

    1.   Right-click on the project node and select **Add**>**Existing Item**, or press **Shift**+**Alt**+**A**.

    2.   In the **Add Existing Item** dialog, set the file filter to either **All Files** or **Image Files**, browse to the image file you want to use, and then select **Add**.

    3.   Select the image file in **Solution Explorer**, then in the **Properties** window, set **Build Action** to **Resource**.

1.   To build and run the application, press **F5** or select **Start Debugging** from the **Debug** menu.

The following illustration shows the application with the [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow) buttons:

![Image 4: Application after you build and run it.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/build-run-application.png)

2.   Close the application to return to Visual Studio.

Layout provides an ordered way to place UI elements, and also manages the size and position of those elements when a UI is resized. You typically create a layout with one of the following layout controls:

*   [Canvas](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.canvas) - Defines an area within which you can explicitly position child elements by using coordinates that are relative to the Canvas area.
*   [DockPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel) - Defines an area where you can arrange child elements either horizontally or vertically, relative to each other.
*   [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) - Defines a flexible grid area that consists of columns and rows.
*   [StackPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.stackpanel) - Arranges child elements into a single line that can be oriented horizontally or vertically.
*   [VirtualizingStackPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.virtualizingstackpanel) - Arranges and virtualizes content on a single line that is oriented either horizontally or vertically.
*   [WrapPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.wrappanel) - Positions child elements in sequential position from left to right, breaking content to the next line at the edge of the containing box. Subsequent ordering happens sequentially from top to bottom or from right to left, depending on the value of the Orientation property.

Each of these layout controls supports a particular type of layout for its child elements. `ExpenseIt` pages can be resized, and each page has elements that are arranged horizontally and vertically alongside other elements. In this example, the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) is used as layout element for the application.

Tip

For more information about [Panel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.panel) elements, see [Panel](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/panel). For more information about layout, see [Layout](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/layout).

In this section, you create a single-column table with three rows and a 10-pixel margin by adding column and row definitions to the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) in _`ExpenseItHome.xaml`_.

1.   In _`ExpenseItHome.xaml`_, set the [Margin](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.margin) property on the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) element to "10,0,10,10", which corresponds to left, top, right and bottom margins:

```
<Grid Margin="10,0,10,10">
```
Tip

You can also set the **Margin** values in the **Properties** window, under the **Layout** category:

![Image 5: Margin values in Properties window](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/properties-margin.png) 
2.   Add the following XAML between the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) tags to create the row and column definitions:

```
<Grid.ColumnDefinitions>
    <ColumnDefinition />
</Grid.ColumnDefinitions>
<Grid.RowDefinitions>
    <RowDefinition Height="Auto"/>
    <RowDefinition />
    <RowDefinition Height="Auto"/>
</Grid.RowDefinitions>
```

The [Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.rowdefinition.height) of two rows is set to [Auto](https://learn.microsoft.com/en-us/dotnet/api/system.windows.gridlength.auto), which means that the rows are sized based on the content in the rows. The default [Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.rowdefinition.height) is [Star](https://learn.microsoft.com/en-us/dotnet/api/system.windows.gridunittype#system-windows-gridunittype-star) sizing, which means that the row height is a weighted proportion of the available space. For example if two rows each have a [Height](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.rowdefinition.height) of "*", they each have a height that is half of the available space.

Your [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) should now contain the following XAML:

```
<Grid Margin="10,0,10,10">
    <Grid.ColumnDefinitions>
        <ColumnDefinition />
    </Grid.ColumnDefinitions>
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto"/>
        <RowDefinition />
        <RowDefinition Height="Auto"/>
    </Grid.RowDefinitions>
</Grid>
```

In this section, you'll update the home page UI to show a list of people, where you select one person to display their expense report. Controls are UI objects that allow users to interact with your application. For more information, see [Controls](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/).

To create this UI, you'll add the following elements to _`ExpenseItHome.xaml`_:

*   A [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listbox) (for the list of people).
*   A [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.label) (for the list header).
*   A [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button) (to click to view the expense report for the person that is selected in the list).

Each control is placed in a row of the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) by setting the [Grid.Row](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid.row) attached property. For more information about attached properties, see [Attached Properties Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/properties/attached-properties-overview).

1.   In _`ExpenseItHome.xaml`_, add the following XAML somewhere between the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) tags:

```
<!-- People list -->
<Border Grid.Column="0" Grid.Row="0" Height="35" Padding="5" Background="#4E87D4">
    <Label VerticalAlignment="Center" Foreground="White">Names</Label>
</Border>
<ListBox Name="peopleListBox" Grid.Column="0" Grid.Row="1">
    <ListBoxItem>Mike</ListBoxItem>
    <ListBoxItem>Lisa</ListBoxItem>
    <ListBoxItem>John</ListBoxItem>
    <ListBoxItem>Mary</ListBoxItem>
</ListBox>

<!-- View report button -->
<Button Grid.Column="0" Grid.Row="2" Margin="0,10,0,10" Width="125" Height="25" HorizontalAlignment="Right">View</Button>
```
Tip

You can also create the controls by dragging them from the **Toolbox** window onto the design window, and then setting their properties in the **Properties** window. 
2.   Build and run the application.

The following illustration shows the controls you created:

![Image 6: ExpenseIt sample screenshot displaying a list of names](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/add-application-controls.png)

In this section, you'll update the home page UI with an image and a page title.

1.   In _`ExpenseItHome.xaml`_, add another column to the [ColumnDefinitions](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid.columndefinitions) with a fixed [Width](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.columndefinition.width) of 230 pixels:

```
<Grid.ColumnDefinitions>
    <ColumnDefinition Width="230" />
    <ColumnDefinition />
</Grid.ColumnDefinitions>
```
2.   Add another row to the [RowDefinitions](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid.rowdefinitions), for a total of four rows:

```
<Grid.RowDefinitions>
    <RowDefinition/>
    <RowDefinition Height="Auto"/>
    <RowDefinition />
    <RowDefinition Height="Auto"/>
</Grid.RowDefinitions>
```
3.   Move the controls to the second column by setting the [Grid.Column](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid.column) property to 1 in each of the three controls (Border, ListBox, and Button).

4.   Move each control down a row by incrementing its [Grid.Row](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid.row) value by 1 for each of the three controls (Border, ListBox, and Button) and for the Border element.

The XAML for the three controls now looks like the following:

```
<Border Grid.Column="1" Grid.Row="1" Height="35" Padding="5" Background="#4E87D4">
      <Label VerticalAlignment="Center" Foreground="White">Names</Label>
  </Border>
  <ListBox Name="peopleListBox" Grid.Column="1" Grid.Row="2">
      <ListBoxItem>Mike</ListBoxItem>
      <ListBoxItem>Lisa</ListBoxItem>
      <ListBoxItem>John</ListBoxItem>
      <ListBoxItem>Mary</ListBoxItem>
  </ListBox>

  <!-- View report button -->
  <Button Grid.Column="1" Grid.Row="3" Margin="0,10,0,0" Width="125"
Height="25" HorizontalAlignment="Right">View</Button>
```
5.   Set the [Background](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.panel.background) property to the _watermark.png_ image file, by adding the following XAML anywhere between the `<Grid>` and `</Grid>` tags:

```
<Grid.Background>
    <ImageBrush ImageSource="watermark.png"/>
</Grid.Background>
```
6.   Before the [Border](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.border) element, add a [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.label) with the content "View Expense Report". This label is the title of the page.

```
<Label Grid.Column="1" VerticalAlignment="Center" FontFamily="Trebuchet MS" 
        FontWeight="Bold" FontSize="18" Foreground="#0066cc">
    View Expense Report
</Label>
```
7.   Build and run the application.

The following illustration shows the results of what you just added:

![Image 7: ExpenseIt sample screenshot showing the new image background and page title](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/add-application-image-title.png)

1.   In _`ExpenseItHome.xaml`_, add a [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.buttonbase.click#system-windows-controls-primitives-buttonbase-click) event handler to the [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button) element. For more information, see [How to: Create a simple event handler](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2010/bb675300(v=vs.100)).

```
<!-- View report button -->
  <Button Grid.Column="1" Grid.Row="3" Margin="0,10,0,0" Width="125"
Height="25" HorizontalAlignment="Right" Click="Button_Click">View</Button>
```
2.   Open _`ExpenseItHome.xaml.vb`_ or _`ExpenseItHome.xaml.cs`_.

3.   Add the following code to the `ExpenseItHome` class to add a button click event handler. The event handler opens the **ExpenseReportPage** page.

```
private void Button_Click(object sender, RoutedEventArgs e)
{
    // View Expense Report
    ExpenseReportPage expenseReportPage = new ExpenseReportPage();
    this.NavigationService.Navigate(expenseReportPage);
}
```

_ExpenseReportPage.xaml_ displays the expense report for the person that's selected on the **`ExpenseItHome`** page. In this section, you'll create the UI for **ExpenseReportPage**. You'll also add background and fill colors to the various UI elements.

1.   Open _ExpenseReportPage.xaml_.

2.   Add the following XAML between the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) tags:

```
<Grid.Background>
     <ImageBrush ImageSource="watermark.png" />
 </Grid.Background>
 <Grid.ColumnDefinitions>
     <ColumnDefinition Width="230" />
     <ColumnDefinition />
 </Grid.ColumnDefinitions>
 <Grid.RowDefinitions>
     <RowDefinition Height="Auto" />
     <RowDefinition />
 </Grid.RowDefinitions>

 <Label Grid.Column="1" VerticalAlignment="Center" FontFamily="Trebuchet MS" 
 FontWeight="Bold" FontSize="18" Foreground="#0066cc">
     Expense Report For:
 </Label>
 <Grid Margin="10" Grid.Column="1" Grid.Row="1">

     <Grid.ColumnDefinitions>
         <ColumnDefinition />
         <ColumnDefinition />
     </Grid.ColumnDefinitions>
     <Grid.RowDefinitions>
         <RowDefinition Height="Auto" />
         <RowDefinition Height="Auto" />
         <RowDefinition />
     </Grid.RowDefinitions>

     <!-- Name -->
     <StackPanel Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="0" Orientation="Horizontal">
         <Label Margin="0,0,0,5" FontWeight="Bold">Name:</Label>
         <Label Margin="0,0,0,5" FontWeight="Bold"></Label>
     </StackPanel>

     <!-- Department -->
     <StackPanel Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="1" Orientation="Horizontal">
         <Label Margin="0,0,0,5" FontWeight="Bold">Department:</Label>
         <Label Margin="0,0,0,5" FontWeight="Bold"></Label>
     </StackPanel>

     <Grid Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="2" VerticalAlignment="Top" 
           HorizontalAlignment="Left">
         <!-- Expense type and Amount table -->
         <DataGrid  AutoGenerateColumns="False" RowHeaderWidth="0" >
             <DataGrid.ColumnHeaderStyle>
                 <Style TargetType="{x:Type DataGridColumnHeader}">
                     <Setter Property="Height" Value="35" />
                     <Setter Property="Padding" Value="5" />
                     <Setter Property="Background" Value="#4E87D4" />
                     <Setter Property="Foreground" Value="White" />
                 </Style>
             </DataGrid.ColumnHeaderStyle>
             <DataGrid.Columns>
                 <DataGridTextColumn Header="ExpenseType" />
                 <DataGridTextColumn Header="Amount"  />
             </DataGrid.Columns>
         </DataGrid>
     </Grid>
 </Grid>
```

This UI is similar to _`ExpenseItHome.xaml`_, except the report data is displayed in a [DataGrid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.datagrid).

3.   Build and run the application.

4.   Select the **View** button.

The expense report page appears. Also notice that the back navigation button is enabled.

The following illustration shows the UI elements added to _ExpenseReportPage.xaml_.

![Image 8: ExpenseIt sample screenshot with the same appearance as in the last section.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/create-application-ui.png)

The appearance of various elements is often the same for all elements of the same type in a UI. UI uses [styles](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/styles-templates-overview) to make appearances reusable across multiple elements. The reusability of styles helps to simplify XAML creation and management. This section replaces the per-element attributes that were defined in previous steps with styles.

1.   Open _Application.xaml_ or _App.xaml_.

2.   Add the following XAML between the [Application.Resources](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.resources) tags:

```
<!-- Header text style -->
<Style x:Key="headerTextStyle">
    <Setter Property="Label.VerticalAlignment" Value="Center"></Setter>
    <Setter Property="Label.FontFamily" Value="Trebuchet MS"></Setter>
    <Setter Property="Label.FontWeight" Value="Bold"></Setter>
    <Setter Property="Label.FontSize" Value="18"></Setter>
    <Setter Property="Label.Foreground" Value="#0066cc"></Setter>
</Style>

<!-- Label style -->
<Style x:Key="labelStyle" TargetType="{x:Type Label}">
    <Setter Property="VerticalAlignment" Value="Top" />
    <Setter Property="HorizontalAlignment" Value="Left" />
    <Setter Property="FontWeight" Value="Bold" />
    <Setter Property="Margin" Value="0,0,0,5" />
</Style>

<!-- DataGrid header style -->
<Style x:Key="columnHeaderStyle" TargetType="{x:Type DataGridColumnHeader}">
    <Setter Property="Height" Value="35" />
    <Setter Property="Padding" Value="5" />
    <Setter Property="Background" Value="#4E87D4" />
    <Setter Property="Foreground" Value="White" />
</Style>

<!-- List header style -->
<Style x:Key="listHeaderStyle" TargetType="{x:Type Border}">
    <Setter Property="Height" Value="35" />
    <Setter Property="Padding" Value="5" />
    <Setter Property="Background" Value="#4E87D4" />
</Style>

<!-- List header text style -->
<Style x:Key="listHeaderTextStyle" TargetType="{x:Type Label}">
    <Setter Property="Foreground" Value="White" />
    <Setter Property="VerticalAlignment" Value="Center" />
    <Setter Property="HorizontalAlignment" Value="Left" />
</Style>

<!-- Button style -->
<Style x:Key="buttonStyle" TargetType="{x:Type Button}">
    <Setter Property="Width" Value="125" />
    <Setter Property="Height" Value="25" />
    <Setter Property="Margin" Value="0,10,0,0" />
    <Setter Property="HorizontalAlignment" Value="Right" />
</Style>
```

This XAML adds the following styles:

    *   `headerTextStyle`: To format the page title [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.label).

    *   `labelStyle`: To format the [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.label) controls.

    *   `columnHeaderStyle`: To format the [DataGridColumnHeader](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.datagridcolumnheader).

    *   `listHeaderStyle`: To format the list header [Border](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.border) controls.

    *   `listHeaderTextStyle`: To format the list header [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.label).

    *   `buttonStyle`: To format the [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button) on `ExpenseItHome.xaml`.

Notice that the styles are resources and children of the [Application.Resources](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application.resources) property element. In this location, the styles are applied to all the elements in an application. For an example of using resources in a .NET app, see [Use Application Resources](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/systems/xaml-resources-how-to-use-application).

3.   In _`ExpenseItHome.xaml`_, replace everything between the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) elements with the following XAML:

```
<Grid.Background>
       <ImageBrush ImageSource="watermark.png"  />
   </Grid.Background>
  
   <Grid.ColumnDefinitions>
       <ColumnDefinition Width="230" />
       <ColumnDefinition />
   </Grid.ColumnDefinitions>
   
   <Grid.RowDefinitions>
       <RowDefinition/>
       <RowDefinition Height="Auto"/>
       <RowDefinition />
       <RowDefinition Height="Auto"/>
   </Grid.RowDefinitions>

   <!-- People list -->
  
   <Label Grid.Column="1" Style="{StaticResource headerTextStyle}" >
       View Expense Report
   </Label>
   
   <Border Grid.Column="1" Grid.Row="1" Style="{StaticResource listHeaderStyle}">
       <Label Style="{StaticResource listHeaderTextStyle}">Names</Label>
   </Border>
   <ListBox Name="peopleListBox" Grid.Column="1" Grid.Row="2">
       <ListBoxItem>Mike</ListBoxItem>
       <ListBoxItem>Lisa</ListBoxItem>
       <ListBoxItem>John</ListBoxItem>
       <ListBoxItem>Mary</ListBoxItem>
   </ListBox>

   <!-- View report button -->
   <Button Grid.Column="1" Grid.Row="3" Click="Button_Click" Style="{StaticResource buttonStyle}">View</Button>
```

The properties such as [VerticalAlignment](https://learn.microsoft.com/en-us/dotnet/api/system.windows.verticalalignment) and [FontFamily](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.fontfamily) that define the look of each control are removed and replaced by applying the styles. For example, the `headerTextStyle` is applied to the "View Expense Report" [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.label).

4.   Open _ExpenseReportPage.xaml_.

5.   Replace everything between the [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) elements with the following XAML:

```
<Grid.Background>
      <ImageBrush ImageSource="watermark.png" />
  </Grid.Background>
  <Grid.ColumnDefinitions>
      <ColumnDefinition Width="230" />
      <ColumnDefinition />
  </Grid.ColumnDefinitions>
  <Grid.RowDefinitions>
      <RowDefinition Height="Auto" />
      <RowDefinition />
  </Grid.RowDefinitions>

  <Label Grid.Column="1" Style="{StaticResource headerTextStyle}">
      Expense Report For:
  </Label>
  <Grid Margin="10" Grid.Column="1" Grid.Row="1">

      <Grid.ColumnDefinitions>
          <ColumnDefinition />
          <ColumnDefinition />
      </Grid.ColumnDefinitions>
      <Grid.RowDefinitions>
          <RowDefinition Height="Auto" />
          <RowDefinition Height="Auto" />
          <RowDefinition />
      </Grid.RowDefinitions>

      <!-- Name -->
      <StackPanel Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="0" Orientation="Horizontal">
          <Label Style="{StaticResource labelStyle}">Name:</Label>
          <Label Style="{StaticResource labelStyle}"></Label>
      </StackPanel>

      <!-- Department -->
      <StackPanel Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="1" 
  Orientation="Horizontal">
          <Label Style="{StaticResource labelStyle}">Department:</Label>
          <Label Style="{StaticResource labelStyle}"></Label>
      </StackPanel>

      <Grid Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="2" VerticalAlignment="Top" 
            HorizontalAlignment="Left">
          <!-- Expense type and Amount table -->
          <DataGrid ColumnHeaderStyle="{StaticResource columnHeaderStyle}" 
                    AutoGenerateColumns="False" RowHeaderWidth="0" >
              <DataGrid.Columns>
                  <DataGridTextColumn Header="ExpenseType" />
                  <DataGridTextColumn Header="Amount"  />
              </DataGrid.Columns>
          </DataGrid>
      </Grid>
  </Grid>
```

This XAML adds styles to the [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.label) and [Border](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.border) elements.

6.   Build and run the application. The window appearance is the same as previously.

![Image 9: ExpenseIt sample screenshot with the same appearance as in the last section.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/create-application-ui.png)

7.   Close the application to return to Visual Studio.

In this section, you'll create the XML data that is bound to various controls.

1.   In _`ExpenseItHome.xaml`_, after the opening [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) element, add the following XAML to create an [XmlDataProvider](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.xmldataprovider) that contains the data for each person:

```
<Grid.Resources>
    <!-- Expense Report Data -->
    <XmlDataProvider x:Key="ExpenseDataSource" XPath="Expenses">
        <x:XData>
            <Expenses xmlns="">
                <Person Name="Mike" Department="Legal">
                    <Expense ExpenseType="Lunch" ExpenseAmount="50" />
                    <Expense ExpenseType="Transportation" ExpenseAmount="50" />
                </Person>
                <Person Name="Lisa" Department="Marketing">
                    <Expense ExpenseType="Document printing"
          ExpenseAmount="50"/>
                    <Expense ExpenseType="Gift" ExpenseAmount="125" />
                </Person>
                <Person Name="John" Department="Engineering">
                    <Expense ExpenseType="Magazine subscription" 
         ExpenseAmount="50"/>
                    <Expense ExpenseType="New machine" ExpenseAmount="600" />
                    <Expense ExpenseType="Software" ExpenseAmount="500" />
                </Person>
                <Person Name="Mary" Department="Finance">
                    <Expense ExpenseType="Dinner" ExpenseAmount="100" />
                </Person>
            </Expenses>
        </x:XData>
    </XmlDataProvider>
</Grid.Resources>
```

The data is created as a [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) resource. Normally this data would be loaded as a file, but for simplicity the data is added inline.

2.   Within the `<Grid.Resources>` element, add the following `<xref:System.Windows.DataTemplate>` element, which defines how to display the data in the [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listbox), after the `<XmlDataProvider>` element:

```
<Grid.Resources>
    <!-- Name item template -->
    <DataTemplate x:Key="nameItemTemplate">
        <Label Content="{Binding XPath=@Name}"/>
    </DataTemplate>
</Grid.Resources>
```

For more information about data templates, see [Data templating overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/data-templating-overview).

3.   Replace the existing [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listbox) with the following XAML:

```
<ListBox Name="peopleListBox" Grid.Column="1" Grid.Row="2" 
         ItemsSource="{Binding Source={StaticResource ExpenseDataSource}, XPath=Person}"
         ItemTemplate="{StaticResource nameItemTemplate}">
</ListBox>
```

This XAML binds the [ItemsSource](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.itemscontrol.itemssource) property of the [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listbox) to the data source and applies the data template as the [ItemTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.itemscontrol.itemtemplate).

Next, you'll add code to retrieve the name that's selected on the **`ExpenseItHome`** page and pass it to the constructor of **ExpenseReportPage**. **ExpenseReportPage** sets its data context with the passed item, which is what the controls defined in _ExpenseReportPage.xaml_ bind to.

1.   Open _ExpenseReportPage.xaml.vb_ or _ExpenseReportPage.xaml.cs_.

2.   Add a constructor that takes an object so you can pass the expense report data of the selected person.

```
public partial class ExpenseReportPage : Page
{
    public ExpenseReportPage()
    {
        InitializeComponent();
    }

    // Custom constructor to pass expense report data
    public ExpenseReportPage(object data):this()
    {
        // Bind to expense report data.
        this.DataContext = data;
    }
}
```
3.   Open _`ExpenseItHome.xaml.vb`_ or _`ExpenseItHome.xaml.cs`_.

4.   Change the [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.buttonbase.click#system-windows-controls-primitives-buttonbase-click) event handler to call the new constructor passing the expense report data of the selected person.

```
private void Button_Click(object sender, RoutedEventArgs e)
{
    // View Expense Report
    ExpenseReportPage expenseReportPage = new ExpenseReportPage(this.peopleListBox.SelectedItem);
    this.NavigationService.Navigate(expenseReportPage);
}
```

In this section, you'll update the UI for each item in the data-bound lists by using data templates.

1.   Open _ExpenseReportPage.xaml_.

2.   Bind the content of the "Name" and "Department" [Label](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.label) elements to the appropriate data source property. For more information about data binding, see [Data binding overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/).

```
<!-- Name -->
<StackPanel Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="0" Orientation="Horizontal">
    <Label Style="{StaticResource labelStyle}">Name:</Label>
    <Label Style="{StaticResource labelStyle}" Content="{Binding XPath=@Name}"></Label>
</StackPanel>

<!-- Department -->
<StackPanel Grid.Column="0" Grid.ColumnSpan="2" Grid.Row="1" Orientation="Horizontal">
    <Label Style="{StaticResource labelStyle}">Department:</Label>
    <Label Style="{StaticResource labelStyle}" Content="{Binding XPath=@Department}"></Label>
</StackPanel>
```
3.   After the opening [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid) element, add the following data templates, which define how to display the expense report data:

```
<!--Templates to display expense report data-->
<Grid.Resources>
    <!-- Reason item template -->
    <DataTemplate x:Key="typeItemTemplate">
        <Label Content="{Binding XPath=@ExpenseType}"/>
    </DataTemplate>
    <!-- Amount item template -->
    <DataTemplate x:Key="amountItemTemplate">
        <Label Content="{Binding XPath=@ExpenseAmount}"/>
    </DataTemplate>
</Grid.Resources>
```
4.   Replace the [DataGridTextColumn](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.datagridtextcolumn) elements with [DataGridTemplateColumn](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.datagridtemplatecolumn) under the [DataGrid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.datagrid) element and apply the templates to them. Also, specify the `ItemsSource` attribute with its value in the `DataGrid` Element.

```
<!-- Expense type and Amount table -->
<DataGrid ItemsSource="{Binding XPath=Expense}" ColumnHeaderStyle="{StaticResource columnHeaderStyle}" AutoGenerateColumns="False" RowHeaderWidth="0" >
   
    <DataGrid.Columns>
        <DataGridTemplateColumn Header="ExpenseType" CellTemplate="{StaticResource typeItemTemplate}" />
        <DataGridTemplateColumn Header="Amount" CellTemplate="{StaticResource amountItemTemplate}" />
    </DataGrid.Columns>
    
</DataGrid>
```
5.   Build and run the application.

6.   Select a person and then select the **View** button.

The following illustration shows both pages of the `ExpenseIt` application with controls, layout, styles, data binding, and data templates applied:

![Image 10: Both pages of the app showing the names list and an expense report.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/walkthrough-my-first-wpf-desktop-application/application-data-templates.png)

In this walkthrough you learned a number of techniques for creating a UI using Windows Presentation Foundation (WPF). You should now have a basic understanding of the building blocks of a data-bound .NET app. For more information about the WPF architecture and programming models, see the following topics:

*   [WPF architecture](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/wpf-architecture)
*   [XAML in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/xaml/)
*   [Dependency properties overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/properties/dependency-properties-overview)
*   [Layout](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/layout)

For more information about creating applications, see the following topics:

*   [Application development](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/)
*   [Controls](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/)
*   [Data binding overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/)
*   [Graphics and multimedia](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/)
*   [Documents in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/documents-in-wpf)

*   [Panel](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/panel)
*   [Data templating overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/data-templating-overview)
*   [Build a WPF application](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/building-a-wpf-application-wpf)
*   [Styles and templates](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/styles-templates-overview)
