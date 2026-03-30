# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/disable-header-and-footer-edit-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/disable-header-and-footer-edit-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/disable-header-and-footer-edit-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/disable-header-and-footer-edit-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/disable-header-and-footer-edit-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/disable-header-and-footer-edit-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/disable-header-and-footer-edit-in-document-editor.md

# How to disable header and footer edit in  Document Editor component

## Disable header and footer edit in DocumentEditorContainer instance

You can use [`restrictEditing`] property to disable header and footer editing based on selection context type.

RestrictEditing allows you to restrict the document modification and makes the Document read only mode. So, by using this property, and if selection inside header or footer, you can set this property as true.

The following example code illustrates how to header and footer edit in `DocumentEditorContainer` instance.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" .selectionChange="onSelectionChanged" height="590px"></ejs-documenteditorcontainer>

<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
    }
    function onSelectionChanged() {
        // Check whether selection is in header
        if (container.documentEditor.selection.contextType.indexOf('Header') > -1 ||
        // Check whether selection is in Footer
          container.documentEditor.selection.contextType.indexOf('Footer') > -1) {
          // Change the document to read only mode
          container.restrictEditing = true;
        } else {
          // Change the document to editable mode
          container.restrictEditing = false;
        }
    }
</script>


{% endhighlight %}
{% highlight c# tabtitle="document-editor.cs" %}
{% endhighlight %}{% endtabs %}

Otherwise, you can disable clicking inside Header or Footer by using [`closeHeaderFooter`] API in selection module.

The following example code illustrates how to close header and footer when selection is inside header or footer in `DocumentEditorContainer` instance.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" selectionChange="onSelectionChanged" height="590px"></ejs-documenteditorcontainer>

<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
    }
    function onSelectionChanged() {
        // Check whether selection is in header
        if (container.documentEditor.selection.contextType.indexOf('Header') > -1 ||
        // Check whether selection is in Footer
          container.documentEditor.selection.contextType.indexOf('Footer') > -1) {
          // Close header Footer
          container.documentEditor.selection.closeHeaderFooter();
        }
    }
</script>


{% endhighlight %}
{% highlight c# tabtitle="document-editor.cs" %}
{% endhighlight %}{% endtabs %}


## Disable header and footer edit in DocumentEditor instance

Like restrictEditing, you can use [`isReadOnly`] property in Document editor to disable header and footer edit.

The following example code illustrates how to header and footer edit in `DocumentEditor` instance.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditor isReadOnly=false id="container" selectionChange="onSelectionChanged"></ejs-documenteditor>

<script>
    var documentEditor;
    document.addEventListener('DOMContentLoaded', function () {
        documentEditor = document.getElementById("container").ej2_instances[0];
        documentEditor.enableAllModules();
    });
    function onSelectionChanged() {
        // Check whether selection is in header
        if (documentEditor.selection.contextType.indexOf('Header') > -1 ||
          // Check whether selection is in Footer
          documentEditor.selection.contextType.indexOf('Footer') > -1) {
          // Change the document to read only mode
          documentEditor.isReadOnly = true;
        } else {
          // Change the document to editable mode
          documentEditor.isReadOnly = false;
        }
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="document-editor.cs" %}
{% endhighlight %}{% endtabs %}

