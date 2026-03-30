# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-create-apply-template

Title: How to create a template - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-create-apply-template

Markdown Content:
With Windows Presentation Foundation (WPF), you can customize an existing control's visual structure and behavior with your own reusable template. Templates can be applied globally to your application, windows and pages, or directly to controls. Most scenarios that require you to create a new control can be covered by instead creating a new template for an existing control.

In this article, you'll explore creating a new [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) for the [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button) control.

Controls have many properties, such as [Background](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.border.background), [Foreground](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.foreground), and [FontFamily](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.fontfamily). These properties control different aspects of the control's appearance, but the changes that you can make by setting these properties are limited. For example, you can set the [Foreground](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.foreground) property to blue and [FontStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.fontstyle) to italic on a [CheckBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.checkbox). When you want to customize the control's appearance beyond what setting the other properties on the control can do, you create a [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate).

In most user interfaces, a button has the same general appearance: a rectangle with some text. If you wanted to create a rounded button, you could create a new control that inherits from the button or recreates the functionality of the button. In addition, the new user control would provide the circular visual.

You can avoid creating new controls by customizing the visual layout of an existing control. With a rounded button, you create a [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) with the desired visual layout.

On the other hand, if you need a control with new functionality, different properties, and new settings, you would create a new [UserControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.usercontrol).

Create a new WPF application and in _MainWindow.xaml_ (or another window of your choice) set the following properties on the **<Window>** element:

| Property | Value |
| --- | --- |
| **Title** | `Template Intro Sample` |
| **SizeToContent** | `WidthAndHeight` |
| **MinWidth** | `250` |

Set the content of the **<Window>** element to the following XAML:

```
<StackPanel Margin="10">
    <Label>Unstyled Button</Label>
    <Button>Button 1</Button>
    <Label>Rounded Button</Label>
    <Button>Button 2</Button>
</StackPanel>
```

In the end, the _MainWindow.xaml_ file should look similar to the following:

```
<Window x:Class="IntroToStylingAndTemplating.Window1"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:IntroToStylingAndTemplating"
        mc:Ignorable="d"
        Title="Template Intro Sample" SizeToContent="WidthAndHeight" MinWidth="250">
    <StackPanel Margin="10">
        <Label>Unstyled Button</Label>
        <Button>Button 1</Button>
        <Label>Rounded Button</Label>
        <Button>Button 2</Button>
    </StackPanel>
</Window>
```

If you run the application, it looks like the following:

![Image 1: WPF window with two unstyled buttons](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-template/unstyled-button.png)

The most common way to declare a [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) is as a resource in the `Resources` section in a XAML file. Because templates are resources, they obey the same scoping rules that apply to all resources. Put simply, where you declare a template affects where the template can be applied. For example, if you declare the template in the root element of your application definition XAML file, the template can be used anywhere in your application. If you define the template in a window, only the controls in that window can use the template.

To start with, add a `Window.Resources` element to your _MainWindow.xaml_ file:

```
<Window x:Class="IntroToStylingAndTemplating.Window2"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:IntroToStylingAndTemplating"
        mc:Ignorable="d"
        Title="Template Intro Sample" SizeToContent="WidthAndHeight" MinWidth="250">
    <Window.Resources>
        
    </Window.Resources>
    <StackPanel Margin="10">
        <Label>Unstyled Button</Label>
        <Button>Button 1</Button>
        <Label>Rounded Button</Label>
        <Button>Button 2</Button>
    </StackPanel>
</Window>
```

Create a new **<ControlTemplate>** with the following properties set:

| Property | Value |
| --- | --- |
| **x:Key** | `roundbutton` |
| **TargetType** | `Button` |

This control template will be simple:

*   a root element for the control, a [Grid](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.grid)
*   an [Ellipse](https://learn.microsoft.com/en-us/dotnet/api/system.windows.shapes.ellipse) to draw the rounded appearance of the button
*   a [ContentPresenter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentpresenter) to display the user-specified button content

```
<ControlTemplate x:Key="roundbutton" TargetType="Button">
    <Grid>
        <Ellipse Fill="{TemplateBinding Background}" Stroke="{TemplateBinding Foreground}" />
        <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center" />
    </Grid>
</ControlTemplate>
```

When you create a new [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate), you still might want to use the public properties to change the control's appearance. The [TemplateBinding](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/templatebinding-markup-extension) markup extension binds a property of an element that is in the [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) to a public property that is defined by the control. When you use a [TemplateBinding](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/templatebinding-markup-extension), you enable properties on the control to act as parameters to the template. That is, when a property on a control is set, that value is passed on to the element that has the [TemplateBinding](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/templatebinding-markup-extension) on it.

Notice that the **Fill** and **Stroke** properties of the **<Ellipse>** element are bound to the control's [Foreground](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.foreground#system-windows-controls-control-foreground) and [Background](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.background#system-windows-controls-control-background) properties.

A [<ContentPresenter>](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentpresenter) element is also added to the template. Because this template is designed for a button, take into consideration that the button inherits from [ContentControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol). The button presents the content of the element. You can set anything inside of the button, such as plain text or even another control. Both of the following are valid buttons:

```
<Button>My Text</Button>

<!-- and -->

<Button>
    <CheckBox>Checkbox in a button</CheckBox>
</Button>
```

In both of the previous examples, the text and the checkbox are set as the [Button.Content](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol.content#system-windows-controls-contentcontrol-content) property. Whatever is set as the content can be presented through a **<ContentPresenter>**, which is what the template does.

If the [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) is applied to a [ContentControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol) type, such as a `Button`, a [ContentPresenter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentpresenter) is searched for in the element tree. If the `ContentPresenter` is found, the template automatically binds the control's [Content](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol.content#system-windows-controls-contentcontrol-content) property to the `ContentPresenter`.

Find the buttons that were declared at the start of this article.

```
<StackPanel Margin="10">
    <Label>Unstyled Button</Label>
    <Button>Button 1</Button>
    <Label>Rounded Button</Label>
    <Button>Button 2</Button>
</StackPanel>
```

Set the second button's [Template](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.template#system-windows-controls-control-template) property to the `roundbutton` resource:

```
<StackPanel Margin="10">
    <Label>Unstyled Button</Label>
    <Button>Button 1</Button>
    <Label>Rounded Button</Label>
    <Button Template="{StaticResource roundbutton}">Button 2</Button>
</StackPanel>
```

If you run the project and look at the result, you'll see that the button has a rounded background.

![Image 2: WPF window with one template oval button](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-template/styled-button.png)

You may have noticed that the button isn't a circle but is skewed. Because of the way the **<Ellipse>** element works, it always expands to fill the available space. Make the circle uniform by changing the button's **width** and **height** properties to the same value:

```
<StackPanel Margin="10">
    <Label>Unstyled Button</Label>
    <Button>Button 1</Button>
    <Label>Rounded Button</Label>
    <Button Template="{StaticResource roundbutton}" Width="65" Height="65">Button 2</Button>
</StackPanel>
```

![Image 3: WPF window with one template circular button](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-template/styled-uniform-button.png)

Even though a button with a template applied looks different, it behaves the same as any other button. If you press the button, the [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.buttonbase.click#system-windows-controls-primitives-buttonbase-click) event fires. However, you may have noticed that when you move your mouse over the button, the button's visuals don't change. These visual interactions are all defined by the template.

With the dynamic event and property systems that WPF provides, you can watch a specific property for a value and then restyle the template when appropriate. In this example, you'll watch the button's [IsMouseOver](https://learn.microsoft.com/en-us/dotnet/api/system.windows.uielement.ismouseover#system-windows-uielement-ismouseover) property. When the mouse is over the control, style the **<Ellipse>** with a new color. This type of trigger is known as a _PropertyTrigger_.

For this to work, you'll need to add a name to the **<Ellipse>** that you can reference. Give it the name of **backgroundElement**.

```
<Ellipse x:Name="backgroundElement" Fill="{TemplateBinding Background}" Stroke="{TemplateBinding Foreground}" />
```

Next, add a new [Trigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.trigger) to the [ControlTemplate.Triggers](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate.triggers#system-windows-controls-controltemplate-triggers) collection. The trigger will watch the `IsMouseOver` event for the value `true`.

```
<ControlTemplate x:Key="roundbutton" TargetType="Button">
    <Grid>
        <Ellipse x:Name="backgroundElement" Fill="{TemplateBinding Background}" Stroke="{TemplateBinding Foreground}" />
        <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center" />
    </Grid>
    <ControlTemplate.Triggers>
        <Trigger Property="IsMouseOver" Value="true">

        </Trigger>
    </ControlTemplate.Triggers>
</ControlTemplate>
```

Next, add a **<Setter>** to the **<Trigger>** that changes the **Fill** property of the **<Ellipse>** to a new color.

```
<Trigger Property="IsMouseOver" Value="true">
    <Setter Property="Fill" TargetName="backgroundElement" Value="AliceBlue"/>
</Trigger>
```

Run the project. Notice that when you move the mouse over the button, the color of the **<Ellipse>** changes.

![Image 4: mouse moves over WPF button to change the fill color](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-template/mouse-move-over-button.gif)

Visual states are defined and triggered by a control. For example, when the mouse is moved on top of the control, the `CommonStates.MouseOver` state is triggered. You can animate property changes based on the current state of the control. In the previous section, a **<PropertyTrigger>** was used to change the background of the button to `AliceBlue` when the `IsMouseOver` property was `true`. Instead, create a visual state that animates the change of this color, providing a smooth transition. For more information about _VisualStates_, see [Styles and templates in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/styles-templates-overview#visual-states).

To convert the **<PropertyTrigger>** to an animated visual state, First, remove the **<ControlTemplate.Triggers>** element from your template.

```
<ControlTemplate x:Key="roundbutton" TargetType="Button">
    <Grid>
        <Ellipse x:Name="backgroundElement" Fill="{TemplateBinding Background}" Stroke="{TemplateBinding Foreground}" />
        <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center" />
    </Grid>
</ControlTemplate>
```

Next, in the **<Grid>** root of the control template, add the **<VisualStateManager.VisualStateGroups>** element with a **<VisualStateGroup>** for `CommonStates`. Define two states, `Normal` and `MouseOver`.

```
<ControlTemplate x:Key="roundbutton" TargetType="Button">
    <Grid>
        <VisualStateManager.VisualStateGroups>
            <VisualStateGroup Name="CommonStates">
                <VisualState Name="Normal">
                </VisualState>
                <VisualState Name="MouseOver">
                </VisualState>
            </VisualStateGroup>
        </VisualStateManager.VisualStateGroups>
        <Ellipse x:Name="backgroundElement" Fill="{TemplateBinding Background}" Stroke="{TemplateBinding Foreground}" />
        <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center" />
    </Grid>
</ControlTemplate>
```

Any animations defined in a **<VisualState>** are applied when that state is triggered. Create animations for each state. Animations are put inside of a **<Storyboard>** element. For more information about storyboards, see [Storyboards Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/storyboards-overview).

*   Normal

This state animates the ellipse fill, restoring it to the control's `Background` color.

```
<Storyboard>
    <ColorAnimation Storyboard.TargetName="backgroundElement" 
        Storyboard.TargetProperty="(Shape.Fill).(SolidColorBrush.Color)"
        To="{TemplateBinding Background}"
        Duration="0:0:0.3"/>
</Storyboard>
```
*   MouseOver

This state animates the ellipse `Background` color to a new color: `Yellow`.

```
<Storyboard>
    <ColorAnimation Storyboard.TargetName="backgroundElement" 
        Storyboard.TargetProperty="(Shape.Fill).(SolidColorBrush.Color)" 
        To="Yellow" 
        Duration="0:0:0.3"/>
</Storyboard>
```

The **<ControlTemplate>** should now look like the following.

```
<ControlTemplate x:Key="roundbutton" TargetType="Button">
    <Grid>
        <VisualStateManager.VisualStateGroups>
            <VisualStateGroup Name="CommonStates">
                <VisualState Name="Normal">
                    <Storyboard>
                        <ColorAnimation Storyboard.TargetName="backgroundElement" 
                            Storyboard.TargetProperty="(Shape.Fill).(SolidColorBrush.Color)"
                            To="{TemplateBinding Background}"
                            Duration="0:0:0.3"/>
                    </Storyboard>
                </VisualState>
                <VisualState Name="MouseOver">
                    <Storyboard>
                        <ColorAnimation Storyboard.TargetName="backgroundElement" 
                            Storyboard.TargetProperty="(Shape.Fill).(SolidColorBrush.Color)" 
                            To="Yellow" 
                            Duration="0:0:0.3"/>
                    </Storyboard>
                </VisualState>
            </VisualStateGroup>
        </VisualStateManager.VisualStateGroups>
        <Ellipse Name="backgroundElement" Fill="{TemplateBinding Background}" Stroke="{TemplateBinding Foreground}" />
        <ContentPresenter x:Name="contentPresenter" HorizontalAlignment="Center" VerticalAlignment="Center" />
    </Grid>
</ControlTemplate>
```

Run the project. Notice that when you move the mouse over the button, the color of the **<Ellipse>** animates.

![Image 5: mouse moves over WPF button to change the fill color with a visual state](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-template/mouse-move-over-button-visualstate.gif)

*   [Create a style for a control](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-create-apply-style)
*   [Styles and templates](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/styles-templates-overview)
*   [Overview of XAML resources](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/systems/xaml-resources-overview)
