# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/mixin/AssignmentModelMixin.md

# [AssignmentModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin)

Mixin that holds configuration shared between assignments in Scheduler and Scheduler Pro.

## Fields

Fields belong to a Model class and define the Model data structure

[resourceId](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#field-resourceId)
Id for the resource to assign to

[eventId](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#field-eventId)
Id for the event to assign

[drawDependencies](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#field-drawDependencies)
Specify `false` to opt out of drawing dependencies from/to this assignment

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAssignmentModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#property-isAssignmentModelMixin)
Identifies an object as an instance of [AssignmentModelMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/AssignmentModelMixin) class, or subclass thereof.

[isAssignmentModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#property-isAssignmentModelMixin-static)
Identifies an object as an instance of [AssignmentModelMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/AssignmentModelMixin) class, or subclass thereof.

[eventResourceKey](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#property-eventResourceKey)
A key made up from the event id and the id of the resource assigned to.

[eventName](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#property-eventName)
Convenience property to get the name of the associated event.

[resourceName](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#property-resourceName)
Convenience property to get the name of the associated resource.

[isPersistable](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#property-isPersistable)
Returns `true` if the Assignment can be persisted (e.g. task and resource are not 'phantoms').

Note that when using single assignments, assignments are not persisted.

## Functions

Functions are methods available for calling on the class

[setAsync](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#function-setAsync)
Set value for the specified field(s), triggering engine calculations immediately. See [Model#set()](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-set) for arguments.

```
assignment.set('resourceId', 2);
// assignment.resource is not yet resolved

await assignment.setAsync('resourceId', 2);
// assignment.resource is resolved
```

[getResource](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#function-getResource)
Returns the resource associated with this assignment.

[toString](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/AssignmentModelMixin#function-toString)
Returns a textual representation of this assignment (e.g. Mike 50%).
