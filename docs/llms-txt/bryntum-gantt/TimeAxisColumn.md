# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/column/TimeAxisColumn.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/TimeAxisColumn.md

# [TimeAxisColumn](https://bryntum.com/docs/gantt/api/Gantt/column/TimeAxisColumn)

A column containing the timeline "viewport", in which tasks, dependencies etc. are drawn. Normally you do not need to interact with or create this column, it is handled by Gantt.

Styling
-------

You can style a timeaxis cell by using the [afterRenderCell](https://bryntum.com/docs/gantt/api/#Gantt/column/TimeAxisColumn#config-afterRenderCell) method.

```
const gantt = new Gantt({
   appendTo : document.body,
   columns : [
       {
           type : 'timeAxis',
           afterRenderCell({ cellElement, record }) {
               cellElement.style.background = 'rgba(255,200,0,0.15)';
           }
       }
   ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[enableCellContextMenu](https://bryntum.com/docs/gantt/api/Gantt/column/TimeAxisColumn#config-enableCellContextMenu)
Set to `false` to disable the [TaskMenu](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskMenu) for the cell elements in this column.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeAxisColumn](https://bryntum.com/docs/gantt/api/Gantt/column/TimeAxisColumn#property-isTimeAxisColumn)
Identifies an object as an instance of [TimeAxisColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/TimeAxisColumn) class, or subclass thereof.

[isTimeAxisColumn](https://bryntum.com/docs/gantt/api/Gantt/column/TimeAxisColumn#property-isTimeAxisColumn-static)
Identifies an object as an instance of [TimeAxisColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/TimeAxisColumn) class, or subclass thereof.

[enableCellContextMenu](https://bryntum.com/docs/gantt/api/Gantt/column/TimeAxisColumn#property-enableCellContextMenu)
Set to `false` to disable the [TaskMenu](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskMenu) for the cell elements in this column.
