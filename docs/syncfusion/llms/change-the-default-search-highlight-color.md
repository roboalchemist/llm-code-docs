# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/change-the-default-search-highlight-color.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/change-the-default-search-highlight-color.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/change-the-default-search-highlight-color.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/change-the-default-search-highlight-color.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/change-the-default-search-highlight-color.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/change-the-default-search-highlight-color.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/change-the-default-search-highlight-color.md

# How to change the default search highlight color in Document Editor

Document editor provides an options to change the default search highlight color using [`searchHighlightColor`] in Document editor settings. The highlight color which is given in [`documentEditorSettings`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditorContainer.html#Syncfusion_EJ2_DocumentEditor_DocumentEditorContainer_DocumentEditorSettings) will be highlighted on the searched text. By default, search highlight color is `yellow`.

Similarly, you can use [`documentEditorSettings`] property for DocumentEditor also.

The following example code illustrates how to change the default search highlight color.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" documentEditorSettings="settings" enableToolbar=true  height="590px"></ejs-documenteditorcontainer>

<script>
    var settings = { searchHighlightColor: 'Grey' };
</script>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


Output will be like below:

![How to change the default search highlight color](../images/search-color.png)