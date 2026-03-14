# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/ScheduleMenu.md

# [ScheduleMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleMenu)

Displays a context menu for empty parts of the schedule. Items are populated in the first place by configurations of this Feature, then by other features and/or application code.

### Default scheduler zone menu items

The Scheduler menu feature provides only one item:

Reference

Text

Weight

Feature

Description

`addEvent`

Add event

100

_This feature_

Add new event at the target time and resource. Hidden when read-only

`pasteEvent`

Paste event

110

[EventCopyPaste](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste)

Paste event at the target time and resource. Hidden when is read-only

`splitSchedule`

Split

200

[Split](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Split)

Shows the "Split schedule" sub-menu

\> `splitHorizontally`

Horizontally

100

[Split](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Split)

Split horizontally

\> `splitVertically`

Vertically

200

[Split](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Split)

Split vertically

\> `splitBoth`

Both

300

[Split](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Split)

Split both ways

`unsplitSchedule`

Split

210

[Split](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Split)

Unsplit a previously split schedule

\>

first level of submenu

### Customizing the menu items

The menu items in the Scheduler menu can be customized, existing items can be changed or removed, and new items can be added. This is handled using the `items` config of the feature.

Add extra item:

```
const scheduler = new Scheduler({
    features : {
        scheduleMenu : {
            items : {
                extraItem : {
                    text : 'Extra',
                    icon : 'fa fa-fw fa-flag',
                    onItem({date, resourceRecord, items}) {
                        // Custom date based action
                    }
                }
            }
        }
    }
});
```

Remove existing item:

```
const scheduler = new Scheduler({
    features : {
        scheduleMenu : {
            items : {
                addEvent : false
            }
        }
    }
});
```

Customize existing item:

```
const scheduler = new Scheduler({
    features : {
        scheduleMenu : {
            items : {
                addEvent : {
                    text : 'Create new booking'
                }
            }
        }
    }
});
```

Manipulate existing items:

```
const scheduler = new Scheduler({
    features : {
        scheduleMenu : {
            // Process items before menu is shown
            processItems({date, resourceRecord, items}) {
                 // Add an extra item for ancient times
                 if (date < new Date(2018, 11, 17)) {
                     items.modernize = {
                         text : 'Modernize',
                         ontItem({ date }) {
                             // Custom date based action
                         }
                     };
                 }

                 // Do not show menu for Sundays
                 if (date.getDay() === 0) {
                     return false;
                 }
            }
        }
    }
});
```

The \`processItems\` implementation my be an \`async\` function which \`awaits\` a result to mutate the \`items\` object.

Video guides
------------

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/dEnpeZvC4Rc)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/HAq12QUBMx8)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/nXMaClkkKdQ)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/0seuhWrIeXc)

Full information of the menu customization can be found in the ["Customizing the Event menu, the Schedule menu, and the TimeAxisHeader menu"](https://bryntum.com/docs/gantt/api/#Scheduler/guides/customization/contextmenu.md) guide.

This feature is **enabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[items](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleMenu#config-items)
This is a preconfigured set of items used to create the default context menu.

The `items` provided by this feature are listed below. These are the predefined property names which you may configure:

* `addEvent` Add an event for at the resource and time indicated by the `contextmenu` event.

To remove existing items, set corresponding keys `null`:

```
const scheduler = new Scheduler({
    features : {
        scheduleMenu : {
            items : {
                addEvent : null
            }
        }
    }
});
```

[processItems](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleMenu#config-processItems)
A function called before displaying the menu that allows manipulations of its items. Returning `false` from this function prevents the menu being shown.

```
features         : {
   scheduleMenu : {
        processItems({ items, date, resourceRecord }) {
           // Add or hide existing items here as needed
           items.myAction = {
               text   : 'Cool action',
               icon   : 'fa fa-cat',
               onItem : () => console.log(`Clicked on ${resourceRecord.name} at ${date}`),
               weight : 1000 // Move to end
           };

           if (!resourceRecord.allowAdd) {
               items.addEvent.hidden = true;
           }
       }
   }
},
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isScheduleMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleMenu#property-isScheduleMenu)
Identifies an object as an instance of [ScheduleMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleMenu) class, or subclass thereof.

[isScheduleMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleMenu#property-isScheduleMenu-static)
Identifies an object as an instance of [ScheduleMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleMenu) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[scheduleMenuBeforeShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleMenu#event-scheduleMenuBeforeShow)
This event fires on the owning Scheduler or Gantt widget before the context menu is shown for the schedule. Allows manipulation of the items to show in the same way as in `processItems`. Returning `false` from a listener prevents the menu from being shown.

[scheduleMenuItem](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleMenu#event-scheduleMenuItem)
This event fires on the owning Scheduler or Gantt widget when an item is selected in the context menu.

[scheduleMenuShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleMenu#event-scheduleMenuShow)
This event fires on the owning Scheduler or Gantt widget after showing the context menu for the schedule.
