# Source: https://docs.syncfusion.com/document-processing/excel/excel-library/net/faqs/how-to-get-the-file-extension-of-excel-file.md

# How to get the file extension of an Excel file using XlsIO?

When an Excel file is opened with XlsIO, you can obtain its full path and extension from the [WorkbookImpl.FullFileName](https://help.syncfusion.com/cr/document-processing/Syncfusion.XlsIO.Implementation.WorkbookImpl.html#Syncfusion_XlsIO_Implementation_WorkbookImpl_FullFileName) property. The following code snippet illustrates this.

{% tabs %}  
{% highlight c# tabtitle="C# [Cross-platform]" %}
using (ExcelEngine excelEngine = new ExcelEngine())
{
    IApplication application = excelEngine.Excel;
    IWorkbook workbook = application.Workbooks.Open("Sample.xlsx");
    
    string fileName = (workbook as WorkbookImpl).FullFileName;
    
    // Display file extension of excel file
    Console.WriteLine(Path.GetExtension(fileName));
}
{% endhighlight %}

{% highlight c# tabtitle="C# [Windows-specific]" %}
using (ExcelEngine excelEngine = new ExcelEngine())
{
    IApplication application = excelEngine.Excel;
    IWorkbook workbook = application.Workbooks.Open("Sample.xlsx");
    
    string fileName = (workbook as WorkbookImpl).FullFileName;
    
    // Display file extension of excel file
    Console.WriteLine(Path.GetExtension(fileName));
}
{% endhighlight %}

{% highlight vb.net tabtitle="VB.NET [Windows-specific]" %}
Using excelEngine As New ExcelEngine()
    Dim application As IApplication = excelEngine.Excel
    Dim workbook As IWorkbook = application.Workbooks.Open("Sample.xlsx")

    Dim fileName As String = CType(workbook, WorkbookImpl).FullFileName
    
    ' Display file extension of excel file
    Console.WriteLine(Path.GetExtension(fileName))
End Using
{% endhighlight %}
{% endtabs %}  

