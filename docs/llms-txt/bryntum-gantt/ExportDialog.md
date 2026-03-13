# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/export/ExportDialog.md

# [ExportDialog](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog)

Dialog window used by the [PDF export feature](https://bryntum.com/docs/gantt/api/#Grid/feature/export/PdfExport). It allows users to select export options like paper format and columns to export. This dialog contains a number of predefined [fields](https://bryntum.com/docs/gantt/api/#Core/widget/Field) which you can access through the popup's [widgetMap](https://bryntum.com/docs/gantt/api/#Grid/view/export/ExportDialog#property-widgetMap).

Default widgets
---------------

The default widgets of this dialog are:

Widget ref

Type

Weight

Description

`columnsField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

100

Choose columns to export

`rowsRangeField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

200

Choose which rows to export

`exporterTypeField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

300

Type of the exporter to use

`alignRowsField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

400

Align row top to the page top on every exported page

`repeatHeaderField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

500

Toggle repeating headers on / off

`fileFormatField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

600

Choose file format

`paperFormatField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

700

Choose paper format

`orientationField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

800

Choose orientation

The default buttons are:

Widget ref

Type

Weight

Description

`exportButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

100

Triggers export

`cancelButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

200

Cancel export

Bottom buttons may be customized using `bbar` config passed to `exportDialog`:

```
const grid = new Grid({
    features : {
        pdfExport : {
            exportDialog : {
                bbar : {
                    items : {
                        exportButton : { text : 'Go!' }
                    }
                }
            }
        }
    }
});
```

Configuring default widgets
---------------------------

Widgets can be customized with [exportDialog](https://bryntum.com/docs/gantt/api/#Grid/feature/export/PdfExport#config-exportDialog) config:

```
const grid = new Grid({
    features : {
        pdfExport : {
            exportDialog : {
                items : {
                    // hide the field
                    orientationField  : { hidden : true },

                    // reorder fields
                    exporterTypeField : { weight : 150 },

                    // change default format in exporter
                    fileFormatField   : { value : 'png' }
                }
            }
        }
    }
});

grid.features.pdfExport.showExportDialog();
```

Configuring default columns
---------------------------

By default all visible columns are selected in the export dialog. This is managed by the [autoSelectVisibleColumns](https://bryntum.com/docs/gantt/api/#Grid/view/export/ExportDialog#config-autoSelectVisibleColumns) config. To change default selected columns you should disable this config and set field value. Value should be an array of valid column ids (or column instances). This way you can preselect hidden columns:

```
const grid = new Grid({
    columns : [
        { id : 'name', text : 'Name', field : 'name' },
        { id : 'age', text : 'Age', field : 'age' },
        { id : 'city', text : 'City', field : 'city', hidden : true }
    ],
    features : {
        pdfExport : {
            exportDialog : {
                autoSelectVisibleColumns : false,
                items : {
                    columnsField : { value : ['name', 'city'] }
                }
            }
        }
    }
})

// This will show export dialog with Name and City columns selected
// even though City column is hidden in the UI
grid.features.pdfExport.showExportDialog();
```

Adding fields
-------------

You can add your own fields to the export dialog. To make such field value acessible to the feature it should follow a specific naming pattern - it should have `ref` config ending with `Field`, see other fields for reference - `orientationField`, `columnsField`, etc. Fields not matching this pattern are ignored. When values are collected from the dialog, `Field` part of the widget reference is removed, so `orientationField` becomes `orientation`, `fooField` becomes `foo`, etc.

```
const grid = new Grid({
    features : {
        pdfExport : {
            exportDialog : {
                items : {
                    // This field gets into export config
                    fooField : {
                        type : 'text',
                        label : 'Foo',
                        value : 'FOO'
                    },

                    // This one does not, because name doesn't end with `Field`
                    bar : {
                        type : 'text',
                        label : 'Bar',
                        value : 'BAR'
                    },

                    // Add a container widget to wrap some fields together
                    myContainer : {
                        type : 'container',
                        items : {
                            // This one gets into config too despite the nesting level
                            bazField : {
                                type : 'text',
                                label : 'Baz',
                                value : 'BAZ'
                            }
                        }
                    }
                }
            }
        }
    }
});

// Assuming export dialog is opened and export triggered with default values
// you can receive custom field values here
grid.on({
    beforePdfExport({ config }) {
        console.log(config.foo) // 'FOO'
        console.log(config.bar) // undefined
        console.log(config.baz) // 'BAZ'
    }
});
```

Configuring widgets at runtime
------------------------------

If you don't know column ids before grid instantiation or you want a flexible config, you can change widget values before dialog pops up:

```
const grid = new Grid({
    columns : [
        { id : 'name', text : 'Name', field : 'name' },
        { id : 'age', text : 'Age', field : 'age' },
        { id : 'city', text : 'City', field : 'city', hidden : true }
    ],
    features : {
        pdfExport : true
    }
});

// Such listener would ignore autoSelectVisibleColumns config. Similar to the snippet
// above this will show Name and City columns
grid.features.pdfExport.exportDialog.on({
    beforeShow() {
        this.widgetMap.columnsField.value = ['age', 'city']
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[client](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#config-client)
Grid instance to build export dialog for

[autoSelectVisibleColumns](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#config-autoSelectVisibleColumns)
Set to `false` to not preselect all visible columns when the dialog is shown

[hidePNGMultipageOption](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#config-hidePNGMultipageOption)
Set to `false` to allow using PNG + Multipage config in export dialog

[useBrowserPrint](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#config-useBrowserPrint)
When set to `true` labels in the dialog will say `Print` instead of `Export`

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isExportDialog](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#property-isExportDialog)
Identifies an object as an instance of [ExportDialog](https://bryntum.com/docs/gantt/api/#Grid/view/export/ExportDialog) class, or subclass thereof.

[isExportDialog](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#property-isExportDialog-static)
Identifies an object as an instance of [ExportDialog](https://bryntum.com/docs/gantt/api/#Grid/view/export/ExportDialog) class, or subclass thereof.

[values](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#property-values)
Returns map of values of dialog fields.

[useBrowserPrint](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#property-useBrowserPrint)
When set to `true` labels in the dialog will say `Print` instead of `Export`

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[export](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#event-export)
Fires when export button is clicked

[cancel](https://bryntum.com/docs/gantt/api/Grid/view/export/ExportDialog#event-cancel)
Fires when cancel button is clicked. Popup will hide itself.
