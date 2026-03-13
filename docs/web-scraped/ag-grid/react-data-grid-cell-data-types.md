# Source: https://ag-grid.com/react-data-grid/cell-data-types/

Title: React Grid: Cell Data Types | AG Grid

URL Source: https://ag-grid.com/react-data-grid/cell-data-types/

Published Time: Fri, 13 Feb 2026 11:23:35 GMT

Markdown Content:
Working with values of different data types is made easy by using cell data types.

This allows different grid features to work without any additional configuration, including [Rendering](https://ag-grid.com/react-data-grid/cell-content/), [Editing](https://ag-grid.com/react-data-grid/cell-editing/), [Filtering](https://ag-grid.com/react-data-grid/filtering/), [Sorting](https://ag-grid.com/react-data-grid/row-sorting/), [Row Grouping](https://ag-grid.com/react-data-grid/grouping/) and Import & Export ([CSV Export](https://ag-grid.com/react-data-grid/csv-export/), [Excel Export](https://ag-grid.com/react-data-grid/excel-export/), [Clipboard](https://ag-grid.com/react-data-grid/clipboard/)).

Enable Cell Data Types [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#enable-cell-data-types)
---------------------------------------------------------------------------------------------------------------

There are a number of pre-defined cell data types: `'text'`, `'number'`, `'bigint'`, `'boolean'`, `'date'`, `'dateString'`, `'dateTime'`, `'dateTimeString'` and `'object'`.

These are enabled by default, with the data type being inferred from the row data if possible (see [Inferring Data Types](https://ag-grid.com/react-data-grid/cell-data-types/#inferring-data-types)).

Specific cell data types can also be defined by setting the `cellDataType` property on the column definition.

```
const [columnDefs, setColumnDefs] = useState([
    {
        field: 'athlete',
        // enables cell data type `text`
        cellDataType: 'text'
    }
]);

<AgGridReact columnDefs={columnDefs} />
```

The following example demonstrates the pre-defined cell data types (most of which are inferred from the row data):

*   The **Athlete** column has a `'text'` data type.
*   The **Age** column has a `'number'` data type.
*   The **Total (BigInt)** column has a `'bigint'` data type.
*   The **Gold** column has a `'boolean'` data type.
*   The **Date** column has a `'date'` data type (cell values are `Date` objects).
*   The **DateTime** column has a `'dateTime'` data type (cell values are `Date` objects). This is explicitly set to `cellDataType: 'dateTime'` as `Date` objects are inferred to be `'date'` data type.
*   The **Date (String)** column has a `'dateString'` data type (cell values are `string`s representing dates).
*   The **DateTime (String)** column has a `'dateTimeString'` data type (cell values are `string`s representing dates).
*   The **Country** column has an `'object'` data type. This also [Overrides the Pre-Defined Cell Data Type Definition](https://ag-grid.com/react-data-grid/cell-data-types/#overriding-the-pre-defined-cell-data-type-definitions) so that the value parser and formatter work with the object structure.

Inferring Data Types [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#inferring-data-types)
-----------------------------------------------------------------------------------------------------------

By default, the grid will infer cell data types the first time that row data is passed into the grid.

For inference to work for a column, it must contain non-null values and have the `field` property set. The resolved column definition (including the default column definition and column types) must also not have the Value Getter, Value Parser or reference data properties set, or be using [Sparklines](https://ag-grid.com/react-data-grid/sparklines-overview/). If these conditions are not met, no cell data type will be set (it will need to be defined directly on the column if desired).

Because `'dateTime'` corresponds to cell values that are `Date` objects, there is no easy way to tell them apart from regular `'date'` columns. If you wish to enable `'dateTime'`'s higher precision fields, please explicitly specify `cellDataType: 'dateTime'` in the corresponding `columnDefs` entry.

Data type inference can be disabled by setting `cellDataType = false` on an individual column, or for all columns on the [Default Column Definition](https://ag-grid.com/react-data-grid/column-definitions/#default-column-definitions).

Note that where inference is possible, but it does not match any of the pre-defined cell data types, it will default to `object`.

Inferring cell data types only works for the Client-Side Row Model. For other row models, you will need to define cell data types for each column.

Pre-Defined Cell Data Types [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#pre-defined-cell-data-types)
-------------------------------------------------------------------------------------------------------------------------

Each of the pre-defined cell data types work by setting specific column definition properties with default values/callbacks. This enables the different grid features to work correctly for that data type.

The column definition properties that are set based on the cell data type will override any in the [Default Column Definition](https://ag-grid.com/react-data-grid/column-definitions/#default-column-definitions), but will be overridden by any [Column Type](https://ag-grid.com/react-data-grid/column-definitions/#default-column-definitions) properties as well as properties set directly on individual column definitions. Note that for `filterParams`, only nested properties on the default column definition will be overridden (rather than the entire object).

If you wish to override one of the properties set below for all types, you can do so by creating a [Column Type](https://ag-grid.com/react-data-grid/column-definitions/#default-column-definitions), and assigning the column type to the [Default Column Definition](https://ag-grid.com/react-data-grid/column-definitions/#default-column-definitions).

All the cell data types set the following (unless specified):

*   A [Value Parser](https://ag-grid.com/react-data-grid/value-parsers/) to convert from `string` to the relevant data type.
*   A [Value Formatter](https://ag-grid.com/react-data-grid/value-formatters/) to convert from the relevant data type to `string` (except for `'text'`).
*   A [Key Creator](https://ag-grid.com/react-data-grid/grouping-data/#grouping-on-object-data) which uses the Value Formatter to allow Row Grouping to work (except for `'number'` and `'text'`).

Note that when using cell data types, the Value Formatter will not run for values in group columns (as they have already been formatted), or for aggregated values where the data type can differ. To apply custom formatting in these cases, cell data types will need to be disabled for the underlying columns.

### Text [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#text)

The `'text'` cell data type is used for `string` values. As most grid functionality works directly with `string` values, the `'text'` cell data type does not set any properties outside the ones specified above for all data types.

### Number [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#number)

The `'number'` cell data type is used for `number` values.

The following properties are set:

*   The [Number Cell Editor](https://ag-grid.com/react-data-grid/provided-cell-editors-number/) is used for editing.
*   When the [Set Filter is Disabled by Default](https://ag-grid.com/react-data-grid/filter-set/#suppress-set-filter-by-default), the [Number Filter](https://ag-grid.com/react-data-grid/filter-number/) is used.
*   When the [Set Filter](https://ag-grid.com/react-data-grid/filter-set/) is used, `filterParams.comparator` is set to [Sort the Filter List](https://ag-grid.com/react-data-grid/filter-set-filter-list/#sorting-filter-lists).

To show only a certain number of decimal places, you can [Override the Pre-Defined Cell Data Type Definition](https://ag-grid.com/react-data-grid/cell-data-types/#overriding-the-pre-defined-cell-data-type-definitions) and provide your own Value Formatter. It is also possible to control the number of decimal places allowed during editing, by providing a precision to the [Number Cell Editor](https://ag-grid.com/react-data-grid/provided-cell-editors-number/).

### BigInt [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#bigint)

The `'bigint'` cell data type is used for `bigint` values.

The following properties are set:

*   The [Text Cell Editor](https://ag-grid.com/react-data-grid/provided-cell-editors-text/) is used for editing, with the Value Parser converting input to `bigint`.
*   When the [Set Filter is Disabled by Default](https://ag-grid.com/react-data-grid/filter-set/#suppress-set-filter-by-default), the [BigInt Filter](https://ag-grid.com/react-data-grid/filter-bigint/) is used.
*   When the [Set Filter](https://ag-grid.com/react-data-grid/filter-set/) is used, `filterParams.comparator` is set to sort the filter list using `bigint` comparisons.
*   A `comparator` is defined to allow [Custom Sorting](https://ag-grid.com/react-data-grid/row-sorting/#custom-sorting) using `bigint` values, including absolute sort.

BigInt behaviour and limitations:

*   Inputs must be decimal integers. Both `500` and `500n` are accepted, but hex, binary, decimals, and scientific notation are rejected.
*   Values are displayed as plain strings by default. Use a Value Formatter to add separators or custom formatting.
*   Aggregation and pivoting support `sum`, `min`, `max`, `count`. `avg` uses integer division when any `bigint` values are present, so the fractional part is discarded.
*   CSV and clipboard export use the exact integer string. Excel export defaults to Text to avoid precision loss; you can opt into Number via [Excel export styles](https://ag-grid.com/javascript-data-grid/excel-export-data-types/), but large values may lose precision.

If you need a custom input format, provide a custom Value Parser/Formatter by [Overriding the Pre-Defined Cell Data Type Definition](https://ag-grid.com/react-data-grid/cell-data-types/#overriding-the-pre-defined-cell-data-type-definitions).

### Boolean [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#boolean)

The `'boolean'` cell data type is used for `boolean` values.

The following properties are set:

*   The Checkbox Cell Renderer is used for rendering, which displays a checkbox. Set `cellRendererParams.disabled=true` for the checkbox to be read only.
*   The [Checkbox Cell Editor](https://ag-grid.com/react-data-grid/provided-cell-editors-checkbox/) is used for editing (similar to the renderer).
*   `suppressKeyboardEvent` is set to enable the ␣ Space key to toggle the renderer value.
*   When the [Set Filter is Disabled by Default](https://ag-grid.com/react-data-grid/filter-set/#suppress-set-filter-by-default), the [Text Filter](https://ag-grid.com/react-data-grid/filter-text/) is used.
*   When the Text Filter is used, `filterParams` is set to display a single dropdown with `'True'`/`'False'` (or equivalents with [Localisation](https://ag-grid.com/react-data-grid/localisation/)).
*   When the [Set Filter](https://ag-grid.com/react-data-grid/filter-set/) is used, `filterParams.valueFormatter` is set to show `'True'`/`'False'` (or equivalents with [Localisation](https://ag-grid.com/react-data-grid/localisation/)).

### Date [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#date)

The `'date'` cell data type is used for date values that are represented as `Date` objects.

The default Value Parser and Value Formatter use the ISO string format `'YYYY-MM-DD'`. If you wish to use a different date format, then you can [Override the Pre-Defined Cell Data Type Definition](https://ag-grid.com/react-data-grid/cell-data-types/#overriding-the-pre-defined-cell-data-type-definitions).

Please note that the `'date'` cell data type compares full Date objects, including the time portion. As a result, if a date includes a time other than midnight (`00:00:00.000`), filtering or editing might behave unexpectedly. For consistent results with built-in filters, it’s best to normalize all time values to the same value. If keeping the time component is important, consider using the `'dateTime'` cell data type instead or defining a custom comparator, as explained in the [Date Filter Comparator](https://ag-grid.com/react-data-grid/filter-date/#filter-comparator).

The following properties are set:

*   The [Date Cell Editor](https://ag-grid.com/react-data-grid/provided-cell-editors-date/) is used for editing.
*   When the [Set Filter is Disabled by Default](https://ag-grid.com/react-data-grid/filter-set/#suppress-set-filter-by-default), the [Date Filter](https://ag-grid.com/react-data-grid/filter-date/) is used.
*   When the [Set Filter](https://ag-grid.com/react-data-grid/filter-set/) is used, the [Set Filter Tree List](https://ag-grid.com/react-data-grid/filter-set-tree-list/) is enabled, and the [Values are Formatted](https://ag-grid.com/react-data-grid/filter-set-tree-list/#formatting-values) by setting `filterParams.treeListFormatter` to convert the months to names and `filterParams.valueFormatter` to format the Floating Filter values using the Value Formatter.

### Date as String [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#date-as-string)

The `'dateString'` cell data type is used for date values that are represented as `string` values.

This data type uses the ISO string format `'YYYY-MM-DD'`. If you wish to use a different date format, then you can [Override the Pre-Defined Cell Data Type Definition](https://ag-grid.com/react-data-grid/cell-data-types/#overriding-the-pre-defined-cell-data-type-definitions).

The following properties are set:

*   The [Date as String Cell Editor](https://ag-grid.com/react-data-grid/provided-cell-editors-date/#enabling-date-as-string-cell-editor) is used for editing.
*   When the [Set Filter is Disabled by Default](https://ag-grid.com/react-data-grid/filter-set/#suppress-set-filter-by-default), the [Date Filter](https://ag-grid.com/react-data-grid/filter-text/) is used.
*   When the Date Filter is used, `filterParams.comparator` is set to parse the `string` date values.
*   When the [Set Filter](https://ag-grid.com/react-data-grid/filter-set/) is used, the [Set Filter Tree List](https://ag-grid.com/react-data-grid/filter-set-tree-list/) is enabled, with `filterParams.treeListPathGetter` set to convert the `string` date values into paths, and the [Values are Formatted](https://ag-grid.com/react-data-grid/filter-set-tree-list/#formatting-values) by setting `filterParams.treeListFormatter` to convert the months to names and `filterParams.valueFormatter` to format the Floating Filter values using the Value Formatter.

### DateTime [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#datetime)

The `'dateTime'` cell data type is used for date and time values that are represented as `Date` objects. Unlike the `'date'` cell data type which only shows the date portion, `'dateTime'` displays both date and time components.

This data type uses the ISO string format `'YYYY-MM-DDThh:mm:ssZ'`. If you wish to use a different format, you can [Override the Pre-Defined Cell Data Type Definition](https://ag-grid.com/react-data-grid/cell-data-types/#overriding-the-pre-defined-cell-data-type-definitions).

The following properties are set:

*   The [Date Cell Editor](https://ag-grid.com/react-data-grid/provided-cell-editors-date/) is used for editing.
*   When the [Set Filter is Disabled by Default](https://ag-grid.com/react-data-grid/filter-set/#suppress-set-filter-by-default), the [Date Filter](https://ag-grid.com/react-data-grid/filter-date/) is used.
*   When the [Set Filter](https://ag-grid.com/react-data-grid/filter-set/) is used, the [Set Filter Tree List](https://ag-grid.com/react-data-grid/filter-set-tree-list/) is enabled, and the [Values are Formatted](https://ag-grid.com/react-data-grid/filter-set-tree-list/#formatting-values) by setting `filterParams.treeListFormatter` to convert the months to names and `filterParams.valueFormatter` to format the Floating Filter values using the Value Formatter.

### DateTime as String [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#datetime-as-string)

The `'dateTimeString'` cell data type is used for date and time values that are represented as `string` values. Unlike the `'dateString'` cell data type which only shows the date portion, `'dateTimeString'` displays both date and time components.

This data type uses the ISO string format `'YYYY-MM-DDThh:mm:ssZ'`. If you wish to use a different format, you can [Override the Pre-Defined Cell Data Type Definition](https://ag-grid.com/react-data-grid/cell-data-types/#overriding-the-pre-defined-cell-data-type-definitions).

The following properties are set:

*   The [Date as String Cell Editor](https://ag-grid.com/react-data-grid/provided-cell-editors-date/#enabling-date-as-string-cell-editor) is used for editing.
*   When the [Set Filter is Disabled by Default](https://ag-grid.com/react-data-grid/filter-set/#suppress-set-filter-by-default), the [Date Filter](https://ag-grid.com/react-data-grid/filter-text/) is used.
*   When the Date Filter is used, `filterParams.comparator` is set to parse the `string` date values.
*   When the [Set Filter](https://ag-grid.com/react-data-grid/filter-set/) is used, the [Set Filter Tree List](https://ag-grid.com/react-data-grid/filter-set-tree-list/) is enabled, with `filterParams.treeListPathGetter` set to convert the `string` date values into paths, and the [Values are Formatted](https://ag-grid.com/react-data-grid/filter-set-tree-list/#formatting-values) by setting `filterParams.treeListFormatter` to convert the months to names and `filterParams.valueFormatter` to format the Floating Filter values using the Value Formatter.

### Object [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#object)

The `'object'` cell data type is used for values that are complex objects (e.g. none of the above data types).

If you have different types of complex object, you will want to [Provide Custom Cell Data Types](https://ag-grid.com/react-data-grid/cell-data-types/#providing-custom-cell-data-types).

For objects to work properly, you must provide a Value Formatter, and a Value Parser if editing is enabled. This is because their behaviour needs to change based on the object structure. Generally these should be provided on the data type definition, but they can be provided directly on the column if necessary.

The following properties are set:

*   `cellEditorParams.useFormatter = true` so that the cell editor uses the Value Formatter.
*   A `comparator` is defined to allow [Custom Sorting](https://ag-grid.com/react-data-grid/row-sorting/#custom-sorting) using the Value Formatter.
*   When the [Text Filter](https://ag-grid.com/react-data-grid/filter-text/) is used, a [Filter Value Getter](https://ag-grid.com/react-data-grid/column-properties/#reference-filtering-filterValueGetter) is used to convert the value with the Value Formatter.
*   When the [Set Filter](https://ag-grid.com/react-data-grid/filter-set/) is used, `filterParams.valueFormatter` is set to format the values using the Value Formatter.

### Pre-Defined Cell Data Type Example [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#pre-defined-cell-data-type-example)

The [Enable Cell Data Types Example](https://ag-grid.com/react-data-grid/cell-data-types/#example-enable-cell-data-types) above demonstrates each of the different pre-defined cell data types with AG Grid Community.

The example below shows the same data types in AG Grid Enterprise:

*   Row grouping is enabled allowing each of the fields to be grouped on.
*   Import/Export features are enabled allowing the following:
    *   Clipboard (copy/paste)
    *   Fill handle
    *   CSV/Excel export

Providing Custom Cell Data Types [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#providing-custom-cell-data-types)
-----------------------------------------------------------------------------------------------------------------------------------

Custom cell data types can be added by setting the grid option `dataTypeDefinitions`.

data Type Definitions

[Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#reference-columns-dataTypeDefinitions)

DataTypeDefinitions

An object map of cell data types to their definitions. Cell data types can either override/update the pre-defined data types (`'text'`, `'number'`, `'boolean'`, `'date'`, `'dateString'`, `'dateTime'`, `'dateTimeString'` or `'object'`), or can be custom data types.

```
const dataTypeDefinitions = useMemo(() => { 
	return {
        percentage: {
            extendsDataType: 'number',
            baseDataType: 'number',
            valueFormatter: params => params.value == null
                ? ''
                : `${Math.round(params.value * 100)}%`,
        }
    };
}, []);

<AgGridReact dataTypeDefinitions={dataTypeDefinitions} />
```

Each custom data type definition must have a `baseDataType` of one of the [Pre-Defined Cell Data Types](https://ag-grid.com/react-data-grid/cell-data-types/#pre-defined-cell-data-types), which represents the data type of the underlying cell values.

Data type definitions support inheritance via the `extendsDataType` property. Each custom cell data type must either extend one of the pre-defined types, or another custom type. Any non-overridden properties are inherited from the parent definition. To prevent inheriting properties from the parent definition, `suppressDefaultProperties = true` can be set on the definition.

[Column Types](https://ag-grid.com/react-data-grid/column-definitions/#default-column-definitions) can be set via the `columnTypes` property to allow other column definition properties to be set for the data type. By default, these will replace any column types against the parent definition. To allow these to be appended to the parent definition column types, `appendColumnTypes = true` can be set.

To allow [Inferring Cell Data Types](https://ag-grid.com/react-data-grid/cell-data-types/#inferring-cell-data-types) to work for custom types, the `dataTypeMatcher` property can be set. This returns `true` if the value is of the correct type. Note that the data type matchers will be called in the order they are provided in `dataTypeDefinitions` (for custom only), and then the pre-defined data type matchers will be called.

The following example demonstrates providing custom cell data types:

*   The **Country** column contains complex objects and has a cell data type of `'country'`.
*   The **Sport** column contains a different type of complex object and has a cell data type of `'sport'`.
*   The **Date** column parses date values from a non-standard date format.
*   The `dataTypeMatcher` callback is defined for all three cell data types to allow inferring the type.

Overriding the Pre-Defined Cell Data Type Definitions [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#overriding-the-pre-defined-cell-data-type-definitions)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default properties for the [Pre-Defined Cell Data Types](https://ag-grid.com/react-data-grid/cell-data-types/#pre-defined-cell-data-types) can be overridden.

For example, this is required if a different date format is desired.

This works in the same way as when [Providing Custom Cell Data Types](https://ag-grid.com/react-data-grid/cell-data-types/#providing-custom-cell-data-types).

```
const dataTypeDefinitions = useMemo(() => { 
	return {
        // override `date` to handle custom date format `dd/mm/yyyy`
        date: {
            baseDataType: 'date',
            extendsDataType: 'date',
            valueParser: params => {
                if (params.newValue == null) {
                    return null;
                }
                // convert from `dd/mm/yyyy`
                const dateParts = params.newValue.split('/');
                return dateParts.length === 3 ? new Date(
                    parseInt(dateParts[2]),
                    parseInt(dateParts[1]) - 1,
                    parseInt(dateParts[0])
                ) : null;
            },
            valueFormatter: params => {
                // convert to `dd/mm/yyyy`
                const date = params.value;
                return date == null
                    ? ''
                    : `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}`;
            },
        }
    };
}, []);

<AgGridReact dataTypeDefinitions={dataTypeDefinitions} />
```

The following example demonstrates overriding pre-defined cell data types:

*   The **Date** column is of type `'dateString'` which has been overridden to use a different date format (`dd/mm/yyyy`).
*   The data type definition for `'dateString'` provides a `dateParser` and `dateFormatter` as it is a [Date as String Data Type Definition](https://ag-grid.com/react-data-grid/cell-data-types/#date-as-string).
*   The **DateTimeWithSpace** column overrides a built-in `'dateTimeString'` type with custom parsing/formatting logic to support `dd/MM/yyyy HH:mm:ss` format instead of the default `yyyy-MM-ddTHH:mm:ss`.

### Date and DateTime as String Data Type Definition [Copy Link](https://ag-grid.com/react-data-grid/cell-data-types/#date-and-datetime-as-string-data-type-definition)

If overriding `'dateString'` or `'dateTimeString''` with a different date format, then a couple of extra properties need to be set to handle conversion between `Date` objects and the desired `string` format.

Function

Converts a date in `string` format to a `Date`.
Function

Converts a date in `Date` format to a `string`.
