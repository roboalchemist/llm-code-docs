# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/link.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/link.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/link.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/link.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/link.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/link.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/link.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/link.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/link.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/link.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/link.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/link.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/link.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/link.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/link.md

# Hyperlink

Document editor supports hyperlink field. You can link a part of the document content to Internet or file location, mail address, or any text within the document.

## Navigate a hyperlink

Document editor triggers ârequestNavigateâ event whenever user clicks Ctrl key or tap a hyperlink within the document. This event provides necessary details about link type, navigation URL, and local URL (if any) as arguments, and allows to easily customize the hyperlink navigation functionality.

### Add the requestNavigate event for DocumentEditor

The following example illustrates how to add requestNavigate event for DocumentEditor.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor enableSelection=true enableSfdtExport=true id="DocumentEditor"></ejs-documenteditor>    
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
        documenteditor.requestNavigate = function (args) {
            if (args.linkType !== 'Bookmark') {
                var link = args.navigationLink;
                if (args.localReference.length > 0) {
                    link += '#' + args.localReference;
                }
                window.open(link);
                args.isHandled = true;
            }
        };
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


### Add the requestNavigate event for DocumentEditorContainer component

The following example illustrates how to add requestNavigate event for DocumentEditorContainer component.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditorcontainer id="container" enableToolbar=true height="590px">
    </ejs-documenteditorcontainer>
</div>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement;
        var container;
        documenteditor = document.getElementById('container');
        container = documenteditor.ej2_instances[0];
        container.documentEditor.requestNavigate = function (args) {
            if (args.linkType !== 'Bookmark') {
                var link = args.navigationLink;
                if (args.localReference.length > 0) {
                    link += '#' + args.localReference;
                }
                window.open(link);
                args.isHandled = true;
            }
        };

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


If the selection is in hyperlink, trigger this event by calling ânavigateHyperlinkâ method of âSelectionâ instance.

```typescript
documenteditor.selection.navigateHyperlink();
```

## Copy link

Document editor copies link text of a hyperlink field to the clipboard if the selection is in hyperlink.

```typescript
documenteditor .selection.copyHyperlink();
```

## Add hyperlink

To create a basic hyperlink in the document, press `ENTER` / `SPACEBAR` / `SHIFT + ENTER` / `TAB` key after typing the address, for instance `http://www.google.com`. Document editor automatically converts this address to a hyperlink field. The text can be considered as a valid URL if it starts with any of the following.

N> `<http://>`<br>
<br/> `<https://>`<br>
<br/> `file:///`<br>
<br/> `www.`<br>
<br/> `mailto:`<br>


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true id="DocumentEditor"></ejs-documenteditor>    
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
        documenteditor.requestNavigate = function (args) {
            if (args.linkType !== 'Bookmark') {
                var link = args.navigationLink;
                if (args.localReference.length > 0) {
                    link += '#' + args.localReference;
                }
                window.open(link);
                args.isHandled = true;
            }
        };
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


## Customize screen tip

You can customize the screen tip text for the hyperlink by using below sample code.

```typescript
documenteditor.insertHyperlink('https://www.google.com', 'Google', '<<Screen tip text>>');
```

Screen tip text can be modified through UI by using the [Hyperlink dialog](../asp-net-core/dialog#hyperlink-dialog)

![Add or modify the screen tip text for hyperlinks in a Word document.](images/screentip.png)

## Remove hyperlink

To remove link from hyperlink in the document, press Backspace key at the end of a hyperlink. By removing the link, it will be converted as plain text. You can use âremoveHyperlinkâ method of âEditorâ instance if the selection is in hyperlink.

```typescript
documenteditor.editor.removeHyperlink();
```

## Hyperlink dialog

Document editor provides dialog support to insert or edit a hyperlink.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true enableHyperlinkDialog=true id="DocumentEditor"></ejs-documenteditor>
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
    });
    //Click the Dialog button, the hyperlink dialog will open
    document.getElementById('dialog').addEventListener('click', function () {
        documenteditor.showDialog('Hyperlink');
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


You can use the following keyboard shortcut to open the hyperlink dialog if the selection is in hyperlink.

| Key Combination | Description |
|-----------------|-------------|
|Ctrl + K | Open hyperlink dialog that allows you to create or edit hyperlink|

## See Also

* [Feature modules](../asp-net-core/feature-module)
* [Hyperlink dialog](../asp-net-core/dialog#hyperlink-dialog)
