# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/util/TableExporter.md

# [TableExporter](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter)

This class transforms grid component into two arrays: rows and columns. Columns array contains objects with meta information about column: field name, column name, width and type of the rendered value, rows array contains arrays of cell values.

```
const exporter = new TableExporter({ target : grid });
exporter.export()

// Output
{
    columns : [
        { field : 'name',     value : 'First name', type : 'string',  width : 100 },
        { field : 'surname',  value : 'Last name',  type : 'string',  width : 100 },
        { field : 'age',      value : 'Age',        type : 'number',  width : 50  },
        { field : 'married',  value : 'Married',    type : 'boolean', width : 50  },
        { field : 'children', value : 'Children',   type : 'object',  width : 100 }
    ],
    rows : [
        ['Michael', 'Scott',   40, false, []],
        ['Jim',     'Halpert', 30, true,  [...]]
    ]
}
```

How data is exported
--------------------

Exporter iterates over store records and processes each record for each column being exported. Exporter uses same approach to retrieve data as column: reading record field, configured on the column, or calling renderer function if one is provided. This means data can be of any type: primitives or objects. So children array in the above code snippet may contain instances of child record class.

Column renderers
----------------

Column renderers are commonly used to style the cell, or even render more HTML into it, like [WidgetColumn](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn) does. This is not applicable in case of export. Also, given grid uses virtual rendering (only renders visible rows) and exporter iterates over all records, not just visible ones, we cannot provide all data necessary to the renderer. Some arguments, like cellElement and row, wouldn't exist. Thus, the renderer is called with as much data we have: value, record, column, grid, other [documented arguments](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) would be undefined.

Exporter adds one more flag for renderer function: isExport. When renderer receives this flag it knows data is being exported and can skip DOM work to return simpler value. Below snippet shows simplified code of the widget column handling export:

```
renderer({ isExport }) {
    if (isExport) {
        return null;
    }
    else {
        // widget rendering routine
        ...
    }
}
```

Column types
------------

Column types are not actually a complete list of JavaScript types (you can get actual type of the cell using typeof) it is a simple and helpful meta information.

Available column types are:

* string
* number
* boolean
* date
* object

Everything which is not primitive like string/number/bool (or a date) is considered an object. This includes null, undefined, arrays, classes, functions etc.

Getting column type
-------------------

If existing grid column is used, column type first would be checked with [exportedType](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-exportedType) config. If exportedType is undefined or column does not exist in grid, type is read from a record field definition. If the field is not defined, object type is used.

Configuring exported type:

```
new Grid({
    columns : [
        {
            name         : 'Name',
            field        : 'name',
            exportedType : 'object',
            renderer     : ({ value, isExport }) => {
                if (isExport) {
                    return { value }; // return value wrapped into object
                }
            }
    ]
})
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[target](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#config-target)
Target grid instance to export data from

[defaultColumnWidth](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#config-defaultColumnWidth)
Specifies a default column width if no width specified

[exportDateAsInstance](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#config-exportDateAsInstance)
Set to `false` to export dates as they are displayed by Date column formatter

[showGroupHeader](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#config-showGroupHeader)
If true and the grid is grouped, shows the grouped value in the first column. True by default.

[columns](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#config-columns)
An array of column configuration objects used to specify column widths, header text and data fields to get the data from. 'field' config is required. If 'text' is missing, it will read it from the grid column or the 'field' config. If 'width' is missing, it will try to get it retrieved from the grid column or [defaultColumnWidth](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter#config-defaultColumnWidth) config. If no columns are provided, the config will be generated from the grid columns.

For example:

```
columns : [
    'firstName', // field
    'age', // field
    { text : 'Starts', field : 'start', width : 140 },
    { text : 'Ends', field : 'finish', width : 140 }
]
```

[indent](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#config-indent)
When true and tree is being exported, node names are indented with [indentationSymbol](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter#config-indentationSymbol)

[indentationSymbol](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#config-indentationSymbol)
This symbol (four spaces by default) is used to indent node names when [indent](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter#config-indent) is `true`

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTableExporter](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#property-isTableExporter)
Identifies an object as an instance of [TableExporter](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter) class, or subclass thereof.

[isTableExporter](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#property-isTableExporter-static)
Identifies an object as an instance of [TableExporter](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[export](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#function-export)
Exports grid data according to provided config

[processColumn](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#function-processColumn)
Extracts export data from the column instance

[processRecord](https://bryntum.com/docs/gantt/api/Grid/util/TableExporter#function-processRecord)
Extracts export data from the record instance reading supplied column configs
