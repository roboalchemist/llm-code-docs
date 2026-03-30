# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/uwp/how-to/customize-the-scrollbar.md

# Customize the scrollbar in UWP PDF Viewer

## Customize the color of the scrollbar thumb

The PDF viewer uses the [ScrollViewer] (https://docs.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.scrollviewer?view=winrt-19041) control to scroll the pages of a PDF. The color of the vertical and horizontal scrollbar thumbs can be customized using the following code. 
 
{% tabs %}
{% highlight xaml %}
<sf:SfPdfViewerControl x:Name = âpdfViewerâ>
<sf:SfPdfViewerControl.Resources>
        <SolidColorBrush x:Key="ScrollBarThumbFill" Color="Gold"/>
        <SolidColorBrush x:Key="ScrollBarThumbFillPointerOver" Color="Orange"/>
        <SolidColorBrush x:Key="ScrollBarThumbFillPressed" Color="Red"/>
        <SolidColorBrush x:Key="ScrollBarThumbFillDisabled" Color="Pink"/>
</sf:SfPdfViewerControl.Resources>
</sf:SfPdfViewerControl>
{% endhighlight %}
{% endtabs %}

## Customize the width of the vertical scrollbar

The width of the vertical scrollbar of the [ScrollViewer](https://docs.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.scrollviewer?view=winrt-20348) can be modified by using the [VerticalScrollBarWidth](https://help.syncfusion.com/cr/uwp/Syncfusion.Windows.PdfViewer.SfPdfViewerControl.html#Syncfusion_Windows_PdfViewer_SfPdfViewerControl_VerticalScrollBarWidth) property. The default value of the API is as same as the default width of the vertical scrollbar of the [ScrollViewer](https://docs.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.scrollviewer?view=winrt-20348) control.

{% tabs %}
{% highlight c# %}

//Sets the width of the vertical scrollbar in the PDF Viewer. 
pdfViewerControl.VerticalScrollBarWidth = 100; 
//Gets the width of the vertical scrollbar in the PDF Viewer. 
double verticalScrollBarWidth = pdfViewerControl.VerticalScrollBarWidth;

{% endhighlight %}
{% endtabs %}

