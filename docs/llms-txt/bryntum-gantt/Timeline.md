# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/Timeline.md

# [Timeline](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/Timeline)

A visual component showing an overview timeline of events having the [showInTimeline](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-showInTimeline) field set to `true`. The timeline component subclasses the [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler) and to use it, simply provide it with a [ProjectModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel):

```
const timeline = new Timeline({
    appendTo  : 'container',
    project   : project
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[project](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/Timeline#config-project)
Project config object or a Project instance

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeline](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/Timeline#property-isTimeline)
Identifies an object as an instance of [Timeline](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/Timeline) class, or subclass thereof.

[isTimeline](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/Timeline#property-isTimeline-static)
Identifies an object as an instance of [Timeline](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/Timeline) class, or subclass thereof.
