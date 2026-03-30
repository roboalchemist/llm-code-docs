# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskMenu.md

# [TaskMenu](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskMenu)

Displays a context menu for tasks. Items are populated by other features and/or application code. Configure it with `false` to disable it completely. If enabled, [CellMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/CellMenu) feature is not available. Cell context menu items are handled by this feature.

Default task menu items
-----------------------

Here is the list of menu items provided by the Task menu feature and populated by the other features:

Reference

Text

Weight

Feature

Description

`editTask`

Edit task

100

[TaskEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit)

Edit the task. Hidden when read-only

`showDetails`

Show details

100

[TaskEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit)

Show details of the task in a non-editable form. Hidden when not read-only

`cut`

Cut task

110

[TaskCopyPaste](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskCopyPaste)

Cut the task

`copy`

Copy task

120

[TaskCopyPaste](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskCopyPaste)

Copy the task

`paste`

Paste task

130

[TaskCopyPaste](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskCopyPaste)

Paste the task

`search`\*

Search for value

200

[Search](https://bryntum.com/docs/gantt/api/#Grid/feature/Search)

Search for cell text

`filterMenu`

Filter

400

[Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter)

Shows a submenu to control filtering. See [Filter submenu](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter#menu-items).

`add`

Add...

500

_This feature_

Submenu for adding tasks

\>`addTaskAbove`

Task above

510

_This feature_

Add a new task above the selected task

\>`addTaskBelow`

Task below

520

_This feature_

Add a new task below the selected task

\>`milestone`

Milestone

530

_This feature_

Add a new milestone below the selected task

\>`subtask`

Subtask

540

_This feature_

Add a new task as a child of the current, turning it into a parent

\>`successor`

Successor

550

_This feature_

Add a new task below current task, linked using an "Finish-to-Start" dependency

\>`predecessor`

Predecessor

560

_This feature_

Add a new task above current task, linked using an "Finish-to-Start" dependency

`convertToMilestone`

Convert to milestone

600

_This feature_

Turns the selected task into a milestone. Shown for leaf tasks only

`splitTask`

Split task

650

[EventSegments](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments)

Split the task

`indent`

Indent

700

_This feature_

Add the task as a child of its previous sibling, turning that task into a parent

`outdent`

Outdent

800

_This feature_

Turn the task into a sibling of its parent

`deleteTask`

Delete task

900

_This feature_

Remove the selected task

`linkTasks`

Add dependencies

1000

_This feature_

Add dependencies between two or more selected tasks

`unlinkTasks`

Remove dependencies

1010

_This feature_

Removes dependencies between selected tasks

`taskColor` ¹

Color

1100

_This feature_

Choose background color for the task bar

**¹** Set [showTaskColorPickers](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#config-showTaskColorPickers) to true to enable this item

\*

items that are shown for the locked grid cells only

\>

first level of submenu

Customizing the menu items
--------------------------

The menu items in the Task menu can be customized, existing items can be changed or removed, and new items can be added. This is handled using the `items` config of the feature.

To add extra items for all events:

```
const gantt = new Gantt({
    features : {
        taskMenu : {
            // Extra items for all events
            items : {
                flagTask : {
                    text : 'Extra',
                    icon : 'fa fa-fw fa-flag',
                    onItem({taskRecord}) {
                        taskRecord.flagged = true;
                    }
                }
            }
        }
    }
});
```

Remove menu/submenu items
-------------------------

Items can be removed from the menu:

```
const gantt = new Gantt({
    features : {
        taskMenu : {
            items : {
                // Hide delete task option
                deleteTask: false,

                // Hide item from the `add` submenu
                add: {
                    menu: {
                         subtask: false
                    }
                }
            }
        }
    }
});
```

Manipulate items for specific tasks
-----------------------------------

Items can behave different depending on the type of the task:

```
const gantt = new Gantt({
    features : {
        taskMenu : {
            // Process items before menu is shown
            processItems({ items, taskRecord }) {
                 // Push an extra item for conferences
                 if (taskRecord.type === 'conference') {
                     items.showSessions = {
                         text : 'Show sessions',
                         ontItem({taskRecord}) {
                             // ...
                         }
                     };
                 }

                 // Do not show menu for secret events
                 if (taskRecord.type === 'secret') {
                     return false;
                 }
            }
        }
    }
});
```

Full information of the menu customization can be found in the "Customizing the Task menu" guide.

This feature is **enabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[processItems](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskMenu#config-processItems)
A function called before displaying the menu that allows manipulations of its items. Returning `false` from this function prevents the menu being shown.

```
features         : {
   taskMenu : {
        processItems({ items, taskRecord }) {
            // Add or hide existing items here as needed
            items.myAction = {
                text   : 'Cool action',
                icon   : 'fa fa-fw fa-ban',
                onItem : () => console.log(`Clicked ${eventRecord.name}`),
                weight : 1000 // Move to end
            };

           if (!eventRecord.allowDelete) {
                items.deleteEvent.hidden = true;
            }
        }
    }
},
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskMenu](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskMenu#property-isTaskMenu)
Identifies an object as an instance of [TaskMenu](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskMenu) class, or subclass thereof.

[isTaskMenu](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskMenu#property-isTaskMenu-static)
Identifies an object as an instance of [TaskMenu](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskMenu) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[taskMenuBeforeShow](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskMenu#event-taskMenuBeforeShow)
This event fires on the owning Gantt before the context menu is shown for a task. Allows manipulation of the items to show in the same way as in `processItems`. Returning false from a listener prevents the menu from being shown.

[taskMenuItem](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskMenu#event-taskMenuItem)
This event fires on the owning Gantt when an item is selected in the context menu.

[taskMenuShow](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskMenu#event-taskMenuShow)
This event fires on the owning Gantt after showing the context menu for an event
