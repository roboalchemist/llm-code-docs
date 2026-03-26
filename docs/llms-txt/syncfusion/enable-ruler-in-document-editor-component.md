# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/enable-ruler-in-document-editor-component.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/enable-ruler-in-document-editor-component.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/enable-ruler-in-document-editor-component.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/enable-ruler-in-document-editor-component.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/enable-ruler-in-document-editor-component.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/enable-ruler-in-document-editor-component.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/enable-ruler-in-document-editor-component.md

# How to enable ruler in ASP.NET Core Document Editor component

Using ruler we can refer to setting specific margins, tab stops, or indentations within a document to ensure consistent formatting in Document Editor.

The following example illustrates how to enable ruler in Document Editor


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="container_ruler_button" content="Show/hide ruler" onclick="onClick()"></ejs-button>
<ejs-documenteditor id="container">
    <ejs-documenteditorcontainerevent (created)="onCreate()" documentEditorSettings="settings" isReadOnly=false></ejs-documenteditorcontainerevent>
</ejs-documenteditor>

<script>
    var container;
    var settings = { showRuler: true };
    function onCreate() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.enableAllModules();
    }
    function onClick() {
        container.documentEditorSettings.showRuler = !container.documentEditorSettings.showRuler;
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}



## How to enable ruler in Document Editor Container component

Using ruler we can refer to setting specific margins, tab stops, or indentations within a document to ensure consistent formatting in Document Editor Container.

The following example illustrates how to enable ruler in Document Editor Container.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="container_ruler_button" content="Show/hide ruler" onclick="onClick()"></ejs-button>
<ejs-documenteditorcontainer id="container" (created)="onCreate()" documentEditorSettings="settings"></ejs-documenteditorcontainer>

<script>
    var container;
    var settings = { showRuler: true };
    function onCreate() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
    }
    function onClick() {
        container.documentEditorSettings.showRuler = !container.documentEditorSettings.showRuler;
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}

