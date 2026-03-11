# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/binding-declarations-overview

Title: Binding declarations overview - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/binding-declarations-overview

Markdown Content:
Typically, developers declare the bindings directly in the XAML markup of the UI elements they want to bind data to. However, you can also declare bindings in code. This article describes how to declare bindings in both XAML and in code.

Before reading this article, it's important that you're familiar with the concept and usage of markup extensions. For more information about markup extensions, see [Markup Extensions and WPF XAML](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/markup-extensions-and-wpf-xaml).

This article doesn't cover data binding concepts. For a discussion of data binding concepts, see [Data binding overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/#basic-data-binding-concepts).

[Binding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding) is a markup extension. When you use the binding extension to declare a binding, the declaration consists of a series of clauses following the `Binding` keyword and separated by commas (,). The clauses in the binding declaration can be in any order and there are many possible combinations. The clauses are _Name_=_Value_ pairs, where _Name_ is the name of the [Binding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding) property and _Value_ is the value you're setting for the property.

When creating binding declaration strings in markup, they must be attached to the specific dependency property of a target object. The following example shows how to bind the [TextBox.Text](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textbox.text) property using the binding extension, specifying the [Source](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.source) and [Path](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.path) properties.

```
<TextBlock Text="{Binding Source={StaticResource myDataSource}, Path=Name}"/>
```

The previous example uses a simple data object type of `Person`. The following snippet is the code for that object:

```
class Person
{
    public string Name { get; set; }
    public DateTime Birthdate { get; set; }
}
```

You can specify most of the properties of the [Binding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding) class this way. For more information about the binding extension and for a list of [Binding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding) properties that cannot be set using the binding extension, see the [Binding Markup Extension (.NET Framework)](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/binding-markup-extension) overview.

For an example on creating a binding in XAML, see [How to create a data binding](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-create-a-simple-binding).

Object element syntax is an alternative to creating the binding declaration. In most cases, there's no particular advantage to using either the markup extension or the object element syntax. However, when the markup extension doesn't support your scenario, such as when your property value is of a non-string type for which no type conversion exists, you need to use the object element syntax.

The previous section demonstrated how to bind with a XAML extension. The following example demonstrates doing the same binding but uses object element syntax:

```
<TextBlock>
    <TextBlock.Text>
        <Binding Source="{StaticResource myDataSource}" Path="Name"/>
    </TextBlock.Text>
</TextBlock>
```

For more information about the different terms, see [XAML Syntax In Detail (.NET Framework)](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/xaml-syntax-in-detail).

[MultiBinding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.multibinding) and [PriorityBinding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.prioritybinding) don't support the XAML extension syntax. That's why you must use the object element syntax if you're declaring a [MultiBinding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.multibinding) or a [PriorityBinding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.prioritybinding) in XAML.

Another way to specify a binding is to set properties directly on a [Binding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding) object in code, and then assign the binding to a property. The following example shows how to create a [Binding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding) object in code.

```
private void Window_Loaded(object sender, RoutedEventArgs e)
{
    // Make a new data source object
    var personDetails = new Person()
    {
        Name = "John",
        Birthdate = DateTime.Parse("2001-02-03")
    };

    // New binding object using the path of 'Name' for whatever source object is used
    var nameBindingObject = new Binding("Name");

    // Configure the binding
    nameBindingObject.Mode = BindingMode.OneWay;
    nameBindingObject.Source = personDetails;
    nameBindingObject.Converter = NameConverter.Instance;
    nameBindingObject.ConverterCulture = new CultureInfo("en-US");

    // Set the binding to a target object. The TextBlock.Name property on the NameBlock UI element
    BindingOperations.SetBinding(NameBlock, TextBlock.TextProperty, nameBindingObject);
}
```

The previous code set the following on the binding:

*   A path of the property on the data source object.
*   The mode of the binding.
*   The data source, in this case, a simple object instance representing a person.
*   An optional converter that processes the value coming in from the data source object before it's assigned to the target property.

When the object you're binding is a [FrameworkElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement) or a [FrameworkContentElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkcontentelement), you can call the `SetBinding` method on your object directly instead of using [BindingOperations.SetBinding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingoperations.setbinding). For an example, see [How to: Create a Binding in Code](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-create-a-binding-in-code).

The previous example uses a simple data object type of `Person`. The following is the code for that object:

```
class Person
{
    public string Name { get; set; }
    public DateTime Birthdate { get; set; }
}
```

Use the [Path](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.path) property to specify the source value you want to bind to:

*   In the simplest case, the [Path](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.path) property value is the name of the property of the source object to use for the binding, such as `Path=PropertyName`.

*   Subproperties of a property can be specified by a similar syntax as in C#. For instance, the clause `Path=ShoppingCart.Order` sets the binding to the subproperty `Order` of the object or property `ShoppingCart`.

*   To bind to an attached property, place parentheses around the attached property. For example, to bind to the attached property [DockPanel.Dock](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.dockpanel.dock), the syntax is `Path=(DockPanel.Dock)`.

*   Indexers of a property can be specified within square brackets following the property name where the indexer is applied. For instance, the clause `Path=ShoppingCart[0]` sets the binding to the index that corresponds to how your property's internal indexing handles the literal string "0". Nested indexers are also supported.

*   Indexers and subproperties can be mixed in a `Path` clause; for example, `Path=ShoppingCart.ShippingInfo[MailingAddress,Street].`

*   Inside indexers. You can have multiple indexer parameters separated by commas (`,`). The type of each parameter can be specified with parentheses. For example, you can have `Path="[(sys:Int32)42,(sys:Int32)24]"`, where `sys` is mapped to the `System` namespace.

*   When the source is a collection view, the current item can be specified with a slash (`/`). For example, the clause `Path=/` sets the binding to the current item in the view. When the source is a collection, this syntax specifies the current item of the default collection view.

*   Property names and slashes can be combined to traverse properties that are collections. For example, `Path=/Offices/ManagerName` specifies the current item of the source collection, which contains an `Offices` property that is also a collection. Its current item is an object that contains a `ManagerName` property.

*   Optionally, a period (`.`) path can be used to bind to the current source. For example, `Text="{Binding}"` is equivalent to `Text="{Binding Path=.}"`.

*   Inside indexers (`[ ]`), the caret character (`^`) escapes the next character.

*   If you set [Path](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.path) in XAML, you also need to escape (using XML entities) certain characters that are special to the XML language definition:

    *   Use `&amp;` to escape the character "`&`".

    *   Use `&gt;` to escape the end tag "`>`".

*   Additionally, if you describe the entire binding in an attribute using the markup extension syntax, you need to escape (using backslash `\`) characters that are special to the WPF markup extension parser:

    *   Backslash (`\`) is the escape character itself.

    *   The equal sign (`=`) separates property name from property value.

    *   Comma (`,`) separates properties.

    *   The right curly brace (`}`) is the end of a markup extension.

Use the [Binding.Mode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.mode) property to specify the direction of the binding. The following modes are the available options for binding updates:

| Binding mode | Description |
| --- | --- |
| [BindingMode.TwoWay](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-twoway) | Updates the target property or the property whenever either the target property or the source property changes. |
| [BindingMode.OneWay](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-oneway) | Updates the target property only when the source property changes. |
| [BindingMode.OneTime](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-onetime) | Updates the target property only when the application starts or when the [DataContext](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.datacontext) undergoes a change. |
| [BindingMode.OneWayToSource](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-onewaytosource) | Updates the source property when the target property changes. |
| [BindingMode.Default](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-default) | Causes the default [Mode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.mode) value of target property to be used. |

For more information, see the [BindingMode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode) enumeration.

The following example shows how to set the [Mode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.mode) property:

```
<TextBlock Name="IncomeText" Text="{Binding Path=TotalIncome, Mode=OneTime}" />
```

To detect source changes (applicable to [OneWay](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-oneway) and [TwoWay](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-twoway) bindings), the source must implement a suitable property change notification mechanism such as [INotifyPropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged). For more information, see [Providing change notifications](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/binding-sources-overview#provide-change-notifications).

For [TwoWay](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-twoway) or [OneWayToSource](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.bindingmode#system-windows-data-bindingmode-onewaytosource) bindings, you can control the timing of the source updates by setting the [UpdateSourceTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.updatesourcetrigger) property. For more information, see [UpdateSourceTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.updatesourcetrigger).

The default behavior is as follows if not specified in the declaration:

*   A default converter is created that tries to do a type conversion between the binding source value and the binding target value. If a conversion cannot be made, the default converter returns `null`.

*   If you don't set [ConverterCulture](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.converterculture), the binding engine uses the `Language` property of the binding target object. In XAML, this defaults to `en-US` or inherits the value from the root element (or any element) of the page, if one has been explicitly set.

*   As long as the binding already has a data context (for example, the inherited data context coming from a parent element), and whatever item or collection being returned by that context is appropriate for binding without requiring further path modification, a binding declaration can have no clauses at all: `{Binding}`. This is often the way a binding is specified for data styling, where the binding acts upon a collection. For more information, see [Using Entire Objects as a Binding Source](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/binding-sources-overview#entire-objects-as-a-binding-source).

*   The default [Mode](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.mode) varies between one-way and two-way depending on the dependency property that is being bound. You can always declare the binding mode explicitly to ensure that your binding has the desired behavior. In general, user-editable control properties, such as [TextBox.Text](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textbox.text) and [RangeBase.Value](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.primitives.rangebase.value), default to two-way bindings, but most other properties default to one-way bindings.

*   The default [UpdateSourceTrigger](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.binding.updatesourcetrigger) value varies between [PropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.updatesourcetrigger#system-windows-data-updatesourcetrigger-propertychanged) and [LostFocus](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.updatesourcetrigger#system-windows-data-updatesourcetrigger-lostfocus) depending on the bound dependency property as well. The default value for most dependency properties is [PropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.updatesourcetrigger#system-windows-data-updatesourcetrigger-propertychanged), while the [TextBox.Text](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.textbox.text) property has a default value of [LostFocus](https://learn.microsoft.com/en-us/dotnet/api/system.windows.data.updatesourcetrigger#system-windows-data-updatesourcetrigger-lostfocus).

*   [Data binding overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/)
*   [Binding sources overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/binding-sources-overview)
*   [How to create a data binding](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-create-a-simple-binding)
*   [PropertyPath XAML Syntax (.NET Framework)](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/propertypath-xaml-syntax)
