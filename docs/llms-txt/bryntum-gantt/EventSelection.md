# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/EventSelection.md

# [EventSelection](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection)

Mixin that tracks event or assignment selection by clicking on one or more events in the scheduler.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[highlightPredecessors](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-highlightPredecessors)
Configure as `true`, or set property to `true` to highlight dependent events as well when selecting an event.

[highlightSuccessors](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-highlightSuccessors)
Configure as `true`, or set property to `true` to highlight dependent events as well when selecting an event.

[deselectOnClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-deselectOnClick)
Configure as `true` to deselect a selected event upon click.

[deselectAllOnScheduleClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-deselectAllOnScheduleClick)
Configure as `false` to preserve selection when clicking the empty schedule area.

[selectResourceOnEventNavigate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-selectResourceOnEventNavigate)
Set to `false` to not select the resource of the event when clicking an event bar.

[selectResourceOnScheduleClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-selectResourceOnScheduleClick)
Set to `false` to not select the row/resource when clicking the empty area in a time axis cell.

[selectedCollection](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-selectedCollection)
Collection to store selection.

[multiEventSelect](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-multiEventSelect)
Configure as `true` to allow `CTRL/CMD+click` to select multiple events in the scheduler.

Or pass an object to control which modifier keys to use for multi selection.

[eventSelectionDisabled](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-eventSelectionDisabled)
Configure as `true`, or set property to `true` to disable event selection.

[eventSelectedCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-eventSelectedCls)
CSS class to add to selected events.

[triggerSelectionChangeOnRemove](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-triggerSelectionChangeOnRemove)
Configure as `true` to trigger `selectionChange` when removing a selected event/assignment.

[maintainSelectionOnDatasetChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-maintainSelectionOnDatasetChange)
This flag controls whether Scheduler should preserve its selection of events when loading a new dataset (if selected event ids are included in the newly loaded dataset).

[eventAssignHighlightCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-eventAssignHighlightCls)
CSS class to add to other instances of a selected event, to highlight them.

[isEventSelectable](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#config-isEventSelectable)
A template method (empty by default) allowing you to control if an event can be selected or not.

```
new Scheduler({
    isEventSelectable(event) {
        return event.startDate >= Date.now();
    }
})
```

This selection process is applicable to calendar too:

```
new Calendar({
    isEventSelectable(event) {
        return event.startDate >= Date.now();
    }
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventSelection](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#property-isEventSelection)
Identifies an object as an instance of [EventSelection](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/EventSelection) class, or subclass thereof.

[isEventSelection](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#property-isEventSelection-static)
Identifies an object as an instance of [EventSelection](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/EventSelection) class, or subclass thereof.

[selectResourceOnEventNavigate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#property-selectResourceOnEventNavigate)
Set to `false` to not select the resource of the event when clicking an event bar.

[selectResourceOnScheduleClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#property-selectResourceOnScheduleClick)
Set to `false` to not select the row/resource when clicking the empty area in a time axis cell.

[selectedEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#property-selectedEvents)
The [events](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) which are selected.

[selectedAssignments](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#property-selectedAssignments)
The [events](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) which are selected.

[isEventSelectable](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#property-isEventSelectable)
A template method (empty by default) allowing you to control if an event can be selected or not.

```
new Scheduler({
    isEventSelectable(event) {
        return event.startDate >= Date.now();
    }
})
```

This selection process is applicable to calendar too:

```
new Calendar({
    isEventSelectable(event) {
        return event.startDate >= Date.now();
    }
})
```

## Functions

Functions are methods available for calling on the class

[isEventSelected](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-isEventSelected)
Returns `true` if the [event](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) is selected.

[isAssignmentSelected](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-isAssignmentSelected)
Returns `true` if the [assignment](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) is selected.

[select](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-select)
Selects the passed [event](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) or [assignment](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) _if it is not selected_. Selecting events results in all their assignments being selected.

[selectEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-selectEvent)
Selects the passed [event](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) _if it is not selected_. Selecting an event will select all its assignments.

[selectAssignment](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-selectAssignment)
Selects the passed [assignment](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) _if it is not selected_.

[deselect](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-deselect)
Deselects the passed [event](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) or [assignment](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) _if it is selected_.

[deselectEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-deselectEvent)
Deselects the passed [event](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) _if it is selected_.

[deselectAssignment](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-deselectAssignment)
Deselects the passed [assignment](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) _if it is selected_.

[selectEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-selectEvents)
Adds [events](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) to the selection.

[deselectEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-deselectEvents)
Removes [events](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) from the selection.

[selectAssignments](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-selectAssignments)
Adds [assignments](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) to the selection.

[deselectAssignments](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-deselectAssignments)
Removes [assignments](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) from the selection.

[clearEventSelection](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-clearEventSelection)
Deselects all [events](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) and [assignments](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel).

[onBeforeSelectedCollectionSplice](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-onBeforeSelectedCollectionSplice)
Responds to mutations of the underlying selection Collection. Keeps the UI synced, eventSelectionChange and assignmentSelectionChange event is fired when `me.silent` is falsy.

[onAssignmentChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-onAssignmentChange)
Assignment change listener to remove events from selection which are no longer in the assignments.

[onAssignmentSelectionClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-onAssignmentSelectionClick)
Mouse listener to update selection.

[onEventNavigate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#function-onEventNavigate)
Navigation listener to update selection.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[eventSelectionChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#event-eventSelectionChange)
Fired any time there is a change to the events selected in the Scheduler.

[beforeEventSelectionChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#event-beforeEventSelectionChange)
Fired any time there is going to be a change to the events selected in the Scheduler. Returning `false` prevents the change

[assignmentSelectionChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#event-assignmentSelectionChange)
Fired any time there is a change to the assignments selected in the Scheduler.

[beforeAssignmentSelectionChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventSelection#event-beforeAssignmentSelectionChange)
Fired any time there is going to be a change to the assignments selected in the Scheduler. Returning `false` prevents the change
