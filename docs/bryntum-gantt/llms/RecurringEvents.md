# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/RecurringEvents.md

# [RecurringEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents)

A mixin that adds functionality related to recurring events to the Scheduler and Calendar widgets.

The main purpose of the code in here is displaying a [special confirmation](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup) when the user interacts with recurring events and their occurrences (via drag-drop/resize/delete etc.). See this in action in the `recurrence` demo found in Calendar and Scheduler.

Recurring event data structure
------------------------------

Recurring timespans can have a [recurrenceRule](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-recurrenceRule) specified defining the repetition pattern (based on the [RFC-5545](https://bryntum.com/docs/gantt/api/https://tools.ietf.org/html/rfc5545#section-3.3.10). You can also provide [exceptionDates](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-exceptionDates) to the data to exclude certain dates. See sample data below for an event record which repeats weekly on Tuesdays and Thursdays at 12pm-1pm (except March 28, 2024).

```
{
    id: 7,
    startDate: '2021-10-12T12:00:00',
    endDate: '2021-10-12T13:00:00',
    name: 'Lunch',
    resourceId: 123,
    recurrenceRule: 'FREQ=WEEKLY;BYDAY=TU,TH',
    exceptionDates: ['2024-03-28']
}
```

To enable this functionality in the Scheduler, set [enableRecurringEvents](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/RecurringEvents#config-enableRecurringEvents) to `true`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[enableRecurringEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#config-enableRecurringEvents)
Enables showing occurrences of recurring events across the scheduler's time axis. If you want to disable the recurrence popup, you can choose set the `defaultAction` to `future` to affect all future occurrences, or `single` to just affect the currently selected event.

Enables extra recurrence UI fields in the system-provided event editor (not in Scheduler Pro's task editor).

[recurrenceConfirmationPopup](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#config-recurrenceConfirmationPopup)
The confirmation dialog shown when a recurring event is edited.

The user is given the opportunity to either change just the occurrence being edited, or all occurrences from that point onwards.

The {Scheduler.view.recurrence.RecurrenceConfirmationPopup} may be reconfigured from its default configuration by specifying a config object here.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRecurringEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#property-isRecurringEvents)
Identifies an object as an instance of [RecurringEvents](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/RecurringEvents) class, or subclass thereof.

[isRecurringEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#property-isRecurringEvents-static)
Identifies an object as an instance of [RecurringEvents](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/RecurringEvents) class, or subclass thereof.

[recurrenceConfirmationPopup](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#property-recurrenceConfirmationPopup)
The confirmation dialog shown when a recurring event is edited.

The user is given the opportunity to either change just the occurrence being edited, or all occurrences from that point onwards.

The {Scheduler.view.recurrence.RecurrenceConfirmationPopup} may be reconfigured from its default configuration by specifying a config object here.

## Functions

Functions are methods available for calling on the class

[getOccurrencesFor](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#function-getOccurrencesFor)
Returns occurrences of the provided recurring event across the date range of this Scheduler.

[removeEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#function-removeEvents)
Internal utility function to remove events. Used when pressing \[DELETE\] or \[BACKSPACE\] or when clicking the delete button in the event editor. Triggers a preventable `beforeEventDelete` or `beforeAssignmentDelete` event.

This function is asynchronous because it potentially has to show a [RecurrenceConfirmationPopup](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup) which prompts the user to confirm the operation.

In these cases, the Promise is resolved when the user clicks the desired outcome.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeAssignmentDelete](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#event-beforeAssignmentDelete)
Fires before an assignment is removed. Can be triggered by user pressing \[DELETE\] or \[BACKSPACE\] or by the event editor. Can for example be used to display a custom dialog to confirm deletion, in which case records should be "manually" removed after confirmation:

```
scheduler.on({
    async beforeAssignmentDelete({
        assignmentRecords,
        context
    }) {
        const result = await MessageDialog.confirm({
            title   : 'Please confirm',
            message : 'Do you want to delete this assignment?'
        });
        context.finalize(result === MessageDialog.yesButton);
        // Prevent default behaviour
        return false;
    }
});
```

[beforeEventDelete](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/RecurringEvents#event-beforeEventDelete)
Fires before an event is removed. Can be triggered by user pressing \[DELETE\] or \[BACKSPACE\] or by the event editor. Return `false` to immediately veto the removal (or a `Promise` yielding `true` or `false` for async vetoing).

Can for example be used to display a custom dialog to confirm deletion, in which case records should be "manually" removed after confirmation:

```
scheduler.on({
    async beforeEventDelete({
        eventRecords,
        context
    }) {
        const result = await MessageDialog.confirm({
            title   : 'Please confirm',
            message : 'Do you want to delete this task?'
        });
        context.finalize(result === MessageDialog.yesButton);
        // Prevent default behaviour
        return false;
    }
});
```
