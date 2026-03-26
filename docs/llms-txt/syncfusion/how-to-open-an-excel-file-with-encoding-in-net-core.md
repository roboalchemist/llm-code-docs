# Source: https://docs.syncfusion.com/document-processing/excel/excel-library/net/faqs/how-to-open-an-excel-file-with-encoding-in-net-core.md

# How to open an Excel file with encoding in .NET Core?

XlsIO do not have direct support to open an Excel file with encoding in .NET Core. But this can be acheived through below workaround.

{% tabs %}
{% highlight c# tabtitle="C# [Cross-platform]" %}
using (ExcelEngine excelEngine = new ExcelEngine())
{
  IApplication application = excelEngine.Excel;

  System.Text.UnicodeEncoding.RegisterProvider(System.Text.CodePagesEncodingProvider.Instance);
  IWorkbook workbook = application.Workbooks.Open("Sample.csv", System.Text.UnicodeEncoding.GetEncoding("big5"));

  workbook.SaveAs("Output.csv", ",");
}

{% endhighlight %}
{% endtabs %}