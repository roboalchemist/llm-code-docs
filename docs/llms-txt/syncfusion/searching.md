# Source: https://docs.syncfusion.com/winui/combobox/searching.md

# Source: https://docs.syncfusion.com/windowsforms/html-viewer/searching.md

# Source: https://docs.syncfusion.com/maui/combobox/searching.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/searching.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/searching.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/searching.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/searching.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/searching.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/searching.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/searching.md

# Find and Replace in ASP.NET Core Spreadsheet control

Find and Replace helps you to search for the target text and replace the found text with alternative text within the sheet or workbook. You can use the [`allowFindAndReplace`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowFindAndReplace) property to enable or disable the Find and Replace functionality.

N> * The default value for `allowFindAndReplace` property is `true`.

## Find

Find feature is used to select the matched contents of a cell within the sheet or workbook. It is extremely useful when working with large set of data source.

**User Interface**:

Find can be done by any of the following ways:

* Select the Search icon in the Ribbon toolbar or use `Ctrl + F` key to open the Find dialog.
* Use find Next and find Previous buttons to search the given value in the workbook.
* Select the option button in Find dialog to open the Find and Replace dialog. Then, select the below properties for enhanced searching.

N> * `Search within`: To search the target in a sheet (default) or in an entire workbook.
<br/> * `Search by`: It enhance the search, either By Rows (default), or By Columns.
<br/> * `Match case`: To find the matched value with case sensitive.
<br/> * `Match exact cell contents`: To find the exact matched cell value with entire match cases.

* Using `find()` method to perform find operation.

## Replace

Replace feature is used to change the find contents of a cell within sheet or workbook. Replace All is used to change all the matched contents of a cell within sheet or workbook.

**User Interface**:

Replace can be done by any of the following ways:

* Use `Ctrl + H` key to open the Find and Replace dialog.
* Use Replace button to change the found value in sheet or workbook.
* Using Replace All button, all the matched criteria can be replaced with find value based on sheet or workbook.
* Using `replace()` method to perform replace operation by passing the argument `args.replaceby` as `replace`.
* Using `replace()` method to perform replace all operation by passing the argument `args.replaceby` as `replaceall`.

## Go to

Go to feature is used to navigate to a specific cell address in the sheet or workbook.

**User Interface**:

* Use `Ctrl + G` key to open the Go To dialog.
* Use `goTo()` method to perform Go To operation.

In the following sample, searching can be done by following ways:

* Select the Home tab in the Ribbon toolbar, and then select the Search icon.
* Enter any value in the search textbox.
* Select the next (or) previous button to find the entered value in the spreadsheet.
* You can have more options to find values by selecting the more options in the search toolbar.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" allowFindAndReplace="true">
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
            <e-spreadsheet-sheet name="Company Details">
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
{% endhighlight %}
{% highlight c# tabtitle="SearchController.cs" %}
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



## Limitations

* Undo/redo for Replace All is not supported in this feature.