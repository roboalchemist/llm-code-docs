# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/ResourceEdit.md

# [ResourceEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit)

Feature that displays a popup containing widgets for editing resource data.

This feature is **enabled** by default.

Customizing the editor
----------------------

Please check [ResourceEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceEditor) docs for details on its controls. And this is how the editor controls can be customized:

```
new ResourceGrid({
    ...
    features : {
        resourceEdit : {
            // configure the editor
            editorConfig : {
                items : {
                    mainTabs : {
                        items : {
                            // change "General" tab controls
                            generalTab : {
                                items : {
                                    // rename "Name" field label to "Foo"
                                    nameField : {
                                        label : 'Foo'
                                    },
                                    // add new "Age" field
                                    ageField : {
                                        type  : 'number',
                                        label : 'Age',
                                        field : 'age'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
});
```

The editor contains tabs by default. Each tab is a container with built-in widgets: text fields, grids, etc.

Tab ref

Text

Weight

Class

Description

`generalTab`

General

100

[ResourceEditorGeneralTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/resourceeditor/ResourceEditorGeneralTab)

Name, start/end dates, duration, percent done, effort

`rateTablesTab`

Costs

200

[ResourceEditorRateTablesTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/resourceeditor/ResourceEditorRateTablesTab)

Grid with incoming dependencies

General tab items
-----------------

Widget ref

Weight

Class

Description

`nameField`

10

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

Resource name field

`typeField`

20

[ResourceTypeField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceTypeField)

Resource type field

`maxUnits`

30

[NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)

Resource maximum effort in percent field

`materialLabel`

40

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

Material resource label field

`costAccrual`

50

[CostAccrualField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CostAccrualField)

Resource cost accrual field

`calendarField`

60

[CalendarField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CalendarField)

Material calendar field

Costs tab items
---------------

Widget ref

Weight

Class

Description

`rateTableCombo`

10

[ModelCombo](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ModelCombo)

Rate table field

`addGroupButton`

20

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

Add rate table button

`removeGroupButton`

30

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

Remove rate table button

`useByDefaultCheckbox`

40

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

Use the selected rate table by default checkbox

`rateTablePanel`

50

[ResourceRateTableContainer](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceRateTableContainer)

A panel with the selected rate table info

`defaultRateTable`

\-

[Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field)

A hidden field containing the resource default rate table

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[editorConfig](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#config-editorConfig)
A configuration object applied to the internal [ResourceEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceEditor).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#property-isResourceEdit)
Identifies an object as an instance of [ResourceEdit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/ResourceEdit) class, or subclass thereof.

[isResourceEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#property-isResourceEdit-static)
Identifies an object as an instance of [ResourceEdit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/ResourceEdit) class, or subclass thereof.

[resourceRecord](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#property-resourceRecord)
The current [ResourceModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceModel) record, which is being edited by the editor.

[editor](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#property-editor)
Returns the editor widget representing this feature

[isEditing](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#property-isEditing)
Returns true if the editor is currently active

## Functions

Functions are methods available for calling on the class

[editResource](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#function-editResource)
Opens an editor for the passed resource. This function is exposed on grid and can be called as `grid.editResource()`.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[resourceEditBeforeSave](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#event-resourceEditBeforeSave)
Fires before the resource editor saves changes to a resource.

[resourceEditSave](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#event-resourceEditSave)
Fires after the resource editor saves changes to a resource.

[resourceEditBeforeRemove](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#event-resourceEditBeforeRemove)
Fires before the resource editor removes a resource.

[resourceEditRemove](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#event-resourceEditRemove)
Fires after the resource editor removes a resource.

[beforeResourceEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceEdit#event-beforeResourceEdit)
Fires on the owning grid before a resource editing starts. This may be listened for to allow an application to take over event editing duties. Returning `false` stops the default editing UI from being shown.
