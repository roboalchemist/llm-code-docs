# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/how-to/change-active-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/how-to/change-active-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/how-to/change-active-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/how-to/change-active-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/how-to/change-active-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/how-to/change-active-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/how-to/change-active-sheet.md

# Changing the active sheet in ASP.NET Core Spreadsheet control

You can change the active sheet of imported file by updating [`activeSheetIndex`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_ActiveSheetIndex) property on the [`openComplete`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_OpenComplete) event.

The following code example shows how to set the active sheet when importing an Excel file.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" openUrl="Open" openComplete="openComplete">

</ejs-spreadsheet>

<script>

    function openComplete(args) {
        var spreadsheetObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        if (spreadsheetObj) {
            spreadsheetObj.activeSheetIndex = 2;
        }
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="OpenController.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}
{% endhighlight %}
{% endtabs %}
