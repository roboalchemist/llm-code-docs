# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/wpf/changing-the-text-displayed-in-the-loading-indicator.md

# Change the text displayed in the loading indicator in WPF Pdf Viewer

PDF Viewer allows you to change the text displayed in the loading indicator. The following code example illustrates the same.

{% tabs %}
{% highlight C# %}

// Changing the text displayed in the loading indicator
pdfviewer1. LoadingIndicator.LoadingMessage = "Document loading";
{% endhighlight %}




{% highlight vbnet %}

'Changing the text displayed in the loading indicator
pdfviewer1.LoadingIndicator.LoadingMessage = "Document loading"

{% endhighlight %}
{% endtabs %}
