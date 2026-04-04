# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/widget/TaskEditor.md

# [TaskEditor](https://bryntum.com/docs/gantt/api/Gantt/widget/TaskEditor)

Provides a UI to edit tasks in a popup dialog. It is implemented as a Tab Panel with several preconfigured built-in tabs. Although the default configuration may be adequate in many cases, the Task Editor is easily configurable.

This demo shows how to use TaskEditor as a standalone widget:

To hide built-in tabs or to add custom tabs, or to append widgets to any of the built-in tabs use the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#config-items) config.

The Task editor contains tabs by default. Each tab is a container with built-in widgets: text fields, grids, etc.

Tab ref

Text

Weight

Description

`generalTab`

General

100

Name, start/end dates, duration, percent done, effort

`predecessorsTab`

Predecessors

200

Grid with incoming dependencies

`successorsTab`

Successors

300

Grid with outgoing dependencies

`resourcesTab`

Resources

400

Grid with assigned resources

`advancedTab`

Advanced

500

Assigned calendar, scheduling mode, constraints, etc

`notesTab`

Notes

600

Text area to add notes to the selected task

Task editor customization example
---------------------------------

This example shows a custom Task Editor configuration. The built-in "Notes" tab is hidden, a custom "Files" tab is added, the "General" tab is renamed to "Common" and "Custom" field is appended to it. Double-click on a task bar to start editing:

Custom fields in the Task Editor work only if the field is explicitly defined in the Task model. When defined, the field can be added, updated, and stored in the `TaskStore`, even if it is not present in the initial task data. Bryntum extracts fields only from the first task record when no definitions are provided, which can lead to inconsistent behavior. Always define custom fields in the Task model to ensure predictable and reliable functionality.

```
export default class CustomTaskModel extends TaskModel {
 static fields = [
     { name: 'custom', type: 'string' }
 ];
}

const project = new ProjectModel({
 taskModelClass : CustomTaskModel,
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskEditor](https://bryntum.com/docs/gantt/api/Gantt/widget/TaskEditor#property-isTaskEditor)
Identifies an object as an instance of [TaskEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor) class, or subclass thereof.

[isTaskEditor](https://bryntum.com/docs/gantt/api/Gantt/widget/TaskEditor#property-isTaskEditor-static)
Identifies an object as an instance of [TaskEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor) class, or subclass thereof.

[isSchedulerTaskEditor](https://bryntum.com/docs/gantt/api/Gantt/widget/TaskEditor#property-isSchedulerTaskEditor)
Identifies an object as an instance of [SchedulerTaskEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) class, or subclass thereof
