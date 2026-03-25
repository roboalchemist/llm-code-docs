# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/export/SchedulerExportDialog.md

# [SchedulerExportDialog](https://bryntum.com/docs/gantt/api/Scheduler/view/export/SchedulerExportDialog)

Extends the Grid's [ExportDialog](https://bryntum.com/docs/gantt/api/#Grid/view/export/ExportDialog) and adds a few extra fields specific to the scheduler.

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

`scheduleRangeField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

150

Choose date range to export

`rangesContainer`

[Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container)

151

Container for range fields

\>`rangeStartField`

[DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)

10

Choose date range start

\>`rangeEndField`

[DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)

30

Choose date range end

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

\>

first level of submenu

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

Configuring default widgets
---------------------------

Widgets can be customized with [exportDialog](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/PdfExport#config-exportDialog) config:

```
const scheduler = new Scheduler({
    features : {
        pdfExport : {
            exportDialog : {
                items : {
                    // hide the field
                    orientationField  : { hidden : true },

                    // reorder fields
                    exporterTypeField : { weight : 150 },

                    // change default format in exporter
                    fileFormatField   : { value : 'png' },

                    // Configure nested fields
                    rangesContainer : {
                        items : {
                            rangeStartField : { value : new Date() },
                            rangeEndField : { value : new Date() }
                        }
                    }
                }
            }
        }
    }
});

scheduler.features.pdfExport.showExportDialog();
```

Using DateTime fields for range start/end
-----------------------------------------

This config system is also capable (but not limited to) of changing layout of the container and replacing widget type:

```
const scheduler = new Scheduler({
    features : {
        pdfExport : {
            exportDialog : {
                items : {
                    rangesContainer : {
                        // DateTime fields are longer, so we better lay them out
                        // vertically
                        layoutStyle : {
                            flexDirection : 'column'
                        },
                        items : {
                            rangeStartField : {
                                // Use DateTime widget for ranges
                                type       : 'datetime',

                                // Sync label width with other fields
                                labelWidth : '12em'
                            },
                            rangeEndField : {
                                type       : 'datetime',
                                labelWidth : '12em'
                            },
                            // Add a filler widget that would add a margin at the bottom
                            filler : {
                                height : '0.6em',
                                weight : 900
                            }
                        }
                    }
                }
            }
        }
    }
});

```

Configuring default columns
---------------------------

By default all visible columns are selected in the export dialog. This is managed by [autoSelectVisibleColumns](https://bryntum.com/docs/gantt/api/#Scheduler/view/export/SchedulerExportDialog#config-autoSelectVisibleColumns) config. To change default selected columns you should disable this config and set field value. Value should be an array of valid column ids (or column instances). This way you can preselect hidden columns:

```
const scheduler = new Scheduler({
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
scheduler.features.pdfExport.showExportDialog();
```

Adding fields
-------------

You can add your own fields to the export dialog. To make such field value acessible to the feature it should follow naming pattern - it should have `ref` config ending with `Field`, see other fields for reference - `orientationField`, `columnsField`, etc. Fields not matching this pattern are ignored. When values are collected from the dialog, `Field` part of the widget reference is removed, so `orientationField` becomes `orientation`, `fooField` becomes `foo`, etc.

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
const scheduler = new Scheduler({
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
scheduler.features.pdfExport.exportDialog.on({
    beforeShow() {
        this.widgetMap.columnsField.value = ['age', 'city']
    }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerExportDialog](https://bryntum.com/docs/gantt/api/Scheduler/view/export/SchedulerExportDialog#property-isSchedulerExportDialog)
Identifies an object as an instance of [SchedulerExportDialog](https://bryntum.com/docs/gantt/api/#Scheduler/view/export/SchedulerExportDialog) class, or subclass thereof.

[isSchedulerExportDialog](https://bryntum.com/docs/gantt/api/Scheduler/view/export/SchedulerExportDialog#property-isSchedulerExportDialog-static)
Identifies an object as an instance of [SchedulerExportDialog](https://bryntum.com/docs/gantt/api/#Scheduler/view/export/SchedulerExportDialog) class, or subclass thereof.
