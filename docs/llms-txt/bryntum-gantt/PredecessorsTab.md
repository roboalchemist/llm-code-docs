# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/taskeditor/PredecessorsTab.md

# [PredecessorsTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/PredecessorsTab)

A tab inside the [scheduler task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) or [gantt task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/GanttTaskEditor) showing the predecessors of an event or task.

The tab has the following contents by default:

Widget ref

Type

Weight

Description

`grid`

[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)

100

Shows predecessors name, dependency type and lag

\> `id`\*

[Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column)

\-

Id column

\> `name`\*

[Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column)

\-

Name column, linked task

\> `type`\*

[Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column)

\-

Dependency type column

\> `lag`\*

[DurationColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/DurationColumn)

\-

Duration column

`toolbar`

[Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar)

\-

Control buttons in a toolbar docked to bottom

\> `add`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

210

Adds a new predecessor

\> `remove`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

220

Removes selected incoming dependency

\*

Columns are kept in the grids column store, they can be customized in a similar manner as other widgets in the editor

\>

first level of submenu

```
const scheduler = new SchedulerPro({
  features : {
    taskEdit : {
      items : {
         predecessorsTab : {
           items : {
             grid : {
               columns : {
                 // Columns are held in a store, thus it uses `data`
                 // instead of `items`
                 data : {
                   name : {
                     // Change header text for the name column
                     text : 'Linked to'
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

Customize the dependency type picker to show only certain dependency types
--------------------------------------------------------------------------

You can customize which dependency types to show in the picker by filtering the picker store. For example, to show only Finish-to-Start and Start-to-Start types:

```
 features : {
     taskEdit : {
         items : {
             predecessorsTab : {
                 items : {
                     grid : {
                         columns : {
                             data : {
                                 type : {
                                     editor : {
                                         type  : 'dependencytypepicker',
                                         store : {
                                             filters : [{
                                                 // Show only Finish-to-Start and Start-to-Start
                                                 filterBy : record => record.id === DependencyModel.Type.EndToStart || record.id === DependencyModel.Type.StartToStart
                                             }]
                                         }
                                     }
                                 }
                             }
                         }
                     }
                 }
             }
         }
     }
 },
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[sortField](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/PredecessorsTab#config-sortField)
Dependency field to sort predecessors by

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPredecessorsTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/PredecessorsTab#property-isPredecessorsTab)
Identifies an object as an instance of [PredecessorsTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/PredecessorsTab) class, or subclass thereof.

[isPredecessorsTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/PredecessorsTab#property-isPredecessorsTab-static)
Identifies an object as an instance of [PredecessorsTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/PredecessorsTab) class, or subclass thereof.
