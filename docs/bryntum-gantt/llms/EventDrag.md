# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventDrag.md

# [EventDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag)

Allows user to drag and drop events within the scheduler, to change `startDate` or resource assignment.

This feature is **enabled** by default

Customizing the drag drop tooltip
---------------------------------

To show custom HTML in the tooltip, please see the [tooltipTemplate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-tooltipTemplate) config. Example:

```
features: {
    eventDrag : {
        // A minimal start date tooltip
        tooltipTemplate : ({ eventRecord, startDate }) => {
            return DateHelper.format(startDate, 'HH:mm');
        }
    }
}
```

Constraining the drag drop area
-------------------------------

You can constrain how the dragged event is allowed to move by using the following configs

* [constrainDragToResource](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-constrainDragToResource) Resource fixed, only allowed to change start date
* [constrainDragToTimeSlot](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-constrainDragToTimeSlot) Start date is fixed, only move between resources
* [getDateConstraints](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-getDateConstraints) A method on the Scheduler instance which lets you define the date range for the dragged event programmatically

```
// Enable dragging + constrain drag to current resource
const scheduler = new Scheduler({
    features : {
        eventDrag : {
            constrainDragToResource : true
        }
    }
});
```

Drag drop events from outside
-----------------------------

Dragging unplanned events from an external grid is a very popular use case. There are several demos showing you how to do this. Please see the [Drag from grid demo](https://bryntum.com/docs/gantt/api/../examples/dragfromgrid) and study the **Drag from grid guide** to learn more.

Drag drop events to outside target
----------------------------------

You can also drag events outside the schedule area by setting [constrainDragToTimeline](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-constrainDragToTimeline) to `false`. You should also either:

* provide a [validatorFn](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-validatorFn) to programmatically define if a drop location is valid or not
* configure a [externalDropTargetSelector](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-externalDropTargetSelector) CSS selector to define where drops are allowed

See [this demo](https://bryntum.com/docs/gantt/api/../examples/drag-outside) to see this in action.

Validating drag drop
--------------------

It is easy to programmatically decide what is a valid drag drop operation. Use the [validatorFn](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-validatorFn) and return either `true` / `false` (optionally a message to show to the user).

```
features : {
    eventDrag : {
       validatorFn({ eventRecords, newResource }) {
           const task  = eventRecords[0],
                 valid = newResource.role === task.resource.role;

           return {
               valid   : newResource.role === task.resource.role,
               message : valid ? '' : 'Resource role does not match required role for this task'
           };
       }
    }
}
```

See [this demo](https://bryntum.com/docs/gantt/api/../examples/validation) to see validation in action.

If you instead want to do a single validation upon drop, you can listen to [beforeEventDropFinalize](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#event-beforeEventDropFinalize) and set the `valid` flag on the context object provided.

```
  const scheduler = new Scheduler({
     listeners : {
         beforeEventDropFinalize({ context }) {
             const { eventRecords } = context;
             // Don't allow dropping events in the past
             context.valid = Date.now() <= eventRecords[0].startDate;
         }
     }
 });
```

Preventing drag of certain events
---------------------------------

To prevent certain events from being dragged, you have two options. You can set [draggable](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-draggable) to `false` in your data, or you can listen for the [beforeEventDrag](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#event-beforeEventDrag) event and return `false` to block the drag.

```
new Scheduler({
   listeners : {
       beforeEventDrag({ eventRecord }) {
           // Don't allow dragging events that have already started
           return Date.now() <= eventRecord.startDate;
       }
   }
})
```

Events that are selected, but not visually accessible, are not included in drag operations. This means that events in collapsed groups or filtered out resources are not dragged, even if they were selected prior to being collapsed or filtered out of visibility.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-tooltipTemplate)
Template used to generate drag tooltip contents.

```
const scheduler = new Scheduler({
    features : {
        eventDrag : {
            tooltipTemplate({eventRecord, startText}) {
                return `${eventRecord.name}: ${startText}`
            }
        }
    }
});
```

[singleDirection](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-singleDirection)
Set to `true` to only allow dragging in one direction (based on initial movement)

[constrainDragToResource](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-constrainDragToResource)
Set to true to only allow dragging events within the same resource.

[constrainDragToTimeSlot](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-constrainDragToTimeSlot)
Set to true to only allow dragging events to different resources, and disallow rescheduling by dragging.

[externalDropTargetSelector](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-externalDropTargetSelector)
A CSS selector specifying elements outside the scheduler element which are valid drop targets.

[validatorFn](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-validatorFn)
An empty function by default, but provided so that you can perform custom validation on the item being dragged. This function is called during the drag and drop process and also after the drop is made. Return `true` if the new position is valid, `false` to prevent the drag.

```
features : {
    eventDrag : {
        validatorFn({ eventRecords, newResource }) {
            const
                task  = eventRecords[0],
                valid = newResource.role === task.resource.role;

            return {
                valid   : newResource.role === task.resource.role,
                message : valid ? '' : 'Resource role does not match required role for this task'
            };
        }
    }
}
```

[validatorFnThisObj](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-validatorFnThisObj)
The `this` reference for the validatorFn

[unifiedDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-unifiedDrag)
When the host Scheduler is `[multiEventSelect](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/EventSelection#config-multiEventSelect): true` then, there are two modes of dragging _within the same Scheduler_.

Non unified means that all selected events are dragged by the same number of resource rows.

Unified means that all selected events are collected together and dragged as one, and are all dropped on the same targeted resource row at the same targeted time.

[snapToPosition](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-snapToPosition)
A hook that allows manipulating the position the drag proxy snaps to. Manipulate the `snapTo` property to alter snap position.

```
const scheduler = new Scheduler({
    features : {
        eventDrag : {
            snapToPosition({ eventRecord, snapTo }) {
                if (eventRecord.late) {
                    snapTo.x = 400;
                }
            }
        }
    }
});
```

[snapToResource](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-snapToResource)
Defaults to `true`, which snaps events to resources while dragging, i.e. vertical row snap in horizontal mode and vice versa. Requires Scheduler to be configured to [snap](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-snap) to have any effect:

```
const scheduler = new Scheduler({
    ...
    // Snap to time & resource
    snap : true
});
```

If you want to customize the number of pixels from the dragged event that will trigger the snapping behavior to the new resource, you can set the `threshold` property:

```
const scheduler = new Scheduler({
    ...
    snap     : true,
    features : {
        eventDrag : {
            // Customized snap threshold
            snapToResource : {
                threshold : 30
            }
        }
    },
    ...
});
```

[copyKey](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-copyKey)
A modifier key (CTRL, SHIFT, ALT, META) that when pressed will copy an event instead of moving it. Set to empty string to disable copying. Defaults to "CTRL" which is the Ctrl-key for Windows, and Meta-key for MacOS.

[copyMode](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-copyMode)
Event can be copied two ways: either by adding new assignment to an existing event ('assignment'), or by copying the event itself ('event'). 'auto' mode will pick 'event' for a single-assignment mode (when event has `resourceId` field) and 'assignment' mode otherwise.

[alwaysCopy](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#config-alwaysCopy)
Set this to `true` to always copy the event on drag drop operation.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-isEventDrag)
Identifies an object as an instance of [EventDrag](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag) class, or subclass thereof.

[isEventDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-isEventDrag-static)
Identifies an object as an instance of [EventDrag](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag) class, or subclass thereof.

[singleDirection](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-singleDirection)
Set to `true` to only allow dragging in one direction (based on initial movement)

[constrainDragToResource](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-constrainDragToResource)
Set to true to only allow dragging events within the same resource.

[constrainDragToTimeSlot](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-constrainDragToTimeSlot)
Set to true to only allow dragging events to different resources, and disallow rescheduling by dragging.

[unifiedDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-unifiedDrag)
When the host Scheduler is `[multiEventSelect](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/EventSelection#config-multiEventSelect): true` then, there are two modes of dragging _within the same Scheduler_.

Non unified means that all selected events are dragged by the same number of resource rows.

Unified means that all selected events are collected together and dragged as one, and are all dropped on the same targeted resource row at the same targeted time.

[snapToResource](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-snapToResource)
Defaults to `true`, which snaps events to resources while dragging, i.e. vertical row snap in horizontal mode and vice versa. Requires Scheduler to be configured to [snap](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-snap) to have any effect:

```
const scheduler = new Scheduler({
    ...
    // Snap to time & resource
    snap : true
});
```

If you want to customize the number of pixels from the dragged event that will trigger the snapping behavior to the new resource, you can set the `threshold` property:

```
const scheduler = new Scheduler({
    ...
    snap     : true,
    features : {
        eventDrag : {
            // Customized snap threshold
            snapToResource : {
                threshold : 30
            }
        }
    },
    ...
});
```

[copyKey](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-copyKey)
A modifier key (CTRL, SHIFT, ALT, META) that when pressed will copy an event instead of moving it. Set to empty string to disable copying. Defaults to "CTRL" which is the Ctrl-key for Windows, and Meta-key for MacOS.

[copyMode](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-copyMode)
Event can be copied two ways: either by adding new assignment to an existing event ('assignment'), or by copying the event itself ('event'). 'auto' mode will pick 'event' for a single-assignment mode (when event has `resourceId` field) and 'assignment' mode otherwise.

[mode](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-mode)
Mode of the current drag drop operation.

[alwaysCopy](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#property-alwaysCopy)
Set this to `true` to always copy the event on drag drop operation.

## Functions

Functions are methods available for calling on the class

[isValidDrop](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#function-isValidDrop)
Checks if an event can be dropped on the specified position.

[updateRecords](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#function-updateRecords)
Update events being dragged.

[updateAssignments](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#function-updateAssignments)
Update assignments being dragged

[getDragData](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#function-getDragData)
Initializes drag data (dates, constraints, dragged events etc). Called when drag starts.

[getRelatedRecords](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#function-getRelatedRecords)
Provide your custom implementation of this to allow additional selected records to be dragged together with the original one.

[getCoordinate](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#function-getCoordinate)
Get correct axis coordinate depending on schedulers mode (horizontal -> x, vertical -> y). Also takes milestone layout into account.

[resolveResource](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#function-resolveResource)
Get resource record occluded by the drag proxy.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[eventDragModeChange](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-eventDragModeChange)
Triggered when drag mode is changed, for example when copy key is pressed or released while dragging.

[beforeEventDropFinalize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-beforeEventDropFinalize)
This event is fired on the owning Scheduler after the event drag operation completes, but before changing any data. It allows implementer to use asynchronous validation/finalization by setting `context.async = true` in the listener, for example, to show a confirmation popup, make async data request etc. In such case, implementer need to call the `context.finalize()` method manually:

```
 scheduler.on('beforeeventdropfinalize', ({ context }) => {
     context.async = true;
     setTimeout(() => {
         // `true` to perform the drop, `false` to ignore it
         context.finalize(true);
     }, 1000);
 })
```

For synchronous one-time validation, simply set `context.valid` to true or false.

```
 scheduler.on('beforeeventdropfinalize', ({ context }) => {
     context.valid = false;
 })
```

[afterEventDrop](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-afterEventDrop)
Fired on the owning Scheduler after event drop

[eventDrop](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-eventDrop)
Fired on the owning Scheduler when an event is dropped

[beforeEventDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-beforeEventDrag)
Fired on the owning Scheduler before event dragging starts. Return `false` to prevent the action.

[eventDragStart](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-eventDragStart)
Fired on the owning Scheduler when event dragging starts

[eventDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-eventDrag)
Fired on the owning Scheduler when event is dragged

[eventDragAbort](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-eventDragAbort)
Fired on the owning Scheduler after an event drag operation has been aborted

[eventDragReset](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#event-eventDragReset)
Fired on the owning Scheduler after an event drag operation regardless of the operation being cancelled or not

## Typedefs

Typedefs are type definitions for the class

[EventDropData](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#typedef-EventDropData)
Object with information about the drop point for a single dragged event.

[AssignmentDropData](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#typedef-AssignmentDropData)
Object with information about the drop point for a dragged assignment.

[DropData](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDrag#typedef-DropData)
Object with information about the drop points for the dragged events. It is used in the Scheduler's [beforeEventDropFinalize](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#event-beforeEventDropFinalize) event.
