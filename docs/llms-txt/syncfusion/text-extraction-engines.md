# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/wpf/text-extraction-engines.md

# Text Extraction Engines in WPF Pdf Viewer

Syncfusion&reg; WPF PDF Viewer extracts text information from PDF files through two different engines for performing text search, text selection, creating text markups and more.

* PDFium (Google Chromeâs text extraction engine)
* SfPdf (Syncfusionâs own text extraction engine)

N> Before version 19.4.0.48, we used our own text extraction engine (SfPdf) to perform text-based operations in the PDF pages. We have updated our default text extraction engine to PDFium from version 19.4.0.48. 

The PDFium text extraction engine is recommended for improved performance. However, you may still use our old text extraction engine by setting the [TextExtractionEngine](https://help.syncfusion.com/cr/wpf/Syncfusion.Windows.PdfViewer.PdfViewerControl.html#Syncfusion_Windows_PdfViewer_PdfViewerControl_TextExtractionEngine) property to `SfPdf`. Refer to the following code snippet to apply the same.

{% tabs %}
{% highlight c# %}

pdfViewer.TextExtractionEngine = PdfTextExtractionEngine.SfPdf;

{% endhighlight %}
{% endtabs %}

For additional information about the usage of the text extraction engine, please refer to the [text extraction](https://help.syncfusion.com/wpf/pdf-viewer/extract-text-from-pdf) functionalities.