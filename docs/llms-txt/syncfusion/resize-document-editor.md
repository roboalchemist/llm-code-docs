# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/resize-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/resize-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/resize-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/resize-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/resize-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/resize-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/resize-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/resize-document-editor.md

# How to change height and width of Document Editor component

This article explains how to change height and width of Document editor.

## Change height of Document Editor

DocumentEditorContainer initially renders with default height. You can change the height of document editor using `height` property, the value which is in pixel.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true height="590px"></ejs-documenteditorcontainer>

{% endhighlight %}
{% highlight c# tabtitle="Change-height.cs" %}
{% endhighlight %}{% endtabs %}



Similarly, you can use `height` property for DocumentEditor also.

## Change width of Document Editor

DocumentEditorContainer initially renders with default width. You can change the width of document editor using `width` property, the value which is in percent.



{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true width="100%"></ejs-documenteditorcontainer>



{% endhighlight %}
{% highlight c# tabtitle="Change-width.cs" %}
{% endhighlight %}{% endtabs %}



Similarly, you can use `width` property for DocumentEditor also.

## Resize Document Editor

Using `resize` method, you change height and width of Document editor.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>

<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        documenteditor = container.documentEditor;
        setInterval(() => {
          updateDocumentEditorSize();
        }, 100);
        //Adds event listener for browser window resize event.
        window.addEventListener('resize', onWindowResize);
    }
    function onWindowResize() {
        //Resizes the document editor component to fit full browser window automatically whenever the browser resized.
        updateDocumentEditorSize();
    }
    function updateDocumentEditorSize() {
        //Resizes the document editor component to fit full browser window.
        var windowWidth = window.innerWidth;
        var windowHeight = window.innerHeight;
        container.resize(windowWidth, windowHeight);
    }
</script>


{% endhighlight %}
{% highlight c# tabtitle="Resize.cs" %}
{% endhighlight %}{% endtabs %}

