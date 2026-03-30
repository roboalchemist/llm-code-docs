# Source: https://docs.syncfusion.com/winui/treegrid/ui-customization.md

# Source: https://docs.syncfusion.com/winui/segmentedcontrol/ui-customization.md

# Source: https://docs.syncfusion.com/winui/datagrid/ui-customization.md

# Source: https://docs.syncfusion.com/winui/combobox/ui-customization.md

# Source: https://docs.syncfusion.com/winui/color-picker/ui-customization.md

# Source: https://docs.syncfusion.com/winui/color-palette/ui-customization.md

# Source: https://docs.syncfusion.com/winui/calendar/ui-customization.md

# Source: https://docs.syncfusion.com/winui/autocomplete/ui-customization.md

# Source: https://docs.syncfusion.com/maui/combobox/ui-customization.md

# Source: https://docs.syncfusion.com/maui/autocomplete/ui-customization.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/flutter/ui-customization.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/maui/ui-customization.md

# UI Customization in .NET MAUI PDF Viewer (SfPdfViewer)

This section walks you through the UI customization options supported in the [SfPdfViewer](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.PdfViewer.SfPdfViewer.html).

## Customize the loading indicator

You can customize the loading indicatorâs properties by applying a style with the `TargetType` property to `ActivityIndicator`. You may also need to set the [ApplyToDerivedTypes](https://learn.microsoft.com/en-us/dotnet/maui/user-interface/styles/xaml?view=net-maui-7.0#apply-a-style-to-derived-types) property to `True` to get the style applied to the derived classes. See the following code example to customize the color of the loading indicator.

{% tabs %}
{% highlight xaml %}

<syncfusion:SfPdfViewer>
	<syncfusion:SfPdfViewer.Resources>
		<Style TargetType="ActivityIndicator" 
			   ApplyToDerivedTypes="True">
				<Setter Property="Color" Value="Red" />
			</Style>
	</syncfusion:SfPdfViewer.Resources>
</syncfusion:SfPdfViewer>

{% endhighlight %} 
{% endtabs %}

N> For complete customization of the PDF Viewer, themes can be applied. Refer to the [theme user guide](https://help.syncfusion.com/maui/themes/themes) for detailed instructions. You can also explore the [sample project](https://github.com/SyncfusionExamples/maui-pdf-viewer-examples/tree/master/Styles/PDFViewerThemes), which demonstrates the custom theme implementation for the PDF Viewer in .NET MAUI applications.