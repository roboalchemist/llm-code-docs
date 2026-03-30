# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineHistogramScaleColumn.md

# [TimelineHistogramScaleColumn](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn)

Mixin of [TimelineHistogram](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogram) class that implements [ScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn) automatic injection and functioning.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[scaleColumn](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#config-scaleColumn)
An object with configuration for the [ScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn).

Example:

```
new TimelineHistogram({
    scaleColumn : {
        width : 50
    },
    ...
});
```

Provide `null` to the config to get rid of the column completely:

```
new TimelineHistogram({
    // do not add scale column
    scaleColumn : null,
    ...
});
```

[scalePoints](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#config-scalePoints)
Array of objects representing the [scale column](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramScaleColumn#config-scaleColumn) scale points. The config basically is a mapping to the column [scalePoints](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn#config-scalePoints) config.

If the config value is not provided the column will try reading it from the displayed record [field](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn#config-field) (`scalePoints` field is expected by default).

```
new TimelineHistogram({
    scalePoints : [
        { text : '8h', value : 8 },
        { text : '16h', value : 16 },
        { text : '24h', value : 24 }
    ]
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineHistogramScaleColumn](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#property-isTimelineHistogramScaleColumn)
Identifies an object as an instance of [TimelineHistogramScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramScaleColumn) class, or subclass thereof.

[isTimelineHistogramScaleColumn](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#property-isTimelineHistogramScaleColumn-static)
Identifies an object as an instance of [TimelineHistogramScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramScaleColumn) class, or subclass thereof.

[scaleColumn](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#property-scaleColumn)
The locked grid scale column reference.

[scalePoints](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#property-scalePoints)
Array of objects representing the [scale column](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramScaleColumn#config-scaleColumn) scale points. The config basically is a mapping to the column [scalePoints](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn#config-scalePoints) config.

If the config value is not provided the column will try reading it from the displayed record [field](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn#config-field) (`scalePoints` field is expected by default).

```
new TimelineHistogram({
    scalePoints : [
        { text : '8h', value : 8 },
        { text : '16h', value : 16 },
        { text : '24h', value : 24 }
    ]
})
```

## Functions

Functions are methods available for calling on the class

[convertUnitsToHistogramValue](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#function-convertUnitsToHistogramValue)
A hook to convert scale point values to histogram ones. In case they use different units.

Override this method in a sub-class to implement your custom application specific conversion.

[convertHistogramValueToUnits](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#function-convertHistogramValueToUnits)
A hook to convert histogram values to scale point ones. In case they use different units.

Override this method in a sub-class to implement your custom application specific conversion.

[buildGroupHeader](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#function-buildGroupHeader)
Group feature hook triggered by the feature to render group headers

[renderRecordScale](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramScaleColumn#function-renderRecordScale)
Renders record scale column content.
