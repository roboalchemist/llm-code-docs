# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/Baselines.md

# [Baselines](https://bryntum.com/docs/gantt/api/Gantt/feature/Baselines)

Displays a [task](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel)'s [baselines](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-baselines) below the tasks in the timeline.

This feature also optionally shows a tooltip when hovering any of the task's baseline elements. The tooltip's content may be customized.

If dates (startDate and endDate) are left out in the baseline data, the task's dates will be applied. If dates are **null**, they will be kept empty and the baseline bar won't be displayed in the UI.

To customize the look of baselines, you can supply `cls` or `style` in the baseline data.

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[renderer](https://bryntum.com/docs/gantt/api/Gantt/feature/Baselines#config-renderer)
An empty function by default, but provided so that you can override it. This function is called each time a task baseline is rendered into the gantt to render the contents of the baseline element.

Returning a string will display it in the baseline bar, it accepts both plain text or HTML. It is also possible to return a DOM config object which will be synced to the baseline bars content.

```
// using plain string
new Gantt({
    features : {
        baselines : {
            renderer : ({ baselineRecord }) => baselineRecord.startDate
        }
    }
});

// using DOM config
new Gantt({
    features : {
        baselines : {
            renderer : ({ baselineRecord }) => {
                return {
                    tag : 'b',
                    html : baselineRecord.startDate
                };
            }
        }
    }
});
```

[template](https://bryntum.com/docs/gantt/api/Gantt/feature/Baselines#config-template)
Template (a function accepting event data and returning a string) used to display info in the tooltip. The template will be called with an object as with fields as detailed below

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isBaselines](https://bryntum.com/docs/gantt/api/Gantt/feature/Baselines#property-isBaselines)
Identifies an object as an instance of [Baselines](https://bryntum.com/docs/gantt/api/#Gantt/feature/Baselines) class, or subclass thereof.

[isBaselines](https://bryntum.com/docs/gantt/api/Gantt/feature/Baselines#property-isBaselines-static)
Identifies an object as an instance of [Baselines](https://bryntum.com/docs/gantt/api/#Gantt/feature/Baselines) class, or subclass thereof.

[renderer](https://bryntum.com/docs/gantt/api/Gantt/feature/Baselines#property-renderer)
An empty function by default, but provided so that you can override it. This function is called each time a task baseline is rendered into the gantt to render the contents of the baseline element.

Returning a string will display it in the baseline bar, it accepts both plain text or HTML. It is also possible to return a DOM config object which will be synced to the baseline bars content.

```
// using plain string
new Gantt({
    features : {
        baselines : {
            renderer : ({ baselineRecord }) => baselineRecord.startDate
        }
    }
});

// using DOM config
new Gantt({
    features : {
        baselines : {
            renderer : ({ baselineRecord }) => {
                return {
                    tag : 'b',
                    html : baselineRecord.startDate
                };
            }
        }
    }
});
```
