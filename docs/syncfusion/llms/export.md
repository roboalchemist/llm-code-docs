# Source: https://docs.syncfusion.com/windowsforms/pivot-chart/export.md

# Source: https://docs.syncfusion.com/windowsforms/syntax-editor/export.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/export.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/export.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/export.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/export.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/export.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/export.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/export.md

# Export in ASP.NET Core in Document Editor Component 

Document editor exports the document into various known file formats in client-side such as Microsoft Word document (.docx), text document (.txt), and its own format called **Syncfusion Document Text (.sfdt)**.

We are providing two types of save APIs  as mentioned below.

|API name|Purpose|Code Snippet for Document Editor|Code Snippet for Document Editor Container|
|--------|---------|----------|----------|
|save(filename,FormatType):void<br>FormatType: Sfdt or Docx or Txt|Creates the document with specified file name and format type. Then, the created file is downloaded in the client browser by default.|documenteditor.save('sample', 'Docx')|container.documentEditor.save('sample', 'Docx')|
|saveAsBlob(FormatType):Blob|Creates the document in specified format type and returns the created document as Blob.<br>This blob can be uploaded to your required server, database, or file path.|documenteditor.saveAsBlob('Docx')|container.documentEditor.saveAsBlob('Docx')|

## Sfdt export

The following example shows how to export documents in document editor as Syncfusion document text (.sfdt).


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}


<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true id="container"></ejs-documenteditor>    
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        document.getElementById('export').addEventListener('click', function () {
            documenteditor.save('sample', 'Sfdt');
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

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditorcontainer id="container" isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true></ejs-documenteditorcontainer> 
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.resize();
        document.getElementById('export').addEventListener('click', function () {
            container.documentEditor.save('sample', 'Sfdt');
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



N>To enable Sfdt export for a document editor instance, set [`enableSfdtExport`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditor.html#Syncfusion_EJ2_DocumentEditor_DocumentEditor_EnableSfdtExport) to true.

## Word export

The following example shows how to export the document as Word document (.docx).


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true enableWordExprot=true id="container"></ejs-documenteditor>    
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");        
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        document.getElementById('export').addEventListener('click', function () {
            documenteditor.save('sample', 'Docx');
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

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditorcontainer id="container" isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true></ejs-documenteditorcontainer> 
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.resize();
        document.getElementById('export').addEventListener('click', function () {
            container.documentEditor.save('sample', 'Docx');
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


N>To enable word export for a document editor instance, set [`enableWordExport`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditor.html#Syncfusion_EJ2_DocumentEditor_DocumentEditor_EnableWordExport) to true.

## Word Template Export 

The following example shows how to export the document as Word Template (.dotx).

>Note: The Syncfusion<sup style="font-size:70%">&reg;</sup> Document Editor component's document pagination (page-by-page display) can't be guaranteed for all the Word documents to match the pagination of Microsoft Word application. For more information about [why the document pagination (page-by-page display) differs from Microsoft Word](../asp-net-core/import#why-the-document-pagination-differs-from-microsoft-word)


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true enableWordExprot=true id="container"></ejs-documenteditor>    
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");        
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        document.getElementById('export').addEventListener('click', function () {
            documenteditor.save('sample', 'Dotx');
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

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditorcontainer id="container" isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true></ejs-documenteditorcontainer> 
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.resize();
        document.getElementById('export').addEventListener('click', function () {
            container.documentEditor.save('sample', 'Dotx');
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


## Text export

The following example shows how to export document as text document (.txt).


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true enableTextExport=true id="container"></ejs-documenteditor>    
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        document.getElementById('export').addEventListener('click', function () {
            documenteditor.save('sample', 'Txt');
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

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditorcontainer id="container" isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true></ejs-documenteditorcontainer> 
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.resize();
        document.getElementById('export').addEventListener('click', function () {
            container.documentEditor.save('sample', 'Txt');
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


N>To enable text export for a document editor instance, set [`enableTextExport`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditor.html#Syncfusion_EJ2_DocumentEditor_DocumentEditor_EnableTextExport) to true.

## Export as blob

Document editor also supports API to store the document into a blob.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor">
    <ejs-documenteditor enableSfdtExport=true enableWordExport=true exnableTextExport=true id="container"></ejs-documenteditor>    
</div>

<script>
    var documenteditor;
    documenteditor = documenteditorElement.ej2_instances[0];
    documenteditor.resize();
    documenteditor.open(sfdt);
    document.getElementById('export').addEventListener('click', function () {
        documenteditor.saveAsBlob('Docx').then(function (exportedDocument) {
            // The blob can be processed further
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

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="export">Export</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditorcontainer id="container" isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true></ejs-documenteditorcontainer> 
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.resize();
        document.getElementById('export').addEventListener('click', function () {
            container.documentEditor.saveAsBlob('Docx');
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



For instance, to export the document as Rich Text Format file, implement an ASP.NET MVC web API controller using DocIO library by passing the DOCX blob.

```csharp
//API controller for the conversion.
[HttpPost]
public HttpResponseMessage ExportAsRtf()
{
    System.Web.HttpPostedFile data = HttpContext.Current.Request.Files[0];
    //Opens document stream
    WordDocument wordDocument = new WordDocument(data.InputStream);
    MemoryStream stream = new MemoryStream();
    //Converts document stream as RTF
    wordDocument.Save(stream, FormatType.Rtf);
    wordDocument.Close();
    stream.Position = 0;
    return new HttpResponseMessage() { Content = new StreamContent(stream) };
}
```

In client-side, you can consume this web service and save the document as Rich Text Format (.rtf) file.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
document.getElementById('export').addEventListener('click', () => {
    documenteditor.saveAsBlob('Docx').then(function (exportedDocument) {
        // The blob can be processed further
        var formData = new FormData();
        formData.append('fileName', 'sample.docx');
        formData.append('data', exportedDocument);
        saveAsRtf(formData);
    });
});

function saveAsRtf(formData) {
    var httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', '/api/DocumentEditor/ExportAsRtf', true);
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState === 4) {
            if (httpRequest.status === 200 || httpRequest.status === 304) {
                if (!(!navigator.msSaveBlob)) {
                    navigator.msSaveBlob(httpRequest.response, 'sample.rtf');
                } else {
                    var downloadLink = document.createElementNS('http://www.w3.org/1999/xhtml', 'a');
                    download('sample.rtf', 'rtf', httpRequest.response, downloadLink, 'download' in downloadLink);
                }
            } else {
                console.error(httpRequest.response);
            }
        }
    }
    httpRequest.responseType = 'blob';
    httpRequest.send(formData);
}

function download(fileName, extension, buffer, downloadLink, hasDownloadAttribute) {
    if (hasDownloadAttribute) {
        downloadLink.download = fileName;
        var dataUrl = window.URL.createObjectURL(buffer);
        downloadLink.href = dataUrl;
        var event = document.createEvent('MouseEvent');
        event.initEvent('click', true, true);
        downloadLink.dispatchEvent(event);
        setTimeout(function () {
            window.URL.revokeObjectURL(dataUrl);
            dataUrl = undefined;
        });
    } else {
        if (extension !== 'docx' && extension !== 'xlsx') {
            var url = window.URL.createObjectURL(buffer);
            var isPopupBlocked = window.open(url, '_blank');
            if (!isPopupBlocked) {
                window.location.href = url;
            }
        }
    }
}
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


## See Also

* [Feature modules](../asp-net-core/feature-module)
* [How to export the document as pdf](../asp-net-core/how-to/export-document-as-pdf).
