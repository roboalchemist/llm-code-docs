# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/exporting/how-to-convert-the-contents-of-gridcontrol-or-grid.md

# How to convert the contents of GridControl or GridDataBoundGridControl to Excel

The Contents of GridControl and GridDataBoundGrid can be transferred to Excel by using GridToExcel method of GridExcelConverter class. Here is the code snippet.

{% tabs %}
{% highlight c# %}

Syncfusion.GridExcelConverter.GridExcelConverterControl excelConverter = new Syncfusion.GridExcelConverter.GridExcelConverterControl();
excelConverter.GridToExcel(this.gridControl1.Model,@"C:\MyGC.xls");

{% endhighlight %}

{% highlight vb %}

Dim excelConverter As New Syncfusion.GridExcelConverter.GridExcelConverterControl
excelConverter.GridToExcel(Me.gridControl1.Model, "C:\MyGC.xls")

{% endhighlight %}
{% endtabs %}

The following assembly files should be added along with the default assembly files in the reference folder: Syncfusion.GridConverter.Base and Syncfusion.XlsIO.Base.

