# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/mixin/EventModelMixin.md

# [EventModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin)

Mixin that holds configuration shared between events in Scheduler and Scheduler Pro.

## Fields

Fields belong to a Model class and define the Model data structure

[startDate](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-startDate)
The start date of a time span (or Event / Task).

Uses [DateHelper.defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static) to convert a supplied string to a Date. To specify another format, either change that setting or subclass TimeSpan and change the dateFormat for this field.

UI fields representing this data field are disabled for summary tasks. See [isEditable](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#function-isEditable) for details.

Note that the field always returns a `Date`.

Also note that modifying the `startDate` at runtime will move the event in time, without affecting its duration (with reservation for other scheduling logic affecting the duration). If you want to change the `startDate` and `duration`, use [setStartDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#function-setStartDate) instead (passing `false` as the second argument).

[endDate](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-endDate)
The end date of a time span (or Event / Task).

Uses [DateHelper.defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static) to convert a supplied string to a Date. To specify another format, either change that setting or subclass TimeSpan and change the dateFormat for this field.

UI fields representing this data field are disabled for summary tasks. See [isEditable](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#function-isEditable) for details.

Note that the field always returns a `Date`.

[duration](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-duration)
The numeric part of the timespan's duration (the number of units).

UI fields representing this data field are disabled for summary tasks. See [isEditable](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#function-isEditable) for details.

[fullDuration](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-fullDuration)
Calculated field which encapsulates the duration's magnitude and unit. This field will not be persisted, setting it will update the [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-duration) and [durationUnit](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-durationUnit) fields.

UI fields representing this data field are disabled for summary tasks. See [isEditable](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#function-isEditable) for details.

[id](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-id)
The unique identifier of a task (mandatory)

[resourceId](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-resourceId)
Id of the resource this event is associated with (only usable for single assignments). We recommend using assignments in an AssignmentStore over this approach. Internally any Event using `resourceId` will have an assignment in AssignmentStore generated.

[resourceIds](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-resourceIds)
Ids of the resources this event is associated with (can be used for for multiple assignments). Any event using `resourceIds` will have assignments in AssignmentStore generated automatically. It only applies if is configured with `persist: true`.

```
  class CustomEventModel extends EventModel {
      static $name = 'CustomEventModel';

      static get fields() {
          return [
              { name : 'resourceIds', persist : true }
          ];
      }
  };

  const
      resources   = [
          { id : 'r1', name : 'Celia' },
          { id : 'r2', name : 'Lee' },
          { id : 'r3', name : 'Macy' },
          { id : 'r4', name : 'Madison' }
      ],
      events      = [
          {
              id          : 1,
              resourceIds : ['r1', 'r2']
              ...
          },
          {
              id          : 2,
              resourceIds : ['r3', 'r4']
              ...
          }
      ];

  const scheduler = new Scheduler({
      ...
      eventStore : {
          modelClass : CustomEventModel,
          data       : events
      },
      ...
  });
```

[resources](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-resources)
The array of [resources](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel) which are assigned to this event.

[draggable](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-draggable)
Specify false to prevent the event from being dragged (if EventDrag feature is used)

[resizable](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-resizable)
Specify `false` to prevent the event from being resized (if EventResize feature is used). You can also specify `'start'` or `'end'` to only allow resizing in one direction

[allDay](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-allDay)
A field marking event as all day(s) spanning event. For example, a holiday day may be represented by a `startDate`, and the `allDay` flag.

[eventStyle](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-eventStyle)
Controls this events appearance, see Schedulers [eventStyle config](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-eventStyle) for available options.

[eventColor](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-eventColor)
Controls the primary color of the event. For available standard colors, see [EventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#typedef-EventColor).

[milestoneWidth](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-milestoneWidth)
Width (in px) to use for this milestone when using Scheduler#milestoneLayoutMode 'data'.

[stickyContents](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#field-stickyContents)
Set this field to `false` to opt out of [sticky event content](https://bryntum.com/docs/gantt/api/#Scheduler/feature/StickyEvents) (keeping event text in view while scrolling).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-isEventModelMixin)
Identifies an object as an instance of [EventModelMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin) class, or subclass thereof.

[isEventModelMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-isEventModelMixin-static)
Identifies an object as an instance of [EventModelMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin) class, or subclass thereof.

[resources](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-resources)
Returns all resources assigned to an event.

[isDraggable](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-isDraggable)
Returns true if event can be drag and dropped

[isResizable](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-isResizable)
Returns true if event can be resized, but can additionally return 'start' or 'end' indicating how this event can be resized.

Milestones and parent events (that are not manuallyScheduled) cannot be resized.

[isPersistable](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-isPersistable)
Returns `false` if the event is not persistable. By default it always is, override this getter if you need custom logic.

[persistableData](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-persistableData)
Override persistable getter to prevent sending resourceId when using multiple resource assignment mode https://github.com/bryntum/support/issues/1345

[resource](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-resource)
Returns the first assigned resource, or assigns a resource

[assignments](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-assignments)
Returns all assignments for the event. Event must be part of the store for this method to work.

[predecessors](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-predecessors)
Returns all predecessor dependencies of this event

[successors](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-successors)
Returns all successor dependencies of this event

[isInterDay](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#property-isInterDay)
Flag which indicates that this event is an interday event. This means that it spans an entire day or multiple days.

This is essentially used by the Calendar package to determine if an event should go into the all day zone of a DayView.

## Functions

Functions are methods available for calling on the class

[setAsync](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-setAsync)
Set value for the specified field(s), triggering engine calculations immediately. See [Model#set()](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-set) for arguments.

```
eventRecord.set('duration', 4);
// eventRecord.endDate is not yet calculated

await eventRecord.setAsync('duration', 4);
// eventRecord.endDate is calculated
```

[forEachResource](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-forEachResource)
Iterate over all associated resources

[getResource](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-getResource)
Returns either the resource associated with this event (when called w/o `resourceId`) or resource with specified id.

[shift](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-shift)
Shift the dates for the date range by the passed amount and unit

[assign](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-assign)
Assigns this event to the specified resource.

_Note:_ The event must be part of an EventStore for this to work. If the EventStore uses single assignment (loaded using resourceId) existing assignments will always be removed.

[unassign](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-unassign)
Unassigns this event from the specified resource

[reassign](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-reassign)
Reassigns an event from an old resource to a new resource

[isAssignedTo](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-isAssignedTo)
Returns true if this event is assigned to a certain resource.

[isEditable](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#function-isEditable)
Defines if the given event field should be manually editable in UI. You can override this method to provide your own logic.

By default, the method defines [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-endDate), [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-duration) and [fullDuration](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-fullDuration) fields editable for leaf events only (in case the event is part of a tree store) and all other fields as editable.

## Typedefs

Typedefs are type definitions for the class

[EventColor](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/EventModelMixin#typedef-EventColor)
Predefined named colors:

red

pink

magenta

purple

violet

deep-purple

indigo

blue

light-blue

cyan

teal

green

light-green

lime

yellow

orange

amber

deep-orange

light-gray

gray

black
