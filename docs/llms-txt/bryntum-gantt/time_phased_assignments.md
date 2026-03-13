# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/data/time_phased_assignments.md

# Time-phased assignments

## Definition

Time-phased assignments are a special kind of resource assignments, that can be limited in time. Normal assignments
lasts during their event's time-span, time-phased assignments however, can have their own start/end date, separate from the
event's start and end dates.

To accommodate for complex scenarios with time-phased assignments, since the 7.0.0 release, there can be more than one assignment
of the same resource to a certain event. Each of those assignments can have its own start/end dates.

For example:

```javascript
const project = new TimePhasedProjectModel({
    resourcesData : [
        { id : 'r1', name : 'Resource1' }
    ],

    tasksData : [
        { id : 't1', name : 'Event1', startDate : '2024-01-01' }
    ],

    assignmentsData : [
        { id : 'a1', resource : 'r1', event : 'e1', startDate : '2024-01-01', endDate : '2024-01-04', effort : 24 },
        { id : 'a1', resource : 'r1', event : 'e1', startDate : '2024-01-07', endDate : '2024-01-10', effort : 48 }
    ]
})
```

In the example above, there are 2 time-phased assignments of the same 'Resource1' for the event 'Event1'.
The 1st assignment lasts from `2024-01-01` till `2024-01-04` and the 2nd from `2024-01-07` till `2024-01-10`.

## Structure of assignments

Internally, it's not the "absolute" start/end dates of the assignments that are preserved, but their relative offset to
the event's start date (or end date for backward scheduling). This offset is calculated according to the calendar
of the assignment's resource.

So if you move an event, its structure will be preserved, all the assignments will keep their offsets,
modulo to the calendars. Calendars may cause a temporary "visual" change of the structure, which is usually restored
when you move event to a different date (with different time-off for resources.)

## Tracking effort of individual assignments

Since 7.0.0 every assignment tracks its effort separately. It is also possible to edit the effort of the assignment.
Previously, the event's effort was tracked at the event level and assignments could have different effort
depending on their position on the time axis. Now, the effort of the assignment is always preserved,
regardless of its position on the time axis.

For example, lets say we have an event with 48h effort which starts at 2024-01-01 and has 2 assignments for Resource1 and Resource2.
Also, Resource2 has a week off in its calendar, starting from 2024-01-01.
Previously, the 48h of effort would be totally consumed by the assignment for Resource1 (while Resource2 is on its week off).
Since 7.0.0, Resource1 and Resource2 both has accurate 24h of effort. Resource2 will start its assignment once the
week off is finished.

## Scheduling modes

Every time-phased assignment actually forms a sub-event of its own. As you may know, the relation between the task's duration, effort and
assignment units is controlled by the event's scheduling mode. Please refer to [this guide](https://bryntum.com/products/gantt/docs/guide/engine/gantt_tasks_scheduling) for more details.

Here we just briefly mention, that there are 3 scheduling modes - `FixedDuration`, `FixedEffort` and `FixedUnits`. Each of the modes,
"fixes" the variable it mentions and during the event mutations it will be changed as a last resort (if possible, other variables
will be changed instead of the "fixed" variable). There's also `effortDriven` flag, which fixes `effort` variable.

Time-phased assignment copies both the scheduling mode and `effortDriven` flag from its event.

If the event has no specific scheduling mode set (default value is `Normal` scheduling mode), its time-phased assignments
are scheduled as `FixedDuration + effortDriven`.

For example, if an event has scheduling mode `FixedUnits` and `effortDriven` flag is enabled, the same parameters will be used
for all of its assignments. And:

- if assignment's units are changed - assignment's duration will be updated.
- if assignment's effort is changed - assignment's duration will be updated.
- if assignment's duration is changed - assignment's effort will be updated (the "fixation" denoted by the scheduling mode takes
precedence over the `effortDriven` flag).

Other scheduling modes works similarly.

When using time-phased assignment, make sure you've provided a correct scheduling mode for its event.

## User interface

On user interface level time-phased assignments can be provided in two places: the resource utilization view and
the task editor.

Effort values can be edited in the resource utilization view since this release which under the hood edits
time-phased assignments.
There are two new features implementing that:

- [AllocationCellEdit](#SchedulerPro/feature/AllocationCellEdit) allows user to enter effort values of ticks
- [AllocationCopyPaste](#SchedulerPro/feature/AllocationCopyPaste) allows user to copy/paste effort values of ticks.

The features rely on exiting `ScheduleContext` feature and can be configured like this:

```javascript
new ResourceUtilization({
    ...
    features : {
        scheduleContext : {
            // allow navigating the timeaxis cells w/ keyboard
            keyNavigation : true,
            // allow multi selecting the timeaxis cells
            // (can be useful for copy/pasting values there)
            multiSelect   : true
        },
        // enable effort values editing
        allocationCellEdit  : true,
        // enable effort values copy/pasting
        allocationCopyPaste : true
    },
    ...
});
```

The task editor widget is another place where time-phased assignments can be edited. Its "Resources" tab has been changed. A resource row now can be expanded to display and edit the resource assignments.
This new user interface actives automatically when a time-phased project is used but can be disabled explicitly if needed like this:

```javascript
new Gantt({
    ...
    features : {
        taskEdit : {
            items : {
                resourcesTab : {
                    // prevent time-phased assignments grid showing
                    showTimePhasedAssignmentsGrid : false
                }
            }
        }
    }
})
```

Please check both of the controls in the updated [resourceutilization](../examples/resourceutilization/) demo.
