# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/ColumnLines.md

# [ColumnLines](https://bryntum.com/docs/gantt/api/Scheduler/feature/ColumnLines)

Displays column lines for ticks, with a different styling for major ticks (by default they are darker). If this feature is disabled, no lines are shown. If it's enabled, line are shown for the tick level which is set in current ViewPreset. Please see [columnLinesFor](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-columnLinesFor) config for details.

The lines are drawn as divs, with only visible lines available in DOM. The color and style of the lines are determined by the CSS rules for `.b-column-line` and `.b-column-line-major`.

For vertical mode, this features also draws vertical resource column lines if scheduler is configured with `columnLines : true` (which is the default, see [columnLines](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-columnLines)).

This feature is **enabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[renderer](https://bryntum.com/docs/gantt/api/Scheduler/feature/ColumnLines#config-renderer)
A renderer function, or name of a function in the ownership hierarchy, called for each line, letting you mutate the DOM element through the passed [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object.

```
scheduler = new Scheduler({
    width     : 1000,
    startDate : '2025-01-03',
    endDate   : '2025-01-09',
    features  : {
        columnLines : {
            renderer(date, domConfig) {
                // Make Sunday line red
                if (date.getDay() === 0) {
                    domConfig.style.borderColor = 'red';
                    domConfig.className.foo = 1;
                }
            }
        }
    }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColumnLines](https://bryntum.com/docs/gantt/api/Scheduler/feature/ColumnLines#property-isColumnLines)
Identifies an object as an instance of [ColumnLines](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ColumnLines) class, or subclass thereof.

[isColumnLines](https://bryntum.com/docs/gantt/api/Scheduler/feature/ColumnLines#property-isColumnLines-static)
Identifies an object as an instance of [ColumnLines](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ColumnLines) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[render](https://bryntum.com/docs/gantt/api/Scheduler/feature/ColumnLines#function-render)
Draw lines when scheduler/gantt is rendered.

[refresh](https://bryntum.com/docs/gantt/api/Scheduler/feature/ColumnLines#function-refresh)
Draw column lines that are in view
