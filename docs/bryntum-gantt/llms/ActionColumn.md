# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/ActionColumn.md

# [ActionColumn](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn)

A column that displays actions as clickable icons in the cell.

```
new TreeGrid({
    appendTo : document.body,
    columns  : [{
        type    : 'action',
        text    : 'Increase amount',
        actions : [{
            cls      : 'fa fa-plus',
            renderer : ({ action, record }) => `<i class="b-action-item ${action.cls} b-${record.enabled ? "green" : "red"}-class"></i>`,
            visible  : ({ record }) => record.canAdd,
            tooltip  : ({ record }) => `<p class="b-nicer-than-default">Add to ${record.name}</p>`,
            onClick  : ({ record }) => console.log(`Adding ${record.name}`)
        }, {
            cls     : 'fa fa-pencil',
            tooltip : 'Edit note',
            onClick : ({ record }) => console.log(`Editing ${record.name}`)
        }]
    }]
});
```

Actions may be placed in [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) headers, by setting `action.showForGroup` to `true`. Those actions will not be shown on normal rows.

Accessibility
-------------

If `ariaLabel` is omitted, adding a `tooltip` to an action will automatically set this as the `aria-label` for the button element. Use `ariaHasPopup` to indicate that the action triggers a popup, helping assistive technology users understand the interaction behavior.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[actions](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#config-actions)
An array of action config objects, see [ActionConfig](https://bryntum.com/docs/gantt/api/#Grid/column/ActionColumn#typedef-ActionConfig) for details.

```
new Grid({
    columns  : [{
        type    : 'action',
        text    : 'Actions',
        actions : [{
            cls      : 'fa fa-plus',
            visible  : ({ record }) => record.canAdd,
            onClick  : ({ record }) => console.log(`Adding ${record.name}`)
        }, {
            cls     : 'fa fa-pencil',
            tooltip : 'Edit note',
            onClick : ({ record }) => console.log(`Editing ${record.name}`)
        }]
    }]
});
```

[disableIfGridReadOnly](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#config-disableIfGridReadOnly)
Set to `true` to disable actions in this column if the grid is [readOnly](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-readOnly)

[minWidth](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#config-minWidth)
Column minimal width. If value is Number then minimal width is in pixels.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isActionColumn](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#property-isActionColumn)
Identifies an object as an instance of [ActionColumn](https://bryntum.com/docs/gantt/api/#Grid/column/ActionColumn) class, or subclass thereof.

[isActionColumn](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#property-isActionColumn-static)
Identifies an object as an instance of [ActionColumn](https://bryntum.com/docs/gantt/api/#Grid/column/ActionColumn) class, or subclass thereof.

[actions](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#property-actions)
An array of action config objects, see [ActionConfig](https://bryntum.com/docs/gantt/api/#Grid/column/ActionColumn#typedef-ActionConfig) for details.

```
new Grid({
    columns  : [{
        type    : 'action',
        text    : 'Actions',
        actions : [{
            cls      : 'fa fa-plus',
            visible  : ({ record }) => record.canAdd,
            onClick  : ({ record }) => console.log(`Adding ${record.name}`)
        }, {
            cls     : 'fa fa-pencil',
            tooltip : 'Edit note',
            onClick : ({ record }) => console.log(`Editing ${record.name}`)
        }]
    }]
});
```

[disableIfGridReadOnly](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#property-disableIfGridReadOnly)
Set to `true` to disable actions in this column if the grid is [readOnly](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-readOnly)

[minWidth](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#property-minWidth)
Column minimal width. If value is Number then minimal width is in pixels.

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#function-defaultRenderer)
Renderer that displays action icon(s) in the cell.

[onCellClick](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#function-onCellClick)
Handle icon click and call action handler.

[updateAutoWidth](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#function-updateAutoWidth)
Update width for actions column to fit content.

## Typedefs

Typedefs are type definitions for the class

[ActionConfig](https://bryntum.com/docs/gantt/api/Grid/column/ActionColumn#typedef-ActionConfig)
Config object for an action in an ActionColumn.
