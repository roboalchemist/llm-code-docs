# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/ProjectModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/ProjectModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/model/ProjectModel.md

# [ProjectModel](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel)

This class represents a global project of your Project plan or Gantt - a central place for all data.

It holds and links the stores used by Gantt:

* [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore)
* [ResourceStore](https://bryntum.com/docs/gantt/api/#Gantt/data/ResourceStore)
* [AssignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentStore)
* [DependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/data/DependencyStore)
* [CalendarManagerStore](https://bryntum.com/docs/gantt/api/#Gantt/data/CalendarManagerStore)
* [TimeRangeStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-timeRangeStore)

The project has an internal scheduling engine to calculate dates, durations and such. It is also responsible for handling references between models, for example to link a task to a resource (via an assignment). These operations are asynchronous, a fact that is hidden when working in the Gantt UI but which you must know about when performing data level operations.

Task Scheduling
---------------

Without constraints in the dataset there is nothing pinning the tasks to their date, and they will be rescheduled as soon as possible, i.e. at the project start date. To avoid this, simply set `autoSetConstraints` to `true` on the ProjectModel config object. This ensures tasks remain on their specified start dates, providing a more accurate project timeline.

```
project : {
   autoSetContraints : true
}
```

With that, if you use the following data, it will show the tasks at their **startDate**.

```
[{
  "id"          : 1,
  "name"        : "Project Initiation",
  "percentDone" : 100,
  "duration"    : 5,
  "startDate"   : "2024-06-03"
},
{
  "id"          : 2,
  "name"        : "Requirements Gathering",
  "percentDone" : 80,
  "duration"    : 10,
  "startDate"   : "2024-06-10"
},
{
  "id"          : 3,
  "name"        : "Design Phase",
  "percentDone" : 60,
  "duration"    : 15,
  "startDate"   : "2024-06-24"
}]
```

More about this topic can be found in the [Gantt scheduling guide](https://bryntum.com/docs/gantt/api/#../engine/gantt_tasks_scheduling.md)

To see it in action, check out the `auto constraints` [demo](https://bryntum.com/docs/gantt/api/../examples/auto-constraints/).

When there is a change to data that requires something else to be recalculated, the project schedules a calculation (a commit) which happens moments later. It is also possible to trigger these calculations directly. This flow illustrates the process:

1. Something changes which requires the project to recalculate, for example adding a new task:

```
const [task] = project.taskStore.add({ startDate, endDate });
```

1. A recalculation is scheduled, thus:

```
task.duration; // <- Not yet calculated
```

1. Calculate now instead of waiting for the scheduled calculation

```
await project.commitAsync();

task.duration; // <- Now available
```

Please refer to [this guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/data/project_data.md) for more information.

Built-in CrudManager
--------------------

Gantt's project has a [CrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin) built-in. Using it is the recommended way of syncing data between Gantt and a backend. Example usage:

```
const gantt = new Gantt({
    project : {
        // Configure urls used by the built-in CrudManager
        transport : {
            load : {
                url : 'php/load.php'
            },
            sync : {
                url : 'php/sync.php'
            }
        }
    }
});

// Load data from the backend
gantt.project.load()
```

URLs may also be specified using shortcut configs:

```
const gantt = new Gantt({
    project : {
        loadUrl : 'php/load.php'
        syncUrl : 'php/sync.php'
    }
});

gantt.project.load()
```

For more information on CrudManager, see Schedulers docs on [CrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager). For a detailed description of the protocol used by CrudManager, please see the [Crud manager guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/data/crud_manager_project.md)

You can access the current Project data changes anytime using the [changes](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-changes) property.

Working with inline data
------------------------

The project provides an [inlineData](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-inlineData) getter/setter that can be used to manage data from all Project stores at once. Populating the stores this way can be useful if you do not want to use the CrudManager for server communication but instead load data using Axios or similar.

### Getting data

```
const data = gantt.project.inlineData;

// use the data in your application
```

### Setting data

```
// Get data from server manually
const data = await axios.get('/project?id=12345');

// Feed it to the project
gantt.project.inlineData = data;
```

See also [loadInlineData](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#function-loadInlineData)

### Getting changed records

You can access the changes in the current Project dataset anytime using the [changes](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-changes) property. It returns an object with all changes:

```
const changes = project.changes;

console.log(changes);
```

The `changes` object has the following structure:

```
{
  tasks : {
      updated : [{
          name : 'My task',
          id   : 12
      }]
  },
  assignments : {
      added : [{
          event      : 12,
          resource   : 7,
          units      : 100,
          $PhantomId : 'abc123'
      }]
    }
};
```

Monitoring data changes
-----------------------

While it is possible to listen for data changes on the projects individual stores, it is sometimes more convenient to have a centralized place to handle all data changes. By listening for the [change event](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#event-change) your code gets notified when data in any of the stores changes. Useful for example to keep an external data model up to date:

```
const gantt = new Gantt({
    project: {
        listeners : {
            change({ store, action, records }) {
                const { $name } = store.constructor;

                if (action === 'add') {
                    externalDataModel.add($name, records);
                }

                if (action === 'remove') {
                    externalDataModel.remove($name, records);
                }
            }
        }
    }
});
```

Processing the data loaded from the server
------------------------------------------

If you want to process the data received from the server after loading, you can use the [beforeLoadApply](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#event-beforeLoadApply) or [beforeSyncApply](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#event-beforeSyncApply) events:

```
const gantt = new Gantt({
    project: {
        listeners : {
            beforeLoadApply({ response }) {
                // do something with load-response object before it is provided to all the project stores
            }
        }
    }
});
```

Built-in StateTrackingManager
-----------------------------

The project also has a built-in [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager) (STM for short), that handles undo/redo for the project stores (additional stores can also be added). By default, it is only used while editing tasks using the task editor, the editor updates tasks live and uses STM to rollback changes if canceled. But you can enable it to track all project store changes:

```
// Enable automatic transaction creation and start recording
project.stm.autoRecord = true;
project.stm.enable();

// Undo a transaction
project.stm.undo();

// Redo
project.stm.redo();
```

Check out the `undoredo` demo to see it in action.

## Fields

Fields belong to a Model class and define the Model data structure

[skipNonWorkingTimeWhenSchedulingManually](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-skipNonWorkingTimeWhenSchedulingManually)
When `true` the project manually scheduled tasks will adjust their proposed start/end dates to skip non working time.

See also [skipNonWorkingTimeInDurationWhenSchedulingManually](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-skipNonWorkingTimeInDurationWhenSchedulingManually)

[skipNonWorkingTimeInDurationWhenSchedulingManually](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-skipNonWorkingTimeInDurationWhenSchedulingManually)
When `true` the project's manually scheduled tasks duration will include only working periods of time. When `false` such tasks will ignore working time calendars and treat all intervals as working.

IMPORTANT: Setting this to `false` also forcefully sets the [skipNonWorkingTimeWhenSchedulingManually](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-skipNonWorkingTimeWhenSchedulingManually) option to `false`.

[startedTaskScheduling](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-startedTaskScheduling)
Specifies how started tasks are scheduled. Possible values are:

* `Auto` - (default) tasks are scheduled regardless of whether they are started or not
* `Manual` - started tasks preserve their current positions ignoring their dependencies The rationale behind this is a started task implies its start date is already established and thus should not be calculated dynamically.

[addConstraintOnDateSet](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-addConstraintOnDateSet)
If this flag is set to `true` (default) when a start/end date is set on the event, a corresponding `start-no-earlier/later-than` constraint is added, automatically. This is done in order to keep the event "attached" to this date, according to the user intention.

Depending on your use case, you might want to disable this behaviour.

[hoursPerDay](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-hoursPerDay)
The number of hours per day.

**Please note:** the value **does not define** the amount of **working** time per day for that purpose one should use calendars.

The value is used when converting the duration from one unit to another. So when user enters a duration of, for example, `5 days` the system understands that it actually means `120 hours` and schedules accordingly.

[daysPerWeek](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-daysPerWeek)
The number of days per week.

**Please note:** the value **does not define** the amount of **working** time per week for that purpose one should use calendars.

The value is used when converting the duration from one unit to another. So when user enters a duration of, for example, `2 weeks` the system understands that it actually means `14 days` (which is then converted to [hours](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-hoursPerDay)) and schedules accordingly.

[daysPerMonth](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-daysPerMonth)
The number of days per month.

**Please note:** the value **does not define** the amount of **working** time per month for that purpose one should use calendars.

The value is used when converting the duration from one unit to another. So when user enters a duration of, for example, `1 month` the system understands that it actually means `30 days` (which is then converted to [hours](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-hoursPerDay)) and schedules accordingly.

[dependenciesCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-dependenciesCalendar)
The source of the calendar for dependencies (the calendar used for taking dependencies lag into account). Possible values are:

* `ToEvent` - successor calendar will be used (default);
* `FromEvent` - predecessor calendar will be used;
* `Project` - the project calendar will be used.
* `AllWorking` - the project 24/7 elapsed calendar will be used.

[calendar](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-calendar)
The project calendar.

[autoCalculatePercentDoneForParentTasks](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-autoCalculatePercentDoneForParentTasks)
`true` to enable automatic [% done](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-percentDone) calculation for summary tasks, `false` to disable it.

[autoMergeAdjacentSegments](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-autoMergeAdjacentSegments)
When `true` (default) adjacent or overlapping task segments get merged automatically.

[allowPostponedConflicts](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-allowPostponedConflicts)
If this field is set to `true` scheduling conflicts will include an additional resolution option to "postpone" the conflict resolution. The conflict then is stored in the task [postponedConflict](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-postponedConflict) field and can be visualized with the [TaskInfoColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/TaskInfoColumn).

To force the resolution of such conflict programmatically, one should call the [resolvePostponedConflict](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-resolvePostponedConflict) method.

[autoPostponeConflicts](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-autoPostponeConflicts)
If this field is set to `true` scheduling conflicts will not show the conflict resolution popup but instead will be saved into tasks [postponedConflict](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-postponedConflict) field.

See also the docs for [allowPostponedConflicts](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-allowPostponedConflicts) for additional details.

[autoPostponedConflicts](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-autoPostponedConflicts)
If this field is set to `true` scheduling conflicts will not show the conflict resolution popup but instead will be saved into tasks [postponedConflict](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-postponedConflict) field.

[autoScheduleManualTasksOnSecondPass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-autoScheduleManualTasksOnSecondPass)
When this flag is enabled (default), manually scheduled tasks are scheduled automatically on the 2nd scheduling pass. This is a backward pass ("late" start/end dates) for forward-scheduled project and forward pass ("early" start/end dates) for backward-scheduled project. Because of it, manually scheduled tasks may have non-zero slack.

This is the same behaviour as in MSProject, though you might have different requirements.

When this flag is disabled, manually scheduled tasks are "fixed" in time during both passes, so they will always have 0 slack.

[ignoreConstraintsOnConflictDuringSecondPass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-ignoreConstraintsOnConflictDuringSecondPass)
**This option is experimental and subject for possible change**.

The second scheduling pass is a backward pass ("late" start/end dates) for forward-scheduled project and forward pass ("early" start/end dates) for backward-scheduled project.

When this flag is enabled, if a conflict between the task's constraint and incoming dependencies occurs during the 2nd scheduling pass, the task's constraint is ignored and task is scheduled according to its dependencies.

This happens only during the specified type of conflict. For other types of conflict and for no-conflict case scheduling is performed as usual.

Enabling this option will enable tasks to have negative slack, which sometimes is desirable.

[maxCriticalPathsCount](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-maxCriticalPathsCount)
The maximum number of _critical paths_ to collect in [criticalPaths](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-criticalPaths). When critical tasks connectivity is high (there are many of such tasks having many critical predecessors) the tasks might produce a huge number of critical paths which can't really be handled by a browser. So this value limits the number of paths to collect to protect from such cases.

Set the value to zero to disable the limitation.

[startDate](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-startDate)
Start date of the project in the ISO 8601 format. Setting this date will constrain all other tasks in the project to start no earlier than it.

If this date is not provided, it will be calculated as the earliest date among all tasks.

Note that the field always returns a `Date`.

[endDate](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-endDate)
End date of the project in the ISO 8601 format. The value is calculated as the latest date among all tasks.

Note that the field always returns a `Date`.

[direction](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-direction)
The scheduling direction of the project tasks. The `Forward` direction corresponds to the As-Soon-As-Possible (ASAP) scheduling, `Backward` - to As-Late-As-Possible (ALAP).

When using backward scheduling on the project, you should either make both start and end date fields persistent on all tasks, or make both start and end date fields on the project persistent. This is because for initial calculation, Gantt will need to have the project's end date upfront, before performing calculations.

To set the scheduling direction of the individual tasks, use the [direction](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-direction) field of the TaskModel.

[statusDate](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-statusDate)
The status date of the project. It is just a date, that sets a reference point to various reporting facilities, like [ProgressLine](https://bryntum.com/docs/gantt/api/#Gantt/feature/ProgressLine) or [PlannedPercentDoneColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/PlannedPercentDoneColumn).

By default, the current date/time is used.

[name](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-name)
Name of the project

[description](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#field-description)
Description of the project

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[silenceInitialCommit](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-silenceInitialCommit)
Silences propagations caused by the project loading.

Applying the loaded data to the project occurs in two basic stages:

1. Data gets into the engine graph which triggers changes propagation
2. The changes caused by the propagation get written to related stores

Setting this flag to `true` makes the component perform step 2 silently without triggering events causing reactions on those changes (like sending changes back to the server if `autoSync` is enabled) and keeping stores in unmodified state.

This is safe if the loaded data is consistent so propagation doesn't really do any adjustments. By default the system treats the data as consistent so this option is `true`.

```
new Gantt({
    project : {
        // We want scheduling engine to recalculate the data properly
        // so then we could save it back to the server
        silenceInitialCommit : false,
        ...
    }
    ...
})
```

[preventSilencingOnIssueResolve](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-preventSilencingOnIssueResolve)
Setting this to `true` (default) vetoes [silenceInitialCommit](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-silenceInitialCommit) effect by preventing silent changes accepting on initial data loading if some scheduling issue gets resolved during it.

Enabling this config allows an application to persist the data in a resolved state.

[maxCalendarRange](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-maxCalendarRange)
Maximum range the project calendars can iterate. The value is defined in milliseconds and by default equals `5 years` roughly.

```
new Gantt({
    project : {
        // adjust calendar iteration limit to 10 years roughly:
        // 10 years expressed in ms
        maxCalendarRange : 10 * 365 * 24 * 3600000,
        ...
    }
});
```

[adjustDurationToDST](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-adjustDurationToDST)
This config manages DST correction in the scheduling engine. It only has effect when DST transition hour is working time. Usually DST transition occurs on Sunday, so with non working weekends the DST correction logic is not involved.

If **true**, it will add/remove one hour when calculating duration from start/end dates. For example: Assume weekends are working and on Sunday, 2020-10-25 at 03:00 clocks are set back 1 hour. Assume there is a task:

```
{
    startDate    : '2020-10-20',
    duration     : 10,
    durationUnit : 'day'
}
```

It will end on 2020-10-29 23:00. Because of the DST transition Sunday is actually 25 hours long and when the Gantt project calculates the end date it converts days to hours multiplying by 24. If you're setting duration and want task to end on the end of the day you should manually correct for DST, like so:

```
{
    startDate    : '2020-10-20',
    duration     : 10 * 24 + 1,
    durationUnit : 'hour'
},
```

If task has start and end dates it will correct for DST twice:

```
{
    startDate    : '2020-10-20',
    endDate      : '2020-10-30'
}
```

This task will end on 2020-10-29 22:00 which is a known quirk.

If **false**, the Gantt project will not add DST correction which fixes the quirk mentioned above and such task will end on 2020-10-30 exactly, having hours duration of 10 days \* 24 hours + 1 hour.

Also, for this task days duration will be a floating point number due to extra (or missing) hour:

```
task.getDuration('day')  // 10.041666666666666
task.getDuration('hour') // 241
```

[calendar](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-calendar)
The project calendar.

[bwcConflictPostpone](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-bwcConflictPostpone)
Enables backward compatible conflicts postponing logic covering only conflicts between a task constraint and its incoming dependencies.

[stm](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-stm)
Configuration options to provide to the STM manager

[eventStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-eventStore)
A [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore) instance or a config object.

[taskStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-taskStore)
An alias for the [eventStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-eventStore).

[dependencyStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-dependencyStore)
A [DependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/data/DependencyStore) instance or a config object.

[resourceStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-resourceStore)
A [ResourceStore](https://bryntum.com/docs/gantt/api/#Gantt/data/ResourceStore) instance or a config object.

[assignmentStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-assignmentStore)
An [AssignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentStore) instance or a config object.

[calendarManagerStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-calendarManagerStore)
A [CalendarManagerStore](https://bryntum.com/docs/gantt/api/#Gantt/data/CalendarManagerStore) instance or a config object.

[taskModelClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-taskModelClass)
The constructor of the event model class, to be used in the project. Will be set as the [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) property of the [eventStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-eventStore)

[dependencyModelClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-dependencyModelClass)
The constructor of the dependency model class, to be used in the project. Will be set as the [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) property of the [dependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-dependencyStore)

[resourceModelClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-resourceModelClass)
The constructor of the resource model class, to be used in the project. Will be set as the [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) property of the [resourceStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-resourceStore)

[assignmentModelClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-assignmentModelClass)
The constructor of the assignment model class, to be used in the project. Will be set as the [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) property of the [assignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-assignmentStore)

[calendarModelClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-calendarModelClass)
The constructor of the calendar model class, to be used in the project. Will be set as the [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) property of the [calendarManagerStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-calendarManagerStore)

[taskStoreClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-taskStoreClass)
The constructor to create an task store instance with. Should be a class, subclassing the [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore)

[dependencyStoreClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-dependencyStoreClass)
The constructor to create a dependency store instance with. Should be a class, subclassing the [DependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/data/DependencyStore)

[resourceStoreClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-resourceStoreClass)
The constructor to create a dependency store instance with. Should be a class, subclassing the [ResourceStore](https://bryntum.com/docs/gantt/api/#Gantt/data/ResourceStore)

[assignmentStoreClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-assignmentStoreClass)
The constructor to create a dependency store instance with. Should be a class, subclassing the [AssignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentStore)

[calendarManagerStoreClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-calendarManagerStoreClass)
The constructor to create a calendar store instance with. Should be a class, subclassing the [CalendarManagerStore](https://bryntum.com/docs/gantt/api/#Gantt/data/CalendarManagerStore)

[tasksData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-tasksData)
The initial data, to fill the [taskStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-taskStore) with. Should be an array of [TaskModels](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) or configuration objects.

[eventsData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-eventsData)
Alias to [tasksData](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-tasksData).

[dependenciesData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-dependenciesData)
The initial data, to fill the [dependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-dependencyStore) with. Should be an array of [DependencyModels](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel) or configuration objects.

[resourcesData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-resourcesData)
The initial data, to fill the [resourceStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-resourceStore) with. Should be an array of [ResourceModels](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel) or configuration objects.

[assignmentsData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-assignmentsData)
The initial data, to fill the [assignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-assignmentStore) with. Should be an array of [AssignmentModels](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel) or configuration objects.

[calendarsData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-calendarsData)
The initial data, to fill the [calendarManagerStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-calendarManagerStore) with. Should be an array of [CalendarModels](https://bryntum.com/docs/gantt/api/#Gantt/model/CalendarModel) or configuration objects.

[timeRangeStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-timeRangeStore)
Store that holds time ranges - instances of [TimeRangeModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeRangeModel) for the [TimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges) feature. A store will be automatically created if none is specified.

[resetUndoRedoQueuesAfterLoad](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-resetUndoRedoQueuesAfterLoad)
Set to `true` to reset the undo/redo queues of the internal [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager) after the Project has loaded. Defaults to `false`

[delayCalculation](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-delayCalculation)
Enables early rendering in Gantt, by postponing calculations to after the first refresh.

Requires task data loaded in Gantt to be pre-normalized to function as intended, since it will be used to render tasks before engine has normalized the data. Given un-normalized data tasks will snap into place when calculations are finished.

The Gantt chart will be read-only until the initial calculations are finished.

[enableProgressNotifications](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-enableProgressNotifications)
Set to `true` to enable calculation progress notifications. When enabled, the project fires [progress](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#event-progress) events and the Gantt chart load mask reacts by showing a progress bar for the Engine calculations.

**Note**: Enabling progress notifications will impact calculation performance, since it needs to pause calculations to allow the UI to redraw.

[includeAsapAlapAsConstraints](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-includeAsapAlapAsConstraints)
Whether to include "As soon as possible" and "As late as possible" in the list of the constraints, for compatibility with the MS Project. Enabled by default.

Note, that when enabling this option, you can not have a regular constraint on the task and ASAP/ALAP flag in the same time.

See also docs of the [direction](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-direction) field.

[autoSetConstraints](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-autoSetConstraints)
When set to `true`, pins a task at its starting date. Otherwise, it is rescheduled to the project's starting date if there is no predecessor or constraint supplied.

When a dataset is loaded without using any constraints, dependencies, or manually scheduled tasks, the tasks are moved to the project's start date. Setting `autoSetConstraints` to `true` avoids this behaviour by showing your tasks based on their **startDate** and **endDate**. To see it in action, check out the `auto constraints` [demo](https://bryntum.com/docs/gantt/api/../examples/auto-constraints/).

[tasks](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-tasks)
Data use to fill the [taskStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-taskStore). Should be an array of [TaskModels](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) or its configuration objects.

[resources](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-resources)
Data use to fill the [resourceStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-resourceStore). Should be an array of [ResourceModels](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel) or its configuration objects.

[assignments](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-assignments)
Data use to fill the [assignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-assignmentStore). Should be an array of [AssignmentModels](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel) or its configuration objects.

[dependencies](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-dependencies)
Data use to fill the [dependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-dependencyStore). Should be an array of [DependencyModels](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel) or its configuration objects.

[timeRanges](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-timeRanges)
Data use to fill the [timeRangeStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-timeRangeStore). Should be an array of [TimeRangeModels](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeRangeModel) or its configuration objects.

[calendars](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-calendars)
Data use to fill the [calendarManagerStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-calendarManagerStore). Should be a [CalendarModel](https://bryntum.com/docs/gantt/api/#Gantt/model/CalendarModel) array or its configuration objects.

[timeRangesData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#config-timeRangesData)
The initial data, to fill the [timeRangeStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-timeRangeStore) with. Should be an array of [TimeRangeModels](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeRangeModel) or configuration objects.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectModel](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-isProjectModel)
Identifies an object as an instance of [ProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel) class, or subclass thereof.

[isProjectModel](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-isProjectModel-static)
Identifies an object as an instance of [ProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel) class, or subclass thereof.

[changes](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-changes)
Returns current Project changes as an object consisting of added/modified/removed arrays of records for every managed store. Returns `null` if no changes exist. Format:

```
{
    resources : {
        added    : [{ name : 'New guy' }],
        modified : [{ id : 2, name : 'Mike' }],
        removed  : [{ id : 3 }]
    },
    events : {
        modified : [{  id : 12, name : 'Cool task' }]
    },
    ...
}
```

[stm](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-stm)
State tracking manager instance the project relies on

[eventStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-eventStore)
The [store](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore) holding the task information.

See also [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel)

[taskStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-taskStore)
An alias for the [eventStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-eventStore).

See also [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel)

[dependencyStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-dependencyStore)
The [store](https://bryntum.com/docs/gantt/api/#Gantt/data/DependencyStore) holding the dependency information.

See also [DependencyModel](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel)

[resourceStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-resourceStore)
The [store](https://bryntum.com/docs/gantt/api/#Gantt/data/ResourceStore) holding the resources that can be assigned to the tasks in the task store.

See also [ResourceModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel)

[assignmentStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-assignmentStore)
The [store](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentStore) holding the assignment information.

See also [AssignmentModel](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel)

[calendarManagerStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-calendarManagerStore)
The [store](https://bryntum.com/docs/gantt/api/#Gantt/data/CalendarManagerStore) holding the calendar information.

See also [CalendarModel](https://bryntum.com/docs/gantt/api/#Gantt/model/CalendarModel)

[timeRangeStore](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-timeRangeStore)
The [store](https://bryntum.com/docs/gantt/api/#Core/data/Store) containing time ranges to be visualized.

See also [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan)

[criticalPaths](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-criticalPaths)
Returns an array of critical paths. Each _critical path_ is an array of critical path nodes. Each _critical path node_ is an object which contains [critical task](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-critical) and [dependency](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel) leading to the next critical path node. Dependency is missing if it is the last critical path node in the critical path. To highlight critical paths, enable [CriticalPaths](https://bryntum.com/docs/gantt/api/#Gantt/feature/CriticalPaths) feature.

```
// This is an example of critical paths structure
[
     // First path
     [
         {
             event : Gantt.model.TaskModel
             dependency : Gantt.model.DependencyModel
         },
         {
             event : Gantt.model.TaskModel
         }
     ],
     // Second path
     [
         {
             event : Gantt.model.TaskModel
         }
     ]
     // and so on....
]
```

For more details on the _critical path method_ theory please check [this article](https://bryntum.com/docs/gantt/api/https://en.wikipedia.org/wiki/Critical_path_method).

[segmentModelClass](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-segmentModelClass)
Class implementing a task segment. Can be used for customizing the class implementing segments:

```
// new class for a segment
class MySegment extends EventSegmentModel {
    static fields = [
       { name : 'responsiblePerson' }
    ];
}
new Gantt({
    project : {
        // tell the project to use the new class for segments
        segmentModelClass : MySegment
    }
})
```

[enableProgressNotifications](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-enableProgressNotifications)
Enables/disables the calculation progress notifications.

[tasks](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-tasks)
Get/set [taskStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-taskStore) data.

Always returns an array of [TaskModels](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) but also accepts an array of its configuration objects as input.

[resources](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-resources)
Get/set [resourceStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-resourceStore) data.

Always returns an array of [ResourceModels](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel) but also accepts an array of its configuration objects as input.

[assignments](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-assignments)
Get/set [assignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-assignmentStore) data.

Always returns an array of [AssignmentModels](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel) but also accepts an array of its configuration objects as input.

[dependencies](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-dependencies)
Get/set [dependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-dependencyStore) data.

Always returns an array of [DependencyModels](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel) but also accepts an array of its configuration objects as input.

[timeRanges](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-timeRanges)
Get/set [timeRangeStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-timeRangeStore) data.

Always returns an array of [TimeSpans](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) but also accepts an array of its configuration objects as input.

[calendars](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-calendars)
Get/set [calendarManagerStore](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#property-calendarManagerStore) data.

Always returns a [CalendarModel](https://bryntum.com/docs/gantt/api/#Gantt/model/CalendarModel) array but also accepts an array of its configuration objects as input.

[inlineData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#property-inlineData)
Get or set data of project stores. The returned data is identical to what [toJSON](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#function-toJSON) returns:

```

const data = scheduler.project.inlineData;

// data:
{
    tasks : [
        { id : 1, name : 'Proof-read docs', startDate : '2017-01-02', endDate : '2017-01-09' },
        { id : 2, name : 'Release docs', startDate : '2017-01-09', endDate : '2017-01-10' }
    ],
    resources : [
        { id : 1, name : 'Arcady' },
        { id : 2, name : 'Don' }
    ],
    dependencies : [
        { fromTask : 1, toTask : 2 }
    ],
    assignments : [
         { 'event' : 1, 'resource' : 1 },
         { 'event' : 2, 'resource' : 2 }
     ]
}

// Plug it back in later
scheduler.project.inlineData = data;
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `tasksData` is deprecated, use `tasks` instead. For now, both naming schemes are included in the data object

## Functions

Functions are methods available for calling on the class

[setStartDate](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-setStartDate)
Sets the project start date and commits the changes.

[isEditable](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-isEditable)
Defines if the given project field should be manually editable in UI. You can override this method to provide your own logic.

[setCalculations](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-setCalculations)
Overrides the project owned store identifiers calculation and launches rescheduling.

[getCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-getCalendar)
Returns a calendar of the project. If task has never been assigned a calendar a project's calendar will be returned.

[setCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-setCalendar)
Sets the calendar of the project. Will cause the schedule to be updated - returns a `Promise`

[propagate](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-propagate)
Causes the scheduling engine to re-evaluate the task data and all associated data and constraints and apply necessary changes.

[suspendPropagate](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-suspendPropagate)
Suspend [propagation](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#function-propagate) processing. When propagation is suspended, calls to [propagate](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#function-propagate) do not proceed, instead a propagate call is deferred until a matching [resumePropagate](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#function-resumePropagate) is called.

[resumePropagate](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-resumePropagate)
Resume [propagation](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#function-propagate). If propagation is resumed (calls may be nested which increments a suspension counter), then if a call to propagate was made during suspension, [propagate](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#function-propagate) is executed.

[loadInlineData](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-loadInlineData)
Accepts a "data package" consisting of data for the projects stores, which is then loaded into the stores.

The package can hold data for TaskStore, AssignmentStore, ResourceStore, DependencyStore and Calendar Manager. It uses the same format as when creating a project with inline data:

```
await project.loadInlineData({
    tasks : [
        { id : 1, name : 'Proof-read docs', startDate : '2017-01-02', endDate : '2017-01-09' },
        { id : 2, name : 'Release docs', startDate : '2017-01-09', endDate : '2017-01-10' }
    ],
    resources : [
        { id : 1, name : 'Arcady' },
        { id : 2, name : 'Don' }
    ],
    dependencies : [
        { fromTask : 1, toTask : 2 }
    ],
    assignments : [
         { 'event' : 1, 'resource' : 1 },
         { 'event' : 2, 'resource' : 2 }
     ]
     calendars    : [
         {
             id        : 111,
             name      : 'My cool calendar',
             intervals : [
                 {
                     recurrentStartDate : 'on Sat',
                     recurrentEndDate   : 'on Mon',
                     isWorking          : false
                 }
             ]
         }
     ]
});
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `tasksData` is deprecated, use `tasks` instead. For now, both naming schemes are included in the data object

After populating the stores it commits the project, starting its calculations. By awaiting `loadInlineData()` you can be sure that project calculations are finished.

[commitAsync](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#function-commitAsync)
Project changes (CRUD operations to records in its stores) are automatically committed on a buffer to the underlying graph based calculation engine. The engine performs it calculations async.

By calling this function, the commit happens right away. And by awaiting it you are sure that project calculations are finished and that references between records are up to date.

The returned promise is resolved with an object. If that object has `rejectedWith` set, there has been a conflict and the calculation failed.

```
// Move a task in time
taskStore.first.shift(1);

// Trigger calculations directly and wait for them to finish
const result = await project.commitAsync();

if (result.rejectedWith) {
    // there was a conflict during the scheduling
}
```

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[progress](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#event-progress)
Fired during the Engine calculation if [enableProgressNotifications](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-enableProgressNotifications) config is `true`

[cycle](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#event-cycle)
Fired when the Engine detects a computation cycle.

[schedulingConflict](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#event-schedulingConflict)
Fired when the Engine detects a scheduling conflict.

[emptyCalendar](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#event-emptyCalendar)
Fired when the Engine detects a calendar misconfiguration when the calendar does not provide any working periods of time which makes usage impossible.

[dataReady](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#event-dataReady)
Fired when the engine has finished its calculations and the results has been written back to the records.

```
gantt.project.on({
    dataReady({ records }) {
        console.log('Calculations finished');
        for (const record of records) {
            console.log(`Modified #${record.id}: ${JSON.stringify(record.modifications)}`);
        }
        // Output:
        // Modified #12: {"endDate":null,"duration":7200000,"id":12}
        // Modified #1: {"percentDone":49.99998611112847,"id":1}
        // Modified #1000: {"percentDone":49.99965834045124,"id":1000}
    }
});

gantt.project.taskStore.first.duration = 10;

// At some point a bit later it will log 'Calculations finished', etc.
```

[change](https://bryntum.com/docs/gantt/api/Gantt/model/ProjectModel#event-change)
Fired when data in any of the projects stores changes.

Basically a relayed version of each stores own change event, decorated with which store it originates from. See the [store change event](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-change) documentation for more information.
