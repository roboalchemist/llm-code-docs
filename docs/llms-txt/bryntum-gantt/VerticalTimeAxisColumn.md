# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/column/VerticalTimeAxisColumn.md

# [VerticalTimeAxisColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/VerticalTimeAxisColumn)

A special column containing the time axis labels when the Scheduler is used in vertical mode. You can configure, it using the [verticalTimeAxisColumn](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-verticalTimeAxisColumn) config object.

**Note**: this column is sized by flexing to consume full width of its containing [SubGrid](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid). To change width of this column, instead size the subgrid like so:

```
const scheduler = new Scheduler({
    mode           : 'vertical',
    subGridConfigs : {
        locked : {
            width : 300
        }
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[minWidth](https://bryntum.com/docs/gantt/api/Scheduler/column/VerticalTimeAxisColumn#config-minWidth)
Column minimal width. If value is Number then minimal width is in pixels

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isVerticalTimeAxisColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/VerticalTimeAxisColumn#property-isVerticalTimeAxisColumn)
Identifies an object as an instance of [VerticalTimeAxisColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/VerticalTimeAxisColumn) class, or subclass thereof.

[isVerticalTimeAxisColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/VerticalTimeAxisColumn#property-isVerticalTimeAxisColumn-static)
Identifies an object as an instance of [VerticalTimeAxisColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/VerticalTimeAxisColumn) class, or subclass thereof.

[minWidth](https://bryntum.com/docs/gantt/api/Scheduler/column/VerticalTimeAxisColumn#property-minWidth)
Column minimal width. If value is Number then minimal width is in pixels
