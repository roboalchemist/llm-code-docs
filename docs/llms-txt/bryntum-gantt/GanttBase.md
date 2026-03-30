# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/view/GanttBase.md

# [GanttBase](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase)

A thin base class for [Gantt](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt). Does not include any features by default, allowing smaller custom-built bundles if used in place of [Gantt](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[readOnly](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-readOnly)
Configure as `true` to make the Gantt read-only, by disabling any UIs for modifying data.

**Note that checks MUST always also be applied at the server side.**

[project](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-project)
A [ProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel) instance or a config object. The project holds all Gantt data.

[resourceImageFolderPath](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-resourceImageFolderPath)
The path for resource images, used by various widgets such as the resource assignment column.

[defaultResourceImageName](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-defaultResourceImageName)
The file name of an image file to use when a resource has no image, or its image cannot be loaded.

[resourceImagePath](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-resourceImagePath)
The path for resource images, used by various widgets such as the resource assignment column.

[toggleParentTasksOnClick](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-toggleParentTasksOnClick)
True to toggle the collapsed/expanded state when clicking a parent task bar.

[scrollTaskIntoViewOnCellClick](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-scrollTaskIntoViewOnCellClick)
True to scroll the task bar into view when clicking a cell, you can also pass a [scroll config](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#function-scrollTaskIntoView) object.

[eventColor](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-eventColor)
Task color used by default. Tasks can specify their own [eventColor](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-eventColor), which will override this config.

For available standard colors, see [EventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#typedef-EventColor).

[taskRenderer](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-taskRenderer)
An empty function by default, but provided so that you can override it. This function is called each time a task is rendered into the gantt to render the contents of the task.

Returning a string will display it in the task bar, it accepts both plain text or HTML. It is also possible to return a DOM config object which will be synced to the task bars content.

You should never modify any records inside this method.

```
// using plain string
new Gantt({
   taskRenderer : ({ taskRecord }) => StringHelper.encodeHtml(taskRecord.name)
});

// using html string
new Gantt({
   taskRenderer : ({ taskRecord }) => StringHelper.xss`${taskRecord.id} <b>${taskRecord.name}</b>`
});

// using DOM config
new Gantt({
   taskRenderer({ taskRecord }) {
      return {
          tag  : 'b',
          html : StringHelper.encodeHtml(taskRecord.name)
      }
   }
});
```

[newTaskDefaults](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-newTaskDefaults)
A callback function or a set of `name: value` properties to apply on tasks created using the task context menu. Be aware that `name` value will be ignored since it's auto generated and may be configured with localization.

Example:

```
// Object form:
newTaskDefaults : {
   duration          : 3,
   manuallyScheduled : true,
   percentDone       : 15
}
```

```
// Function form:
newTaskDefaults : (targetRecord) => {
   return {
       duration          : targetRecord.duration,
       manuallyScheduled : targetRecord.manuallyScheduled
   }
}
```

[dependencyIdField](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-dependencyIdField)
A task field (id, wbsCode, sequenceNumber etc) that will be used when displaying and editing linked tasks.

[getDateConstraints](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-getDateConstraints)
Returns dates that will constrain resize and drag operations. The method will be called with the task being dragged.

[showTaskColorPickers](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-showTaskColorPickers)
If set to `true` this will show a color field in the [TaskEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskEdit) editor and also a picker in the [TaskMenu](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskMenu). Both enables the user to choose a color which will be applied to the task bar's background. See TaskModel's [eventColor](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-eventColor) config.

[showCostControls](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-showCostControls)
If set to `true` this will:

* show cost, quantity and rate table columns on the task editor "Resources" tab
* show "Rate table" columns in the assignment column editor picker
* include "Cost" column in the "Add new..." column dropdown list

[keyMap](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#keyboard-shortcuts) for details

[showUnscheduledTasks](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-showUnscheduledTasks)
Specify as `false` to not show unscheduled tasks on the Gantt chart. Unscheduled tasks will be rendered as an icon

[transition](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-transition)
Configure UI transitions for various actions in the grid.

[inheritEventColor](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#config-inheritEventColor)
Set to `true` for sub tasks to inherit their parent´s `eventColor`

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGanttBase](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-isGanttBase)
Identifies an object as an instance of [GanttBase](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase) class, or subclass thereof.

[isGanttBase](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-isGanttBase-static)
Identifies an object as an instance of [GanttBase](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase) class, or subclass thereof.

[readOnly](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-readOnly)
Configure as `true` to make the Gantt read-only, by disabling any UIs for modifying data.

**Note that checks MUST always also be applied at the server side.**

[project](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-project)
The [ProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel) instance containing the data visualized by the Gantt chart.

[toggleParentTasksOnClick](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-toggleParentTasksOnClick)
True to toggle the collapsed/expanded state when clicking a parent task bar.

[scrollTaskIntoViewOnCellClick](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-scrollTaskIntoViewOnCellClick)
True to scroll the task bar into view when clicking a cell, you can also pass a [scroll config](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#function-scrollTaskIntoView) object.

[eventColor](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-eventColor)
Task color used by default. Tasks can specify their own [eventColor](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-eventColor), which will override this config.

For available standard colors, see [EventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#typedef-EventColor).

[showUnscheduledTasks](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-showUnscheduledTasks)
Specify as `false` to not show unscheduled tasks on the Gantt chart. Unscheduled tasks will be rendered as an icon

[transition](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-transition)
Configure UI transitions for various actions in the grid.

[inheritEventColor](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#property-inheritEventColor)
Set to `true` for sub tasks to inherit their parent´s `eventColor`

## Functions

Functions are methods available for calling on the class

[resolveDependencyRecord](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-resolveDependencyRecord)
Returns the dependency record for a DOM element

_NOTE: Only available when the [Dependencies](https://bryntum.com/docs/gantt/api/#Gantt/feature/Dependencies) feature is enabled._

[populateTaskMenu](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-populateTaskMenu)
Populates the task context menu. Chained in features to add menu items.

[addTaskAbove](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-addTaskAbove)
Adds a new task above the passed reference task. If no options are provided, the new task will inherit the data from the reference task

[addTaskBelow](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-addTaskBelow)
Adds a new task below the passed reference task. If no options are provided, the new task will inherit the data from the reference task

[addMilestoneBelow](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-addMilestoneBelow)
Adds a new milestone task below the passed reference task

[addSubtask](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-addSubtask)
Adds a new subtask to the passed reference task

[addSuccessor](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-addSuccessor)
Adds a successor task to the passed reference task

[addPredecessor](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-addPredecessor)
Adds a predecessor task to the passed reference task

[indent](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-indent)
Increase the indentation level of one or more tasks in the tree. Has no effect if [TreeGroup](https://bryntum.com/docs/gantt/api/#Gantt/feature/TreeGroup) has regrouped the tree.

[outdent](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-outdent)
Decrease the indentation level of one or more tasks in the tree. Has no effect if [TreeGroup](https://bryntum.com/docs/gantt/api/#Gantt/feature/TreeGroup) has regrouped the tree.

[highlightTasks](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-highlightTasks)
Highlights the elements of the passed task records (or ids). If `scrollToClosest` is set to `true` (which it is by default), the highlighted task element closest to the viewport center will be scrolled into view.

The highlighting will be done by adding the css class `b-highlighted` to the highlighted task elements. Also, the css class `b-is-highlighting` will be added to the `TimeAxisSubGrid` element.

```
// Highlight a single task
gantt.highlightTasks({ tasks : 22 });
// Highlight multiple tasks
gantt.highlightTasks({ tasks : [1, 40] });
// Don't scroll to highlighted task and don't un-highlight on click
gantt.highlightTasks({ tasks : 1000, scroll : false, unhighlightOnClick : false });
```

[unhighlightTasks](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#function-unhighlightTasks)
Removes highlighting from the elements of the passed task records (or ids). If no tasks are passed all highlighted tasks will be un-highlighted.

```
gantt.unhighlightTasks({ tasks : 22 }); // single task
gantt.unhighlightTasks({ tasks : [1, 40] }); // multiple events
```

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[taskMouseDown](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskMouseDown)
Triggered after a mousedown on a task bar.

[taskMouseUp](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskMouseUp)
Triggered after a mouseup on a task bar.

[taskClick](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskClick)
Triggered after a click on a task bar.

[taskDblClick](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskDblClick)
Triggered after a doubleclick on a task.

[taskContextMenu](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskContextMenu)
Triggered after a rightclick (or long press on a touch device) on a task.

[taskMouseOver](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskMouseOver)
Triggered after a mouseover on a task.

[taskMouseOut](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskMouseOut)
Triggered for mouseout from a task.

[taskKeyDown](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskKeyDown)
Triggered when a keydown event is observed if there are selected tasks.

[taskKeyUp](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-taskKeyUp)
Triggered when a keyup event is observed if there are selected tasks.

[renderTask](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-renderTask)
Task is rendered, its element is available in DOM.

[releaseTask](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-releaseTask)
Task is released, no longer in view/removed. A good spot for cleaning custom things added in a `renderTask` listener up, if needed.

[resourceAssignmentClick](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-resourceAssignmentClick)
Triggered when clicking a resource avatar or chip in the cells of the [ResourceAssignmentColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/ResourceAssignmentColumn).

[beforeTaskAdd](https://bryntum.com/docs/gantt/api/Gantt/view/GanttBase#event-beforeTaskAdd)
Fires when adding a task from the UI to allow data mutation.
