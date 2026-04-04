# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/base/GridEditBase.md

# [GridEditBase](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase)

Base for features, which edit the grid.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[continueEditingOnCellClick](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#config-continueEditingOnCellClick)
By default, while editing, clicking on a grid cell outside the editor will commence editing for the clicked cell context.

Set to `false` to stop editing when clicking another cell while editing.

[autoEdit](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#config-autoEdit)
Set to `true` to start editing when user starts typing text on a focused cell (as in Excel)

[triggerEvent](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#config-triggerEvent)
The name of the grid event that will trigger cell editing. Defaults to [celldblclick](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridElementEvents#event-cellDblClick) but can be changed to any other event, such as [cellclick](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridElementEvents#event-cellClick).

```
features : {
    cellEdit : {
        triggerEvent : 'cellclick'
    }
}
```

[ignoreCSSSelector](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#config-ignoreCSSSelector)
A CSS selector for elements that when clicked, should not trigger editing. Useful if you render actionable icons or buttons into a grid cell.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridEditBase](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#property-isGridEditBase)
Identifies an object as an instance of [GridEditBase](https://bryntum.com/docs/gantt/api/#Grid/feature/base/GridEditBase) class, or subclass thereof.

[isGridEditBase](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#property-isGridEditBase-static)
Identifies an object as an instance of [GridEditBase](https://bryntum.com/docs/gantt/api/#Grid/feature/base/GridEditBase) class, or subclass thereof.

[autoEdit](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#property-autoEdit)
Set to `true` to start editing when user starts typing text on a focused cell (as in Excel)

[isEditing](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#property-isEditing)
Is editing currently active?

[activeRecord](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#property-activeRecord)
Returns the record currently being edited, or `null`

## Functions

Functions are methods available for calling on the class

[onCellClickWhileEditing](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#function-onCellClickWhileEditing)
Event handler added when editing is active called when user clicks a cell in the grid during editing. It finishes editing and moves editor to the selected cell instead.

[onCellClick](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#function-onCellClick)
Starts editing if user taps selected cell again on touch device. Chained function called when user clicks a cell.

[onTriggerEditEvent](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#function-onTriggerEditEvent)
Called when the user triggers the edit action in [triggerEvent](https://bryntum.com/docs/gantt/api/#Grid/feature/base/GridEditBase#config-triggerEvent) config. Starts editing.

[onStoreUpdate](https://bryntum.com/docs/gantt/api/Grid/feature/base/GridEditBase#function-onStoreUpdate)
Update the input field if underlying data changes during edit.
