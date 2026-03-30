# Source: https://docs.syncfusion.com/flutter/xlsio/working-with-image.md

# Working with Excel Images

## Adding Images to worksheet

Flutter XlsIO allows to insert images like JPEG and PNG formats into a worksheet. 

Refer to the following code snippet to add images to worksheet.

{% highlight dart %}

// CreateÂ aÂ newÂ ExcelÂ document.
final Workbook workbook = Workbook();

// AccessingÂ worksheetÂ viaÂ index.
final Worksheet sheet = workbook.worksheets[0];

// Adding an image.
final List<int> imageBytes = File('image.jpeg').readAsBytesSync();
sheet.pictures.addStream(1, 1, imageBytes);

// Save and dispose workbook.
final List<int> bytes = workbook.saveSync();
workbook.dispose();

File('AddImage.xlsx').writeAsBytes(bytes);

{% endhighlight %}


## Re-Sizing, Flip and Rotation Images

Pictures can be re-sized, flip and formatted using various properties of **Picture** class. Refer to the following code snippet.

{% highlight dart %}

// CreateÂ aÂ newÂ ExcelÂ document.
final Workbook workbook = Workbook();

// AccessingÂ worksheetÂ viaÂ index.
final Worksheet sheet = workbook.worksheets[0];

// AddÂ aÂ image.
final List<int> imageBytes = File('image.jpeg').readAsBytesSync();
sheet.pictures.addStream(1, 1, imageBytes);

final Picture picture = sheet.pictures[0];

// Re-sizeÂ anÂ image
picture.height = 200;
picture.width = 200;

// rotateÂ anÂ image.
picture.rotation = 100;

// FlipÂ anÂ image.
picture.horizontalFlip = true;

// saveÂ andÂ disposeÂ workbook
final List<int> bytes = workbook.saveSync();
workbook.dispose();

File('Image.xlsx').writeAsBytes(bytes);

{% endhighlight %}

