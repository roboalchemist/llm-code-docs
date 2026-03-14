# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/TaskEdit.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskEdit.md

# [TaskEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskEdit)

Feature that allows editing tasks using a [TaskEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor), a popup with fields for editing task data.

This demo shows the task edit feature, double-click child task bar to start editing:

Customizing tabs and their widgets
----------------------------------

To customize tabs you can:

* Reconfigure built-in tabs by providing override configs in the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#config-items) config.
* Remove existing tabs or add your own in the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#config-items) config.
* Advanced: Reconfigure the whole editor widget using [editorConfig](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#config-editorConfig) or replace the whole editor using [editorClass](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#config-editorClass).

This example shows a custom Task Editor configuration. The built-in "Notes" tab is hidden, a custom "Files" tab is added, the "General" tab is renamed to "Common" and "Custom" field is appended to it. Double-click on a task bar to start editing:

To add extra items to a tab you need to specify [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) for the tab container. This example shows custom widgets added to "General" tab:

Note that object notation is used to specify all built-in items in the tabs in the editor, thus object notation has to be used to manipulate them - array notation is not supported.

Expand to see Default tabs and fields
-------------------------------------

The [Task editor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor) contains tabs by default. Each tab is a container with built-in widgets: text fields, grids, etc.

Tab ref

Type

Text

Weight

Description

`generalTab`

[GeneralTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/GeneralTab)

General

100

Name, start/end dates, duration, percent done, effort.

`predecessorsTab`

[PredecessorsTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/PredecessorsTab)

Predecessors

200

Grid with incoming dependencies

`successorsTab`

[SuccessorsTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/SuccessorsTab)

Successors

300

Grid with outgoing dependencies

`resourcesTab`

[ResourcesTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/ResourcesTab)

Resources

400

Grid with assigned resources

`advancedTab`

[AdvancedTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/AdvancedTab)

Advanced

500

Assigned calendar, scheduling mode, constraints, etc.

`notesTab`

[NotesTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/NotesTab)

Notes

600

Text area to add notes to the selected task

### General tab

General tab contains widgets for basic configurations

Widget ref

Type

Text

Weight

Description

`name`

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

Name

100

Task name

`percentDone`

[NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)

% Complete

200

Shows what part of task is done already in percentage

`effort`

[EffortField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EffortField)

Effort

300

Amount of working time required to complete the whole task

`divider`

[Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget)

400

Visual splitter between 2 groups of fields

`startDate`

[StartDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField)

Start

500

Shows when the task begins

`endDate`

[EndDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField)

Finish

600

Shows when the task ends

`duration`

[DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField)

Duration

700

Shows how long the task is

`colorField` ¹

[EventColorField](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorField)

Color ¹

800

Choose background color for the task bar

**¹** Set the [showTaskColorPickers](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#config-showTaskColorPickers) config to `true` to enable this field

### Predecessors tab

Predecessors tab contains a grid with incoming dependencies and controls to remove/add dependencies

Widget ref

Type

Weight

Description

`grid`

[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)

100

Predecessors task name, dependency type and lag

`toolbar`

[Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar)

200

Control buttons

\>`add`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

210

Adds a new predecessor, select task using the name column editor

\>`remove`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

220

Removes selected incoming dependency

\>

first level of submenu

### Successors tab

Successors tab contains a grid with outgoing dependencies and controls to remove/add dependencies

Widget ref

Type

Weight

Description

`grid`

[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)

100

Successors task name, dependency type and lag

`toolbar`

[Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar)

200

Control buttons

\>`add`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

210

Adds a new successor, select task using the name column editor

\>`remove`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

220

Removes selected outgoing dependency

\>

first level of submenu

### Resources tab

Resources tab contains a grid with assignments

Widget ref

Type

Weight

Description

`grid`

[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)

100

Assignments resource name and units (100 means that the assigned resource spends 100% of its working time to the task)

`toolbar`

[Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar)

200

Shows control buttons

\>`add`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

210

Adds a dummy assignment, select resource using the name column editor

\>`remove`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

220

Removes selected assignment

\>

first level of submenu

### Advanced tab

Advanced tab contains additional task scheduling options

Widget ref

Type

Weight

Description

`calendarField`

[Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

100

Shows a list of available calendars for this task

`manuallyScheduledField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

200

If checked, the task is not considered in scheduling

`schedulingModeField`

[SchedulingModePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulingModePicker)

300

Shows a list of available scheduling modes for this task

`effortDrivenField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

400

If checked, the effort of the task is kept intact, and the duration is updated. Works when scheduling mode is "Fixed Units".

`divider`

[Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget)

500

Visual splitter between 2 groups of fields

`constraintTypeField`

[ConstraintTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ConstraintTypePicker)

600

Shows a list of available constraints for this task

`constraintDateField`

[DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)

700

Shows a date for the selected constraint type

`rollupField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

800

If checked, shows a bar below the parent task. Works when the "Rollup" feature is enabled.

`inactiveField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

900

Allows to inactivate the task so it won't take part in the scheduling process.

`ignoreResourceCalendarField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

1000

If checked the task ignores the assigned resource calendars when scheduling

### Notes tab

Notes tab contains a text area to show notes

Field ref

Type

Weight

Description

`noteField`

[TextAreaField](https://bryntum.com/docs/gantt/api/#Core/widget/TextAreaField)

100

Shows a text area to add text notes to the task

Removing a built-in item
------------------------

To remove a built-in tab or widget, specify its `ref` as `false` in the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#config-items) config:

```
const gantt = new Gantt({
    features : {
        taskEdit : {
            items : {
                generalTab      : {
                    items : {
                        // Remove "% Complete","Effort", and the divider in the "General" tab
                        percentDone : false,
                        effort      : false,
                        divider     : false
                    }
                },
                // Remove all tabs except the "General" tab
                notesTab        : false,
                predecessorsTab : false,
                successorsTab   : false,
                resourcesTab    : false,
                advancedTab     : false
            }
        }
    }
})
```

The built-in buttons are:

Widget ref

Type

Weight

Description

`saveButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

100

Save event button on the bbar

`deleteButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

200

Delete event button on the bbar

`cancelButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

300

Cancel event editing button on the bbar

Bottom buttons may be hidden using `bbar` config passed to `editorConfig`:

```
const gantt = new Gantt({
    features : {
        taskEdit : {
            editorConfig : {
                bbar : {
                    items : {
                        deleteButton : false
                    }
                }
            }
        }
    }
})
```

Customizing a built-in item
---------------------------

To customize a built-in tab or field, use its `ref` as the key in the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#config-items) config and specify the configs you want to change (they will be merged with the tabs or fields default configs correspondingly):

```
const gantt = new Gantt({
    features : {
        taskEdit : {
            items : {
                generalTab      : {
                    // Rename "General" tab
                    title : 'Main',
                    items : {
                        // Rename "% Complete" field
                        percentDone : {
                            label : 'Status'
                        }
                    }
                }
            }
        }
    }
})
```

Adding a custom item
--------------------

To add a custom tab or field, add an entry to the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#config-items) config. When you add a field, the `name` property links the input field to a field in the loaded task record:

```
const gantt = new Gantt({
    features : {
        taskEdit : {
            items : {
                generalTab : {
                    items : {
                        // Add new field to the last position
                        newGeneralField : {
                            type   : 'textfield',
                            weight : 710,
                            label  : 'New field in General Tab',
                            // Name of the field matches data field name, so value is loaded/saved automatically
                            name   : 'custom'
                        }
                    }
                },
                // Add a custom tab to the first position
                newTab     : {
                    // Tab is a FormTab by default
                    title  : 'New tab',
                    weight : 90,
                    items  : {
                        newTabField : {
                            type   : 'textfield',
                            weight : 710,
                            label  : 'New field in New Tab',
                            // Name of the field matches data field name, so value is loaded/saved automatically.
                            // In this case it is equal to the Task "name" field.
                            name   : 'name'
                        }
                    }
                }
            }
        }
    }
})
```

Manipulating TaskEditor items at run time
-----------------------------------------

To change input items depending upon the task being edited, use a [beforeTaskEditShow](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#event-beforeTaskEditShow) listener to access the [editor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor) instance.

The available widgets are described [here](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit#expand-to-see-default-tabs-and-fields).

The [editor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor) exposes all its descendant widgets in its [widgetMap](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-widgetMap).

```
const gantt = new Gantt({
    features : {
        taskEdit : true
    },
    listeners : {
        // When editing a parent task, the user may not edit the duration.
        // When editing a leaf level task she may edit the duration.
        beforeTaskEditShow({ taskRecord, editor }) {
            if (taskRecord.isParent) {
                editor.widgetMap.duration.disabled = true;
            }
            else {
                editor.widgetMap.duration.disabled = false;
            }
        }
    }
});
```

To turn off the Task Editor just simple disable the feature.

```
const gantt = new Gantt({
    features : {
        taskEdit : false
    }
})
```

For more info on customizing the Task Editor, please see Guides/Customization/Customize task editor

This feature is **enabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[triggerEvent](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskEdit#config-triggerEvent)
The event that shall trigger showing the editor. Set to \`\` or null to disable editing of existing events.

[editorClass](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskEdit#config-editorClass)
Class to use as the editor. By default it uses [TaskEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskEdit#property-isTaskEdit)
Identifies an object as an instance of [TaskEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit) class, or subclass thereof.

[isTaskEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskEdit#property-isTaskEdit-static)
Identifies an object as an instance of [TaskEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit) class, or subclass thereof.

[editor](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskEdit#property-editor)
The editor widget used for editing task details. Provides an interface to modify task properties within the Gantt.

## Functions

Functions are methods available for calling on the class

[editTask](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskEdit#function-editTask)
Shows a [TaskEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor) to edit the passed task. This function is exposed on the Gantt instance and can be called as `gantt.editTask()`.
