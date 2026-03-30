# Source: https://docs.syncfusion.com/flutter/range-selector/basic-features.md

# Source: https://docs.syncfusion.com/flutter/range-slider/basic-features.md

# Source: https://docs.syncfusion.com/flutter/slider/basic-features.md

# Source: https://docs.syncfusion.com/winui/slider/basic-features.md

# Source: https://docs.syncfusion.com/winui/rangeslider/basic-features.md

# Source: https://docs.syncfusion.com/maui/numericentry/basic-features.md

# Source: https://docs.syncfusion.com/maui/masked-entry/basic-features.md

# Source: https://docs.syncfusion.com/maui/autocomplete/basic-features.md

# Basic Features with .NET MAUI Autocomplete (SfAutocomplete)

## Selection

The [.NET MAUI Autocomplete](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.Inputs.SfAutocomplete.html) allows the user to select an item from the drop-down list by clicking the `Enter` key or losing focus from the text box.

{% tabs %}
{% highlight xaml %}

<editors:SfAutocomplete x:Name="autocomplete"
                        DisplayMemberPath = "Name"
                        TextMemberPath = "Name"
                        ItemsSource="{Binding SocialMedias}" />

{% endhighlight %}
{% highlight C# %}

SfAutocomplete autocomplete = new SfAutocomplete()
{
    DisplayMemberPath = "Name",
    TextMemberPath = "Name",
    ItemsSource = socialMediaViewModel.SocialMedias,
};

{% endhighlight %}
{% endtabs %}

The following image illustrates the output:

![.NET MAUI Autocomplete with single selection mode](Images/GettingStarted/SingleSelection.gif)

## Text

The [Text](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.Inputs.DropDownControls.DropDownListBase.html#Syncfusion_Maui_Inputs_DropDownControls_DropDownListBase_Text) property is used to get the user-submitted text in the [SfAutocomplete](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.Inputs.SfAutocomplete.html). The default value of the `Text` property is `string.Empty`.

## Automation ID

The [SfAutocomplete](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.Inputs.SfAutocomplete.html) control provides `AutomationId` support specifically for the `editable entry` and the `clear button`, enabling UI automation frameworks to reliably target these two elements. Each elementâs AutomationId is derived from the controlâs `AutomationId` to ensure uniqueness. 

For example, if the SfAutocompleteâs `AutomationId` is set to âEmployee Autocomplete,â the editable entry can be targeted as âEmployee Autocomplete Entryâ and the clear button as âEmployee Autocomplete Clear Button.â This focused support improves accessibility and automated UI testing by providing stable, predictable identifiers for the primary interactive elements

The following screenshot illustrates the AutomationIds of inner elements.

![.NET MAUI Autocomplete AutomationId Image demonstration](Images/GettingStarted/AutoComplete_AutomationID.png)