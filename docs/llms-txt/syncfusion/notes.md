# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/notes.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/notes.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/notes.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/notes.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/notes.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/notes.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/notes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/notes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/notes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/notes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/notes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/notes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/notes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/notes.md

# Insert footnote endnote

DocumentEditorContainer component provides support for inserting footnotes and endnotes through the in-built toolbar.

![Insert footnote endnote](images/note-toolbar.jpg)

The footnotes and endnotes are both ways of adding extra bits of information to your writing outside of the main text. You can use footnotes and endnotes to add side comments to your work or to place other publications like books, articles, or websites.

## Insert footnotes

Document editor exposes an API to insert footnotes at cursor position programmatically or can be inserted to the end of selected text.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="insertFootnote">insert Footnote</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true id="DocumentEditor"></ejs-documenteditor>
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
    });    
    document.getElementById('insertFootnote').addEventListener('click', function () {
        documenteditor.editor.insertFootnote();
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


## Insert endnotes

Document editor exposes an API to insert endnotes at cursor position programmatically or can be inserted to the end of selected text.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="InsertEndnote">Insert Endnote</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true id="DocumentEditor"></ejs-documenteditor>
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
    });    
    document.getElementById('InsertEndnote').addEventListener('click', function () {
        documenteditor.editor.insertEndnote();
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


## Update or edit footnotes and endnotes

You can update or edit the footnotes and endnotes using the built-in context menu shown up by right-clicking it. The footnote endnote dialog box popup and you can customize the number format and start at.

![Update or edit footnotes and endnotes](images/notes-option.jpg)
