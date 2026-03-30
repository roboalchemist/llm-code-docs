# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/TimeAxisHeaderMenu.md

# [TimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeAxisHeaderMenu)

Adds scheduler specific menu items to the timeline header context menu.

Default time axis header menu items
-----------------------------------

Here is the list of menu items provided by this and other features:

Reference

Text

Weight

Feature

Description

`eventsFilter`

Filter tasks

100

[EventFilter](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventFilter)

Submenu for event filtering

\>`nameFilter`

By name

110

[EventFilter](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventFilter)

Filter by `name`

_Removed when a mode of a `Calendar`_

`zoomLevel`

Zoom

200

_This feature_

Submenu for timeline zooming

\>`zoomSlider`

\-

210

_This feature_

Changes current zoom level

`dateRange`

Date range

300

_This feature_

Submenu for timeline range

`setRange`

Time range

300

_Only added when a `mode` of a `Calendar`_

Sets the Scheduler's`range`

_Replaces the Date range menu item_

\>`startDateField`

Start date

310

_This feature_

Start date for the timeline

\>`endDateField`

End date

320

_This feature_

End date for the timeline

\>`leftShiftBtn`

<

330

_This feature_

Shift backward

\>`todayBtn`

Today

340

_This feature_

Go to today

\>`rightShiftBtn`

\>

350

_This feature_

Shift forward

`currentTimeLine`

Show current timeline

400

[TimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges)

Show current time line

\>

first level of submenu

Customizing the menu items
--------------------------

The menu items in the TimeAxis Header menu can be customized, existing items can be changed or removed, and new items can be added. This is handled using the `items` config of the feature.

### Add extra items

```
const scheduler = new Scheduler({
    features : {
        timeAxisHeaderMenu : {
            items : {
                extraItem : {
                    text : 'Extra',
                    icon : 'fa fa-fw fa-flag',
                    onItem() {
                        ...
                    }
                }
            }
        }
    }
});
```

### Remove existing items

```
const scheduler = new Scheduler({
    features : {
        timeAxisHeaderMenu : {
            items : {
                zoomLevel : false
            }
        }
    }
});
```

### Customize existing item

```
const scheduler = new Scheduler({
    features : {
        timeAxisHeaderMenu : {
            items : {
                zoomLevel : {
                    text : 'Scale'
                }
            }
        }
    }
});
```

### Customizing submenu items

```
const scheduler = new Scheduler({
     features : {
         timeAxisHeaderMenu : {
             items : {
                 dateRange : {
                     menu : {
                         items : {
                             todayBtn : {
                                 text : 'Now'
                             }
                         }
                     }
                 }
             }
         }
     }
});
```

### Manipulate existing items

```
const scheduler = new Scheduler({
    features : {
        timeAxisHeaderMenu : {
            // Process items before menu is shown
            processItems({ items }) {
                 // Add an extra item dynamically
                items.coolItem = {
                    text : 'Cool action',
                    onItem() {
                          // ...
                    }
                }
            }
        }
    }
});
```

The \`processItems\` implementation my be an \`async\` function which \`awaits\` a result to mutate the \`items\` object.

Full information of the menu customization can be found in the ["Customizing the Event menu, the Schedule menu, and the TimeAxisHeader menu"](https://bryntum.com/docs/gantt/api/#Scheduler/guides/customization/contextmenu.md) guide.

Video guides
------------

[@youtube](https://bryntum.com/docs/gantt/api/https://youtube.com/embed/dEnpeZvC4Rc)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/HAq12QUBMx8)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/nXMaClkkKdQ)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/0seuhWrIeXc)

This feature is **enabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[processItems](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeAxisHeaderMenu#config-processItems)
A function called before displaying the menu that allows manipulations of its items. Returning `false` from this function prevents the menu being shown.

```
  features         : {
      timeAxisHeaderMenu : {
          processItems({ items }) {
              // Add or hide existing items here as needed
              items.myAction = {
                  text   : 'Cool action',
                  icon   : 'fa fa-fw fa-ban',
                  onItem : () => console.log('Some coolness'),
                  weight : 300 // Move to end
              };

              // Hide zoom slider
              items.zoomLevel.hidden = true;
          }
      }
  },
```

[items](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeAxisHeaderMenu#config-items)
This is a preconfigured set of items used to create the default context menu.

The `items` provided by this feature are listed in the intro section of this class. You can configure existing items by passing a configuration object to the keyed items.

To remove existing items, set corresponding keys `null`:

```
const scheduler = new Scheduler({
    features : {
        timeAxisHeaderMenu : {
            items : {
                eventsFilter : null
            }
        }
    }
});
```

See the feature config in the above example for details.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeAxisHeaderMenu#property-isTimeAxisHeaderMenu)
Identifies an object as an instance of [TimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeAxisHeaderMenu) class, or subclass thereof.

[isTimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeAxisHeaderMenu#property-isTimeAxisHeaderMenu-static)
Identifies an object as an instance of [TimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeAxisHeaderMenu) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[timeAxisHeaderMenuBeforeShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeAxisHeaderMenu#event-timeAxisHeaderMenuBeforeShow)
This event fires on the owning Scheduler or Gantt widget before the context menu is shown for the time axis header. Allows manipulation of the items to show in the same way as in the [processItems](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeAxisHeaderMenu#config-processItems).

Returning `false` from a listener prevents the menu from being shown.

[timeAxisHeaderMenuShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeAxisHeaderMenu#event-timeAxisHeaderMenuShow)
This event fires on the owning Scheduler or Gantt widget after the context menu is shown for a header

[timeAxisHeaderMenuItem](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeAxisHeaderMenu#event-timeAxisHeaderMenuItem)
This event fires on the owning Scheduler or Gantt widget when an item is selected in the header context menu.
