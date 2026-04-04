# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventMenu.md

# [EventMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu)

Displays a context menu for events. Items are populated by other features and/or application code.

### Default event menu items

Here is the list of menu items provided by the feature and populated by the other features:

Reference

Text

Weight

Feature

Description

`editEvent`

Edit event

100

[EventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit)

Edit event in the event editor. Hidden when read-only

`showDetails`

Edit event

100

[EventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit)

Show event in a non-editable form. Hidden when not read-only

`copyEvent`

Copy event

110

[EventCopyPaste](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste)

Copy event or assignment. Hidden when read-only

`cutEvent`

Cut event

120

[EventCopyPaste](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste)

Cut event or assignment. Hidden when read-only

`unassignEvent`

Unassign event

300

_This feature_

Unassign event. Hidden when read-only, shown for multi-assignment

`deleteEvent`

Delete event

500

_This feature_

Remove event. Hidden when read-only

`splitEvent`

Split event

650

_Scheduler Pro only_

Split an event into two segments at the mouse position

`renameSegment`

Rename segment

660

_Scheduler Pro only_

Show an inline editor to rename the segment

`eventColor` ¹

Color

400

_This feature_

Choose background color for the event bar

**¹** Set [showEventColorPickers](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-showEventColorPickers) to `true` to enable this item

### Customizing the menu items

The menu items in the Event menu can be customized, existing items can be changed or removed, and new items can be added. This is handled using the `items` config of the feature.

Add extra items for all events:

```
const scheduler = new Scheduler({
    features : {
        eventMenu : {
            items : {
                extraItem : {
                    text : 'Extra',
                    icon : 'fa fa-fw fa-flag',
                    onItem({eventRecord}) {
                        eventRecord.flagged = true;
                    }
                }
            }
        }
    }
});
```

Remove existing items:

```
const scheduler = new Scheduler({
    features : {
        eventMenu : {
            items : {
                deleteEvent   : false,
                unassignEvent : false
            }
        }
    }
});
```

Customize existing item:

```
const scheduler = new Scheduler({
    features : {
        eventMenu : {
            items : {
                deleteEvent : {
                    text : 'Delete booking'
                }
            }
        }
    }
});
```

Manipulate existing items for all events or specific events:

```
const scheduler = new Scheduler({
    features : {
        eventMenu : {
            // Process items before menu is shown
            processItems({eventRecord, items}) {
                 // Push an extra item for conferences
                 if (eventRecord.type === 'conference') {
                     items.showSessionItem = {
                         text : 'Show sessions',
                         onItem({eventRecord}) {
                             // ...
                         }
                     };
                 }

                 // Do not show menu for secret events
                 if (eventRecord.type === 'secret') {
                     return false;
                 }
            }
        }
    }
});
```

The `processItems` implementation may be an `async` function which `awaits` a result to mutate the `items` object.

Note that the [menuContext](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventMenu#property-menuContext) is applied to the Menu's `item` event, so your `onItem` handler's single event parameter also contains the following properties:

* **source** The [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler) whose UI was right-clicked.
* **targetElement** The element right-clicked on.
* **eventRecord** The [event record](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) clicked on.
* **resourceRecord** The [resource record](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel) clicked on.
* **assignmentRecord** The [assignment record](https://bryntum.com/docs/gantt/api/#Scheduler/model/AssignmentModel) clicked on.

Video guides
------------

[@youtube](https://bryntum.com/docs/gantt/api/https://youtube.com/embed/dEnpeZvC4Rc)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/HAq12QUBMx8)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/nXMaClkkKdQ)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/0seuhWrIeXc)

Full information of the menu customization can be found in the "Customizing the Event menu, the Schedule menu, and the TimeAxisHeader menu" guide.

This feature is **enabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[processItems](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#config-processItems)
A function called before displaying the menu that allows manipulations of its items. Returning `false` from this function prevents the menu being shown.

```
features         : {
   eventMenu : {
        processItems({ items, eventRecord, assignmentRecord, resourceRecord }) {
            // Add or hide existing items here as needed
            items.myAction = {
                text   : 'Cool action',
                icon   : 'fa fa-fw fa-ban',
                onItem : () => console.log(`Clicked ${eventRecord.name}`),
                weight : 1000 // Move to end
            };

           if (!eventRecord.allowDelete) {
                items.deleteEvent.hidden = true;
            }
        }
    }
},
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#property-isEventMenu)
Identifies an object as an instance of [EventMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventMenu) class, or subclass thereof.

[isEventMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#property-isEventMenu-static)
Identifies an object as an instance of [EventMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventMenu) class, or subclass thereof.

[menuContext](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#property-menuContext)
An informational object containing contextual information about the last activation of the context menu.

## Functions

Functions are methods available for calling on the class

[showContextMenuFor](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#function-showContextMenuFor)
Shows context menu for the provided event. If record is not rendered (outside of time span/filtered) menu won't appear.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[eventMenuBeforeShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#event-eventMenuBeforeShow)
This event fires on the owning Scheduler before the context menu is shown for an event. Allows manipulation of the items to show in the same way as in `processItems`. Returning `false` from a listener prevents the menu from being shown.

[eventMenuItem](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#event-eventMenuItem)
This event fires on the owning Scheduler when an item is selected in the context menu.

[eventMenuShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#event-eventMenuShow)
This event fires on the owning Scheduler after showing the context menu for an event

## Typedefs

Typedefs are type definitions for the class

[SchedulerMenuContext](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventMenu#typedef-SchedulerMenuContext)
A context object passed to any `processItems` method defined for a context menu feature, and the basis of events fired by context menu features.
