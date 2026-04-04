# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/freeze-pane.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/freeze-pane.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/freeze-pane.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/freeze-pane.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/freeze-pane.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/freeze-pane.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/freeze-pane.md

# FreezePanes in ASP.NET Core Spreadsheet control

Freeze Panes helps you to keep particular rows or columns visible when scrolling the sheet content in the spreadsheet. You can specify the number of frozen rows and columns using the `frozenRows` and `frozenColumns` properties inside the [`Sheet`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_Sheets) property.

## Apply freeze panes on UI

**User Interface**:

In the active spreadsheet, click the cell where you want to create freeze panes. Freeze panes can be done in any of the following ways:

* Select the View tab in the Ribbon toolbar and choose the `Freeze Panes` item.
* Use the `freezePanes` method programmatically.

## FrozenRows

It allows you to keep a certain number of rows visible while scrolling vertically through the rest of the worksheet.

**User Interface**:

In the active spreadsheet, select the cell where you want to create frozen rows. Frozen rows can be done in any one of the following ways:

* Select the View tab in the Ribbon toolbar and choose the `Freeze Rows` item.
* You can specify the number of frozen rows using the `frozenRows` property inside the `Sheet` property.

## FrozenColumns

It allows you to keep a certain number of columns visible while scrolling horizontally through the rest of the worksheet.

**User Interface**:

In the active spreadsheet, select the cell where you want to create frozen columns. Frozen columns can be done in any one of the following ways:

* Select the View tab in the Ribbon toolbar and choose the `Freeze Columns` item.
* You can specify the number of frozen columns using the `frozenColumns` property inside the `Sheet` property.

In this demo, the frozenColumns is set as â2â, and the frozenRows is set as â2â. Hence, the two columns on the left and the top two rows are frozen.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" created="createdHandler">
            <e-spreadsheet-sheets>
                <e-spreadsheet-sheet name="Gross Salary" frozenRows="2" frozenColumns="2" selectedRange="C1">
                    <e-spreadsheet-ranges>
                        <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A2"></e-spreadsheet-range>
                    </e-spreadsheet-ranges>
                    <e-spreadsheet-rows>
                        <e-spreadsheet-row>
                            <e-spreadsheet-cells>
                                <e-spreadsheet-cell index=1 value="Period">
                                    <e-spreadsheet-cellstyle fontSize="12pt" fontWeight="Bold" textAlign="Center" verticalAlign="Middle"></e-spreadsheet-cellstyle>
                                </e-spreadsheet-cell>
                                <e-spreadsheet-cell index=3 value="Total Gross Salary">
                                    <e-spreadsheet-cellstyle fontSize="12pt" fontWeight="Bold" textAlign="Center" verticalAlign="Middle"></e-spreadsheet-cellstyle>
                                </e-spreadsheet-cell>
                            </e-spreadsheet-cells>
                        </e-spreadsheet-row>
                        <e-spreadsheet-row>
                            <e-spreadsheet-cells>
                                <e-spreadsheet-cell index=2 value="Basic Salary"></e-spreadsheet-cell>
                                <e-spreadsheet-cell value="Revised Basic Salary"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="DA"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Revised DA"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="HRA"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Revised HRA"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Conveyance Allowance"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Revised Conveyance Allowance"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Medical Expenses"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Revised Medical Expenses"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Special Allowance"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Revised Spcial Allowance"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Total Gross Salary"></e-spreadsheet-cell>;
                                <e-spreadsheet-cell value="Revised Total Gross Salary"></e-spreadsheet-cell>;
                            </e-spreadsheet-cells>
                        </e-spreadsheet-row>
                        <e-spreadsheet-row index=26>
                            <e-spreadsheet-cells>
                                <e-spreadsheet-cell index=13 value="Total Amount">
                                    <e-spreadsheet-cellstyle fontSize="12pt" fontWeight="Bold" textAlign="Center" verticalAlign="Middle"></e-spreadsheet-cellstyle>
                                </e-spreadsheet-cell>
                                <e-spreadsheet-cell formula="=SUM(O4:O26)">
                                    <e-spreadsheet-cellstyle fontSize="12pt" fontWeight="Bold" textAlign="Center" verticalAlign="Middle"></e-spreadsheet-cellstyle>
                                </e-spreadsheet-cell>
                                <e-spreadsheet-cell formula="=SUM(P4:P26)">
                                    <e-spreadsheet-cellstyle fontSize="12pt" fontWeight="Bold" textAlign="Center" verticalAlign="Middle"></e-spreadsheet-cellstyle>
                                </e-spreadsheet-cell>
                            </e-spreadsheet-cells>
                        </e-spreadsheet-row>
                    </e-spreadsheet-rows>
                    <e-spreadsheet-columns>
                        <e-spreadsheet-column width="80"></e-spreadsheet-column>
                        <e-spreadsheet-column width="80"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="80"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                        <e-spreadsheet-column width="100"></e-spreadsheet-column>
                    </e-spreadsheet-columns>
                </e-spreadsheet-sheet>
            </e-spreadsheet-sheets>
        </ejs-spreadsheet>

<script>
    function createdHandler() {
        this.wrap("C2:P2");
        this.merge('A1:B1');
        this.merge('C1:P1');
        this.cellFormat({ backgroundColor: '#4e4ee6', color: '#FFFFF4', fontSize: '12pt', fontWeight: 'bold', textAlign: 'center', verticalAlign: 'middle' }, 'A1:P2');
        this.cellFormat({ backgroundColor: '#4e4ee6', color: '#FFFFF4' }, 'A3:B26');
        this.numberFormat('$#,##0.00', 'C2:P26');
        this.numberFormat('$#,##0.00', 'O27:P27');
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="FreezePane.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { Month= "January",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C3,E3,G3,I3,K3,M3)", RevisedTotalGrossSalary= "=SUM(D3,F3,H3,J3,L3,N3)", },
        new { Month= "February",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C4,E4,G4,I4,K4,M4)", RevisedTotalGrossSalary= "=SUM(D4,F4,H4,J4,L4,N4)", },
        new { Month= "March",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C5,E5,G5,I5,K5,M5)", RevisedTotalGrossSalary= "=SUM(D5,F5,H5,J5,L5,N5)", },
        new { Month= "April",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C6,E6,G6,I6,K6,M6)", RevisedTotalGrossSalary= "=SUM(D6,F6,H6,J6,L6,N6)", },
        new { Month= "May",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C7,E7,G7,I7,K7,M7)", RevisedTotalGrossSalary= "=SUM(D7,F7,H7,J7,L7,N7)", },
        new { Month= "June",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C8,E8,G8,I8,K8,M8)", RevisedTotalGrossSalary= "=SUM(D8,F8,H8,J8,L8,N8)", },
        new { Month= "July",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C9,E9,G9,I9,K9,M9)", RevisedTotalGrossSalary= "=SUM(D9,F9,H9,J9,L9,N9)", },
        new { Month= "August",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C10,E10,G10,I10,K10,M10)", RevisedTotalGrossSalary= "=SUM(D10,F10,H10,J10,L10,N10)", },
        new { Month= "September",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C11,E11,G11,I11,K11,M11)", RevisedTotalGrossSalary= "=SUM(D11,F11,H11,J11,L11,N11)", },
        new { Month= "October",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C12,E12,G12,I12,K12,M12)", RevisedTotalGrossSalary= "=SUM(D12,F12,H12,J12,L12,N12)", },
        new { Month= "November",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C13,E13,G13,I13,K13,M13)", RevisedTotalGrossSalary= "=SUM(D13,F13,H13,J13,L13,N13)", },
        new { Month= "December",  Year= "2019",  BasicSalary= 15100,  RevisedBasicSalary= 15800,  DA= 2000,  RevisedDA= 2200, HRA= 5000,  RevisedHRA= 6500,  ConveyanceAllowance= 1500,  RevisedConveyanceAllowance= 1700, MedicalExpenses= 1250, RevisedMedicalExpenses= 1500, SpecialAllowance= 1000, RevisedSpecialAllowance= 1200, TotalGrossSalary= "=SUM(C14,E14,G14,I14,K14,M14)", RevisedTotalGrossSalary= "=SUM(D14,F14,H14,J14,L14,N14)", },
        new { Month= "January",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C15,E15,G15,I15,K15,M15)", RevisedTotalGrossSalary= "=SUM(D15,F15,H15,J15,L15,N15)", },
        new { Month= "February",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C16,E16,G16,I16,K16,M16)", RevisedTotalGrossSalary= "=SUM(D16,F16,H16,J16,L16,N16)", },
        new { Month= "March",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C17,E17,G17,I17,K17,M17)", RevisedTotalGrossSalary= "=SUM(D17,F17,H17,J17,L17,N17)", },
        new { Month= "April",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C18,E18,G18,I18,K18,M18)", RevisedTotalGrossSalary= "=SUM(D18,F18,H18,J18,L18,N18)", },
        new { Month= "May",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C19,E19,G19,I19,K19,M19)", RevisedTotalGrossSalary= "=SUM(D19,F19,H19,J19,L19,N19)", },
        new { Month= "June",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C20,E20,G20,I20,K20,M20)", RevisedTotalGrossSalary= "=SUM(D20,F20,H20,J20,L20,N20)", },
        new { Month= "July",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C21,E21,G21,I21,K21,M21)", RevisedTotalGrossSalary= "=SUM(D21,F21,H21,J21,L21,N21)", },
        new { Month= "August",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C22,E22,G22,I22,K22,M22)", RevisedTotalGrossSalary= "=SUM(D22,F22,H22,J22,L22,N22)", },
        new { Month= "September",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C23,E23,G23,I23,K23,M23)", RevisedTotalGrossSalary= "=SUM(D23,F23,H23,J23,L23,N23)", },
        new { Month= "October",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C24,E24,G24,I24,K24,M24)", RevisedTotalGrossSalary= "=SUM(D24,F24,H24,J24,L24,N24)", },
        new { Month= "November",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C25,E25,G25,I25,K25,M25)", RevisedTotalGrossSalary= "=SUM(D25,F25,H25,J25,L25,N25)", },
        new { Month= "December",  Year= "2020",  BasicSalary= 16610,  RevisedBasicSalary= 17380,  DA= 2200,  RevisedDA= 2420, HRA= 5500,  RevisedHRA= 7150,  ConveyanceAllowance= 1650,  RevisedConveyanceAllowance= 1870, MedicalExpenses= 1375, RevisedMedicalExpenses= 1650, SpecialAllowance= 1100, RevisedSpecialAllowance= 1320, TotalGrossSalary= "=SUM(C26,E26,G26,I26,K26,M26)", RevisedTotalGrossSalary= "=SUM(D26,F26,H26,J26,L26,N26)", }
    };
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



## Limitations

Freeze Panes feature is not compatible with all the features which are available in the spreadsheet. Below features are not compatible with Freeze Panes feature.

* Merging the cells between freeze and unfreeze area.
* If images and charts are added inside the freeze area cells, their portion in the unfreeze area will not move when scrolling.

## See Also

* [Sorting](./sort)
* [Filtering](./filter)
* [Undo Redo](./undo-redo)
