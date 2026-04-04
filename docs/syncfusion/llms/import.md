# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/import.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/import.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/import.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/import.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/import.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/import.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/import.md

# Import in Document Editor Component

In Document Editor, the documents are stored in its own format called **Syncfusion Document Text (SFDT)**.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditor id="container"></ejs-documenteditor>

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        var sfdt = {
            "sections": [
                {
                    "blocks": [
                        {
                            "inlines": [
                                {
                                    "characterFormat": {
                                        "bold": true,
                                        "italic": true
                                    },
                                    "text": "Hello World"
                                }
                            ]
                        }
                    ],
                    "headersFooters": {
                    }
                }
            ]
        };

        documenteditor.open(JSON.stringify(sfdt));
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


## Import document from local machine


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<input type="file" id="file_upload" accept=".sfdt" style="position:fixed; left:-100em" /> 
<ejs-button id="import">Import</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");        
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        document.getElementById("import").addEventListener("click", function () {
            document.getElementById('file_upload').click();
        });

        document.getElementById('file_upload').addEventListener("change", function (e) {
            if (e.target.files[0]) {
                var file = e.target.files[0];
                if (file.name.substr(file.name.lastIndexOf('.')) === '.sfdt') {
                    var fileReader = new FileReader();
                    fileReader.onload = function (e) {
                        var contents = e.target.result;
                        documenteditor.open(contents);
                    };
                    fileReader.readAsText(file);
                    documenteditor.documentName = file.name.substr(0, file.name.lastIndexOf('.'));
                }
            }
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



## Convert word documents into SFDT

You can convert word documents into SFDT format using the .NET Standard library [`Syncfusion.EJ2.WordEditor.AspNet.Core`](<https://www.nuget.org/packages/Syncfusion.EJ2.WordEditor.AspNet.Core/>) by the web API service implementation. This library helps to convert word documents (.dotx,.docx,.docm,.dot,.doc), rich text format documents (.rtf), and text documents (.txt) into SFDT format.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<input type="file" id="file_upload" accept=".sfdt" style="position:fixed; left:-100em" /> 
<ejs-button id="import">Import</ejs-button>
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");        
        documenteditor = documenteditorElement.ej2_instances[0];
        documenteditor.resize();
        document.getElementById('file_upload').setAttribute('accept', '.dotx,.docx,.docm,.dot,.doc,.rtf,.txt,.xml,.sfdt');

        document.getElementById('file_upload').addEventListener("change", function (e) {
            if (e.target.files[0]) {
                var file = e.target.files[0];
                if (file.name.substr(file.name.lastIndexOf('.')) !== '.sfdt') {
                    loadFile(file);
                }
            }
        });

        function loadFile(file) {
            var ajax = new XMLHttpRequest();
            ajax.open('POST', 'https://localhost:4000/api/documenteditor/Import', true);
            ajax.onreadystatechange = function () {
                if (ajax.readyState === 4) {
                    if (ajax.status === 200 || ajax.status === 304) {
                        // open SFDT text in document editor
                        documenteditor.open(ajax.responseText);
                    }
                }
            }
            var formData = new FormData();
            formData.append('files', file);
            ajax.send(formData);
        }
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


Hereâs how to handle the server-side action for converting word document into SFDT.

```csharp
[AcceptVerbs("Post")]
public string Import(IFormCollection data)
{
    if (data.Files.Count == 0)
        return null;
    Stream stream = new MemoryStream();
    IFormFile file = data.Files[0];
    int index = file.FileName.LastIndexOf('.');
    string type = index > -1 && index < file.FileName.Length - 1 ?
        file.FileName.Substring(index) : ".docx";
    file.CopyTo(stream);
    stream.Position = 0;

    WordDocument document = WordDocument.Load(stream, GetFormatType(type.ToLower()));
    string sfdt = Newtonsoft.Json.JsonConvert.SerializeObject(document);
    document.Dispose();
    return sfdt;
}

internal static FormatType GetFormatType(string format)
{
    if (string.IsNullOrEmpty(format))
        throw new NotSupportedException("EJ2 DocumentEditor does not support this file format.");
    switch (format.ToLower()) {
        case ".dotx":
        case ".docx":
        case ".docm":
        case ".dotm":
            return FormatType.Docx;
        case ".dot":
        case ".doc":
            return FormatType.Doc;
        case ".rtf":
            return FormatType.Rtf;
        case ".txt":
            return FormatType.Txt;
        case ".xml":
            return FormatType.WordML;
        default:
            throw new NotSupportedException("EJ2 DocumentEditor does not support this file format.");
    }
}
```

## See Also

* [Feature modules](../asp-net-core/feature-module)
