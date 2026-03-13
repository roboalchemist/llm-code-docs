# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskTooltip.md

# [TaskTooltip](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskTooltip)

This feature displays a task tooltip on mouse hover. The template of the tooltip is customizable with the [template](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskTooltip#config-template) function.

Showing custom HTML in the tooltip
----------------------------------

```
new Gantt({
    features : {
        taskTooltip : {
            template : ({ taskRecord }) => `Tooltip for ${taskRecord.name}`,
            // Tooltip configs can be used here
            align    : 'l-r' // Align left to right
        }
    }
});
```

Showing remotely loaded data
----------------------------

Loading remote data into the task tooltip is easy. Simply use the [template](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskTooltip#config-template) and return a Promise which yields the content to show.

```
new Gantt({
    features : {
        taskTooltip : {
            template : ({ taskRecord }) => AjaxHelper.get(`./fakeServer?name=${taskRecord.name}`).then(response => response.text())
        }
    }
});
```

This feature is **enabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[template](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskTooltip#config-template)
Template (a function accepting task data and returning a string) used to display info in the tooltip. The template will be called with an object as with fields as detailed below

[decimalPrecision](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskTooltip#config-decimalPrecision)
Precision of displayed duration, defaults to use [durationDisplayPrecision](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-durationDisplayPrecision). Specify an integer value to override that setting, or `false` to use raw value

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskTooltip](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskTooltip#property-isTaskTooltip)
Identifies an object as an instance of [TaskTooltip](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskTooltip) class, or subclass thereof.

[isTaskTooltip](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskTooltip#property-isTaskTooltip-static)
Identifies an object as an instance of [TaskTooltip](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskTooltip) class, or subclass thereof.

[decimalPrecision](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskTooltip#property-decimalPrecision)
Precision of displayed duration, defaults to use [durationDisplayPrecision](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-durationDisplayPrecision). Specify an integer value to override that setting, or `false` to use raw value
