# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/column/ScaleColumn.md

# [ScaleColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/ScaleColumn)

A specialized column showing a graduated scale from a defined array of values and labels. This column is used in the [TimelineHistogram](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogram) and is not editable. Normally you should not need to interact with this class directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[scalePoints](https://bryntum.com/docs/gantt/api/Scheduler/column/ScaleColumn#config-scalePoints)
Array of objects representing scale points. If not provided the column will try reading points from the displayed record [field](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn#config-field) (`scalePoints` field by default).

```
new TimelineHistogram({
    columns : {
        type        : 'scale',
        scalePoints : [
            { text : '8h', value : 8 },
            { text : '16h', value : 16 },
            { text : '24h', value : 24 }
        ]
    }
})
```

[field](https://bryntum.com/docs/gantt/api/Scheduler/column/ScaleColumn#config-field)
The [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-name) of the [data model](https://bryntum.com/docs/gantt/api/#Core/data/Model) field to read scale point values from.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isScaleColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/ScaleColumn#property-isScaleColumn)
Identifies an object as an instance of [ScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn) class, or subclass thereof.

[isScaleColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/ScaleColumn#property-isScaleColumn-static)
Identifies an object as an instance of [ScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn) class, or subclass thereof.

[scalePoints](https://bryntum.com/docs/gantt/api/Scheduler/column/ScaleColumn#property-scalePoints)
Array of objects representing scale points. If not provided the column will try reading points from the displayed record [field](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn#config-field) (`scalePoints` field by default).

```
new TimelineHistogram({
    columns : {
        type        : 'scale',
        scalePoints : [
            { text : '8h', value : 8 },
            { text : '16h', value : 16 },
            { text : '24h', value : 24 }
        ]
    }
})
```

[field](https://bryntum.com/docs/gantt/api/Scheduler/column/ScaleColumn#property-field)
The [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-name) of the [data model](https://bryntum.com/docs/gantt/api/#Core/data/Model) field to read scale point values from.

## Typedefs

Typedefs are type definitions for the class

[ScalePoint](https://bryntum.com/docs/gantt/api/Scheduler/column/ScaleColumn#typedef-ScalePoint)
An object representing a point on the scale displayed by [ScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn).
