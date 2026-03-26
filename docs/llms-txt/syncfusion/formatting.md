# Source: https://docs.syncfusion.com/uwp/timepicker/formatting.md

# Source: https://docs.syncfusion.com/uwp/datetimepicker/formatting.md

# Source: https://docs.syncfusion.com/uwp/datepicker/formatting.md

# Source: https://docs.syncfusion.com/winui/numberbox/formatting.md

# Source: https://docs.syncfusion.com/windowsforms/numeric-textbox/formatting.md

# Source: https://docs.syncfusion.com/wpf/classic/spreadsheet/formatting.md

# Source: https://docs.syncfusion.com/wpf/numericupdown/formatting.md

# Source: https://docs.syncfusion.com/wpf/timepicker/formatting.md

# Source: https://docs.syncfusion.com/wpf/datepicker/formatting.md

# Source: https://docs.syncfusion.com/maui/timepicker/formatting.md

# Source: https://docs.syncfusion.com/maui/numericentry/formatting.md

# Source: https://docs.syncfusion.com/maui/datetimepicker/formatting.md

# Source: https://docs.syncfusion.com/maui/datepicker/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/wpf/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/winforms/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/uwp/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/blazor/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/formatting.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/formatting.md

# Formatting in ASP.NET Core Spreadsheet Control

Formatting options make your data easier to view and understand. The different types of formatting options in the Spreadsheet are,
* Number Formatting
* Text Formatting
* Cell Formatting

## Number Formatting

Number formatting provides a type for your data in the Spreadsheet. Use the [`allowNumberFormatting`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowNumberFormatting) property to enable or disable the number formatting option in the Spreadsheet. The different types of number formatting supported in Spreadsheet are,

| Types | Format Code | Format ID |
|---------|---------|---------|
| General(default) | NA | 0 |
| Number | `0.00` | 2 |
| Currency | `$#,##0.00` | NA |
| Accounting | `_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)` | 44 |
| ShortDate | `m/d/yyyy` | 14 |
| LongDate | `dddd, mmmm dd, yyyy` | NA |
| Time | `h:mm:ss AM/PM` | NA |
| Percentage | `0.00%` | 10 |
| Fraction | `# ?/?` | 12 |
| Scientific |`0.00E+00`  | 11 |
| Text | `@` | 49 |

Number formatting can be applied in following ways,
* Using the `format` property in `cell`, you can set the desired format to each cell at initial load.
* Using the `numberFormat` method, you can set the number format to a cell or range of cells.
* Selecting the number format option from ribbon toolbar.

### Custom Number Formatting

Spreadsheet supports custom number formats to display your data as numbers, dates, times, percentages, and currency values. If the pre-defined number formats do not meet your needs, you can set your own custom formats using custom number formats dialog or `numberFormat` method.

The different types of custom number format populated in the custom number format dialog are,

| Type | Format Code | Format ID |
|-------|---------|---------|
| General(default) | NA | 0 |
| Number | `0` | 1 |
| Number | `0.00` | 2 |
| Number | `#,##0` | 3 |
| Number | `#,##0.00` | 4 |
| Number | `#,##0_);(#,##0)` | 37 |
| Number | `#,##0_);[Red](#,##0)` | 38 |
| Number | `#,##0.00_);(#,##0.00)` | 39 |
| Number | `#,##0.00_);[Red](#,##0.00)` | 40 |
| Currency | `$#,##0_);($#,##0)` | 5 |
| Currency | `$#,##0_);[Red]($#,##0)` | 6 |
| Currency | `$#,##0.00_);($#,##0.00)` | 7 |
| Currency | `$#,##0.00_);[Red]($#,##0.00)` | 8 |
| Percentage | `0%` | 9 |
| Percentage | `0.00%` | 10 |
| Scientific |`0.00E+00`  | 11 |
| Scientific |`##0.0E+0`  | 48 |
| Fraction | `# ?/?` | 12 |
| Fraction | `# ??/??` | 13 |
| ShortDate | `m/d/yyyy` | 14 |
| Custom | `d-mmm-yy` | 15 |
| Custom | `d-mmm` | 16 |
| Custom | `mmm-yy` | 17 |
| Custom | `h:mm AM/PM` | 18 |
| Custom | `h:mm:ss AM/PM` | 19 |
| Custom | `h:mm` | 20 |
| Custom | `h:mm:ss` | 21 |
| Custom | `m/d/yyyy h:mm` | 22 |
| Custom | `mm:ss` | 45 |
| Custom | `mm:ss.0` | 47 |
| Text | `@` | 49 |
| Custom | `[h]:mm:ss` | 46 |
| Accounting | `_($* #,##0_);_($* (#,##0);_($* "-"_);_(@_)` | 42 |
| Accounting | `_(* #,##0_);_(* (#,##0);_(* "-"_);_(@_)` | 41 |
| Accounting | `_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)` | 44 |
| Accounting | `_(* #,##0.00_);_(* (#,##0.00);_(* "-"??_);_(@_)` | 43 |

Custom Number formatting can be applied in following ways,
* Using the `numberFormat` method, you can set your own custom number format to a cell or range of cells.
* Selecting the custom number format option from custom number formats dialog or type your own format in dialog input and then click apply button. It will apply the custom format for selected cells.

The following code example shows the number formatting in cell data.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
    <ejs-spreadsheet id="spreadsheet" created="created" showRibbon="false" showSheetTabs="false" showFormulaBar="false" allowDelete="false" allowInsert="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet selectedRange="U15">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A2"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row height="35" customHeight="true">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Sales Team Summary" colSpan="6">
                                <e-spreadsheet-cellstyle textAlign="Center" fontWeight="Bold" verticalAlign="Middle" fontStyle="Italic" fontSize="16pt" border="1px solid #e0e0e0" backgroundColor="#EEEEEE" color="#279377"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row index="10">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Total:" index="1">
                                <e-spreadsheet-cellstyle fontWeight="Bold" verticalAlign="Middle" fontStyle="Italic"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(C3:C10)" format="$#,##0.00"></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(D3:D10)" format='_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@@_)'></e-spreadsheet-cell>
                            <e-spreadsheet-cell formula="=SUM(E3:E10)" format='_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@@_)'></e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="160"></e-spreadsheet-column>
                    <e-spreadsheet-column width="160"></e-spreadsheet-column>
                    <e-spreadsheet-column width="160"></e-spreadsheet-column>
                    <e-spreadsheet-column width="120"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

       function created() {
        this.cellFormat({ fontWeight: 'bold', fontSize: '12pt', backgroundColor: '#279377', textAlign: 'center', color: '#ffffff', borderBottom: '1px solid #e0e0e0' }, 'A2:F2');
        this.cellFormat({ borderTop: '1px solid #e0e0e0', backgroundColor: '#EEEEEE' }, 'A11:F11');
        this.setBorder({ border: '1px solid #e0e0e0' }, 'A2:F11', 'Outer');
        // Applied Accounting format to the cells from C3 to E10 range.
        this.numberFormat('_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@@_)', 'C3:E10');
        // Applied Percentage format to the cells from C3 to E11 range.
        this.numberFormat('0%', 'F3:F10');
        // applied the custom number format for cell form D3 to D10 range
        this.numberFormat('[Red][<=2000]$#,##0.00;[Blue][>2000]$#,##0.00', 'D3:D10');
        // applied the custom number format for cell from F3 to F10 range
        this.numberFormat('#,##0.00_);[Red](#,##0.00)', 'F3:F10');
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="NumberFormatController.cs" %}
public IActionResult Index()
{
      List<object> data = new List<object>()
   {
      new { Salesperson= "Jeffrey Burke",  RegionCovered= "Oklahoma",  February2019Sales= "28000",  CostofSales= "2460",  January2019Sales= "21238", PercentChange = ".32"},
      new { Salesperson= "Amy Fernandez",  RegionCovered= "North Carolina",  February2019Sales= "23138",  CostofSales= "1521",  January2019Sales= "23212", PercentChange = "0"},
      new { Salesperson= "Mark Hayes",  RegionCovered= "Massachusetts",  February2019Sales= "25092",  CostofSales= "1521",  January2019Sales= "20454", PercentChange = ".23"},
      new { Salesperson= "Judith Ray",  RegionCovered= "California",  February2019Sales= "21839",  CostofSales= "1923",  January2019Sales= "24619", PercentChange = "-.11"},
      new { Salesperson= "Rany Graham",  RegionCovered= "South Carolina",  February2019Sales= "23342",  CostofSales= "2397",  January2019Sales= "20045", PercentChange = ".16"},
      new { Salesperson= "Christina Foster",  RegionCovered= "Delaware",  February2019Sales= "23368",  CostofSales= "1500",  January2019Sales= "17537", PercentChange = ".33"},
      new { Salesperson= "Judy Green",  RegionCovered= "Texas",  February2019Sales= "21510",  CostofSales= "1657",  January2019Sales= "17537", PercentChange = "-.14"},
      new { Salesperson= "Paula Hall",  RegionCovered= "Virginia",  February2019Sales= "21314",  CostofSales= "2418",  January2019Sales= "18082", PercentChange = ".18"},
   };
   ViewBag.DefaultData = data;
   return View();
}
{% endhighlight %}
{% endtabs %}

## Configure culture-based custom format

Previously, the custom format dialog always displayed formats using the English settings (group separator, decimal separator, and currency symbol were not updated based on the applied culture). Starting from version `27.1.*`, the custom format dialog will now display formats according to the applied culture. You can select a culture-based number format from the dialog or enter your own format using the culture-specific decimal separator, group separator, and currency symbol. Then, click "Apply" to apply the culture-specific custom format to the selected cells.

The spreadsheet allows customization of formats in the custom format dialog using the `configureLocalizedFormat` method. In this method, you need to pass a collection containing the default number format IDs and their corresponding format codes as arguments. Based on this collection, the custom format dialog will display the customized formats. You can refer to the [default number format IDs](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.spreadsheet.numberingformat?view=openxml-2.8.1) from the Excel built-in number format reference.

Compared to Excel, the date, time, currency, and accounting formats vary across different cultures. For example, when an Excel file with the date format `'m/d/yyyy'` is imported in the `en-US` culture, the spreadsheet displays the date in that format. However, when the same file is imported in the German culture, the date format changes to `'dd.MM.yyyy'`, which is the default for that region. The default number format ID for the date is 14. To customize the date format based on the culture, you should map the default number format ID to the appropriate culture-specific format code, like this: `{ id: 14, code: 'dd.MM.yyyy' }` in the `configureLocalizedFormat` method.

> The format code should use the default decimal separator (.) and group separator (,).

The code below illustrates how culture-based format codes are mapped to their corresponding number format ID for the `German` culture.

```csharp
List<object> deLocaleFormats = new List<object>()
{
    new { id = 37, code = @"#,##0;-#,##0" },
    new { id = 38, code = @"#,##0;[Red]-#,##0" },
    new { id = 39, code = @"#,##0.00;-#,##0.00" },
    new { id = 40, code = @"#,##0.00;[Red]-#,##0.00" },
    new { id = 5, code = @"#,##0 ""â¬"";-#,##0 ""â¬""" },
    new { id = 6, code = @"#,##0 ""â¬"";[Red]-#,##0 ""â¬""" },
    new { id = 7, code = @"#,##0.00 ""â¬"";-#,##0.00 ""â¬""" },
    new { id = 8, code = @"#,##0.00 ""â¬"";[Red]-#,##0.00 ""â¬""" },
    new { id = 41, code = @"_-* #,##0_-;-* #,##0_-;_-* ""-""_-;_-@_-" },
    new { id = 42, code = @"_-* #,##0 ""â¬""_-;-* #,##0 ""â¬""_-;_-* ""-"" ""â¬""_-;_-@_-" },
    new { id = 43, code = @"_-* #,##0.00_-;-* #,##0.00_-;_-* ""-""??_-;_-@_-" },
    new { id = 44, code = @"_-* #,##0.00 ""â¬""_-;-* #,##0.00 ""â¬""_-;_-* ""-""?? ""â¬""_-;_-@_-" },
    new { id = 14, code = @"dd.MM.yyyy" },
    new { id = 15, code = @"dd. MMM yy" },
    new { id = 16, code = @"dd. MMM" },
    new { id = 17, code = @"MMM yy" },
    new { id = 20, code = @"hh:mm" },
    new { id = 21, code = @"hh:mm:ss" },
    new { id = 22, code = @"dd.MM.yyyy hh:mm" }
};
ViewBag.deLocaleFormats = deLocaleFormats;

<script>
    var deLocaleFormats = @Html.Raw(Json.Serialize(deLocaleFormats));
    // Mapping culture-based number formats for the "de" culture: The "spreadsheet" parameter is an instance of the spreadsheet component, and the "deLocaleFormats" parameter is an array containing format codes and their corresponding format IDs for the "de" culture.
    ej.spreadsheet.configureLocalizedFormat(spreadsheet, deLocaleFormats);
</script>
```

The following code example demonstrates how to configure culture-based formats for different cultures in the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
@{
    var localeFormats = ViewBag.LocaleFormats as Dictionary<string, List<object>>;
}

<div id="wrapper">
    <ejs-dropdownlist id="ddlelement" index="0" dataSource="ViewBag.CultureList" placeholder="Select a locale" change="change" width="150px" popupHeight="220px">
        <e-dropdownlist-fields text="Culture" value="Locale"></e-dropdownlist-fields>
    </ejs-dropdownlist>
    <ejs-spreadsheet id="spreadsheet" locale="de" listSeparator=";" created="created">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
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
    var localeFormats = @Html.Raw(Json.Serialize(localeFormats));

    function loadCultureFiles (localeOptions) {
        for (var locale = 0; locale < localeOptions.length; locale++) {
            var files = ['ca-gregorian', 'currencies', 'numbers', 'timeZoneNames', 'numberingSystems'];
            var loader = ej.base.loadCldr;
            var loadCulture = function (fileName) {
                var val;
                var url = location.origin + '/../cldr-data/' + (fileName === 'numberingSystems' ? 'supplemental/' : ('main/' + (localeOptions[locale] + '/'))) + fileName + '.json';
                var ajax = new ej.base.Ajax(url, 'GET', false);
                ajax.onSuccess = function (value) {
                    val = value;
                };
                ajax.send();
                loader(JSON.parse(val));
            };
            for (var prop = 0; prop < files.length; prop++) {
                loadCulture(files[prop]);
            }
        }
    }
    loadCultureFiles(['de', 'fr-CH', 'zh']);

    // Setting German culture.
    ej.base.setCulture('de');
    // Setting currency code for the German culture.
    ej.base.setCurrencyCode('EUR');

    // Mapping default number formats for the 'de' locale before the spreadsheet is created.
    ej.spreadsheet.configureLocalizedFormat(null, localeFormats['de']);

    function created() {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        spreadsheet.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:H1');
        applyFormats();
    }

    function change(args) {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        var localeOption = args.value.split(' ');
        // Setting the culture name like 'de', 'fr-CH', 'zh', and 'en-US'.
        var cultureName = localeOption[0];
        ej.base.setCulture(cultureName);
        // Setting the currency code for the selected locale like 'EUR', 'CNY', 'CHF', and 'USD'.
        ej.base.setCurrencyCode(localeOption[1]);
        // Mapping the default number format codes for the selected locale.
        ej.spreadsheet.configureLocalizedFormat(spreadsheet, localeFormats[cultureName]);
        // Setting the culture for the spreadsheet.
        spreadsheet.locale = cultureName;
        // Setting the list separator for the selected locale.
        spreadsheet.listSeparator = localeOption[2];
        // Refreshing the changes immediately in the spreadsheet.
        spreadsheet.dataBind();
        applyFormats();
    }

    function applyFormats() {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        // Apply format to the specified range in the active sheet.
        // The getFormatFromType method returns the culture-based format code based on the mapped formats.
        // If a format ID is not mapped or is not applicable, it will return the format code based on the loaded culture.
        // For 'en-US' (English) culture, the format code will be 'm/d/yyyy'.
        // For 'de' (German) culture, the format code will be 'dd.MM.yyyy'.
        // For 'fr-CH' (French-Switzerland) culture, the format code will be 'dd.MM.yyyy'.
        // For 'zh' (Chinese) culture, the format code will be 'yyyy/m/d'.
        spreadsheet.numberFormat(ej.spreadsheet.getFormatFromType('ShortDate'), 'B2:B11');
        // For 'en-US' (English) culture, the format code will be 'h:mm:ss AM/PM'.
        // For 'de' (German) culture, the format code will be 'HH:mm:ss'.
        // For 'fr-CH' (French-Switzerland) culture, the format code will be 'HH:mm:ss'.
        // For 'zh' (Chinese) culture, the format code will be 'h:mm:ss AM/PM'.
        spreadsheet.numberFormat(ej.spreadsheet.getFormatFromType('Time'), 'C2:C11');
        // For 'en-US' (English) culture, the format code will be '$#,##0.00'.
        // For 'de' (German) culture, the format code will be '#,##0.00 "â¬"'.
        // For 'fr-CH' (French-Switzerland) culture, the format code will be '#,##0.00 "CHF"'.
        // For 'zh' (Chinese) culture, the format code will be '"Â¥"#,##0.00'.
        spreadsheet.numberFormat(ej.spreadsheet.getFormatFromType('Currency'), 'E2:F11');
        // For 'en-US' (English) culture, the format code will be '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'.
        // For 'de' (German) culture, the format code will be '_-* #,##0.00 "â¬"_-;-* #,##0.00 "â¬"_-;_-* "-"?? "â¬"_-;_-@_-'.
        // For 'fr-CH' (French-Switzerland) culture, the format code will be '_-* #,##0.00 "CHF"_-;-* #,##0.00 "CHF"_-;_-* "-"?? "CHF"_-;_-@_-'
        // For 'zh' (Chinese) culture, the format code will be '_ "Â¥"* #,##0.00_ ;_ "Â¥"* -#,##0.00_ ;_ "Â¥"* "-"??_ ;_ @_'
        spreadsheet.numberFormat(ej.spreadsheet.getFormatFromType('Accounting'), 'H2:H11');
        // The percentage format code will be '0.00%' for all the cultures.
        spreadsheet.numberFormat('0.00%', 'G2:G11');
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="CultureController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { ItemName= "Casual Shoes", Date= "14.02.2014", Time= "11:34:32 AM", Quantity= 10, Price= 20, Amount= "=PRODUCT(D2;E2)", Discount= "2%", Profit= "=PRODUCT(G2;F2)" },
        new { ItemName= "Sports Shoes", Date= "11.06.2014", Time= "05:56:32 AM", Quantity= 20, Price= 30, Amount= "=PRODUCT(D3;E3)", Discount= "5%", Profit= "=PRODUCT(G3;F3)" },
        new { ItemName= "Formal Shoes", Date= "27.07.2014", Time= "03:32:44 AM", Quantity= 20, Price= 15, Amount= "=PRODUCT(D4;E4)", Discount= "7,5%", Profit= "=PRODUCT(G4;F4)" },
        new { ItemName= "Sandals & Floaters", Date= "21.11.2014", Time= "06:23:54 AM", Quantity= 15, Price= "20,45", Amount= "=PRODUCT(D5;E5)", Discount= "11%", Profit= "=PRODUCT(G5;F5)" },
        new { ItemName= "Flip- Flops & Slippers", Date= "23.06.2014", Time= "12:43:59 AM", Quantity= 30, Price= "10,67", Amount= "=PRODUCT(D6;E6)", Discount= "10%", Profit= "=PRODUCT(G6;F6)" },
        new { ItemName= "Sneakers", Date= "22.07.2014", Time= "10:55:53 AM", Quantity= 40, Price= 20, Amount= "=PRODUCT(D7;E7)", Discount= "13,2%", Profit= "=PRODUCT(G7;F7)" },
        new { ItemName= "Running Shoes", Date= "04.02.2014", Time= "03:44:34 AM", Quantity= 20, Price= "10,5", Amount= "=PRODUCT(D8;E8)", Discount= "3%", Profit= "=PRODUCT(G8;F8)" },
        new { ItemName= "Loafers", Date= "30.11.2014", Time= "03:12:52 AM", Quantity= 31, Price= 10, Amount= "=PRODUCT(D9;E9)", Discount= "6,67", Profit= "=PRODUCT(G9;F9)" },
        new { ItemName= "Cricket Shoes", Date= "09.07.2014", Time= "11:32:14 AM", Quantity= 41, Price= 30, Amount= "=PRODUCT(D10;E10)", Discount= "12,5%", Profit= "=PRODUCT(G10;F10)" },
        new { ItemName= "T-Shirts", Date= "31.10.2014", Time= "12:01:44 AM", Quantity= 50, Price= "10,75", Amount= "=PRODUCT(D11;E11)", Discount= "9%", Profit= "=PRODUCT(G11;F11)" }
    };
    List<object> cultureList = new List<object>()
    {
        new { Culture= "German - Germany", Locale= "de EUR ;" },
        new { Culture= "French - Switzerland", Locale = "fr-CH CHF ;" },
        new { Culture= "Chinese - China", Locale= "zh CNY ," },
        new { Culture= "English", Locale= "en-US USD ," }
    };
    
    Dictionary<string, List<object>> localeFormats = new Dictionary<string, List<object>> {
            { "de", new List<object> {
                new { id = 37, code = @"#,##0;-#,##0" },
                new { id = 38, code = @"#,##0;[Red]-#,##0" },
                new { id = 39, code = @"#,##0.00;-#,##0.00" },
                new { id = 40, code = @"#,##0.00;[Red]-#,##0.00" },
                new { id = 5, code = @"#,##0 ""â¬"";-#,##0 ""â¬""" },
                new { id = 6, code = @"#,##0 ""â¬"";[Red]-#,##0 ""â¬""" },
                new { id = 7, code = @"#,##0.00 ""â¬"";-#,##0.00 ""â¬""" },
                new { id = 8, code = @"#,##0.00 ""â¬"";[Red]-#,##0.00 ""â¬""" },
                new { id = 41, code = @"_-* #,##0_-;-* #,##0_-;_-* ""-""_-;_-@_-" },
                new { id = 42, code = @"_-* #,##0 ""â¬""_-;-* #,##0 ""â¬""_-;_-* ""-"" ""â¬""_-;_-@_-" },
                new { id = 43, code = @"_-* #,##0.00_-;-* #,##0.00_-;_-* ""-""??_-;_-@_-" },
                new { id = 44, code = @"_-* #,##0.00 ""â¬""_-;-* #,##0.00 ""â¬""_-;_-* ""-""?? ""â¬""_-;_-@_-" },
                new { id = 14, code = @"dd.MM.yyyy" },
                new { id = 15, code = @"dd. MMM yy" },
                new { id = 16, code = @"dd. MMM" },
                new { id = 17, code = @"MMM yy" },
                new { id = 20, code = @"hh:mm" },
                new { id = 21, code = @"hh:mm:ss" },
                new { id = 22, code = @"dd.MM.yyyy hh:mm" }
            }},
            { "zh", new List<object> {
                new  { id = 37, code = @"#,##0;-#,##0" },
                new  { id = 38, code = @"#,##0;[Red]-#,##0" },
                new  { id = 39, code = @"#,##0.00;-#,##0.00" },
                new  { id = 40, code = @"#,##0.00;[Red]-#,##0.00" },
                new  { id = 5, code = @"""Â¥""#,##0;""Â¥""-#,##0" },
                new  { id = 6, code = @"""Â¥""#,##0;[Red]""Â¥""-#,##0" },
                new  { id = 7, code = @"""Â¥""#,##0.00;""Â¥""-#,##0.00" },
                new  { id = 8, code = @"""Â¥""#,##0.00;[Red]""Â¥""-#,##0.00" },
                new  { id = 41, code = @"_ * #,##0_ ;_ * -#,##0_ ;_ * ""-""_ ;_ @_" },
                new  { id = 42, code = @"_ ""Â¥""* #,##0_ ;_ ""Â¥""* -#,##0_ ;_ ""Â¥""* ""-""_ ;_ @_" },
                new  { id = 43, code = @"_ * #,##0.00_ ;_ * -#,##0.00_ ;_ * ""-""??_ ;_ @_" },
                new  { id = 44, code = @"_ ""Â¥""* #,##0.00_ ;_ ""Â¥""* -#,##0.00_ ;_ ""Â¥""* ""-""??_ ;_ @_" },
                new  { id = 14, code = @"yyyy/m/d" },
                new  { id = 22, code = @"yyyy/m/d h:mm" }
            }},
            { "fr-CH", new List<object> {
                new { id = 37, code = @"#,##0;-#,##0" },
                new { id = 38, code = @"#,##0;[Red]-#,##0" },
                new { id = 39, code = @"#,##0.00;-#,##0.00" },
                new { id = 40, code = @"#,##0.00;[Red]-#,##0.00" },
                new { id = 5, code = @"#,##0 ""CHF"";-#,##0 ""CHF""" },
                new { id = 6, code = @"#,##0 ""CHF"";[Red]-#,##0 ""CHF""" },
                new { id = 7, code = @"#,##0.00 ""CHF"";-#,##0.00 ""CHF""" },
                new { id = 8, code = @"#,##0.00 ""CHF"";[Red]-#,##0.00 ""CHF""" },
                new { id = 14, code = @"dd.MM.yyyy" },
                new { id = 15, code = @"dd.MMM.yy" },
                new { id = 16, code = @"dd.MMM" },
                new { id = 17, code = @"MMM.yy" },
                new { id = 20, code = @"HH:mm" },
                new { id = 21, code = @"HH:mm:ss" },
                new { id = 22, code = @"dd.MM.yyyy HH:mm" },
                new { id = 42, code = @"_-* #,##0 ""CHF""_-;-* #,##0 ""CHF""_-;_-* ""-"" ""CHF""_-;_-@__-" },
                new { id = 44, code = @"_-* #,##0.00 ""CHF""_-;-* #,##0.00 ""CHF""_-;_-* ""-""?? ""CHF""_-;_-@__-" },
                new { id = 41, code = @"_-* #,##0_-;-* #,##0_-;_-* ""-""_-;_-@__-" },
                new { id = 43, code = @"_-* #,##0.00_-;-* #,##0.00_-;_-* ""-""??_-;_-@__-" }
            }},
            { "en-US", new List<object>() }
            };
    ViewBag.LocaleFormats = localeFormats;
    ViewBag.CultureList = cultureList;
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}

## Text and cell formatting

Text and cell formatting enhances the look and feel of your cell. It helps to highlight a particular cell or range of cells from a whole workbook. You can apply formats like font size, font family, font color, text alignment, border etc. to a cell or range of cells. Use the [`allowCellFormatting`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowCellFormatting) property to enable or disable the text and cell formatting option in Spreadsheet. You can set the formats in following ways,
* Using the `style` property, you can set formats to each cell at initial load.
* Using the `cellFormat` method, you can set formats to a cell or range of cells.
* You can also apply by clicking the desired format option from the ribbon toolbar.

### Fonts

Various font formats supported in the spreadsheet are font-family, font-size, bold, italic, strike-through, underline and font color.

### Text Alignment

You can align text in a cell either vertically or horizontally using the  `textAlign` and `verticalAlign` property.

### Indents

To enhance the appearance of text in a cell, you can change the indentation of a cell content using `textIndent` property.

### Fill color

To highlight cell or range of cells from whole workbook you can apply background color for a cell using `backgroundColor` property.

### Borders

You can add borders around a cell or range of cells to define a section of worksheet or a table. The different types of border options available in the spreadsheet are,

| Types | Actions |
|-------|---------|
| Top Border | Specifies the top border of a cell or range of cells.|
| Left Border | Specifies the left border of a cell or range of cells.|
| Right Border | Specifies the right border of a cell or range of cells.|
| Bottom Border | Specifies the bottom border of a cell or range of cells.|
| No Border | Used to clear the border from a cell or range of cells.|
| All Border | Specifies all border of a cell or range of cells.|
| Horizontal Border | Specifies the top and bottom border of a cell or range of cells.|
| Vertical Border | Specifies the left and right border of a cell or range of cells.|
| Outside Border | Specifies the outside border of a range of cells.|
| Inside Border | Specifies the inside border of a range of cells.|

You can also change the color, size, and style of the border. The size and style supported in the spreadsheet are,

| Types | Actions |
|-------|---------|
| Thin | Specifies the `1px` border size (default).|
| Medium | Specifies the `2px` border size.|
| Thick | Specifies the `3px` border size.|
| Solid | Used to create the `solid` border (default).|
| Dashed | Used to create the `dashed` border.|
| Dotted | Used to create the `dotted` border.|
| Double | Used to create the `double` border.|

Borders can be applied in the following ways,
* Using the  `border`, `borderLeft`, `borderRight`, `borderBottom` properties, you can set the desired border to each cell at initial load.
* Using the `setBorder` method, you can set various border options to a cell or range of cells.
* Selecting the border options from ribbon toolbar.

The following code example shows the style formatting in text and cells of the spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
 <ejs-spreadsheet id="spreadsheet" created="created" showRibbon="false" showSheetTabs="false" showFormulaBar="false" allowDelete="false" allowInsert="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet selectedRange="U15" showGridLines="false">
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A2"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-rows>
                    <e-spreadsheet-row height="40" customHeight="true">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell value="Order Summary" colSpan="5">
                                <e-spreadsheet-cellstyle textAlign="Center" fontWeight="Bold" verticalAlign="Middle" fontStyle="Italic" fontSize="16pt" border="1px solid #e0e0e0" backgroundColor="#EEEEEE" color="#279377"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="30">
                        <e-spreadsheet-cells>
                            <e-spreadsheet-cell index="2">
                                <e-spreadsheet-cellstyle textAlign="Right"></e-spreadsheet-cellstyle>
                            </e-spreadsheet-cell>
                        </e-spreadsheet-cells>
                    </e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                    <e-spreadsheet-row height="30"></e-spreadsheet-row>
                </e-spreadsheet-rows>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    <e-spreadsheet-column width="200"></e-spreadsheet-column>
                    <e-spreadsheet-column width="110"></e-spreadsheet-column>
                    <e-spreadsheet-column width="140"></e-spreadsheet-column>
                    <e-spreadsheet-column width="90"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>


    <script>

      
    function created() {
        // Setting common styles to table header cells
        this.cellFormat({ fontWeight: 'bold', fontSize: '12pt', backgroundColor: '#279377', color: '#ffffff' }, 'A2:E2');
        // Setting common styles to whole table cells
        this.cellFormat({ verticalAlign: 'middle', fontFamily: 'Axettac Demo' }, 'A2:E12');
        // Column wise styles setting
        this.cellFormat({ textAlign: 'center' }, 'A2:A12');
        // Setting text-indent to 2 and 4 column
        var style = { textAlign: 'left', textIndent: '8pt' };
        this.cellFormat(style, 'B2:B12');
        this.cellFormat(style, 'D2:D12');
        this.cellFormat({ fontStyle: 'italic', textAlign: 'right' }, 'C3:C12');
        this.cellFormat({ textAlign: 'center' }, 'E2:E12');
        // Applied border to range of cells using 'setBorder' method
        this.setBorder({ borderLeft: '1px solid #e0e0e0', borderRight: '1px solid #e0e0e0' }, 'A2:E2');
        this.setBorder({ border: '1px solid #e0e0e0' }, 'A4:E11', 'Horizontal');
        this.setBorder({ border: '1px solid #e0e0e0' }, 'A3:E12', 'Outer');
        this.cellFormat({ color: '#10c469', textDecoration: 'line-through' }, 'E3:E4');
        this.cellFormat({ color: '#10c469', textDecoration: 'line-through' }, 'E9');
        this.cellFormat({ color: '#10c469', textDecoration: 'line-through' }, 'E12');
        this.cellFormat({ color: '#FFC107', textDecoration: 'underline' }, 'E5');
        this.cellFormat({ color: '#FFC107', textDecoration: 'underline' }, 'E8');
        this.cellFormat({ color: '#FFC107', textDecoration: 'underline' }, 'E11');
        this.cellFormat({ color: '#62c9e8' }, 'E6');
        this.cellFormat({ color: '#62c9e8' }, 'E10');
        this.cellFormat({ color: '#ff5b5b' }, 'E7');
    }

    </script>
{% endhighlight %}
{% highlight c# tabtitle="CellFormatController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { OrderId= "SF1001",  Product= "Laptop Backpack (Blue)",  OrderedDate= "02/14/2014",  OrderedBy= "Rahul Sharma",  Shipment= "Delivered"},
        new { OrderId= "SF1002",  Product= "Oppo F1 S mobile back cover",  OrderedDate= "06/11/2014",  OrderedBy= "Adi Pathak",  Shipment= "Delivered"},
        new { OrderId= "SF1003",  Product= "Tupperware 4 bottle set",  OrderedDate= "07/27/2014",  OrderedBy= "Himani Arora",  Shipment= "Pending"},
        new { OrderId= "SF1004",  Product= "Tupperware Lunch box",  OrderedDate= "11/21/2014",  OrderedBy= "Samuel Samson",  Shipment= "Shipped"},
        new { OrderId= "SF1005",  Product= "Panosonic Hair Dryer",  OrderedDate= "06/23/2014",  OrderedBy= "Neha",  Shipment= "Cancelled"},
        new { OrderId= "SF1006",  Product= "Philips LED 2 bulb set",  OrderedDate= "07/22/2014",  OrderedBy= "Christine J",  Shipment= "Pending"},
        new { OrderId= "SF1007",  Product= "Moto G4 plus headphone",  OrderedDate= "02/04/2014",  OrderedBy= "Shiv Nagar",  Shipment= "Delivered"},
        new { OrderId= "SF1008",  Product= "Lakme Eyeliner Pencil",  OrderedDate= "11/30/2014",  OrderedBy= "Cherry",  Shipment= "Shipped"},
        new { OrderId= "SF1009",  Product= "Listerine mouthwash",  OrderedDate= "07/09/2014",  OrderedBy= "Siddartha Mishra",  Shipment= "Pending"},
        new { OrderId= "SF1010",  Product= "Protinex original",  OrderedDate= "10/31/2014",  OrderedBy= "Ravi Chugh",  Shipment= "Delivered"},
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



### Limitations of Formatting

The following features are not supported in Formatting:

* Insert row/column between the formatting applied cells.
* Formatting support for row/column.

## Conditional Formatting

Conditional formatting helps you to format a cell or range of cells based on the conditions applied. You can enable or disable conditional formats by using the `allowConditionalFormat` property.

N> * The default value for the `allowConditionalFormat` property is `true`.

### Apply Conditional Formatting

You can apply conditional formatting by using one of the following ways,

* Select the conditional formatting icon in the Ribbon toolbar under the Home Tab.
* Using the `conditionalFormat` method to define the condition.
* Using the `conditionalFormats` in sheets model.

Conditional formatting has the following types in the spreadsheet,

### Highlight cells rules

Highlight cells rules option in the conditional formatting enables you to highlight cells with a preset color depending on the cell's value.

The following options can be given for the highlight cells rules as type,

N>* 'GreaterThan', 'LessThan', 'Between', 'EqualTo', 'ContainsText', 'DateOccur', 'Duplicate', 'Unique'.

The following preset colors can be used for formatting styles,

N>* `"RedFT"` - Light Red Fill with Dark Red Text,
<br/>* `"YellowFT"` - Yellow Fill with Dark Yellow Text,
<br/>* `"GreenFT"` - Green Fill with Dark Green Tex/t,
<br/>* `"RedF"` - Red Fill,
<br/>* `"RedT"` - Red Text.

### Top bottom rules

Top bottom rules option in the conditional formatting allows you to apply formatting to the cells that satisfy a statistical condition with other cells in the range.

The following options can be given for the top bottom rules as type,

N>* 'Top10Items', 'Bottom10Items', 'Top10Percentage', 'Bottom10Percentage', 'BelowAverage', 'AboveAverage'.

### Data Bars

You can apply data bars to represent the data graphically inside a cell. The longest bar represents the highest value and the shorter bars represent the smaller values.

The following options can be given for the data bars as type,

N>* 'BlueDataBar', 'GreenDataBar', 'RedDataBar', 'OrangeDataBar', 'LightBlueDataBar', 'PurpleDataBar'.

### Color Scales

Using color scales, you can format your cells with two or three colors, where different color shades represent the different cell values. In the Green-Yellow-Red(GYR) Color Scale, the cell that holds the minimum value is colored as red. The cell that holds the median is colored as yellow, and the cell that holds the maximum value is colored as green. All other cells are colored proportionally.

The following options can be given for the color scales as type,

N>* 'GYRColorScale', 'RYGColorScale', 'GWRColorScale', 'RWGColorScale', 'BWRColorScale', 'RWBColorScale', 'WRColorScale', 'RWColorScale', 'GWColorScale', 'WGColorScale', 'GYColorScale', 'YGColorScale'.

### Icon Sets

Icon sets will help you to visually represent your data with icons. Every icon represents a range of values. In the Three Arrows(colored) icon, the green arrow icon represents the values greater than 67%, the yellow arrow icon represents the values between 33% to 67%, and the red arrow icon represents the values less than 33%.

The following options can be given for the icon sets as type,

N>* 'ThreeArrows', 'ThreeArrowsGray', 'FourArrowsGray', 'FourArrows', 'FiveArrowsGray', 'FiveArrows', 'ThreeTrafficLights1', 'ThreeTrafficLights2', 'ThreeSigns', 'FourTrafficLights', 'FourRedToBlack', 'ThreeSymbols', 'ThreeSymbols2', 'ThreeFlags', 'FourRating', 'FiveQuarters', 'FiveRating', 'ThreeTriangles', 'ThreeStars', 'FiveBoxes'.

### Custom Format

Using custom format for conditional formatting you can set cell styles like color, background color, font style, font weight and underline.

In the MAY and JUN columns, we have applied conditional formatting custom format.

N> * In the Conditional format, custom format supported for Highlight cells rules and Top bottom rules.

### Clear Rules

You can clear the defined rules by using one of the following ways,

* Using the âClear Rulesâ option in the Conditional Formatting button of HOME Tab in the ribbon to clear the rule from selected cells.
* Using the `clearConditionalFormat` method to clear the defined rules.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="created" showFormulaBar="false">
        <e-spreadsheet-sheets>
            <e-spreadsheet-sheet>
                <e-spreadsheet-ranges>
                    <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
                </e-spreadsheet-ranges>
                <e-spreadsheet-conditionalformats>
                        <e-spreadsheet-conditionalformat type= "GreaterThan", cFColor= "RedFT", value= "700", range= 'B2:B9'></e-spreadsheet-conditionalformat>
                        <e-spreadsheet-conditionalformat type= "Bottom10Items", cFColor= "YellowFT", value= '4', range= 'C2:C9'></e-spreadsheet-conditionalformat>
                        <e-spreadsheet-conditionalformat type= "BlueDataBar", range= 'D2:D9'></e-spreadsheet-conditionalformat>
                </e-spreadsheet-conditionalformats>
                <e-spreadsheet-columns>
                    <e-spreadsheet-column index="1" width="120"></e-spreadsheet-column>
                </e-spreadsheet-columns>
            </e-spreadsheet-sheet>
        </e-spreadsheet-sheets>
    </ejs-spreadsheet>

    <script>
    function created() {
        this.cellFormat({ fontWeight: 'bold', textAlign: 'center' }, 'A1:N1');
        this.conditionalFormat({ type: "RYGColorScale", range: 'E2:E9' });
        this.conditionalFormat({ type: "ThreeArrows", range: 'H2:H9' });
        //Custom format
        this.conditionalFormat({ type: 'Top10Items', value: '1',
            format: { style: { color: '#ffffff', backgroundColor: '#009999', fontWeight: 'bold'}}, range: 'F2:F9' });
        this.conditionalFormat({ type: 'Bottom10Items', value: '1',
            format: { style: { color: '#ffffff', backgroundColor: '#c68d53', fontWeight: 'bold'}}, range: 'G2:G9' });
    }
    </script>
{% endhighlight %}
{% highlight c# tabtitle="ConditionalFormattingController.cs" %}
public IActionResult Index()
{
    List<object> conditionalFormatData = new List<object>()
    {
        new { EVModel= "BMW I3", JAN= "1224", FEB= "423", MAR= "585", APR= "367", MAY= "729", JUN= "733", TOTAL= "=SUM(B2=G2)" },
        new { EVModel= "Tesla Model S", JAN= "975", FEB= "763", MAR= "723", APR= "483", MAY= "983", JUN= "589", TOTAL= "=SUM(B3=G3)" }, 
        new { EVModel= "Chevrolet Volt", JAN= "113", FEB= "289", MAR= "675", APR= "458", MAY= "391", JUN= "198", TOTAL= "=SUM(B4=G4)" },
        new { EVModel= "Jaguar I-PACE", JAN= "78", FEB= "177", MAR= "244", APR= "99", MAY= "312", JUN= "129", TOTAL= "=SUM(B5=G5)" },
        new { EVModel= "Tesla Model X", JAN= "978", FEB= "1108", MAR= "1604", APR= "879", MAY= "1070", JUN= "1001", TOTAL= "=SUM(B6=G6)" },
        new { EVModel= "Nissan LEAF", JAN= "229", FEB= "978", MAR= "1202", APR= "822", MAY= "135", JUN= "878", TOTAL= "=SUM(B7=G7)" },
        new { EVModel= "Honda Clarity EV", JAN= "671", FEB= "1302", MAR= "466", APR= "989", MAY= "679", JUN= "891", TOTAL= "=SUM(B8=G8)" },
        new { EVModel= "Toyota Prius Prime", JAN= "978", FEB= "1362", MAR= "1872", APR= "678", MAY= "900", JUN= "867", TOTAL= "=SUM(B9=G9)" }
    };
    ViewBag.DefaultData = conditionalFormatData;
    return View();
}
{% endhighlight %}
{% endtabs %}



### Limitations of Conditional formatting

The following features have some limitations in Conditional Formatting:

* Insert row/column between the conditional formatting.
* Conditional formatting with formula support.
* Copy and paste the conditional formatting applied cells.
* Custom rule support.

## See Also

* [Rows and columns](./rows-and-columns)
* [Hyperlink](./link)
* [Sorting](./sort)
* [Filtering](./filter)
* [`Ribbon customization`](./ribbon#ribbon-customization)
