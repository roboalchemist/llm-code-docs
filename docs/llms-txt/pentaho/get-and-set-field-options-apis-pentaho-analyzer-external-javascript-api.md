# Source: https://docs.pentaho.com/analyzer-external-javascript-api/cv-apis-pentaho-analyzer-external-javascript-api-cp/report-apis-pentaho-analyzer-external-javascript-api/get-and-set-field-options-apis-pentaho-analyzer-external-javascript-api.md

# Get and Set Field Options APIs

This set of APIs allows for the manipulation of the user fields in Analyzer. Depending on the field type, different options are available. As these options are turned on and off, the values will be reflected in the in the right-click context menu for the appropriate field.

## How to Call these API's

There are two functions for editing field options, `getFieldOption` and `setFieldOption`. Get returns the value of the option specified in the call. Method signatures are below:

```javascript
cv.api.report.getFieldOption(formula:string, name:string);
```

To set an option on a field, the level or formula that contains the field is passed into the `setFieldOption` method along with the field name and the value to set as below:

```javascript
cv.api.report.setFieldOption(formula:string, name:string, value:string);
```

To make sure changes are reflected in the report, the `refreshReport` method needs to be called.

```javascript
cv.api.operation.refreshReport();
```

These are the field options that are available for Analyzer.

## label

This option allows the user to set the string label for a field. This option is available for measures and attributes.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Markets].[Territory]", "label", "SAMPLE_LABEL_TITLE");

  ```

The current value of label for a field can be retrieved using the `getFieldOption` method. If the label is not specified the function returns null.

* **Example**

  ```javascript
  var labelValue = cv.api.report.getFieldOption("[Markets].[Territory]", "label");

  ```

## sortOrderEnum

This option allows the user to set the sort order to ascending or descending as well as remove the sort order for a field. The following are acceptable string values values for the value parameter:

* NONE - remove sort order
* ASC - set ascending order
* DESC - set descending order

This option is available for measures and attributes.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Markets].[Territory]", "sortOrderEnum", "ASC");

  ```

The current value of `sortOrderEnum` for a field can be retrieved using the `getFieldOption` method. This function returns one of acceptable values: NONE, ASC, DESC.

* **Example**

  ```javascript
  var sortOrderValue = cv.api.report.getFieldOption("[Markets].[Territory]", "sortOrderEnum");

  ```

## showAggregate

This option allows the user to show or hide the aggregate value panel. There are two acceptable strings for the value parameter, true and false. This option is available only for measures.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "showAggregate", "true");

  ```

The current value of `showAggregate` for a field can be retrieved using the `getFieldOption` method. This function returns either true or false.

* **Example**

  ```javascript
  var showAggregate = cv.api.report.getFieldOption("[Measures].[Sales]", "showAggregate");

  ```

## showSum

This option allows the user to show or hide the sum value panel. There are two acceptable strings for the value parameter, true and false. This option is available only for measures.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "showSum", "true");

  ```

The current value of `showSum` for a field can be retrieved using the `getFieldOption` method. This function returns either true or false based on whether the panel is visible or not.

* **Example**

  ```javascript
  var showSum = cv.api.report.getFieldOption("[Measures].[Sales]", "showSum");

  ```

## showAverage

This option allows the user to show or hide the average value panel. There are two acceptable strings for the value parameter, true and false. This option is available only for measures.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "showAverage", "true");

  ```

The current value of `showAverage` for a field can be retrieved using the `getFieldOption` method. This function returns either true or false based on whether the panel is visible or not.

* **Example**

  ```javascript
  var showAverage = cv.api.report.getFieldOption("[Measures].[Sales]", "showAverage");

  ```

## showMin

This option allows the user to show or hide the minimum value panel. There are two acceptable strings for the value parameter, true and false. This option is available only for measures.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "showMin", "true");
  ```

The current value of `showMin` for a field can be retrieved using the `getFieldOption` method. This function returns either true or false based on whether the panel is visible or not.

* **Example**

  ```javascript
  var showMin = cv.api.report.getFieldOption("[Measures].[Sales]", "showMin");

  ```

## showMax

This option allows the user to show or hide the max value panel. There are two acceptable strings for the value parameter, true and false. This option is available only for measures.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "showMax", "true");

  ```

The current value of `showMax` for a field can be retrieved using the `getFieldOption` method. This function returns either true or false based on whether the panel is visible or not.

* **Example**

  ```javascript
  var showMax = cv.api.report.getFieldOption("[Measures].[Sales]", "showMax");

  ```

## showSubtotal

This option allows the user to show or hide the subtotal panel. There are two acceptable strings for the value parameter, true and false. This option is available only for measures.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Markets].[Territory]", "showSubtotal", "true");
  ```

The current value of `showSubtotal` for a field can be retrieved using the `getFieldOption` method. This function returns either true or false based on whether the panel is visible or not.

* **Example**

  ```javascript
  var subTotal = cv.api.report.getFieldOption("[Markets].[Territory]", "showSubtotal");
  ```

## formatShortcut

This option allows the user to define conditional formatting on a measure. The value parameter can be set to one of the following options:

* NONE - remove all color formatting.
* COLOR\_SCALE\_G\_Y\_R - green, yellow and red gradients are applied from maximum value to minimum value.
* COLOR\_SCALE\_R\_Y\_G - red, yellow and green gradients are applied from maximum value to minimum value.
* COLOR\_SCALE\_B\_Y\_R - blue, yellow and red gradients are applied from maximum value to minimum value.
* COLOR\_SCALE\_R\_Y\_B - red, yellow and blue gradients are applied from maximum value to minimum value.
* TREND\_ARROW\_GR - gradient for green arrow.
* TREND\_ARROW\_RG - gradient for red arrow.
* DATA\_BAR\_RED - red gradient for bar scale.
* DATA\_BAR\_GREEN - green gradient for bar scale.
* DATA\_BAR\_BLUE - blue gradient for bar scale.
* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "formatShortcut", "DATA_BAR_BLUE");

  ```

The current value of `formatShortcut` for a field can be retrieved using the `getFieldOptions` method. This function returns the shortcut color gradient as a string.

* **Example**

  ```javascript
  var format = cv.api.report.getFieldOption("[Measures].[Sales]", "formatShortcut");

  ```

## formatCategory

This option allows the user to define category formatting on a measure. The following strings are acceptable for the the value parameter: Default, General Number, Currency ($), Percentage (%), Expression.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "formatCategory", "Percentage (%)");

  ```

The current value of `formatCategory` for a field can be retrieved using the `getFieldOption` method. This function returns the category as a string.

* **Example**

  ```javascript
  var category = cv.api.report.getFieldOption("[Measures].[Sales]", "formatCategory")

  ```

## formatScale

This option allows the user to set the number of decimal digits used in a measure. The parameter value can have one of the following string values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. The user can see this result with any `formatCategory` except for Expression, since it is not a numeric value.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "formatScale", "3");

  ```

The current value of `formatScale` for a field can be retrieved using the `getFieldOption` method. This function returns the scale as a string.

* **Example**

  ```javascript
  var scale = cv.api.report.getFieldOption("[Measures].[Sales]", "formatScale");

  ```

## formatExpression

This option allows the user to define an MDX expression for formatting a measure. This can only be used with the `formatCategory` set to Expression. The value parameter must be a string representation of a valid MDX expression.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "formatExpression", "Case When [Measures].CurrentMember > 0 Then '~~#,##0~~' Else '|#,##0' End");
  ```

The current value of `formatExpression` for a field can be retrieved using the `getFieldOptions` method. This function returns the MDX expression as a string.

* **Example**

  ```javascript
  cv.api.report.getFieldOption("[Measures].[Sales]", "formatExpression");

  ```

## currencySymbol

This option allows the user to set the currency symbol for a measure. This symbol is displayed with the value of a measure. The value parameter can be any string value. This option only works with `formatCategory = “Currency ($)”`.

* **Example**

  ```javascript
  cv.api.report.setFieldOption("[Measures].[Sales]", "currencySymbol", "!!!");

  ```

The current value of `currencySymbol` for a field can be retrieved using the `getFieldOption` method. This function returns the currency symbol as a string.

* **Example**

  ```javascript
  cv.api.report.getFieldOption("[Measures].[Sales]", "currencySymbol");

  ```
