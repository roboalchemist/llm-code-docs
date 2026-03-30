# Source: https://docs.syncfusion.com/uwp/cellgrid/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/wpf/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/winforms/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/uwp/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/blazor/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/formulas.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/formulas.md

# Formulas in ASP.NET Core Spreadsheet control

Formulas are used for calculating the data in a worksheet. You can refer the cell reference from same sheet or from different sheets.

## Usage

You can set formula for a cell in the following ways,

* Using the `formula` property from `cell`, you can set the formula or expression to each cell at initial load.
* Set the formula or expression through data binding.
* You can set formula for a cell by [`editing`](./editing).
* Using the `updateCell` method, you can set or update the cell formula.

## Culture-Based Argument Separator

Previously, although you could import culture-based Excel files into the Spreadsheet control, the formulas wouldn't calculate correctly. This was due to the absence of culture-based argument separators and support for culture-based formatted numeric values as arguments. However, starting from version 25.1.35, you can now import culture-based Excel files into the Spreadsheet component.

> Before importing culture-based Excel files, ensure that the Spreadsheet control is rendered with the corresponding culture. Additionally, launch the import/export services with the same culture to ensure compatibility.

When loading spreadsheet data with culture-based formula argument separators using cell data binding, local/remote data, or JSON, ensure to set the [listSeparator](https://help.syncfusion.com/cr/aspnetcore-js2/syncfusion.ej2.spreadsheet.spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_ListSeparator) property value as the culture-based list separator from your end. Additionally, note that when importing an Excel file, the [listSeparator](https://help.syncfusion.com/cr/aspnetcore-js2/syncfusion.ej2.spreadsheet.spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_ListSeparator) property will be updated based on the culture of the launched import/export service.

In the example below, the Spreadsheet control is rendered with the `German culture` [`de`]. Additionally, you can find references on how to set the culture-based argument separator and culture-based formatted numeric value as arguments to the formulas.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div>
    <ejs-spreadsheet id="spreadsheet" locale="de" listSeparator=";" showRibbon="false" showSheetTabs="false" created="created">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet selectedRange="E14">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row index="12">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="3" value="Subtotal:"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUBTOTAL(9;E2:E12)"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="3" value="Discount (8,5%):"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=PRODUCT(8,5;E13)/100"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="3" value="Total Amount:"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=E13-E14"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="180"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>
</div>

<script>
    function loadCultureFiles(name) {
        ej.base.setCulture(name);
        ej.base.setCurrencyCode('EUR');
        var files = ['ca-gregorian.json', 'currencies.json', 'numbers.json', 'timeZoneNames.json', 'numberingSystems.json'];
        var loader = ej.base.loadCldr;
        var loadCulture = function (prop) {
            var val, ajax;
            if (files[prop] === 'numberingSystems.json') {
                ajax = new ej.base.Ajax(location.origin + '/../cldr-data/supplemental/' + files[prop], 'GET', false);
            } else {
                ajax = new ej.base.Ajax(location.origin + '/../cldr-data/main/' + name + '/' + files[prop], 'GET', false);
            }
            ajax.onSuccess = function (value) {
                val = value;
            };
            ajax.send();
            loader(JSON.parse(val));
        };
        for (var prop = 0; prop < files.length; prop++) {
            loadCulture(prop);
        }
    }
    loadCultureFiles('de');

    function created() {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        spreadsheet.cellFormat({ textAlign: 'center', fontWeight: 'bold' }, 'A1:E1');
        spreadsheet.numberFormat(ej.spreadsheet.getFormatFromType('Currency'), 'D2:E12');
        spreadsheet.numberFormat(ej.spreadsheet.getFormatFromType('Currency'), 'E13:E15');
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="FormulaController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { ItemCode= "I231",  ItemName= "Chinese Combo Noodle",  Quantity= "2",  Rate= "125",  Amount= "=PRODUCT(C2;D2)" },
        new { ItemCode= "I245",  ItemName= "Chinese Combo Rice",  Quantity= "3",  Rate= "125",  Amount= "=PRODUCT(C3;D3)" },
        new { ItemCode= "I237",  ItemName= "Amritsari Chola",  Quantity= "2",  Rate= "225",  Amount= "=PRODUCT(C4;D4)" },
        new { ItemCode= "I291",  ItemName= "Asian Mixed Entree Platt",  Quantity= "3",  Rate= "165",  Amount= "=PRODUCT(C5;D5)" },
        new { ItemCode= "I268",  ItemName= "Chinese Combo Chicken",  Quantity= "3",  Rate= "125",  Amount= "=PRODUCT(C6;D6)" },
        new { ItemCode= "I251",  ItemName= "Chivas Regal",  Quantity= "1",  Rate= "325",  Amount= "=PRODUCT(C7;D7)" },
        new { ItemCode= "I256",  ItemName= "Chicken Drumsticks",  Quantity= "2",  Rate= "180",  Amount= "=PRODUCT(C8;D8)" },
        new { ItemCode= "I232",  ItemName= "Manchow Soup",  Quantity= "2",  Rate= "160",  Amount= "=PRODUCT(C9;D9)" },
        new { ItemCode= "I290",  ItemName= "Schezuan Chicken",  Quantity= "3",  Rate= "180",  Amount= "=PRODUCT(C10;D10)" },
        new { ItemCode= "I229",  ItemName= "Manchow Soup",  Quantity= "2",  Rate= "125",  Amount= "=PRODUCT(C11;D11)" },
        new { ItemCode= "I239",  ItemName= "Jw Black Lable",  Quantity= "2",  Rate= "175",  Amount= "=PRODUCT(C12;D12)" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}

## Create User Defined Functions / Custom Functions

The Spreadsheet includes a number of built-in formulas. For your convenience, a list of supported formulas can be found [here](https://ej2.syncfusion.com/aspnetcore/documentation/spreadsheet/formulas#supported-formulas).

You can define and use an unsupported formula, i.e. a user defined/custom formula, in the spreadsheet by using the `addCustomFunction` function. Meanwhile, remember that you should define a user defined/custom formula whose results should only return a single value. If a user-defined/custom formula returns an array, it will be time-consuming to update adjacent cell values.

The following code example shows an unsupported formula in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
  <ejs-spreadsheet id="spreadsheet" created="created" showRibbon="false" showSheetTabs="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A2"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row height="40" customHeight="true">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Monthly Expense" colSpan="5">
                                <e-spreadsheet-cellstyle textAlign="Center" fontWeight="Bold" verticalAlign="Middle" fontStyle="Italic" fontSize="15pt"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row index="11">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Totals" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" fontStyle="Italic"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(B3:B11)"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(C3:C11)"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(D3:D11)"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Number of Categories" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=COUNTA(A3:A11)"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Average Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=AVERAGE(B3:B11)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Min Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=MIN(B3:B11)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Max Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=MAX(B3:B11)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="150"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="150"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

        function created() {
            this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A2:F2');
            this.numberFormat('$#,##0', 'B3:D12');
            this.numberFormat('0%', 'E3:E12');
            // Adding custom function for calculating the percentage between two cells.
            this.addCustomFunction(calculatePercentage, 'PERCENTAGE');
            // Adding custom function for calculating round down for the value.
            this.addCustomFunction(roundDownHandler, 'ROUNDDOWN');
            // Calculate percentage using custom added formula in E12 cell.
            this.updateCell({ formula: '=PERCENTAGE(C12,D12)' }, 'E12');
            // Calculate round down for average values using custom added formula in F12 cell.
            this.updateCell({ formula: '=ROUNDDOWN(F11,1)' }, 'F12');
        }

        // Custom function to calculate percentage between two cell values.
        function calculatePercentage(firstCell, secondCell) {
            return (firstCell) / (secondCell);
        }

        // Custom function to calculate round down for values.
        function roundDownHandler(value, digit) {
            var multiplier = Math.pow(10, digit);
            return Math.floor(value * multiplier) / multiplier;
        }
    </script>
{% endhighlight %}
{% highlight c# tabtitle="FormulaController.cs" %}
public IActionResult Index()
{
   List<object> data = new List<object>()
   {
      new { Category= "Household Utilities",  MonthlySpend= "=C3/12",  AnnualSpend= "3000",  LastYearSpend= "3000",  PercentageChange= "=C3/D3", AverageChange= "=7.9/E3"},
      new { Category= "Food",  MonthlySpend= "=C4/12",  AnnualSpend= "2500",  LastYearSpend= "2250",  PercentageChange= "=C4/D4", AverageChange= "=7.9/E4"},
      new { Category= "Gasoline",  MonthlySpend= "=C5/12",  AnnualSpend= "1500",  LastYearSpend= "1200",  PercentageChange= "=C5/D5", AverageChange= "=7.9/E5"},
      new { Category= "Clothes",  MonthlySpend= "=C6/12",  AnnualSpend= "1200",  LastYearSpend= "1000",  PercentageChange= "=C6/D6", AverageChange= "=7.9/E6"},
      new { Category= "Insurance",  MonthlySpend= "=C7/12",  AnnualSpend= "1500",  LastYearSpend= "1500",  PercentageChange= "=C7/D7", AverageChange= "=7.9/E7"},
      new { Category= "Taxes",  MonthlySpend= "=C8/12",  AnnualSpend= "3500",  LastYearSpend= "3500",  PercentageChange= "=C8/D8", AverageChange= "=7.9/E8"},
      new { Category= "Entertainment",  MonthlySpend= "=C9/12",  AnnualSpend= "2000",  LastYearSpend= "2250",  PercentageChange= "=C9/D9", AverageChange= "=7.9/E9"},
      new { Category= "Vacation",  MonthlySpend= "=C10/12",  AnnualSpend= "1500",  LastYearSpend= "2000",  PercentageChange= "=C10/D10", AverageChange= "=7.9/E10"},
      new { Category= "Miscellaneous",  MonthlySpend= "=C11/12",  AnnualSpend= "1250",  LastYearSpend= "1558",  PercentageChange= "=C11/D11", AverageChange= "=7.9/E11"},
   };
   ViewBag.DefaultData = data;
   return View();
}
{% endhighlight %}
{% endtabs %}

Second, if you want to directly compute any formula or expression, you can use the `computeExpression` method. This method will work for both built-in and used-defined/custom formula.

The following code example shows how to use `computeExpression` method in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
  <ejs-spreadsheet id="spreadsheet" created="created" showRibbon="false" showSheetTabs="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A2"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row height="40" customHeight="true">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Monthly Expense" colSpan="5">
                                <e-spreadsheet-cellstyle textAlign="Center" fontWeight="Bold" verticalAlign="Middle" fontStyle="Italic" fontSize="15pt"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row index="11">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Totals" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" fontStyle="Italic"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(B3:B11)"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(C3:C11)"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(D3:D11)"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Number of Categories" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=COUNTA(A3:A11)"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Average Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=AVERAGE(B3:B11)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Min Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=MIN(B3:B11)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Max Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=MAX(B3:B11)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="150"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

        function created() {
            this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A2:E2');
            this.numberFormat('$#,##0', 'B3:D12');
            this.numberFormat('0%', 'E3:E12');
            // Adding custom function for calculating the percentage between two cells.
            this.addCustomFunction(calculatePercentage, 'PERCENTAGE');
            // Calculate percentage using custom added formula in E11 cell.
            this.updateCell({ formula: '=PERCENTAGE(C11,D11)' }, 'E11');
            // Calculate expressions using computeExpression in E10 cell.
            this.updateCell({ value: this.computeExpression('C10/D10') },'E10');
            // Calculate custom formula values using computeExpression in E12 cell.
            this.updateCell({ value: this.computeExpression('=PERCENTAGE(C12,D12)'), }, 'E12');
            // Calculate SUM (built-in) formula values using computeExpression in D12 cell.
            this.updateCell({ value: this.computeExpression('=SUM(D3:D11)') }, 'D12');
        }

        // Custom function to calculate percentage between two cell values.
        function calculatePercentage(firstCell, secondCell) {
            return (firstCell) / (secondCell);
        }
    </script>
{% endhighlight %}
{% highlight c# tabtitle="FormulaController.cs" %}
public IActionResult Index()
{
   List<object> data = new List<object>()
   {
      new { Category= "Household Utilities",  MonthlySpend= "=C3/12",  AnnualSpend= "3000",  LastYearSpend= "3000",  PercentageChange= "=C3/D3"},
      new { Category= "Food",  MonthlySpend= "=C4/12",  AnnualSpend= "2500",  LastYearSpend= "2250",  PercentageChange= "=C4/D4"},
      new { Category= "Gasoline",  MonthlySpend= "=C5/12",  AnnualSpend= "1500",  LastYearSpend= "1200",  PercentageChange= "=C5/D5"},
      new { Category= "Clothes",  MonthlySpend= "=C6/12",  AnnualSpend= "1200",  LastYearSpend= "1000",  PercentageChange= "=C6/D6"},
      new { Category= "Insurance",  MonthlySpend= "=C7/12",  AnnualSpend= "1500",  LastYearSpend= "1500",  PercentageChange= "=C7/D7"},
      new { Category= "Taxes",  MonthlySpend= "=C8/12",  AnnualSpend= "3500",  LastYearSpend= "3500",  PercentageChange= "=C8/D8"},
      new { Category= "Entertainment",  MonthlySpend= "=C9/12",  AnnualSpend= "2000",  LastYearSpend= "2250",  PercentageChange= "=C9/D9"},
      new { Category= "Vacation",  MonthlySpend= "=C10/12",  AnnualSpend= "1500",  LastYearSpend= "2000",  PercentageChange= "=C10/D10"},
      new { Category= "Miscellaneous",  MonthlySpend= "=C11/12",  AnnualSpend= "1250",  LastYearSpend= "1558",  PercentageChange= "=C11/D11"},
   };
   ViewBag.DefaultData = data;
   return View();
}
{% endhighlight %}
{% endtabs %}

## Formula bar

Formula bar is used to edit or enter cell data in much easier way. By default, the formula bar is enabled in the spreadsheet. Use the [`showFormulaBar`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_ShowFormulaBar) property to enable or disable the formula bar.

## Named Ranges

You can define a meaningful name for a cell range and use it in the formula for calculation. It makes your formula much easier to understand and maintain. You can add named ranges to the Spreadsheet in the following ways,

* Using the [`definedNames`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_DefinedNames) collection, you can add multiple named ranges at initial load.
* Use the `addDefinedName` method to add a named range dynamically.
* You can remove an added named range dynamically using the `removeDefinedName` method.
* Select the range of cells, and then enter the name for the selected range in the name box.

The following code example shows the usage of named ranges support.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created" showRibbon="false" showSheetTabs="false" beforeDataBound="beforeDataBound">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet name="Budget Details">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A2"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row height="40" customHeight="true">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Monthly Expense" colSpan="5">
                                <e-spreadsheet-cellstyle textAlign="Center" fontWeight="Bold" verticalAlign="Middle" fontStyle="Italic" fontSize="15pt"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row index="11">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Totals" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" fontStyle="Italic"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(MonthlySpendings)"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(AnnualSpendings)"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(LastYearSpendings)"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=C12/D12"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Number of Categories" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=COUNTA(Categories)"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Average Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=AVERAGE(MonthlySpendings)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Min Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=MIN(MonthlySpendings)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" value="Max Spend" colSpan="2">
                                <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell index="3" formula="=MAX(MonthlySpendings)" format="$#,##0"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="150"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
        <e-spreadsheet-definednames>
            <e-spreadsheet-definedname name="Categories" refersTo="=Budget Details!A3:A11"></e-spreadsheet-definedname>
            <e-spreadsheet-definedname name="MonthlySpendings" refersTo="=Budget Details!B3:B11"></e-spreadsheet-definedname>
            <e-spreadsheet-definedname name="AnnualSpendings" refersTo="=Budget Details!C3:C11"></e-spreadsheet-definedname>
        </e-spreadsheet-definednames>
    </ejs-spreadsheet>


    <script>

      function created() {
        // Removing the unwanted `PercentageChange` named range
        this.removeDefinedName('PercentageChange', '');

        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A2:E2');
        this.numberFormat('$#,##0', 'B3:D12');
        this.numberFormat('0%', 'E3:E12');
    }

    function beforeDataBound() {
        // Adding name dynamically for `last year spending` and `percentage change` ranges.
        this.addDefinedName({ name: 'LastYearSpendings', refersTo: '=D3:D11' });
        this.addDefinedName({ name: 'PercentageChange', refersTo: '=E3:E11' });
    }
    </script>
{% endhighlight %}
{% highlight c# tabtitle="DefinedNameController.cs" %}
public IActionResult Index()
{
   List<object> data = new List<object>()
   {
      new { Category= "Household Utilities",  MonthlySpend= "=C3/12",  AnnualSpend= "3000",  LastYearSpend= "3000",  PercentageChange= "=C3/D3"},
      new { Category= "Food",  MonthlySpend= "=C4/12",  AnnualSpend= "2500",  LastYearSpend= "2250",  PercentageChange= "=C4/D4"},
      new { Category= "Gasoline",  MonthlySpend= "=C5/12",  AnnualSpend= "1500",  LastYearSpend= "1200",  PercentageChange= "=C5/D5"},
      new { Category= "Clothes",  MonthlySpend= "=C6/12",  AnnualSpend= "1200",  LastYearSpend= "1000",  PercentageChange= "=C6/D6"},
      new { Category= "Insurance",  MonthlySpend= "=C7/12",  AnnualSpend= "1500",  LastYearSpend= "1500",  PercentageChange= "=C7/D7"},
      new { Category= "Taxes",  MonthlySpend= "=C8/12",  AnnualSpend= "3500",  LastYearSpend= "3500",  PercentageChange= "=C8/D8"},
      new { Category= "Entertainment",  MonthlySpend= "=C9/12",  AnnualSpend= "2000",  LastYearSpend= "2250",  PercentageChange= "=C9/D9"},
      new { Category= "Vacation",  MonthlySpend= "=C10/12",  AnnualSpend= "1500",  LastYearSpend= "2000",  PercentageChange= "=C10/D10"},
      new { Category= "Miscellaneous",  MonthlySpend= "=C11/12",  AnnualSpend= "1250",  LastYearSpend= "1558",  PercentageChange= "=C11/D11"},
   };
   ViewBag.DefaultData = data;
   return View();
}
{% endhighlight %}
{% endtabs %}

## Calculation Mode

The Spreadsheet provides a `Calculation Mode` feature like the calculation options in online Excel. This feature allows you to control when and how formulas are recalculated in the spreadsheet. The available modes are:

* `Automatic`: Formulas are recalculated instantly whenever a change occurs in the dependent cells.
* `Manual`: Formulas are recalculated only when triggered explicitly by the user using options like `Calculate Sheet` or `Calculate Workbook`.

You can configure the calculate mode using the [`calculationMode`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_CalculationMode) property of the Spreadsheet. These modes offer flexibility to balance real-time updates and performance optimization.

### Automatic Mode

In Automatic Mode, formulas are recalculated instantly whenever a dependent cell is modified. This mode is perfect for scenarios where real-time updates are essential, ensuring that users see the latest results without additional actions.

For example, consider a spreadsheet where cell `C1` contains the formula `=A1+B1`. When the value in `A1` or `B1` changes, `C1` updates immediately without requiring any user intervention. You can enable this mode by setting the [`calculationMode`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_CalculationMode) property to `Automatic`.

The following code example demonstrates how to set the Automatic calculation mode in a Spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created" calculationMode="Automatic">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet name="Product Details">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A1"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="130"></e-spreadsheet-column>
                    <e-spreadsheet-column width="92"></e-spreadsheet-column>
                    <e-spreadsheet-column width="96"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

      function created() {
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:H1');
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="CalculationModeController.cs" %}
public IActionResult Index()
{
   List<object> data = new List<object>()
   {
      new { ItemName= "Casual Shoes", Date= "2/14/2024", Time= "11:34:32 AM", Quantity= 10, Price= 20, Amount= "=PRODUCT(D2=E2)", Discount= "2%", Profit= "=PRODUCT(G2=F2)" },
      new { ItemName= "Sports Shoes", Date= "6/11/2024", Time= "05:56:32 AM", Quantity= 20, Price= 30, Amount= "=PRODUCT(D3=E3)", Discount= "5%", Profit= "=PRODUCT(G3=F3)" },
      new { ItemName= "Formal Shoes", Date= "7/27/2024", Time= "03:32:44 AM", Quantity= 20, Price= 15, Amount= "=PRODUCT(D4=E4)", Discount= "7.5%", Profit= "=PRODUCT(G4=F4)" },
      new { ItemName= "Sandals & Floaters", Date= "11/21/2024", Time= "06:23:54 PM", Quantity= 15, Price= 20.45, Amount= "=PRODUCT(D5=E5)", Discount= "11%", Profit= "=PRODUCT(G5=F5)" },
      new { ItemName= "Flip- Flops & Slippers", Date= "6/23/2024", Time= "12:43:59 AM", Quantity= 30, Price= 10.67, Amount= "=PRODUCT(D6=E6)", Discount= "10%", Profit= "=PRODUCT(G6=F6)" },
      new { ItemName= "Sneakers", Date= "7/22/2024", Time= "10:55:53 AM", Quantity= 40, Price= 20, Amount= "=PRODUCT(D7=E7)", Discount= "13.2%", Profit= "=PRODUCT(G7=F7)" },
      new { ItemName= "Running Shoes", Date= "2/4/2024", Time= "03:44:34 AM", Quantity= 20, Price= 10.5, Amount= "=PRODUCT(D8=E8)", Discount= "3%", Profit= "=PRODUCT(G8=F8)" },
      new { ItemName= "Loafers", Date= "11/30/2024", Time= "03:12:52 AM", Quantity= 31, Price= 10, Amount= "=PRODUCT(D9=E9)", Discount= "6.67%", Profit= "=PRODUCT(G9=F9)" },
      new { ItemName= "Cricket Shoes", Date= "7/9/2024", Time= "11:32:14 PM", Quantity= 41, Price= 30, Amount= "=PRODUCT(D10=E10)", Discount= "12.5%", Profit= "=PRODUCT(G10=F10)" },
      new { ItemName= "T-Shirts", Date= "10/31/2024", Time= "12:01:44 AM", Quantity= 50, Price= 10.75, Amount= "=PRODUCT(D11=E11)", Discount= "9%", Profit= "=PRODUCT(G11=F11)" }
   };
   ViewBag.DefaultData = data;
   return View();
}
{% endhighlight %}
{% endtabs %}

### Manual Mode

In Manual Mode, formulas are not recalculated automatically when cell values are modified. Instead, recalculations must be triggered explicitly. This mode is ideal for scenarios where performance optimization is a priority, such as working with large datasets or computationally intensive formulas.

For example, imagine a spreadsheet where cell `C1` contains the formula `=A1+B1`. When the value in `A1` or `B1` changes, the value in `C1` will not update automatically. Instead, the recalculation must be initiated manually using either the `Calculate Sheet` or `Calculate Workbook` option. To manually initiate recalculation, the Spreadsheet provides two options:

* `Calculate Sheet`: Recalculates formulas for the active sheet only.
* `Calculate Workbook`: Recalculates formulas across all sheets in the workbook.

The following code example demonstrates how to set the Manual calculation mode in a Spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created" calculationMode="Manual">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet name="Product Details">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A1"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="130"></e-spreadsheet-column>
                    <e-spreadsheet-column width="92"></e-spreadsheet-column>
                    <e-spreadsheet-column width="96"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

      function created() {
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:H1');
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="CalculationModeController.cs" %}
public IActionResult Index()
{
   List<object> data = new List<object>()
   {
      new { ItemName= "Casual Shoes", Date= "2/14/2024", Time= "11:34:32 AM", Quantity= 10, Price= 20, Amount= "=PRODUCT(D2=E2)", Discount= "2%", Profit= "=PRODUCT(G2=F2)" },
      new { ItemName= "Sports Shoes", Date= "6/11/2024", Time= "05:56:32 AM", Quantity= 20, Price= 30, Amount= "=PRODUCT(D3=E3)", Discount= "5%", Profit= "=PRODUCT(G3=F3)" },
      new { ItemName= "Formal Shoes", Date= "7/27/2024", Time= "03:32:44 AM", Quantity= 20, Price= 15, Amount= "=PRODUCT(D4=E4)", Discount= "7.5%", Profit= "=PRODUCT(G4=F4)" },
      new { ItemName= "Sandals & Floaters", Date= "11/21/2024", Time= "06:23:54 PM", Quantity= 15, Price= 20.45, Amount= "=PRODUCT(D5=E5)", Discount= "11%", Profit= "=PRODUCT(G5=F5)" },
      new { ItemName= "Flip- Flops & Slippers", Date= "6/23/2024", Time= "12:43:59 AM", Quantity= 30, Price= 10.67, Amount= "=PRODUCT(D6=E6)", Discount= "10%", Profit= "=PRODUCT(G6=F6)" },
      new { ItemName= "Sneakers", Date= "7/22/2024", Time= "10:55:53 AM", Quantity= 40, Price= 20, Amount= "=PRODUCT(D7=E7)", Discount= "13.2%", Profit= "=PRODUCT(G7=F7)" },
      new { ItemName= "Running Shoes", Date= "2/4/2024", Time= "03:44:34 AM", Quantity= 20, Price= 10.5, Amount= "=PRODUCT(D8=E8)", Discount= "3%", Profit= "=PRODUCT(G8=F8)" },
      new { ItemName= "Loafers", Date= "11/30/2024", Time= "03:12:52 AM", Quantity= 31, Price= 10, Amount= "=PRODUCT(D9=E9)", Discount= "6.67%", Profit= "=PRODUCT(G9=F9)" },
      new { ItemName= "Cricket Shoes", Date= "7/9/2024", Time= "11:32:14 PM", Quantity= 41, Price= 30, Amount= "=PRODUCT(D10=E10)", Discount= "12.5%", Profit= "=PRODUCT(G10=F10)" },
      new { ItemName= "T-Shirts", Date= "10/31/2024", Time= "12:01:44 AM", Quantity= 50, Price= 10.75, Amount= "=PRODUCT(D11=E11)", Discount= "9%", Profit= "=PRODUCT(G11=F11)" }
   };
   ViewBag.DefaultData = data;
   return View();
}
{% endhighlight %}
{% endtabs %}

## Supported Formulas

The following are the list of formulas supported in spreadsheet,

| Formula | Description |
|-------|---------|
| ABS | Returns the value of a number without its sign. |
| ADDRESS | Returns a cell reference as text, given specified row and column numbers. |
| AND | Returns TRUE if all the arguments are TRUE, otherwise returns FALSE. |
| AVERAGE | Calculates average for the series of numbers and/or cells excluding text. |
| AVERAGEA | Calculates the average for the cells evaluating TRUE as 1, text and FALSE as 0. |
| AVERAGEIF | Clears content of the active cell and enables edit mode. |
| AVERAGEIFS | Calculates average for the cells based on specified conditions. |
| CEILING | Rounds a number up to the nearest multiple of a given factor. |
| CHOOSE | Returns a value from list of values, based on index number. |
| CHAR | Returns the character from the specified number. |
| CODE | Returns the numeric code for the first character in a given string. |
| CONCAT | Concatenates a list or a range of text strings. |
| CONCATENATE | Combines two or more strings together. |
| COUNT | Counts the cells that contain numeric values in a range. |
| COUNTA | Counts the cells that contains values in a range. |
| COUNTBLANK | Returns the number of empty cells in a specified range of cells. |
| COUNTIF | Counts the cells based on specified condition. |
| COUNTIFS | Counts the cells based on specified conditions. |
| DATE | Returns the date based on given year, month, and day. |
| DATEVALUE | Converts a date string into date value. |
| DAY | Returns the day from the given date. |
| DAYS | Returns the number of days between two dates. |
| DECIMAL | Converts a text representation of a number in a given base into a decimal number. |
| DEGREES | Converts radians to degrees. |
| DOLLAR | Converts the number to currency formatted text. |
| EDATE | Returns a date with given number of months before or after the specified date. |
| EOMONTH | Returns the last day of the month that is a specified number of months before or after an initially supplied start date. |
| EVEN | Rounds a positive number up and negative number down to the nearest even integer. |
| EXACT | Checks whether a two text strings are exactly same and returns TRUE or FALSE. |
| EXP | Returns e raised to the power of the given number. |
| FACT | Returns the factorial of a number. |
| FIND | Returns the position of a string within another string, which is case sensitive.|
| FLOOR | Rounds a number down to the nearest multiple of a given factor. |
| HLOOKUP | Looks for a value in the top row of the array of values and then returns a value in the same column from a row in the array that you specify. |
| HOUR | Returns the number of hours in a specified time string. |
| IF | Returns value based on the given expression. |
| IFERROR | Returns value if no error found else it will return specified value. |
| IFS | Returns value based on the given multiple expressions. |
| INDEX | Returns a value of the cell in a given range based on row and column number. |
| INT | Rounds a number down to the nearest integer. |
| INTERCEPT | Calculates the point of the Y-intercept line via linear regression. |
| ISNUMBER | Returns true when the value parses as a numeric value. |
| LARGE | Returns the `k-th` largest value in a given array. |
| LEN | Returns a number of characters in a given string. |
| LN | Returns the natural logarithm of a number. |
| LOG | Returns the logarithm of a number to the base that you specify. |
| LOOKUP | Looks for a value in a one-row or one-column range, then returns a value from the same position in a second one-row or one-column range. |
| MATCH | Returns the relative position of a specified value in given range. |
| MAX | Returns the largest number of the given arguments. |
| MEDIAN | Returns the median of the given set of numbers. |
| MINUTE | Returns the number of minutes in a specified time string. |
| MIN | Returns the smallest number of the given arguments. |
| MOD | Returns a remainder after a number is divided by divisor. |
| MONTH | Returns the number of months in a specified date string. |
| NOT | Returns the inverse of a given logical expression. |
| NOW | Returns the current date and time. |
| ODD | Rounds a positive number up and negative number down to the nearest odd integer. |
| OR | Returns TRUE if any of the arguments are TRUE, otherwise returns FALSE. |
| PI | Returns the value of pi. |
| POWER | Returns the result of a number raised to power. |
| PRODUCT | Multiplies a series of numbers and/or cells. |
| RADIANS | Converts degrees into radians. |
| RAND | Returns a random number between 0 and 1. |
| RANDBETWEEN | Returns a random integer based on specified values. |
| ROUND | Rounds a number to the specified number of digits. |
| ROUNDDOWN | Rounds a number down, toward zero. |
| ROUNDUP | Rounds a number up, away from zero. |
| RSQ | Returns the square of the Pearson product moment correlation coefficient based on data points in known_y's and known_x's. |
| SECOND | Returns the number of seconds in a specified time string. |
| SMALL | Returns the `k-th` smallest value in a given array. |
| SLOPE | Returns the slope of the line from linear regression of the data points. |
| SORT | Sorts the contents of a column, range, or array in ascending or descending order. |
| SQRT | Returns the square root of a positive number. |
| SUBTOTAL | Returns subtotal for a range using the given function number. |
| SUM | Adds a series of numbers and/or cells. |
| SUMIF | Adds the cells based on specified condition. |
| SUMIFS | Adds the cells based on specified conditions. |
| SUMPRODUCT | Returns the sum of the products of the corresponding array in given arrays. |
| T | Checks whether a value is text or not and returns the text. |
| TEXT | Converts the supplied value into text by using the user-specified format. |
| TIME | Converts hours, minutes, seconds to the time formatted text. |
| TODAY | Returns the current date. |
| TRUNC | Truncates a supplied number to a specified number of decimal places. |
| UNIQUE | Returns a unique values from a range or array. |
| VLOOKUP | Looks for a specific value in the first column of a lookup range and returns a corresponding value from a different column within the same row. |

## Formula Error Dialog

If you enter an invalid formula in a cell, an error dialog with an error message will appear. For instance, a formula with the incorrect number of arguments, a formula without parenthesis, etc.

| Error Message | Reason |
|-------|---------|
| We found that you typed a formula with an invalid arguments | Occurs when passing an argument even though it wasn't needed. |
| We found that you typed a formula with an empty expression | Occurs when passing an empty expression in the argument. |
| We found that you typed a formula with one or more missing opening or closing parenthesis | Occurs when an open parenthesis or a close parenthesis is missing. |
| We found that you typed a formula which is improper | Occurs when passing a single reference but a range was needed. |
| We found that you typed a formula with a wrong number of arguments | Occurs when the required arguments were not passed. |
| We found that you typed a formula which requires 3 arguments | Occurs when the required 3 arguments were not passed. |
| We found that you typed a formula with a mismatched quotes | Occurs when passing an argument with mismatched quotes. |
| We found that you typed a formula with a circular reference | Occurs when passing a formula with circular cell reference. |
| We found that you typed a formula which is invalid | Except in the cases mentioned above, all other errors will fall into this broad category. |

![Formula Alert Dialog](./images/formula-alert-dialog.png)

## See Also

* [Editing](./editing)
* [Formatting](./formatting)
* [Open](./open-save#open)
* [Save](./open-save#save)
