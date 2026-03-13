# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/SchedulerDom.md

# [SchedulerDom](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom)

Mixin with EventModel and ResourceModel <-> HTMLElement mapping functions

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerDom](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#property-isSchedulerDom)
Identifies an object as an instance of [SchedulerDom](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerDom) class, or subclass thereof.

[isSchedulerDom](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#property-isSchedulerDom-static)
Identifies an object as an instance of [SchedulerDom](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerDom) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getElementFromAssignmentRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#function-getElementFromAssignmentRecord)
Returns a single HTMLElement representing an event record assigned to a specific resource.

[getElementFromEventRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#function-getElementFromEventRecord)
Returns a single HTMLElement representing an event record assigned to a specific resource.

[getElementsFromEventRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#function-getElementsFromEventRecord)
Returns all the HTMLElements representing an event record.

[resolveResourceRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#function-resolveResourceRecord)
Resolves the resource based on a dom element or event. In vertical mode, if resolving from an element higher up in the hierarchy than event elements, then it is required to supply coordinates since resources are virtual columns.

[resolveRowRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#function-resolveRowRecord)
Product agnostic method which yields the [ResourceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel) record which underpins the row which encapsulates the passed element. The element can be a grid cell, or an event element, and the result will be a [ResourceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel)

[resolveEventRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#function-resolveEventRecord)
Returns the event record for a DOM element

[resolveAssignmentRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDom#function-resolveAssignmentRecord)
Returns an assignment record for a DOM element
