# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/AttachToProjectMixin.md

# [AttachToProjectMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin)

Mixin that calls the target class `attachToProject()` function when a new project is assigned to Scheduler/Gantt.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAttachToProjectMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin#property-isAttachToProjectMixin)
Identifies an object as an instance of [AttachToProjectMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/AttachToProjectMixin) class, or subclass thereof.

[isAttachToProjectMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin#property-isAttachToProjectMixin-static)
Identifies an object as an instance of [AttachToProjectMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/AttachToProjectMixin) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[attachToProject](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin#function-attachToProject)
Override to take action when the project instance is replaced.

[attachToEventStore](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin#function-attachToEventStore)
Override to take action when the EventStore instance is replaced, either from being replaced on the project or from assigning a new project.

[attachToResourceStore](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin#function-attachToResourceStore)
Override to take action when the ResourceStore instance is replaced, either from being replaced on the project or from assigning a new project.

[attachToAssignmentStore](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin#function-attachToAssignmentStore)
Override to take action when the AssignmentStore instance is replaced, either from being replaced on the project or from assigning a new project.

[attachToDependencyStore](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin#function-attachToDependencyStore)
Override to take action when the DependencyStore instance is replaced, either from being replaced on the project or from assigning a new project.

[attachToCalendarManagerStore](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AttachToProjectMixin#function-attachToCalendarManagerStore)
Override to take action when the CalendarManagerStore instance is replaced, either from being replaced on the project or from assigning a new project.
