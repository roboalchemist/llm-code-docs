# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/TaskEditBase.md

# [TaskEditBase](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase)

Base class for [taskEdit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TaskEdit) and the Gantt `projectEdit` features.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[triggerEvent](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#config-triggerEvent)
The event that shall trigger showing the editor. Set to \`\` or null to disable editing.

[editorClass](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#config-editorClass)
Class to use as the editor.

[saveAndCloseOnEnter](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#config-saveAndCloseOnEnter)
True to save and close this panel if ENTER is pressed in one of the input fields inside the panel.

[blurAction](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#config-blurAction)
What action should be taken when you click outside the editor, `cancel` or `save`

[weekStartDay](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#config-weekStartDay)
The week start day used in all date fields of the feature editor form by default. 0 means Sunday, 6 means Saturday. Defaults to the locale's week start day.

[editorConfig](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#config-editorConfig)
A configuration object applied to the internal editor.

[suspendHasChangesEvent](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#config-suspendHasChangesEvent)
When field in task editor is changed, project model normally will trigger `hasChanges` event. If you use this event to handle project changes excessive events might be a problem. Set this flag to true to only trigger single `hasChanges` event after task changes are applied.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskEditBase](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#property-isTaskEditBase)
Identifies an object as an instance of [TaskEditBase](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TaskEditBase) class, or subclass thereof.

[isTaskEditBase](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#property-isTaskEditBase-static)
Identifies an object as an instance of [TaskEditBase](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TaskEditBase) class, or subclass thereof.

[isEditing](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#property-isEditing)
Returns true if the editor is currently active

## Functions

Functions are methods available for calling on the class

[save](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#function-save)
Call this method to close task editor saving changes.

[cancel](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TaskEditBase#function-cancel)
Call this method to close task editor reverting changes.
