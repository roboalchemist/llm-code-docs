# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-create-apply-style

Title: How to create a style for a control - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-create-apply-style

Markdown Content:
With Windows Presentation Foundation (WPF), you can customize an existing control's appearance with your own reusable style. Styles can be applied globally to your app, windows and pages, or directly to controls.

You can think of a [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style) as a convenient way to apply a set of property values to one or more elements. You can use a style on any element that derives from [FrameworkElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement) or [FrameworkContentElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkcontentelement) such as a [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) or a [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button).

The most common way to declare a style is as a resource in the `Resources` section in a XAML file. Because styles are resources, they obey the same scoping rules that apply to all resources. Put simply, where you declare a style affects where the style can be applied. For example, if you declare the style in the root element of your app definition XAML file, the style can be used anywhere in your app.

```
<Application x:Class="IntroToStylingAndTemplating.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="clr-namespace:IntroToStylingAndTemplating"
             StartupUri="WindowExplicitStyle.xaml">
    <Application.Resources>
        <ResourceDictionary>
            
            <Style x:Key="Header1" TargetType="TextBlock">
                <Setter Property="FontSize" Value="15" />
                <Setter Property="FontWeight" Value="ExtraBold" />
            </Style>
            
        </ResourceDictionary>
    </Application.Resources>
</Application>
```

If you declare the style in one of the app's XAML files, the style can be used only in that XAML file. For more information about scoping rules for resources, see [Overview of XAML resources](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/systems/xaml-resources-overview).

```
<Window x:Class="IntroToStylingAndTemplating.WindowSingleResource"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:IntroToStylingAndTemplating"
        mc:Ignorable="d"
        Title="WindowSingleResource" Height="450" Width="800">
    <Window.Resources>
        
        <Style x:Key="Header1" TargetType="TextBlock">
            <Setter Property="FontSize" Value="15" />
            <Setter Property="FontWeight" Value="ExtraBold" />
        </Style>
        
    </Window.Resources>
    <Grid />
</Window>
```

A style is made up of `<Setter>` child elements that set properties on the elements the style is applied to. In the example above, notice that the style is set to apply to `TextBlock` types through the `TargetType` attribute. The style will set the [FontSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.fontsize) to `15` and the [FontWeight](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.fontweight) to `ExtraBold`. Add a `<Setter>` for each property the style changes.

A [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style) is a convenient way to apply a set of property values to more than one element. For example, consider the following [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) elements and their default appearance in a window.

```
<StackPanel>
    <TextBlock>My Pictures</TextBlock>
    <TextBlock>Check out my new pictures!</TextBlock>
</StackPanel>
```

![Image 1: Styling sample screenshot before](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-style/stylingintro-textblocksbefore.png)

You can change the default appearance by setting properties, such as [FontSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.fontsize) and [FontFamily](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.fontfamily), on each [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) element directly. However, if you want your [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) elements to share some properties, you can create a [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style) in the `Resources` section of your XAML file, as shown here.

```
<Window.Resources>
    <!--A Style that affects all TextBlocks-->
    <Style TargetType="TextBlock">
        <Setter Property="HorizontalAlignment" Value="Center" />
        <Setter Property="FontFamily" Value="Comic Sans MS"/>
        <Setter Property="FontSize" Value="14"/>
    </Style>
</Window.Resources>
```

When you set the [TargetType](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style.targettype) of your style to the [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) type and omit the `x:Key` attribute, the style is applied to all the [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) elements scoped to the style, which is generally the XAML file itself.

Now the [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) elements appear as follows.

![Image 2: Styling sample screenshot base style](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-style/stylingintro-textblocksbasestyle.png)

If you add an `x:Key` attribute with value to the style, the style is no longer implicitly applied to all elements of [TargetType](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style.targettype). Only elements that explicitly reference the style will have the style applied to them.

Here is the style from the previous section, but declared with the `x:Key` attribute.

```
<Window.Resources>
    <Style x:Key="TitleText" TargetType="TextBlock">
        <Setter Property="HorizontalAlignment" Value="Center" />
        <Setter Property="FontFamily" Value="Comic Sans MS"/>
        <Setter Property="FontSize" Value="14"/>
    </Style>
</Window.Resources>
```

To apply the style, set the [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.style) property on the element to the `x:Key` value, using a [StaticResource markup extension](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/staticresource-markup-extension), as shown here.

```
<StackPanel>
    <TextBlock Style="{StaticResource TitleText}">My Pictures</TextBlock>
    <TextBlock>Check out my new pictures!</TextBlock>
</StackPanel>
```

Notice that the first [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) element has the style applied to it while the second TextBlock element remains unchanged. The implicit style from the previous section was changed to a style that declared the `x:Key` attribute, meaning, the only element affected by the style is the one that referenced the style directly.

![Image 3: Styling sample screenshot textblock](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-style/create-a-style-explicit-textblock.png)

Once a style is applied, explicitly or implicitly, it becomes sealed and can't be changed. If you want to change a style that has been applied, create a new style to replace the existing one. For more information, see the [IsSealed](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style.issealed) property.

You can create an object that chooses a style to apply based on custom logic. For an example, see the example provided for the [StyleSelector](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.styleselector) class.

To assign a named style to an element programmatically, get the style from the resources collection and assign it to the element's [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.style) property. The items in a resources collection are of type [Object](https://learn.microsoft.com/en-us/dotnet/api/system.object). Therefore, you must cast the retrieved style to a [System.Windows.Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style) before assigning it to the `Style` property. For example, the following code sets the style of a `TextBlock` named `textblock1` to the defined style `TitleText`.

```
textblock1.Style = (Style)Resources["TitleText"];
```

Perhaps you want your two [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) elements to share some property values, such as the [FontFamily](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.fontfamily) and the centered [HorizontalAlignment](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.horizontalalignment). But you also want the text **My Pictures** to have some additional properties. You can do that by creating a new style that is based on the first style, as shown here.

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

Then, apply the style to a `TextBlock`.

```
<StackPanel>
    <TextBlock Style="{StaticResource TitleText}" Name="textblock1">My Pictures</TextBlock>
    <TextBlock>Check out my new pictures!</TextBlock>
</StackPanel>
```

This `TextBlock` style is now centered, uses a `Comic Sans MS` font with a size of `26`, and the foreground color set to the [LinearGradientBrush](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.lineargradientbrush) shown in the example. Notice that it overrides the [FontSize](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.control.fontsize) value of the base style. If there's more than one [Setter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.setter) pointing to the same property in a [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style), the `Setter` that is declared last takes precedence.

The following shows what the [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) elements now look like:

![Image 4: Styled TextBlocks](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/how-to-create-apply-style/stylingintro-textblocks.png)

This `TitleText` style extends the style that has been created for the [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) type, referenced with `BasedOn="{StaticResource {x:Type TextBlock}}"`. You can also extend a style that has an `x:Key` by using the `x:Key` of the style. For example, if there was a style named `Header1` and you wanted to extend that style, you would use `BasedOn="{StaticResource Header1}"`.

As previously shown, setting the [TargetType](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style.targettype) property to `TextBlock` without assigning the style an `x:Key` causes the style to be applied to all [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) elements. In this case, the `x:Key` is implicitly set to `{x:Type TextBlock}`. This means that if you explicitly set the `x:Key` value to anything other than `{x:Type TextBlock}`, the [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style) isn't applied to all `TextBlock` elements automatically. Instead, you must apply the style (by using the `x:Key` value) to the `TextBlock` elements explicitly. If your style is in the resources section and you don't set the `TargetType` property on your style, then you must set the `x:Key` attribute.

In addition to providing a default value for the `x:Key`, the `TargetType` property specifies the type to which setter properties apply. If you don't specify a `TargetType`, you must qualify the properties in your [Setter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.setter) objects with a class name by using the syntax `Property="ClassName.Property"`. For example, instead of setting `Property="FontSize"`, you must set [Property](https://learn.microsoft.com/en-us/dotnet/api/system.windows.setter.property) to `"TextBlock.FontSize"` or `"Control.FontSize"`.

Also note that many WPF controls consist of a combination of other WPF controls. If you create a style that applies to all controls of a type, you might get unexpected results. For example, if you create a style that targets the [TextBlock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textblock) type in a [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window), the style is applied to all `TextBlock` controls in the window, even if the `TextBlock` is part of another control, such as a [ListBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.listbox).

*   [How to create a template for a control](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/how-to-create-apply-template)
*   [Overview of XAML resources](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/systems/xaml-resources-overview)
*   [XAML overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/xaml/)
