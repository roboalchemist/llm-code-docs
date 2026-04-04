# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/DependencyBaseModel.md

# [DependencyBaseModel](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel)

Base class used for both Scheduler and Gantt. Not intended to be used directly

## Fields

Fields belong to a Model class and define the Model data structure

[from](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-from)
From event, id of source event

[to](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-to)
To event, id of target event

[type](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-type)
Dependency type, see static property [Type](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#property-Type-static)

[cls](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-cls)
CSS class to apply to lines drawn for the dependency

[bidirectional](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-bidirectional)
Bidirectional, drawn with arrows in both directions

[fromSide](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-fromSide)
Start side on source (top, left, bottom, right)

[toSide](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-toSide)
End side on target (top, left, bottom, right)

[lag](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-lag)
The magnitude of this dependency's lag (the number of units).

[lagUnit](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-lagUnit)
The units of this dependency's lag, defaults to "d" (days). Valid values are:

* "ms" (milliseconds)
* "s" (seconds)
* "m" (minutes)
* "h" (hours)
* "d" (days)
* "w" (weeks)
* "M" (months)
* "y" (years)

This field is readonly after creation, to change `lagUnit` use [setLag()](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#function-setLag).

[fromEvent](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-fromEvent)
Gets/sets the source event of the dependency.

Accepts multiple formats but always returns an [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel).

**NOTE:** This is not a proper field but rather an alias, it will be serialized but cannot be remapped. If you need to remap, consider using [from](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#field-from) instead.

[toEvent](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#field-toEvent)
Gets/sets the target event of the dependency.

Accepts multiple formats but always returns an [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel).

**NOTE:** This is not a proper field but rather an alias, it will be serialized but cannot be remapped. If you need to remap, consider using [to](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#field-to) instead.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyBaseModel](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#property-isDependencyBaseModel)
Identifies an object as an instance of [DependencyBaseModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel) class, or subclass thereof.

[isDependencyBaseModel](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#property-isDependencyBaseModel-static)
Identifies an object as an instance of [DependencyBaseModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel) class, or subclass thereof.

[Type](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#property-Type-static)
An enumerable object, containing names for the dependency types integer constants.

* 0 StartToStart
* 1 StartToEnd
* 2 EndToStart
* 3 EndToEnd

[hardType](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#property-hardType)
Alias to dependency type, but when set resets [fromSide](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#field-fromSide) & [toSide](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#field-toSide) to null as well.

[fullLag](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#property-fullLag)
Property which encapsulates the lag's magnitude and units. An object which contains two properties:

[isPersistable](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#property-isPersistable)
Returns `true` if the linked events have been persisted (e.g. neither of them are 'phantoms')

[isValid](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#property-isValid)
Returns `true` if the dependency is valid. It is considered valid if it has a valid type and both from and to events are set and pointing to different events.

## Functions

Functions are methods available for calling on the class

[setAsync](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#function-setAsync)
Set value for the specified field(s), triggering engine calculations immediately. See [Model#set()](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-set) for arguments. \*

```
dependency.set('from', 2);
// dependency.fromEvent is not yet up to date

await dependency.setAsync('from', 2);
// dependency.fromEvent is up to date
```

[getHardType](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#function-getHardType)
Returns dependency hard type, see [hardType](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#property-hardType).

[setHardType](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#function-setHardType)
Sets dependency [type](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#field-type) and resets [fromSide](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#field-fromSide) and [toSide](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#field-toSide) to null.

[setLag](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#function-setLag)
Sets lag and lagUnit in one go. Only allowed way to change lagUnit, the lagUnit field is readonly after creation

[highlight](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#function-highlight)
Applies given CSS class to dependency, the value doesn't persist

[unhighlight](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#function-unhighlight)
Removes given CSS class from dependency if applied, the value doesn't persist

[isHighlightedWith](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#function-isHighlightedWith)
Checks if the given CSS class is applied to dependency.

[getDefaultType](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#function-getDefaultType-static)
Returns the default dependency type value from the model's field definition.

## Typedefs

Typedefs are type definitions for the class

[DependencyType](https://bryntum.com/docs/gantt/api/Scheduler/model/DependencyBaseModel#typedef-DependencyType)
