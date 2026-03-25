# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/taskeditor/ResourcesTab.md

# [ResourcesTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/ResourcesTab)

A tab inside the [scheduler task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) or [gantt task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/GanttTaskEditor) showing the assigned resources for an event or task.

The tab has the following contents by default:

Widget ref

Type

Weight

Description

`grid`

[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)

100

Shows resource name and assigned units

\> `resource`\*

[Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column)

\-

"Name" column

\> `units`\*

[NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn)

\-

"Units" column

\> `quantity`\*

[NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn)

\-

"Quantity" column

\> `cost`\*

[CurrencyColumn](https://bryntum.com/docs/gantt/api/#Grid/column/CurrencyColumn)

\-

"Cost" column

\> `rateTable`\*

[Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column)

\-

"Rate table" column

`toolbar`

[Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar)

\-

Toolbar docked to bottom

\> `add`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

210

Adds a new assignment

\> `remove`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

220

Removes selected assignment

\*

Columns are kept in the grids column store, they can be customized in a similar manner as other widgets in the editor

\>

first level of submenu

```
const scheduler = new SchedulerPro({
  features : {
    taskEdit : {
      items : {
        resourcesTab : {
          items : {
            grid : {
              columns : {
                // Columns are held in a store, thus it uses `data`
                // instead of `items`
                data : {
                  resource : {
                    // Change header text for the resource column
                    text : 'Machine'
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

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showUnits](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/ResourcesTab#config-showUnits)
Specify `true` to show the "Units" column representing the [assignment units](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/AssignmentModel) value.

[showTimePhasedAssignmentsGrid](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/ResourcesTab#config-showTimePhasedAssignmentsGrid)
Provide `false` to prevent automatic showing of nested time-phased assignments grid when loading a time-phased project data.

[showRateTable](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/ResourcesTab#config-showRateTable)
Specify `true` to show the "Rates table" column representing the [assignment rateTable](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/AssignmentModel#field-rateTable) value.

[showQuantity](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/ResourcesTab#config-showQuantity)
Specify `true` to show the "Quantity" column representing the assigned material resource [quantity](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/AssignmentModel#field-quantity).

[showCost](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/ResourcesTab#config-showCost)
Specify `true` to show the "Cost" column displaying the [assignment cost](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/AssignmentModel#field-cost).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourcesTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/ResourcesTab#property-isResourcesTab)
Identifies an object as an instance of [ResourcesTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/ResourcesTab) class, or subclass thereof.

[isResourcesTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/ResourcesTab#property-isResourcesTab-static)
Identifies an object as an instance of [ResourcesTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/ResourcesTab) class, or subclass thereof.
