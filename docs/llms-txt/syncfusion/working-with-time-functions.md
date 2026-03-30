# Source: https://docs.syncfusion.com/flutter/xlsio/working-with-time-functions.md

# Working with Time Function Formulas

Time Function Formulas includes the following functions:

* NOW
* TODAY

## NOW Function

NOW Function is used to returns the serial number of the current date and time.

The following code snippet illustrates on how to use NOW function formula.

{% highlight dart %}

// Create a new Excel Document.
final Workbook workbook = Workbook();

// Accessing sheet via index.
final Worksheet sheet = workbook.worksheets[0];

// FormulaÂ calculationÂ isÂ enabledÂ forÂ theÂ sheet.
sheet.enableSheetCalculations();

// SettingÂ formulaÂ inÂ theÂ cell.
final Range range = sheet.getRangeByName('A1');
range.setFormula('=NOW()');
double.parse(range.calculatedValue).toStringAsFixed(2);
range.numberFormat = 'm/d/yyyy h:mm';

// Save and dispose workbook.
final List<int> bytes = workbook.saveSync();
File('NOWFunction.xlsx').writeAsBytes(bytes);
workbook.dispose();

{% endhighlight %}

## TODAY Function

TODAY Function is used to returns the serial number of the current date.

The following code snippet illustrates on how to use TODAY function formula.

{% highlight dart %}

// Create a new Excel Document.
final Workbook workbook = Workbook();

// Accessing sheet via index.
final Worksheet sheet = workbook.worksheets[0];

// FormulaÂ calculationÂ isÂ enabledÂ forÂ theÂ sheet.
sheet.enableSheetCalculations();

// SettingÂ formulaÂ inÂ theÂ cell.
final Range range = sheet.getRangeByName('A1');
range.setFormula('=TODAY()');
range.numberFormat = 'mm/dd/yyyy';

// Save and dispose workbook.
final List<int> bytes = workbook.saveSync();
File('TODAYFunction.xlsx').writeAsBytes(bytes);
workbook.dispose();

{% endhighlight %}




