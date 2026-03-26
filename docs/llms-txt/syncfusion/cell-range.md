# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/cell-range.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/cell-range.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/cell-range.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/cell-range.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/blazor/cell-range.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/cell-range.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/cell-range.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/cell-range.md

# Cell Range in ASP.NET Core Spreadsheet control

A group of cells in a sheet is known as cell range.

## Wrap text

Wrap text allows you to display large content as multiple lines in a single cell. By default, the wrap text support is enabled. Use the [`allowWrap`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowWrap) property to enable or disable the wrap text support in spreadsheet.

Wrap text can be applied or removed to a cell or range of cells in the following ways,

* Using the `wrap` property in `cell`, you can enable or disable wrap text to a cell at initial load.
* Select or deselect wrap button from ribbon toolbar to apply or remove the wrap text to the selected range.
* Using the `wrap` method, you can apply or remove the wrap text once the component is loaded.

The following code example shows the wrap text functionality in spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet selectedRange="C7" >
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="7" wrap="true"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="7" wrap="true"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="7" wrap="true"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row>
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="7" wrap="true"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column index="1" width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="150"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="180"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

    function created() {
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:H1');
        this.cellFormat({ verticalAlign: 'middle' }, 'A1:H5');
        this.cellFormat({ textAlign: 'center' }, 'A2:B5');
        this.cellFormat({ textAlign: 'center' }, 'D2:D5');
        // To wrap the cells from E2 to E5 range
        this.wrap('E2:E5');
        // To unwrap the H3 cell
        this.wrap('H3', false);
    }
    </script>
{% endhighlight %}
{% highlight c# tabtitle="WrapTextController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { No= "1",  ReleasedOn= "1994",  Title= "Forrest Gump",  Rating= "5 Stars",  Casts= "Tom Hanks, Robin Wright, Gary Sinise",  DirectedBy= "Robert Zemeckis", Genre= "Drama", Comments= "Based on the 1986 novel of the same name by Winston Groom" },
        new { No= "2",  ReleasedOn= "1946",  Title= "Itâs a Wonderful Life",  Rating= "2 Stars",  Casts= "James Stewart, Donna Reed, Lionel Barrymore",  DirectedBy= "Frank Capra", Genre= "Drama", Comments= "Colorized version"  },
        new { No= "3",  ReleasedOn= "1988",  Title= "Big",  Rating= "4 Stars",  Casts= "Tom Hanks, Elizabeth Perkins, Robert Loggia",  DirectedBy= "Penny Marshall", Genre= "Comedy", Comments= "A thirteen-year-old boy wishes to be big, and his wish comes true."  },
        new { No= "4",  ReleasedOn= "1954",  Title= "Rear Window",  Rating= "4 Stars",  Casts= "James Stewart, Grace Kelly, Wendell Corey",  DirectedBy= "Alfred Hitchcock" , Genre= "Suspense", Comments= "Truly suspenseful and masterfully crafted" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



### Limitations of Wrap text

The following features have some limitations in wrap text:

* Sorting with wrap text applied data.
* Merge with wrap text

## Merge cells

Merge cells allows users to span two or more cells in the same row or column into a single cell. When cells with multiple values are merged, top-left most cell data will be the data for the merged cell. By default, the merge cells option is enabled. Use [`allowMerge`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowMerge) property to enable or disable the merge cells option in spreadsheet.

You can merge the range of cells in the following ways,

* Set the `rowSpan` and `colSpan` property in `cell` to merge the number of cells at initial load.
* Select the range of cells and apply merge by selecting the desired option from ribbon toolbar.
* Use `merge` method to merge the range of cells, once the component is loaded.

The available merge options in spreadsheet are,

| Type | Action |
|-------|---------|
| Merge All | Combines all the cells in a range in to a single cell (default). |
| Merge Horizontally | Combines cells in a range as row-wise. |
| Merge Vertically | Combines cells in a range as column-wise. |
| UnMerge | Splits the merged cells into multiple cells. |

The following code example shows the merge cells operation in spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
 <ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet name="Merge Cells" >
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row height="35"></e-spreadsheet-row>
                    <e-spreadsheet-row height="35">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="1" rowSpan="2"></e-spreadsheet-cell>
                            <e-spreadsheet-cell colSpan="2"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="6" colSpan="3"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="10" rowSpan="2" colSpan="3"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="13" colSpan="2"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="17" colSpan="2"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="35">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="3" colSpan="3"></e-spreadsheet-cell>
                            <e-spreadsheet-cell colSpan="4" index="6"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="13" colSpan="3"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="17" colSpan="2"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="35">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="2" colSpan="3"></e-spreadsheet-cell>
                            <e-spreadsheet-cell colSpan="2" index="5"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="7" colSpan="3"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="15" colSpan="2"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="35">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="2" colSpan="3"></e-spreadsheet-cell>
                            <e-spreadsheet-cell colSpan="4" index="6"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="16" colSpan="2"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="35">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="2" colSpan="4"></e-spreadsheet-cell>
                            <e-spreadsheet-cell colSpan="3" index="7"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="15" colSpan="2"></e-spreadsheet-cell>
                            <e-spreadsheet-cell index="17" colSpan="2"></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                    <e-spreadsheet-column width="150"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

      function created() {
       this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:S1');
        this.numberFormat('h:mm AM/PM', 'C1:S1');
        this.cellFormat({ verticalAlign: 'middle' }, 'A1:S11');
        // Merging the `K4:M4` cells using method
        this.merge('K4:M4');
        // Merging the 5th and 6th row cells across 11th, 12th and 13th column
        this.merge('K5:M6', 'Vertically');
        // Merging the 18th and 19th column cells across 2nd, 3rd and 4th row
        this.merge('N4:O6', 'Horizontally');
    }
    </script>
{% endhighlight %}
{% highlight c# tabtitle="MergeCellController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { EmployeeID= "10001",  EmployeeName= "Davolio",  NineAM= "Analysis Task",  NinethirtyAM= "Analysis Task",  TenAM= "Team Meeting",  TenthirtyAM= "Testing", ElevenAM= "Development",  EleventhirtyAM= "Development",  TwelvePM= "Development",  TwelvethirtyPM= "Support", OnePM= "Lunch Break",  OnethirtyPM= "Lunch Break",  TwoPM= "Lunch Break",  TwothirtyPM= "Testing", ThreePM= "Testing",  ThreethirtyPM= "Development",  FourPM= "Conference",  FourthirtyPM= "Team Meeting", FivePM= "Team Meeting" },
        new { EmployeeID= "10002",  EmployeeName= "Buchanan",  NineAM= "Task Assign",  NinethirtyAM= "Support",  TenAM= "Support",  TenthirtyAM= "Support", ElevenAM= "Testing",  EleventhirtyAM= "Testing",  TwelvePM= "Testing",  TwelvethirtyPM= "Testing", OnePM= "Lunch Break",  OnethirtyPM= "Lunch Break",  TwoPM= "Lunch Break",  TwothirtyPM= "Development", ThreePM= "Development",  ThreethirtyPM= "Check Mail",  FourPM= "Check Mail",  FourthirtyPM= "Team Meeting", FivePM= "Team Meeting" },
        new { EmployeeID= "10003",  EmployeeName= "Fuller",  NineAM= "Check Mail",  NinethirtyAM= "Check Mail",  TenAM= "Check Mail",  TenthirtyAM= "Analysis Tasks", ElevenAM= "Analysis Tasks",  EleventhirtyAM= "Support",  TwelvePM= "Support",  TwelvethirtyPM= "Support", OnePM= "Lunch Break",  OnethirtyPM= "Lunch Break",  TwoPM= "Lunch Break",  TwothirtyPM= "Development", ThreePM= "Development",  ThreethirtyPM= "Team Meeting",  FourPM= "Team Meeting",  FourthirtyPM= "Development", FivePM= "Development" },
        new { EmployeeID= "10004",  EmployeeName= "Leverling",  NineAM= "Testing",  NinethirtyAM= "Check Mail",  TenAM= "Check Mail",  TenthirtyAM= "Support", ElevenAM= "Testing",  EleventhirtyAM= "Testing",  TwelvePM= "Testing",  TwelvethirtyPM= "Testing", OnePM= "Lunch Break",  OnethirtyPM= "Lunch Break",  TwoPM= "Lunch Break",  TwothirtyPM= "Development", ThreePM= "Development",  ThreethirtyPM= "Check Mail",  FourPM= "Conference",  FourthirtyPM= "Conference", FivePM= "Team Meeting" },
        new { EmployeeID= "10005",  EmployeeName= "Peacock",  NineAM= "Task Assign",  NinethirtyAM= "Task Assign",  TenAM= "Task Assign",  TenthirtyAM= "Task Assign", ElevenAM= "Check Mail",  EleventhirtyAM= "Support",  TwelvePM= "Support",  TwelvethirtyPM= "Support", OnePM= "Lunch Break",  OnethirtyPM= "Lunch Break",  TwoPM= "Lunch Break",  TwothirtyPM= "Development", ThreePM= "Development",  ThreethirtyPM= "Team Meeting",  FourPM= "Team Meeting",  FourthirtyPM= "Testing", FivePM= "Testing" },
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



### Limitations of Merge

The following features have some limitations in Merge:

* Merge with filter.
* Merge with wrap text.

## Data Validation

Data Validation is used to restrict the user from entering the invalid data. You can use the [`allowDataValidation`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowDataValidation) property to enable or disable data validation.

N> * The default value for `allowDataValidation` property is `true`.

### Apply Validation

You can apply data validation to restrict the type of data or the values that users enter into a cell.

You can apply data validation by using one of the following ways,

* Select the Data tab in the Ribbon toolbar, and then choose the Data Validation item.
* Use the `addDataValidation()` method programmatically.

### Clear Validation

Clear validation feature is used to remove data validations from the specified ranges or the whole worksheet.

You can clear data validation rule by one of the following ways,

* Select the Data tab in the Ribbon toolbar, and then choose the Clear Validation item.
* Use the `removeDataValidation()` method programmatically.

### Highlight Invalid Data

Highlight invalid data feature is used to highlight the previously entered invalid values.

You can highlight an invalid data by using one of the following ways,

* Select the Data tab in the Ribbon toolbar, and then choose the Highlight Invalid Data item.
* Use the `addInvalidHighlight()` method programmatically.

### Clear Highlighted Invalid Data

Clear highlight feature is used to remove the highlight from invalid cells.

You can clear the highlighted invalid data by using the following ways,

* Select the Data tab in the Ribbon toolbar, and then choose the Clear Highlight item.
* Use the `removeInvalidHighlight()` method programmatically.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false">
<e-spreadsheet-sheets>
    <e-spreadsheet-sheet name="PriceDetails">
        <e-spreadsheet-rows>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="Seller Name">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Customer Id">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Customer Name">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Product Name">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Product Price">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Sales Date">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Billing Time">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Total Price">
                        <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                    </e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="John"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="1">
                        <e-cell-validation type="WholeNumber" operator="NotEqualTo" value1="1"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Nash"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Digger">
                        <e-cell-validation type="List" value1="Digger, Digger, Cherrypicker"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="50000">
                        <e-cell-validation type="List" value1="50000,50000,45000"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="04/11/2019"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="11:34:32 AM"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="1,45,000.00"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="Mike"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="2">
                        <e-cell-validation type="WholeNumber" operator="NotEqualTo" value1="1"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Jim"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Cherrypicker">
                        <e-cell-validation type="List" value1="Cherrypicker, JCB, Wheelbarrow"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="45000">
                        <e-cell-validation type="List" value1="45000,90000,40"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="04/11/2019"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="11:34:32 AM"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="1,45,000.00"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="shane"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="3">
                        <e-cell-validation type="WholeNumber" operator="NotEqualTo" value1="1"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Sean"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Kango">
                        <e-cell-validation type="List" value1="Kango, Ropes"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="450">
                        <e-cell-validation type="List" value1="450, 95"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="06/25/2019"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="01:30:11 PM"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="545.00"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
            <e-spreadsheet-row>
                <e-spreadsheet-cells>
                    <e-spreadsheet-cell value="John"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="1">
                        <e-cell-validation type="WholeNumber" operator="NotEqualTo" value1="1"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="Nash"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="JCB">
                        <e-cell-validation type="List" value1="JCB, Ropes, scaffolding"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="90000">
                        <e-cell-validation type="List" value1="90000, 95, 10000"></e-cell-validation>
                    </e-spreadsheet-cell>
                    <e-spreadsheet-cell value="09/22/2019"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="12:30:02 PM"></e-spreadsheet-cell>
                    <e-spreadsheet-cell value="1,00,095.00"></e-spreadsheet-cell>
                </e-spreadsheet-cells>
            </e-spreadsheet-row>
        </e-spreadsheet-rows>
        <e-spreadsheet-columns>
            <e-spreadsheet-column width="88"></e-spreadsheet-column>
            <e-spreadsheet-column width="88"></e-spreadsheet-column>
            <e-spreadsheet-column width="106"></e-spreadsheet-column>
            <e-spreadsheet-column width="98"></e-spreadsheet-column>
            <e-spreadsheet-column width="88"></e-spreadsheet-column>
            <e-spreadsheet-column width="86"></e-spreadsheet-column>
            <e-spreadsheet-column width="107"></e-spreadsheet-column>
            <e-spreadsheet-column width="81"></e-spreadsheet-column>
        </e-spreadsheet-columns>
    </e-spreadsheet-sheet>
</e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>
    function created() {
        //Add Data Validation to range.
        this.addDataValidation({ type: 'TextLength', operator: 'LessThanOrEqualTo', value1: '4' }, 'A2:A5');
        this.addDataValidation({ type: 'WholeNumber', operator: 'NotEqualTo', value1: '1' }, 'B2:B5');
        this.addDataValidation({ type: 'Date', operator: 'NotEqualTo', value1: '04/11/2019' }, 'F2:F5');
        this.addDataValidation({ type: 'Time', operator: 'Between', value1: '10:00:00 AM', value2: '11:00:00 AM' }, 'G2:G5');
        this.addDataValidation({ type: 'Decimal', operator: 'LessThan', value1: '100000.00' }, 'H2:H5');
        //Highlight Invalid Data.
        this.addInvalidHighlight('A1:H5');
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="DataValidation.cs" %}
public IActionResult Index()
{
    return View();
}
{% endhighlight %}
{% endtabs %}

### Custom Data validation

The Spreadsheet supports custom data validation, allowing users to define their own validation rules for specific cells or ranges. This feature enables you to set conditions that the entered data must meet, making it particularly useful when predefined validation options, such as numbers, dates, or lists, are insufficient.

With custom validation, you can enforce rules using logical expressions or formulas, ensuring that only valid data is entered into the Spreadsheet.

For example, consider a scenario where you want to ensure that a cell contains a number between 10 and 100. To achieve this, define a validation rule using a formula that checks if the entered value is greater than 10 and less than 100. The formula for this validation is =AND(A1>10, A1<100), where A1 refers to the cell being validated.

When this rule is applied, the Spreadsheet evaluates the entered value against the formula. If a user enters a value outside the specified range, an alert notifies them of the invalid input. This helps users correct errors efficiently and ensures that only desired values are accepted.

You can apply custom data validation using two methods.

* The first is through the Data Validation dialog in the Ribbon toolbar. Navigate to the Data tab, select the Data Validation option, and choose the Custom type from the Allow dropdown menu.
* The second method is programmatically, using the `addDataValidation()` method, which allows developers to set custom rules dynamically via code.

The following code example demonstrates how to add custom data validation with a formula in a Spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet name="PriceDetails">
            <e-spreadsheet-rows>
                <e-spreadsheet-row>
                    <e-spreadsheet-cells>
                        <e-spreadsheet-cell value="Seller Name">
                            <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Customer Id">
                            <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Customer Name">
                            <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Product Name">
                            <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Product Price">
                            <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Total Price">
                            <e-spreadsheet-cellstyle fontWeight="Bold" textAlign="Center"></e-spreadsheet-cellstyle>
                        </e-spreadsheet-cell>
                    </e-spreadsheet-cells>
                </e-spreadsheet-row>
                <e-spreadsheet-row>
                    <e-spreadsheet-cells>
                        <e-spreadsheet-cell value="John"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="101">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Nash"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Digger">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="50000">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="1,45,000.00"></e-spreadsheet-cell>
                    </e-spreadsheet-cells>
                </e-spreadsheet-row>
                <e-spreadsheet-row>
                    <e-spreadsheet-cells>
                        <e-spreadsheet-cell value="Mike"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="25">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Jim"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Cherrypicker">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="45000">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="1,45,000.00"></e-spreadsheet-cell>
                    </e-spreadsheet-cells>
                </e-spreadsheet-row>
                <e-spreadsheet-row>
                    <e-spreadsheet-cells>
                        <e-spreadsheet-cell value="shane"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="35">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Sean"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Kango">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="35000">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="1,54,500.00"></e-spreadsheet-cell>
                    </e-spreadsheet-cells>
                </e-spreadsheet-row>
                <e-spreadsheet-row>
                    <e-spreadsheet-cells>
                        <e-spreadsheet-cell value="John"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="101">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="Nash"></e-spreadsheet-cell>
                        <e-spreadsheet-cell value="JCB">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="90000">
                        </e-spreadsheet-cell>
                        <e-spreadsheet-cell value="1,00,095.00"></e-spreadsheet-cell>
                    </e-spreadsheet-cells>
                </e-spreadsheet-row>
            </e-spreadsheet-rows>
            <e-spreadsheet-columns>
                <e-spreadsheet-column width="88"></e-spreadsheet-column>
                <e-spreadsheet-column width="88"></e-spreadsheet-column>
                <e-spreadsheet-column width="106"></e-spreadsheet-column>
                <e-spreadsheet-column width="98"></e-spreadsheet-column>
                <e-spreadsheet-column width="88"></e-spreadsheet-column>
                <e-spreadsheet-column width="81"></e-spreadsheet-column>
            </e-spreadsheet-columns>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>
    function created() {
        var spreadsheet = document.getElementById("spreadsheet").ej2_instances[0];
        //Add Data Validation to range.
        spreadsheet.addDataValidation({ type: 'Custom', value1: '=AND(B2>10, B2<100)' }, 'E2:E5');
        //Highlight Invalid Data.
        spreadsheet.addInvalidHighlight('E2:E5');
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="DataValidation.cs" %}
public IActionResult Index()
{
    return View();
}
{% endhighlight %}
{% endtabs %}

### Limitations of Data validation

The following features have some limitations in Data Validation:

* Entire row data validation.
* Insert row between the data validation.
* Copy/paste with data validation.
* Delete cells between data validation applied range.

## Auto Fill

Auto Fill is used to fill the cells with data based on adjacent cells. It also follows a pattern from adjacent cells if available. There is no need to enter the repeated data manually. You can use [`allowAutoFill`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowAutoFill) property to enable/disable the auto fill support. You can also use `showFillOptions` property to enable/disable the fill option and `fillType` property to change the default auto fill option which is available in [`autoFillSettings`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AutoFillSettings).

You can do this by one of the following ways,

* Using âAutoFillOptionsâ menu which is open, while drag and drop the cell using fill handle element.
* Use the autoFill() method programmatically.

The available parameters in `autoFill()` method are,

| Parameter | Type | Description |
|-----|------|----|
| dataRange | `string` | Specifies the data range. |
| fillRange | `string` | Specifies the fill range. |
| direction | `AutoFillDirection` | Specifies the direction("Up","Right","Down","Left")to be filled. |
| fillType | `AutoFillType` | Specifies the fill type("CopyCells","FillSeries","FillFormattingOnly","FillWithoutFormatting") for autofill action. |

In Auto Fill we have following options,

* Copy Cells
* Fill Series
* Fill Formatting Only
* Fill Without Formatting

N>* The default auto fill option is âFillSeriesâ which can be referred from `fillType` property.

### Copy Cells

To copy the selected cell content to the adjacent cells. You can do this by one of the following ways,

* Using fill handle to select the adjacent cell range and âCopy Cellsâ option in âAutoFillOptionsâ menu to fill the adjacent cells.
* Using âCopyCellsâ as fill type in `autoFill` method to fill the adjacent cells.

### Fill Series

To fill the series of numbers, characters, or dates based on selected cell content to the adjacent cells with their formats.

You can do this by one of the following ways,

* Using fill handle to select the adjacent cell range and âFill Seriesâ option in âAutoFillOptionsâ menu to fill the adjacent cells.
* Using âFillSeriesâ as fill type in `autoFill` method to fill the adjacent cells.

### Fill Formatting Only

To fill the cell style and number formatting based on the selected cell content to the adjacent cells without their content.

You can do this by one of the following ways,

* Using fill handle to select the adjacent cell range and âFill Formatting Onlyâ option in âAutoFillOptionsâ menu to fill the adjacent cells.
* Using âFillFormattingOnlyâ as fill type in `autoFill` method to fill the adjacent cells.

### Fill Without Formatting

To fill series of numbers, characters, or dates based on the selected cells to the adjacent cells without their formats.

You can do this by one of the following ways,

* Using fill handle to select the adjacent cell range and âFill Without Formattingâ option in âAutoFillOptionsâ menu to fill the adjacent cells.
* Using âFillWithoutFormattingâ as fill type in `autoFill` method to fill the adjacent cells.

In the following sample, you can enable/disable the fill option on the button click event byÂ using the `showFillOptions` property inÂ `autoFillSettings`.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="showfillbtn" content="Change showFillOptions"></ejs-button>
<ejs-spreadsheet id="spreadsheet" created="created">
            <e-spreadsheet-sheets>
                <e-spreadsheet-sheet name="Price Details">
					<e-spreadsheet-rows>
						<e-spreadsheet-row height=30>
						</e-spreadsheet-row>
					</e-spreadsheet-rows>
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
    function created() {
		this.cellFormat({ backgroundColor: '#357cd2', color: '#fff', fontWeight: 'bold', textAlign: 'center' }, 'A1:H1');
        this.autoFill('D4:D11', 'D2:D3', 'Down', 'CopyCells');
		this.autoFill('E4:E11', 'E2:E3', 'Down', 'FillSeries');
		this.autoFill('B4:B11', 'B2:B3', 'Down', 'FillFormattingOnly');
		this.autoFill('C4:C11', 'C2:C3', 'Down', 'FillWithoutFormatting');
    }
	 document.getElementById("showfillbtn").addEventListener('click', function () {
            var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
			var showFillOptions = spreadsheetObj.autoFillSettings.showFillOptions;
            spreadsheetObj.autoFillSettings.showFillOptions = !showFillOptions;
        });
    </script>

{% endhighlight %}
{% highlight c# tabtitle="AutofillController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
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
    ViewBag.DefaultData = data;
    return View();

}
{% endhighlight %}
{% endtabs %}



## Clear

Clear feature helps you to clear the cell contents (formulas and data), formats (including number formats, conditional formats, and borders) in a spreadsheet. When you apply clear all, both the contents and the formats will be cleared simultaneously.

### Apply Clear Feature

You can apply clear feature by using one of the following ways,

* Select the clear icon in the Ribbon toolbar under the Home Tab.
* Using the `clear()` method to clear the values.

Clear has the following types in the spreadsheet,

| Options | Uses |
|-----|------|
| `Clear All` | Used to clear all contents, formats, and hyperlinks.  |
| `Clear Formats` | Used to clear the formats (including number formats, conditional formats, and borders) in a cell. |
| `Clear Contents` | Used to clear the contents (formulas and data) in a cell. |
| `Clear Hyperlinks` | Used to clear the hyperlink in a cell. |

### Methods

Clear the cell contents and formats in the Spreadsheet document by using the `clear` method. The clear method has `type` and `range` as parameters. The following code example shows how to clear the cell contents and formats in the button click event.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-dropdownbutton id="element" content="Clear" items="ViewBag.items" select="itemSelect"></ejs-dropdownbutton>
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
        this.cellFormat({ fontWeight: 'bold', fontSize: '12pt'}, 'A1:F1');
        this.cellFormat({ color: '#10c469' }, 'B1:B10');
    }

    function itemSelect(args) {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        if (args.item.text === 'Clear All')
      spreadsheet.clear({ type: 'Clear All', range: 'D1:D10' }); // Clear the content, formats and hyperlinks applied in the provided range.
    if (args.item.text === 'Clear Formats')
      spreadsheet.clear({ type: 'Clear Formats', range: 'B1:B10' }); // Clear the formats applied in the provided range
    if (args.item.text === 'Clear Contents')
      spreadsheet.clear({ type: 'Clear Contents', range: 'A1:A10' }); // Clear the content in the provided range
    if (args.item.text === 'Clear Hyperlinks')
      spreadsheet.clear({ type: 'Clear Hyperlinks', range: 'F2:F6' }); // Clear the hyperlinks applied in the provided range
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="ClearController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { OrderID= "10248",  CustomerID= "VINET",  EmployeeID= "5",  ShipName= "Vins et alcools Chevalier",  ShipCity= "Reims",  Website= "https://www.amazon.com/" },
        new { OrderID= "10249",  CustomerID= "TOMSP",  EmployeeID= "6",  ShipName= "Toms SpezialitÃ¤ten",  ShipCity= "MÃ¼nster",  Website= "https://www.overstock.com/" },
        new { OrderID= "10250",  CustomerID= "HANAR",  EmployeeID= "4",  ShipName= "Hanari Carnes",  ShipCity= "Rio de Janeiro",  Website= "https://www.aliexpress.com/" },
        new { OrderID= "10251",  CustomerID= "VICTE",  EmployeeID= "3",  ShipName= "Victuailles en stock",  ShipCity= "Lyon",  Website= "http://www.alibaba.com/" },
        new { OrderID= "10252",  CustomerID= "SUPRD",  EmployeeID= "4",  ShipName= "SuprÃªmes dÃ©lices",  ShipCity= "Charleroi",  Website= "https://taobao.com/" },
        
    };
    List<object> items = new List<object>();
    items.Add(new
    {
        text = "Clear All"
    });
    items.Add(new
    {
        text = "Clear Formats"
    });
    items.Add(new
    {
        text = "Clear Contents"
    });
    items.Add(new
    {
        text = "Clear Hyperlinks"
    });
    ViewBag.items = items;
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



## See Also

* [Rows and columns](./rows-and-columns)
* [Formatting](./formatting)
* [Hyperlink](./link)
* [Sorting](./sort)
* [Filtering](./filter)
