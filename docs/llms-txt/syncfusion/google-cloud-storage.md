# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/saving-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/opening-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/saving-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/opening-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/saving-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/opening-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/saving-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/opening-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/saving-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/opening-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/saving-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/opening-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/saving-documents/google-cloud-storage.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/opening-documents/google-cloud-storage.md

# Open document from Google Cloud Storage

To load a document from Google Cloud Storage in a Document editor, you can follow the steps below


**Step 1:** Create a Simple Document Editor Sample in ASP.NET Core

Start by following the steps provided in this [link](../../document-editor/getting-started-core) to create a simple Document Editor sample in ASP.NET Core. This will give you a basic setup of the Document Editor component. 


**Step 2:** Modify the `DocumentEditorController.cs` File in the Web Service Project

* Open the `DocumentEditorController.cs` file in your web service project.

* Import the required namespaces at the top of the file:

```csharp
using System.IO;
using Google.Cloud.Storage.V1;
using Google.Apis.Auth.OAuth2;
```

* Add the following private fields and constructor parameters to the `DocumentEditorController` class, In the constructor, assign the values from the configuration to the corresponding fields

```csharp
// Private readonly object _storageClient
private readonly StorageClient _storageClient;

private IConfiguration _configuration;

public readonly string _bucketName;

public DocumentEditorController(IWebHostEnvironment hostingEnvironment, IMemoryCache cache, IConfiguration configuration)
{
  _hostingEnvironment = hostingEnvironment;
  _cache = cache;

  // The key file is used to authenticate with Google Cloud Storage.
  string keyFilePath = "path/to/service-account-key.json";

  // Load the service account credentials from the key file.
  var credentials = GoogleCredential.FromFile(keyFilePath);

  // Create a storage client with Application Default Credentials
  _storageClient = StorageClient.Create(credentials);

   _configuration = configuration;

   _bucketName = _configuration.GetValue<string>("BucketName");
}
```

* Create the `LoadFromGoogleCloud()` method to load the document from Google Cloud Storage.

```csharp
[AcceptVerbs("Post")]
[HttpPost]
[EnableCors("AllowAllOrigins")]
[Route("LoadFromGoogleCloud")]
//Post action for Loading the documents

public async Task<string> LoadFromGoogleCloud([FromBody] Dictionary<string, string> jsonObject)
{
    if (jsonObject == null && !jsonObject.ContainsKey("documentName"))
    {
      return null
    }
    MemoryStream stream = new MemoryStream();

    string bucketName = _bucketName;
    string objectName = jsonObject["document"];
    _storageClient.DownloadObject(bucketName, objectName, stream);
    stream.Position = 0;

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
  "BucketName": "Your Bucket name from Google Cloud Storage"
}
```

N> Replace **Your Bucket name from Google Cloud Storage** with the actual name of your Google Cloud Storage bucket

N> Replace **path/to/service-account-key.json** with the actual file path to your service account key JSON file. Make sure to provide the correct path and filename.

**Step 3:**  Modify the Index.cshtml File in the Document Editor sample

In the client-side, the document is returned from the web service is opening using `open` method.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="load">Open Document From Google cloud storage</ejs-button>
<ejs-documenteditorcontainer id="container"></ejs-documenteditorcontainer>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");        
        container = documenteditorElement.ej2_instances[0];
        document.getElementById('load').addEventListener('click', function () {
            fetch(
                window.baseurl + 'api/documenteditor/LoadFromGoogleCloud',
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


N> The **Google.Cloud.Storage.V1** NuGet package must be installed in your application to use the previous code example.
