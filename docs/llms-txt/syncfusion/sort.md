# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/sort.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/sort.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/sort.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/sort.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/sort.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/sort.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/sort.md

# Sorting in ASP.NET Core Spreadsheet control

Sorting helps arranging the data to a specific order in a selected range of cells. You can use the [`allowSorting`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowSorting) property to enable or disable sorting functionality.

N> * The default value for `allowSorting` property is `true`.

By default, the `sort` module is injected internally into Spreadsheet to perform sorting.

## Sort by cell value

In the active Spreadsheet, select a range of cells to sort by cell value. The range sort can be done by any of the following ways:
* Select the sort item in the Ribbon toolbar and choose the ascending or descending item.
* Right-click the sheet, select the sort item in the context menu and choose the ascending/descending item.
* Use the `sort()` method programmatically.

The cell values can be sorted in the following orders:
* Ascending
* Descending

N> * Ascending is the default order for sorting.

The `sort()` method with empty arguments will sort the selected range by active cellâs column as sort column in ascending order.

N> * The `beforeSort` event will be triggered before sorting the specified range.
<br/> * The `sortComplete` event will be triggered after the sort action is completed successfully.

The following code example shows `sort` functionality in the Spreadsheet control.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" allowSorting="true" dataBound="dataBound" beforeSort="beforeSort" sortComplete="sortComplete">
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
            spreadsheetObj.sort({ containsHeader: true }, 'A1:F15');
        }
    }

    function beforeSort(args) {
        //code here to handle sorting arguments.
    }
    function sortComplete(args) {
        spreadsheet.selectRange(args.range);
        // code here.
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="SortController.cs" %}
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



## Data contains header

You can specify whether the selected range of cells contains header. To specify, you need to set the `containsHeader` property to `true` and pass it as `sortOption` arguments of the sort() method.

N> * If the `containsHeader` property is not set and active cell columnâs first cell value type is differed from the second cell value type, the first row data in the range are marked as column headers.

You can also enable or disable this property using `beforeSort` event arguments,

```javascript

   function beforeSort(args) {
        args.sortOptions.containsHeader = true;
    }
```

In the custom sort dialog, the `Data contains header` checkbox is checked on load. Thus, the default value for `containsHeader` is `true` in custom sort dialog.

## Case sensitive sort

The default sort functionality of Spreadsheet is a case insensitive sorting. When you want to perform sorting with case sensitive, you need to set the `caseSensitive` property to `true` and pass it as `sortOption` arguments of the sort() method.

Case sensitive sorting is applicable only for cells with alphabets. In ascending order sorting with case sensitive enabled, the cells with lower case text will be placed above the cells with upper case text.

N> * The default value for the `caseSensitive` property is `false`.

You can also enable or disable this property using `beforeSort` event arguments,

```javascript

    function beforeSort (args) {
        args.sortOptions.caseSensitive = true;
    }

```

In the custom sort dialog, the `Case sensitive` checkbox is unchecked on load as the default value is `false`.

## Sort multiple columns

When you want to perform sorting on multiple columns, it can be done by any of the following ways:
* Select the `Custom sortâ¦` menu item from the Ribbon toolbar item or context menu item.
* Use the `sort()` method programmatically by providing sort criteria.

N> * The current sorting functionality supports sorting based on cell values only.

### Custom sort dialog

The custom sort dialog helps sorting multiple columns in the selected range by utilizing the rich UI. This dialog will be appeared while choosing the `Custom sortâ¦` from the Ribbon item or context menu item. By default, sort criteria with the first column name from the selected range will be appeared in the dialog on initial load and it cannot be removed.

You can add multiple criteria using the `Add Column` button at the bottom of the dialog. Thus, multiple columns can be specified with different sort order. The newly added sort criteria items can be removed using the `delete` icons at the end of each items.

You can refer to the [`Data contains header`](https://ej2.syncfusion.com/aspnetmvc/documentation/spreadsheet/sort#data-contains-header) topic to learn more about `Data contains header` checkbox. To learn more about `Case sensitive` checkbox, you can refer to [`Case sensitive sort`](https://ej2.syncfusion.com/aspnetmvc/documentation/spreadsheet/sort#case-sensitive-sort) topic.

### Passing sort criteria manually

The multi-column sorting can also be performed manually by passing sort options to the `sort()` method programmatically. The `sortOption` have the following arguments:
* `sortDescriptors` â Sort criteria collection that holds the collection of field name, sort order, and `sortComparer`.
* `containsHeader` â Boolean argument that specifies whether the range has headers in it.
* `caseSensitive` â Boolean argument that specifies whether the range needs to consider case.

N> * All the arguments are optional.
<br/> * When a `sortDescriptor` is specified without field, the field of the first `sortDescriptor` from the collection will be assigned from active cellâs column name and others will be ignored. Hence, it will act as single column sorting.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" allowSorting="true" dataBound="dataBound" beforeSort="beforeSort" sortComplete="sortComplete">
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
        var sortDescriptors = [{
            field: 'A',
            order: 'Ascending'
        },
        {
            field: 'B',
            order: 'Ascending'
        },
        {
            field: 'C',
            order: 'Descending'
        }];
        if (spreadsheetObj.activeSheetIndex === 0) {
            spreadsheetObj.sort({ sortDescriptors: sortDescriptors, containsHeader: true }, 'A1:F15');
        }
    }

    function beforeSort(args) {
        //code here to handle sorting arguments.
    }
    function sortComplete(args) {
        spreadsheet.selectRange(args.range);
        // code here.
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="PassingSortController.cs" %}
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



## Custom sort comparer

The `sortDescriptor` holds the `sortComparer` property, which is a function and it is used to customize the sort comparer for specific sort criteria. Each `sortDescriptor` can be customized using the custom sort comparer function.

By customizing sort comparer, you can define the sort action as desired.

N> * The `sortComparer` is an optional property of `sortDescriptor`.

For custom sort comparer example, refer to the [`Sort a range by custom list`] below section.

### Sort a range by custom list

You can also define the sorting of cell values based on your own customized personal list. In this article, custom list is achieved using `custom sort comparer`.

In the following demo, the `Trustworthiness` column is sorted based on the custom lists `Perfect`, `Sufficient`, and `Insufficient`.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" allowSorting="true" dataBound="dataBound" sortComplete="sortComplete">
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
            spreadsheetObj.sort({ sortDescriptors: { field: 'C', sortComparer: mySortComparer }, containsHeader: true }, 'A1:H20');
        }
    }
    function sortComplete(args) {
        spreadsheet.selectRange(args.range);
        // code here.
    }
    // custom sort comparer to sort based on the custom list.
    var customList = ['Pink', 'Aquamarine', 'Blue'];
    function mySortComparer(x, y) {
        var comparer = ej.data.DataUtil.fnSort('Ascending');
        return comparer(x ? customList.indexOf(x.value) : x, y ? customList.indexOf(y.value) : y);
    };

</script>
{% endhighlight %}
{% highlight c# tabtitle="CustomSortController.cs" %}
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

## Known error validations

The following errors have been handled for sorting,
* *Out of range validation:* When the selected range is not a used range of the active sheet, it is considered as invalid and the out of range alert with the message `Select a cell or range inside the used range and try again` will be displayed. No sort will be performed if the range is invalid.

* *Empty field validation:* When the sort criteria does not have a column selected (empty) in the custom sort dialog, it will become invalid, and an error message `Sort criteria column should not be empty` will be displayed on `OK` button click.

* *Duplicate field validation:* When the column names of added sort criteria are repeated more than once in the custom sort dialog, it will become invalid and an error message `<Column name> is mentioned more than once. Duplicate columns must be removed` will be displayed on `OK` button click.

## Limitations

* Sorting is not supported with formula contained cells.

## See Also

* [Hyperlink](./link)
* [Filtering](./filter)
* [Undo Redo](./undo-redo)