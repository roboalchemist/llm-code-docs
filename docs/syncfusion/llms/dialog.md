# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/dialog.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/dialog.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/dialog.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/dialog.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/dialog.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/dialog.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/dialog.md

# Dialog in ASP.NET Core in Document Editor Component

Document Editor provides dialog support to major operations such as insert or edit hyperlink, formatting text, paragraph, style, list and table properties.

## Font Dialog

Font dialog allows to modify all text properties for selected contents at once such as bold, italic, underline, font size, font color, strikethrough, subscript and superscript.

N>To enable font dialog for a document editor instance, set âenableFontDialogâ to true.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableFontDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    var containerPanel;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open Font Dialog
            documenteditor.showDialog('Font');
        });
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


## Paragraph dialog

This dialog allows modifying the paragraph formatting for selection at once such as text alignment, indentation, and spacing.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableParagraphDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    var containerPanel;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open Paragraph Dialog
            documenteditor.showDialog('Paragraph');
        });
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


## Table dialog

This dialog allows creating and inserting a table at cursor position by specifying the required number of rows and columns.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableTableDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>
<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor =  document.getElementById("container").ej2_instances[0];        
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open Table Dialog
            documenteditor.showDialog('Table');
        });
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


## Bookmark dialog

This dialog allows to perform the following operations:

* View all bookmarks.
* Navigate to a bookmark.
* Create a bookmark at current selection.
* Delete an existing bookmark.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableBookmarkDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open Bookmark Dialog
            documenteditor.showDialog('Bookmark');
        });
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


## Hyperlink dialog

This dialog allows editing or inserting a hyperlink at cursor position.


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


## Table of contents dialog

This dialog allows creating and inserting table of contents at cursor position. If the table of contents already exists at cursor position, you can customize its properties.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableTableOfContentsDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor = document.getElementById("container").ej2_instances[0];        
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open TableOfContents Dialog
            documenteditor.showDialog('TableOfContents');
        });
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


## Styles Dialog

This dialog allows managing the styles in a document. It will display all the styles in the document with options to modify the properties of the existing style or create new style with the help of âStyle dialogâ.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableStyleDialog=true enableStylesDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>
<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor =  document.getElementById("container").ej2_instances[0];        
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open Styles Dialog
            documenteditor.showDialog('Styles');
        });
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


## Style dialog

You can directly use this dialog for modifying any existing style or add new style by providing the style name.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableStyleDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>
<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor =  document.getElementById("container").ej2_instances[0];        
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open Style Dialog
            documenteditor.showDialog('Style');
        });
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


## List dialog

This dialog allows creating a new list or modifying existing lists in the document.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableListDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>
<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor =  document.getElementById("container").ej2_instances[0];        
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open List Dialog
            documenteditor.showDialog('List');
        });
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


## Borders and shading dialog

This dialog allows customizing the border style, border width, and background color of the table or selected cells.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableBordersAndShadingDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open BordersAndShading Dialog
            documenteditor.showDialog('BordersAndShading');
        });
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


## Table options dialog

This dialog allows customizing the default cell margins and spacing between each cells of the selected table.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableTableOptionsDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open TableOptions Dialog
            documenteditor.showDialog('TableOptions');
        });
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


## Table properties dialog

This dialog allows customizing the table, row, and cell properties of the selected table.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableTablePropertiesDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open TableProperties Dialog
            documenteditor.showDialog('TableProperties');
        });
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


## Page setup dialog

This dialog allows customizing margins, size, and layout options for pages of the section.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="dialog">Dialog</ejs-button>
<div id="documenteditor">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enablePageSetupDialog=true enableSfdtExport=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        var button = document.getElementById('dialog');
        button.addEventListener('click', function () {
            // To open PageSetup Dialog
            documenteditor.showDialog('PageSetup');
        });
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


## See Also

* [Feature module](../asp-net-core/feature-module)
