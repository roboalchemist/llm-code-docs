# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/wpf/how-to/changing-the-current-user.md

# Change the CurrentUser in WPF Pdf Viewer

The PDF Viewer allows you to change the CurrentUser. If the CurrentUser property is not set, it defaults to the system user name. When you set the CurrentUser, the changes will be reflected in the author property of newly added annotations. The following code example illustrates how to set the CurrentUser:

{% tabs %}
{% highlight C# %}

//Initialize PDF Viewer.
PdfViewerControl pdfViewer = new PdfViewerControl();
//Load the PDF.
pdfViewer.Load("Sample.pdf");

//Changing the CurrentUser of document
pdfViewer.CurrentUser = "set the name here";
{% endhighlight %}



{% highlight vbnet %}

'Initialize PDF Viewer.
Private pdfViewer As New PdfViewerControl()
'Load the PDF.
pdfViewer.Load("Sample.pdf")

'Changing the CurrentUser of document
pdfViewer.CurrentUser = "set the name here";

{% endhighlight %}
{% endtabs %}
