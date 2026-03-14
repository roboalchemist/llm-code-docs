# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/SimpleEventEdit.md

# [SimpleEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit)

Feature that displays a text field to edit the event name.

You can control the flow of this by listening to the events relayed by this class from the underlying [Editor](https://bryntum.com/docs/gantt/api/#Core/widget/Editor).

To use this feature, you also need to disable the built-in default editing feature:

```
const scheduler = new Scheduler({
    features : {
        eventEdit       : false,
        simpleEventEdit : true
    }
});
```

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[triggerEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#config-triggerEvent)
The event that shall trigger showing the editor. Defaults to `eventDblClick`, set to `''` or `null` to disable editing of existing events.

[field](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#config-field)
The [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) field to edit

[editorConfig](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#config-editorConfig)
The editor configuration, where you can control which widget to show

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSimpleEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#property-isSimpleEventEdit)
Identifies an object as an instance of [SimpleEventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/SimpleEventEdit) class, or subclass thereof.

[isSimpleEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#property-isSimpleEventEdit-static)
Identifies an object as an instance of [SimpleEventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/SimpleEventEdit) class, or subclass thereof.

[eventRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#property-eventRecord)
The current [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) record, which is being edited by the event editor.

## Functions

Functions are methods available for calling on the class

[editEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#function-editEvent)
Opens an Editor for the passed event. This function is exposed on Scheduler and can be called as `scheduler.editEvent()`.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeStart](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#event-beforeStart)
Fired before the editor is shown to start an edit operation. Returning `false` from a handler vetoes the edit operation.

[start](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#event-start)
Fired when an edit operation has begun.

[beforeComplete](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#event-beforeComplete)
Fired when an edit completion has been requested, either by `ENTER`, or focus loss (if configured to complete on blur). The completion may be vetoed, in which case, focus is moved back into the editor.

[complete](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#event-complete)
Edit has been completed, and any associated record or element has been updated.

[beforeCancel](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#event-beforeCancel)
Fired when cancellation has been requested, either by `ESC`, or focus loss (if configured to cancel on blur). The cancellation may be vetoed, in which case, focus is moved back into the editor.

[cancel](https://bryntum.com/docs/gantt/api/Scheduler/feature/SimpleEventEdit#event-cancel)
Edit has been canceled without updating the associated record or element.
