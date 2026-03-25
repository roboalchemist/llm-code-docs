# Source: https://docs.pentaho.com/analyzer-external-javascript-api/cv-apis-pentaho-analyzer-external-javascript-api-cp/report-apis-pentaho-analyzer-external-javascript-api/get-and-set-chart-options-apis-pentaho-analyzer-external-javascript-api.md

# Get and Set Chart Options APIs

This API allows for the manipulation of a wide range of chart options for Analyzer reports. Depending on the visualization type, different types of options are available. As these values are set, the result will be reflected in the report once a refresh is called. Methods and example calls for each option are provided below.

## How to Call These APIs

There are two functions for editing field options, `getChartOption` and `setChartOption`. The `getChartOption` returns the value of the option specified in the call. Method signatures are below:

```javascript
cv.api.report.setChartOption(name:string, value:string);
```

```javascript
cv.api.report.getChartOption(name:string)
```

To make sure changes are reflected in the report, the `refreshReport` method needs to be called.

```javascript
cv.api.operation.refreshReport();
```

Below is a listing of all of the available chart options along with how to set their values.

## legendPosition

This option allows the user to set the position of the legend on a report.

The following string values are allowed:

* TOP - positions the legend at the top of the report
* BOTTOM - positions the legend at the bottom of the report
* RIGHT - positions the legend to the right of the report
* LEFT - positions the legend to the left of the report
* **Example**

  ```javascript
  cv.api.report.setChartOption('legendPosition', 'LEFT');

  ```

The current value of legendPosition for a report can be retrieved using the getChartOption method. This function returns the legend position as a string.

* **Example**

  ```javascript
  cv.api.report.getChartOption('legendPosition');

  ```

## showLegend

This option allows the user to hide or show the legend on a report. There are the two acceptable strings for the value parameter 'true' and 'false'.

* **Example**

  ```javascript
  cv.api.report.setChartOption('showLegend', 'true');

  ```

The current value of `showLegend` for a report can be retrieved using the `getChartOption` method. This function returns either 'true' or 'false' as a string.

```javascript
cv.api.report.getChartOption('showLegend');

```

## autoRange

This option allows the user to turn `autoRange` on and off for the primary axis. When turned on, `autoRange` will calculate the lower and upper limits of the primary axis automatically. There are two acceptable strings for the value parameter, 'true' and 'false'.

* **Example**

  ```javascript
  cv.api.report.setChartOption('autoRange', 'true');

  ```

The current value of `autoRange` for a report can be retrieved using the `getChartOption` method. This function returns either 'true' or 'false' as a string.

```javascript
cv.api.report.getChartOption('autoRange');

```

## valueAxisLowerLimit

This option allows the user to set the lower limit for the primary axis. The value parameter accepts any double as a string.

* **Example**

  ```javascript
  cv.api.report.setChartOption('valueAxisLowerLimit', '10.55');

  ```

The current value of `valueAxisLowerLimit` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('valueAxisLowerLimit');

```

## valueAxisUpperLimit

This option allows the user to set the upper limit for the primary axis. The value parameter accepts any double as a string.

* **Example**

  ```javascript
  cv.api.report.setChartOption('valueAxisUpperLimit', '10.55');

  ```

The current value of `valueAxisUpperLimit` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('valueAxisUpperLimit');

```

## displayUnits

This option allows the user to set the scale of units for the for the primary axis. The value parameter accepts one of the following string parameters:

* UNITS\_0 - default value
* UNITS\_2 - increase the scale to the hundreds place
* UNITS\_3 - increase the scale to the thousands place
* UNITS\_4 - increase the scale to the ten thousands place
* UNITS\_5 - increase the scale to one hundred thousands place
* UNITS\_6 - increase the scale to the millions place
* **Example**

  ```javascript
  cv.api.report.setChartOption('displayUnits', 'UNITS_2');

  ```

The current value of `displayUnits` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('displayUnits');

```

## autoRangeSecondary

This option allows the user to turn `autoRangeSecondary` on and off for the secondary axis. When turned on, `autoRangeSecondary` will calculate the lower and upper limits the secondary axis automatically. There are two acceptable strings for the value parameter, 'true' and 'false'.

* **Example**

  ```javascript
  cv.api.report.setChartOption('autoRangeSecondary', 'true');

  ```

The current value of `autoRangeSecondary` for a report can be retrieved using the `getChartOption` method. This function returns either 'true' or 'false' as a string.

```javascript
cv.api.report.getChartOption('autoRangeSecondary');

```

## valueAxisLowerLimitSecondary

This option allows the user to set the lower limit for the secondary axis. The value parameter accepts any double as a string.

* **Example**

  ```javascript
  cv.api.report.setChartOption('valueAxisLowerLimitSecondary', '10.55');

  ```

The current value of `valueAxisLowerLimit` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('valueAxisLowerLimitSecondary');

```

## valueAxisUpperLimitSecondary

This option allows the user to set the upper limit for the secondary axis. The value parameter accepts any double as a string.

* **Example**

  ```javascript
  cv.api.report.setChartOption('valueAxisUpperLimitSecondary', '10.55');

  ```

The current value of `valueAxisUpperLimit` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('valueAxisUpperLimitSecondary');

```

## displayUnitsSecondary

This option allows the user to set the scale of units for the for the secondary axis. The value parameter accepts one of the following string parameters:

* UNITS\_0 - default value
* UNITS\_2 - increase the scale to the hundreds place
* UNITS\_3 - increase the scale to the thousands place
* UNITS\_4 - increase the scale to the ten thousands place
* UNITS\_5 - increase the scale to one hundred thousands place
* UNITS\_6 - increase the scale to the millions place
* **Example**

  ```javascript
  cv.api.report.setChartOption('displayUnitsSecondary', 'UNITS_2');

  ```

The current value of `displayUnitsSecondary` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('displayUnitsSecondary');

```

## maxValues

This option allows the user to set a maximum number of plot values in a report. The value parameter accepts any integer as a string. When setting this value, the user's value will be rounded to the closest predefined max value. Each visualization has its own list of maximum values.

* **Example**

  ```javascript
  cv.api.report.setChartOption('maxValues', '250');

  ```

For a scatter plot the predefined values are 1000, 2500, 5000, and 10000. So the above call of '250' would set the `maxValues` to 1000. Below are some more examples:

* '100' will set maxValues to 1000
* '2500' will set maxValues to 2500
* '50000' will set maxValues to 10000
* '1750' will set maxValues to 1000
* '1751' will set maxValues to 2500

The current value of `maxValues` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('maxValues');

```

## backgroundColor

This option allows the user to set the background color of the report. It will only work if the `backgroundFilll` option is not set to 'NONE'. The value parameter accepts hexidecimal color values.

* **Example**

  ```javascript
  cv.api.report.setChartOption('backgroundColor', '#aaaabb');

  ```

The current value of `backgroundColor` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('backgroundColor');

```

## labelColor

This option allows the user to set the label color of the report. The value parameter accepts hexidecimal color values.

* **Example**

  ```javascript
  cv.api.report.setChartOption('labelColor', '#aacc11');

  ```

The current value of `labelColor` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('labelColor');

```

## labelSize

This option allows the user to set the font size for axis labels on the report. The value parameter accepts integer values as a string.

* **Example**

  ```javascript
  cv.api.report.setChartOption('labelSize', '14');

  ```

The current value of `labelSize` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('labelSize');

```

Each visualization has a predefined list of font sizes. An example list could be 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40. When a user sets a `labelSize`, the algorithm searches to find the closest size available. Below are some examples:

* A value of '1' will set the labelSize to 7
* A value of '14' will set the labelSize to 14
* A value of '50' will set the labelSize to 40
* A value of '30' will set the labelSize to 28
* A value of '31' will set the labelSize to 32

## backgroundFill

This option allows users to set the type of background used on the report. The value parameter accepts the following strings:

* NONE - Default value. The background of the report has no color
* SOLID - The background of the report is set to the color chosen in the `backgroundColor` option.
* GRADIENT - The background of the report is a gradient with a starting value chosen by the `backgroundColor` option and the ending value set by the `backgroundColorEnd` option.
* **Example**

  ```javascript
  cv.api.report.setChartOption('backgroundFill', 'SOLID');

  ```

The current value of `backgroundFill` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('backgroundFill');
```

## maxChartsPerRow

This option allows the user to set the maximum number of multi-charts which appear on each row of a report. The value parameter accepts integer values as a string.

* **Example**

  ```javascript
  cv.api.report.setChartOption('maxChartsPerRow', '4');

  ```

The current value of `maxChartsPerRow` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('maxChartsPerRow');

```

Each visualization has a predefined list of acceptable values. An example list could be 1, 2, 3, 4, 5. When a user sets `maxChartsPerRow`, the algorithm searches to find the closest size available. Below are some examples:

* A value of '1' will set the maxChartsPerRow to 1
* A value of '3' will set the maxChartsPerRow to 3
* A value of '10' will set the maxChartsPerRow to 10
* A value of '50' will set the maxChartsPerRow to 50

## multiChartRangeScope

This option allows users to set set the axis range for multi-charts in a report. The value parameter accepts the following strings:

* GLOBAL - default value. Use the same value for all multi-charts.
* CELL - Each cell uses its own range values.
* **Example**

  ```javascript
  cv.api.report.setChartOption('multiChartRangeScope', 'GLOBAL');

  ```

The current value of `multiChartRangeScope` for a report can be retrieved using the `getChartOption` method. This function returns the current value of this option as a string.

```javascript
cv.api.report.getChartOption('multiChartRangeScope');

```

## emptyCellMode

This option allows you to set how empty cells appear in the Line and Area charts. The value parameter accepts the following strings:

* GAP - show gap
* ZERO - treat as zero
* LINEAR - connect with dotted line
* **Example**

  ```javascript
  cv.api.report.setChartOption('emptyCellMode', 'LINEAR');

  ```

The current value of `emptyCellMode` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('emptyCellMode');

```

## sizeByNegativesMode

This option allows you to control the domain of the size scale (treat negative values). The value parameter accepts the following strings:

* NEG\_LOWEST - Default smallest values. The values of the 'Size' gembar is taken directly such that the lowest value of the size scale can be negative.
* USE\_ABS - Absolute. The values of the 'Size' gembar are taken first, where the absolute value and the values are mapped to the size range in pixels.
* **Example**

  ```javascript
  cv.api.report.setChartOption('sizeByNegativeMode', 'USE_ABS');

  ```

The current value of `sizeByNegativesMode` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('sizeByNegativeMode');
```

## backgroundColorEnd

This option allows you to set the second background color of the chart for gradient. This property is only used if the `backgroundFill` option is set to ‘GRADIENT’. The value parameter accepts values of hex type.

* **Example**

  ```javascript
  cv.api.report.setChartOption('backgroundColorEnd', '#AA9922');

  ```

The current value of `backgroundColorEnd` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('backgroundColorEnd');

```

## labelStyle

This option allows you to set the style for axis labels of the chart. The value parameter accepts the following strings:

* PLAIN - default normal style.
* BOLD - bold style.
* ITALIC - italic style.
* **Example**

  ```javascript
  cv.api.report.setChartOption('labelStyle', 'BOLD');

  ```

The current value of `labelStyle` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('labelStyle');

```

## legendBackgroundColor

This option allows you to set the background color of the chart’s legend. The value parameter accepts values of hex type.

* **Example**

  ```javascript
  cv.api.report.setChartOption('legendBackgroundColor', '#aaaabb');

  ```

The current value of `legendBackgroundColor` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('legendBackgroundColor');

```

## legendSize

This option allows you to set the font size for legend of the chart. The value parameter accepts values of integer type. When the value is set, a special algorithm of searching for the closest value from predefined values is used.

* **Example**

  ```javascript
  cv.api.report.setChartOption('legendSize', '14');

  ```

The current value of `legendSize` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('legendSize');

```

Visualizations have a predefined list of font sizes. When you set the `labelSize` option, it searches for the closest size from the predefined list. The predefined size values are 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40. Below are some examples:

* A value of '1' will set the legendSize to 7
* A value of '14' will set he legendSize to 14
* A value of '50' will set the legendSize to 40
* A value of '30' will set the legendASize to 28
* A value of '31' will set the legendSize to 32

## legendColor

This option allows you to set the font color for legend of the chart. The value parameter accepts values of hex type.

* **Example**

  ```javascript
  cv.api.report.setChartOption('legendColor', '#aacc11');

  ```

The current value of `backgroundColorEnd` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('legendColor');

```

## legendStyle

This option allows you to set the font style for legend of the chart. The value parameter accepts the following strings:

* PLAIN - default normal style
* BOLD - bold style
* ITALIC - italic style
* **Example**

  ```javascript
  cv.api.report.setChartOption('legendStyle', 'BOLD');

  ```

The current value of `legendStyle` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('legendStyle');

```

## labelFontFamily

This option allows you to set the font family for axis labels of the chart. The value parameter accepts strings.

* **Example**

  ```javascript
  cv.api.report.setChartOption('labelFontFamily', 'Times New Roman');

  ```

The current value of `labelFontFamily` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('labelFontFamily');

```

## legendFontFamily

This option allows you to set the font family for legend of the chart. The value parameter accepts strings.

* **Example**

  ```javascript
  cv.api.report.setChartOption('legendFontFamily', 'Times New Roman');

  ```

The current value of `legendFontFamily` for a report can be retrieved as a string using the `getChartOption` method.

```javascript
cv.api.report.getChartOption('legendFontFamily');

```

## URL parameters

All of the above options are available through the URL via URL parameters. For a hex value you should escape the '#' character for URL. For example, instead of writing `'legendBackgroundColor=#EEAADD'` you can write `'legendBackgroundColor=%23EEAADD'`.

* **Example URL with all parameters**

  ```javascript
  http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3ALeading%20Product%20Lines%20%28pivot%20table%29.xanalyzer/editor?ts=1421660200377&showFieldList=true&showFieldLayout=true&vizId=ccc_scatter&showLegend=true&legendPosition=LEFT&legendBackgroundColor=%23EEAADD&legendSize=12&legendColor=%23AA11AA&legendStyle=BOLD&legendFontFamily=Times%20New%20Roman&backgroundFill=SOLID&backgroundColor=%23DDBBCC&labelColor=%23FF2322&labelSize=14&backgroundColorEnd=%23EEAADD&labelStyle=BOLD&labelFontFamily=Times%20New%20Roman&autoRange=false&autoRangeSecondary=false&displayUnits=UNITS_2&displayUnitsSecondary=UNITS_2&valueAxisLowerLimit=500&valueAxisUpperLimit=9000&valueAxisLowerLimitSecondary=4&valueAxisUpperLimitSecondary=55.5&maxValues=3&maxChartsPerRow=2&multiChartRangeScope=GLOBAL&emptyCellMode=GAP&sizeByNegativesMode=USE_ABS
  ```
