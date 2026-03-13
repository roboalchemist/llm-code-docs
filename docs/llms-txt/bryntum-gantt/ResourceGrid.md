# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/view/ResourceGrid.md

# [ResourceGrid](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceGrid)

This grid displays resources of a provided [store](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceGrid#config-store) or [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceGrid#config-project).

The Grid has the following columns by default:

Column Id

Type

Description

`name`

[Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column)

Resource name

`type`

[ResourceTypeColumn](https://bryntum.com/docs/gantt/api/#SchedulerPro/column/ResourceTypeColumn)

Resource type

`materialLabel`

[Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column)

Material resource label

`maxUnits`

[NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn)

Work resource maximum possible effort in percent

`costAccrual`

[ResourceCostAccrualColumn](https://bryntum.com/docs/gantt/api/#SchedulerPro/column/ResourceCostAccrualColumn)

Resource cost accrual

`cost`

[CurrencyColumn](https://bryntum.com/docs/gantt/api/#Grid/column/CurrencyColumn)

Resource cost

`calendar`

[ResourceCalendarColumn](https://bryntum.com/docs/gantt/api/#SchedulerPro/column/ResourceCalendarColumn)

Resource calendar

Customizing columns
-------------------

One should use an object when to configure columns preserving their default set:

```
new ResourceGrid({
    ...
    columns : {
        data : {
            // override default cost column
            cost : {
                text : 'TheCost'
            },
            // override default name column
            name : {
                text : 'Resource Name'
            },
            // append new "City" column
            city : {
                text  : 'City',
                field : 'city'
            }
        }
    }
});
```

Using an array notation in contrast will override the whole set of columns:

```
new ResourceGrid({
    ...
    // The grid will have only one "City" column
    columns : [
        {
            text  : 'City',
            field : 'city'
        }
    ]
});
```

In order to add a new column while preserving the

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceGrid](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceGrid#property-isResourceGrid)
Identifies an object as an instance of [ResourceGrid](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceGrid) class, or subclass thereof.

[isResourceGrid](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceGrid#property-isResourceGrid-static)
Identifies an object as an instance of [ResourceGrid](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceGrid) class, or subclass thereof.
