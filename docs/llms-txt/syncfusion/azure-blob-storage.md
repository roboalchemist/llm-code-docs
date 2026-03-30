# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/saving-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/opening-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/saving-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/opening-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/saving-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/opening-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/saving-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/opening-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/saving-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/opening-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/saving-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/opening-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/saving-documents/azure-blob-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/opening-documents/azure-blob-storage.md

# Open document from Azure Blob Storage

To load document from Azure Blob Storage in a Document Editor, you can follow the steps below


**Step 1:** Create a Simple Document Editor Sample in ASP.NET Core

Start by following the steps provided in this [link](../../document-editor/getting-started-core) to create a simple Document Editor sample in ASP.NET Core. This will give you a basic setup of the Document Editor component. 


**Step 2:** Modify the `DocumentEditorController.cs` File in the Web Service Project

* Open the `DocumentEditorController.cs` file in your web service project.

* Import the required namespaces at the top of the file:

```csharp
using System.IO;
using Azure.Storage.Blobs;
using Azure.Storage.Blobs.Specialized;
```

* Add the following private fields and constructor parameters to the `DocumentEditorController` class, In the constructor, assign the values from the configuration to the corresponding fields


```csharp
private readonly string _storageConnectionString;
private readonly string _storageContainerName;
private readonly ILogger<DocumentEditorController> _logger;

public DocumentEditorController(IConfiguration configuration, ILogger<DocumentEditorController> logger)
{
  _storageConnectionString = configuration.GetValue<string>("connectionString");
  _storageContainerName = configuration.GetValue<string>("containerName");
  _logger = logger;
}
```

* Modify the `LoadFromAzure()` method to load the document from  Azure Blob Storage

```csharp

[HttpPost("LoadFromAzure")]
[Microsoft.AspNetCore.Cors.EnableCors("MyPolicy")]
[Route("[controller]/LoadFromAzure")]
//Post action for Loading the PDF documentsÂ 
Â  
public IActionResult LoadFromAzure([FromBody] Dictionary<string, string> jsonObject)
{
  MemoryStream stream = new MemoryStream();

  if (jsonObject == null && !jsonObject.ContainsKey("documentName"))
  {
     return null
  }
  BlobServiceClient blobServiceClient = new BlobServiceClient(_storageConnectionString);
  string fileName = jsonObject["documentName"];
  BlobContainerClient containerClient = blobServiceClient.GetBlobContainerClient(_storageContainerName);
  BlockBlobClient blockBlobClient = containerClient.GetBlockBlobClient(fileName);
  blockBlobClient.DownloadTo(stream);
  WordDocument document = WordDocument.Load(stream, FormatType.Docx);
  string json = Newtonsoft.Json.JsonConvert.SerializeObject(document);
  document.Dispose();
  stream.Close();
  return json;
}
```

* Open the `appsettings.json` file in your web service project, Add the following lines below the existing `"AllowedHosts"` configuration

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "connectionString": "*Your Connection string from Azure*",
  "containerName": "*Your container name in Azure*"
}
```

N> Replace **Your Connection string from Azure** with the actual connection string for your Azure Blob Storage account and **Your container name in Azure** with the actual container name 

**Step 3:**  Modify the Index.cshtml File in the Document Editor sample

In the client-side, the document is returned from the web service is opening using `open` method.


{% tabs %}
{% highlight razor tabtitle="CSHTML" %}
@Html.EJS().Button("load").Content("Open Document From Azure Blob Storage").Render()
@Html.EJS().DocumentEditorContainer("container").EnableToolbar(true).Render()

<script>
    var container;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");        
        container = documenteditorElement.ej2_instances[0];
        document.getElementById('load').addEventListener('click', function () {
            fetch(
                window.baseurl + 'api/documenteditor/LoadFromAzure',
                {
                    method: 'Post',
                    headers: { 'Content-Type': 'application/json;charset=UTF-8' },
                    body: JSON.stringify({ documentName: 'Getting Started.docx' })
                }
            )
                .then(response => {
                    if (response.status === 200 || response.status === 304) {
                        return response.json(); // Return the Promise
                    } else {
                        throw new Error('Error loading data');
                    }
                })
                .then(json => {
                    container.documentEditor.open(JSON.stringify(json));
                })
                .catch(error => {
                    console.error(error);
                });
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

N> The **Azure.Storage.Blobs** NuGet package must be installed in your application to use the previous code example.
