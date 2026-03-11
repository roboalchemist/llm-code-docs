# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/create-app-visual-studio

Title: Create a WPF app with Visual Studio tutorial - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/create-app-visual-studio

Markdown Content:
In this tutorial, you learn how to use Visual Studio to create a Windows Presentation Foundation (WPF) app. With Visual Studio, you add controls to windows and handle events. By the end of this tutorial, you have a simple app that adds names to a list box.

In this tutorial, you:

*   Create a new WPF app.
*   Add controls to a window.
*   Handle control events to provide app functionality.
*   Run the app.

Here's a preview of the app created while following this tutorial:

![Image 1: Running a WPF for .NET app in Visual Studio 2026.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/app-finished.png)

*   [Visual Studio 2026](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&0utm_content=download+vs2026+desktopguide+winforms)
    *   Select the [.NET desktop development workload](https://learn.microsoft.com/en-us/visualstudio/install/modify-visual-studio?view=visualstudio&preserve-view=true#change-workloads-or-individual-components)
    *   Select the [.NET 10 individual component](https://learn.microsoft.com/en-us/visualstudio/install/modify-visual-studio?view=visualstudio&preserve-view=true#change-workloads-or-individual-components)

The first step to creating a new app is opening Visual Studio and generating the app from a template.

1.   Open Visual Studio.

2.   Select **Create a new project**.

![Image 2: A screenshot of the start dialog from Visual Studio 2026. The 'create a new project' button is highlighted with a red box.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/vs-start-1-intro.png)

3.   In the **Search for templates** box, type **wpf**, and wait for the search results to appear.

4.   In the **code language** dropdown, choose **C#** or **Visual Basic**.

5.   In the list of templates, select **WPF Application** and then select **Next**.

Important

Don't select the **WPF Application (.NET _Framework_)** template. 
The following image shows both C# and Visual Basic .NET project templates. If you applied the **code language** filter, the corresponding template is listed.

![Image 3: Screenshot of Visual Studio's 'Create a new project' dialog with 'wpf' in the search box and WPF Application templates highlighted.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/vs-start-2-templates.png)

6.   In the **Configure your new project** window, set the **Project name** to _Names_ and select **Next**.

You can also save your project to a different folder by adjusting the **Location** path.

![Image 4: A screenshot of the 'configure your new project' dialog from Visual Studio 2026. The 'Project name' textbox has the word 'Names' in it and is highlighted with a red box. The 'Next' button is also highlighted with a red box.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/vs-start-3-name.png)

7.   Finally, in the **Additional information** window, select **.NET 10.0 (Long Term Support)** for the **Framework** setting, and then select **Create**.

![Image 5: A screenshot of the 'Additional information' dialog from Visual Studio 2026. The 'Framework' dropdown box has '.NET 10 (Long Term Support)' selected and highlighted with a red box. The 'Create' button is also highlighted with a red box.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/vs-start-4-framework.png)

After Visual Studio generates the app, it opens the XAML designer window for the default window, _MainWindow_. If the designer isn't visible, double-click on the _MainWindow.xaml_ file in the **Solution Explorer** window to open the designer.

Support for WPF in Visual Studio has five important components that you interact with as you create an app:

![Image 6: The important components of Visual Studio 2026 you should know when creating a WPF project for .NET.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/vs-main-window.png)

1.   Solution Explorer

All of your project files, code, windows, and resources appear in this window.

2.   Properties

This window shows property settings you can configure based on the context of the item selected. For example, if you select an item from **Solution Explorer**, settings related to the file are displayed. If an object in the **Designer** is selected, the properties of the control or window are displayed.

3.   Toolbox

The toolbox contains all of the controls you can add to a design surface. To add a control to the current surface, double-click a control or drag-and-drop the control to the designer. It's common to instead use the XAML code editor window to design a user interface (UI), while using the XAML designer window to preview the results.

4.   XAML designer

This is the designer for a XAML document. It's interactive and you can drag-and-drop objects from the **Toolbox**. By selecting and moving items in the designer, you can visually compose the UI for your app.

When both the designer and editor are visible, changes to one is reflected in the other.

When you select items in the designer, the **Properties** window displays the properties and attributes about that object.

5.   XAML code editor

This is the XAML code editor for a XAML document. The XAML code editor is a way to craft your UI by hand without a designer. The designer might automatically set properties on a control when the control is added in the designer. The XAML code editor gives you a lot more control.

When both the designer and editor are visible, changes to one is reflected in the other. As you navigate the text caret in the code editor, the **Properties** window displays the properties and attributes about that object.

After you create your project, the XAML code editor opens. It shows a minimal amount of XAML code to display the window. If the editor isn't open, double-click the _MainWindow.xaml_ item in the **Solution Explorer** window. You should see XAML similar to the following example:

```
<Window x:Class="Names.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:Names"
        mc:Ignorable="d"
        Title="MainWindow" Height="450" Width="800">
    <Grid>

    </Grid>
</Window>
```

Important

If you're coding in **Visual Basic**, the XAML is slightly different, specifically the `x:Class=".."` attribute. XAML in Visual Basic uses the object's class name and omits the namespace to the class.

To better understand the XAML, let's break it down. XAML is simply XML that WPF processes to create a UI. To understand XAML, you should, at a minimum, be familiar with the basics of XML.

The document root `<Window>` represents the type of object described by the XAML file. The file declares eight attributes, and they generally belong to three categories:

*   XML namespaces

An XML namespace provides structure to the XML. It determines what XML content you can declare in the file.

The main `xmlns` attribute imports the XML namespace for the entire file. In this case, it maps to the types declared by WPF. The other XML namespaces declare a prefix and import other types and objects for the XAML file. For example, the `xmlns:local` namespace declares the `local` prefix and maps to the objects declared by your project, the ones declared in the `Names` code namespace.

*   `x:Class` attribute

This attribute maps the `<Window>` to the type defined by your code: the _MainWindow.xaml.cs_ or _MainWindow.xaml.vb_ file, which is the `Names.MainWindow` class in C# and `MainWindow` in Visual Basic.

*   `Title` attribute

Any normal attribute you declare on the XAML object sets a property of that object. In this case, the `Title` attribute sets the `Window.Title` property.

For our example app, this window is too large, and the title bar isn't descriptive. Let's fix that.

1.   First, run the app by pressing the F5 key or by selecting **Debug**>**Start Debugging** from the menu.

You see the default window generated by the template, without any controls, and a title of **MainWindow**:

![Image 7: A blank WPF app](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/app-default.png)

2.   Change the title of the window by setting the `Title` to `Names`.

3.   Change the size of the window by setting the `Height` to `180` and `Width` to `260`.

```
<Window x:Class="Names.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:Names"
        mc:Ignorable="d"
        Title="Names" Height="180" Width="260">
    <Grid>
        
    </Grid>
</Window>
```

WPF provides a powerful layout system with many different layout controls. Layout controls help place and size child controls, and can even do so automatically. The default layout control provided in this XAML is the `<Grid>` control.

The grid control lets you define rows and columns, much like a table, and place controls within the bounds of a specific row and column combination. You can add any number of child controls or other layout controls to the grid. For example, you can place another `<Grid>` control in a specific row and column combination, and that new grid can then define more rows and columns and have its own children.

The grid control places its child controls in rows and columns. A grid always has a single row and column declared, meaning, the grid by default is a single cell. That default setting doesn't give you much flexibility in placing controls.

Adjust the grid's layout for the controls required for this app.

1.   Add a new attribute to the `<Grid>` element: `Margin="10"`.

This setting brings the grid in from the window edges and makes it look a little nicer.

2.   Define two rows and two columns, dividing the grid into four cells:

```
<Grid Margin="10">
    
    <Grid.RowDefinitions>
        <RowDefinition Height="*" />
        <RowDefinition Height="*" />
    </Grid.RowDefinitions>

    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="*" />
        <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>
    
</Grid>
```
3.   Select the grid in either the XAML code editor or XAML designer. The XAML designer shows each row and column:

![Image 8: A WPF app with the margin set on a grid](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/vs-designer-grid-rows-columns.png)

Now that the grid is configured, you can start adding controls to it. First, add the label control.

1.   Create a new `<Label>` element inside the `<Grid>` element, after the row and column definitions. Set the content of the element to the string value `Names`:

```
<Grid Margin="10">

    <Grid.RowDefinitions>
        <RowDefinition Height="*" />
        <RowDefinition Height="*" />
    </Grid.RowDefinitions>

    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="*" />
        <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>

    <Label>Names</Label>

</Grid>
```

The `<Label>Names</Label>` defines the content `Names`. Some controls understand how to handle content, others don't. The content of a control maps to the `Content` property. If you set the content through XAML attribute syntax, use this format: `<Label Content="Names" />`. Both ways accomplish the same thing, setting the content of the label to display the text `Names`.

The label takes up half the window, as it was automatically positioned to the first row and column of the grid. For the first row, you don't need that much space because you're only going to use that row for the label.

2.   Change the `Height` attribute of the first `<RowDefinition>` from `*` to `Auto`.

The `Auto` value automatically sizes the grid row to the size of its contents, in this case, the label control.

```
<Grid.RowDefinitions>
    <RowDefinition Height="Auto" />
    <RowDefinition Height="*" />
</Grid.RowDefinitions>
```

The designer now shows the label occupying a small amount of the available height. There's more room for the next row to occupy.

![Image 9: A WPF app with the margin set on a grid and a label control in the first row](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/vs-designer-grid-rows-columns-label.png)

Let's talk about control placement. The label you created in the previous section is automatically placed in row 0 and column 0 of the grid. The numbering for rows and columns starts at 0 and increments by 1. The control doesn't know anything about the grid, and the control doesn't define any properties to control its placement within the grid.

How do you tell a control to use a different row or column when the control has no knowledge of the grid? Attached properties! The grid takes advantage of the property system provided by WPF.

The grid control defines new properties that the child controls can attach to themselves. The properties don't actually exist on the control itself, but they become available to the control once it's added to the grid.

The grid defines two properties to determine the row and column placement of a child control: `Grid.Row` and `Grid.Column`. If you omit these properties from the control, the default values are 0. So, the control is placed in row `0` and column `0` of the grid. Try changing the placement of the `<Label>` control by setting the `Grid.Column` attribute to `1`:

```
<Label Grid.Column="1">Names</Label>
```

Notice that the label moved to the second column. You can use the `Grid.Row` and `Grid.Column` attached properties to place the next controls you'll create. For now though, restore the label to column 0.

Now that the grid is correctly sized and the label created, add a list box control on the row below the label.

1.   Declare the `<ListBox />` control under the `<Label>` control.

2.   Set the `Grid.Row` property to `1`.

3.   Set the `x:Name` property to `lstNames`.

Once a control is named, you can reference it in the code-behind. Assign the name to the control by using the `x:Name` attribute.

Here's what the XAML should look like:

```
<Grid Margin="10">

    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />
        <RowDefinition Height="*" />
    </Grid.RowDefinitions>

    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="*" />
        <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>

    <Label>Names</Label>
    <ListBox Grid.Row="1" x:Name="lstNames" />

</Grid>
```

Add a text box and a button. The user uses these controls to enter a name to add to the list box. Instead of creating more rows and columns in the grid to arrange these controls, put these controls into the `<StackPanel>` layout control.

The stack panel differs from the grid in how it places controls. While you use the `Grid.Row` and `Grid.Column` attached properties to tell the grid where you want the controls, the stack panel works automatically. It lays out each of its child controls sequentially. It "stacks" each control after the other.

1.   Declare the `<StackPanel>` control under the `<ListBox>` control.

2.   Set the `Grid.Row` property to `1`.

3.   Set the `Grid.Column` property to `1`.

4.   Set the `Margin` to `5,0,0,0`.

```
<Grid.RowDefinitions>
    <RowDefinition Height="Auto" />
    <RowDefinition Height="*" />
</Grid.RowDefinitions>

<Grid.ColumnDefinitions>
    <ColumnDefinition Width="*" />
    <ColumnDefinition Width="*" />
</Grid.ColumnDefinitions>

<Label>Names</Label>
<ListBox Grid.Row="1" x:Name="lstNames" />

<StackPanel Grid.Row="1" Grid.Column="1" Margin="5,0,0,0">
    
</StackPanel>
```

You previously used the `Margin` attribute on the grid, but you only put in a single value, `10`. This margin has a value of `5,0,0,0`, which is very different from `10`. The margin property is a `Thickness` type and can interpret both values. A thickness defines the space around each side of a rectangular frame, **left**, **top**, **right**, **bottom**, respectively. If the value for the margin is a single value, it uses that value for all four sides.

5.   Inside of the `<StackPanel>` control, create a `<TextBox />` control.

    1.   Set the `x:Name` property to `txtName`.

6.   Lastly, after the `<TextBox>`, still inside of the `<StackPanel>`, create a `<Button>` control.

    1.   Set the `x:Name` property to `btnAdd`.
    2.   Set the `Margin` to `0,5,0,0`.
    3.   Set the content to `Add Name`.

Here's what the XAML should look like:

```
<StackPanel Grid.Row="1" Grid.Column="1" Margin="5,0,0,0">
    <TextBox x:Name="txtName" />
    <Button x:Name="btnAdd" Margin="0,5,0,0">Add Name</Button>
</StackPanel>
```

The layout for the window is complete. However, the app doesn't have any logic to actually be functional. Next, you need to hook up the control events to code and get the app to actually do something.

The `<Button>` you created has a `Click` event that the app raises when the user presses the button. Subscribe to this event and add code to add a name to the list box. Use XAML attributes to subscribe to events, just like you use them to set properties.

1.   Locate the `<Button>` control.

2.   Set the `Click` attribute to `ButtonAddName_Click`.

```
<StackPanel Grid.Row="1" Grid.Column="1" Margin="5,0,0,0">
    <TextBox x:Name="txtName" />
    <Button x:Name="btnAdd" Margin="0,5,0,0" Click="ButtonAddName_Click">Add Name</Button>
</StackPanel>
```
3.   Generate the event handler code. Right-click on `ButtonAddName_Click` and select **Go To Definition**.

This action generates a method in the code-behind that matches the handler name you provided.

```
private void ButtonAddName_Click(object sender, RoutedEventArgs e)
{

}
```
4.   Next, add the following code to do these three steps:

    1.   Make sure that the text box contains a name.
    2.   Validate that the name entered in the text box doesn't already exist.
    3.   Add the name to the list box.

```
private void ButtonAddName_Click(object sender, RoutedEventArgs e)
{
    if (!string.IsNullOrWhiteSpace(txtName.Text) && !lstNames.Items.Contains(txtName.Text))
    {
        lstNames.Items.Add(txtName.Text);
        txtName.Clear();
    }
}
```

After handling the event, run the app. The window appears, and you can enter a name in the textbox. Add the name by selecting the button.

![Image 10: Running a WPF for .NET app in Visual Studio 2026.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/media/create-app-visual-studio/app-finished.png)

*   [Learn more about Windows Presentation Foundation](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/)
*   [XAML overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/xaml/)
