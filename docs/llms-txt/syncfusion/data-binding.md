# Source: https://docs.syncfusion.com/flutter/datagrid/data-binding.md

# Source: https://docs.syncfusion.com/uwp/treegrid/data-binding.md

# Source: https://docs.syncfusion.com/uwp/map/data-binding.md

# Source: https://docs.syncfusion.com/uwp/datagrid/data-binding.md

# Source: https://docs.syncfusion.com/winui/treeview/data-binding.md

# Source: https://docs.syncfusion.com/winui/treegrid/data-binding.md

# Source: https://docs.syncfusion.com/winui/datagrid/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/treeview/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/pivot-grid/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/pivot-chart/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/classic/multiselectioncombobox/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/multicolumn-treeview/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/multicolumn-combobox/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/grouping/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/data-binding.md

# Source: https://docs.syncfusion.com/windowsforms/diagram/data-binding.md

# Source: https://docs.syncfusion.com/wpf/classic/griddata/data-binding.md

# Source: https://docs.syncfusion.com/wpf/classic/chart/data-binding.md

# Source: https://docs.syncfusion.com/wpf/classic/autocomplete/data-binding.md

# Source: https://docs.syncfusion.com/wpf/treegrid/data-binding.md

# Source: https://docs.syncfusion.com/wpf/tab-navigation/data-binding.md

# Source: https://docs.syncfusion.com/wpf/split-button/data-binding.md

# Source: https://docs.syncfusion.com/wpf/pivot-grid/data-binding.md

# Source: https://docs.syncfusion.com/wpf/olap-gauge/data-binding.md

# Source: https://docs.syncfusion.com/wpf/olap-client/data-binding.md

# Source: https://docs.syncfusion.com/wpf/olap-chart/data-binding.md

# Source: https://docs.syncfusion.com/wpf/multi-column-dropdown/data-binding.md

# Source: https://docs.syncfusion.com/wpf/menu/data-binding.md

# Source: https://docs.syncfusion.com/wpf/grouping/data-binding.md

# Source: https://docs.syncfusion.com/wpf/navigation-pane/data-binding.md

# Source: https://docs.syncfusion.com/wpf/gantt/data-binding.md

# Source: https://docs.syncfusion.com/wpf/dropdown-button/data-binding.md

# Source: https://docs.syncfusion.com/wpf/docking/data-binding.md

# Source: https://docs.syncfusion.com/wpf/datagrid/data-binding.md

# Source: https://docs.syncfusion.com/wpf/step-progressbar/data-binding.md

# Source: https://docs.syncfusion.com/wpf/surface-chart/data-binding.md

# Source: https://docs.syncfusion.com/maui/datagrid/data-binding.md

# Source: https://docs.syncfusion.com/maui/chat/data-binding.md

# Source: https://docs.syncfusion.com/maui/aiassistview/data-binding.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/data-binding.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/data-binding.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/data-binding.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/data-binding.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/data-binding.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/data-binding.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/data-binding.md

# Data Binding in ASP.NET Core Spreadsheet Control

The Spreadsheet uses `DataManager`, which supports both RESTful JSON data services and local JavaScript object array binding to a range. The `dataSource` property can be assigned either with the instance of `DataManager` or JavaScript object array collection.

N> To bind data to a cell, use `cell data binding` support.

## Local data

To bind local data to the Spreadsheet, you can assign a JavaScript object array to the `dataSource` property.

Refer to the following code example for local data binding.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet>
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>
{% endhighlight %}
{% highlight c# tabtitle="LocalDataController.cs" %}
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



N> The local data source can also be provided as an instance of the `DataManager`. By default, `DataManager` uses `JsonAdaptor` for local data-binding.

### Customizing column data mapping

By default, when a data source is bound to a sheet, columns are auto-assigned from the data source fields sequentially. This means that the first field in the data source is assigned to Column A, the second to Column B, and so on, sequentially. However, now you can customize the column assignments by specifying the appropriate field names in the desired order using the `fieldsOrder` property.

> You can customize the mapping of column data only in the local data binding support.

The following code example demonstrates how to customize the mapping of column data:

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" openUrl="Home/Open" saveUrl="Home/Save">
            <e-spreadsheet-sheets>
                <e-spreadsheet-sheet name="Price Details">
                    <e-spreadsheet-ranges>
                        <e-spreadsheet-range dataSource="ViewBag.DefaultData" fieldsOrder="ViewBag.Order"></e-spreadsheet-range>
                    </e-spreadsheet-ranges>
                </e-spreadsheet-sheet>
            </e-spreadsheet-sheets>
</ejs-spreadsheet>

{% endhighlight %}
{% highlight c# tabtitle="FieldMappingController.cs" %}
public IActionResult Index()
{
    List<object> defaultData = new List<object>()
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
    ViewBag.DefaultData = defaultData;
    string[] fieldOrder = new string[] { "CustomerName", "PaymentMode", "Model", "Color", "Amount", "DeliveryDate" };
    ViewBag.Order = fieldOrder;
    return View();

}
{% endhighlight %}
{% endtabs %}


## Remote data

To bind remote data to the Spreadsheet control, assign service data as an instance of `DataManager` to the `dataSource` property. To interact with remote data source, provide the service endpoint `url`.

Refer to the following code example for remote data binding.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet name="Shipment Details">
            <e-spreadsheet-ranges>
                <e-spreadsheet-range showFieldAsHeader=false startCell="A2" query="new ej.data.Query().select(['OrderID', 'CustomerID', 'ShipName', 'ShipCity', 'ShipCountry', 'Freight']).take(200)">
                    <e-data-manager url="https://services.syncfusion.com/js/production/api/Orders" crossdomain=true></e-data-manager>
                </e-spreadsheet-range>
            </e-spreadsheet-ranges>
            <e-spreadsheet-rows>
                <e-spreadsheet-row>
                    <e-spreadsheet-cells>
                        <e-spreadsheet-cell value="Order ID"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Customer Name"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Freight"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Ship Name"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Ship City"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Ship Country"></e-spreadsheet-cell>
                    </e-spreadsheet-cells>
                </e-spreadsheet-row>
            </e-spreadsheet-rows>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>
{% endhighlight %}
{% highlight c# tabtitle="RemoteDataController.cs" %}
public IActionResult Index()
{
    return View();
}
{% endhighlight %}
{% endtabs %}



N> By default, `DataManager` uses **ODataAdaptor** for remote data-binding.

### Binding with OData services

`OData` is a standardized protocol for creating and consuming data. You can retrieve data from OData service using the DataManager. Refer to the following code example for remote Data binding using OData service.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet name="Order Details" created="created">
            <e-spreadsheet-ranges>
                <e-spreadsheet-range>
                    <e-data-manager url="https://ej2services.syncfusion.com/production/web-services/api/Orders" adaptor="ODataAdaptor" crossdomain="true"></e-data-manager>
                </e-spreadsheet-range>
            </e-spreadsheet-ranges>
            <e-spreadsheet-columns>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="280"></e-spreadsheet-column>
                    <e-spreadsheet-column width="180"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="180"></e-spreadsheet-column>
                    <e-spreadsheet-column width="180"></e-spreadsheet-column>
                </e-spreadsheet-columns>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

  <script>

    function dataBound() {
        var spreadsheetObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        //Applies cell and number formatting to specified range of the active sheet
        spreadsheetObj.cellFormat({ fontWeight: 'bold', textAlign: 'center', verticalAlign: 'middle' },
      'A1:K1');
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="ODataController.cs" %}
public IActionResult Index()
{
    return View();
}
{% endhighlight %}
{% endtabs %}



### Web API

You can use WebApiAdaptor to bind spreadsheet with Web API created using OData endpoint.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet name="Order Details" created="created">
            <e-spreadsheet-ranges>
                <e-spreadsheet-range>
                    <e-data-manager url="https://ej2services.syncfusion.com/production/web-services/api/Orders" adaptor="WebApiAdaptor" crossdomain="true"></e-data-manager>
                </e-spreadsheet-range>
            </e-spreadsheet-ranges>
            <e-spreadsheet-columns>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="280"></e-spreadsheet-column>
                    <e-spreadsheet-column width="180"></e-spreadsheet-column>
                    <e-spreadsheet-column width="80"></e-spreadsheet-column>
                    <e-spreadsheet-column width="180"></e-spreadsheet-column>
                    <e-spreadsheet-column width="180"></e-spreadsheet-column>
                </e-spreadsheet-columns>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

  <script>

    function dataBound() {
        var spreadsheetObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        //Applies cell and number formatting to specified range of the active sheet
        spreadsheetObj.cellFormat({ fontWeight: 'bold', textAlign: 'center', verticalAlign: 'middle' },
      'A1:K1');
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="WebApiController.cs" %}
public IActionResult Index()
{
    return View();
}
{% endhighlight %}
{% endtabs %}



## Cell data binding

The Spreadsheet control can bind the data to individual cell in a sheet . To achieve this you can use the `value` property.

Refer to the following code example for cell data binding.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet">
<e-spreadsheet-sheets>
    <e-spreadsheet-sheet name="Monthly Budget" selectedRange="D13">
        <e-spreadsheet-rows>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="Category">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Planned cost">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Actual cost">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="Food"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$7000"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$8120"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="Loan"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$1500"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$1500"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="Medical"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$300"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$0"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="Clothing"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$400"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$140"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="Education"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$900"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="$750"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
        </e-spreadsheet-rows>
    </e-spreadsheet-sheet>
</e-spreadsheet-sheets>
</ejs-spreadsheet>
{% endhighlight %}
{% highlight c# tabtitle="CellDataController.cs" %}
public IActionResult Index()
{
    return View();
}
{% endhighlight %}
{% endtabs %}



N> The cell data binding also supports formula, style, number format, and more.

## Dynamic data binding and Datasource change event

You can dynamically change the datasource of the spreadsheet by changing the `dataSource` property of the `range` object of the `sheet`. The `dataSourceChanged` event handler will be triggered when editing, inserting, and deleting a row in the datasource range. This event will be triggered with a parameter named `action` which indicates the `edit`, `add` and `delete` actions for the respective ones.

The following table defines the arguments of the `dataSourceChanged` event.

| Property | Type | Description |
|-----|-----|-------|
| action | string | Indicates the type of action such as `edit`, `add`, and `delete` performed in the datasource range. |
| data | object[] | Modified data for `edit` action; New data for `add` action; Deleted data for `delete` action. |
| rangeIndex | number | Specifies the range index of the datasource. |
| sheetIndex | number | Specifies the sheet index of the datasource. |

N> For `add` action, the value for all the fields will be `null` in the data. In the case that you do not want the primary key field to be null which needs to be updated in the backend service, you can use `edit` action after updating the primary key field to update in the backend service. <br><br>
<br/> For inserting a row at the end of the datasource range, you should insert a row below at the end of the range to trigger the `dataSourceChanged` event with action `add`.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div>
    <button id="changeDataBtn" class='e-btn'>Change Datasource</button>
</div>
<ejs-spreadsheet id="spreadsheet" dataSourceChanged="dataSourceChanged">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet>
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>
<div>
    <h4><b>Event Trace</b></h4>
    <div id="evt">
        <div style="height:173px;overflow: auto;min-width: 250px;">
            <span id="EventLog" style="word-break: normal;"></span>
        </div>
        <button id="clearBtn" class='e-btn'>Clear</button>
    </div>
</div>

<script>

    document.getElementById('changeDataBtn').addEventListener('click', () => {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        var itemData = [
            {
                'Item Name': 'Casual Shoes',
                'Date': '02/14/2019',
                'Time': '11:34:32 AM',
                'Quantity': 10,
                'Price': 20,
                'Amount': '=D2*E2',
                'Discount': 1,
                'Profit': 10
            },
            {
                'Item Name': 'Sports Shoes',
                'Date': '06/11/2019',
                'Time': '05:56:32 AM',
                'Quantity': 20,
                'Price': 30,
                'Amount': '=D3*E3',
                'Discount': 5,
                'Profit': 50
            } 
        ];
        spreadsheet.sheets[0].ranges[0].dataSource = itemData;
    });

    document.getElementById('clearBtn').addEventListener('click', () => {
        document.getElementById('EventLog').innerHTML = "";
    });

    function appendElement(html) {
        var span = document.createElement("span");
        span.innerHTML = html;
        var log = document.getElementById('EventLog');
        log.insertBefore(span, log.firstChild);
    }

    function dataSourceChanged(args) {
        appendElement("Data source changed with" + "<b>&nbsp;" + args.action + "</b> action<hr>"
        );
    }

</script>

<style>
    #changeDataBtn {
        margin-bottom: 10px;
    }
    
    #EventLog b {
        color: #388e3c;
    }

    #evt {
        border: 1px solid #dcdcdc;
        padding: 10px;
    }

    hr {
        margin-top: 0;
        margin-bottom: 0;
    }
</style>

{% endhighlight %}
{% highlight c# tabtitle="DynamicDataController.cs" %}
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

## Dynamic data binding using updateRange method

The `updateRange` method allows you to dynamically update the `dataSource` in a spreadsheet without manually iterating through each cell. This method is especially useful for efficiently applying bulk updates to a specific range within the spreadsheet.

To use the `updateRange` method, provide the new `dataSource` and specify the starting cell for the update using the `startCell` property of the `RangeModel`. Additionally, set the `sheetIndex` to target the appropriate sheet for the update.

The following code example demonstrates how to dynamically update data using the `updateRange` method.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="updateDynamicData" content="Update Dynamic Data"></ejs-button>
<ejs-spreadsheet id="spreadsheet">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet>
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>


    document.getElementById("updateDynamicData").addEventListener('click', function () {
        var spreadsheet = document.getElementById("spreadsheet").ej2_instances[0];
        var newDataCollection = {
            dataSource: [
                {
                    'Payment Mode': 'Debit Card',
                    'Delivery Date': '07/11/2015',
                    'Amount': '8529.22',
                },
                {
                    'Payment Mode': 'Cash On Delivery',
                    'Delivery Date': '7/13/2016',
                    'Amount': '17866.19',
                },
                {
                    'Payment Mode': 'Net Banking',
                    'Delivery Date': '09/04/2015',
                    'Amount': '13853.09',
                },
                {
                    'Payment Mode': 'Credit Card',
                    'Delivery Date': '12/15/2017',
                    'Amount': '2338.74',
                },
                {
                    'Payment Mode': 'Credit Card',
                    'Delivery Date': '10/08/2014',
                    'Amount': '9578.45',
                },
                {
                    'Payment Mode': 'Cash On Delivery',
                    'Delivery Date': '7/01/2017',
                    'Amount': '19141.62',
                },
                {
                    'Payment Mode': 'Credit Card',
                    'Delivery Date': '12/20/2015',
                    'Amount': '6543.30',
                },
                {
                    'Payment Mode': 'Credit Card',
                    'Delivery Date': '11/24/2014',
                    'Amount': '13035.06',
                },
                {
                    'Payment Mode': 'Debit Card',
                    'Delivery Date': '05/12/2014',
                    'Amount': '18488.80',
                },
                {
                    'Payment Mode': 'Net Banking',
                    'Delivery Date': '12/30/2014',
                    'Amount': '12317.04',
                },
                {
                    'Payment Mode': 'Credit Card',
                    'Delivery Date': '12/18/2013',
                    'Amount': '6230.13',
                },
                {
                    'Payment Mode': 'Cash On Delivery',
                    'Delivery Date': '02/02/2015',
                    'Amount': '9709.49',
                },
                {
                    'Payment Mode': 'Debit Card',
                    'Delivery Date': '11/19/2014',
                    'Amount': '9766.10',
                },
                {
                    'Payment Mode': 'Net Banking',
                    'Delivery Date': '02/08/2014',
                    'Amount': '7685.49',
                },
                {
                    'Payment Mode': 'Debit Card',
                    'Delivery Date': '08/05/2016',
                    'Amount': '18012.45',
                },
                {
                    'Payment Mode': 'Credit Card',
                    'Delivery Date': '05/30/2016',
                    'Amount': '2785.49',
                },
                {
                    'Payment Mode': 'Debit Card',
                    'Delivery Date': '12/10/2016',
                    'Amount': '9967.74',
                },
            ],
            startCell: 'D1',
        };
        spreadsheet.updateRange(newDataCollection, 0);
    });

</script>
{% endhighlight %}
{% highlight c# tabtitle="UpdateRangeController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { CustomerName= "Romona Heaslip",  Model= "Taurus",  Color= "Aquamarine"},
        new { CustomerName= "Clare Batterton",  Model= "Sparrow",  Color= "Pink"},
        new { CustomerName= "Eamon Traise",  Model= "Grand Cherokee",  Color= "Blue" },
        new { CustomerName= "Julius Gorner",  Model= "GTO",  Color= "Aquamarine" },
        new { CustomerName= "Jenna Schoolfield",  Model= "LX",  Color= "Yellow" },
        new { CustomerName= "Marylynne Harring",  Model= "Catera",  Color= "Pink"},
        new { CustomerName= "Vilhelmina Leipelt",  Model= "7 Series",  Color= "Goldenrod"},
        new { CustomerName= "Barby Heisler",  Model= "Corvette",  Color= "Red"},
        new { CustomerName= "Karyn Boik",  Model= "Regal",  Color= "Pink"},
        new { CustomerName= "Jeanette Pamplin",  Model= "S4",  Color= "Fuscia"},
        new { CustomerName= "Cristi Espinos",  Model= "TL",  Color= "Aquamarine"},
        new { CustomerName= "Issy Humm",  Model= "Club Wagon",  Color= "Pink" },
        new { CustomerName= "Tuesday Fautly",  Model= "V8 Vantage",  Color= "Crimson"},
        new { CustomerName= "Rosemaria Thomann",  Model= "Caravan",  Color= "Violet"},
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}

## See Also

* [Filtering](filter)
* [Sorting](sort)
* [Hyperlink](link)