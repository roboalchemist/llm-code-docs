# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/view.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/view.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/view.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/view.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/view.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/view.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/view.md

# View in DocumentEditor

## Web Layout

DocumentEditor allows to change the view to web layout and print using the [`layoutType`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditor.html#Syncfusion_EJ2_DocumentEditor_DocumentEditor_LayoutType) property with the supported [`LayoutType`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.LayoutType.html)


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditor id="container" layoutType="Continuous"></ejs-documenteditor>

{% endhighlight %}
{% highlight c# tabtitle="Web-layout.cs" %}
{% endhighlight %}{% endtabs %}


## Ruler

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


## Navigation Pane

Using the heading navigation pane allows users to swiftly navigate documents by heading, enhancing their ability to move through the document efficiently.

The following example illustrates how to enable heading navigation pane in Document Editor


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditor id="container">
    <ejs-documenteditorcontainerevent (created)="onCreate()" documentEditorSettings="settings" isReadOnly=false></ejs-documenteditorcontainerevent>
</ejs-documenteditor>

<script>
    var container;
    var settings = { showNavigationPane: true };
    function onCreate() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.enableAllModules();
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="heading-navigation.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}

