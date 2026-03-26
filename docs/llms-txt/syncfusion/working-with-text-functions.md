# Source: https://docs.syncfusion.com/flutter/xlsio/working-with-text-functions.md

# Working with Text Function Formulas

Text Function Formulas includes the following functions:

* CONCATENATE
* TRIM
* LOWER
* UPPER

## CONCATENATE Function

CONCATENATE Function is a Text Function used to join two or more text strings into one string.

The following code snippet illustrates on how to use CONCATENATE function formula.

{% highlight dart %}

// Create a new Excel Document.
final Workbook workbook = Workbook();

// Accessing sheet via index.
final Worksheet sheet = workbook.worksheets[0];

// setÂ theÂ valueÂ toÂ theÂ cell.
sheet.getRangeByName('A1').setText('Syncfusion ');
sheet.getRangeByName('A2').setText('Software');

sheet.getRangeByName('B1').setText('Hello');
sheet.getRangeByName('B2').setText('World');

// FormulaÂ calculationÂ isÂ enabledÂ forÂ theÂ sheet.
sheet.enableSheetCalculations();

// SettingÂ formulaÂ inÂ theÂ cell.
Range range = sheet.getRangeByName('A4');
range.setFormula('=CONCATENATE(A1,A2)');
range = sheet.getRangeByName('A6');
range.setFormula('=CONCATENATE(B1,B2)');

// Save and dispose workbook.
final List<int> bytes = workbook.saveSync();
File('CONCATENATEFunction.xlsx').writeAsBytes(bytes);
workbook.dispose();

{% endhighlight %}

## TRIM Function

TRIM Function is used to removes all spaces from text except for single spaces between words.

The following code snippet illustrates on how to use TRIM function formula.

{% highlight dart %}

// Create a new Excel Document.
final Workbook workbook = Workbook();

// Accessing sheet via index.
final Worksheet sheet = workbook.worksheets[0];

// setÂ theÂ valueÂ toÂ theÂ cell.
sheet.getRangeByName('A1').setText('   Hello  ');
sheet.getRangeByName('A2').setText('     World  Hi');

// FormulaÂ calculationÂ isÂ enabledÂ forÂ theÂ sheet.
sheet.enableSheetCalculations();

// SettingÂ formulaÂ inÂ theÂ cell.
Range range = sheet.getRangeByName('A4');
range.setFormula('=TRIM(A1)');
range = sheet.getRangeByName('A6');
range.setFormula('=TRIM(A2)');

// Save and dispose workbook.
final List<int> bytes = workbook.saveSync();
File('TRIMFunction.xlsx').writeAsBytes(bytes);
workbook.dispose();

{% endhighlight %}

## LOWER Function

LOWER Function used to converts all uppercase letters in a text string to lowercase.

The following code snippet illustrates on how to use LOWER function formula.

{% highlight dart %}

// Create a new Excel Document.
final Workbook workbook = Workbook();

// Accessing sheet via index.
final Worksheet sheet = workbook.worksheets[0];

// setÂ theÂ valueÂ toÂ theÂ cell.
sheet.getRangeByName('A1').setText('HELLO');
sheet.getRangeByName('A2').setText('World HI');

// FormulaÂ calculationÂ isÂ enabledÂ forÂ theÂ sheet.
sheet.enableSheetCalculations();

// SettingÂ formulaÂ inÂ theÂ cell.
Range range = sheet.getRangeByName('A4');
range.setFormula('=LOWER(A1)');
range = sheet.getRangeByName('A6');
range.setFormula('=LOWER(A2)');

// Save and dispose workbook.
final List<int> bytes = workbook.saveSync();
File('LOWERFunction.xlsx').writeAsBytes(bytes);
workbook.dispose();

{% endhighlight %}

## UPPER Function

LOWER Function used to converts all lowercase letters in a text string to uppercase.

The following code snippet illustrates on how to use UPPER function formula.

{% highlight dart %}

// Create a new Excel Document.
final Workbook workbook = Workbook();

// Accessing sheet via index.
final Worksheet sheet = workbook.worksheets[0];

// setÂ theÂ valueÂ toÂ theÂ cell.
sheet.getRangeByName('A1').setText('hello');
sheet.getRangeByName('A2').setText('World hi');

// FormulaÂ calculationÂ isÂ enabledÂ forÂ theÂ sheet.
sheet.enableSheetCalculations();

// SettingÂ formulaÂ inÂ theÂ cell.
Range range = sheet.getRangeByName('A4');
range.setFormula('=UPPER(A1)');
range = sheet.getRangeByName('A6');
range.setFormula('=UPPER(A2)');

// Save and dispose workbook.
final List<int> bytes = workbook.saveSync();
File('UPPERFunction.xlsx').writeAsBytes(bytes);
workbook.dispose();

{% endhighlight %}


