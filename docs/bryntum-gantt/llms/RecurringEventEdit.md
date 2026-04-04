# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/mixin/RecurringEventEdit.md

# [RecurringEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/RecurringEventEdit)

This mixin class provides recurring events functionality to the [event editor](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showRecurringUI](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/RecurringEventEdit#config-showRecurringUI)
Set to `false` to hide recurring fields in event editor, even if the [Recurring Events](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/RecurringEvents#config-enableRecurringEvents) is `true` and a recurring event is being edited.

[useContextualRecurrenceRules](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/RecurringEventEdit#config-useContextualRecurrenceRules)
By default, the day of week and week of month of the event's start date are used to create helpful contextual recurrence types when editing a non-recurring event record and choosing an initial recurrence type.

Set this to `false` to disable this and always show unconfigured WEEKLY, MONTHLY and YEARLY options.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRecurringEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/RecurringEventEdit#property-isRecurringEventEdit)
Identifies an object as an instance of [RecurringEventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/RecurringEventEdit) class, or subclass thereof.

[isRecurringEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/RecurringEventEdit#property-isRecurringEventEdit-static)
Identifies an object as an instance of [RecurringEventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/RecurringEventEdit) class, or subclass thereof.

[recurrenceCombo](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/RecurringEventEdit#property-recurrenceCombo)
Reference to the `Repeat` event field, if used

[editRecurrenceButton](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/RecurringEventEdit#property-editRecurrenceButton)
Reference to the button that opens the event repeat settings dialog, if used

[useContextualRecurrenceRules](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/RecurringEventEdit#property-useContextualRecurrenceRules)
By default, the day of week and week of month of the event's start date are used to create helpful contextual recurrence types when editing a non-recurring event record and choosing an initial recurrence type.

Set this to `false` to disable this and always show unconfigured WEEKLY, MONTHLY and YEARLY options.
