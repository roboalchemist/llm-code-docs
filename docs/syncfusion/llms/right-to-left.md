# Source: https://docs.syncfusion.com/flutter/treemap/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/range-selector/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/range-slider/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/slider/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/maps/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/daterangepicker/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/datagrid/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/funnel-chart/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/pyramid-chart/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/circular-charts/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/cartesian-charts/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/chat/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/calendar/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/ai-assistview/right-to-left.md

# Source: https://docs.syncfusion.com/flutter/right-to-left.md

# Source: https://docs.syncfusion.com/winui/common/right-to-left.md

# Source: https://docs.syncfusion.com/windowsforms/right-to-left.md

# Source: https://docs.syncfusion.com/wpf/treeview/right-to-left.md

# Source: https://docs.syncfusion.com/wpf/textinputlayout/right-to-left.md

# Source: https://docs.syncfusion.com/wpf/right-to-left.md

# Source: https://docs.syncfusion.com/maui/treeview/right-to-left.md

# Source: https://docs.syncfusion.com/maui/textinputlayout/right-to-left.md

# Source: https://docs.syncfusion.com/maui/treemap/right-to-left.md

# Source: https://docs.syncfusion.com/maui/switch/right-to-left.md

# Source: https://docs.syncfusion.com/maui/stepprogressbar/right-to-left.md

# Source: https://docs.syncfusion.com/maui/segmented-control/right-to-left.md

# Source: https://docs.syncfusion.com/maui/listview/right-to-left.md

# Source: https://docs.syncfusion.com/maui/imageeditor/right-to-left.md

# Source: https://docs.syncfusion.com/maui/dataform/right-to-left.md

# Source: https://docs.syncfusion.com/maui/button/right-to-left.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/right-to-left.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/right-to-left.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/right-to-left.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/flutter/right-to-left.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/maui/right-to-left.md

# Right to left in .NET MAUI PDF Viewer (SfPdfViewer)

By default, the [SfPdfViewer](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.PdfViewer.SfPdfViewer.html) control is laid out in the left-to-right flow direction. For the convenience of right-to-left language users, it enables changing the flow direction to right-to-left (RTL). This can be achieved by setting the [FlowDirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.iview.flowdirection?view=net-maui-7.0) property to `RightToLeft`. 
Setting the [FlowDirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.iview.flowdirection?view=net-maui-7.0) property to `RightToLeft` on the SfPdfViewer sets the alignment to the right, and layouts the built-in controls used in the SfPdfViewer to flow from right-to-left. Refer to the following code example to apply the same.

{% tabs %}
{% highlight XAML %}

<syncfusion:SfPdfViewer
	x:Name="PdfViewer"
	FlowDirection="RightToLeft"/>

{% endhighlight %}
{% highlight C# %}

PdfViewer.FlowDirection = FlowDirection.RightToLeft;

{% endhighlight %}
{% endtabs %}

N> Right-to-Left language users can also refer to this [section](https://help.syncfusion.com/maui/pdf-viewer/migration#upcoming-features) for information on how to localize the static text used in the PDF reader to other languages.