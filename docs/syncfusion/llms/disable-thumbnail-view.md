# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/uwp/how-to/disable-thumbnail-view.md

# Disable thumbnail view in UWP PDF Viewer
The SfPdfViewer control allows you to enable and disable thumbnail view that is opened when the document is magnified below 100%. The following code illustrates the same.
{% tabs %}
{% highlight c# %}
pdfViewer.IsThumbnailViewEnabled = false;
{% endhighlight %}
{% highlight vbnet %}
pdfViewer.IsThumbnailViewEnabled = False
{% endhighlight %}
{% endtabs %}
