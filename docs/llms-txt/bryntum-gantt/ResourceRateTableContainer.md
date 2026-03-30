# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/ResourceRateTableContainer.md

# [ResourceRateTableContainer](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ResourceRateTableContainer)

A container displaying and allowing to edit a rate table record. The widget is used by the resource editor ["Costs" tab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/resourceeditor/ResourceEditorRateTablesTab) and [ResourceRateTableEditor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceRateTableEditor) widget.

The container has the following items:

Widget ref

Weight

Class

Description

`rateTableNameField`

10

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

Rate table name field

`rateGrid`

20

[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)

Grid displaying rates

And the grid has the following columns:

Column id

Class

Description

`startDate`

[DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn)

Rate start date

`standardRate`

[CurrencyColumn](https://bryntum.com/docs/gantt/api/#Grid/column/CurrencyColumn)

Rate amount

`perUseCost`

[CurrencyColumn](https://bryntum.com/docs/gantt/api/#Grid/column/CurrencyColumn)

Per use cost amount

`actions`

[ActionColumn](https://bryntum.com/docs/gantt/api/#Grid/column/ActionColumn)

Actions to be done on the rate: "Add rate" and "Remove rate"

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceRateTableContainer](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ResourceRateTableContainer#property-isResourceRateTableContainer)
Identifies an object as an instance of [ResourceRateTableContainer](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceRateTableContainer) class, or subclass thereof.

[isResourceRateTableContainer](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/ResourceRateTableContainer#property-isResourceRateTableContainer-static)
Identifies an object as an instance of [ResourceRateTableContainer](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ResourceRateTableContainer) class, or subclass thereof.
