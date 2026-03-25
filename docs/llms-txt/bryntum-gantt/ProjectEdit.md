# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/ProjectEdit.md

# [ProjectEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit)

Feature that displays the [project editor](https://bryntum.com/docs/gantt/api/#Gantt/widget/ProjectEditor) allowing users to edit the project settings.

This demo shows the project edit feature, click "Edit project" button to start editing:

Customizing tabs and their widgets
----------------------------------

To customize tabs you can:

* Reconfigure built-in tabs by providing override configs in the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#config-items) config.
* Remove existing tabs or add your own in the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#config-items) config.
* Advanced: Reconfigure the whole editor widget using [editorConfig](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#config-editorConfig) or replace the whole editor using [editorClass](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#config-editorClass).

This example shows a custom Project Editor configuration. The built-in "Description" tab is hidden, the "General" tab is renamed to "Common" and "Custom" field is appended to it. Click "Edit project" button to start editing::

Expand to see Default tabs and fields
-------------------------------------

The [project editor](https://bryntum.com/docs/gantt/api/#Gantt/widget/ProjectEditor) contains tabs by default. Each tab is a container with built in widgets.

Tab ref

Type

Text

Weight

Description

`generalTab`

[ProjectEditorGeneralTab](https://bryntum.com/docs/gantt/api/#Gantt/widget/projecteditor/ProjectEditorGeneralTab)

General

100

Shows basic configuration: name, start/end dates, schedule form

`descriptionTab`

[ProjectEditorDescriptionTab](https://bryntum.com/docs/gantt/api/#Gantt/widget/projecteditor/ProjectEditorDescriptionTab)

Description

200

Shows a text area to add a description to the edited project

`advancedTab`

[ProjectEditorAdvancedTab](https://bryntum.com/docs/gantt/api/#Gantt/widget/projecteditor/ProjectEditorAdvancedTab)

Advanced

300

Shows advanced options: number of hours per day, days per week and days per month

### General tab

General tab contains widgets for basic configurations

Field ref

Type

Weight

Description

`nameField`

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

100

Project [name](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-name) field

`startDateField`

[StartDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField)

200

Project [start date](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-startDate) field

`endDateField`

[EndDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField)

300

Project [end date](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-endDate) field

`calendarField`

[CalendarField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CalendarField)

400

Project [calendar](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-calendar) field

`scheduleFromField`

[RadioGroup](https://bryntum.com/docs/gantt/api/#Core/widget/RadioGroup)

500

Project [scheduling direction](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-direction) field

`readOnlyField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

600

Project [readOnly](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-readOnly) field

### Advanced tab

A tab showing the advanced options for a project.

Field ref

Type

Weight

Description

`hoursPerDayField`

[NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)

100

Project [hours per day](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-hoursPerDay) field

`daysPerWeekField`

[NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)

200

Project [days per week](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-daysPerWeek) field

`daysPerMonthField`

[NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)

300

Project [days per month](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-daysPerMonth) field

### Description tab

Notes tab contains a text area to show notes

A tab showing the description for a project.

Field ref

Type

Weight

Description

`descriptionField`

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

100

A textarea field, to set a description to the project

Removing a built-in item
------------------------

To remove a built-in tab or widget, specify its `ref` as `false` in the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#config-items) config:

```
const gantt = new Gantt({
    features : {
        projectEdit : {
            items : {
                generalTab  : {
                    items : {
                        // Remove the "Calendar" field in the "General" tab
                        calendarField : false
                    }
                },
                // Remove all tabs except the "General" tab
                descriptionTab : false,
                advancedTab    : false
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

`cancelButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

300

Cancel event editing button on the bbar

Bottom buttons may be hidden using `bbar` config passed to `editorConfig`:

```
const gantt = new Gantt({
    features : {
        projectEdit : {
            editorConfig : {
                bbar : {
                    items : {
                        cancelButton : false
                    }
                }
            }
        }
    }
})
```

Customizing a built-in item
---------------------------

To customize a built-in tab or field, use its `ref` as the key in the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#config-items) config and specify the configs you want to change (they will be merged with the tabs or fields default configs correspondingly):

```
const gantt = new Gantt({
    features : {
        projectEdit : {
            items : {
                generalTab : {
                    // Rename "General" tab
                    title : 'Main',
                    items : {
                        // Rename "Calendar" field
                        calendarField : {
                            label : 'Work time'
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

To add a custom tab or field, add an entry to the [items](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#config-items) config. When you add a field, the `name` property links the input field to a field in the loaded project record:

```
const gantt = new Gantt({
    features : {
        projectEdit : {
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
                    // provide weight less than General tab has to make sure this tab goes first
                    weight : 90,
                    items  : {
                        newTabField : {
                            type   : 'textfield',
                            weight : 710,
                            label  : 'New field in New Tab',
                            // Name of the field matches data field name, so value is loaded/saved automatically.
                            // In this case it is equal to the project "name" field.
                            name   : 'name'
                        }
                    }
                }
            }
        }
    }
})
```

Manipulating ProjectEditor items at run time
--------------------------------------------

To change input items depending upon the project being edited, use a [beforeProjectEditShow](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#event-beforeProjectEditShow) listener to access the [editor](https://bryntum.com/docs/gantt/api/#Gantt/widget/ProjectEditor) instance.

The available widgets are described [here](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#expand-to-see-default-tabs-and-fields).

The [editor](https://bryntum.com/docs/gantt/api/#Gantt/widget/ProjectEditor) exposes all its descendant widgets in its [widgetMap](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-widgetMap).

```
const gantt = new Gantt({
    features : {
        projectEdit : true
    },
    listeners : {
        beforeProjectEditShow({ projectRecord, editor }) {
            // if editing a project having non empty startDate value.
            if (projectRecord.startDate) {
                // do not allow editing the project start date
                editor.widgetMap.startDate.disabled = true;
            }
        }
    }
});
```

This feature is **disabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[items](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#config-items)
A configuration object used to customize the contents of the project editor. Supply a config object or boolean per tab (listed below) to either affects its contents or toggle it on/off.

Supplied config objects will be merged with the tabs predefined configs.

To remove existing items, set corresponding keys to `null`.

Built-in tab names are:

* `generalTab`
* `descriptionTab`
* `advancedTab`

```
features : {
    projectEdit : {
        items : {
            // Custom settings and additional items for the general tab
            generalTab : {
                title : 'Common',
                items : {
                    // hide project name field
                    nameField : false,
                    // add a new custom text field
                    myCustomField : {
                        type : 'text',
                        name : 'color'
                    }
                }
            },
            // Hide the advanced tab
            advancedTab : null
        }
    }
}
```

[editorConfig](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#config-editorConfig)
A configuration object applied to the internal [ProjectEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/ProjectEditor). Useful to for example change the title of the editor or to set its dimensions in code:

```
features : {
    projectEdit : {
        editorConfig : {
            title : 'My title',
            height : 300
        }
    }
}
```

NOTE: The easiest approach to affect editor contents is to use the [items config](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit#config-items).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#property-isProjectEdit)
Identifies an object as an instance of [ProjectEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit) class, or subclass thereof.

[isProjectEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#property-isProjectEdit-static)
Identifies an object as an instance of [ProjectEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProjectEdit) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[editProject](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#function-editProject)
Shows a [project editor](https://bryntum.com/docs/gantt/api/#Gantt/widget/ProjectEditor) to edit the passed project. This function is exposed on the Gantt instance and can be called as `gantt.editProject()`.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeProjectEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#event-beforeProjectEdit)
Fires on the owning Gantt widget instance before a project is displayed in the editor. This may be listened to in order to take over the project editing flow. Returning `false` stops the default editing UI from being shown.

Allows async flows by awaiting async listeners. For example:

```
new Gantt({
    listeners : {
        async beforeProjectEdit() {
           await asyncCheckOfRightsOnBackend();
        }
    }
});
```

[projectEditCanceled](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#event-projectEditCanceled)
Fires on the owning Gantt widget when the editor for a project is canceled.

[beforeProjectEditShow](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#event-beforeProjectEditShow)
Fires on the owning Gantt widget when the editor for a project is available but before it is shown. Allows manipulating fields etc.

[beforeProjectSave](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#event-beforeProjectSave)
Fires on the owning Gantt widget instance before a project is saved, return `false` to prevent it.

Allows async flows by awaiting async listeners. For example:

```
new Gantt({
    listeners : {
        async beforeProjectSave() {
           await someAsyncConditionLikeAskingForConfirmation();
        }
    }
});
```

[afterProjectSave](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#event-afterProjectSave)
Fires on the owning Gantt widget instance after a project is saved

[afterProjectEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/ProjectEdit#event-afterProjectEdit)
Fires on the owning Gantt widget instance after project editing is finished by applying changes or cancelling them.
