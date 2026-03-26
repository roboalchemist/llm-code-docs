# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/customize-color-picker.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/customize-color-picker.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/customize-color-picker.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/customize-color-picker.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/customize-color-picker.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/customize-color-picker.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/customize-color-picker.md

# How to customize the color picker in Document Editor component

Document editor provides an options to customize the color picker using `colorPickerSettings` in Document editor settings. The color picker offers customization options for default appearance, by allowing selection between Picker or Palette mode, for font and border colors."

Similarly, you can use `documentEditorSettings` property for DocumentEditor also.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" documentEditorSettings="settings" enableToolbar=true  height="590px"></ejs-documenteditorcontainer>

<script>
    var settings = { colorPickerSettings: { mode: 'Palette', modeSwitcher: true, showButtons: true } };
</script>
{% endhighlight %}
{% highlight c# tabtitle="customize-color-picker.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


The following table illustrates all the possible properties for the color picker.

| Property | Behavior |
|---|---|
| columns | It is used to render the ColorPicker palette with specified columns. Defaults to 10 |
| disabled | It is used to enable / disable ColorPicker component. If it is disabled the ColorPicker popup wonât open. Defaults to false |
| mode | It is used to render the ColorPicker with the specified mode. Defaults to âPickerâ |
| modeSwitcher | It is used to show / hide the mode switcher button of ColorPicker component. Defaults to true |
| showButtons | It is used to show / hide the control buttons (apply / cancel) of ColorPicker component. Defaults to true |


>**Note**: According to the Word document specifications, it is not possible to modify the **`Predefined Highlight colors`**. This limitation means that the range of highlight colors provided by default cannot be customized or expanded upon by the user to suit individual preferences. Consequently, users must work within the confines of the existing color palette, as no functionality currently exists to modify or personalize these predefined highlighting options.
