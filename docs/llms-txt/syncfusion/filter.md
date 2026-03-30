# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/filter.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/filter.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/filter.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/filter.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/filter.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/filter.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/filter.md

# Filtering in ASP.NET Core Spreadsheet control

Filtering helps you to view specific rows in the spreadsheet by hiding the other rows. You can use the [`allowFiltering`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowFiltering) property to enable or disable filtering functionality.

N> * The default value for `allowFiltering` property is `true`.

By default, the `filter` module is injected internally into Spreadsheet to perform filtering.

## Apply filter on UI

In the active Spreadsheet, select a range of cells to filter by value of the cell. The filtering can be done by any of the following ways:

* Select the filter item in the Ribbon toolbar.
* Right-click the sheet, select the filter item in the context menu.
* Use the `applyFilter()` method programmatically.
* Use `Ctrl + Shift + L` keyboard shortcut to apply the filter.

N> * Use `Alt + Up/Down` keyboard shortcut to open the filter dialog.

## Filter by criteria

The `applyFilter()` method will apply the filter UI, based on the predicate and range given in the arguments.

N> * The `beforeFilter` event will be triggered before filtering the specified range.
<br/> * The `filterComplete` event will be triggered after the filter action is completed successfully.

The following code example shows `filter` functionality in the Spreadsheet control.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" allowFiltering="true" dataBound="dataBound">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet>
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>

function dataBound() {
    var spreadsheetObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
    if (spreadsheetObj.activeSheetIndex === 0) {
        var colors = ['Pink', 'Aquamarine', 'Blue'];
        var predicateList = []
        colors.forEach((color) => { predicateList.push({ field: 'C', predicate: 'or', operator: 'equal', value: color }); })
        spreadsheetObj.applyFilter(predicateList);
    }
}

</script>
{% endhighlight %}
{% highlight c# tabtitle="FilterController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { CustomerName= "Romona Heaslip",  Model= "Taurus",  Color= "Aquamarine",  PaymentMode= "Debit Card",  DeliveryDate= "07/11/2015",  Amount= "8529.22" },
        new { CustomerName= "Clare Batterton",  Model= "Sparrow",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/13/2016",  Amount= "17866.19" },
        new { CustomerName= "Eamon Traise",  Model= "Grand Cherokee",  Color= "Blue",  PaymentMode= "Net Banking",  DeliveryDate= "09/04/2015",  Amount= "13853.09" },
        new { CustomerName= "Julius Gorner",  Model= "GTO",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/15/2017",  Amount= "2338.74" },
        new { CustomerName= "Jenna Schoolfield",  Model= "LX",  Color= "Yellow",  PaymentMode= "Credit Card",  DeliveryDate= "10/08/2014",  Amount= "9578.45" },
        new { CustomerName= "Marylynne Harring",  Model= "Catera",  Color= "Green",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/01/2017",  Amount= "19141.62" },
        new { CustomerName= "Vilhelmina Leipelt",  Model= "7 Series",  Color= "Goldenrod",  PaymentMode= "Credit Card",  DeliveryDate= "12/20/2015",  Amount= "6543.30" },
        new { CustomerName= "Barby Heisler",  Model= "Corvette",  Color= "Red",  PaymentMode= "Credit Card",  DeliveryDate= "11/24/2014",  Amount= "13035.06" },
        new { CustomerName= "Karyn Boik",  Model= "Regal",  Color= "Indigo",  PaymentMode= "Debit Card",  DeliveryDate= "05/12/2014",  Amount= "18488.80" },
        new { CustomerName= "Jeanette Pamplin",  Model= "S4",  Color= "Fuscia",  PaymentMode= "Net Banking",  DeliveryDate= "12/30/2014",  Amount= "12317.04" },
        new { CustomerName= "Cristi Espinos",  Model= "TL",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/18/2013",  Amount= "6230.13" },
        new { CustomerName= "Issy Humm",  Model= "Club Wagon",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "02/02/2015",  Amount= "9709.49" },
        new { CustomerName= "Tuesday Fautly",  Model= "V8 Vantage",  Color= "Crimson",  PaymentMode= "Debit Card",  DeliveryDate= "11/19/2014",  Amount= "9766.10" },
        new { CustomerName= "Rosemaria Thomann",  Model= "Caravan",  Color= "Violet",  PaymentMode= "Net Banking",  DeliveryDate= "02/08/2014",  Amount= "7685.49" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



## Filter by cell value

To apply a filter for a cell value, right-click the cell and choose filter -> `Filter By Selected Cell's Value` option from the menu. It applies the filter based on the value of the selected cell in the current sheet.

## Clear filter

After applying filter to a certain column, you may want to clear it to make all filtered rows visible again. It can be done in the following ways,

* Choose `Clear` option in ribbon toolbar under `Filter and Sort`. It clears the filters applied in the spreadsheet for all fields.

* Use the `clearFilter()` method programmatically, to clear the applied filters in spreadsheet for all fields.

## Clear filter on a field

After filtering, you can clear/reset the filter for a field alone. It can be done in the following ways,

* Click filter icon in the columnâs header and then choose `Clear Filter` option from the filter dialog.
* You can right-click on a filtered column cell and choose `Clear Filter from <Column Name>.` option from the context menu.
* Use the `clearFilter(field)` method programmatically, to clear the filter in a particular column.

## Reapply filter

When you want to reapply the filter after some changes happened in the rows. It can be done in the following ways,

* You can choose `Reapply` option in ribbon toolbar under `Filter and Sort` to reapply the filtered columns again.
* You can right-click on a filtered cell and choose `Reapply` option from the context menu. It reapplies the filters again in the Spreadsheet for all the fields.

## Known error validations

The following errors have been handled for filtering,
* *Out of range validation:* When the selected range is not a used range of the active sheet, it is considered as invalid and the out of range alert with the message `Select a cell or range inside the used range and try again` will be displayed. No filter will be performed if the range is invalid.

## Get data from filtered rows

Filtering allows you to view specific rows in a spreadsheet while hiding the others. The [allowFiltering](https://help.syncfusion.com/cr/aspnetcore-js2/syncfusion.ej2.spreadsheet.spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowFiltering) property allows you to enable or disable filtering functionality through the UI. You can also use the [allowFiltering](https://help.syncfusion.com/cr/aspnetcore-js2/syncfusion.ej2.spreadsheet.spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowFiltering) property and `applyFilter` method combination to filter data via code behind. The filtered rows can be identified by iterating through the row collection on the sheet and using the `isFiltered` property available in each row object.

The following code example shows how to get the filtered rows.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="getFilterData" content="Get Filtered Data"></ejs-button>
<ejs-spreadsheet id="spreadsheet" allowFiltering="true">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet>
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>


    document.getElementById("getFilterData").addEventListener('click', function () {
        var spreadsheet = document.getElementById("spreadsheet").ej2_instances[0];
        var activeSheet = spreadsheet.getActiveSheet();
        var usedRange = activeSheet.usedRange;
        for (var i = 0; i <= usedRange.rowIndex; i++) {
            // Get the filtered row using isFiltered property.
            var filteredRow = (activeSheet.rows[i]).isFiltered;
            if (!filteredRow) {
                var rowData = spreadsheet.getRowData(i);
                console.log("Row:", i + 1, "Cells", rowData);
            }
        }
    });

</script>
{% endhighlight %}
{% highlight c# tabtitle="InsertSheetController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { CustomerName= "Romona Heaslip",  Model= "Taurus",  Color= "Aquamarine",  PaymentMode= "Debit Card",  DeliveryDate= "07/11/2015",  Amount= "8529.22" },
        new { CustomerName= "Clare Batterton",  Model= "Sparrow",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/13/2016",  Amount= "17866.19" },
        new { CustomerName= "Eamon Traise",  Model= "Grand Cherokee",  Color= "Blue",  PaymentMode= "Net Banking",  DeliveryDate= "09/04/2015",  Amount= "13853.09" },
        new { CustomerName= "Julius Gorner",  Model= "GTO",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/15/2017",  Amount= "2338.74" },
        new { CustomerName= "Jenna Schoolfield",  Model= "LX",  Color= "Yellow",  PaymentMode= "Credit Card",  DeliveryDate= "10/08/2014",  Amount= "9578.45" },
        new { CustomerName= "Marylynne Harring",  Model= "Catera",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/01/2017",  Amount= "19141.62" },
        new { CustomerName= "Vilhelmina Leipelt",  Model= "7 Series",  Color= "Goldenrod",  PaymentMode= "Credit Card",  DeliveryDate= "12/20/2015",  Amount= "6543.30" },
        new { CustomerName= "Barby Heisler",  Model= "Corvette",  Color= "Red",  PaymentMode= "Credit Card",  DeliveryDate= "11/24/2014",  Amount= "13035.06" },
        new { CustomerName= "Karyn Boik",  Model= "Regal",  Color= "Pink",  PaymentMode= "Debit Card",  DeliveryDate= "05/12/2014",  Amount= "18488.80" },
        new { CustomerName= "Jeanette Pamplin",  Model= "S4",  Color= "Fuscia",  PaymentMode= "Net Banking",  DeliveryDate= "12/30/2014",  Amount= "12317.04" },
        new { CustomerName= "Cristi Espinos",  Model= "TL",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/18/2013",  Amount= "6230.13" },
        new { CustomerName= "Issy Humm",  Model= "Club Wagon",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "02/02/2015",  Amount= "9709.49" },
        new { CustomerName= "Tuesday Fautly",  Model= "V8 Vantage",  Color= "Crimson",  PaymentMode= "Debit Card",  DeliveryDate= "11/19/2014",  Amount= "9766.10" },
        new { CustomerName= "Rosemaria Thomann",  Model= "Caravan",  Color= "Violet",  PaymentMode= "Net Banking",  DeliveryDate= "02/08/2014",  Amount= "7685.49" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}

## Limitations

The following features have some limitations in Filter:

* Insert/delete row/column between the filter applied cells.
* Merge cells with filter.
* Copy/cut paste the filter applied cells.

## See Also

* [Sorting](./sort)
* [Hyperlink](./link)
* [Undo Redo](./undo-redo)