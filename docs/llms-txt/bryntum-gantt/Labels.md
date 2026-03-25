# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/Labels.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/Labels.md

# [Labels](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels)

A feature that lets you display a label on each side of a Gantt task bar. See [Labels](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Labels) for more information.

```
new Gantt({
   features : {
       labels : {
           // Label rendered before the task bar with content from the record's `name` field
           before : {
               field  : 'name',
               editor : {
                   type : 'textfield'
               }
           },
           // Label rendered below the task bar with custom content
           // from a renderer
           bottom : {
               renderer : ({ taskRecord }) => `ID: ${taskRecord.id}`
           }
       }
   }
});
```

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[top](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#config-top)
Top label configuration object.

[after](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#config-after)
Configuration object for the label which appears _after_ the task bar in the current writing direction.

[right](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#config-right)
Right label configuration object.

[bottom](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#config-bottom)
Bottom label configuration object.

[before](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#config-before)
Configuration object for the label which appears _before_ the task bar in the current writing direction.

[left](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#config-left)
Left label configuration object.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isLabels](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#property-isLabels)
Identifies an object as an instance of [Labels](https://bryntum.com/docs/gantt/api/#Gantt/feature/Labels) class, or subclass thereof.

[isLabels](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#property-isLabels-static)
Identifies an object as an instance of [Labels](https://bryntum.com/docs/gantt/api/#Gantt/feature/Labels) class, or subclass thereof.

## Typedefs

Typedefs are type definitions for the class

[GanttLabelConfig](https://bryntum.com/docs/gantt/api/Gantt/feature/Labels#typedef-GanttLabelConfig)
Configuration object for a label used by the Labels feature.
