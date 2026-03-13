# Source: https://bryntum.com/products/gantt/docs-llm/guide/../engine/gantt_tasks_scheduling.md

# Gantt task scheduling

The Bryntum Gantt engine optimizes task scheduling by placing tasks as early as possible (ASAP) within a project
timeline; this is true for forward-scheduled projects only, which is the default case. For a backward-scheduled project,
scheduling happens as late as possible (ALAP). Unpinned tasks automatically align with the startDate of their parent
task or project, while the engine accounts for any dependencies and constraints to ensure accurate scheduling.
It also excludes any manually scheduled or inactive tasks.

This guide helps you understand these concepts in detail, ensuring there is no confusion about task scheduling.

## Scheduling

Tasks can be either **automatically** (default) or **manually** scheduled. This is defined by the
[manuallyScheduled](#Gantt/model/TaskModel#field-manuallyScheduled) task flag.

You can exclude any task from the scheduling process by deactivating it. To do this, set the task's
[inactive](#Gantt/model/TaskModel#field-inactive) field to `true`. Inactive tasks neither push their linked tasks nor add
their attributes to parent tasks.

## Manually scheduled tasks

Tasks that are manually scheduled ([manuallyScheduled](#Gantt/model/TaskModel#field-manuallyScheduled)) are not affected by
the automatic rescheduling process, they are meant to be adjusted manually by a user.

It is also possible to treat started tasks as manually scheduled if their start dates are already determined and should not be auto-calculated.
Configure this behavior using the [startedTaskScheduling](#Gantt/model/ProjectModel#field-startedTaskScheduling) field.

## Automatic task scheduling

One of the most common questions is why tasks of my app are moved to the project's start? It's because of
automatic task scheduling.

The Gantt scheduling engine updates the start and end dates of automatically scheduled tasks based on their
constraints, links and position in the task hierarchy.
It means that the [startDate](#Gantt/model/TaskModel#field-startDate) and [endDate](#Gantt/model/TaskModel#field-endDate) are revalidated and
may be recalculated as soon as the task is added or loaded to a project.

When auto-scheduling, the Gantt engine checks if a task has any predecessors or constraints and schedules
accordingly. If it has none, it will be scheduled as early as possible, which is at the project's start.

You may also want to check [autoSetConstraints](#Gantt/model/ProjectModel#config-autoSetConstraints), enabling this config results in
auto constraints to the tasks, showing your task based on the [startDate](#Gantt/model/TaskModel#field-startDate) and
[endDate](#Gantt/model/TaskModel#field-endDate), if no constraints or dependencies affects it.

### Project direction

The Gantt engine supports both forward and backward scheduling, controlled by
 the [project direction](#Gantt/model/ProjectModel#field-direction) config.

#### Forward scheduled project

In a forward-scheduled project (default), the Gantt engine schedules tasks as soon as possible (ASAP).
For such projects, the [start date](#Gantt/model/ProjectModel#field-startDate) is mandatory and sets an implicit
[Start no earlier than](#Gantt/model/TaskModel#field-constraintType) constraint (see constraint details in the below chapters)
inherited by all tasks. It means any task with no restrictions will fall back to that date.

The [end date](#Gantt/model/ProjectModel#field-endDate) of a forward scheduled project is a calculated value equal to the latest
[end date](#Gantt/model/TaskModel#field-endDate) of its tasks.

#### Backward scheduled project

In a backward scheduled project, the Gantt engine schedules tasks as late as possible (ALAP).
In such a project, the [end date](#Gantt/model/ProjectModel#field-endDate) value is mandatory and the
[start date](#Gantt/model/ProjectModel#field-startDate) is calculated as the earliest [start date](#Gantt/model/TaskModel#field-startDate) of the
project tasks. The project [end date](#Gantt/model/ProjectModel#field-endDate) creates an implicit
[Finish no later than](#Gantt/model/TaskModel#field-constraintType) constraint inherited by all tasks.
It means that any task with no restrictions will fall back to finish on that date.

### Propagating changes through task dependencies

When a task changes, the Gantt engine will automatically reschedule its linked tasks.
In forward-scheduled projects, successors react to their predecessor's changes and in backward-scheduled projects,
the predecessors respond to changes made in their successors.

How dependent tasks will be updated after a modification depends on the
[dependency type](#Gantt/model/DependencyModel#field-type).
The Gantt engine supports the following four types of dependencies:

* Finish-to-Start (default)
* Start-to-Start
* Finish-to-Finish
* Start-to-Finish

#### Finish-to-Start

<img src="engine/media/dependency-fs.png" alt="Finish-to-Start dependency" class="b-half">

The default type of a dependency is "Finish-to-Start" (FS). This type of dependency restricts the dependent task
to not start earlier than the end date of the preceding task.

#### Start-to-Start

<img src="engine/media/dependency-ss.png" alt="Start-to-Start dependency" class="b-half">

With this dependency type, the succeeding task is delayed not to start earlier than the start of the preceding task.

#### Finish-to-Finish

<img src="engine/media/dependency-ff.png" alt="Finish-to-Finish dependency" class="b-half">

The succeeding task cannot finish before the completion of the preceding task.

#### Start-to-Finish

<img src="engine/media/dependency-sf.png" alt="Start-to-Finish dependency" class="b-half">

The finish of the succeeding task is constrained by the start of the preceding task. The successor cannot finish
before the predecessor starts.

#### Dependency lead and lag

A [dependency](#Gantt/model/DependencyModel) can have a [lag (or lead)](#Gantt/model/DependencyModel#field-lag) value which
can delay the succeeding task by the number of [lag units](#Gantt/model/DependencyModel#field-lagUnit) specified.

<img src="engine/media/dependency-lag.png" alt="Dependency lag" class="b-half">

Lead (or "negative lag") will accelerate the succeeding task by the number of time units specified.

<img src="engine/media/dependency-lead.png" alt="Dependency lead" class="b-half">

The [lag](#Gantt/model/DependencyModel#field-lag) value specifies the amount of **working time**. The
calendar controlling which time to use is defined by the [calendar](#Gantt/model/DependencyModel#field-calendar) field. By
 default, the successor calendar is used.

### Event constraint effect on the scheduling

A task constraint defines boundaries for the schedulable date range of a task, and it is taken into account
 when the engine schedules the project tasks.

A constraint is a combination of two task properties: [constraintType](#Gantt/model/TaskModel#field-constraintType) and
[constraintDate](#Gantt/model/TaskModel#field-constraintDate).
The date range specified by a constraint restricts the task start/end dates to be **not earlier than**,
**not later than** or **equal** to the provided [constraintDate](#Gantt/model/TaskModel#field-constraintDate).

As mentioned above, a task with no restrictions is scheduled for the project start for forward projects
(and on the project end date for backward projects). When a user manually drags a task in a Gantt chart,
the Gantt enforces the position by setting a constraint on the task.
In a forward scheduled project, it uses:

* [Start no earlier than](#Gantt/model/TaskModel#field-constraintType) (SNET) constraint when the task is moved by changing
 its [start date](#Gantt/model/TaskModel#field-startDate)
* [Finish no earlier than](#Gantt/model/TaskModel#field-constraintType) (FNET) constraint when the task is moved by changing
 its [end date](#Gantt/model/TaskModel#field-endDate).

For a backward scheduled project, it uses:

* [Start no later than](#Gantt/model/TaskModel#field-constraintType) (SNLT) constraint when the task is moved by changing its
[start date](#Gantt/model/TaskModel#field-startDate)
* [Finish no later than](#Gantt/model/TaskModel#field-constraintType) (FNLT) constraint when the task is moved by changing its
[end date](#Gantt/model/TaskModel#field-endDate).

How a constraint affects a task depends on its [type](#Gantt/model/TaskModel#field-constraintType). There are two groups of
constraints available:

* Inflexible constraints.
* Semi-flexible constraints.

#### Inflexible constraints

There are two constraint types in this group: [Must start on](#Gantt/model/TaskModel#field-constraintType) (MSO) and
[Must finish on](#Gantt/model/TaskModel#field-constraintType) (MFO).
They force a task to start/finish exactly on the [date](#Gantt/model/TaskModel#field-constraintDate) provided.

#### Semi-flexible constraints

These constraints share the same priority with task dependencies. They all work together respecting the task working
time:

* [Start no earlier than](#Gantt/model/TaskModel#field-constraintType) (SNET) - restricts the task to start on or after the
specified date.
* [Finish no earlier than](#Gantt/model/TaskModel#field-constraintType) (FNET) - restricts the task to finish on or after the
specified date.
* [Start no later than](#Gantt/model/TaskModel#field-constraintType) (SNLT) - restricts the task to start before (or on) the
specified date.
* [Finish no later than](#Gantt/model/TaskModel#field-constraintType) (FNLT) - restricts the task to finish before (or on) the
specified date.

Effectively, the task start/end dates are calculated as aggregated values considering dependencies
and such constraints. The earliest start date for a task is computed as the latest of the earliest start allowed by
its constraint and the earliest start allowed by its dependencies.

An example, Event A has two incoming dependencies which don't allow it to start earlier than _01/18/2017_ and the task
has a SNET constraint which forces it to start not earlier than _01/17/2017_. In this case, the resulting earliest
start date of the task is _01/18/2017_. If we change the constraint date to _01/19/2017_ the resulting earliest start
date will be _01/19/2017_.

## Taking into account the project hierarchy

When scheduling tasks, the Gantt engine takes the hierarchy into account by following these two principles:

* Each task inherits its parent (_summary_) task restrictions (dependencies and constraints).
* A summary task [start date](#Gantt/model/TaskModel#field-startDate) and [end date](#Gantt/model/TaskModel#field-endDate) should match the minimum
[start date](#Gantt/model/TaskModel#field-startDate) and maximum [end date](#Gantt/model/TaskModel#field-endDate) of its children respectively. Its
[effort](#Gantt/model/TaskModel#field-effort) equals the sum of the [effort](#Gantt/model/TaskModel#field-effort) values of all its children.

The [% completed](#Gantt/model/TaskModel#field-percentDone) value of a parent task is calculated based on its children's progress. It
is determined by dividing the sum of each child's completed duration by the total duration of all children. The
completed duration for each child is obtained by multiplying its individual percentage completion value by its duration.

To explain this more, consider the following example:
<img src="engine/media/gantt-chart.png" alt="Gantt Chart" class="b-half">

It has the following values:

| Cell                  | Duration | Complete Duration |
| ---------             | -------- | ----------------- |
| Contact designers     | 5        | 350               |
| Shortlist designers   | 3        | 180               |
| Review design         | 2        | 100               |
| Inform management...  | 0        | 0                 |
| Apply design...       | 7        | 0                 |
| **Sum of all**        | 17       | 630               |

Next, divide the sum of the complete duration by the sum of the duration
(`630/17`), which will result in **37%**.

**FYI:** calculation of % done for parent tasks can be disabled by setting
[autoCalculatePercentDoneForParentTasks](#Gantt/model/ProjectModel#field-autoCalculatePercentDoneForParentTasks) to `false`.

Following the above rules, the Gantt engine recalculates summary tasks when their children are updated. The same
goes for the reverse case, child tasks will react to changes to constraints and dependencies of their parents.

## Event scheduling mode

Unlike the dependencies and constraints affecting the task position on the time axis,
the [scheduling mode](#Gantt/model/TaskModel#field-schedulingMode) specifies how the task's properties depend on each other.
It defines which properties are **fixed** (provided by the user) and which should be **calculated**.

There are four [scheduling modes](#Gantt/model/TaskModel#field-schedulingMode) available in the Gantt engine:

* Normal (default mode).
* Fixed Duration
* Fixed Effort
* Fixed Units

There is also an additional [effortDriven](#Gantt/model/TaskModel#field-effortDriven) flag allowing to fix
 the [task effort](#Gantt/model/TaskModel#field-effort) value. When set, it tells the task to preserve its [effort](#Gantt/model/TaskModel#field-effort)
 value and instead recalculate other properties.

### Normal

In the Normal mode (default), the task is scheduled based on information about its start/end dates.
The task [effort](#Gantt/model/TaskModel#field-effort) and [assignments](#Gantt/model/TaskModel#field-assigned) are not calculated in this mode.

This mode is always used for summary tasks.

The [effortDriven](#Gantt/model/TaskModel#field-effortDriven) flag is not used in this mode.

### Fixed Duration

Fixed Duration mode means that the task has fixed [start](#Gantt/model/TaskModel#field-startDate) and [end](#Gantt/model/TaskModel#field-endDate) dates
and [duration](#Gantt/model/TaskModel#field-duration), but its [effort](#Gantt/model/TaskModel#field-effort) is computed dynamically
based on the assigned resources.

A typical example of such a task is a meeting. Meetings typically have pre-defined start and end dates, and the
The more people participating in the meeting, the more effort is spent on the task.
When the duration of such a task increases, its effort increases, too.

Changes to the [effort](#Gantt/model/TaskModel#field-effort) of such a task will cause assignment units recalculation and vice-versa
(assignments change will cause recalculation of the [effort](#Gantt/model/TaskModel#field-effort)).

Enabling [effortDriven](#Gantt/model/TaskModel#field-effortDriven) for a task will change that behavior and force the task to
**always** recalculate its assignment units whenever the task changes its [duration](#Gantt/model/TaskModel#field-duration) or
[effort](#Gantt/model/TaskModel#field-effort).

<div class="warning">
Calculations provided by this mode work only if the task has at least one resource assigned.
</div>

### Fixed Effort

Fixed Effort mode means that the task has a fixed [effort](#Gantt/model/TaskModel#field-effort) and computed
[duration](#Gantt/model/TaskModel#field-duration).
The more resources are assigned to the task, the less the [duration](#Gantt/model/TaskModel#field-duration) will be.

A typical example is a "paint the walls" task - several painters will complete it faster.

Enabling the [effortDriven](#Gantt/model/TaskModel#field-effortDriven) flag makes no sense in this mode.

<div class="warning">
Calculations provided by this mode work only if the task has at least one resource assigned.
</div>

### Fixed Units

Fixed Units mode means, that task has fixed [assignments](#Gantt/model/TaskModel#field-assigned) and computed
[duration](#Gantt/model/TaskModel#field-duration)
or [effort](#Gantt/model/TaskModel#field-effort).

Changes to the [effort](#Gantt/model/TaskModel#field-effort) of such a task will cause [duration](#Gantt/model/TaskModel#field-duration) recalculation
and
vice-versa ([duration](#Gantt/model/TaskModel#field-duration) change will cause recalculation of [effort](#Gantt/model/TaskModel#field-effort)).

Changes of the [assignment](#Gantt/model/TaskModel#field-assigned) of such a task will cause [effort](#Gantt/model/TaskModel#field-effort) recalculation
and [duration](#Gantt/model/TaskModel#field-duration) recalculation if the [effortDriven](#Gantt/model/TaskModel#field-effortDriven) flag is enabled.

<div class="warning">
Calculations provided by this mode work only if the task has at least one resource assigned.
</div>
