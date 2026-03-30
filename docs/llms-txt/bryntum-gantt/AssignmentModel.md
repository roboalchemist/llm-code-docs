# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/AssignmentModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/AssignmentModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/model/AssignmentModel.md

# [AssignmentModel](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel)

This class represents a single assignment of a [resource](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel) to a [task](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) in your gantt chart.

## Fields

Fields belong to a Model class and define the Model data structure

[startDate](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-startDate)
The start date of this assignment. Assigning at least 2 variables from 3 (`startDate`, [endDate](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-endDate), [duration](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-duration)) will make assignment "time-phased".

**Please note** that the field has effect only only when [TimePhasedProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TimePhasedProjectModel) is used. Please refer to [time-phased assignments guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/data/time_phased_assignments.md) for more details.

[endDate](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-endDate)
The end date of this assignment. Assigning at least 2 variables from 3 ([startDate](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-startDate), `endDate`, [duration](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-duration)) will make assignment "time-phased".

**Please note** that the field has effect only only when [TimePhasedProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TimePhasedProjectModel) is used. Please refer to [time-phased assignments guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/data/time_phased_assignments.md) for more details.

[duration](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-duration)
The duration of this assignment. Assigning at least 2 variables from 3 ([startDate](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-startDate), [endDate](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-endDate), `duration`) will make assignment "time-phased".

Please refer to [time-phased assignments guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/data/time_phased_assignments.md) for more details.

See also [durationUnit](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-durationUnit).

[durationUnit](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-durationUnit)
The time unit for [duration](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-duration). It has the same meaning and values as [durationUnit](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-durationUnit).

[effort](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-effort)
A numeric value indicating the effort contributed by this assignment to the [event](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-event).

Since 7.0.0 release, the effort for all assignments is tracked separately (previously it was tracked on the event level).

Note, that relation between the assignment's [duration](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-duration), [effort](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-effort) and [units](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-units) is defined by the event's scheduling mode and `effortDriven` flag.

Please refer to [time-phased assignments guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/data/time_phased_assignments.md) for more details.

[effortUnit](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-effortUnit)
The time unit for [effort](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel#field-effort). It has the same meaning and values as [effortUnit](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-effortUnit).

[units](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-units)
The numeric, percent-like value, indicating what is the "contribution level" of the resource availability to the task. Number 100, means that the assigned resource spends 100% of its working time to the task. Number 50 means that the resource spends only half of its available time for the assigned task.

[event](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-event)
Id for event to assign. Note that after load it will be populated with the actual event.

[resource](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#field-resource)
Id for resource to assign to. Note that after load it will be populated with the actual resource.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAssignmentModel](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#property-isAssignmentModel)
Identifies an object as an instance of [AssignmentModel](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel) class, or subclass thereof.

[isAssignmentModel](https://bryntum.com/docs/gantt/api/Gantt/model/AssignmentModel#property-isAssignmentModel-static)
Identifies an object as an instance of [AssignmentModel](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel) class, or subclass thereof.
