# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/ResourceEditor.md

# [ResourceEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ResourceEditor)

A widget allowing to edit the provided [resource](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceModel).

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

The [tab panel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel) itself has `mainTabs` ref.

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

[resource](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ResourceEditor#config-resource)
A resource to edit.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ResourceEditor#property-isResourceEditor)
Identifies an object as an instance of [ResourceEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceEditor) class, or subclass thereof.

[isResourceEditor](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ResourceEditor#property-isResourceEditor-static)
Identifies an object as an instance of [ResourceEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceEditor) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[save](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ResourceEditor#function-save)
Saves changes to the resource.
