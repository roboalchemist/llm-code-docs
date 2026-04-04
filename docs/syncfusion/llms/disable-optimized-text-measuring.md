# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/disable-optimized-text-measuring.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/disable-optimized-text-measuring.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/disable-optimized-text-measuring.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/disable-optimized-text-measuring.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/disable-optimized-text-measuring.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/disable-optimized-text-measuring.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/disable-optimized-text-measuring.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/disable-optimized-text-measuring.md

# How to disable optimized text measuring in Document Editor component

Starting from v19.3.0.x, the accuracy of text size measurements in Document editor is improved such as to match Microsoft Word pagination for most Word documents. This improvement is included as default behavior along with an optional API `enableOptimizedTextMeasuring` in Document editor settings.

If you want the Document editor component to retain the document pagination (display page-by-page) behavior like v19.2.0.x and older versions. Then, you can disable this optimized text measuring improvement, by setting `false` to `enableOptimizedTextMeasuring` property of Document Editor component.

## Disable optimized text measuring in `DocumentEditorContainer` instance

The following example code illustrates how to disable optimized text measuring improvement in `DocumentEditorContainer` instance.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div>
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enablePageSetupDialog=true enableSfdtExport=true id="container" documentEditorSettings="settings"></ejs-documenteditor>
</div>
<script>
    var settings = { enableOptimizedTextMeasuring: false };
</script>
{% endhighlight %}
{% highlight c# tabtitle="Optimized-text.cs" %}
{% endhighlight %}{% endtabs %}



## Disable optimized text measuring in `DocumentEditor` instance

The following example code illustrates how to disable optimized text measuring improvement in `DocumentEditor` instance.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" documentEditorSettings="settings" enableToolbar=true  height="590px"></ejs-documenteditorcontainer>

<script>
    var settings = { enableOptimizedTextMeasuring: false };
</script>
{% endhighlight %}
{% highlight c# tabtitle="Optimized-text.cs" %}
{% endhighlight %}{% endtabs %}

