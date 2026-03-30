# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/NestedEvents.md

# [NestedEvents](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents)

A feature that renders child events nested inside their parent. Requires Scheduler Pro to use a tree event store (normally handled automatically when events in data has children).

The feature has configs for [eventLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-eventLayout), [resourceMargin](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-resourceMargin) and [barMargin](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-barMargin) that are separate from those on Scheduler Pro and only affect nested events.

You can by default drag nested events out of their parents and drop any event onto root level events to nest. The drag and drop behaviour can be customized using the [constrainDragToParent](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-constrainDragToParent), [allowNestingOnDrop](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-allowNestingOnDrop) and [allowDeNestingOnDrop](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-allowDeNestingOnDrop) configs.

Note that for a nested event to show up for a resource both the parent and the nested event has to be assigned to that resource.

Parent / children scheduling
----------------------------

Scheduler Pro uses a scheduling engine closely related to the one used by Gantt (a subset of it). It for example schedules based on calendars (skipping non-working time), dependencies and constraints.

### Scheduling parents

Part of the scheduling engines default logic is that parent events' start and end dates (and thus duration) is defined by their children. This means that if you remove the latest scheduled child of a parent, the parents end date and duration will be adjusted to match the new latest scheduled child (shrink-wrapping children).

Depending on what you plan to use nested events for in your application, this might not be the desired behaviour. If you want the parent event to keep its dates regardless of its children, you should flag it as [manuallyScheduled](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-manuallyScheduled).

Note that by flagging an event as manually scheduled, it will no longer take non-working time or constraints into account either.

A parent defined like this will shrink / grow with its children:

```
{
    "id"        : 1,
    "startDate" : "2022-03-24",
    "children"  : [
        ...
    ]
}
```

Try removing an event here to see what happens:

A parent with `manuallyScheduled : true` will **not** shrink / grow with is children:

```
{
    "id"                : 1,
    "startDate"         : "2022-03-24",
    "duration"          : 10,
    "manuallyScheduled" : true
    "children"          : [
        ...
    ]
}
```

Try the same thing here:

Note that this also makes resizing a parent event that is not manually scheduled useless, it would only snap back to the dates defined by its children. To avoid confusion, resizing is turned off for parent events unless they have `manuallyScheduled: true`

#### Drag and drop for parent events

Normally the dates of a parent event is defined by its children (as described above), with exception for when drag dropping a parent event along the time axis. In this case the operation will update the dates of all the children, which will thus also move the parent event in time.

If a parent event is dragged to a new resource, all its children will also be assigned to that resource.

### Scheduling children (nested events)

Nested events are scheduled using much of the same logic as normal/parent events, but with some differences:

* To maintain the relative position in time of nested events within their parent, they utilize a `delayFromParent` field. The field accepts a magnitude of `durationUnit` (defaults to days). Sample dataset (note that supplying `delayFromParent` is optional, see the next bullet):

    ```
    {
      "name" : "Parent",
      "startDate" : "2023-08-21", // Monday
      "children" : [
        { "name" : "Child 1", "delayFromParent" : 0 }
        { "name" : "Child 2", "delayFromParent" : 2 }
      ]
    }
    ```

    Parent starts on 2023-08-21, the first child will start on the same date, the second child will start 2 days later (2023-08-23).

    If the parent instead started on a Friday, the outcome would be that the second child starts 2 working days later, which would be the following Tuesday.

    Note that when supplying `delayFromParent` in data, since parent events shrink wrap their children, the earliest child must have `"delayFromParent": 0`.

* If `delayFromParent` is not present in the loaded data, the field is calculated as `nestedStart - parentStart - non-working time` (for example if parent starts on a Friday, and nested event on a Monday, `delayFromParent` will be 1). Sample dataset:

    ```
    {
     "name" : "Parent",
     "startDate" : "2023-08-21", // Monday
     "children" : [
       { "name" : "Child 1", "startDate" : "2023-08-21" },
       { "name" : "Child 2", "startDate" : "2023-08-23" }
     ]
    }
    ```

    Yields the same result as above, parent and first child starts on 2023-08-21, second child starts 2 days later. Child 1 gets `delayFromParent: 0` and child 2 gets `delayFromParent: 2` from the calculation.

Dependencies
------------

Nested events support dependencies, with some caveats:

* Dependency lines are by default drawn on the top of events, instead of behind them. This is to ensure they are visible when drawn into a parent (or fully within one). The Dependencies feature can be configured with [drawAroundParents](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Dependencies#config-drawAroundParents) set to `true` to instead attempt to draw around parents when possible.
* When using dependencies, the body of parent events with overflowing nested children is not scrollable. This is because there is no tracking of the scrolling of parent events, and thus dependency lines would not be drawn correctly on scroll. If your app only needs dependencies between parents, you can configure [allowCreateOnlyParent](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/DependencyCreation#config-allowCreateOnlyParent) as `true`. In this case, their container is scrollable.
* Dependencies are only supported for one level of nesting (with `maxNesting: 1`, which is the default).

Caveats
-------

Usage of the feature comes with some requirements/caveats:

* As already mentioned, it requires a tree event store
* Requires using an AssignmentStore, the legacy single assignment mode does not handle tree stores
* Scheduler must use stack or overlap [eventLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro#config-eventLayout), pack not supported
* Multi event drag is not supported for nested events
* Cannot [EventDragCreate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragCreate) within parent events
* [Labels](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Labels) are not supported for nested events
* [EventBuffer](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventBuffer) won't work with nested events
* [TaskEdit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TaskEdit) does not allow assigning resources or dependencies to nested events
* Does not work in combination with recurring events

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[eventLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-eventLayout)
This config defines how to handle overlapping nested events. Valid values are:

* `stack`, events use fixed height and stack on top of each other (not supported in vertical mode)
* `pack`, adjusts event height
* `none`, allows events to overlap

Note that stacking works differently for nested events as compared to normal events (and not at all in vertical mode). The height of the parent event will never change, all nested events use [fixed height](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-eventHeight) and will stack until all available space is consumed, after which they will overflow the parent.

Also note that stacked nested events are clipped by the parent, making it scrollable on vertical overflow. This cannot be combined with sticky events. If stacking events in your app won't overflow the parent, you can specify \`overflow: visible\` on \`.b-nested-events-container.b-nested-events-layout-stack\` to not clip and make sticky events work.

[barMargin](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-barMargin)
Vertical (horizontal in vertical mode) space between nested event bars, in px

[resourceMargin](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-resourceMargin)
Control how much space to leave between the first nested event bar/last nested event and the parent event (top/bottom margin within the parent event row in horizontal mode, left/right margin within the parent event column in vertical mode), in px.

It's also possible to set different values for top/left and bottom/right by assigning an object to `resourceMargin` with `start` (margin top in horizontal mode, margin left in vertical mode) and `end` (margin bottom / margin right) properties:

```
scheduler = new SchedulerPro({
    features : {
        nestedEvents : {
            resourceMargin : {
                start : 15,
                end   : 1
            }
        }
    }
});
```

[eventHeight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-eventHeight)
Fixed event height (width in vertical mode) to use when configured with `eventLayout : 'stack'`.

Also accepts an array, used to control height for each level if nesting deeper than 1 level. Make sure you supply a value for each level, where later values are smaller than earlier ones.

```
const scheduler = new SchedulerPro({
    features : {
        nestedEvents : {
        eventHeight : [40, 20]
    }
});
```

[headerHeight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-headerHeight)
Space (in px) in a parent element reserved for displaying a title etc. Used to compute available space for the nested events container inside the parent.

Setting this config updates the `--b-nested-events-header-height` CSS variable.

[constrainDragToParent](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-constrainDragToParent)
Constrains dragging of nested events within their parent when configured as `true`, allows them to be dragged out of it when configured as `false` (the default).

[allowNestingOnDrop](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-allowNestingOnDrop)
Allow an event to be dropped on another to nest it.

Dropping an event on another will add the dropped event as a child of the target, turning the target into a parent if it was not already.

Parent events dropped on another event are ignored.

[allowDeNestingOnDrop](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-allowDeNestingOnDrop)
Allow dropping a nested event directly on a resource to de-nest it, turning it into an ordinary event.

Requires [constrainDragToParent](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-constrainDragToParent) to be configured with `false` to be applicable.

[constrainResizeToParent](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-constrainResizeToParent)
Constrains resizing of nested events to their parents start and end dates when configured as `true` (the default), preventing them from changing their parents dates.

Configure as `false` if you want to allow resizing operations to extend the parents dates (only applies for parents not configured with `manuallyScheduled: true`).

Note that when using \`eventLayout: stack\` the nested events are clipped by the parent, the part extending outside if not constrained to parent will not be shown until it re-renders after resize. If stacking events in your app won't overflow the parent, you can specify \`overflow: visible\` on \`.b-nested-events-container.b-nested-events-layout-stack\` to not clip.

[maxNesting](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#config-maxNesting)
Maximum nesting level for events.

Larger depths than 2 are not recommended, even if technically possible.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isNestedEvents](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-isNestedEvents)
Identifies an object as an instance of [NestedEvents](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents) class, or subclass thereof.

[isNestedEvents](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-isNestedEvents-static)
Identifies an object as an instance of [NestedEvents](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents) class, or subclass thereof.

[eventLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-eventLayout)
This config defines how to handle overlapping nested events. Valid values are:

* `stack`, events use fixed height and stack on top of each other (not supported in vertical mode)
* `pack`, adjusts event height
* `none`, allows events to overlap

Note that stacking works differently for nested events as compared to normal events (and not at all in vertical mode). The height of the parent event will never change, all nested events use [fixed height](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-eventHeight) and will stack until all available space is consumed, after which they will overflow the parent.

Also note that stacked nested events are clipped by the parent, making it scrollable on vertical overflow. This cannot be combined with sticky events. If stacking events in your app won't overflow the parent, you can specify \`overflow: visible\` on \`.b-nested-events-container.b-nested-events-layout-stack\` to not clip and make sticky events work.

[barMargin](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-barMargin)
Vertical (horizontal in vertical mode) space between nested event bars, in px

[resourceMargin](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-resourceMargin)
Control how much space to leave between the first nested event bar/last nested event and the parent event (top/bottom margin within the parent event row in horizontal mode, left/right margin within the parent event column in vertical mode), in px.

It's also possible to set different values for top/left and bottom/right by assigning an object to `resourceMargin` with `start` (margin top in horizontal mode, margin left in vertical mode) and `end` (margin bottom / margin right) properties:

```
scheduler = new SchedulerPro({
    features : {
        nestedEvents : {
            resourceMargin : {
                start : 15,
                end   : 1
            }
        }
    }
});
```

[eventHeight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-eventHeight)
Fixed event height (width in vertical mode) to use when configured with `eventLayout : 'stack'`.

Also accepts an array, used to control height for each level if nesting deeper than 1 level. Make sure you supply a value for each level, where later values are smaller than earlier ones.

```
const scheduler = new SchedulerPro({
    features : {
        nestedEvents : {
        eventHeight : [40, 20]
    }
});
```

[headerHeight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-headerHeight)
Space (in px) in a parent element reserved for displaying a title etc. Used to compute available space for the nested events container inside the parent.

Setting this config updates the `--b-nested-events-header-height` CSS variable.

[constrainDragToParent](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-constrainDragToParent)
Constrains dragging of nested events within their parent when configured as `true`, allows them to be dragged out of it when configured as `false` (the default).

[allowNestingOnDrop](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-allowNestingOnDrop)
Allow an event to be dropped on another to nest it.

Dropping an event on another will add the dropped event as a child of the target, turning the target into a parent if it was not already.

Parent events dropped on another event are ignored.

[allowDeNestingOnDrop](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-allowDeNestingOnDrop)
Allow dropping a nested event directly on a resource to de-nest it, turning it into an ordinary event.

Requires [constrainDragToParent](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/NestedEvents#config-constrainDragToParent) to be configured with `false` to be applicable.

[constrainResizeToParent](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-constrainResizeToParent)
Constrains resizing of nested events to their parents start and end dates when configured as `true` (the default), preventing them from changing their parents dates.

Configure as `false` if you want to allow resizing operations to extend the parents dates (only applies for parents not configured with `manuallyScheduled: true`).

Note that when using \`eventLayout: stack\` the nested events are clipped by the parent, the part extending outside if not constrained to parent will not be shown until it re-renders after resize. If stacking events in your app won't overflow the parent, you can specify \`overflow: visible\` on \`.b-nested-events-container.b-nested-events-layout-stack\` to not clip.

[maxNesting](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/NestedEvents#property-maxNesting)
Maximum nesting level for events.

Larger depths than 2 are not recommended, even if technically possible.
