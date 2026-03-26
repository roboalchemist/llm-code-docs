# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/winforms/how-to/view-the-pdf-stream-in-viewer.md

#  View the PDF Stream in PDF Viewer

PDF files as stream can be viewed in Essential&reg; PdfViewerControl using the overload available in the Load method. Following are the code snippets.


{% tabs %}
{% highlight c# %}

FileStream stream = new FileStream("Sample.pdf", FileMode.Open);
//Initialize PDF Viewer
PdfViewerControl pdfViewerControl1 =Â newÂ PdfViewerControl();
//Load the PDF
pdfViewerControl1.Load(stream);

{% endhighlight %}

{% highlight vb %}

Dim stream As New FileStream("Sample.pdf", FileMode.Open)
'Initialize PDF Viewer
Dim pdfViewerControl1 As New PdfViewerControl()
'Load the PDF
pdfViewerControl1.Load(stream)

{% endhighlight %}
{% endtabs %}
