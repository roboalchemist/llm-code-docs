# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/customize-font-family-drop-down.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/customize-font-family-drop-down.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/customize-font-family-drop-down.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/customize-font-family-drop-down.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/customize-font-family-drop-down.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/customize-font-family-drop-down.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/customize-font-family-drop-down.md

# How to customize the font family dropdown in Document Editor

Document editor provides options to customize the font family drop down list values using `fontFamilies` in Document editor settings. Fonts which are added in `fontFamilies` of `documentEditorSettings` will be displayed on font drop down list of text properties pane and font dialog.

Similarly, you can use `documentEditorSettings` property for DocumentEditor also.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" documentEditorSettings="settings" enableToolbar=true  height="590px"></ejs-documenteditorcontainer>

<script>
    var settings = { fontFamilies: ['Algerian', 'Arial', 'Calibri', 'Cambria'] };
</script>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


![Font](../images/font-family.png)