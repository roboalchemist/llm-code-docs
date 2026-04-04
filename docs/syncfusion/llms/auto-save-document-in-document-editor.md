# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/auto-save-document-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/auto-save-document-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/auto-save-document-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/auto-save-document-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/auto-save-document-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/auto-save-document-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/auto-save-document-in-document-editor.md

# How to auto save the document of Document Editor component into AWS S3

This article explains how to auto save the document in AWS S3. You can automatically save the edited content in regular intervals of time. It helps to reduce the risk of data loss by saving an open document automatically at customized intervals.

* In the client-side, using content change event, the edited content can be automatically saved in regular intervals of time. Based on `contentChanged` boolean, the document send as DOCX format to server-side using `saveAsBlob` method.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" enableToolbar=true  height="590px"></ejs-documenteditorcontainer>

<script>
    var container;
    var containerPanel;
    var contentChanged =false;
    document.addEventListener('DOMContentLoaded', function () {
        var documenteditorElement = document.getElementById("container");
    container = documenteditorElement.ej2_instances[0];
    container.contentChange=function(){
        contentChanged = true;
    }
    });
    function onCreate() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        setInterval(() => {
            if (contentChanged) {
                //You can save the document as below
                container.documentEditor.saveAsBlob('Docx').then((blob) => {
                    console.log('Saved sucessfully');
                    let exportedDocument = blob;
                    //Now, save the document where ever you want.
                    let formData = new FormData();
                    formData.append('fileName', 'sample.docx');
                    formData.append('data', exportedDocument);
                    /* tslint:disable */
                    var req = new XMLHttpRequest();
                    // Replace your running Url here
                    req.open(
                        'POST',
                        'http://localhost:62869/api/documenteditor/SaveToS3',
                        true
                    );
                    req.onreadystatechange = () => {
                        if (req.readyState === 4) {
                            if (req.status === 200 || req.status === 304) {
                                console.log('Saved sucessfully');
                            }
                        }
                    };
                    req.send(formData);
                });
                contentChanged = false;
            }
        }, 1000);
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


* Configure the access key and secret key in `web.config` file and register profile in `startup.cs`.

In `web.config`, add key like below format:

```c#
<appSettings>
    <add key="AWSProfileName" value="sync_development" />
    <add key="AWSAccessKey" value="" />
    <add key="AWSSecretKey" value="" />
</appSettings>
```

In `startup.cs`, register profile in below format:

```c#
Amazon.Util.ProfileManager.RegisterProfile("sync_development","", "");
```

* In server-side, Receives the stream content from client-side and process it to save the document in aws s3. Add Web API in controller file like below to save the document in aws s3.

```c#
[AcceptVerbs("Post")]
[HttpPost]
[EnableCors("AllowAllOrigins")]
[Route("SaveToS3")]
public string SaveToS3()
{
    IFormFile file = HttpContext.Request.Form.Files[0];
    Stream stream = new MemoryStream();
    file.CopyTo(stream);
    UploadFileStreamToS3(stream, "documenteditor", "", "GettingStarted.docx");
    stream.Close();
    return "Sucess";
}

public bool UploadFileStreamToS3(System.IO.Stream localFilePath, string bucketName, string subDirectoryInBucket, string fileNameInS3)
{
    AWSCredentials credentials = new StoredProfileAWSCredentials("sync_development");
    IAmazonS3 client = new AmazonS3Client(credentials, Amazon.RegionEndpoint.USEast1);
    TransferUtility utility = new TransferUtility(client);
    TransferUtilityUploadRequest request = new TransferUtilityUploadRequest();

    if (subDirectoryInBucket == "" || subDirectoryInBucket == null)
    {
        request.BucketName = bucketName; //no subdirectory just bucket name  
    }
    else
    {   // subdirectory and bucket name  
        request.BucketName = bucketName + @"/" + subDirectoryInBucket;
    }
    request.Key = fileNameInS3; //file name up in S3  
    request.InputStream = localFilePath;
    utility.Upload(request); //commensing the transfer  

    return true; //indicate that the file was sent  
}
```

Get the complete working sample in this [`link`](https://github.com/SyncfusionExamples/Auto-Save-documents-in-Word-Processor).
