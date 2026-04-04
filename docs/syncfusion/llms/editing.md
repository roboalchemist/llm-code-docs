# Source: https://docs.syncfusion.com/flutter/datagrid/editing.md

# Source: https://docs.syncfusion.com/uwp/treegrid/editing.md

# Source: https://docs.syncfusion.com/uwp/datagrid/editing.md

# Source: https://docs.syncfusion.com/uwp/cellgrid/editing.md

# Source: https://docs.syncfusion.com/winui/treeview/editing.md

# Source: https://docs.syncfusion.com/winui/treegrid/editing.md

# Source: https://docs.syncfusion.com/winui/datagrid/editing.md

# Source: https://docs.syncfusion.com/winui/combobox/editing.md

# Source: https://docs.syncfusion.com/windowsforms/treeview/editing.md

# Source: https://docs.syncfusion.com/windowsforms/datagrid/editing.md

# Source: https://docs.syncfusion.com/windowsforms/combobox/editing.md

# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/editing.md

# Source: https://docs.syncfusion.com/windowsforms/grid-control/editing.md

# Source: https://docs.syncfusion.com/windowsforms/syntax-editor/editing.md

# Source: https://docs.syncfusion.com/wpf/treeview/editing.md

# Source: https://docs.syncfusion.com/wpf/treegrid/editing.md

# Source: https://docs.syncfusion.com/wpf/pivot-grid/editing.md

# Source: https://docs.syncfusion.com/wpf/gridcontrol/editing.md

# Source: https://docs.syncfusion.com/wpf/datagrid/editing.md

# Source: https://docs.syncfusion.com/maui/datagrid/editing.md

# Source: https://docs.syncfusion.com/maui/dataform/editing.md

# Source: https://docs.syncfusion.com/maui/combobox/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/wpf/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/winforms/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/uwp/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/blazor/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/editing.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/editing.md

# Editing in ASP.NET Core Spreadsheet control

You can edit the contents of a cell directly in the cell or by typing in the formula bar. By default, the editing feature is enabled in the spreadsheet. Use the [`allowEditing`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowEditing) property to enable or disable the editing feature.

## Edit cell

You can start editing by one of the following ways,

* Double click a cell to start the edit mode.
* Press `F2` key to edit the active cell.
* Use formula bar to perform editing.
* Use `BACKSPACE` or `SPACE` key to clear the cell content and start the edit mode.
* Using the `startEdit` method.

## Save cell

If the cell is in editable state, you can save the edited cell by one of the following ways,

* Perform mouse click on any other cell rather than the current editing cell.
* Press `Enter` or `Tab` keys to save the edited cell content.
* Using the `endEdit` method.

## Cancel editing

To cancel the editing without saving the changes, you can use one of the following ways,

* Press `ESCAPE` key, this will remove the editable state and update the unchanged cell content.
* Using the `closeEdit` method.

The following sample shows how to prevent the editing and cell save. Here `E` column prevent the editing by using cancel argument as true in [`cellEdit`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_CellEdit) event. In `D` column, prevent saving the edited changes by using cancel argument as true in [`beforeCellSave`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeCellSave) and use `closeEdit` method in spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
 <ejs-spreadsheet id="spreadsheet" created="created" cellEdit="cellEdit" beforeCellSave="beforeCellSave" showSheetTabs="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet selectedRange="C7" >
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row index="10">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="3" value="Total Amount:">
                                <e-spreadsheet-cellstyle fontWeight="Bold"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(E2:E10"></e-spreadsheet-cell>
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


    <script>

      
  
    function created() {
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:E1');
        this.cellFormat({ textAlign: 'center' }, 'A2:A10');
        this.cellFormat({ textAlign: 'center' }, 'C2:C10');
        this.numberFormat('$#,##0.00', 'D2:D10');
        this.numberFormat('$#,##0.00', 'E2:E11');
    }
    function cellEdit(args) {
        // Preventing the editing in 5th(Amount) column.
        if (args.address.includes('E')) { args.cancel = true; }
    }
    function beforeCellSave(args) {
        // Prevent saving the edited changes in 4th(Rate) column.
        if (args.address.includes('D')) {
            args.cancel = true;
            // Manually removes the editable state without saving the changes. Use `endEdit` method if you want to save the changes.
            this.closeEdit();
        }
    }
    </script>
{% endhighlight %}
{% highlight c# tabtitle="EditingController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { ItemCode= "I231",  ItemName= "Chinese Combo Noodle",  Quantity= "2",  Rate= "125",  Amount= "=PRODUCT(C2,D2)"},
        new { ItemCode= "I245",  ItemName= "Chinese Combo Rice",  Quantity= "3",  Rate= "125",  Amount= "=PRODUCT(C3,D3)"},
        new { ItemCode= "I237",  ItemName= "Amritsari Chola",  Quantity= "2",  Rate= "225",  Amount= "=PRODUCT(C4,D4)"},
        new { ItemCode= "I291",  ItemName= "Asian Mixed Entree Platt",  Quantity= "3",  Rate= "165",  Amount= "=PRODUCT(C5,D5)"},
        new { ItemCode= "I268",  ItemName= "Chinese Combo Chicken",  Quantity= "3",  Rate= "125",  Amount= "=PRODUCT(C6,D6)"},
        new { ItemCode= "I251",  ItemName= "Chivas Regal",  Quantity= "1",  Rate= "325",  Amount= "=PRODUCT(C7,D7)"},
        new { ItemCode= "I256",  ItemName= "Chicken Drumsticks",  Quantity= "2",  Rate= "180",  Amount= "=PRODUCT(C8,D8)"},
        new { ItemCode= "I232",  ItemName= "Manchow Soup",  Quantity= "2",  Rate= "160",  Amount= "=PRODUCT(C9,D9)"},
        new { ItemCode= "I290",  ItemName= "Schezuan Chicken",  Quantity= "3",  Rate= "180",  Amount= "=PRODUCT(C10,D10)"},
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



## Limitations

* Text overflow in cells is not supported in Editing.

## See Also

* [Cell range](./cell-range)
* [Formatting](./formatting)
* [Hyperlink](./link)
* [Undo and Redo](./undo-redo)
* [Unlock the particular cells in the protected sheet](./protect-sheet#unlock-the-particular-cells-in-the-protected-sheet)
