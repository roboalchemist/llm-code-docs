# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/maui/document-link-annotations.md

# Document Link Navigation in .NET MAUI PDF Viewer (SfPdfViewer)

The PDF viewer allows navigating from one part of the PDF document to another using document link annotations. When a document link annotation is tapped, the PDF viewer scrolls to its destination. This type of link annotation is most often used to represent the table of contents of a PDF document. 

The document link navigation can be turned on or off using the [EnableDocumentLinkNavigation](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.PdfViewer.SfPdfViewer.html#Syncfusion_Maui_PdfViewer_SfPdfViewer_EnableDocumentLinkNavigation) property. The default value of this property is true. The code snippet below illustrates disabling the document link navigation.

{% tabs %}
{% highlight c# %}

pdfViewer.EnableDocumentLinkNavigation = false;

{% endhighlight %}
{% endtabs %}
