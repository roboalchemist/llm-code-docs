# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/styles-templates-overview

Title: Styles and templates - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/styles-templates-overview

Markdown Content:
Windows Presentation Foundation (WPF) styling and templating refer to a suite of features that let developers and designers create visually compelling effects and a consistent appearance for their product. When customizing the appearance of an app, you want a strong styling and templating model that enables maintenance and sharing of appearance within and among apps. WPF provides that model.

Another feature of the WPF styling model is the separation of presentation and logic. Designers can work on the appearance of an app by using only XAML at the same time that developers work on the programming logic by using C# or Visual Basic.

This overview focuses on the styling and templating aspects of the app and doesn't discuss any data-binding concepts. For information about data binding, see [Data Binding Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/).

It's important to understand resources, which are what enable styles and templates to be reused. For more information about resources, see [Overview of XAML resources](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/systems/xaml-resources-overview).

The sample code provided in this overview is based on a [simple photo browsing application](https://github.com/Microsoft/WPF-Samples/tree/master/Styles%20&%20Templates/IntroToStylingAndTemplating) shown in the following illustration.

![Image 1: Styled ListView](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/styles-and-templates-overview/stylingintro-triggers.png)

This simple photo sample uses styling and templating to create a visually compelling user experience. The sample has two [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) elements and a [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listbox) control that is bound to a list of images.

For the complete sample, see [Introduction to Styling and Templating Sample](https://github.com/Microsoft/WPF-Samples/tree/master/Styles%20&%20Templates/IntroToStylingAndTemplating).

You can think of a [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style) as a convenient way to apply a set of property values to multiple elements. You can use a style on any element that derives from [FrameworkElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement) or [FrameworkContentElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkcontentelement) such as a [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) or a [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button).

The most common way to declare a style is as a resource in the `Resources` section in a XAML file. Because styles are resources, they obey the same scoping rules that apply to all resources. Put simply, where you declare a style affects where the style can be applied. For example, if you declare the style in the root element of your app definition XAML file, the style can be used anywhere in your app.

For example, the following XAML code declares two styles for a `TextBlock`, one automatically applied to all `TextBlock` elements, and another that must be explicitly referenced.

```
<Window.Resources>
    <!-- .... other resources .... -->

    <!--A Style that affects all TextBlocks-->
    <Style TargetType="TextBlock">
        <Setter Property="HorizontalAlignment" Value="Center" />
        <Setter Property="FontFamily" Value="Comic Sans MS"/>
        <Setter Property="FontSize" Value="14"/>
    </Style>
    
    <!--A Style that extends the previous TextBlock Style with an x:Key of TitleText-->
    <Style BasedOn="{StaticResource {x:Type TextBlock}}"
           TargetType="TextBlock"
           x:Key="TitleText">
        <Setter Property="FontSize" Value="26"/>
        <Setter Property="Foreground">
            <Setter.Value>
                <LinearGradientBrush StartPoint="0.5,0" EndPoint="0.5,1">
                    <LinearGradientBrush.GradientStops>
                        <GradientStop Offset="0.0" Color="#90DDDD" />
                        <GradientStop Offset="1.0" Color="#5BFFFF" />
                    </LinearGradientBrush.GradientStops>
                </LinearGradientBrush>
            </Setter.Value>
        </Setter>
    </Style>
</Window.Resources>
```

Here is an example of the styles declared above being used.

```
<StackPanel>
    <TextBlock Style="{StaticResource TitleText}" Name="textblock1">My Pictures</TextBlock>
    <TextBlock>Check out my new pictures!</TextBlock>
</StackPanel>
```

![Image 2: Styled textblocks](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/styles-and-templates-overview/stylingintro-textblocks.png)

For more information, see [Create a style for a control](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-create-apply-style).

In WPF, the [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) of a control defines the appearance of the control. You can change the structure and appearance of a control by defining a new [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) and assigning it to a control. In many cases, templates give you enough flexibility so that you do not have to write your own custom controls.

Each control has a default template assigned to the [Control.Template](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.template#system-windows-controls-control-template) property. The template connects the visual presentation of the control with the control's capabilities. Because you define a template in XAML, you can change the control's appearance without writing any code. Each template is designed for a specific control, such as a [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button).

Important

When you change the visual tree of a control, you must replace the entire [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate). There is no way to replace only part of the visual tree of a control. To change the visual tree of a control, you must set the [Template](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.template) property of the control to its new and complete [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate).

Commonly you declare a template as a resource on the `Resources` section of a XAML file. As with all resources, scoping rules apply.

Control templates are a lot more involved than a style. This is because the control template rewrites the visual appearance of the entire control, while a style simply applies property changes to the existing control. However, since the template of a control is applied by setting the [Control.Template](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.template#system-windows-controls-control-template) property, you can use a style to define or set a template.

Designers generally allow you to create a copy of an existing template and modify it. For example, in the Visual Studio WPF designer, select a `CheckBox` control, and then right-click and select **Edit template**>**Create a copy**. This command generates a _style that defines a template_.

```
<Style x:Key="CheckBoxStyle1" TargetType="{x:Type CheckBox}">
    <Setter Property="FocusVisualStyle" Value="{StaticResource FocusVisual1}"/>
    <Setter Property="Background" Value="{StaticResource OptionMark.Static.Background1}"/>
    <Setter Property="BorderBrush" Value="{StaticResource OptionMark.Static.Border1}"/>
    <Setter Property="Foreground" Value="{DynamicResource {x:Static SystemColors.ControlTextBrushKey}}"/>
    <Setter Property="BorderThickness" Value="1"/>
    <Setter Property="Template">
        <Setter.Value>
            <ControlTemplate TargetType="{x:Type CheckBox}">
                <Grid x:Name="templateRoot" Background="Transparent" SnapsToDevicePixels="True">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="Auto"/>
                        <ColumnDefinition Width="*"/>
                    </Grid.ColumnDefinitions>
                    <Border x:Name="checkBoxBorder" Background="{TemplateBinding Background}" BorderThickness="{TemplateBinding BorderThickness}" BorderBrush="{TemplateBinding BorderBrush}" HorizontalAlignment="{TemplateBinding HorizontalContentAlignment}" Margin="1" VerticalAlignment="{TemplateBinding VerticalContentAlignment}">
                        <Grid x:Name="markGrid">
                            <Path x:Name="optionMark" Data="F1 M 9.97498,1.22334L 4.6983,9.09834L 4.52164,9.09834L 0,5.19331L 1.27664,3.52165L 4.255,6.08833L 8.33331,1.52588e-005L 9.97498,1.22334 Z " Fill="{StaticResource OptionMark.Static.Glyph1}" Margin="1" Opacity="0" Stretch="None"/>
                            <Rectangle x:Name="indeterminateMark" Fill="{StaticResource OptionMark.Static.Glyph1}" Margin="2" Opacity="0"/>
                        </Grid>
                    </Border>
                    <ContentPresenter x:Name="contentPresenter" Grid.Column="1" Focusable="False" HorizontalAlignment="{TemplateBinding HorizontalContentAlignment}" Margin="{TemplateBinding Padding}" RecognizesAccessKey="True" SnapsToDevicePixels="{TemplateBinding SnapsToDevicePixels}" VerticalAlignment="{TemplateBinding VerticalContentAlignment}"/>
                </Grid>
                <ControlTemplate.Triggers>
                    <Trigger Property="HasContent" Value="true">
                        <Setter Property="FocusVisualStyle" Value="{StaticResource OptionMarkFocusVisual1}"/>
                        <Setter Property="Padding" Value="4,-1,0,0"/>

... content removed to save space ...
```

Editing a copy of a template is a great way to learn how templates work. Instead of creating a new blank template, it's easier to edit a copy and change a few aspects of the visual presentation.

For an example, see [Create a template for a control](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-create-apply-template).

You may have noticed that the template resource defined in the previous section uses the [TemplateBinding Markup Extension](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/templatebinding-markup-extension). A `TemplateBinding` is an optimized form of a binding for template scenarios, analogous to a binding constructed with `{Binding RelativeSource={RelativeSource TemplatedParent}}`. `TemplateBinding` is useful for binding parts of the template to properties of the control. For example, each control has a [BorderThickness](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.borderthickness#system-windows-controls-control-borderthickness) property. Use a `TemplateBinding` to manage which element in the template is affected by this control setting.

If a [ContentPresenter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentpresenter) is declared in the [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) of a [ContentControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol), the [ContentPresenter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentpresenter) will automatically bind to the [ContentTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol.contenttemplate) and [Content](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol.content) properties. Likewise, an [ItemsPresenter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.itemspresenter) that is in the [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate) of an [ItemsControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.itemscontrol) will automatically bind to the [ItemTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.itemscontrol.itemtemplate) and [Items](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.itemscontrol.items) properties.

In this sample app, there is a [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listbox) control that is bound to a list of photos.

```
<ListBox ItemsSource="{Binding Source={StaticResource MyPhotos}}"
         Background="Silver" Width="600" Margin="10" SelectedIndex="0"/>
```

This [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listbox) currently looks like the following.

![Image 3: ListBox before applying template](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/styles-and-templates-overview/stylingintro-listboxbefore.png)

Most controls have some type of content, and that content often comes from data that you are binding to. In this sample, the data is the list of photos. In WPF, you use a [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) to define the visual representation of data. Basically, what you put into a [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) determines what the data looks like in the rendered app.

In our sample app, each custom `Photo` object has a `Source` property of type string that specifies the file path of the image. Currently, the photo objects appear as file paths.

```
public class Photo
{
    public Photo(string path)
    {
        Source = path;
    }

    public string Source { get; }

    public override string ToString() => Source;
}
```

For the photos to appear as images, you create a [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) as a resource.

```
<Window.Resources>
    <!-- .... other resources .... -->

    <!--DataTemplate to display Photos as images
    instead of text strings of Paths-->
    <DataTemplate DataType="{x:Type local:Photo}">
        <Border Margin="3">
            <Image Source="{Binding Source}"/>
        </Border>
    </DataTemplate>
</Window.Resources>
```

Notice that the [DataType](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate.datatype) property is similar to the [TargetType](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style.targettype) property of the [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style). If your [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) is in the resources section, when you specify the [DataType](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate.datatype) property to a type and omit an `x:Key`, the [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) is applied whenever that type appears. You always have the option to assign the [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) with an `x:Key` and then set it as a `StaticResource` for properties that take [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) types, such as the [ItemTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.itemscontrol.itemtemplate) property or the [ContentTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol.contenttemplate) property.

Essentially, the [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) in the above example defines that whenever there is a `Photo` object, it should appear as an [Image](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.image) within a [Border](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.border). With this [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate), our app now looks like this.

![Image 4: Photo image](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/styles-and-templates-overview/stylingintro-photosasimages.png)

The data templating model provides other features. For example, if you are displaying collection data that contains other collections using a [HeaderedItemsControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.headereditemscontrol) type such as a [Menu](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.menu) or a [TreeView](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.treeview), there is the [HierarchicalDataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.hierarchicaldatatemplate). Another data templating feature is the [DataTemplateSelector](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.datatemplateselector), which allows you to choose a [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) to use based on custom logic. For more information, see [Data Templating Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/data-templating-overview), which provides a more in-depth discussion of the different data templating features.

A trigger sets properties or starts actions, such as an animation, when a property value changes or when an event is raised. [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style), [ControlTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.controltemplate), and [DataTemplate](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatemplate) all have a `Triggers` property that can contain a set of triggers. There are several types of triggers.

A [Trigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.trigger) that sets property values or starts actions based on the value of a property is called a property trigger.

To demonstrate how to use property triggers, you can make each [ListBoxItem](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listboxitem) partially transparent unless it is selected. The following style sets the [Opacity](https://learn.microsoft.com/en-us/dotnet/api/system.windows.uielement.opacity) value of a [ListBoxItem](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listboxitem) to `0.5`. When the [IsSelected](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listboxitem.isselected) property is `true`, however, the [Opacity](https://learn.microsoft.com/en-us/dotnet/api/system.windows.uielement.opacity) is set to `1.0`.

```
<Window.Resources>
    <!-- .... other resources .... -->

    <Style TargetType="ListBoxItem">
        <Setter Property="Opacity" Value="0.5" />
        <Setter Property="MaxHeight" Value="75" />
        <Style.Triggers>
            <Trigger Property="IsSelected" Value="True">
                <Trigger.Setters>
                    <Setter Property="Opacity" Value="1.0" />
                </Trigger.Setters>
            </Trigger>
        </Style.Triggers>
    </Style>
</Window.Resources>
```

This example uses a [Trigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.trigger) to set a property value, but note that the [Trigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.trigger) class also has the [EnterActions](https://learn.microsoft.com/en-us/dotnet/api/system.windows.triggerbase.enteractions) and [ExitActions](https://learn.microsoft.com/en-us/dotnet/api/system.windows.triggerbase.exitactions) properties that enable a trigger to perform actions.

Notice that the [MaxHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxheight) property of the [ListBoxItem](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listboxitem) is set to `75`. In the following illustration, the third item is the selected item.

![Image 5: Styled ListView](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/styles-and-templates-overview/stylingintro-triggers.png)

Another type of trigger is the [EventTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.eventtrigger), which starts a set of actions based on the occurrence of an event. For example, the following [EventTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.eventtrigger) objects specify that when the mouse pointer enters the [ListBoxItem](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listboxitem), the [MaxHeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.maxheight) property animates to a value of `90` over a `0.2` second period. When the mouse moves away from the item, the property returns to the original value over a period of `1` second. Note how it is not necessary to specify a [To](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.animation.doubleanimation.to) value for the [MouseLeave](https://learn.microsoft.com/en-us/dotnet/api/system.windows.contentelement.mouseleave#system-windows-contentelement-mouseleave) animation. This is because the animation is able to keep track of the original value.

```
<Style.Triggers>
    <Trigger Property="IsSelected" Value="True">
        <Trigger.Setters>
            <Setter Property="Opacity" Value="1.0" />
        </Trigger.Setters>
    </Trigger>
    <EventTrigger RoutedEvent="Mouse.MouseEnter">
        <EventTrigger.Actions>
            <BeginStoryboard>
                <Storyboard>
                    <DoubleAnimation
                        Duration="0:0:0.2"
                        Storyboard.TargetProperty="MaxHeight"
                        To="90"  />
                </Storyboard>
            </BeginStoryboard>
        </EventTrigger.Actions>
    </EventTrigger>
    <EventTrigger RoutedEvent="Mouse.MouseLeave">
        <EventTrigger.Actions>
            <BeginStoryboard>
                <Storyboard>
                    <DoubleAnimation
                        Duration="0:0:1"
                        Storyboard.TargetProperty="MaxHeight"  />
                </Storyboard>
            </BeginStoryboard>
        </EventTrigger.Actions>
    </EventTrigger>
</Style.Triggers>
```

For more information, see the [Storyboards overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/storyboards-overview).

In the following illustration, the mouse is pointing to the third item.

![Image 6: Styling sample screenshot](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/styles-and-templates-overview/stylingintro-eventtriggers.png)

In addition to [Trigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.trigger) and [EventTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.eventtrigger), there are other types of triggers. [MultiTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.multitrigger) allows you to set property values based on multiple conditions. You use [DataTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.datatrigger) and [MultiDataTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.multidatatrigger) when the property of your condition is data-bound.

Controls are always in a specific **state**. For example, when the mouse moves over the surface of a control, the control is considered to be in a common state of `MouseOver`. A control without a specific state is considered to be in the common `Normal` state. States are broken into groups, and the previously mentioned states are part of the state group `CommonStates`. Most controls have two state groups: `CommonStates` and `FocusStates`. Of each state group applied to a control, a control is always in one state of each group, such as `CommonStates.MouseOver` and `FocusStates.Unfocused`. However, a control can't be in two different states within the same group, such as `CommonStates.Normal` and `CommonStates.Disabled`. Here is a table of states most controls recognize and use.

| VisualState Name | VisualStateGroup Name | Description |
| --- | --- | --- |
| `Normal` | `CommonStates` | The default state. |
| `MouseOver` | `CommonStates` | The mouse pointer is positioned over the control. |
| `Pressed` | `CommonStates` | The control is pressed. |
| `Disabled` | `CommonStates` | The control is disabled. |
| `Focused` | `FocusStates` | The control has focus. |
| `Unfocused` | `FocusStates` | The control does not have focus. |

By defining a [System.Windows.VisualStateManager](https://learn.microsoft.com/en-us/dotnet/api/system.windows.visualstatemanager) on the root element of a control template, you can trigger animations when a control enters a specific state. The `VisualStateManager` declares which combinations of [VisualStateGroup](https://learn.microsoft.com/en-us/dotnet/api/system.windows.visualstategroup) and [VisualState](https://learn.microsoft.com/en-us/dotnet/api/system.windows.visualstate) to watch. When the control enters a watched state, the animation defined by the `VisualStateManager` is started.

For example, the following XAML code watches the `CommonStates.MouseOver` state to animate the fill color of the element named `backgroundElement`. When the control returns to the `CommonStates.Normal` state, the fill color of the element named `backgroundElement` is restored.

```
<ControlTemplate x:Key="roundbutton" TargetType="Button">
    <Grid>
        <VisualStateManager.VisualStateGroups>
            <VisualStateGroup Name="CommonStates">
                <VisualState Name="Normal">
                    <ColorAnimation Storyboard.TargetName="backgroundElement"
                                    Storyboard.TargetProperty="(Shape.Fill).(SolidColorBrush.Color)"
                                    To="{TemplateBinding Background}"
                                    Duration="0:0:0.3"/>
                </VisualState>
                <VisualState Name="MouseOver">
                    <ColorAnimation Storyboard.TargetName="backgroundElement"
                                    Storyboard.TargetProperty="(Shape.Fill).(SolidColorBrush.Color)"
                                    To="Yellow"
                                    Duration="0:0:0.3"/>
                </VisualState>
            </VisualStateGroup>
        </VisualStateManager.VisualStateGroups>

        ...
```

For more information about storyboards, see [Storyboards Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/storyboards-overview).

A typical WPF app might have multiple UI resources that are applied throughout the app. Collectively, this set of resources can be considered the theme for the app. WPF provides support for packaging UI resources as a theme by using a resource dictionary that is encapsulated as the [ResourceDictionary](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resourcedictionary) class.

WPF themes are defined by using the styling and templating mechanism that WPF exposes for customizing the visuals of any element.

WPF theme resources are stored in embedded resource dictionaries. These resource dictionaries must be embedded within a signed assembly, and can either be embedded in the same assembly as the code itself or in a side-by-side assembly. For PresentationFramework.dll, the assembly that contains WPF controls, theme resources are embedded in a series of side-by-side assemblies. The operating system determines which theme resource dictionary is used at runtime.

The theme becomes the last place to look when searching for the style of an element. Typically, the search will begin by walking up the element tree searching for an appropriate resource, then look in the app resource collection and finally query the system. This gives app developers a chance to redefine the style for any object at the tree or app level before reaching the theme.

You can define resource dictionaries as individual files that enable you to reuse a theme across multiple apps. You can also create swappable themes by defining multiple resource dictionaries that provide the same types of resources but with different values. Redefining these styles or other resources at the app level is the recommended approach for skinning an app.

To share a set of resources, including styles and templates, across apps, you can create a XAML file and define a [ResourceDictionary](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resourcedictionary) that includes reference to a `shared.xaml` file.

```
<ResourceDictionary.MergedDictionaries>
  <ResourceDictionary Source="Shared.xaml" />
</ResourceDictionary.MergedDictionaries>
```

It is the sharing of `shared.xaml`, which itself defines a [ResourceDictionary](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resourcedictionary) that contains a set of style and brush resources, that enables the controls in an app to have a consistent look.

For more information, see [Merged resource dictionaries](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/systems/xaml-resources-merged-dictionaries).

If you are creating a theme for your custom control, see the **Defining resources at the theme level** section of the [Control authoring overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/control-authoring-overview#defining-resources-at-the-theme-level).

WPF includes several built-in themes that you can explicitly apply to your application. These themes are embedded within PresentationFramework assemblies and can be referenced using pack URIs in your application's resource dictionaries.

To apply a built-in theme, merge the theme's resource dictionary into your application resources in `App.xaml`:

```
<Application x:Class="MyApp.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             StartupUri="MainWindow.xaml">
    <Application.Resources>
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ResourceDictionary Source="/PresentationFramework.Aero2;component/themes/Aero2.NormalColor.xaml"/>
            </ResourceDictionary.MergedDictionaries>
        </ResourceDictionary>
    </Application.Resources>
</Application>
```

The following table lists the built-in themes available through pack URIs:

| Theme | Pack URI | Description |
| --- | --- | --- |
| **Aero2** | `/PresentationFramework.Aero2;component/themes/Aero2.NormalColor.xaml` | Default theme for Windows 8 and later applications. |
| **AeroLite** | `/PresentationFramework.AeroLite;component/themes/AeroLite.NormalColor.xaml` | Simplified version of Aero2 with reduced visual effects. |
| **Aero** | `/PresentationFramework.Aero;component/themes/Aero.NormalColor.xaml` | Windows 7-era theme with glass effects and gradients. |
| **Fluent** | `/PresentationFramework.Fluent;component/Themes/Fluent.xaml` | Windows 11-style theme with light/dark mode support (.NET 9+). |
| **Luna (Blue)** | `/PresentationFramework.Luna;component/themes/Luna.NormalColor.xaml` | Windows XP default blue color scheme. |
| **Luna (Silver)** | `/PresentationFramework.Luna;component/themes/Luna.Metallic.xaml` | Windows XP metallic silver color scheme. |
| **Luna (Olive)** | `/PresentationFramework.Luna;component/themes/Luna.Homestead.xaml` | Windows XP olive green color scheme. |
| **Royale** | `/PresentationFramework.Royale;component/themes/Royale.NormalColor.xaml` | Windows XP Media Center Edition theme. |
| **Classic** | `/PresentationFramework.Classic;component/themes/Classic.xaml` | Traditional Windows 95/98/2000 appearance. |

Note

For .NET Framework applications, you may need to add references to the theme assemblies (such as PresentationFramework.Aero2) in your project. For .NET Core/.NET 5+ applications, the theme assemblies are typically included automatically.

Tip

For developer reference, Visual Studio includes XAML files for these themes in your installation directory, typically located at _C:\Program Files\Microsoft Visual Studio\2022\<edition>\DesignTools\SystemThemes\wpf_. These files are helpful for understanding theme structure but are not used at runtime.

For .NET 9 and later, you can use the new Fluent theme which supports light and dark modes:

```
<Application.Resources>
    <ResourceDictionary>
        <ResourceDictionary.MergedDictionaries>
            <ResourceDictionary Source="pack://application:,,,/PresentationFramework.Fluent;component/Themes/Fluent.xaml"/>
        </ResourceDictionary.MergedDictionaries>
    </ResourceDictionary>
</Application.Resources>
```

Alternatively, you can use the `ThemeMode` property for even simpler theme application:

```
<Application x:Class="MyApp.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             StartupUri="MainWindow.xaml"
             ThemeMode="System">
</Application>
```

*   [Pack URIs in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/pack-uris-in-wpf)
*   [How to: Find ControlTemplate-Generated Elements](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-find-controltemplate-generated-elements)
*   [Find DataTemplate-Generated Elements](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-find-datatemplate-generated-elements)
