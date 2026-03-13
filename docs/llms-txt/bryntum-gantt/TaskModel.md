# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/model/TaskModel.md

# [TaskModel](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel)

This class represents a task in your Gantt project. Extend it to add your own custom task fields and methods.

Subclassing the TaskModel class
-------------------------------

To subclass the TaskModel and add extra [fields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fields-static) and API methods, please see the snippet below.

```
class MyTaskModel extends TaskModel {
  static get fields() {
      return [
          { name: 'importantDate', type: 'date' }
      ]
  }
```

After creating your own Task model class, configure the [taskModelClass](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-taskModelClass) on Project to use it:

```
new Gantt({
    project : {
        taskModelClass : MyTaskModel
    }
});
```

Creating a new Task programmatically
------------------------------------

To create a new task programmatically, simply call the TaskModel constructor and pass in any field values.

```
const newTask = new TaskModel({
    name          : 'My awesome task',
    importantDate : new Date(2022, 0, 1),
    percentDone   : 80 // So awesome it's almost done
    // ...
});
```

Async scheduling
----------------

A record created from an [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) is normally part of a [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore), which in turn is part of a [project](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel). When dates or the duration of a task is changed, the project performs async calculations of the other related fields (including the field of other tasks affected by the change). For example if [duration](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-duration) is changed, it will recalculate [endDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-endDate).

As a result of this being an async operation, the values of other fields are not guaranteed to be up to date immediately after a change. To ensure data is up to date, `await` the calculations to finish.

For example, `endDate` is not up to date after this operation:

```
taskRecord.duration = 5;
// taskRecord.endDate not yet calculated
```

But if calculations are awaited it is up to date:

```
taskRecord.duration = 5;
await taskRecord.project.commitAsync();
// endDate is calculated
```

In case of multiple changes no need to trigger recalculation after each of them:

```
// change taskRecord1 start and duration
taskRecord1.startDate = '2021-11-15';
taskRecord1.duration = 5;
// change taskRecord2 duration
taskRecord2.duration = 1;
// change taskRecord3 finish date
taskRecord3.endDate = '2021-11-17';

// now when all changes are done trigger rescheduling
await taskRecord.project.commitAsync();
```

Manually vs automatically scheduled tasks
-----------------------------------------

A task can be either **automatically** (default) or **manually** scheduled. This is defined by the [manuallyScheduled](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-manuallyScheduled) field. Manually scheduled tasks are not affected by the automatic scheduling process, which means their start/end dates are meant to be changed by user manually. Such tasks are not shifted by their predecessors nor such summary tasks rollup their children start/end dates. While automatically scheduled tasks start/end dates are calculated by the Gantt.

Start and end dates
-------------------

For all tasks, the end date is non-inclusive: [startDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-startDate) <= date < [endDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-endDate). Example: a task which starts at 2020/07/18 and has 2 days duration, should have the end date: 2020/07/20, **not** 2018/07/19 23:59:59. The start and end dates of tasks in are _points_ on the time axis and if you specify that a task starts 01/01/2020 and has 1 day duration, that means the start point is 01/01/2020 00:00 and end point is 02/01/2020 00:00.

## Fields

Fields belong to a Model class and define the Model data structure

[direction](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-direction)
The scheduling direction of this event. The `Forward` direction corresponds to the as-soon-as-possible scheduling (ASAP), `Backward` - to as-late-as-possible (ALAP). The ASAP tasks "sticks" to the project's start date, and ALAP tasks - to the project's end date.

If not specified (which is the default), direction is inherited from the parent task (and from the project for top-level tasks). By default, the project model has forward scheduling mode.

**Note** The ALAP-scheduled task in the ASAP-scheduled project will turn all of its successors into ALAP-scheduled tasks, even if their scheduling direction is specified explicitly by the user as ASAP. We can say that ALAP-scheduling is propagated down through the successors chain. This propagation, however, will stop in the following cases:

* If a successor is manually scheduled
* If a successor has a "Must start/finish on" constraint
* If a dependency to successor is inactive

Similarly, the ASAP-scheduled task in the ALAP-scheduled project will turn all of its predecessors into ASAP-scheduled tasks (also regardless of the user-provided value).

When such propagation is in action, the value of this field is ignored and the UI will disable controls for it.

To determine the actual scheduling direction of the task (which might be different from the user-provided value), one can use the [effectiveDirection](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-effectiveDirection) field.

**Note** For the purposes of compatibility with MS Project and to ease the migration process for users, by default, scheduling direction can be set using the "Constraint type" field on the "Advanced" tab of the task editor. The forward scheduling is specified in it as "As soon as possible" option and backward - "As late as possible". One can also disable the [includeAsapAlapAsConstraints](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-includeAsapAlapAsConstraints) config to render a separate "Scheduling direction" field.

[effectiveDirection](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-effectiveDirection)
The calculated effective scheduling direction of this event. See the [direction](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-direction) field for details.

[id](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-id)
Unique identifier of task (mandatory)

[name](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-name)
Name of the task

[assigned](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-assigned)
A set of resources assigned to this task

[unscheduled](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-unscheduled)
This field is automatically set to `true` when the task is "unscheduled" - user has provided an empty string in one of the UI editors for start date, end date or duration. Such task is not rendered, and does not affect the schedule of its successors.

To schedule the task back, enter one of the missing values, so that there's enough information to calculate start date, end date and duration.

Note, that setting this field manually does nothing. This field should be persisted, but not updated manually.

[startDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-startDate)
Start date of the task in ISO 8601 format

UI fields representing this data field are disabled for summary events except the [manually scheduled](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-manuallyScheduled) events. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

Note that the field always returns a `Date`.

[endDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-endDate)
End date of the task in ISO 8601 format

UI fields representing this data field are disabled for summary events except the [manually scheduled](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-manuallyScheduled) events. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

Note that the field always returns a `Date`.

[duration](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-duration)
The numeric part of the task duration (the number of units).

UI fields representing this data field are disabled for summary events except the [manually scheduled](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-manuallyScheduled) events. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[segments](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-segments)
Segments of the task that appear when the task gets [splitToSegments](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-splitToSegments).

[cls](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-cls)
An encapsulation of the CSS classes to be added to the rendered event element.

Always returns a [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList), but may still be treated as a string. For granular control of adding and removing individual classes, it is recommended to use the [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList) API.

[cost](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-cost)
The total projected cost for the event.

[percentDone](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-percentDone)
The current status of a task, expressed as the percentage completed (integer from 0 to 100)

UI fields representing this data field are disabled for summary events. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[effort](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-effort)
The numeric part of the task effort (the number of units). The effort of the "parent" tasks will be automatically set to the sum of efforts of their "child" tasks

UI fields representing this data field are disabled for summary events. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[durationUnit](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-durationUnit)
The unit part of the task duration, defaults to "day" (days). Valid values are:

Unit

Description

`millisecond`

Milliseconds

`second`

Seconds

`minute`

Minutes

`hour`

Hours

`day`

Days

`week`

Weeks

`month`

Months

`quarter`

Quarters

`year`

Years

It also supports `e*` (elapsed) duration units, where tasks run continuously 24 hours a day, 7 days a week, ignoring all non-working time, ideal for tasks that need to run without breaks or for rough project planning with limited date/duration info.

Unit

Description

`eminute`

Elapsed minute. Lasts 60 seconds.

`ehour`

Elapsed hours. Lasts 60 minutes.

`eday`

Elapsed day. Lasts 24 hours.

`eweek`

Elapsed week. Lasts 7 elapsed days.

`emonth`

Elapsed month. Lasts 30 elapsed days.

`equarter`

Elapsed quarter. Lasts 3 elapsed months.

`eyear`

Elapsed year. Lasts 3 elapsed quarters or 12 elapsed months.

For example:

```
new TaskModel({
    startDate    : '2024-09-10',
    endDate      : '2024-09-17',
    duration     : 7,
    durationUnit : 'ed'
});
```

This field is readonly after creation, to change it use the [setDuration](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-setDuration) call.

[actualEffort](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-actualEffort)
Shows the amount of effort that has already been done by resources assigned to the task.

For a summary task the value is calculated as sum of children actual effort values. Otherwise if the task has assignments the value is calculated as sum of assignments actual efforts. And if not the value is calculated as [effort](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-effort) multiplied by [percentDone](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-percentDone) value.

[effortUnit](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-effortUnit)
The unit part of the task's effort, defaults to "h" (hours). Valid values are:

* "millisecond" - Milliseconds
* "second" - Seconds
* "minute" - Minutes
* "hour" - Hours
* "day" - Days
* "week" - Weeks
* "month" - Months
* "quarter" - Quarters
* "year"- Years

This field is readonly after creation, to change it use the [setEffort](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-setEffort) call.

[effectiveCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-effectiveCalendar)
The effective calendar used by the task. Returns the task own [calendar](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-calendar) if provided or the project [calendar](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-calendar).

[calendar](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-calendar)
The calendar, assigned to the task. Allows you to set the time when task can be performed.

[baselines](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-baselines)
The getter will yield a [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) of [Baseline](https://bryntum.com/docs/gantt/api/#Gantt/model/Baseline)s.

When constructing a task the baselines will be constructed from an array of [Baseline](https://bryntum.com/docs/gantt/api/#Gantt/model/Baseline) data objects.

When serializing, it will yield an array of [Baseline](https://bryntum.com/docs/gantt/api/#Gantt/model/Baseline) data objects.

[note](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-note)
A freetext note about the task.

[postponedConflict](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-postponedConflict)
The field contains a postponed unresolved scheduling conflict the task (if any).

The conflict postponing functionality can be activated with the [allowPostponedConflicts](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-allowPostponedConflicts) and [autoPostponeConflicts](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-autoPostponeConflicts) configuration options, Please refer to those docs for additional details.

[constraintType](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-constraintType)
Field storing the task constraint alias or `null` if not constraint set. Valid values are:

* "finishnoearlierthan"
* "finishnolaterthan"
* "mustfinishon"
* "muststarton"
* "startnoearlierthan"
* "startnolaterthan"

[constraintDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-constraintDate)
Field defining the constraint boundary date or `null` if [constraintType](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-constraintType) is `null`.

[manuallyScheduled](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-manuallyScheduled)
When set to `true`, the [startDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-startDate) of the task will not be changed by any of its incoming dependencies or constraints.

[inactive](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-inactive)
When set to `true` the task becomes inactive and stops taking part in the project scheduling (doesn't affect linked tasks, rolls up its attributes and affect its assigned resources allocation).

[projectConstraintResolution](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-projectConstraintResolution)
Specifies how the task should treat the project border (the project start or end depending if it's scheduled forward or backwards respectively).

The task can either respect the project border which for example means it cannot be placed before its forward scheduled project start. Or the task can ignore the project border and be scheduled regardless of that constraint.

Possible values are:

* `honor` - task respects the project border.
* `ignore` - task ignores the project border.
* `conflict` - the project triggers [schedulingConflict](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#event-schedulingConflict) event when the task attempts to violate its border. So if Gantt has [displaySchedulingIssueResolutionPopup](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-displaySchedulingIssueResolutionPopup) enabled it will display a popup asking user to choose an appropriate resolution. If the option is disabled the application can track the event and implement some other way to handle the conflict.

[ignoreResourceCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-ignoreResourceCalendar)
When set to `true` the calendars of the assigned resources are not taken into account when scheduling the task.

By default the field value is `false` resulting in that the task performs only when its own [calendar](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-calendar) and some of the assigned resource calendars allow that.

[schedulingMode](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-schedulingMode)
This field defines the scheduling mode for the task. Based on this field some fields of the task will be "fixed" (should be provided by the user) and some - computed.

Possible values are:

* `Normal` is the default (and backward compatible) mode. It means the task will be scheduled based on information about its start/end dates, task own calendar (project calendar if there's no one) and calendars of the assigned resources.

* `FixedDuration` mode means, that task has fixed start and end dates, but its effort will be computed dynamically, based on the assigned resources information. Typical example of such task is - meeting. Meetings typically have pre-defined start and end dates and the more people are participating in the meeting, the more effort is spent on the task. When duration of such task increases, its effort is increased too (and vice-versa). Note: fixed start and end dates here doesn't mean that a user can't update them via GUI, the only field which won't be editable in GUI is the [effort field](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-effort), it will be calculated according to duration and resources assigned to the task.

* `FixedEffort` mode means, that task has fixed effort and computed duration. The more resources will be assigned to this task, the less the duration will be. The typical example will be a "paint the walls" task - several painters will complete it faster.

* `FixedUnits` mode means, that the assignment level of all assigned resources will be kept as provided by the user, and either [effort](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-effort) or duration of the task is recalculated, based on the [effortDriven](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-effortDriven) flag.

[effortDriven](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-effortDriven)
This boolean flag defines what part of task data should be updated in the `FixedUnits` scheduling mode. If it is `true`, then [effort](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-effort) is kept intact, and duration is updated. If it is `false` - vice-versa.

[earlyStartDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-earlyStartDate)
A calculated field storing the _early start date_ of the task. The _early start date_ is the earliest possible date the task can start. This value is calculated based on the earliest dates of the task predecessors and the task own constraints. If the task has no predecessors nor other constraints, its early start date matches the project start date.

UI fields representing this data field are naturally disabled since the field is readonly. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[earlyEndDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-earlyEndDate)
A calculated field storing the _early end date_ of the task. The _early end date_ is the earliest possible date the task can finish. This value is calculated based on the earliest dates of the task predecessors and the task own constraints. If the task has no predecessors nor other constraints, its early end date matches the project start date plus the task duration.

UI fields representing this data field are naturally disabled since the field is readonly. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[lateStartDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-lateStartDate)
A calculated field storing the _late start date_ of the task. The _late start date_ is the latest possible date the task can start. This value is calculated based on the latest dates of the task successors and the task own constraints. If the task has no successors nor other constraints, its late start date matches the project end date minus the task duration.

UI fields representing this data field are naturally disabled since the field is readonly. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[lateEndDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-lateEndDate)
A calculated field storing the _late end date_ of the task. The _late end date_ is the latest possible date the task can finish. This value is calculated based on the latest dates of the task successors and the task own constraints. If the task has no successors nor other constraints, its late end date matches the project end date.

UI fields representing this data field are naturally disabled since the field is readonly. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[totalSlack](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-totalSlack)
A calculated field storing the _total slack_ (or _total float_) of the task. The _total slack_ is the amount of working time the task can be delayed without causing a delay to the project end. The value is expressed in [slackUnit](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-slackUnit) units.

```
// let output slack info to the console
console.log(`The ${task.name} task can be delayed for ${task.totalSlack} ${slackUnit}s`)
```

UI fields representing this data field are naturally disabled since the field is readonly. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[slackUnit](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-slackUnit)
A calculated field storing unit for the [totalSlack](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-totalSlack) value.

[critical](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-critical)
A calculated field indicating if the task is _critical_. A task considered _critical_ if its delaying causes the project delay. The field value is calculated based on [totalSlack](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-totalSlack) field value.

```
if (task.critical) {
    Toast.show(`The ${task.name} is critical!`);
}
```

[children](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-children)
Child nodes. To allow loading children on demand, specify `children : true` in your data. Omit the field for leaf tasks.

Note, if the task store loads data from a remote origin, make sure [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl) is specified, and optionally [parentIdParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-parentIdParamName) is set, otherwise [loadChildren](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-loadChildren) has to be implemented.

[showInTimeline](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-showInTimeline)
Set this to true if this task should be shown in the Timeline widget

[rollup](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-rollup)
Set this to true to roll up a task to its closest parent

[wbsValue](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-wbsValue)
The [WBS](https://bryntum.com/docs/gantt/api/#Core/data/Wbs) for this task record. This field is automatically calculated and maintained by the store. This calculation can be refreshed by calling [refreshWbs](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-refreshWbs).

To get string representation of the WBS value (e.g. '2.1.3'), use [value](https://bryntum.com/docs/gantt/api/#Core/data/Wbs#property-value) property.

[deadlineDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-deadlineDate)
A deadline date for this task. Does not affect scheduling logic.

Note that the field always returns a `Date`.

[iconCls](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-iconCls)
CSS class specifying an icon to apply to the task row

[taskIconCls](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-taskIconCls)
CSS class specifying an icon to apply to the task bar

[draggable](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-draggable)
Specify false to prevent the event from being dragged (if [TaskDrag](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskDrag) feature is used)

[resizable](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-resizable)
Specify false to prevent the task from being resized (if [TaskResize](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskResize) feature is used). You can also specify 'start' or 'end' to only allow resizing in one direction

[eventColor](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#field-eventColor)
Changes task's background color. Named colors are applied as a `b-color-{color}` (for example `b-color-red`) CSS class to the task's bar. Colors specified as hex, `rgb()` etc. are applied as a `--b-primary` CSS variable to the bar.

If no color is specified, any color defined in Gantt's [eventColor](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#config-eventColor) config will apply instead.

For available standard colors, see [EventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#typedef-EventColor).

Using named colors:

```
const gantt = new Gantt({
    project {
        tasks : [
            { id : 1, name : 'Important task', eventColor : 'red' }
        ]
    }
});
```

Will result in:

```
<div class="b-gantt-task-wrap b-color-red">
```

Using non-named colors:

```
const gantt = new Gantt({
    project {
        tasks : [
            { id : 1, name : 'Important task', eventColor : '#ff0000' }
        ]
    }
});
```

Will result in:

```
<div class="b-gantt-task-wrap" style="--b-primary: #ff0000">
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskModel](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-isTaskModel)
Identifies an object as an instance of [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) class, or subclass thereof.

[isTaskModel](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-isTaskModel-static)
Identifies an object as an instance of [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) class, or subclass thereof.

[hasPostponedOwnConstraintConflict](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-hasPostponedOwnConstraintConflict)
A read only alias for [postponedConflict](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-postponedConflict) field.

[convertEmptyParentToLeaf](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-convertEmptyParentToLeaf-static)
This static configuration option allows you to control whether an empty parent task should be converted into a leaf. Enable/disable it for a whole class:

```
TaskModel.convertEmptyParentToLeaf = false;
```

By specifying `true`, all empty parents will be considered leafs. Can also be assigned a configuration object with the following Boolean properties to customize the behaviour:

* `onLoad` - Apply the transformation on load to any parents without children (`children : []`)
* `onRemove` - Apply the transformation when all children have been removed from a parent

```
TaskModel.convertEmptyParentToLeaf = {
    onLoad   : false,
    onRemove : true
}
```

[predecessors](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-predecessors)
Returns all predecessor dependencies of this task

[successors](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-successors)
Returns all successor dependencies of this task

[firstSegment](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-firstSegment)
The event first segment or null if the event is not segmented.

[lastSegment](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-lastSegment)
The event last segment or null if the event is not segmented.

[allDependencies](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-allDependencies)
Returns all dependencies of this task (both incoming and outgoing)

[predecessorTasks](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-predecessorTasks)
Returns all direct predecessor tasks of a task

[successorTasks](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-successorTasks)
Returns all direct successor tasks of a task

[durationMS](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-durationMS)
Returns the task [duration](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-duration) in milliseconds.

[previousSiblingsTotalCount](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-previousSiblingsTotalCount)
Returns count of all sibling nodes (including their children).

[sequenceNumber](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-sequenceNumber)
Returns the sequential number of the task. A sequential number means the ordinal position of the task in the total dataset, regardless of its nesting level and collapse/expand state of any parent tasks. The root node has a sequential number equal to 0.

For example, in the following tree data sample sequential numbers are specified in the comments:

```
root : {
    children : [
        {   // 1
            leaf : true
        },
        {       // 2
            children : [
                {   // 3
                    children : [
                        {   // 4
                            leaf : true
                        },
                        {   // 5
                            leaf : true
                        }
                    ]
                }]
        },
        {   // 6
            leaf : true
        }
    ]
}
```

If we collapse parent tasks, sequential number of collapsed tasks won't change.

[fullEffort](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-fullEffort)
Property which encapsulates the effort's magnitude and units.

UI fields representing this property are disabled for summary events. See [isEditable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-isEditable) for details.

[resources](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-resources)
Returns all resources assigned to an event.

[outgoingDeps](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-outgoingDeps)
A `Set<Gantt.model.DependencyModel>` of the outgoing dependencies for this task

[incomingDeps](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-incomingDeps)
A `Set<Gantt.model.DependencyModel>` of the incoming dependencies for this task

[assignments](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#property-assignments)
An array of the assignments, related to this task

## Functions

Functions are methods available for calling on the class

[resolvePostponedConflict](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-resolvePostponedConflict)
Starts a [postponed conflict](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-postponedConflict) resolution (if task has any) and then calls [commitAsync](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#function-commitAsync) method and returns its result.

Please refer to [allowPostponedConflicts](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-allowPostponedConflicts) config documentation for details.

[commitAsync](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-commitAsync)
Propagates changes to the dependent tasks. For example:

```
// double a task duration
task.duration *= 2;
// call commitAsync() to do further recalculations caused by the duration change
task.commitAsync().then(() => console.log('Schedule updated'));
```

[setInactive](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setInactive)
Either activates or deactivates the task depending on the passed value. Will cause the schedule to be updated - returns a `Promise`

[setSegments](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setSegments)
Sets [segments](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-segments) field value.

[splitToSegments](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-splitToSegments)
Splits the task to segments.

[mergeSegments](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-mergeSegments)
Merges the task segments. The method merges two provided task segments (and all the segment between them if any).

[setIgnoreResourceCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setIgnoreResourceCalendar)
Sets the task [ignoreResourceCalendar](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-ignoreResourceCalendar) field value and triggers rescheduling.

[getIgnoreResourceCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-getIgnoreResourceCalendar)
Returns the event [ignoreResourceCalendar](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-ignoreResourceCalendar) field value.

[setBaseline](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setBaseline)
Applies the start/end dates from the task to the corresponding baseline.

```
const task = new TaskModel({
     name: 'New task',
     startDate: '2019-01-14',
     endDate: '2019-01-17',
     duration: 3,
     baselines: [
         // Baseline version 1
         {
             startDate: '2019-01-13',
             endDate: '2019-01-16'
         },
         // Baseline version 2
         {
             startDate: '2019-01-14',
             endDate: '2019-01-17'
         },
         // Baseline version 3
         {
             startDate: '2019-01-15',
             endDate: '2019-01-18'
         }
     ]
});

// Apply the task's start/end dates to the baseline version 3
task.setBaseline(3);
```

[getBaseline](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-getBaseline)
Returns the baseline of the provided version (1-based index).

```
// return the baseline version 3
task.getBaseline(3);
```

[getPlannedPercentDone](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-getPlannedPercentDone)
Returns the task's planned percent done. To calculate it, task needs to have at least 1 baseline set and the reference "status" date should be provided either to this method, or [to the project](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-statusDate).

The calculation is performed as follows:

* If the baseline's end date is before the status date, result value is `100%`
* If the baseline's start date is after the status date, result value is `0%`
* Now the status date is in between the baseline's start and end date, result value is: (status date - baseline start date) / (baseline end date - baseline start date). Here the "minus" operation effectively calculates the duration between the two moments on timeaxis. Duration calculation takes into account the task's calendar.

[isEditable](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-isEditable)
Defines if the given task field should be manually editable in UI. You can override this method to provide your own logic.

By default, the method defines:

* [earlyStartDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-earlyStartDate), [earlyEndDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-earlyEndDate), [lateStartDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-lateStartDate), [lateEndDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-lateEndDate), [totalSlack](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-totalSlack) as not editable;
* [effort](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-effort), [fullEffort](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#property-fullEffort), [percentDone](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-percentDone) as not editable for summary tasks;
* [endDate](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-endDate), [duration](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-duration) and [fullDuration](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-fullDuration) fields as not editable for summary tasks except the [manually scheduled](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-manuallyScheduled) ones.

[convertToMilestone](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-convertToMilestone)
Converts this task to a milestone (start date will match the end date).

[convertToRegular](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-convertToRegular)
Converts the milestone task to a regular task with a duration of 1 (keeping current [durationUnit](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-durationUnit)).

[getAssignmentFor](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-getAssignmentFor)
If given resource is assigned to this task, returns a [AssignmentModel](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel) record. Otherwise returns `null`

[assign](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-assign)
This method assigns a resource to this task.

Will cause the schedule to be updated - returns a `Promise`

[unassign](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-unassign)
This method unassigns a resource from this task.

Will cause the schedule to be updated - returns a `Promise`

[canConvertDuration](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-canConvertDuration)
Indicates whether the task can perform the provided duration conversion. The task might not be able to convert units on early stages of data loading when the project has not loaded its conversion rates yet. So the method by default checks that the project has loaded the rates needed for conversion.

[convertDurationGen](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-convertDurationGen)
Converts a duration value from one time unit to another. The method is a generator since it embeds into the Engine scheduling mechanics.

[setCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setCalendar)
Sets the calendar of the task. Will cause the schedule to be updated - returns a `Promise`

[getCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-getCalendar)
Returns the task calendar.

[setStartDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setStartDate)
Sets the start date of the task. Will cause the schedule to be updated - returns a `Promise`

Note, that the actually set start date may be adjusted, according to the calendar, by skipping the non-working time forward.

[setEndDate](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setEndDate)
Sets the end date of the task. Will cause the schedule to be updated - returns a `Promise`

Note, that the actually set end date may be adjusted, according to the calendar, by skipping the non-working time backward.

[setDuration](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setDuration)
Updates the duration (and optionally unit) of the task. Will cause the schedule to be updated - returns a `Promise`

[setEffort](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setEffort)
Updates the effort (and optionally unit) of the task. Will cause the schedule to be updated - returns a `Promise`

[setConstraint](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-setConstraint)
Sets the constraint type and (optionally) constraining date to the task.

[refreshWbs](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#function-refreshWbs)
Refreshes the [wbsValue](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-wbsValue) of this record and its children. This is rarely needed but may be required after a complex series of filtering, inserting, or removing nodes. In particular, removing nodes does create a gap in `wbsValue` values that may be undesirable.

## Typedefs

Typedefs are type definitions for the class

[ConvertEmptyParentToLeafOptions](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#typedef-ConvertEmptyParentToLeafOptions)
Options for the `convertEmptyParentToLeaf` static property.

[EffectiveDirection](https://bryntum.com/docs/gantt/api/Gantt/model/TaskModel#typedef-EffectiveDirection)
