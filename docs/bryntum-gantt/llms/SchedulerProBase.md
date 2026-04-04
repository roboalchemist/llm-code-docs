# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/view/SchedulerProBase.md

# [SchedulerProBase](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase)

A thin base class for [SchedulerPro](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro). Includes fewer features by default, allowing smaller custom-built bundles if used in place of [SchedulerPro](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro).

**NOTE:** In most scenarios you should use SchedulerPro instead of SchedulerProBase.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[dependencyIdField](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-dependencyIdField)
A task field (id, wbsCode, sequenceNumber etc) that will be used when displaying and editing linked tasks.

[showTaskColorPickers](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-showTaskColorPickers)
If set to `true` this will show a color field in the [TaskEdit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TaskEdit) editor and also a picker in the [EventMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventMenu). Both enables the user to choose a color which will be applied to the event bar's background. See EventModel's [eventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-eventColor) config. config.

[project](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-project)
A [ProjectModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel) instance or a config object. The project holds all SchedulerPro data.

[events](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-events)
Inline events, will be loaded into the backing project's EventStore.

[eventStore](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-eventStore)
The [EventStore](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/EventStore) holding the events to be rendered into the scheduler.

[resources](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-resources)
Inline resources, will be loaded into the backing project's ResourceStore.

[resourceStore](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-resourceStore)
The [ResourceStore](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/ResourceStore) holding the resources to be rendered into the scheduler.

[assignments](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-assignments)
Inline assignments, will be loaded into the backing project's AssignmentStore.

[assignmentStore](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-assignmentStore)
The optional [AssignmentStore](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/AssignmentStore), holding assignments between resources and events. Required for multi assignments.

[dependencies](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-dependencies)
Inline dependencies, will be loaded into the backing project's DependencyStore.

[dependencyStore](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-dependencyStore)
The optional [DependencyStore](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/DependencyStore).

[calendars](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#config-calendars)
Inline calendars, will be loaded into the backing project's CalendarManagerStore.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerProBase](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-isSchedulerProBase)
Identifies an object as an instance of [SchedulerProBase](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerProBase) class, or subclass thereof.

[isSchedulerProBase](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-isSchedulerProBase-static)
Identifies an object as an instance of [SchedulerProBase](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerProBase) class, or subclass thereof.

[project](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-project)
Get/set ProjectModel instance, containing the data visualized by the SchedulerPro.

[events](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-events)
Get/set events, applies to the backing project's EventStore.

[eventStore](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-eventStore)
Get/set the event store instance of the backing project.

[resources](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-resources)
Get/set resources, applies to the backing project's ResourceStore.

[resourceStore](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-resourceStore)
Get/set the resource store instance of the backing project

[assignments](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-assignments)
Get/set assignments, applies to the backing project's AssignmentStore.

[assignmentStore](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-assignmentStore)
Get/set the event store instance of the backing project.

[dependencies](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-dependencies)
Get/set dependencies, applies to the backing projects DependencyStore.

[dependencyStore](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-dependencyStore)
Get/set the dependencies store instance of the backing project.

[calendars](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-calendars)
Get/set calendars, applies to the backing projects CalendarManagerStore.

[mode](https://bryntum.com/docs/gantt/api/SchedulerPro/view/SchedulerProBase#property-mode)
Get mode (horizontal/vertical)
