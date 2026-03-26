# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/protect-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/protect-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/protect-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/protect-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/protect-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/protect-sheet.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/protect-sheet.md

# Protection in ASP.NET Core Spreadsheet Control

Sheet protection helps you to prevent the users from modifying the data in the spreadsheet.

## Protect Sheet

Protect sheet feature helps you to prevent the unknown users from accidentally changing, editing, moving, or deleting data in a spreadsheet. And you can also protect the sheet with password. You can use the [`isProtected`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_IsProtected) property to enable or disable the Protecting functionality.

N> The default value for `isProtected` property is `false`.

By default in protected sheet, selecting, formatting, inserting, deleting functionalities are disabled. To enable some of the above said functionalities the `protectSettings` options are used in a protected spreadsheet.

The available `protectSettings` options in spreadsheet are,

| Options | Uses |
|-----|------|
| `Select Cells` | Used to perform Cell Selection. |
| `Format Cells` | Used to perform Cell formatting. |
| `Format Rows` | Used to perform Row formatting. |
| `Format Columns` | Used to perform Column formatting. |
| `Insert Link` | Used to perform Hyperlink Insertions. |

N> * The default value for all `protectSettings` options are `false`.

By default, the `Protect Sheet` module is injected internally into the Spreadsheet to perform sheet protection function.

**User Interface**:

In the active Spreadsheet, the sheet protection can be done by any of the following ways:

* Select the Protect Sheet item in the Ribbon toolbar under the Data Tab, and then select your desired options.
* Right-click the sheet tab, select the Protect Sheet item in the context menu, and then select your desired options.
* Use the `protectSheet()` method programmatically.

The following example shows `Protect Sheet` functionality with password in the Spreadsheet control.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
    <ejs-spreadsheet id="spreadsheet" dataBound="dataBound">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet isProtected="true" name="Budget">
                <e-spreadsheet-protect-settings selectCells="true"></e-spreadsheet-protect-settings>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.budgetData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
            <e-spreadsheet-sheet name="Salary">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.salaryData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>

 

    <script>

      function dataBound() {
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:D1');
        this.cellFormat({ fontWeight: 'bold'}, 'A11:D11');
        this.protectSheet(1, { selectCells: false}, "syncfusion"); // protect sheet with password
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="ProtectSheetController.cs" %}
public IActionResult Index()
{
   List<object> data1 = new List<object>()
   {
      new { ExpenseType= "Housing",  ProjectedCost= "7000",  ActualCost= "7500",  Difference= "-500"},
      new { ExpenseType= "Transportation",  ProjectedCost= "500",  ActualCost= "500",  Difference= "0"},
      new { ExpenseType= "Insurance",  ProjectedCost= "1000",  ActualCost= "1000",  Difference= "0"},
      new { ExpenseType= "Food",  ProjectedCost= "2000",  ActualCost= "1800",  Difference= "200"},
      new { ExpenseType= "Pets",  ProjectedCost= "300",  ActualCost= "200",  Difference= "100"},
      new { ExpenseType= "Personel Care",  ProjectedCost= "500",  ActualCost= "500",  Difference= "0"},
      new { ExpenseType= "Loan",  ProjectedCost= "1000",  ActualCost= "1000",  Difference= "0"},
      new { ExpenseType= "Tax",  ProjectedCost= "200",  ActualCost= "200",  Difference= "0"},
      new { ExpenseType= "Savings",  ProjectedCost= "1000",  ActualCost= "900",  Difference= "100"},
      new { ExpenseType= "Total",  ProjectedCost= "13500",  ActualCost= "13600",  Difference= "-100"},
   };
   List<object> data2 = new List<object>()
   {
         new { Earnings= "Basic",  CreditAmount= "20000",  Deductions= "Provident Fund",  DebitAmount= "2400"},
      new { Earnings= "HRA",  CreditAmount= "8000",  Deductions= "ESI",  DebitAmount= "0"},
      new { Earnings= "Special Allowance",  CreditAmount= "25000",  Deductions= "Professional Tax",  DebitAmount= "200"},
      new { Earnings= "Incentives",  CreditAmount= "2000",  Deductions= "TDS",  DebitAmount= "2750"},
      new { Earnings= "Bonus",  CreditAmount= "1500",  Deductions= "Other Deduction",  DebitAmount= "0"},
      new { Earnings= "Total Earnings",  CreditAmount= "56500",  Deductions= "Total Deductions",  DebitAmount= "5350"},
   };
   ViewBag.budgetData = data1;
   ViewBag.salaryData = data2;
   return View();
}
{% endhighlight %}
{% endtabs %}



### Limitations of Protect sheet

* Password encryption is not supported

## Unprotect Sheet

Unprotect sheet is used to enable all the functionalities that are already disabled in a protected spreadsheet.

**User Interface**:

In the active Spreadsheet, the sheet can be unprotected by any of the following ways:

* Select the `Unprotect Sheet` item in the Ribbon toolbar under the Data Tab.
* Right-click the sheet tab, select the `Unprotect Sheet` item in the context menu.
* Use the `unprotectSheet()` method programmatically.

## Unlock the particular cells in the protected sheet

In protected spreadsheet, to make some particular cell or range of cells are editable, you can use `lockCells()` method, with the parameter `range` and `isLocked` property as false.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
    <button id="customBtn" class="e-btn"> Unlock cells</button>
    <ejs-spreadsheet id="spreadsheet" dataBound="dataBound">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet isProtected="true" name="Budget">
                <e-spreadsheet-protect-settings selectCells="true"></e-spreadsheet-protect-settings>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.budgetData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
            <e-spreadsheet-sheet name="Salary">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.salaryData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>

<ejs-dialog id="defaultDialog" header="Spreadsheet" target="#spreadsheet" content="'A1:F3' range of cells has been unlocked." showCloseIcon="true" isModal="true" visible="false" width="500px" buttons="ViewBag.DefaultButtons"></ejs-dialog>
 

    <script>

        document.getElementById("customBtn").addEventListener('click', showAlert);
        function dataBound() {
            this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:D1');
            this.cellFormat({ fontWeight: 'bold' }, 'A11:D11');
        }
        function lockCells() {
            var spreadsheetObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
            var dialogObj = ej.base.getComponent(document.getElementById('defaultDialog'), 'dialog');
            spreadsheetObj.lockCells('A1:F3', false);
            dialogObj.hide();
        }
        function showAlert() {
            var dialogObj = ej.base.getComponent(document.getElementById('defaultDialog'), 'dialog');
            dialogObj.show();
        }
    </script>
{% endhighlight %}
{% highlight c# tabtitle="LockCellController.cs" %}
public ActionResult Index()
{
    List<object> data1 = new List<object>()
    {
        new { ExpenseType= "Housing",  ProjectedCost= "7000",  ActualCost= "7500",  Difference= "-500"},
        new { ExpenseType= "Transportation",  ProjectedCost= "500",  ActualCost= "500",  Difference= "0"},
        new { ExpenseType= "Insurance",  ProjectedCost= "1000",  ActualCost= "1000",  Difference= "0"},
        new { ExpenseType= "Food",  ProjectedCost= "2000",  ActualCost= "1800",  Difference= "200"},
        new { ExpenseType= "Pets",  ProjectedCost= "300",  ActualCost= "200",  Difference= "100"},
        new { ExpenseType= "Personel Care",  ProjectedCost= "500",  ActualCost= "500",  Difference= "0"},
        new { ExpenseType= "Loan",  ProjectedCost= "1000",  ActualCost= "1000",  Difference= "0"},
        new { ExpenseType= "Tax",  ProjectedCost= "200",  ActualCost= "200",  Difference= "0"},
        new { ExpenseType= "Savings",  ProjectedCost= "1000",  ActualCost= "900",  Difference= "100"},
        new { ExpenseType= "Total",  ProjectedCost= "13500",  ActualCost= "13600",  Difference= "-100"},
    };
    List<object> data2 = new List<object>()
    {
        new { Earnings= "Basic",  CreditAmount= "20000",  Deductions= "Provident Fund",  DebitAmount= "2400"},
        new { Earnings= "HRA",  CreditAmount= "8000",  Deductions= "ESI",  DebitAmount= "0"},
        new { Earnings= "Special Allowance",  CreditAmount= "25000",  Deductions= "Professional Tax",  DebitAmount= "200"},
        new { Earnings= "Incentives",  CreditAmount= "2000",  Deductions= "TDS",  DebitAmount= "2750"},
        new { Earnings= "Bonus",  CreditAmount= "1500",  Deductions= "Other Deduction",  DebitAmount= "0"},
        new { Earnings= "Total Earnings",  CreditAmount= "56500",  Deductions= "Total Deductions",  DebitAmount= "5350"},
    };
    List<DialogDialogButton> buttons = new List<DialogDialogButton>() { };
    buttons.Add(new DialogDialogButton() { Click = "lockCells", ButtonModel = new DefaultButtonModel() { content = "OK", isPrimary = true } });
    ViewBag.DefaultButtons = buttons;
    ViewBag.budgetData = data1;
    ViewBag.salaryData = data2;
    return View();
}

public class DefaultButtonModel
{
    public string content { get; set; }
    public bool isPrimary { get; set; }
}
{% endhighlight %}
{% endtabs %}

## Make cells read-only without protecting worksheet

Previously, you could make cells read-only by protecting the entire sheet using the `protectSheet` method or through the UI option. Meanwhile, to make a specific range of cells editable within a protected sheet, you needed to use the `lockCells` method, passing the `range` parameter and setting the `isLocked` property to **false**. 

Now, you can make an entire row, an entire column, or a specific range of cells read-only using the `setRangeReadOnly` method without protecting the entire sheet. This method accepts three parameters, as detailed in the following table:

| Parameter | Description |
|-----|------|
| `readOnly` | Specifies whether an entire row, an entire column, or a specific range of cells should be set as read-only (**true**) or editable (**false**). |.
| `range` | Specifies the particular range of cells to be set as read-only. |
| `sheetIndex` | Specifies the index of the sheet. |

You can make an entire row, an entire column, or a specific range of cells read-only by passing the range as shown in the code snippet below:

```js
// To set read-only for single cell.
spreadsheet.setRangeReadOnly(true, 'A2', 0)
// To set read-only for range of cells.
spreadsheet.setRangeReadOnly(true, 'A2:B5', 0)
// To set read-only for entire row.
spreadsheet.setRangeReadOnly(true, '3:3', 0)
// To set read-only for entire column.
spreadsheet.setRangeReadOnly(true, 'A:A', 0)
```

You can make the cells read-only in the cell data binding by setting the `isReadOnly` property to **true** for the respective rows, columns, and cells.

The following example demonstrates how to make rows, columns, and cells read-only without protecting the sheet:

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="fullRow" content="Make row 2 Read Only"></ejs-button>
<ejs-button id="fullCol" content="Make Column A Read Only"></ejs-button>
<ejs-button id="singleCell" content="Make E5 cell Read Only"></ejs-button>
<ejs-button id="removeAll" content="Remove Read Only"></ejs-button>
<ejs-spreadsheet id="spreadsheet" openUrl="Home/Open">
            <e-spreadsheet-sheets>
                <e-spreadsheet-sheet name="Price Details">
                    <e-spreadsheet-ranges>
                        <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A1"></e-spreadsheet-range>
                    </e-spreadsheet-ranges>
                    <e-spreadsheet-rows>
						<e-spreadsheet-row index="3" isReadOnly="true"></e-spreadsheet-row>
                        <e-spreadsheet-row index="4">
                            <e-spreadsheet-cells>
                                <e-spreadsheet-cell index="5" isReadOnly="true"></e-spreadsheet-cell>
                            </e-spreadsheet-cells>
                        </e-spreadsheet-row>
                    </e-spreadsheet-rows>
					<e-spreadsheet-columns>
						<e-spreadsheet-column width="130"></e-spreadsheet-column>
						<e-spreadsheet-column width="100"></e-spreadsheet-column>
						<e-spreadsheet-column width="100" isReadOnly="true"></e-spreadsheet-column>
					</e-spreadsheet-columns>
                </e-spreadsheet-sheet>
            </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>

// To make row 2 readonly.
    document.getElementById("fullRow").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        spreadsheetObj.setRangeReadOnly(true, '2:2', spreadsheetObj.activeSheetIndex);
    });
    // To make Column A readonly.
    document.getElementById("fullCol").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        spreadsheetObj.setRangeReadOnly(true, 'A:A', spreadsheetObj.activeSheetIndex);
    });
    // To make E5 cell readonly.
    document.getElementById("singleCell").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        spreadsheetObj.setRangeReadOnly(true, 'E5:E5', spreadsheetObj.activeSheetIndex);
    });
    // To remove readonly.
    document.getElementById("removeAll").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        spreadsheetObj.setRangeReadOnly(false, '2:2', spreadsheetObj.activeSheetIndex);
        spreadsheetObj.setRangeReadOnly(false, 'A:A', spreadsheetObj.activeSheetIndex);
        spreadsheetObj.setRangeReadOnly(false, 'E5:E5', spreadsheetObj.activeSheetIndex);
    });
</script>

{% endhighlight %}
{% highlight c# tabtitle="ReadOnlyController.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}

public IActionResult Save(SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}

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
    return View();

}
{% endhighlight %}
{% endtabs %}

## Protect Workbook

Protect workbook feature helps you to protect the workbook so that users cannot insert, delete, rename, hide the sheets in the spreadsheet.

You can use the [`password`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_Password) property to protect workbook with password.

You can use the [`isProtected`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_IsProtected) property to protect or unprotect the workbook without the password.

N> The default value for `isProtected` property is `false`.

**User Interface**:

In the active Spreadsheet, you can protect the worksheet by selecting the Data tab in the Ribbon toolbar and choosing the `Protect Workbook` item. Then, enter the password and confirm it and click on OK.

The following example shows `Protect Workbook` by using the [`isProtected`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_IsProtected) property in the Spreadsheet control.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
    <ejs-spreadsheet id="spreadsheet" isProtected="true" dataBound="dataBound">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet name="Budget">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.budgetData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

      function dataBound() {
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:D1');
        this.cellFormat({ fontWeight: 'bold'}, 'A11:D11');
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="ProtectWorkbookController.cs" %}
public IActionResult Index()
{
   List<object> data = new List<object>()
   {
      new { ExpenseType= "Housing",  ProjectedCost= "7000",  ActualCost= "7500",  Difference= "-500"},
      new { ExpenseType= "Transportation",  ProjectedCost= "500",  ActualCost= "500",  Difference= "0"},
      new { ExpenseType= "Insurance",  ProjectedCost= "1000",  ActualCost= "1000",  Difference= "0"},
      new { ExpenseType= "Food",  ProjectedCost= "2000",  ActualCost= "1800",  Difference= "200"},
      new { ExpenseType= "Pets",  ProjectedCost= "300",  ActualCost= "200",  Difference= "100"},
      new { ExpenseType= "Personel Care",  ProjectedCost= "500",  ActualCost= "500",  Difference= "0"},
      new { ExpenseType= "Loan",  ProjectedCost= "1000",  ActualCost= "1000",  Difference= "0"},
      new { ExpenseType= "Tax",  ProjectedCost= "200",  ActualCost= "200",  Difference= "0"},
      new { ExpenseType= "Savings",  ProjectedCost= "1000",  ActualCost= "900",  Difference= "100"},
      new { ExpenseType= "Total",  ProjectedCost= "13500",  ActualCost= "13600",  Difference= "-100"},
   };
   ViewBag.budgetData = data;
   return View();
}
{% endhighlight %}
{% endtabs %}



The following example shows `Protect Workbook` by using the [`password`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_Password) property in the Spreadsheet control. To unprotect the workbook, click the unprotect workbook button in the data tab and provide the password as Syncfusion<sup style="font-size:70%">&reg;</sup> in the dialog box.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
    <ejs-spreadsheet id="spreadsheet" password="syncfusion" dataBound="dataBound">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet name="Budget">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.budgetData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>

 

    <script>

      function dataBound() {
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:D1');
        this.cellFormat({ fontWeight: 'bold'}, 'A11:D11');
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="PasswordController.cs" %}
public IActionResult Index()
{
   List<object> data = new List<object>()
   {
      new { ExpenseType= "Housing",  ProjectedCost= "7000",  ActualCost= "7500",  Difference= "-500"},
      new { ExpenseType= "Transportation",  ProjectedCost= "500",  ActualCost= "500",  Difference= "0"},
      new { ExpenseType= "Insurance",  ProjectedCost= "1000",  ActualCost= "1000",  Difference= "0"},
      new { ExpenseType= "Food",  ProjectedCost= "2000",  ActualCost= "1800",  Difference= "200"},
      new { ExpenseType= "Pets",  ProjectedCost= "300",  ActualCost= "200",  Difference= "100"},
      new { ExpenseType= "Personel Care",  ProjectedCost= "500",  ActualCost= "500",  Difference= "0"},
      new { ExpenseType= "Loan",  ProjectedCost= "1000",  ActualCost= "1000",  Difference= "0"},
      new { ExpenseType= "Tax",  ProjectedCost= "200",  ActualCost= "200",  Difference= "0"},
      new { ExpenseType= "Savings",  ProjectedCost= "1000",  ActualCost= "900",  Difference= "100"},
      new { ExpenseType= "Total",  ProjectedCost= "13500",  ActualCost= "13600",  Difference= "-100"},
   };
   ViewBag.budgetData = data;
   return View();
}
{% endhighlight %}
{% endtabs %}



## Unprotect Workbook

Unprotect Workbook is used to enable the insert, delete, rename, move, copy, hide or unhide sheets feature  in the spreadsheet.

**User Interface**:

In the active Spreadsheet, the workbook can be unprotected in any of the following ways:

* Select the `Unprotect Workbook` item in the Ribbon toolbar under the Data Tab and provide the valid password in the dialog box.

## See Also

* [Hyperlink](./link)