# Source: https://docs.syncfusion.com/wpf/classic/griddata/exporting-and-persistence.md

# Exporting and Persistence in WPF GridDataControl (Classic)

This section covers the Exporting and persistence:

## Exporting GDC to Excel

The GridExcelConverter class provides support for exporting data from a GridDataControl to an Excel spreadsheet for verification and/or computation. This control automatically copies the GridDataControl's styles and formats to Excel. The GridExcelConverter controlÂ is derived from GridExcelConverterBase. The XlsIO libraries are used to support the conversion of the GridDataControl contents to Excel. The following dll files should be added, along with the default dll files in the reference folder: 

* Syncfusion.XlsIO.Base
*  Syncfusion.XlsIO.WPF  
* Syncfusion.GridConverter.Wpf

### Features

#### Entire Content


You can convert the entire content of a GridDataControl to an Excel Spreadsheet. You can also avail the option for specifying the version of the Excel file using the ExcelVersion enum. The version can be one of the following: 

* ExcelVersion.Excel97to2003  
* ExcelVersion.Excel2007

The following code illustrates the conversion of GridDataControl contents to an Excel Spreadsheet: 

{% highlight c# %}

gridDataControl.ExportToExcel("Sample.xlsx", ExcelVersion.Excel2007 );

(or)

gridDataControl.ExportToExcel("Sample.xls", ExcelVersion.Excel97to2003 );

{% endhighlight  %}

![Before exporting the data from WPF GridData control](Getting-Started_images/Getting-Started_img129.jpeg)

![After exporting the data to spreadsheet from WPF GridData control](Getting-Started_images/Getting-Started_img130.jpeg)

The above images shows how the entire content of the GridDataControl is exported to an Excel Spreadsheet.

#### Selected Rows

You can also avail the choice of converting the selected rows of GridDataControl to an Excel Spreadsheet.

The following code illustrates the conversion of selected rows of GridDataControl to an Excel Spreadsheet:

{% highlight c# %}

grid.ExportToExcel(grid.Model.SelectedRanges.ActiveRange,"sample.xlsx", ExcelVersion.Excel2007);

{% endhighlight  %}

#### GridDataControl with Nested Child

You can convert the content of a GridDataControl, with Nested Child to an Excel Spreadsheet. Parent and visible child content are exported to Excel Spreadsheet.

The following code illustrates the conversion of GridDataControl with Nested Child to an Excel Spreadsheet:

{% highlight c# %}

gridDataControl.ExportToExcel("Sample.xlsx", ExcelVersion.Excel2007 );

(or)

gridDataControl.ExportToExcel("Sample.xls", ExcelVersion.Excel97to2003 );

{% endhighlight  %}

N> Only the visible child's contents are exported.

![Before exporting the nested child data from WPF GridData control](Getting-Started_images/Getting-Started_img131.jpeg)

![After exporting the nested child data from WPF GridData control](Getting-Started_images/Getting-Started_img132.jpeg)

The above images shows how the GridControl, with Nested Child is exported to an Excel Spreadsheet.

#### GridDataControl with Grouping

You can convert the content of a GridDataControl, with Grouping to an Excel Spreadsheet. The following code illustrates this feature:

{% highlight c# %}

gridDataControl.ExportToExcel("Sample.xlsx", ExcelVersion.Excel2007 );

(or)

gridDataControl.ExportToExcel("Sample.xls", ExcelVersion.Excel97to2003 );

{% endhighlight  %}

N> Only the visible grouping contents are exported.

![Before exporting the grouping data from WPF GridData control](Getting-Started_images/Getting-Started_img133.jpeg)

![After exporting the grouping data from WPF GridData control](Getting-Started_images/Getting-Started_img134.jpeg)

The above images shows how the GridControl, with Grouping is exported to an Excel Spreadsheet.

### GridDataControl Export to CSV

The ExportToCSV method of the GridModelExportExtensions class enables GridDataControl to easily be exported to CSV format.

To enable exporting, the following .dll files must be added along with the default .dll files in the reference folder:

* Syncfusion.XlsIO.Base
* Syncfusion.XlsIO.WPFÂ 
* Syncfusion.GridConverter.Wpf

Converting GridDataControl to CSV format

You can convert the entire content of a grid control to a CSV file by using the following code:

{% highlight c# %}

this.gdc.Model.ExportToCSV("Sample.csv")

{% endhighlight  %}

{% highlight vbnet %}

Me.gdc.Model.ExportToCSV("Sample.csv")

{% endhighlight  %}

When the code runs, the following output displays.

![Before exporting the grid from WPF GridData control to CSV](Getting-Started_images/Getting-Started_img135.jpeg)

When you are ready to export the entire grid, click Export to CSV; the grid content can then be converted to CSV format. 

![After exporting the grid from WPF GridData control to CSV](Getting-Started_images/Getting-Started_img136.jpeg)

## Export to PDF

Essential GridData control enables you to export the content of the GridData control into a pdf file. This feature allows you to maintain the records as a pdf file. The pdf libraries are used to support the conversion of the GridData controlâs content to pdf. The following dll files should be added along the default dll in the reference folder:

* Syncfusion.Pdf.Base.
* Syncfusion.GridConverter.Wpf

The pdf export can be performed in the following two ways:

* Export by PdfGrid
* Export by PdfLightTable

PdfGrid: In the PdfGrid, the formatting can be done to all levels of the PdfGrid. The features like row and column spanning are also supported by the PdfGrid. It offers, full control over the appearance of the PdfGrid table and is recommended to draw complex table structures. 

PdfLightTable: It allows you to perform simple formatting, using the events. The PdfLightTable allows minimal customization options. Rendering the table using PdfLightTable is faster than PdfGrid and drawing a simple table is recommended.

### Features

The export to pdf comprises the following features:

* Export entire content.
* Export selected range.
* Export GridData control with grouping.
* Export with styles and formatted cell value (This works by default). 

#### Export Entire Content


Essential GridData control allows you to export the GridData controlâs entire content as a PDF file.

#### Use Case Scenario

A large data can be maintained as PDF file and the entire content of the GridData control can be exported iPDF a pdf file.

The following XAML code example shows, how the GridData control is defined in an application.

{% highlight xaml %}

<syncfusion:GridDataControâÂ x:Name=âdataGrid"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â AutoPopulatâColumâs="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â AutoPopulateRâlatioâs="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ColâmnSiâer="Star"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â IteâsSource="{BindingÂ OrdeâDetails}"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ShowAâdNewRâw="False"Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â VisâalStyle="SyncfuâionTheme">

Â Â Â Â <!--Â Â codeÂ forÂ VisibleÂ ColumnsÂ Â yncfusionyncfusion:GridDataControl.VisibleColumns>

 yncfusionyncfusion:GridDataVisibleColumnÂ HeâderText=âOrderÂ ID"Â MapâingNameâ"OrderID">

Â Â Â Â yncfusionyncfusion:GridDataVisibleColumn.HeaderStyle>

Â Â Â Â Â Â Â Â yncfusionyncfusion:GridDataColumnStyleÂ HorizontalAâignmenâ="Center"Â />

Â Â Â Â Â yncfusionyncfusion:GridDataVisibleColumn.HeaderStyle>

Â Â Â Â yncfusionyncfusion:GridDataVisibleColumn.ColumnStyle>

Â Â Â Â Â Â Â Â yncfusionyncfusion:GridDataColumnStyleÂ HorizontalAâignmeât="Right"Â />

Â Â Â Â Â yncfusionyncfusion:GridDataVisibleColumn.ColumnStyle>

Â yncfusionyncfusion:GridDataVisibleColumn>



yncfusionyncfusion:GridDataVisibleColumnÂ AâlowSoât="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â HeâderText="CuâtomerÂ ID"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â MapâingName="CâstomerID">

Â Â Â Â yncfusionyncfusion:GridDataVisibleColumn.HeaderStyle>

Â Â Â Â Â Â Â Â yncfusionyncfusion:GridDataColumnStyleÂ HorizontalAâignmenâ="Center"Â />

Â Â Â Â Â yncfusionyncfusion:GridDataVisibleColumn.HeaderStyle>

Â yncfusionyncfusion:GridDataVisibleColumn>



yncfusionyncfusion:GridDataVisibleColumnÂ HeâderText="âhipÂ Name"Â 

                                          MapâingName=âShipName">

Â Â Â Â yncfusionyncfusion:GridDataVisibleColumn.HeaderStyle>

Â Â Â Â Â Â Â Â yncfusionyncfusion:GridDataColumnStyleÂ HorizontalAâignmenâ="Center"Â />

Â Â Â Â Â yncfusionyncfusion:GridDataVisibleColumn.HeaderStyle>

Â yncfusionyncfusion:GridDataVisibleColumn>



yncfusionyncfusion:GridDataVisibleColumnÂ HeâderText="ShiâÂ Address"Â 

                                          MapâingName="ShâpAddress"Â />yncfusionyncfusion:GridDataControl.VisibleColuyncfusionyncfusion:GridDataControl>

{% endhighlight  %}

![Export entire data to the WPF GridData control](Getting-Started_images/Getting-Started_img137.png)

#### Exporting to PdfGrid

The following code example illustrates how to export the entire content of the GridData control into a PdfGrid.

{% highlight c# %}

//Â DialogÂ toÂ saveÂ theÂ newlyÂ createdÂ pdfÂ document.

SaveFileDialogÂ sfdÂ =Â newÂ SaveFileDialog

{

Â Â DefaultExtÂ =Â ".pdf",

Â Â FilterÂ =Â "AdobeÂ PDFÂ Files(*.pdf)|*.pdf",

Â Â FilterIndexÂ =Â 1

};

//Â NewlyÂ createdÂ pdf documentÂ object.

PdfDocumentÂ documentÂ =Â newÂ PdfDocument();

ifÂ (sfd.ShowDialog()Â ==Â true)

{

Â Â Â Â usingÂ (StreamÂ streamÂ =Â sfd.OpenFile())

Â Â Â Â {Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 

Â Â Â Â Â Â Â Â //MethodÂ callingÂ toÂ exportÂ theÂ gridÂ contentÂ intoÂ pdf.

Â Â Â Â Â Â Â Â documentÂ =Â grid.Model.ExportToPdfGridDocument(GridRangeInfo.Table());

Â Â Â Â Â Â Â Â document.Save(stream);

Â Â Â Â Â Â Â Â Process.Start(sfd.FileName);

Â Â Â Â }

}

{% endhighlight  %}

The following screenshot shows the exported pdf document:

![Export the PDF document in WPF GridData control](Getting-Started_images/Getting-Started_img138.png)

#### Exporting to PdfLightTable Document

The following code example illustrates how to export the entire content of the GridData control into a PdfLightTable document file.

{% highlight c# %}

//Â DialogÂ toÂ saveÂ theÂ newlyÂ createdÂ pdfÂ document.

SaveFileDialogÂ sfdÂ =Â newÂ SaveFileDialog

{

Â Â Â Â DefaultExtÂ =Â ".pdf",

Â Â Â Â FilterÂ =Â "AdobeÂ PDFÂ Files(*.pdf)|*.pdf",

Â Â Â Â FilterIndexÂ =Â 1

};

//Â NewlyÂ createdÂ pdf documentÂ object.

PdfDocumentÂ documentÂ =Â newÂ PdfDocument();

ifÂ (sfd.ShowDialog()Â ==Â true)

{

Â Â Â Â usingÂ (Â StreamÂ streamÂ =Â sfd.OpenFile())

Â Â Â Â {

Â Â Â Â Â Â Â Â //MethodÂ callingÂ toÂ exportÂ theÂ gridÂ contentÂ intoÂ pdf.

Â Â Â Â Â Â Â Â documentÂ =Â grid.Model.ExportToPdfLightTableDocument(GridRangeInfo.Table());

Â Â Â Â Â Â Â Â document.Save(stream);

Â Â Â Â Â Â Â Â Process.Start(sfd.FileName);

Â Â Â Â }
}

{% endhighlight  %}

![Exporitng to PDF table in WPF GridDataControl](Getting-Started_images/Getting-Started_img139.png)

#### Export Selected Range

You can convert the selected range of the GridData control into a pdf file.

![Export selected ranges in WPF GridData control](Getting-Started_images/Getting-Started_img140.png)

#### Exporting to PdfGrid

The following code illustrates the conversion of a selected range of the GridData control to a PdfGrid.

{% highlight c# %}

//Â DialogÂ toÂ saveÂ theÂ newlyÂ createdÂ pdfÂ document.

SaveFileDialogÂ sfdÂ =Â newÂ SaveFileDialog

{

	DefaultExtÂ =Â ".pdf",

Â Â Â Â FilterÂ =Â "AdobeÂ PDFÂ Files(*.pdf)|*.pdf",

Â Â Â Â FilterIndexÂ =Â 1

};

//Â NewlyÂ createdÂ pdf documentÂ object.

PdfDocumentÂ documentÂ =Â newÂ PdfDocument();

ifÂ (sfd.ShowDialog()Â ==Â true)

{

Â Â Â Â usingÂ (StreamÂ streamÂ =Â sfd.OpenFile())

Â Â Â Â {Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 

Â Â Â Â Â Â Â Â //MethodÂ callingÂ toÂ exportÂ theÂ gridÂ contentÂ intoÂ pdf.

Â Â Â Â Â Â Â Â documentÂ =Â grid.Model.ExportToPdfGridDocument(

Â Â Â Â Â Â Â Â grid.Model.SelectedRanges.ActiveRange);

Â Â Â Â Â Â Â Â document.Save(stream);

Â Â Â Â Â Â Â Â Process.Start(sfd.FileName);

Â Â Â Â }

}
{% endhighlight  %}

The following screenshot shows the exported pdf document of a selected range of the GridData control:

![Exproting to PDF grid in WPF GridData control](Getting-Started_images/Getting-Started_img141.png)

#### Exporting to PdfLightTable Document

The following code illustrates the conversion of a selected range of the GridData control to a PdfLightTable document.

{% highlight c# %}

//Â DialogÂ toÂ saveÂ theÂ newlyÂ createdÂ pdfÂ document.

SaveFileDialogÂ sfdÂ =Â newÂ SaveFileDialog

{

DefaultExtÂ =Â ".pdf",

FilterÂ =Â "AdobeÂ PDFÂ Files(*.pdf)|*.pdf",

FilterIndexÂ =Â 1

};

//Â NewlyÂ createdÂ pdf documentÂ object.

PdfDocumentÂ documentÂ =Â newÂ PdfDocument();

ifÂ (sfd.ShowDialog()Â ==Â true)

{

usingÂ (Â StreamÂ streamÂ =Â sfd.OpenFile())

{

Â Â Â Â //MethodÂ callingÂ toÂ exportÂ theÂ gridÂ contentÂ intoÂ pdf.

Â Â Â Â documentÂ =Â grid.Model.ExportToPdfLightTableDocument(grid.Model.SelectedRanges.ActiveRange);

Â Â Â Â document.Save(stream);

Â Â Â Â Process.Start(sfd.FileName);

}

}

{% endhighlight  %}

The following screenshot shows the exported PdfLightTable document of the selected range of the GridData control.

![Exporting to Adobe reader document in WPF GridData control](Getting-Started_images/Getting-Started_img142.png)

#### Export GridDataControl with Grouping

The GridData control converts the content of the GridData control to a pdf document with grouping.

The following screenshot illustrates how the GridData control appears as a pdf file after grouping the data.

![Before exporting WPF GridData control with grouping data](Getting-Started_images/Getting-Started_img143.png)

![After exporting WPF GridData control with grouping data](Getting-Started_images/Getting-Started_img144.png)

The following screenshot illustrates how the GridData control appears as a PdfLightTable document after grouping the data.

![Export the grouping data in WPF GridData control](Getting-Started_images/Getting-Started_img145.png)

#### Exporting Customized GridData Control 

Use the following code to customize the GridData control with blend styling.

{% highlight xaml %}


<syncfusion:GridDataControlÂ x:Name="grid"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Grid.Row="0"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Margin="10"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â AllowEdit="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â AutoPopulateColumns="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â AutoPopulateRelations="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ColumnSizer="Star"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ContextMenuOptions="CustomWithDefault"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ContextMenuStyle="{StaticResourceÂ RContextMenuStyle}"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â EnableBlendStyling="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â HeaderStyle="{StaticResourceÂ                                                                             

									GridDataHeaderCellControlStyle2}"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â HideColumnsWhenGrouped="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â IsGroupsExpanded="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ItemsSource="{BindingÂ Path=MovieDetails}"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ListBoxSelectionMode="MultiExtended"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â PersistGroupsExpandState="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ShowAddNewRow="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ShowFilters="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ShowGroupDropArea="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ShowHoveringBackground="false"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ShowTableSummaries="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ShowTooltips="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â StyleManager="{StaticResourceÂ CustomGridDataStyleManager}">

Â Â Â Â Â Â Â Â Â Â Â Â <!--Â Â TableÂ SummaryÂ rowsÂ createdÂ hereÂ Â -->

Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataControl.TableSummaryRows>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataSummaryRowÂ Title="TotalÂ :Â {CountSummary}Â Items"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â ShowSummaryInRow="True"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â TitleColumnCount="2">

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataSummaryRow.SummaryColumns>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataSummaryColumnÂ Name="CountSummary"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Format="'{Count:d}'"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â MappingName="OrderId"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â SummaryType="CountAggregate"Â />

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataSummaryRow.SummaryColumns>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataSummaryRow>

Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataControl.TableSummaryRows>



Â Â Â Â Â Â Â Â Â Â Â Â <!--Â Â GroupedÂ ColumnÂ CreatedÂ hereÂ Â -->

Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataControl.GroupedColumns>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataGroupColumnÂ ColumnName="Movie"Â />

Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataControl.GroupedColumns>



Â Â Â Â Â Â Â Â Â Â Â Â <!--Â Â VisibleÂ ColumnÂ CreatedÂ hereÂ Â -->

Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataControl.VisibleColumns>



Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataVisibleColumnÂ MappingName="Movie">

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataTextFilteringPaneÂ Foreground="Black"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â IsThemed="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â PredicateType="And"Â />

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn>



Â Â <syncfusion:GridDataVisibleColumnÂ ColumnStyle="{StaticResourceÂ GridDataColumnStyle}"Â                                                                 MappingName="OrderId">

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataTextFilteringPaneÂ Foreground="Black"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â IsThemed="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â PredicateType="And"Â />

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn>



Â Â <syncfusion:GridDataVisibleColumnÂ ColumnStyle="{StaticResourceÂ GridDataColumnStyle}"Â                                                                   MappingName="Name">

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataTextFilteringPaneÂ Foreground="Black"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â IsThemed="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â PredicateType="And"Â />

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn>



Â Â <syncfusion:GridDataVisibleColumnÂ ColumnStyle="{StaticResourceÂ GridDataColumnStyle}"Â                                                                 MappingName="SeatNo">

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataTextFilteringPaneÂ Foreground="Black"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â IsThemed="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â PredicateType="And"Â />

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn>



Â Â Â <syncfusion:GridDataVisibleColumnÂ ColumnStyle="{StaticResourceÂ GridDataColumnStyle}"Â                                                                  MappingName="City">

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:GridDataTextFilteringPaneÂ Foreground="Black"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â IsThemed="False"

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â PredicateType="And"Â />

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn.FilterPane>

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataVisibleColumn>

Â Â Â <syncfusion:GridDataVisibleColumnÂ ColumnStyle="{StaticResourceÂ GridDataColumnStyle}"Â                                                               MappingName="Theatre"Â />

Â Â Â Â Â Â Â Â Â Â Â Â </syncfusion:GridDataControl.VisibleColumns>



Â Â Â Â Â Â Â Â </syncfusion:GridDataControl>

{% endhighlight %}

Use the following code to export a customized GridData control:

#### Button Code to Export:

{% highlight xaml %}

<ButtonÂ Name="Exportbtn"Â Content="ExportÂ ToÂ Pdf"Â Â Click="Exportbtn_Click"/>

{% endhighlight  %}

Button Click Event Code:

{% highlight c# %}


privateÂ voidÂ Exportbtn_Click(objectÂ sender,Â RoutedEventArgsÂ e)

{

// Dialog to save the exported document.

SaveFileDialogÂ sfdÂ =Â newÂ SaveFileDialog

{

Â Â DefaultExtÂ =Â ".pdf",

Â Â FilterÂ =Â "AdobeÂ PDFÂ Files(*.pdf)|*.pdf",

Â Â FilterIndexÂ =Â 1

Â };

// Pdf document object to save the data as a pdf file.

Â PdfDocumentÂ documentÂ =Â newÂ PdfDocument();

Â ifÂ (sfd.ShowDialog()Â ==Â true)

{

Â Â usingÂ (StreamÂ streamÂ =Â sfd.OpenFile())

Â Â {

Â Â Â documentÂ =Â dataGrid.Model.ExportToPdfGridDocument(GridRangeInfo.Table());

Â Â Â document.Save(stream);

Â Â Â Process.Start(sfd.FileName);

Â Â }

Â Â }

}

{% endhighlight  %}

#### GridDataControl with Blend Styling

The below screenshot shows the customized blend styling of the GridData control.

![WPF GridData control with Blend style](Getting-Started_images/Getting-Started_img146.png)

#### Exported PDF Document

The screenshot below shows a PDF document of the blend styling GridData control.

![Export the WPF GridData control with Blend style to PDF document](Getting-Started_images/Getting-Started_img147.png)

## Serialization in GridDataControl

GridDataControl state can be serialized in XML format. 

All the properties that are exposed in GridDataTableProperties can be serialized. 

### Serializing 

There are two methods to serialize forms:

* XML string
* XML file



### API Usage

### Serializing as XML String

The following code illustrates how to serialize as an XML string. 

{% highlight c# %}

string result = this.dataGrid.Model.SerializeAsString();

{% endhighlight %}

### Serializing as an XML File

The following code illustrates how to serialize as an XML file. 

{% highlight c# %}

this.dataGrid.Model.Serialize("sample.xml");

{% endhighlight  %}

### De-serializing 

There are two methods to serialize forms:

* XML string
* XML file

### API Usage

### De-serialize from XML String

The following code illustrates how to de-serialize from an XML string_._ 

{% highlight c# %}

this.dataGrid.Model.DeserializeFromString(content); 

// the content should be an XML string saved during the serialization process.

{% endhighlight  %}


### De-serialize from XML File

The following code illustrates how to de-serialize from an XML file.

{% highlight c# %}

this.dataGrid.Model.Deserialize("sample.xml"); 

// sample.xml file should be the XML file saved during the serialization process.

{% endhighlight  %}