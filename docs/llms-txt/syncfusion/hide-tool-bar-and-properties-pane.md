# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/hide-tool-bar-and-properties-pane.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/hide-tool-bar-and-properties-pane.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/hide-tool-bar-and-properties-pane.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/hide-tool-bar-and-properties-pane.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/hide-tool-bar-and-properties-pane.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/hide-tool-bar-and-properties-pane.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/hide-tool-bar-and-properties-pane.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/hide-tool-bar-and-properties-pane.md

# How to hide the default tool bar and properties pane in Document Editor component

**Document editor container** provides the main document view area along with the built-in toolbar and properties pane.

**Document editor** provides just the main document view area. Here, the user can compose, view, and edit the Word documents. You may prefer to use this component when you want to design your own UI options for your application.

## Hide the properties pane

By default, Document editor container has built-in properties pane which contains options for formatting text, table, image and header and footer. You can use [`showPropertiesPane`] API in `DocumentEditorContainer` to hide the properties pane.

The following example code illustrates how to hide the properties pane.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true showPropertiesPane=false height="590px"></ejs-documenteditorcontainer>
</div>


{% endhighlight %}
{% highlight c# tabtitle="Hide-the-default-propertiespane.cs" %}
{% endhighlight %}{% endtabs %}


N> Positioning and customizing the properties pane in Document editor container is not possible. Instead, you can hide the exiting properties pane and create your own pane using public API's.

## Hide the toolbar

You can use [`enableToolbar`] API in `DocumentEditorContainer` to hide the existing toolbar.

The following example code illustrates how to hide the existing toolbar.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=false height="590px"></ejs-documenteditorcontainer>
</div>

{% endhighlight %}
{% highlight c# tabtitle="Hide-the-default-toolbar.cs" %}
{% endhighlight %}{% endtabs %}


## See Also

* [How to customize the toolbar](./customize-tool-bar)