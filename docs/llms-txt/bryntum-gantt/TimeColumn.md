# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/TimeColumn.md

# [TimeColumn](https://bryntum.com/docs/gantt/api/Grid/column/TimeColumn)

A column that displays a time in the specified format (see [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for formatting options).

Default editor is a [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField).

```
new Grid({
    appendTo : document.body,

    columns : [
         { type: 'time', text: 'Start time', format: 'HH:mm:ss', field : 'start' }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[format](https://bryntum.com/docs/gantt/api/Grid/column/TimeColumn#config-format)
Time format for time displayed in cell and editor (see [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for formatting options)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeColumn](https://bryntum.com/docs/gantt/api/Grid/column/TimeColumn#property-isTimeColumn)
Identifies an object as an instance of [TimeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TimeColumn) class, or subclass thereof.

[isTimeColumn](https://bryntum.com/docs/gantt/api/Grid/column/TimeColumn#property-isTimeColumn-static)
Identifies an object as an instance of [TimeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TimeColumn) class, or subclass thereof.

[format](https://bryntum.com/docs/gantt/api/Grid/column/TimeColumn#property-format)
Time format for time displayed in cell and editor (see [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for formatting options)

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/TimeColumn#function-defaultRenderer)
Renderer that displays the time with the specified format. Also adds cls 'b-time-cell' to the cell.

[groupRenderer](https://bryntum.com/docs/gantt/api/Grid/column/TimeColumn#function-groupRenderer)
Group renderer that displays the time with the specified format.

[formatValue](https://bryntum.com/docs/gantt/api/Grid/column/TimeColumn#function-formatValue)
Used by both renderer and groupRenderer to do the actual formatting of the time
