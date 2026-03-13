# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/mixin/ResourceModelMixin.md

# [ResourceModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin)

Mixin that holds configuration shared between resources in Scheduler and Scheduler Pro.

## Fields

Fields belong to a Model class and define the Model data structure

[id](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-id)
Unique identifier

[name](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-name)
Get or set resource name

[eventColor](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-eventColor)
Controls the primary color used for events assigned to this resource. Can be overridden per event using EventModels [eventColor config](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-eventColor). Also, see Schedulers [eventColor config](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-eventColor).

For available standard colors, see [EventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#typedef-EventColor).

**Note**: In a TreeStore, leaf nodes inherits their parent´s eventColor if they lack their own color.

[eventStyle](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-eventStyle)
Controls the style used for events assigned to this resource. Can be overridden per event using EventModels [eventStyle config](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-eventStyle). See Schedulers [eventStyle config](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-eventStyle) for available options.

[imageUrl](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-imageUrl)
Fully qualified image URL, used by `ResourceInfoColumn` and vertical modes `ResourceHeader` to display a miniature image for the resource.

[image](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-image)
Image name relative to [resourceImagePath](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-resourceImagePath), used by `ResourceInfoColumn` and vertical modes `ResourceHeader` to display a miniature image for the resource. Set value to `false` to disable image display.

[resourceMargin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-resourceMargin)
Control how much space to leave between the first event/last event and the resources edge (top/bottom margin within the resource row in horizontal mode, left/right margin within the resource column in vertical mode), in px.

It's also possible to set different values for top/left and bottom/right by assigning an object to `resourceMargin` with `start` (margin top in horizontal mode, margin left in vertical mode) and `end` (margin bottom / margin right) properties:

```
scheduler = new Scheduler({
    resourceMargin : {
        start : 15,
        end   : 1
    }
});
```

[barMargin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-barMargin)
Margin between stacked event bars for this resource, in px.

[rowHeight](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-rowHeight)
The base height of this resource, in px. When unset, Schedulers configured rowHeight is used.

This value is used in horizontal mode to determine row height. When stacking, it is used as input for calculating the actual row height:

```
row.height = (resource.rowHeight - (resourceMargin.start + resourceMargin.end)) * overlap count - barMargin * (overlap count - 1)
```

When packing or overlapping, it is used as the actual row height.

[columnWidth](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-columnWidth)
Base width of this resource, in px. If not set, the `columnWidth` specified in the Scheduler's configured [resourceColumns](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-resourceColumns) is used.

This value is used in vertical mode to determine column width.

[eventLayout](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-eventLayout)
Specify this to use a resource specific event layout in horizontal mode, see [eventLayout](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-eventLayout) for options.

When unset (the default) Schedulers setting is used.

[allowOverlap](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-allowOverlap)
Set to `false` to prevent overlapping events for this resource

[showAvatar](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#field-showAvatar)
Set to `false` to not display an avatar for this resource in the [ResourceInfoColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ResourceInfoColumn)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#property-isResourceModelMixin)
Identifies an object as an instance of [ResourceModelMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ResourceModelMixin) class, or subclass thereof.

[isResourceModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#property-isResourceModelMixin-static)
Identifies an object as an instance of [ResourceModelMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ResourceModelMixin) class, or subclass thereof.

[assignments](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#property-assignments)
Returns all assignments for the resource

[isPersistable](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#property-isPersistable)
Returns `true` if the resource can be persisted. In a flat store, a resource is always considered persistable. In a tree store, a resource is considered persistable if its parent node is persistable.

[initials](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#property-initials)
Returns the initials (first letter of the first & last space-separated word in the name) or an empty string if this resource has no name. You can override this method in a ResourceModel subclass to provide your own implementation

## Functions

Functions are methods available for calling on the class

[setAsync](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#function-setAsync)
Set value for the specified field(s), triggering engine calculations immediately. See [Model#set()](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-set) for arguments.

This does not matter much on the resource itself, but is of importance when manipulating its references:

```
assignment.set('resourceId', 2);
// resource.assignments is not yet up to date

await assignment.setAsync('resourceId', 2);
// resource.assignments is up to date
```

[unassignAll](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#function-unassignAll)
Unassigns this Resource from all its Events

## Typedefs

Typedefs are type definitions for the class

[ResourceMarginConfig](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ResourceModelMixin#typedef-ResourceMarginConfig)
Config object used to set different values for top/left and bottom/right margin.
