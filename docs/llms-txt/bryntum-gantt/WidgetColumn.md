# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/WidgetColumn.md

# [WidgetColumn](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn)

A column that displays one or more [widgets](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) in the grid cells.

When rendered into a cell, all widgets will have a special [cellInfo](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-cellInfo) context property injected into them so that event handlers can ascertain the context in which they are operating.

```
new Grid({
    columns : [{
        type    : 'widget',
        widgets : [{
            type     : 'button',
            menuIcon : false,
            icon     : 'fa fa-ellipsis-v',
            menu     : {
                type  : 'menu',
                items : {
                    viewResponses : {
                        icon : 'fa fa-fw fa-file-signature',
                        text : 'View Responses'
                    },
                    clearConsent : {
                        icon : 'fa fa-fw fa-times-circle',
                        text : 'Clear Consent',
                    },
                    surveyList : {
                        icon : 'fa fa-fw fa-file-signature',
                        text : 'Survey List (Read-Only)'
                    }
                },

                // Method is called for all descendant levels.
                // 'up.' will find it defined on the Grid.
                onItem : 'up.onWidgetColumnMenuClick'
            }
        }
    }],

    onWidgetColumnMenuClick({ source }) {
        // Find the source widget's Button ancestor. It's the cell widget.
        // A WidgetColumn's cell widget gets a cellInfo property injected
        const { cellInfo } = source.up('button');

        console.log(`Clicked ${source.ref} on ${cellInfo.record.name}`);
    }
});
```

Data binding to fields
----------------------

If you use [Fields](https://bryntum.com/docs/gantt/api/#Core/widget/Field) inside this column, the field widget can optionally bind its `value` to a field in the data model using the [name](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-name) (shown in the snippet below). This will provide two-way data binding and update the underlying row record as you make changes in the field.

```
new Grid({
    columns : [{
        type    : 'widget',
        widgets : [{
            type : 'numberfield',
            name : 'percentDone'
        }]
    }]
});
```

If you use a [Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button) and want it to display the value from the cell as its text, set its [defaultBindProperty](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-defaultBindProperty) to `'text'`:

```
new Grid({
    columns : [{
        type    : 'widget',
        widgets : [{
            type                : 'button',
            name                : 'age',
            defaultBindProperty : 'text'
        }]
    }]
});
```

There is no `editor` provided. It is the configured widget's responsibility to provide editing if needed.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[widgets](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#config-widgets)
An array of [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) config objects

[afterRenderCell](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#config-afterRenderCell)
A renderer function, which gives you access to render data like the current `record`, `cellElement` and the [widgets](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn#config-widgets) of the column. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn#config-renderer) for more information.

```
new Grid({
    columns : [
        {
             type: 'check',
             field: 'allow',
             // In the column afterRenderCell callback, we get access to the record and column widgets
             afterRenderCell({ record, widgets }) {
                 // Hide checkboxes in certain rows
                 widgets[0].hidden = record.readOnly;
             }
        }
    ]
});
```

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#config-renderer)
A renderer function, which gives you access to render data like the current `record`, `cellElement` and the [widgets](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn#config-widgets) of the column. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn#config-renderer) for more information.

```
new Grid({
    columns : [
        {
             type: 'check',
             field: 'allow',
             // In the column afterRenderCell callback, we get access to the record and column widgets
             afterRenderCell({ record, widgets }) {
                 // Hide checkboxes in certain rows
                 widgets[0].hidden = record.readOnly;
             }
        }
    ]
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isWidgetColumn](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#property-isWidgetColumn)
Identifies an object as an instance of [WidgetColumn](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn) class, or subclass thereof.

[isWidgetColumn](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#property-isWidgetColumn-static)
Identifies an object as an instance of [WidgetColumn](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn) class, or subclass thereof.

[widgets](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#property-widgets)
An array of [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) config objects

[afterRenderCell](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#property-afterRenderCell)
A renderer function, which gives you access to render data like the current `record`, `cellElement` and the [widgets](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn#config-widgets) of the column. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn#config-renderer) for more information.

```
new Grid({
    columns : [
        {
             type: 'check',
             field: 'allow',
             // In the column afterRenderCell callback, we get access to the record and column widgets
             afterRenderCell({ record, widgets }) {
                 // Hide checkboxes in certain rows
                 widgets[0].hidden = record.readOnly;
             }
        }
    ]
});
```

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#property-renderer)
A renderer function, which gives you access to render data like the current `record`, `cellElement` and the [widgets](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn#config-widgets) of the column. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn#config-renderer) for more information.

```
new Grid({
    columns : [
        {
             type: 'check',
             field: 'allow',
             // In the column afterRenderCell callback, we get access to the record and column widgets
             afterRenderCell({ record, widgets }) {
                 // Hide checkboxes in certain rows
                 widgets[0].hidden = record.readOnly;
             }
        }
    ]
});
```

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#function-defaultRenderer)
Renderer that displays a widget in the cell.

[onBeforeWidgetCreate](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#function-onBeforeWidgetCreate)
Called before widget is created on rendering

[onAfterWidgetCreate](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#function-onAfterWidgetCreate)
Called after widget is created on rendering

[onBeforeWidgetSetValue](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#function-onBeforeWidgetSetValue)
Called before the widget gets its value on rendering. Pass `false` to skip value setting while rendering

[onAfterWidgetSetValue](https://bryntum.com/docs/gantt/api/Grid/column/WidgetColumn#function-onAfterWidgetSetValue)
Called after the widget gets its value on rendering.
