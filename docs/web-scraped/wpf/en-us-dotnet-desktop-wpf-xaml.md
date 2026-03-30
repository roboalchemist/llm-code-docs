# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/xaml/

Title: XAML language overview - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/xaml/

Markdown Content:
This article describes the features of the XAML language and demonstrates how you can use XAML to write Windows Presentation Foundation (WPF) apps. This article specifically describes XAML as implemented by WPF. XAML itself is a larger language concept than WPF.

XAML is a declarative markup language. As applied to the .NET programming model, XAML simplifies creating a UI for a .NET app. You can create visible UI elements in the declarative XAML markup, and then separate the UI definition from the run-time logic by using code-behind files that are joined to the markup through partial class definitions. XAML directly represents the instantiation of objects in a specific set of backing types defined in assemblies. This is unlike most other markup languages, which are typically an interpreted language without such a direct tie to a backing type system. XAML enables a workflow where separate parties can work on the UI and the logic of an app, using potentially different tools.

When represented as text, XAML files are XML files that generally have the `.xaml` extension. The files can be encoded by any XML encoding, but encoding as UTF-8 is typical.

The following example shows how you might create a button as part of a UI. This example is intended to give you a flavor of how XAML represents common UI programming metaphors (it's not a complete sample).

```
<StackPanel>
    <Button Content="Click Me"/>
</StackPanel>
```

The following sections explain the basic forms of XAML syntax, and give a short markup example. These sections aren't intended to provide complete information about each syntax form, such as how these are represented in the backing type system. For more information about the specifics of XAML syntax, see [XAML Syntax In Detail](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/xaml-syntax-in-detail).

Much of the material in the next few sections will be elementary to you if you have previous familiarity with the XML language. This is a consequence of one of the basic design principles of XAML. The XAML language defines concepts of its own, but these concepts work within the XML language and markup form.

An object element typically declares an instance of a type. That type is defined in the assemblies referenced by the technology that uses XAML as a language.

Object element syntax always starts with an opening angle bracket (`<`). This is followed by the name of the type where you want to create an instance. (The name can include a prefix, a concept that will be explained later.) After this, you can optionally declare attributes on the object element. To complete the object element tag, end with a closing angle bracket (`>`). You can instead use a self-closing form that doesn't have any content, by completing the tag with a forward slash and closing angle bracket in succession (`/>`). For example, look at the previously shown markup snippet again.

```
<StackPanel>
    <Button Content="Click Me"/>
</StackPanel>
```

This specifies two object elements: `<StackPanel>` (with content, and a closing tag later), and `<Button .../>` (the self-closing form, with several attributes). The object elements `StackPanel` and `Button` each map to the name of a class that is defined by WPF and is part of the WPF assemblies. When you specify an object element tag, you create an instruction for XAML processing to create a new instance of the underlying type. Each instance is created by calling the parameterless constructor of the underlying type when parsing and loading the XAML.

Properties of an object can often be expressed as attributes of the object element. The attribute syntax names the object property that is being set, followed by the assignment operator (=). The value of an attribute is always specified as a string that is contained within quotation marks.

Attribute syntax is the most streamlined property setting syntax and is the most intuitive syntax to use for developers who have used markup languages in the past. For example, the following markup creates a button that has red text and a blue background with a display text of `Content`.

```
<Button Background="Blue" Foreground="Red" Content="This is a button"/>
```

For some properties of an object element, attribute syntax isn't possible, because the object or information necessary to provide the property value can't be adequately expressed within the quotation mark and string restrictions of attribute syntax. For these cases, a different syntax known as property element syntax can be used.

The syntax for the property element start tag is `<TypeName.PropertyName>`. Generally, the content of that tag is an object element of the type that the property takes as its value. After specifying the content, you must close the property element with an end tag. The syntax for the end tag is `</TypeName.PropertyName>`.

If an attribute syntax is possible, using the attribute syntax is typically more convenient and enables a more compact markup, but that is often just a matter of style, not a technical limitation. The following example shows the same properties being set as in the previous attribute syntax example, but this time by using property element syntax for all properties of the `Button`.

```
<Button>
    <Button.Background>
        <SolidColorBrush Color="Blue"/>
    </Button.Background>
    <Button.Foreground>
        <SolidColorBrush Color="Red"/>
    </Button.Foreground>
    <Button.Content>
        This is a button
    </Button.Content>
</Button>
```

The XAML language includes some optimizations that produce more human-readable markup. One such optimization is that if a particular property takes a collection type, then items that you declare in markup as child elements within that property's value become part of the collection. In this case, a collection of child object elements is the value being set to the collection property.

The following example shows collection syntax for setting values of the [GradientStops](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.gradientbrush.gradientstops) property.

```
<LinearGradientBrush>
    <LinearGradientBrush.GradientStops>
        <!-- no explicit new GradientStopCollection, parser knows how to find or create -->
        <GradientStop Offset="0.0" Color="Red" />
        <GradientStop Offset="1.0" Color="Blue" />
    </LinearGradientBrush.GradientStops>
</LinearGradientBrush>
```

XAML specifies a language feature whereby a class can designate exactly one of its properties to be the XAML _content_ property. Child elements of that object element are used to set the value of that content property. In other words, for the content property uniquely, you can omit a property element when setting that property in XAML markup and produce a more visible parent/child metaphor in the markup.

For example, [Border](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.border) specifies a _content_ property of [Child](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.decorator.child). The following two [Border](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.border) elements are treated identically. The first one takes advantage of the content property syntax and omits the `Border.Child` property element. The second one shows `Border.Child` explicitly.

```
<Border>
    <TextBox Width="300"/>
</Border>
<!--explicit equivalent-->
<Border>
    <Border.Child>
        <TextBox Width="300"/>
    </Border.Child>
</Border>
```

As a rule of the XAML language, the value of a XAML content property must be given either entirely before or entirely after any other property elements on that object element. For instance, the following markup doesn't compile.

```
<Button>I am a
  <Button.Background>Blue</Button.Background>
  blue button</Button>
```

For more information about the specifics of XAML syntax, see [XAML Syntax In Detail](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/xaml-syntax-in-detail).

A small number of XAML elements can directly process text as their content. To enable this, one of the following cases must be true:

*   The class must declare a content property, and that content property must be of a type assignable to a string (the type could be [Object](https://learn.microsoft.com/en-us/dotnet/api/system.object)). For instance, any [ContentControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol) uses [Content](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol.content) as its content property and it's type [Object](https://learn.microsoft.com/en-us/dotnet/api/system.object), and this supports the following usage on a [ContentControl](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.contentcontrol) such as a [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button): `<Button>Hello</Button>`.

*   The type must declare a type converter, in which case the text content is used as initialization text for that type converter. For example, `<Brush>Blue</Brush>` converts the content value of `Blue` into a brush. This case is less common in practice.

*   The type must be a known XAML language primitive.

Consider this example.

```
<StackPanel>
    <Button>First Button</Button>
    <Button>Second Button</Button>
</StackPanel>
```

Here, each [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button) is a child element of [StackPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.stackpanel). This is a streamlined and intuitive markup that omits two tags for two different reasons.

*   **Omitted StackPanel.Children property element:**[StackPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.stackpanel) derives from [Panel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.panel). [Panel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.panel) defines [Panel.Children](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.panel.children) as its XAML content property.

*   **Omitted UIElementCollection object element:** The [Panel.Children](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.panel.children) property takes the type [UIElementCollection](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.uielementcollection), which implements [IList](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ilist). The collection's element tag can be omitted, based on the XAML rules for processing collections such as [IList](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ilist). (In this case, [UIElementCollection](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.uielementcollection) actually can't be instantiated because it doesn't expose a parameterless constructor, and that is why the [UIElementCollection](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.uielementcollection) object element is shown commented out).

```
<StackPanel>
    <StackPanel.Children>
        <!--<UIElementCollection>-->
        <Button>First Button</Button>
        <Button>Second Button</Button>
        <!--</UIElementCollection>-->
    </StackPanel.Children>
</StackPanel>
```

Attribute syntax can also be used for members that are events rather than properties. In this case, the attribute's name is the name of the event. In the WPF implementation of events for XAML, the attribute's value is the name of a handler that implements that event's delegate. For example, the following markup assigns a handler for the [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.buttonbase.click#system-windows-controls-primitives-buttonbase-click) event to a [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button) created in markup:

```
<Button Click="Button_Click" >Click Me!</Button>
```

There's more to events and XAML in WPF than just this example of the attribute syntax. For example, you might wonder what the `ClickHandler` referenced here represents and how it's defined. This will be explained in the upcoming [Events and XAML code-behind](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/xaml/#events-and-xaml-code-behind) section of this article.

In general, XAML is case-sensitive. For purposes of resolving backing types, WPF XAML is case-sensitive by the same rules that the CLR is case-sensitive. Object elements, property elements, and attribute names must all be specified by using the sensitive casing when compared by name to the underlying type in the assembly, or to a member of a type. XAML language keywords and primitives are also case-sensitive. Values aren't always case-sensitive. Case sensitivity for values will depend on the type converter behavior associated with the property that takes the value, or the property value type. For example, properties that take the [Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean) type can take either `true` or `True` as equivalent values, but only because the native WPF XAML parser type conversion for string to [Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean) already permits these as equivalents.

WPF XAML processors and serializers will ignore or drop all nonsignificant white space, and will normalize any significant white space. This is consistent with the default white-space behavior recommendations of the XAML specification. This behavior is only of consequence when you specify strings within XAML content properties. In simplest terms, XAML converts space, linefeed, and tab characters into spaces, and then preserves one space if found at either end of a contiguous string. The full explanation of XAML white-space handling isn't covered in this article. For more information, see [White space processing in XAML](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/white-space-processing).

Markup extensions are a XAML language concept. When used to provide the value of an attribute syntax, curly braces (`{` and `}`) indicate a markup extension usage. This usage directs the XAML processing to escape from the general treatment of attribute values as either a literal string or a string-convertible value.

The most common markup extensions used in WPF app programming are [`Binding`](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/binding-markup-extension), used for data binding expressions, and the resource references [`StaticResource`](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/staticresource-markup-extension) and [`DynamicResource`](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/dynamicresource-markup-extension). By using markup extensions, you can use attribute syntax to provide values for properties even if that property doesn't support an attribute syntax in general. Markup extensions often use intermediate expression types to enable features such as deferring values or referencing other objects that are only present at run-time.

For example, the following markup sets the value of the [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.style) property using attribute syntax. The [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.style) property takes an instance of the [Style](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style) class, which by default could not be instantiated by an attribute syntax string. But in this case, the attribute references a particular markup extension, `StaticResource`. When that markup extension is processed, it returns a reference to a style that was previously instantiated as a keyed resource in a resource dictionary.

```
<Window x:Class="index.Window1"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Window1" Height="100" Width="300">
    <Window.Resources>
        <SolidColorBrush x:Key="MyBrush" Color="Gold"/>
        <Style TargetType="Border" x:Key="PageBackground">
            <Setter Property="BorderBrush" Value="Blue"/>
            <Setter Property="BorderThickness" Value="5" />
        </Style>
    </Window.Resources>
    <Border Style="{StaticResource PageBackground}">
        <StackPanel>
            <TextBlock Text="Hello" />
        </StackPanel>
    </Border>
</Window>
```

For a reference listing of all markup extensions for XAML implemented specifically in WPF, see [WPF XAML Extensions](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/wpf-xaml-extensions). For a reference listing of the markup extensions that are defined by System.Xaml and are more widely available for .NET XAML implementations, see [XAML Namespace (x:) Language Features](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/namespace-language-features). For more information about markup extension concepts, see [Markup Extensions and WPF XAML](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/markup-extensions-and-wpf-xaml).

In the [XAML Syntax in Brief](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/xaml/#xaml-syntax-in-brief) section, it was stated that the attribute value must be able to be set by a string. The basic, native handling of how strings are converted into other object types or primitive values is based on the [String](https://learn.microsoft.com/en-us/dotnet/api/system.string) type itself, along with native processing for certain types such as [DateTime](https://learn.microsoft.com/en-us/dotnet/api/system.datetime) or [Uri](https://learn.microsoft.com/en-us/dotnet/api/system.uri). But many WPF types or members of those types extend the basic string attribute processing behavior in such a way that instances of more complex object types can be specified as strings and attributes.

The [Thickness](https://learn.microsoft.com/en-us/dotnet/api/system.windows.thickness) structure is an example of a type that has a type conversion enabled for XAML usages. [Thickness](https://learn.microsoft.com/en-us/dotnet/api/system.windows.thickness) indicates measurements within a nested rectangle and is used as the value for properties such as [Margin](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.margin). By placing a type converter on [Thickness](https://learn.microsoft.com/en-us/dotnet/api/system.windows.thickness), all properties that use a [Thickness](https://learn.microsoft.com/en-us/dotnet/api/system.windows.thickness) are easier to specify in XAML because they can be specified as attributes. The following example uses a type conversion and attribute syntax to provide a value for a [Margin](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.margin):

```
<Button Margin="10,20,10,30" Content="Click me"/>
```

The previous attribute syntax example is equivalent to the following more verbose syntax example, where the [Margin](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.margin) is instead set through property element syntax containing a [Thickness](https://learn.microsoft.com/en-us/dotnet/api/system.windows.thickness) object element. The four key properties of [Thickness](https://learn.microsoft.com/en-us/dotnet/api/system.windows.thickness) are set as attributes on the new instance:

```
<Button Content="Click me">
    <Button.Margin>
        <Thickness Left="10" Top="20" Right="10" Bottom="30"/>
    </Button.Margin>
</Button>
```

Note

There are also a limited number of objects where the type conversion is the only public way to set a property to that type without involving a subclass, because the type itself doesn't have a parameterless constructor. An example is [Cursor](https://learn.microsoft.com/en-us/dotnet/api/system.windows.input.cursor).

For more information on type conversion, see [TypeConverters and XAML](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/typeconverters-and-xaml).

A XAML file must have only one root element, to be both a well-formed XML file and a valid XAML file. For typical WPF scenarios, you use a root element that has a prominent meaning in the WPF app model (for example, [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) or [Page](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.page) for a page, [ResourceDictionary](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resourcedictionary) for an external dictionary, or [Application](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application) for the app definition). The following example shows the root element of a typical XAML file for a WPF page, with the root element of [Page](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.page).

```
<Page x:Class="index.Page1"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      Title="Page1">

</Page>
```

The root element also contains the attributes `xmlns` and `xmlns:x`. These attributes indicate to a XAML processor which XAML namespaces contain the type definitions for backing types that the markup will reference as elements. The `xmlns` attribute specifically indicates the default XAML namespace. Within the default XAML namespace, object elements in the markup can be specified without a prefix. For most WPF app scenarios, and for almost all of the examples given in the WPF sections of the SDK, the default XAML namespace is mapped to the WPF namespace `http://schemas.microsoft.com/winfx/2006/xaml/presentation`. The `xmlns:x` attribute indicates an additional XAML namespace, which maps the XAML language namespace `http://schemas.microsoft.com/winfx/2006/xaml`.

This usage of `xmlns` to define a scope for usage and mapping of a namescope is consistent with the XML 1.0 specification. XAML namescopes are different from XML namescopes only in that a XAML namescope also implies something about how the namescope's elements are backed by types when it comes to type resolution and parsing the XAML.

The `xmlns` attributes are only strictly necessary on the root element of each XAML file. `xmlns` definitions will apply to all descendant elements of the root element (this behavior is again consistent with the XML 1.0 specification for `xmlns`.) `xmlns` attributes are also permitted on other elements underneath the root, and would apply to any descendant elements of the defining element. However, frequent definition or redefinition of XAML namespaces can result in a XAML markup style that is difficult to read.

The WPF implementation of its XAML processor includes an infrastructure that has awareness of the WPF core assemblies. The WPF core assemblies are known to contain the types that support the WPF mappings to the default XAML namespace. This is enabled through configuration that is part of your project build file and the WPF build and project systems. Therefore, declaring the default XAML namespace as the default `xmlns` is all that is necessary to reference XAML elements that come from WPF assemblies.

In the previous root element example, the prefix `x:` was used to map the XAML namespace `http://schemas.microsoft.com/winfx/2006/xaml`, which is the dedicated XAML namespace that supports XAML language constructs. This `x:` prefix is used for mapping this XAML namespace in the templates for projects, in examples, and in documentation throughout this SDK. The XAML namespace for the XAML language contains several programming constructs that you will use frequently in your XAML. The following is a listing of the most common `x:` prefix programming constructs you will use:

*   [x:Key](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xkey-directive): Sets a unique key for each resource in a [ResourceDictionary](https://learn.microsoft.com/en-us/dotnet/api/system.windows.resourcedictionary) (or similar dictionary concepts in other frameworks). `x:Key` will probably account for 90 percent of the `x:` usages you will see in a typical WPF app's markup.

*   [x:Class](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xclass-directive): Specifies the CLR namespace and class name for the class that provides code-behind for a XAML page. You must have such a class to support code-behind per the WPF programming model, and therefore you almost always see `x:` mapped, even if there are no resources.

*   [x:Name](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xname-directive): Specifies a run-time object name for the instance that exists in run-time code after an object element is processed. In general, you will frequently use a WPF-defined equivalent property for [x:Name](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xname-directive). Such properties map specifically to a CLR backing property and are thus more convenient for app programming, where you frequently use run-time code to find the named elements from initialized XAML. The most common such property is [FrameworkElement.Name](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.name). You might still use [x:Name](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xname-directive) when the equivalent WPF framework-level [Name](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.name) property isn't supported in a particular type. This occurs in certain animation scenarios.

*   [x:Static](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xstatic-markup-extension): Enables a reference that returns a static value that isn't otherwise a XAML-compatible property.

*   [x:Type](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xtype-markup-extension): Constructs a [Type](https://learn.microsoft.com/en-us/dotnet/api/system.type) reference based on a type name. This is used to specify attributes that take [Type](https://learn.microsoft.com/en-us/dotnet/api/system.type), such as [Style.TargetType](https://learn.microsoft.com/en-us/dotnet/api/system.windows.style.targettype), although frequently the property has native string-to-[Type](https://learn.microsoft.com/en-us/dotnet/api/system.type) conversion in such a way that the [x:Type](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xtype-markup-extension) markup extension usage is optional.

There are additional programming constructs in the `x:` prefix/XAML namespace, which aren't as common. For details, see [XAML Namespace (x:) Language Features](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/namespace-language-features).

For your own custom assemblies, or for assemblies outside the WPF core of **PresentationCore**, **PresentationFramework** and **WindowsBase**, you can specify the assembly as part of a custom `xmlns` mapping. You can then reference types from that assembly in your XAML, so long as that type is correctly implemented to support the XAML usages you are attempting.

The following is a basic example of how custom prefixes work in XAML markup. The prefix `custom` is defined in the root element tag, and mapped to a specific assembly that is packaged and available with the app. This assembly contains a type `NumericUpDown`, which is implemented to support general XAML usage as well as using a class inheritance that permits its insertion at this particular point in a WPF XAML content model. An instance of this `NumericUpDown` control is declared as an object element, using the prefix so that a XAML parser knows which XAML namespace contains the type, and therefore where the backing assembly is that contains the type definition.

```
<Page
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:custom="clr-namespace:NumericUpDownCustomControl;assembly=CustomLibrary"
    >
  <StackPanel Name="LayoutRoot">
    <custom:NumericUpDown Name="numericCtrl1" Width="100" Height="60"/>
...
  </StackPanel>
</Page>
```

For more information about custom types in XAML, see [XAML and Custom Classes for WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/xaml-and-custom-classes-for-wpf).

For more information about how XML namespaces and code namespaces in assemblies are related, see [XAML Namespaces and Namespace Mapping for WPF XAML](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/xaml-namespaces-and-namespace-mapping-for-wpf-xaml).

Most WPF apps consist of both XAML markup and code-behind. Within a project, the XAML is written as a `.xaml` file, and a CLR language such as Microsoft Visual Basic or C# is used to write a code-behind file. When a XAML file is markup compiled as part of the WPF programming and application models, the location of the XAML code-behind file for a XAML file is identified by specifying a namespace and class as the `x:Class` attribute of the root element of the XAML.

In the examples so far, you have seen several buttons, but none of these buttons had any logical behavior associated with them yet. The primary application-level mechanism for adding a behavior for an object element is to use an existing event of the element class, and to write a specific handler for that event that is invoked when that event is raised at run-time. The event name and the name of the handler to use are specified in the markup, whereas the code that implements your handler is defined in the code-behind.

```
<Page x:Class="ExampleNamespace.ExamplePage"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
    <StackPanel>
        <Button Click="Button_Click">Click me</Button>
    </StackPanel>
</Page>
```

```
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace ExampleNamespace;

public partial class ExamplePage : Page
{
    public ExamplePage() =>
        InitializeComponent();

    private void Button_Click(object sender, RoutedEventArgs e)
    {
        var buttonControl = (Button)e.Source;
        buttonControl.Foreground = Brushes.Red;
    }
}
```

Notice that the code-behind file uses the CLR namespace `ExampleNamespace` (the namespace isn't visible in Visual Basic) and declares `ExamplePage` as a partial class within that namespace. This parallels the `x:Class` attribute value of `ExampleNamespace`.`ExamplePage` that was provided in the markup root. The WPF markup compiler will create a partial class for any compiled XAML file, by deriving a class from the root element type. When you provide code-behind that also defines the same partial class, the resulting code is combined within the same namespace and class of the compiled app.

Important

In Visual Basic, the root namespace is implied for both the XAML and code-behind. Only nested namespaces are visible. This article demonstrates the C# project's XAML.

For more information about requirements for code-behind programming in WPF, see [Code-behind, Event Handler, and Partial Class Requirements in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/code-behind-and-xaml-in-wpf#code-behind-event-handler-and-partial-class-requirements-in-wpf).

If you don't want to create a separate code-behind file, you can also inline your code in a XAML file. However, inline code is a less versatile technique that has substantial limitations. For more information, see [Code-Behind and XAML in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/code-behind-and-xaml-in-wpf).

A particular event feature that is fundamental to WPF is a routed event. Routed events enable an element to handle an event that was raised by a different element, as long as the elements are connected through a tree relationship. When specifying event handling with a XAML attribute, the routed event can be listened for and handled on any element, including elements that don't list that particular event in the class members table. This is accomplished by qualifying the event name attribute with the owning class name. For instance, the parent `StackPanel` in the ongoing `StackPanel` / `Button` example could register a handler for the child element button's [Click](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.buttonbase.click#system-windows-controls-primitives-buttonbase-click) event by specifying the attribute `Button.Click` on the `StackPanel` object element, with your handler name as the attribute value. For more information, see [Routed Events Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/events/routed-events-overview).

By default, the object instance that is created in an object graph by processing a XAML object element doesn't have a unique identifier or object reference. In contrast, if you call a constructor in code, you almost always use the constructor result to set a variable to the constructed instance, so that you can reference the instance later in your code. To provide standardized access to objects that were created through a markup definition, XAML defines the [x:Name attribute](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xname-directive). You can set the value of the `x:Name` attribute on any object element. In your code-behind, the identifier you choose is equivalent to an instance variable that refers to the constructed instance. In all respects, named elements function as if they were object instances (the name references that instance), and your code-behind can reference the named elements to handle run-time interactions within the app. This connection between instances and variables is accomplished by the WPF XAML markup compiler, and more specifically involve features and patterns such as [InitializeComponent](https://learn.microsoft.com/en-us/dotnet/api/system.windows.markup.icomponentconnector.initializecomponent) that won't be discussed in detail in this article.

WPF framework-level XAML elements inherit a [Name](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.name) property, which is equivalent to the XAML defined `x:Name` attribute. Certain other classes also provide property-level equivalents for `x:Name`, which is also usually defined as a `Name` property. Generally speaking, if you can't find a `Name` property in the members table for your chosen element/type, use `x:Name` instead. The `x:Name` values will provide an identifier to a XAML element that can be used at run-time, either by specific subsystems or by utility methods such as [FindName](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.findname).

The following example sets [Name](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.name) on a [StackPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.stackpanel) element. Then, a handler on a [Button](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.button) within that [StackPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.stackpanel) references the [StackPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.stackpanel) through its instance reference `buttonContainer` as set by [Name](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.name).

```
<StackPanel Name="buttonContainer">
    <Button Click="RemoveThis_Click">Click to remove this button</Button>
</StackPanel>
```

```
private void RemoveThis_Click(object sender, RoutedEventArgs e)
{
    var element = (FrameworkElement)e.Source;
    
    if (buttonContainer.Children.Contains(element))
        buttonContainer.Children.Remove(element);
}
```

Just like a variable, the XAML name for an instance is governed by a concept of scope, so that names can be enforced to be unique within a certain scope that is predictable. The primary markup that defines a page denotes one unique XAML namescope, with the XAML namescope boundary being the root element of that page. However, other markup sources can interact with a page at run-time, such as styles or templates within styles, and such markup sources often have their own XAML namescopes that don't necessarily connect with the XAML namescope of the page. For more information on `x:Name` and XAML namescopes, see [Name](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.name), [x:Name Directive](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/xname-directive), or [WPF XAML Namescopes](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/wpf-xaml-namescopes).

XAML specifies a language feature that enables certain properties or events to be specified on any element, even if the property or event doesn't exist in the type's definitions for the element it's being set on. The properties version of this feature is called an attached property, the events version is called an attached event. Conceptually, you can think of attached properties and attached events as global members that can be set on any XAML element/object instance. However, that element/class or a larger infrastructure must support a backing property store for the attached values.

Attached properties in XAML are typically used through attribute syntax. In attribute syntax, you specify an attached property in the form `ownerType.propertyName`.

Superficially, this resembles a property element usage, but in this case the `ownerType` you specify is always a different type than the object element where the attached property is being set. `ownerType` is the type that provides the accessor methods that are required by a XAML processor to get or set the attached property value.

The most common scenario for attached properties is to enable child elements to report a property value to their parent element.

The following example illustrates the [DockPanel.Dock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel.dock) attached property. The [DockPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel) class defines the accessors for [DockPanel.Dock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel.dock) and owns the attached property. The [DockPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel) class also includes logic that iterates its child elements and specifically checks each element for a set value of [DockPanel.Dock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel.dock). If a value is found, that value is used during layout to position the child elements. Use of the [DockPanel.Dock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel.dock) attached property and this positioning capability is in fact the motivating scenario for the [DockPanel](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel) class.

```
<DockPanel>
    <Button DockPanel.Dock="Left" Width="100" Height="20">I am on the left</Button>
    <Button DockPanel.Dock="Right" Width="100" Height="20">I am on the right</Button>
</DockPanel>
```

In WPF, most or all the attached properties are also implemented as dependency properties. For more information, see [Attached Properties Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/properties/attached-properties-overview).

Attached events use a similar `ownerType.eventName` form of attribute syntax. Just like the non-attached events, the attribute value for an attached event in XAML specifies the name of the handler method that is invoked when the event is handled on the element. Attached event usages in WPF XAML are less common. For more information, see [Attached Events Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/events/attached-events-overview).

Underlying WPF XAML and its XAML namespace is a collection of types that correspond to CLR objects and markup elements for XAML. However, not all classes can be mapped to elements. Abstract classes, such as [ButtonBase](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.buttonbase), and certain non-abstract base classes, are used for inheritance in the CLR objects model. Base classes, including abstract ones, are still important to XAML development because each of the concrete XAML elements inherits members from some base class in its hierarchy. Often these members include properties that can be set as attributes on the element, or events that can be handled. [FrameworkElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement) is the concrete base UI class of WPF at the WPF framework level. When designing UI, you will use various shape, panel, decorator, or control classes, which all derive from [FrameworkElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement). A related base class, [FrameworkContentElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkcontentelement), supports document-oriented elements that work well for a flow layout presentation, using APIs that deliberately mirror the APIs in [FrameworkElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement). The combination of attributes at the element level and a CLR object model provides you with a set of common properties that are settable on most concrete XAML elements, regardless of the specific XAML element and its underlying type.

XAML is a markup language that directly represents object instantiation and execution. That's why elements created in XAML have the same ability to interact with system resources (network access, file system IO, for example) as your app code does. XAML also has the same access to the system resources as the hosting app does.

Unlike .NET Framework, WPF for .NET doesn't support CAS. For more information, see [Code Access Security differences](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/migration/differences-from-net-framework#code-access-security).

XAML can be used to define all of the UI, but it's sometimes also appropriate to define just a piece of the UI in XAML. This capability could be used to:

*   Enable partial customization.
*   Local storage of UI information.
*   Model a business object.

The key to these scenarios is the [XamlReader](https://learn.microsoft.com/en-us/dotnet/api/system.windows.markup.xamlreader) class and its [Load](https://learn.microsoft.com/en-us/dotnet/api/system.windows.markup.xamlreader.load) method. The input is a XAML file, and the output is an object that represents all of the run-time tree of objects that was created from that markup. You then can insert the object to be a property of another object that already exists in the app. As long as the property is in the content model and has display capabilities that will notify the execution engine that new content has been added into the app, you can modify a running app's contents easily by dynamically loading in XAML.

*   [XAML Syntax In Detail](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/xaml-syntax-in-detail)
*   [XAML and Custom Classes for WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/xaml-and-custom-classes-for-wpf)
*   [XAML Namespace (x:) Language Features](https://learn.microsoft.com/en-us/dotnet/desktop/xaml-services/namespace-language-features)
*   [WPF XAML Extensions](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/wpf-xaml-extensions)
*   [Base Elements Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/base-elements-overview)
*   [Trees in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/trees-in-wpf)
