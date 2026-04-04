# Source: https://docs.syncfusion.com/document-processing/excel/excel-library/net/faqs/how-to-clear-formats-in-worksheet.md

# How to clear formats in a worksheet using XlsIO?

You can clear all formats in an Excel worksheet by using the ClearFormat option of the [ExcelClearOptions](https://help.syncfusion.com/cr/document-processing/syncfusion.xlsio.excelclearoptions.html) enum on an [IRange](https://help.syncfusion.com/cr/document-processing/Syncfusion.XlsIO.IRange.html) object.

{% tabs %}
{% highlight c# tabtitle="C# [Cross-platform]" %}
// Clear formats in the worksheet
worksheet.UsedRange.Clear(ExcelClearOptions.ClearFormat); 
{% endhighlight %}

{% highlight c# tabtitle="C# [Windows-specific]" %}
// Clear formats in the worksheet
worksheet.UsedRange.Clear(ExcelClearOptions.ClearFormat); 
{% endhighlight %}

{% highlight vb.net tabtitle="VB.NET [Windows-specific]" %}
' Clear formats in the worksheet
worksheet.UsedRange.Clear(ExcelClearOptions.ClearFormat)
{% endhighlight %}
{% endtabs %}

