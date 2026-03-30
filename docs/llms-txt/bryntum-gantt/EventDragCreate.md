# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventDragCreate.md

# [EventDragCreate](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate)

Feature that allows the user to create new events by dragging in empty parts of the scheduler rows.

This feature is **enabled** by default.

Incompatible with the [EventDragSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragSelect) and [Pan](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Pan) features. If either of those features are enabled, this feature has no effect.

Conditionally preventing drag creation
--------------------------------------

To conditionally prevent drag creation for a certain resource or a certain timespan, you listen for the [beforeDragCreate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragCreate#event-beforeDragCreate) event, add your custom logic to it and return `false` to prevent the operation from starting. For example to not allow drag creation on the topmost resource:

```
const scheduler = new Scheduler({
    listeners : {
        beforeDragCreate({ resource }) {
            // Prevent drag creating on the topmost resource
            if (resource === scheduler.resourceStore.first) {
                return false;
            }
        }
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[lockLayout](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#config-lockLayout)
Locks the layout during drag create, overriding the default behaviour that uses the same rendering pathway for drag creation as for already existing events.

This more closely resembles the behaviour of versions prior to 4.2.0.

Enabling this config also leads to cheaper drag creation, only the events of the affected resource are refreshed during the operation.

For even cheaper drag creation, configure it as `'minimal-updates'`. In this mode, no other events are updated during the operation.

[validatorFn](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#config-validatorFn)
An empty function by default, but provided so that you can perform custom validation on the event being created. Return `true` if the new event is valid, `false` to prevent an event being created.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventDragCreate](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#property-isEventDragCreate)
Identifies an object as an instance of [EventDragCreate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragCreate) class, or subclass thereof.

[isEventDragCreate](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#property-isEventDragCreate-static)
Identifies an object as an instance of [EventDragCreate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragCreate) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[createEventRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#function-createEventRecord)
Creates an event by the event object coordinates

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[dragCreateEnd](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#event-dragCreateEnd)
Fires on the owning Scheduler after the new event has been created.

[beforeDragCreate](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#event-beforeDragCreate)
Fires on the owning Scheduler at the beginning of the drag gesture. Returning `false` from a listener prevents the drag create operation from starting.

```
const scheduler = new Scheduler({
    listeners : {
        beforeDragCreate({ date }) {
            // Prevent drag creating events in the past
            return date >= Date.now();
        }
    }
});
```

[dragCreateStart](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#event-dragCreateStart)
Fires on the owning Scheduler after the drag start has created a new Event record.

[beforeDragCreateFinalize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#event-beforeDragCreateFinalize)
Fires on the owning Scheduler to allow implementer to prevent immediate finalization by setting `data.context.async = true` in the listener, to show a confirmation popup etc.

```
 scheduler.on('beforeDragCreateFinalize', ({context}) => {
     context.async = true;
     setTimeout(() => {
         // async code don't forget to call finalize
         context.finalize();
     }, 1000);
 })
```

Note that at this point the new `eventRecord` does not yet have the dates set, you can instead find the dates in the context object.

[afterDragCreate](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragCreate#event-afterDragCreate)
Fires on the owning Scheduler at the end of the drag create gesture whether or not a new event was created by the gesture.
