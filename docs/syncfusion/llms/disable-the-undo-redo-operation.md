# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/wpf/how-to/disable-the-undo-redo-operation.md

# Disable the Undo Redo operation 

To disable the Undo Redo operation, set the Limit property of UndoRedoSettings to zero. By default, this value is set to 100. Reducing the value to zero will disable the Undo Redo functionality. The following code example demonstrates how to set the Limit value:

{% tabs %}
{% highlight C# %}

//Initialize PDF Viewer.
PdfViewerControl pdfViewer = new PdfViewerControl();
//Set Limit property as zero
pdfViewer.UndoRedoSettings.Limit = 0;
//Load the PDF.
pdfViewer.Load("Sample.pdf");


{% endhighlight %}



{% highlight vbnet %}

'Initialize PDF Viewer.
Private pdfViewer As New PdfViewerControl()
'Set Limit property as zero
pdfViewer.UndoRedoSettings.Limit = 0
'Load the PDF.
pdfViewer.Load("Sample.pdf")


{% endhighlight %}
{% endtabs %}