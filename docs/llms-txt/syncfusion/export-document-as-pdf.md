# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/export-document-as-pdf.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/export-document-as-pdf.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/export-document-as-pdf.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/export-document-as-pdf.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/export-document-as-pdf.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/export-document-as-pdf.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/export-document-as-pdf.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/export-document-as-pdf.md

# How to export the document as PDF in React Document Editor

This article explains how to export the document as PDF format. You can export the document as PDF in following ways:

## Export the document as PDF in client-side

Use [`pdf export component`](https://www.npmjs.com/package/@syncfusion/ej2-pdf-export) in application level to export the document as PDF using `exportAsImage` API. Here, all pages will be converted to image and inserted as PDF pages (works like print as PDF).

>Note: 
* The Document Editor exports PDFs by converting pages into images on the client side, which may slightly increase file size compared to text-based PDFs.
* Text search is not supported in the exported PDF, as the content is stored as images.
* You can install the PDF export packages from this [`link`](https://www.npmjs.com/package/@syncfusion/ej2-pdf-export).


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-button id="element" content="Using Pdf Export" onclick="exportClientSide()"></ejs-button>

    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>
</div>
<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        documenteditor = container.documentEditor;
    }
    //Pdf document exported using pdf export
    function exportClientSide() {
        let pdfdocument = new ej.pdfexport.PdfDocument();
        let count = container.documentEditor.pageCount;
        container.documentEditor.documentEditorSettings.printDevicePixelRatio = 2;
        let loadedPage = 0;
        for (let i = 1; i <= count; i++) {
            setTimeout(() => {
                let format = 'image/jpeg';
                // Getting pages as image
                let image = container.documentEditor.exportAsImage(i, format);
                image.onload = function () {
                    let imageHeight = parseInt(
                        image.style.height.toString().replace('px', '')
                    );
                    let imageWidth = parseInt(
                        image.style.width.toString().replace('px', '')
                    );
                    let section = pdfdocument.sections.add();
                    let settings = new ej.pdfexport.PdfPageSettings(0);
                    if (imageWidth > imageHeight) {
                        settings.orientation = PdfPageOrientation.Landscape;
                    }
                    settings.size = new ej.pdfexport.SizeF(imageWidth, imageHeight);
                    (section).setPageSettings(settings);
                    let page = section.pages.add();
                    let graphics = page.graphics;
                    let imageStr = image.src.replace('data:image/jpeg;base64,', '');
                    let pdfImage = new ej.pdfexport.PdfBitmap(imageStr);
                    graphics.drawImage(pdfImage, 0, 0, imageWidth, imageHeight);
                    loadedPage++;
                    if (loadedPage == count) {
                        // Exporting the document as pdf
                        pdfdocument.save(
                            (container.documentEditor.documentName === ''
                                ? 'sample'
                                : container.documentEditor.documentName) + '.pdf'
                        );
                    }
                };
            }, 500);
        }
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="Export-pdf-client.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}



## Export document as PDF in server-side using Syncfusion<sup style="font-size:70%">&reg;</sup> DocIO

With the help of [`Syncfusion DocIO`](https://help.syncfusion.com/file-formats/docio/word-to-pdf), you can export the document as PDF in server-side. Here, you can search the text.

The following way illustrates how to convert the document as PDF:

* Using `serialize` API, convert the document as Sfdt and send it to server-side.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-button id="element" content="Export" onclick="exportServerSide()"></ejs-button>
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated"
        height="590px"></ejs-documenteditorcontainer>
</div>
<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        documenteditor = container.documentEditor;
    }
    function exportServerSide() {
        let http = new XMLHttpRequest();
        // Replace your running web service Url here
        http.open('POST', '/api/documenteditor/ExportPdf');
        http.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        http.responseType = 'json';
        //Serialize document content as SFDT.
        let sfdt = { content: container.documentEditor.serialize() };
        //Send the sfdt content to server side.
        http.send(JSON.stringify(sfdt));
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Export-pdf-server.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}



* Using Save API in server-side, you can convert the sfdt to stream.
* Finally, convert the stream to PDF using `Syncfusion.DocIORenderer.Net.Core` library.

```csharp
[AcceptVerbs("Post")]
[HttpPost]
[EnableCors("AllowAllOrigins")]
[Route("ExportPdf")]
public void ExportPdf([FromBody]SaveParameter data)
{
    // Converts the sfdt to stream
    Stream document = WordDocument.Save(data.content, FormatType.Docx);
    Syncfusion.DocIO.DLS.WordDocument doc = new Syncfusion.DocIO.DLS.WordDocument(document, Syncfusion.DocIO.FormatType.Docx);
    //Instantiation of DocIORenderer for Word to PDF conversion
    DocIORenderer render = new DocIORenderer();
    //Converts Word document into PDF document
    PdfDocument pdfDocument = render.ConvertToPDF(doc);
    // Saves the document to server machine file system, you can customize here to save into databases or file servers based on requirement.
    FileStream fileStream = new FileStream("sample.pdf", FileMode.OpenOrCreate, FileAccess.ReadWrite);
    //Saves the PDF file
    pdfDocument.Save(fileStream);
    pdfDocument.Close();
    fileStream.Close();
    document.Close();
}

```

Get the complete working sample in this [`link`](https://github.com/SyncfusionExamples/Export-document-as-PDF-in-Document-Editor/).