# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/auto-save-document.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/auto-save-document.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/auto-save-document.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/auto-save-document.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/auto-save-document.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/auto-save-document.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/auto-save-document.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/auto-save-document.md

# Auto save document in Document editor control

In this article, we are going to see how to auto save the document to server. You can automatically save the edited content in regular intervals of time. It helps reduce the risk of data loss by saving an open document automatically at customized intervals.

The following example illustrates how to auto save the document in server.

* In the client-side, using content change event, we can automatically save the edited content in regular intervals of time. Based on `contentChanged` boolean, the document send as DOCX format to server-side using [`saveAsBlob`] method.


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
                        'http://localhost:62869/api/documenteditor/AutoSave',
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



* In server-side, Receives the stream content from client-side and process it to save the document in Server or Database from the received stream. Add Web API in controller file like below to save the document.

```c#
[AcceptVerbs("Post")]
[HttpPost]
[EnableCors("AllowAllOrigins")]
[Route("AutoSave")]
public string AutoSave()
{
    IFormFile file = HttpContext.Request.Form.Files[0];
    Stream stream = new MemoryStream();    
    file.CopyTo(stream);
    //Save the stream to database or server as per the requirement.
    stream.Close();
    return "Sucess";
}
```

## See Also
* [AutoSave document in DocumentEditor](./auto-save-document-in-document-editor)
