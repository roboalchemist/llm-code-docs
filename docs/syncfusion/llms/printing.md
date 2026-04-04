# Source: https://docs.syncfusion.com/uwp/datagrid/printing.md

# Source: https://docs.syncfusion.com/winui/datagrid/printing.md

# Source: https://docs.syncfusion.com/windowsforms/treeview/printing.md

# Source: https://docs.syncfusion.com/windowsforms/pivot-grid/printing.md

# Source: https://docs.syncfusion.com/windowsforms/html-viewer/printing.md

# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/printing.md

# Source: https://docs.syncfusion.com/windowsforms/grid-control/printing.md

# Source: https://docs.syncfusion.com/windowsforms/syntax-editor/printing.md

# Source: https://docs.syncfusion.com/wpf/treegrid/printing.md

# Source: https://docs.syncfusion.com/wpf/olap-chart/printing.md

# Source: https://docs.syncfusion.com/wpf/gridcontrol/printing.md

# Source: https://docs.syncfusion.com/wpf/diagram/printing.md

# Source: https://docs.syncfusion.com/wpf/datagrid/printing.md

# Source: https://docs.syncfusion.com/wpf/charts/printing.md

# Source: https://docs.syncfusion.com/wpf/syntax-editor/printing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/wpf/printing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/winforms/printing.md

# Printing in Windows Forms Spreadsheet

Spreadsheet control allows you to print the data in the workbook with the help of PDF Conversion. To provide the printing support in Spreadsheet, you need to convert the workbook into PDF document using ExcelToPdfConverter.

For Conversion of Excel Workbook in Spreadsheet to PDF document, use `Convert` method of `ExcelToPdfConverter`.

For viewing the PDF document, you can use `PdfViewerControl` to load the saved PDF stream.

{% tabs %}
{% highlight c# %}

//Create the pdf viewer for load the document.
PdfViewerControl pdfViewer = new PdfViewerControl();

//Create Memory Stream to save pdf document
MemoryStream pdfStream = new MemoryStream();
ExcelToPdfConverter converter = new ExcelToPdfConverter (spreadsheet.Workbook);  

//Initialize the ExcelToPdfConverter Settings
ExcelToPdfConverterSettings settings = new ExcelToPdfConverterSettings(); 
settings.LayoutOptions = LayoutOptions.NoScaling;

{% endhighlight %}
{% endtabs %}

For print preview you can load the PDF stream into viewer and for direct printing use `Print` method in PdfViewerControl  which is available under the namespace âSyncfusion.PdfViewer.Windowsâ

{% tabs %}
{% highlight c# %}

//Initialize the PdfDocument
PdfDocument pdfDoc = new PdfDocument ();

//Assign the PdfDocument to the templateDocument property of ExcelToPdfConverterSettings  
settings.TemplateDocument = pdfDoc;
settings.DisplayGridLines = GridLinesDisplayStyle.Invisible;

//Convert Excel Document into PDF document
pdfDoc = converter.Convert(settings);

//Save the PDF file     
pdfDoc.Save(pdfStream);

//Load the document to pdf viewer
pdfViewer.Load(pdfStream);

//Print the doc
pdfViewer.Print(true);

{% endhighlight %}
{% endtabs %}
