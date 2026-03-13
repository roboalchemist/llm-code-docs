# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/view/Gantt.md

# [Gantt](https://bryntum.com/docs/gantt/api/Gantt/view/Gantt)

Summary
-------

The **Gantt** widget is the main component that visualizes the project data contained in a [ProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel) instance. The Gantt view is implemented as a TreeGrid consisting of a left section showing the task hierarchy (or WBS) and a right section showing a graphical representation of the tasks on the time axis. Task relationships (or "dependencies") are rendered as arrows between the tasks and in the background you can (optionally) render non-working time too.

The view is very interactive by default:

* hovering over elements shows informative tooltips
* right-clicking various elements shows context menus
* double-clicking the task name shows an inline editor
* double-clicking a task bar opens a detailed task editor popup
* task bars can be dragged and resized
* task progress can be changed by drag drop
* task dependencies can be created by drag drop

The Gantt view is very easy to use and is fully functional with minimal configuration yet it is highly configurable through many configuration options and features.

The minimum configuration consists of a [project](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-project) and [columns](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-columns). (If you only want to show the "Name" column, you can even omit `columns` as it's the default column set.)

Inheriting from Bryntum Grid
----------------------------

Bryntum Gantt inherits from Bryntum Grid, meaning that most features available in the grid are also available for the Gantt component. Common features include columns, cell editing, context menus, row grouping, sorting and more. Note: If you want to use the Grid component standalone, e.g. to use drag-from-grid functionality, you need a separate license for the Grid component.

For more information on configuring columns, filtering, search etc. please see the [Grid API docs](https://bryntum.com/docs/gantt/api/#Grid/view/Grid).

Configuring data for Gantt
--------------------------

The central place for all data visualized in the Gantt chart is the [ProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel) instance, passed as the [project](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-project) configuration option when configuring the Gantt.

For details related to the Gantt data structure / updating data / loading and saving data to the server, adding custom fields and other information, please refer to the [Project data guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/data/project_data.md).

Configuring columns
-------------------

The only mandatory column is the `name` column which is of type [NameColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/NameColumn). It is a tree column that shows the project WBS structure, and allows inline editing of the [name](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-name) field.

The Gantt chart ships with lots of predefined columns (such as [PercentDoneColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/PercentDoneColumn)) but you can of course add your own columns too, showing any additional data in your data model.

Advanced configurations
-----------------------

Almost any aspect of Bryntum Gantt can be configured. The included examples cover most of the supported configuration options. To see some of the features in action, please click on the links below:

* [Labels](https://bryntum.com/docs/gantt/api/../examples/labels/)
* [Tooltips](https://bryntum.com/docs/gantt/api/../examples/tooltips)
* [Time Ranges](https://bryntum.com/docs/gantt/api/../examples/timeranges/)
* [Resource Picker](https://bryntum.com/docs/gantt/api/../examples/resourceassignment/)
* [Task Menu](https://bryntum.com/docs/gantt/api/../examples/taskmenu/)
* [Task Editor](https://bryntum.com/docs/gantt/api/../examples/taskeditor/)
* [Undo/Redo](https://bryntum.com/docs/gantt/api/../examples/undoredo/)
* [Advanced](https://bryntum.com/docs/gantt/api/../examples/advanced)

Keyboard shortcuts
------------------

Gantt has the following default keyboard shortcuts:

Keys

Action

Action description

`Alt`+`Shift`+`ArrowRight`

_indent_

Indents currently selected tasks

`Alt`+`Shift`+`ArrowLeft`

_outdent_

Outdents currently selected tasks

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

As Gantt is a subclass of Grid, many of Grid's [keyboard-shortcuts](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#keyboard-shortcuts) works for Gantt as well.

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/customization/keymap.md).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[crudManagerClass](https://bryntum.com/docs/gantt/api/Gantt/view/Gantt#config-crudManagerClass)
**This config is not used in the Gantt**

[crudManager](https://bryntum.com/docs/gantt/api/Gantt/view/Gantt#config-crudManager)
**This config is not used in the Gantt. Please use [project](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-project) config instead**

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGantt](https://bryntum.com/docs/gantt/api/Gantt/view/Gantt#property-isGantt)
Identifies an object as an instance of [Gantt](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt) class, or subclass thereof.

[isGantt](https://bryntum.com/docs/gantt/api/Gantt/view/Gantt#property-isGantt-static)
Identifies an object as an instance of [Gantt](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt) class, or subclass thereof.
