# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/view/SchedulerPro.md

# [SchedulerPro](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerPro)

Intro
-----

The Scheduler Pro is an extension of the [Bryntum Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler), and combines the visualisation capabilities of the Scheduler with the powerful scheduling engine from the Gantt. This means it can manage [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel) data composed by tasks, dependencies, resources, assignments and calendars (for working / non-working time). If you have inter-task dependencies, task updates will be propagated to any successors after a task is moved. The engine will reschedule tasks according to the constraints, dependencies and calendars defined in the project. To familiarize yourself with the various APIs and data structures of the Scheduler Pro, we recommend starting with these resources:

* [Project data model guide](https://bryntum.com/docs/gantt/api/#SchedulerPro/guides/basics/project_data.md)
* [Bryntum Scheduler API docs](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler)
* [Bryntum Grid API docs](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)
* [Localization](https://bryntum.com/docs/gantt/api/#SchedulerPro/guides/customization/localization.md)

Basic setup
-----------

To create an instance of this class, simply configure it with:

* The [columns](https://bryntum.com/docs/gantt/api/#Grid/column/Column) you want
* The [features](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-features) you want, quite a lot to choose from, and you can build your own too
* A [Project](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel) instance:
* A [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) identifier, specifying the granularity of the time axis.

```
const scheduler = new SchedulerPro({
   // A Project holds the data and the calculation engine for Scheduler Pro. It also acts as a CrudManager, allowing
   // loading data into all stores at once
   project : {
       autoLoad  : true,
       transport : {
           load : {
               url : './data/data.json'
           }
      }
   },

   adopt             : 'container',
   startDate         : '2020-05-01',
   endDate           : '2020-09-30',
   resourceImagePath : '../_shared/images/users/',
   viewPreset        : 'dayAndWeek'
   features : {
      columnLines  : false,
      dependencies : true
  },

  columns : [
      {
          type           : 'resourceInfo',
          text           : 'Worker',
          showEventCount : true
      }
  ]
});
```

Inheriting from Bryntum Grid
----------------------------

Bryntum Scheduler Pro inherits from Bryntum Grid, meaning that most features available in the grid are also available for the scheduler. Common features include columns, cell editing, context menus, row grouping, sorting and more. Note: If you want to use the Grid component standalone, e.g. to use drag-from-grid functionality, you need a separate license for the Grid component.

Customisation
-------------

You can style any aspect of the Scheduler using plain CSS or modify our themes using our built-in SASS variables. Using the [eventRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-eventRenderer) you can customize the HTML output for each event bar. The Scheduler comes with a few different [event styles](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro#config-eventStyle) which you can define globally on the Scheduler, in the resource data, or on individual events.

For more information about styling, please refer to the [styling guide](https://bryntum.com/docs/gantt/api/#SchedulerPro/guides/customization/styling.md).

Partnering with other timeline widgets
--------------------------------------

You can also pair the Scheduler Pro with other timeline based widgets such as the [histogram widget](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram) to view resource allocation levels, using the [partner](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro#config-partner) config.

### Differences between Scheduler and Scheduler Pro

Scheduler Pro extends Scheduler and schedules tasks based on the Project, Resource and Event calendars, while also taking into account dependencies and constraints. Scheduler Pro also comes with more demos showing off advanced use cases. Below is a list of technical differences between the two versions:

* Scheduler uses an EventStore, ResourceStore (optionally an AssignmentStore and a DependencyStore), whereas Scheduler Pro always uses an AssignmentStore to manage event assignments.
* Scheduler Pro uses the same data model as the Gantt and can visualise a Project side by side with the Gantt.
* Scheduler supports showing dependencies but they are just visual elements, they do not impact scheduling. In Scheduler Pro, adding a dependency between two tasks will affect the scheduling of the successor task.
* Scheduler Pro supports visualising a task completion progress bar.
* Scheduler Pro includes a Timeline widget and a Resource Histogram widget.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerPro](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerPro#property-isSchedulerPro)
Identifies an object as an instance of [SchedulerPro](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro) class, or subclass thereof.

[isSchedulerPro](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerPro#property-isSchedulerPro-static)
Identifies an object as an instance of [SchedulerPro](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro) class, or subclass thereof.
