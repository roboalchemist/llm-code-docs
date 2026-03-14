# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/mixin/PercentDoneMixin.md

# [PercentDoneMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/PercentDoneMixin)

PercentDone mixin to get the current status of a task.

## Fields

Fields belong to a Model class and define the Model data structure

[percentDone](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/PercentDoneMixin#field-percentDone)
The current status of a task, expressed as the percentage completed (integer from 0 to 100)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPercentDoneMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/PercentDoneMixin#property-isPercentDoneMixin)
Identifies an object as an instance of [PercentDoneMixin](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/PercentDoneMixin) class, or subclass thereof.

[isPercentDoneMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/PercentDoneMixin#property-isPercentDoneMixin-static)
Identifies an object as an instance of [PercentDoneMixin](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/PercentDoneMixin) class, or subclass thereof.

[isStarted](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/PercentDoneMixin#property-isStarted)
Indicates if the task is started (its [percent completion](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/PercentDoneMixin#field-percentDone) is greater than zero).

[isCompleted](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/PercentDoneMixin#property-isCompleted)
Indicates if the task is complete (its [percent completion](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/PercentDoneMixin#field-percentDone) is 100% (or greater)).

[isInProgress](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/PercentDoneMixin#property-isInProgress)
Indicates if the task is in progress (its [percent completion](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/PercentDoneMixin#field-percentDone) is greater than zero and less than 100%).

[renderedPercentDone](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/PercentDoneMixin#property-renderedPercentDone)
Human-friendly rounding. When task is completed < 99%, it rounds the value. It floors value between 99 and 100, to not show task as completed when it is for example 99.51% done.
