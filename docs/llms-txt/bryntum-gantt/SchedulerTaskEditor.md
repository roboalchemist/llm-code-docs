# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/SchedulerTaskEditor.md

# [SchedulerTaskEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/SchedulerTaskEditor)

[TaskEditorBase](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/TaskEditorBase) subclass for SchedulerPro projects. Provides a UI to edit tasks in a dialog.

This demo shows how to use TaskEditor as a standalone widget:

Task editor customization
-------------------------

To append Widgets to any of the built-in tabs, use the `items` config. The Task editor contains tabs by default. Each tab contains built-in widgets: text fields, grids, etc.

Tab ref

Text

Weight

Description

`generalTab`

[SchedulerGeneralTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/SchedulerGeneralTab)

100

Shows basic configuration: name, resources, start/end dates, duration, percent done

`recurrenceTab`

[RecurrenceTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/RecurrenceTab)

150

Options for recurring events, when Scheduler is configured to use them

`predecessorsTab`

[PredecessorsTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/PredecessorsTab)

200

Shows a grid with incoming dependencies

`successorsTab`

[SuccessorsTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/SuccessorsTab)

300

Shows a grid with outgoing dependencies

`advancedTab`

[SchedulerAdvancedTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/SchedulerAdvancedTab)

500

Shows advanced configuration: constraints and manual scheduling mode

`notesTab`

[NotesTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/NotesTab)

600

Shows a text area to add notes to the selected task

This demo shows adding of custom widgets to the task editor, double-click child task bar to start editing:

Custom fields in the Event Editor work only if the field is explicitly defined in the Task model. When defined, the field can be added, updated, and stored in the `EventStore`, even if it is not present in the initial task data. Bryntum extracts fields only from the first event record when no definitions are provided, which can lead to inconsistent behavior. Always define custom fields in the Event model to ensure predictable and reliable functionality.

```
export default class CustomEventModel extends EventModel {
 static fields = [
     { name: 'custom', type: 'string' } // Custom field for storing address ID
 ];
}

const project = new ProjectModel({
 eventModelClass : CustomEventModel,
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerTaskEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/SchedulerTaskEditor#property-isSchedulerTaskEditor)
Identifies an object as an instance of [SchedulerTaskEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) class, or subclass thereof.

[isSchedulerTaskEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/SchedulerTaskEditor#property-isSchedulerTaskEditor-static)
Identifies an object as an instance of [SchedulerTaskEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) class, or subclass thereof.
