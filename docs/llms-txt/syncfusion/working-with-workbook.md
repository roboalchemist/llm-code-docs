# Source: https://docs.syncfusion.com/flutter/xlsio/working-with-workbook.md

# Working with Workbook

## Saving a Excel workbook to file system

You can save the created or manipulated workbook to file system using saveSync() method of Workbook. The workbook is saved in the XLSX format.

{% highlight dart %}

// Creates a new instance for workbook.
final Workbook workbook = Workbook();

// Save the workbook in file system as XLSX format.
final List<int> bytes = workbook.saveSync();
workbook.dispose();

File('Output.xlsx').writeAsBytes(bytes);

{% endhighlight %}

Flutter XlsIO now supports saving an Excel document asynchronously using save() method of Workbook.

{% highlight dart %}

// Creates a new instance for workbook.
final Workbook workbook = Workbook();

// Save the workbook in file system as XLSX format.
final List<int> bytes = await workbook.save();
workbook.dispose();

File('Output.xlsx').writeAsBytes(bytes);

{% endhighlight %}

## Closing a workbook

Once after the workbook manipulation and save operation are completed, you should dispose the instance of Workbook, in order to release all the memory consumed by XlsIOâs DOM. The following code snippet illustrates how dispose the instance of Workbook.

{% highlight dart %}

// Creates a new instance for workbook.
final WorkbookÂ workbookÂ =Â newÂ Workbook();

// Save the workbook in file system as XLSX format.
final List<int> bytes = workbook.saveSync();

// Dipose the workbook.
workbook.dispose();

File('Output.xlsx').writeAsBytes(bytes);

{% endhighlight %}

