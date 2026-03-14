# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/PercentDoneColumn.md

# [PercentDoneColumn](https://bryntum.com/docs/gantt/api/Gantt/column/PercentDoneColumn)

A column representing the [percentDone](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-percentDone) field of the task.

Styling
-------

Cells in this column get a `b-percent-done-cell` class added.

If [mode](https://bryntum.com/docs/gantt/api/#Gantt/column/PercentDoneColumn#config-mode) is set to `circle`, the resulting progress circle element in the cell gets a few special CSS classes added:

* If value equals 0, a `b-empty` CSS class is added to the circle element.
* If value equals 100, a `b-full` CSS class is added to the circle element.
* If value is > 100, a `b-over` CSS class is added to the circle element.

Default editor is a [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPercentDoneColumn](https://bryntum.com/docs/gantt/api/Gantt/column/PercentDoneColumn#property-isPercentDoneColumn)
Identifies an object as an instance of [PercentDoneColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/PercentDoneColumn) class, or subclass thereof.

[isPercentDoneColumn](https://bryntum.com/docs/gantt/api/Gantt/column/PercentDoneColumn#property-isPercentDoneColumn-static)
Identifies an object as an instance of [PercentDoneColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/PercentDoneColumn) class, or subclass thereof.
