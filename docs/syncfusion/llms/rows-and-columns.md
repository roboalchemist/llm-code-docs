# Source: https://docs.syncfusion.com/uwp/cellgrid/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/wpf/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/winforms/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/uwp/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/blazor/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/rows-and-columns.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/rows-and-columns.md

# Rows and columns in ASP.NET Core Spreadsheet control

Spreadsheet is a tabular format consisting of rows and columns. The intersection point of rows and columns are called as cells. The list of operations that you can perform in rows and columns are,

* Insert
* Delete
* Show and Hide

## Insert

You can insert rows or columns anywhere in a spreadsheet. Use the [`allowInsert`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowInsert) property to enable or disable the insert option in Spreadsheet.

### Row

The rows can be inserted in the following ways,

* Using `insertRow` method, you can insert the rows once the component is loaded.
* Using context menu, insert the empty rows in the desired position.

The following code example shows the options for inserting rows in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
 <ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false" showSheetTabs="false" showRibbon="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="B1"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="20"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
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
            // Rows model that is going to insert dynamically
            var rowsModel = [{
                index: 9, // Need to specify the index for the first row collection, the specified rows will be inserted in this index.
                cells: [{ value: '' }, { value: '8' }, { value: 'Northwoods Cranberry Sauce' }, { value: '3' }, { value: '12 - 12 oz jars' },
                { value: '40.00' }, { value: '6' }, { value: 'false' }]
            },
            {
                cells: [{ value: '' }, { value: '9' }, { value: 'Mishi Kobe Niku' }, { value: '4' }, { value: '18 - 500 g pkgs.' }, { value: '97.00' }, { value: '29' }, { value: 'true' }]
            }];
            // Applies style formatting before inserting the rows
            this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'B1:H1');
            // inserting a empty row at 0th index
            this.insertRow();
            // inserting 2 rows at the 9th index with data
            this.insertRow(rowsModel);
            // Applies style formatting after the rows are inserted
            this.cellFormat({ textAlign: 'center' }, 'B3:B12');
            this.cellFormat({ textAlign: 'center' }, 'D3:D12');
            this.cellFormat({ textAlign: 'center' }, 'F3:H12');
        }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="InsertRowController.cs" %}
public IActionResult Index()
{
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
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



### Column

The columns can be inserted in the following ways,

* Using `insertColumn` method, you can insert the columns once the component is loaded.
* Using context menu, insert the empty columns in the desired position.

The following code example shows the options for inserting columns in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
    <ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false" showSheetTabs="false" showRibbon="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A2"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
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
        // Cells model that you are going to update in the inserted 5th column dynamically
        var cellsModel = [{ value: 'UnitPrice', style: { fontWeight: 'bold', textAlign: 'center' } }, { value: '18.00' },
        { value: '19.00' }, { value: '10.00' }, { value: '22.00' }, { value: '21.35' }, { value: '25.00' }, { value: '30.00' },
        { value: '21.00' }, { value: '40.00' }, { value: '97.00' }];
        // Applies style formatting before inserting the column
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A2:G2');
        // inserting a empty column at 0th index
        this.insertColumn();
        // inserting 1 column at the 5th index with column model
        this.insertColumn([{ index: 5, width: 90 }]);
        var rowIndex = 1;
        // Updating the 5th column data
        cellsModel.forEach((cell) => {
            this.updateCell(cell, ej.spreadsheet.getCellAddress(rowIndex, 5)); rowIndex++;
        });
        // Applies style formatting after the columns are inserted
        this.cellFormat({ textAlign: 'center' }, 'B3:B12');
        this.cellFormat({ textAlign: 'center' }, 'D3:D12');
        this.cellFormat({ textAlign: 'center' }, 'F3:H12');
    }

    </script>

{% endhighlight %}
{% highlight c# tabtitle="InsertColumnController.cs" %}
public IActionResult Index()
{
        List<object> data = new List<object>()
    {
        new { ProductId= "1",  ProductName= "Chai",  SupplierId= "1",  QuantityPerUnit= "10 boxes x 20 bags",  UnitsInStock= "39",  Discontinued= "false" },
        new { ProductId= "2",  ProductName= "Chang",  SupplierId= "1",  QuantityPerUnit= "24 - 12 oz bottles",  UnitsInStock= "17",  Discontinued= "true" },
        new { ProductId= "3",  ProductName= "Aniseed Syrup",  SupplierId= "1",  QuantityPerUnit= "12 - 550 ml bottles",  UnitsInStock= "13",  Discontinued= "false" },
        new { ProductId= "4",  ProductName= "Chef Anton\'s Cajun Seasoning",  SupplierId= "2",  QuantityPerUnit= "48 - 6 oz jars",  UnitsInStock= "53",  Discontinued= "true" },
        new { ProductId= "5",  ProductName= "Chef Anton\'s Gumbo Mix",  SupplierId= "2",  QuantityPerUnit= "36 boxes', 'Unit Price", UnitsInStock= "0",  Discontinued= "true" },
        new { ProductId= "6",  ProductName= "Grandma\'s Boysenberry Spread",  SupplierId= "3",  QuantityPerUnit= "12 - 8 oz jars",  UnitsInStock= "120",  Discontinued= "false" },
        new { ProductId= "7",  ProductName= "Uncle Bob\'s Organic Dried Pears",  SupplierId= "3",  QuantityPerUnit= "12 - 1 lb pkgs.", UnitsInStock= "15",  Discontinued= "true" },
        new { ProductId= "8",  ProductName= "Queso Cabrales",  SupplierId= "5",  QuantityPerUnit= "1 kg pkg.",  UnitsInStock= "22",  Discontinued= "false" },
        new { ProductId= "9",  ProductName= "Northwoods Cranberry Sauce",  SupplierId= "3",  QuantityPerUnit= "12 - 12 oz jars",  UnitsInStock= "6",  Discontinued= "false" },
        new { ProductId= "10",  ProductName= "Mishi Kobe Niku",  SupplierId= "4",  QuantityPerUnit= "18 - 500 g pkgs.",   UnitsInStock= "29", Discontinued= "false" },
    };
    ViewBag.DefaultData = data;
    return View();
}
        
{% endhighlight %}
{% endtabs %}



## Delete

Delete support provides an option for deleting the rows and columns in the spreadsheet. Use [`allowDelete`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowDelete) property to enable or disable the delete option in Spreadsheet.

The rows and columns can be deleted dynamically in the following ways,

* Using `delete` method, you can delete the loaded rows and columns.
* Using context menu, you can delete the selected rows and columns.

The following code example shows the delete operation of rows and columns in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
 <ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false" allowDelete="true" showRibbon="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet name="Sheet1">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="220"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
            <e-spreadsheet-sheet name="Sheet2">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
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
        // deleting the rows from 8th to 10th index. To delete row, the third argument of enum type is passed as 'Row', the last argument specifies the sheet name or index in which the delete operation will perform. By default,active sheet will be considered. It is applicable only for model type Row and Column.
        this.delete(8, 10, 'Row', 0); // startIndex, endIndex, Row, sheet index
        // deleting the 2nd and 5th indexed columns
        this.delete(2, 2, 'Column', 'Sheet2');
        this.delete(5, 5, 'Column');
        this.delete(0, 0, "Sheet"); // delete the first sheet. sheet index starts from 0
        // Applies style formatting after deleted the rows and columns
        this.cellFormat({ textAlign: 'center' }, 'A2:A8');
        this.cellFormat({ textAlign: 'center' }, 'D2:G8');
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="DeleteRowController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { ProductId= "1",  ProductName= "Chai",  SupplierId= "1",  QuantityPerUnit= "10 boxes x 20 bags",  UnitPrice= "18.00",  UnitsInStock= "39",  Discontinued= "false" },
        new { ProductId= "2",  ProductName= "Chang",  SupplierId= "1",  QuantityPerUnit= "24 - 12 oz bottles",  UnitPrice= "19.00",  UnitsInStock= "17",  Discontinued= "true" },
        new { ProductId= "3",  ProductName= "Aniseed Syrup",  SupplierId= "1",  QuantityPerUnit= "12 - 550 ml bottles",  UnitPrice= "10.00",  UnitsInStock= "13",  Discontinued= "false" },
        new { ProductId= "4",  ProductName= "Chef Anton\'s Cajun Seasoning",  SupplierId= "2",  QuantityPerUnit= "48 - 6 oz jars",  UnitPrice= "22.00",  UnitsInStock= "53",  Discontinued= "true" },
        new { ProductId= "5",  ProductName= "Chef Anton\'s Gumbo Mix",  SupplierId= "2",  QuantityPerUnit= "36 boxes', 'Unit Price",  UnitPrice= "21.35",  UnitsInStock= "0",  Discontinued= "true" },
        new { ProductId= "6",  ProductName= "Grandma\'s Boysenberry Spread",  SupplierId= "3",  QuantityPerUnit= "12 - 8 oz jars",  UnitPrice= "25.00",  UnitsInStock= "120",  Discontinued= "false" },
        new { ProductId= "7",  ProductName= "Uncle Bob\'s Organic Dried Pears",  SupplierId= "3",  QuantityPerUnit= "12 - 1 lb pkgs.",  UnitPrice= "30.00",  UnitsInStock= "15",  Discontinued= "true" },
        new { ProductId= "8",  ProductName= "Queso Cabrales",  SupplierId= "5",  QuantityPerUnit= "1 kg pkg.",  UnitPrice= "21.00",  UnitsInStock= "22",  Discontinued= "false" },
        new { ProductId= "9",  ProductName= "Northwoods Cranberry Sauce",  SupplierId= "3",  QuantityPerUnit= "12 - 12 oz jars",  UnitPrice= "21.00",  UnitsInStock= "6",  Discontinued= "false" },
        new { ProductId= "10",  ProductName= "Mishi Kobe Niku",  SupplierId= "4",  QuantityPerUnit= "18 - 500 g pkgs.",  UnitPrice= "21.00",  UnitsInStock= "29",  Discontinued= "true" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



## Hide and show

You can show or hide the rows and columns in the spreadsheet through property binding, method, and context menu.

### Row

The rows can be hidden or shown through the following ways,

* Using `hidden` property in row, you can hide/show the rows at initial load.
* Using `hideRow` method, you can hide the rows by specifying the start and end row index, set the last argument `hide` as `false` to unhide the hidden rows.
* Right-click on the row header and select the desired option from context menu

### Column

The columns can be hidden or shown through following ways,

* Using `hidden` property in columns, you can hide/show the columns at initial load.
* Using `hideColumn` method, you can hide the columns by specifying the start and end column index, set the last argument `hide` as `false` to unhide the hidden columns.
* Right-click on the column header and select the desired option from context menu

The following code example shows the hide/show rows and columns operation in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false" showSheetTabs="false" showRibbon="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row index="2" hidden="true"> </e-spreadsheet-row>
                    <e-spreadsheet-row hidden="true"> </e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="220" hidden="true"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90" hidden="true"></e-spreadsheet-column>
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
        // Unhide the 2nd index hidden column
        this.hideColumn(1, 1, false);
        // Unhide the 3rd index hidden row
        this.hideRow(3, 3, false);
        // Hiding the 6th index column
        this.hideColumn(6);
        // Hiding the 8th and 9th index row
        this.hideRow(8, 9);
        this.cellFormat({ textAlign: 'center' }, 'D2:H11');
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="ShowHideController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { ProductId= "1",  ProductName= "Chai",  SupplierId= "1",  QuantityPerUnit= "10 boxes x 20 bags",  UnitPrice= "18.00",  UnitsInStock= "39",  Discontinued= "false" },
        new { ProductId= "2",  ProductName= "Chang",  SupplierId= "1",  QuantityPerUnit= "24 - 12 oz bottles",  UnitPrice= "19.00",  UnitsInStock= "17",  Discontinued= "true" },
        new { ProductId= "3",  ProductName= "Aniseed Syrup",  SupplierId= "1",  QuantityPerUnit= "12 - 550 ml bottles",  UnitPrice= "10.00",  UnitsInStock= "13",  Discontinued= "false" },
        new { ProductId= "4",  ProductName= "Chef Anton\'s Cajun Seasoning",  SupplierId= "2",  QuantityPerUnit= "48 - 6 oz jars",  UnitPrice= "22.00",  UnitsInStock= "53",  Discontinued= "true" },
        new { ProductId= "5",  ProductName= "Chef Anton\'s Gumbo Mix",  SupplierId= "2",  QuantityPerUnit= "36 boxes', 'Unit Price",  UnitPrice= "21.35",  UnitsInStock= "0",  Discontinued= "true" },
        new { ProductId= "6",  ProductName= "Grandma\'s Boysenberry Spread",  SupplierId= "3",  QuantityPerUnit= "12 - 8 oz jars",  UnitPrice= "25.00",  UnitsInStock= "120",  Discontinued= "false" },
        new { ProductId= "7",  ProductName= "Uncle Bob\'s Organic Dried Pears",  SupplierId= "3",  QuantityPerUnit= "12 - 1 lb pkgs.",  UnitPrice= "30.00",  UnitsInStock= "15",  Discontinued= "true" },
        new { ProductId= "8",  ProductName= "Queso Cabrales",  SupplierId= "5",  QuantityPerUnit= "1 kg pkg.",  UnitPrice= "21.00",  UnitsInStock= "22",  Discontinued= "false" },
        new { ProductId= "9",  ProductName= "Northwoods Cranberry Sauce",  SupplierId= "3",  QuantityPerUnit= "12 - 12 oz jars",  UnitPrice= "21.00",  UnitsInStock= "6",  Discontinued= "false" },
        new { ProductId= "10",  ProductName= "Mishi Kobe Niku",  SupplierId= "4",  QuantityPerUnit= "18 - 500 g pkgs.",  UnitPrice= "21.00",  UnitsInStock= "29",  Discontinued= "true" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



## Size

You can change the size of rows and columns in the spreadsheet by using `setRowsHeight` and `setColumnsWidth` methods.

### Row

You can change the height of single or multiple rows by using the `setRowsHeight` method.

You can provide the following type of ranges to the method:

* Single row range: `['2:2']`
* Multiple rows range: `['1:100']`
* Multiple rows with discontinuous range: `['1:10', '15:25', '30:40']`
* Multiple rows with different sheets: `[Sheet1!1:50, 'Sheet2!1:50', 'Sheet3!1:50']`

The following code example shows how to change the height for single/multiple rows in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>

 

    <script>

         function created() {
            // To change height for single row
            this.setRowsHeight(40, ['2']);
            // To change height for multiple rows
            this.setRowsHeight(40, ['4:8', '10:12']);
        }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="RowHeightController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { ProductId= "1",  ProductName= "Chai",  SupplierId= "1",  QuantityPerUnit= "10 boxes x 20 bags",  UnitPrice= "18.00",  UnitsInStock= "39",  Discontinued= "false" },
        new { ProductId= "2",  ProductName= "Chang",  SupplierId= "1",  QuantityPerUnit= "24 - 12 oz bottles",  UnitPrice= "19.00",  UnitsInStock= "17",  Discontinued= "true" },
        new { ProductId= "3",  ProductName= "Aniseed Syrup",  SupplierId= "1",  QuantityPerUnit= "12 - 550 ml bottles",  UnitPrice= "10.00",  UnitsInStock= "13",  Discontinued= "false" },
        new { ProductId= "4",  ProductName= "Chef Anton\'s Cajun Seasoning",  SupplierId= "2",  QuantityPerUnit= "48 - 6 oz jars",  UnitPrice= "22.00",  UnitsInStock= "53",  Discontinued= "true" },
        new { ProductId= "5",  ProductName= "Chef Anton\'s Gumbo Mix",  SupplierId= "2",  QuantityPerUnit= "36 boxes', 'Unit Price",  UnitPrice= "21.35",  UnitsInStock= "0",  Discontinued= "true" },
        new { ProductId= "6",  ProductName= "Grandma\'s Boysenberry Spread",  SupplierId= "3",  QuantityPerUnit= "12 - 8 oz jars",  UnitPrice= "25.00",  UnitsInStock= "120",  Discontinued= "false" },
        new { ProductId= "7",  ProductName= "Uncle Bob\'s Organic Dried Pears",  SupplierId= "3",  QuantityPerUnit= "12 - 1 lb pkgs.",  UnitPrice= "30.00",  UnitsInStock= "15",  Discontinued= "true" },
        new { ProductId= "8",  ProductName= "Queso Cabrales",  SupplierId= "5",  QuantityPerUnit= "1 kg pkg.",  UnitPrice= "21.00",  UnitsInStock= "22",  Discontinued= "false" },
        new { ProductId= "9",  ProductName= "Northwoods Cranberry Sauce",  SupplierId= "3",  QuantityPerUnit= "12 - 12 oz jars",  UnitPrice= "21.00",  UnitsInStock= "6",  Discontinued= "false" },
        new { ProductId= "10",  ProductName= "Mishi Kobe Niku",  SupplierId= "4",  QuantityPerUnit= "18 - 500 g pkgs.",  UnitPrice= "21.00",  UnitsInStock= "29",  Discontinued= "true" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}

### Column

You can change the width of single or multiple columns by using the `setColumnsWidth` method.

You can provide the following type of ranges to the method:

* Single column range: `['F:F']`
* Multiple columns range: `['A:F']`
* Multiple columns with discontinuous range: `['A:C', 'G:I', 'K:M']`
* Multiple columns with different sheets: `[Sheet1!A:H, 'Sheet2!A:H', 'Sheet3!A:H']`

The following code example shows how to change the width for single/multiple columns in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>

 

    <script>

         function created() {
            // To change width of single column
            this.setColumnsWidth(100, ['F']);
            // To change width of multiple columns
            this.setColumnsWidth(120, ['A:C', 'G:I', 'K:M']);
        }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="ColumnWidthController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { ProductId= "1",  ProductName= "Chai",  SupplierId= "1",  QuantityPerUnit= "10 boxes x 20 bags",  UnitPrice= "18.00",  UnitsInStock= "39",  Discontinued= "false" },
        new { ProductId= "2",  ProductName= "Chang",  SupplierId= "1",  QuantityPerUnit= "24 - 12 oz bottles",  UnitPrice= "19.00",  UnitsInStock= "17",  Discontinued= "true" },
        new { ProductId= "3",  ProductName= "Aniseed Syrup",  SupplierId= "1",  QuantityPerUnit= "12 - 550 ml bottles",  UnitPrice= "10.00",  UnitsInStock= "13",  Discontinued= "false" },
        new { ProductId= "4",  ProductName= "Chef Anton\'s Cajun Seasoning",  SupplierId= "2",  QuantityPerUnit= "48 - 6 oz jars",  UnitPrice= "22.00",  UnitsInStock= "53",  Discontinued= "true" },
        new { ProductId= "5",  ProductName= "Chef Anton\'s Gumbo Mix",  SupplierId= "2",  QuantityPerUnit= "36 boxes', 'Unit Price",  UnitPrice= "21.35",  UnitsInStock= "0",  Discontinued= "true" },
        new { ProductId= "6",  ProductName= "Grandma\'s Boysenberry Spread",  SupplierId= "3",  QuantityPerUnit= "12 - 8 oz jars",  UnitPrice= "25.00",  UnitsInStock= "120",  Discontinued= "false" },
        new { ProductId= "7",  ProductName= "Uncle Bob\'s Organic Dried Pears",  SupplierId= "3",  QuantityPerUnit= "12 - 1 lb pkgs.",  UnitPrice= "30.00",  UnitsInStock= "15",  Discontinued= "true" },
        new { ProductId= "8",  ProductName= "Queso Cabrales",  SupplierId= "5",  QuantityPerUnit= "1 kg pkg.",  UnitPrice= "21.00",  UnitsInStock= "22",  Discontinued= "false" },
        new { ProductId= "9",  ProductName= "Northwoods Cranberry Sauce",  SupplierId= "3",  QuantityPerUnit= "12 - 12 oz jars",  UnitPrice= "21.00",  UnitsInStock= "6",  Discontinued= "false" },
        new { ProductId= "10",  ProductName= "Mishi Kobe Niku",  SupplierId= "4",  QuantityPerUnit= "18 - 500 g pkgs.",  UnitPrice= "21.00",  UnitsInStock= "29",  Discontinued= "true" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}

## Changing text in column headers

Using the [`beforeCellRender`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeCellRender) event, you can change the text in the column headers. In that event, you can use the `e-header-cell` class to identify the header cell element and update its text value.

The following code example shows how to change the text in the column headers.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" beforeCellRender="beforeCellRender"></ejs-spreadsheet>

<script>

    function beforeCellRender(args) {
        if (
            args.colIndex >= 0 &&
            args.colIndex <= 10 &&
            args.element.classList.contains('e-header-cell')
        ) {
            var text = 'custom header ' + args.colIndex.toString();
            // Add the custom text to the innerText of the element.
            args.element.innerText = text;
        }
    }

</script>
{% endhighlight %}
{% endtabs %}

## Limitations of insert and delete

The following features have some limitations in Insert/Delete:

* Insert row/column between the formatting applied cells.
* Insert row/column between the data validation.
* Insert row/column between the conditional formatting applied cells.
* Insert/delete row/column between the filter applied cells.

## See Also

* [Hyperlink](./link)
* [Sorting](./sort)
* [Filtering](./filter)
