# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/worksheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/worksheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/worksheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/worksheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/blazor/worksheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/worksheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/worksheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/worksheet.md

# Worksheet in ASP.NET Core Spreadsheet control

Worksheet is a collection of cells organized in the form of rows and columns that allows you to store, format, and manipulate the data.

## Add sheet

You can dynamically add or insert a sheet by one of the following ways,

* Click the `Add Sheet` button in the sheet tab. This will add a new empty sheet next to current active sheet.
* Right-click on the sheet tab, and then select `Insert` option from the context menu to insert a new empty sheet before the current active sheet.
* Using `insertSheet`method, you can insert one or more sheets at your desired index.

The following code example shows the insert sheet operation in spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" showRibbon="false" showFormulaBar="false" created="created">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet name="Shipment Details">
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>

            <e-spreadsheet-columns>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="220"></e-spreadsheet-column>
                <e-spreadsheet-column width="90"></e-spreadsheet-column>
                <e-spreadsheet-column width="140"></e-spreadsheet-column>
                <e-spreadsheet-column width="90"></e-spreadsheet-column>
                <e-spreadsheet-column width="100"></e-spreadsheet-column>
                <e-spreadsheet-column width="100"></e-spreadsheet-column>
            </e-spreadsheet-columns>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>

    function created() {
      // Applies style formatting to the active sheet before inserting a new sheet
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:H1');
        this.cellFormat({ textAlign: 'center' }, 'D2:H15');
        // inserting a new sheet with data at 1st index
        // You can also insert empty sheets by specifying the start and end sheet index instead of sheet model
        this.insertSheet([{
            index: 1,
            name: 'Inserted Sheet',
            ranges: [{ dataSource: @Html.Raw(JsonConvert.SerializeObject(@ViewBag.DefaultData)) }],
            columns: [{ width: 150 }, { width: 110 }, { width: 110 }, { width: 85 }, { width: 85 }, { width: 85 }, { width: 85 },
                { width: 85 }]
        }]);
        // Applies style formatting for the inserted sheet
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'Inserted Sheet!A1:H1');
        this.cellFormat({ textAlign: 'center' }, 'Inserted Sheet!D2:H15');
    }

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

### Insert a sheet programmatically and make it active sheet

A sheet is a collection of cells organized in the form of rows and columns that allows you to store, format, and manipulate the data. Using `insertSheet` method, you can insert one or more sheets at the desired index. Then, you can make the inserted sheet as active sheet by focusing the start cell of that sheet using the `goTo` method.

The following code example shows how to insert a sheet programmatically and make it the active sheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="insertSheet" content="Insert Sheet"></ejs-button>
<ejs-spreadsheet id="spreadsheet">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet name="Price Details">
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A1"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
            <e-spreadsheet-columns>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="100"></e-spreadsheet-column>
                <e-spreadsheet-column width="100"></e-spreadsheet-column>
            </e-spreadsheet-columns>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>
    document.getElementById("insertSheet").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        spreadsheetObj.insertSheet(
            [
                {
                    index: 1,
                    name: 'new_sheet',
                    ranges: [
                        {
                            dataSource: ViewBag.ProductData,
                            startCell: 'A1'
                        },
                    ]
                },
            ]
        );
        // Use the timeout function to wait until the sheet is inserted.
        setTimeout(() => {
            // Method for switching to a new sheet.
            spreadsheetObj.goTo('new_sheet!A1');
        })
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="InsertSheetController.cs" %}
public IActionResult Index()
{
    List<object> defaultData = new List<object>()
    {
        new { ItemName= "Casual Shoes", Date= "02/14/2014", Time= "11:34:32 AM", Quantity= "10", Price= "20", Amount= "200", Discount= "1", Profit= "10" },
        new { ItemName= "Sports Shoes", Date= "06/11/2014", Time= "05:56:32 AM", Quantity= "20", Price= "30", Amount= "600", Discount= "5", Profit= "50" },
        new { ItemName= "Formal Shoes", Date= "07/27/2014", Time= "03:32:44 AM", Quantity= "20", Price= "15", Amount= "300", Discount= "7", Profit= "27" },
        new { ItemName= "Sandals & Floaters", Date= "11/21/2014", Time= "06:23:54 AM", Quantity= "15", Price= "20", Amount= "300", Discount= "11", Profit= "67" },
        new { ItemName= "Flip- Flops & Slippers", Date= "06/23/2014", Time= "12:43:59 AM", Quantity= "30", Price= "10", Amount= "300", Discount= "10", Profit= "70" },
        new { ItemName= "Sneakers", Date= "07/22/2014", Time= "10:55:53 AM", Quantity= "40", Price= "20", Amount= "800", Discount= "13", Profit= "66" },
        new { ItemName= "Running Shoes", Date= "02/04/2014", Time= "03:44:34 AM", Quantity= "20", Price= "10", Amount= "200", Discount= "3", Profit= "14" },
        new { ItemName= "Loafers", Date= "11/30/2014", Time= "03:12:52 AM", Quantity= "31", Price= "10", Amount= "310", Discount= "6", Profit= "29" },
        new { ItemName= "Cricket Shoes", Date= "07/09/2014", Time= "11:32:14 AM", Quantity= "41", Price= "30", Amount= "1210", Discount= "12", Profit= "166" },
        new { ItemName= "T-Shirts", Date= "10/31/2014", Time= "12:01:44 AM", Quantity= "50", Price= "10", Amount= "500", Discount= "9", Profit= "55" }
    };
    ViewBag.DefaultData = defaultData;

    List<object> data = new List<object>()
    {
        new { ProductId= "1",  ProductName= "Chai",  SupplierId= "1",  QuantityPerUnit= "10 boxes x 20 bags",  UnitPrice= "18.00",  UnitsInStock= "39",  Discontinued= "false" },
        new { ProductId= "2",  ProductName= "Chang",  SupplierId= "1",  QuantityPerUnit= "24 - 12 oz bottles",  UnitPrice= "19.00",  UnitsInStock= "17",  Discontinued= "true" },
        new { ProductId= "3",  ProductName= "Aniseed Syrup",  SupplierId= "1",  QuantityPerUnit= "12 - 550 ml bottles",  UnitPrice= "10.00",  UnitsInStock= "13",  Discontinued= "false" },
        new { ProductId= "4",  ProductName= "Chef Anton\'s Cajun Seasoning",  SupplierId= "2",  QuantityPerUnit= "48 - 6 oz jars",  UnitPrice= "22.00",  UnitsInStock= "53",  Discontinued= "true" },
        new { ProductId= "5",  ProductName= "Chef Anton\'s Gumbo Mix",  SupplierId= "2",  QuantityPerUnit= "36 boxes', 'Unit Price",  UnitPrice= "21.35",  UnitsInStock= "0",  Discontinued= "true" },
        new { ProductId= "6",  ProductName= "Grandma\'s Boysenberry Spread",  SupplierId= "3",  QuantityPerUnit= "12 - 8 oz jars",  UnitPrice= "25.00",  UnitsInStock= "120",  Discontinued= "false" },
        new { ProductId= "7",  ProductName= "Uncle Bob\'s Organic Dried Pears",  SupplierId= "3",  QuantityPerUnit= "12 - 1 lb pkgs.",  UnitPrice= "30.00",  UnitsInStock= "15",  Discontinued= "true" },
        new { ProductId= "10",  ProductName= "Queso Cabrales",  SupplierId= "5",  QuantityPerUnit= "1 kg pkg.",  UnitPrice= "21.00",  UnitsInStock= "22",  Discontinued= "false" },
    };
    ViewBag.ProductData = data;
    return View();

}
{% endhighlight %}
{% endtabs %}


## Delete sheet

The Spreadsheet has support for removing an existing worksheet. You can dynamically delete the existing sheet by the following way,

* Right-click on the sheet tab, and then select `Delete` option from context menu.
* Using `delete` method to delete the sheets.

## Rename sheet

You can dynamically rename an existing worksheet in the following way,

* Right-click on the sheet tab, and then select `Rename` option from the context menu.

## Headers

By default, the row and column headers are visible in worksheets. You can dynamically show or hide worksheet headers by using one of the following ways,

* Switch to `View` tab, and then select `Hide Headers` option to hide both the row and column headers.
* Set `showHeaders` property in `sheets` as `true` or `false` to show or hide the headers at initial load. By default, the `showHeaders` property is enabled in each worksheet.

## Gridlines

Gridlines act as a border like appearance of cells. They are used to distinguish cells on the worksheet. You can dynamically show or hide gridlines by using one of the following ways,

* Switch to `View` tab, and then select `Hide Gridlines` option to hide the gridlines in worksheet.
* Set `showGridLines` property in `sheets` as `true` or `false` to show or hide the gridlines at initial load. By default, the `showGridLines` property is enabled in each worksheet.

The following code example shows the headers and gridlines operation in spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" showRibbon="false" showFormulaBar="false" created="created">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet name="Shipment Details" showGridLines="false" showHeaders="false">
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>

            <e-spreadsheet-columns>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="220"></e-spreadsheet-column>
                <e-spreadsheet-column width="90"></e-spreadsheet-column>
                <e-spreadsheet-column width="140"></e-spreadsheet-column>
                <e-spreadsheet-column width="90"></e-spreadsheet-column>
                <e-spreadsheet-column width="100"></e-spreadsheet-column>
                <e-spreadsheet-column width="100"></e-spreadsheet-column>
            </e-spreadsheet-columns>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>

     function created() {
       this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:H1');
        this.cellFormat({ textAlign: 'center' }, 'D2:H15');
        // The gridlines have been removed to set border for the range of cells
        this.setBorder({ border: '1px solid #e0e0e0' }, 'A1:H15');
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="HeaderController.cs" %}
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

## Sheet visibility

Hiding a worksheet can help prevent unauthorized or accidental changes to your file.

There are three visibility state as like Microsoft Excel,

| State | Description |
|-------|---------|
| `Visible` | You can see the worksheet once the component is loaded. |
| `Hidden` | This worksheet is not visible, but you can unhide by selecting the sheet from `List All Sheets`
dropdown menu. |
| `VeryHidden` | This worksheet is not visible and cannot be unhidden. Changing the
state property to `Visible` is the only way to view this sheet. |

The following code example shows the three types of sheet visibility state.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
 <ejs-spreadsheet id="spreadsheet" showFormulaBar="false" created="created">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet name="Visible Sheet" state="Visible">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="130"></e-spreadsheet-column>
                    <e-spreadsheet-column width="220"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        
            <e-spreadsheet-sheet name="Very Hidden Sheet" state="VeryHidden">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="130"></e-spreadsheet-column>
                    <e-spreadsheet-column width="220"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
            <e-spreadsheet-sheet name="Hidden Sheet" state="Hidden">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="130"></e-spreadsheet-column>
                    <e-spreadsheet-column width="220"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>

<script>
     function created() {
      // Applies style formatting to active visible sheet
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:H1');
        this.cellFormat({ textAlign: 'center' }, 'D2:F15');
        // Applies style formatting to active hidden sheet
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'Hidden Sheet!A1:H1');
        this.cellFormat({ textAlign: 'center' }, 'Hidden Sheet!D2:F15');
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="SheetVisiblityController.cs" %}
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



## See Also

* [Sheet protection](./protect-sheet)
* [Rows and columns](./rows-and-columns)
* [Cell range](./cell-range)
* [Formatting](./formatting)
