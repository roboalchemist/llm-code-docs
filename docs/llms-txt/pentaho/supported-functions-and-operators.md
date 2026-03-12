# Source: https://docs.pentaho.com/pba-metadata-editor/supported-functions-and-operators.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/supported-functions-and-operators.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/supported-functions-and-operators.md

# Supported functions and operators

The following functions and operators are supported by the Metadata Editor.

## Supported functions

The table below contains a listing of supported functions. Examples are shown below for each supported function.

| Function Name | Parameters                                | Description                                        |
| ------------- | ----------------------------------------- | -------------------------------------------------- |
| `OR`          | Two or more Boolean expression parameters | Returns `true` if one or more parameters are true. |

```
OR( [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "EuroCars";
                [BT_CUSTOMERS.BC_CUSTOMERS_CREDITLIMIT] > 1000 )
```

| Function Name | Parameters                                | Description                                |
| ------------- | ----------------------------------------- | ------------------------------------------ |
| `AND`         | Two or more Boolean expression parameters | Returns `true` if all parameters are true. |

```
AND( [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "EuroCars";
                [BT_CUSTOMERS.BC_CUSTOMERS_CREDITLIMIT] > 1000 )
```

| Function Name | Parameters     | Description                                                          |
| ------------- | -------------- | -------------------------------------------------------------------- |
| `LIKE`        | Two parameters | Compares a column to a regular expression, using `%` as a wild card. |

```
LIKE([BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME]; "%SMITH%")

```

| Function Name | Parameters             | Description                                                                        |
| ------------- | ---------------------- | ---------------------------------------------------------------------------------- |
| `IN`          | Two or more parameters | Checks to determine if the first parameter is in the following list of parameters. |

```
IN([BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME]; "Adam Smith"; "Brian
                Jones")
```

| Function Name | Parameters | Description      |
| ------------- | ---------- | ---------------- |
| `NOW`         | None       | The current date |

```
NOW()

```

| Function Name | Parameters                                     | Description      |
| ------------- | ---------------------------------------------- | ---------------- |
| `DATE`        | Three numeric parameters: year, month, and day | A specified date |

```
DATE(2008;4;15)
```

| Function Name | Parameters                          | Description      |
| ------------- | ----------------------------------- | ---------------- |
| `DATEVALUE`   | One text parameter "year-month-day" | A specified date |

```
DATEVALUE("2008-04-15")

```

| Function Name | Parameters             | Description                                                                                                                                                                                                                                                                                                     |
| ------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CASE`        | Two or more parameters | Evaluates the first, third, etc. parameter, and returns the second, fourth, etc. parameter value. If there are an odd number of parameters, the last parameter is returned if no other parameter evaluates to true. Note that when using this function, the formula must be set on a new column as shown below. |

```
CASE( [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "EuroCars"; "European Cars";
                [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "AsiaCars"; "Asian Cars"; "Unknown Cars"
                )
```

| Function Name | Parameters             | Description                           |
| ------------- | ---------------------- | ------------------------------------- |
| `COALESCE`    | One or more parameters | Returns the first non-null parameter. |

```
CASE( [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "EuroCars"; "European Cars";
                [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "AsiaCars"; "Asian Cars"; "Unknown Cars"
                )
```

| Function Name | Parameters                                                                                                                                           | Description                                                                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DATEMATH`    | One or more parameters; see [DateMath Javadoc for full syntax](http://javadoc.pentaho.com/bi-platform/2.0.x/org/pentaho/platform/util/DateMath.html) | <p>Returns a date based on an expression.</p><p>Note that this function does not return a timestamp irrespective of the implementation details in the description below.</p> |

\`\`\`\
DATEMATH("0:ME -1:DS") - 00:00:00.000 of the day before the last day of the current month\
DATEMATH("0:MS 0:WE") - 23:59:59.999 the last day of the first week of the month\
DATEMATH("0:ME") - 23:59:59.999 of the last day of the current month\
DATEMATH("5:Y") - the current month, day and time 5 years in the future\
DATEMATH("5:YS") - 00:00:00.000 of the first day of the years 5 years in the future\
\`\`\`

## Supported aggregate functions

The table below contains a listing of supported aggregate functions.

| Function Name | Description                                                |
| ------------- | ---------------------------------------------------------- |
| `SUM`         | Sums a specific columns values determined by grouping.     |
| `COUNT`       | Counts a specific columns values determined by grouping.   |
| `AVG`         | Averages a specific columns values determined by grouping. |
| `MIN`         | Selects the minimum column value determined by grouping.   |
| `MAX`         | Selects the maximum column value determined by grouping.   |

## Supported operators

The table below contains a listing of supported operators.

| Operator | **Description**                                                            |
| -------- | -------------------------------------------------------------------------- |
| `=`      | Returns `true` if two expressions are equal.                               |
| `>`      | Returns `true` if first expression is larger than the second.              |
| `<`      | Returns `true` if first expression is smaller than the second.             |
| `>=`     | Returns `true` if first expression is larger than or equal to the second.  |
| `<=`     | Returns `true` if first expression is smaller than or equal to the second. |
| `<>`     | Returns `true` if two expressions are not equal.                           |
| `+`      | Adds two values.                                                           |
| `-`      | Subtracts two values.                                                      |
| `*`      | Multiplies two values.                                                     |
| `/`      | Divides two values.                                                        |
