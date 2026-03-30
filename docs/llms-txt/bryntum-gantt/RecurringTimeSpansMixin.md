# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/RecurringTimeSpansMixin.md

# [RecurringTimeSpansMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin)

This mixin provides recurrence functionality to a store containing [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) models. Normally you don't need to interact with this mixin directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoAdjustRecurrence](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin#config-autoAdjustRecurrence)
When a recurring event _base_ is rescheduled, the new start date may not conform with the recurrence pattern if for example certain weekdays are selected, such as to repeat every Monday.

By default, changing the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-startDate) to a date that is _not_ visited by the recurrence pattern does not recalculate that pattern. It merely changes the date at which that pattern begins.

So if an event is explicitly configured to repeat every Monday (The [recurrenceRule](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-recurrenceRule) contains `BYDAY=MO`) and the base event is changed by any means to have its [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-startDate) on the following Tuesday, visually, the effect would be that the base event "disappears" and the following occurrences _do not move_.

The recurrence pattern still repeats every Monday. It's just that that pattern is calculated starting from a different date.

To have a rescheduling change to a recurring event _base_ recalculate the recurrence pattern to conform to the new start date - to include that date in the pattern - configure `autoAdjustRecurrence` as `true`

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRecurringTimeSpansMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin#property-isRecurringTimeSpansMixin)
Identifies an object as an instance of [RecurringTimeSpansMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/RecurringTimeSpansMixin) class, or subclass thereof.

[isRecurringTimeSpansMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin#property-isRecurringTimeSpansMixin-static)
Identifies an object as an instance of [RecurringTimeSpansMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/RecurringTimeSpansMixin) class, or subclass thereof.

[autoAdjustRecurrence](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin#property-autoAdjustRecurrence)
When a recurring event _base_ is rescheduled, the new start date may not conform with the recurrence pattern if for example certain weekdays are selected, such as to repeat every Monday.

By default, changing the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-startDate) to a date that is _not_ visited by the recurrence pattern does not recalculate that pattern. It merely changes the date at which that pattern begins.

So if an event is explicitly configured to repeat every Monday (The [recurrenceRule](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-recurrenceRule) contains `BYDAY=MO`) and the base event is changed by any means to have its [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-startDate) on the following Tuesday, visually, the effect would be that the base event "disappears" and the following occurrences _do not move_.

The recurrence pattern still repeats every Monday. It's just that that pattern is calculated starting from a different date.

To have a rescheduling change to a recurring event _base_ recalculate the recurrence pattern to conform to the new start date - to include that date in the pattern - configure `autoAdjustRecurrence` as `true`

## Functions

Functions are methods available for calling on the class

[onDataChange](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin#function-onDataChange)
Responds to mutations of the underlying storage Collection.

Maintain indices for fast finding of events by date.

[isRecurrenceRelatedFieldChange](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin#function-isRecurrenceRelatedFieldChange)
The method restricts which field modifications should trigger timespan occurrences building. By default, any field change of a recurring timespan causes the rebuilding.

[getOccurrencesForTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin#function-getOccurrencesForTimeSpan)
Builds occurrences for the provided timespan across the provided date range.

[getRecurringTimeSpans](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/RecurringTimeSpansMixin#function-getRecurringTimeSpans)
Returns all the recurring timespans.
