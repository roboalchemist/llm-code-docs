# Source: https://docs.pentaho.com/pba/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties/properties-of-time-dimension-levels.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties/properties-of-time-dimension-levels.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties/properties-of-time-dimension-levels.md

# Properties of time dimension levels

The **Time Level Type** and **Source Column Format** drop-down menus in the **Properties** pane of the Data Source Model Editor allow you to specify how time-specific data is formatted in your data source.

**Time Level Type** specifies the role of a level and the increment of the date it represents. **Time Level Type** is used by a number of time-period functions in Analyzer.

**Source Column Format** field lets you specify how a value in the source column is formatted and represents a date increment belonging to that level. This information is used when filtering in Analyzer to the levels of a time dimension.

Assigning the **Source Column Format** in the Data Source Model Editor does not change how the values in your data display, rather it enables you to describe the format of your data.

Here are several commonly used formats for time measurements.

* Years: `yy`, `yyyy`
* Quarters: `Q`, `QQ`, `QQQ`
* Months: `M`, `MM`, `MMM`
* Weeks: `w`, `ww`, `W`
* Days: `d`, `dd`, `D`, `DDD`, `yyyy-MM-dd`
* Hours: `k`, `kk`, `H`, `HH`, `K`, `KK`
* Minutes: `m`, `mm`
* Seconds: `s`, `ss`

If the options provided in the drop-down menu do not reflect the format of your data, you can override the formats by entering directly into the **Source Column Format** field. However, the format of your data must adhere to the [ICU](http://www-01.ibm.com/software/globalization/icu/) [Simple Date Format](http://icu-project.org/apiref/icu4j/com/ibm/icu/text/SimpleDateFormat.html) specification.

For instance, a level may have `Quarters` as **Time Level Type**, indicating the level corresponds to quarter date increments. If that value is represented by the numbers `1` through `4`, you would set the **Source Column Format** as `Q`.

Alternatively, the same increment could also be represented as strings `Q1`, `Q2`, `Q3`, and `Q4`. In this case, you specify the **Source Column Format** with the value `'Q'Q`. The first `'Q'` indicates a string, while the second, unquoted `Q` represents a numerical value, `1` through `4`.

Or, your source column could contain values like `2001-Q1`, `2001-Q2`, `2001-Q3`, `2001-Q4`, in which case you would input `yyyy-'Q'Q` into the **Source Column Format** field
