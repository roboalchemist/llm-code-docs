# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/ProgressLine.md

# [ProgressLine](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine)

This feature draws project progress line with SVG lines. Requires [PercentBar](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/PercentBar) to be enabled (which by default, it is)

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

```
let gantt = new Gantt({
    features : {
        progressLine : {
           statusDate : new Date(2017, 2, 8)
        }
    }
});
```

Status date can be changed dynamically:

```
gantt.features.progressLine.statusDate = new Date();
```

If status date is not provided, a project's [statusDate](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-statusDate) is used.

If status date is not in the current Gantt time span, progress line will use view start or end coordinates. This behavior can be customized with [drawLineOnlyWhenStatusDateVisible](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProgressLine#config-drawLineOnlyWhenStatusDateVisible) config. Or you can override [shouldDrawProgressLine](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProgressLine#function-shouldDrawProgressLine) method and provide more complex condition.

Progress line is a set of SVG elements drawn between all the tasks.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[statusDate](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#config-statusDate)
A reference date, to track the progress from. If not provided, the project's [status date](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-statusDate) is used.

[drawLineOnlyWhenStatusDateVisible](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#config-drawLineOnlyWhenStatusDateVisible)
Set to `true` to hide progress line, when status date is not in the current time axis.

[parentOffsetY](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#config-parentOffsetY)
Vertical pixel offset for connecting point at parent task containers, to keep lines visually consistent. Adjust this value when the task containers are styled differently from default themes. Negative value moves the connecting point up, positive value moves it down.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProgressLine](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#property-isProgressLine)
Identifies an object as an instance of [ProgressLine](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProgressLine) class, or subclass thereof.

[isProgressLine](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#property-isProgressLine-static)
Identifies an object as an instance of [ProgressLine](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProgressLine) class, or subclass thereof.

[statusDate](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#property-statusDate)
A reference date, to track the progress from. If not provided, the project's [status date](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-statusDate) is used.

[statusDate](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#property-statusDate)
Progress line status date. If not provided, current date is used.

## Functions

Functions are methods available for calling on the class

[onProjectRefresh](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#function-onProjectRefresh)
Redraws the line when the project propagation is done

[shouldDrawProgressLine](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#function-shouldDrawProgressLine)
Returns true if progress line should be drawn

[isStatusLineTask](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#function-isStatusLineTask)
Returns true if task should be connected to the progress line.

[getStatusDateX](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#function-getStatusDateX)
Returns status date horizontal position relative to the foreground canvas

[getRenderData](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#function-getRenderData)
Returns object with status date local coordinate and view x,y coordinates. Used to convert page coordinates to view local.

[draw](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#function-draw)
Renders the progress line.

[updateLineForTask](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#function-updateLineForTask)
Updates progress line segment for one task

[calculateCoordinateForTask](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#function-calculateCoordinateForTask)
This method will calculate point inside task element to be connected with line.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[progressLineDrawn](https://bryntum.com/docs/gantt/api/Gantt/feature/ProgressLine#event-progressLineDrawn)
Fired when progress line is rendered
