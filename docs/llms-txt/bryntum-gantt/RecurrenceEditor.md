# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/recurrence/RecurrenceEditor.md

# [RecurrenceEditor](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceEditor)

A class implementing a dialog to edit a [RecurrenceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel). The class is used by the [RecurringEvents](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/RecurringEvents) feature, and you normally don't need to instantiate it.

Before showing the dialog, you need to use [record](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-record) to load a [recurrence model](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel) data into the editor fields. For example:

```
// make the editor instance
const editor = new RecurrenceEditor();
// load recurrence model into it
editor.record = new RecurrenceModel({ frequency : "WEEKLY" });
// display the editor
editor.show();
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRecurrenceEditor](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceEditor#property-isRecurrenceEditor)
Identifies an object as an instance of [RecurrenceEditor](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceEditor) class, or subclass thereof.

[isRecurrenceEditor](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceEditor#property-isRecurrenceEditor-static)
Identifies an object as an instance of [RecurrenceEditor](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceEditor) class, or subclass thereof.
