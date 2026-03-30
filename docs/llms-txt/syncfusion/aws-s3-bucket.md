# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/saving-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/opening-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/saving-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/opening-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/saving-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/opening-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/saving-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/opening-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/saving-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/opening-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/saving-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/opening-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/saving-documents/aws-s3-bucket.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/opening-documents/aws-s3-bucket.md

# Open document from AWS S3

To load a document from AWS S3 in a Document Editor, you can follow the steps below


**Step 1:** Create a Simple Document Editor Sample in ASP.NET Core

Start by following the steps provided in this [link](../../document-editor/getting-started-core) to create a simple Document Editor sample in ASP.NET Core. This will give you a basic setup of the Document Editor component. 



**Step 2:** Modify the `DocumentEditorController.cs` File in the Web Service Project

* Open the `DocumentEditorController.cs` file in your web service project.

* Import the required namespaces at the top of the file:

```csharp
using System.IO;
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
```

* Add the following private fields and constructor parameters to the `DocumentEditorController` class, In the constructor, assign the values from the configuration to the corresponding fields

```csharp
private IConfiguration _configuration;
public readonly string _accessKey;
public readonly string _secretKey;
public readonly string _bucketName;

public DocumentEditorController(IWebHostEnvironment hostingEnvironment, IMemoryCache cache, IConfiguration configuration)
{
  _hostingEnvironment = hostingEnvironment;
  _cache = cache;
  _configuration = configuration;
  _accessKey = _configuration.GetValue<string>("AccessKey");
  _secretKey = _configuration.GetValue<string>("SecretKey");
  _bucketName = _configuration.GetValue<string>("BucketName");
}
```

* Create the `LoadFromS3()` method to load the document from AWS S3.

```csharp

[AcceptVerbs("Post")]
[HttpPost]
[EnableCors("AllowAllOrigins")]
[Route("LoadFromS3")]
//Post action for Loading the documents

public async Task<string> LoadFromS3([FromBody] Dictionary<string, string> onObject)
{
  MemoryStream stream = new MemoryStream();

  if (jsonObject == null && !jsonObject.ContainsKey("documentName"))
  {
     return null;
  }
  RegionEndpoint bucketRegion = RegionEndpoint.USEast1;

  // Configure the AWS SDK with your access credentials and other settings
  var s3Client = new AmazonS3Client(_accessKey, _secretKey, bucketRegion);
      
  string documentName = jsonObject["documentName"];
      
  // Specify the document name or retrieve it from a different source
  var response = await s3Client.GetObjectAsync(_bucketName, documentName);
      
  Stream responseStream = response.ResponseStream;
  responseStream.CopyTo(stream);
  stream.Seek(0, SeekOrigin.Begin);
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
  "AccessKey": "Your Access Key from AWS S3",
  "SecretKey": "Your Secret Key from AWS S3",
  "BucketName": "Your Bucket name from AWS S3"
}
```

N> Replace **Your Access Key from AWS S3**, **Your Secret Key from AWS S3**, and **Your Bucket name from AWS S3** with your actual AWS access key, secret key and bucket name

**Step 3:**  Modify the Index.cshtml File in the Document Editor sample

In the client-side, the document is returned from the web service is opening using `open` method.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="load">Open Document From AWS S3 Bucket</ejs-button>
<ejs-documenteditorcontainer id="container"></ejs-documenteditorcontainer>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");        
        container = documenteditorElement.ej2_instances[0];
        document.getElementById('load').addEventListener('click', function () {
            fetch(
                window.baseurl + 'api/documenteditor/LoadFromS3',
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



N> The **AWSSDK.S3** NuGet package must be installed in your application to use the previous code example.
