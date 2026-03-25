# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/view/mixin/GanttStores.md

# [GanttStores](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores)

Functions for store assignment and store event listeners. Properties are aliases to corresponding ones of Gantt's [project](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel) instance.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[tasks](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#config-tasks)
Inline tasks, will be loaded into an internally created TaskStore.

[taskStore](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#config-taskStore)
The [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore) holding the tasks to be rendered into the Gantt.

[resources](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#config-resources)
Inline resources, will be loaded into the backing project's ResourceStore.

[assignments](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#config-assignments)
Inline assignments, will be loaded into the backing project's AssignmentStore.

[dependencies](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#config-dependencies)
Inline dependencies, will be loaded into the backing project's DependencyStore.

[timeRanges](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#config-timeRanges)
Inline time ranges, will be loaded into the backing project's time range store.

[calendars](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#config-calendars)
Inline calendars, will be loaded into the backing project's CalendarManagerStore.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGanttStores](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-isGanttStores)
Identifies an object as an instance of [GanttStores](https://bryntum.com/docs/gantt/api/#Gantt/view/mixin/GanttStores) class, or subclass thereof.

[isGanttStores](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-isGanttStores-static)
Identifies an object as an instance of [GanttStores](https://bryntum.com/docs/gantt/api/#Gantt/view/mixin/GanttStores) class, or subclass thereof.

[resources](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-resources)
Get/set resources, applies to the backing project's ResourceStore.

[assignments](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-assignments)
Get/set assignments, applies to the backing project's AssignmentStore.

[dependencies](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-dependencies)
Get/set dependencies, applies to the backing projects DependencyStore.

[timeRanges](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-timeRanges)
Get/set time ranges, applies to the backing project's TimeRangeStore.

[calendars](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-calendars)
Get/set calendars, applies to the backing projects CalendarManagerStore.

[tasks](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-tasks)
Get/set tasks, applies to the backing project's EventStore. Returns a flat array of all tasks in the task store.

[calendarManagerStore](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-calendarManagerStore)
The [CalendarManagerStore](https://bryntum.com/docs/gantt/api/#Gantt/data/CalendarManagerStore) instance of the backing project.

[taskStore](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#property-taskStore)
Get/set the task store instance of the backing project.

## Functions

Functions are methods available for calling on the class

[onEventStoreBatchedUpdate](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttStores#function-onEventStoreBatchedUpdate)
Listener to the batchedUpdate event which fires when a field is changed on a record which is batch updating. Occasionally UIs must keep in sync with batched changes. For example, the TaskResize feature performs batched updating of the startDate/endDate and it tells its client to listen to batchedUpdate.
