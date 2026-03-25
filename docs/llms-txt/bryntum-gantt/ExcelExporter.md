# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/experimental/ExcelExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/experimental/ExcelExporter.md

# [ExcelExporter](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter)

A feature that allows exporting Grid data to Excel or CSV without involving the server. It uses [TableExporter](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter) class as data provider, 3rd party provider to generate XLS files, and [Microsoft XML specification](https://bryntum.com/docs/gantt/api/https://msdn.microsoft.com/en-us/library/office/documentformat.openxml.spreadsheet.aspx).

```
import WriteExcelFileProvider from '../../lib/Grid/feature/experimental/xlsproviders/WriteExcelFileProvider.js';

new Grid({
    features : {
        excelExporter : {
            xlsProvider : WriteExcelFileProvider
        }
    }
});
```

### Implementing custom provider

```
// Global scope
<script src="https://cdn.jsdelivr.net/npm/write-excel-file/bundle/write-excel-file.min.js"></script>
```

```
// importing from package
import writeXlsxFile from 'write-excel-file';

const typeMap = { string : String, number : Number, date : Date };

class MyXlsProvider {
    static write({ filename, columns, rows }) {
        columns.forEach(col => delete col.type);
        rows.forEach(row => row.forEach(cell => cell.type = typeMap[cell.type] || String));

        globalThis.writeXlsxFile([columns, ...rows], {
            // write-excel-file uses amount of symbols as width, so we need to convert pixels to symbols
            columns    : columns.map(col => ({ ...col, width : Math.round(col.width / 10) })),
            fileName   : filename,
            dateFormat : 'yyyy-mm-dd'
        });
    }
}

const grid = new Grid({
    features : {
        excelExporter : {
            xlsProvider : MyXlsProvider
        }
    }
})
```

Here is an example of how to add the feature:

```
const grid = new Grid({
    features : {
        excelExporter : {
            // Choose the date format for date fields
            dateFormat : 'YYYY-MM-DD HH:mm',

            exporterConfig : {
                // Choose the columns to include in the exported file
                columns : ['name', 'role'],
                // Optional, export only selected rows
                rows    : grid.selectedRecords
            }
        }
    }
});
```

And how to call it:

```
grid.features.excelExporter.export({
    filename       : 'Export',
    exporterConfig : {
        columns : [
            { text : 'First Name', field : 'firstName', width : 90 },
            { text : 'Age', field : 'age', width : 40 },
            { text : 'Starts', field : 'start', width : 140 },
            { text : 'Ends', field : 'finish', width : 140 }
        ]
    }
})
```

Exporting to CSV is done with the `csv` config:

```
grid.features.excelExporter.export({
    filename : 'myfile',
    csv      : true
})
```

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

This feature will not work properly when Store uses [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad)

This class requires a 3rd party library to export to XLSX

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[filename](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#config-filename)
Name of the exported file

[dateFormat](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#config-dateFormat)
Defines how dates in a cell will be formatted

[exporterClass](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#config-exporterClass)
Exporter class to use as a data provider. [TableExporter](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter) by default.

[exporterConfig](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#config-exporterConfig)
Configuration object for [exporter class](https://bryntum.com/docs/gantt/api/#Grid/feature/experimental/ExcelExporter#config-exporterClass).

[xlsProvider](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#config-xlsProvider)
This hook allows to use 3rd party libraries to generate XLSX files.

The default provider is the built-in [WriteExcelFileProvider](https://bryntum.com/docs/gantt/api/#Grid/feature/experimental/xlsproviders/WriteExcelFileProvider).

A custom provider must extend [XlsProviderBase](https://bryntum.com/docs/gantt/api/#Grid/feature/experimental/xlsproviders/XlsProviderBase) and implement a static [write](https://bryntum.com/docs/gantt/api/#Grid/feature/experimental/xlsproviders/XlsProviderBase#function-write-static) method.

[csvMimeType](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#config-csvMimeType)
Allows configuring MIME type of the exported CSV file

[convertEmptyValueToEmptyString](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#config-convertEmptyValueToEmptyString)
If this config is true, exporter will convert all empty values to ''. Empty values are:

* undefined, null, NaN
* Objects/class instances that do not have toString method defined and are stringified to \[object Object\]
* functions

[exportAllColumns](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#config-exportAllColumns)
Set this config to `true` to export all [exportable](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-exportable) columns including [hidden](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-hidden) columns as well.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isExcelExporter](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#property-isExcelExporter)
Identifies an object as an instance of [ExcelExporter](https://bryntum.com/docs/gantt/api/#Grid/feature/experimental/ExcelExporter) class, or subclass thereof.

[isExcelExporter](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#property-isExcelExporter-static)
Identifies an object as an instance of [ExcelExporter](https://bryntum.com/docs/gantt/api/#Grid/feature/experimental/ExcelExporter) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[export](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#function-export)
Generate and download an Excel (.xlsx), or CSV file (.csv).

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeCSVExport](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#event-beforeCSVExport)
Fires on the owning Grid before CSV export starts. Return `false` to cancel the export.

[beforeExcelExport](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#event-beforeExcelExport)
Fires on the owning Grid before Excel export starts. Return `false` to cancel the export.

## Typedefs

Typedefs are type definitions for the class

[ExportConfig](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/ExcelExporter#typedef-ExportConfig)
Object describing config param for `beforeExcelExport` and `beforeCSVExport` event.
