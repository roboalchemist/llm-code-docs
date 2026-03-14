# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/eventlayout/ProHorizontalLayout.md

# [ProHorizontalLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout)

Mixin for SchedulerPro horizontal layouts ([ProHorizontalLayoutPack](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayoutPack) and [ProHorizontalLayoutStack](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayoutStack)). Should not be used directly, instead specify [eventLayout](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-eventLayout) in the SchedulerPro config (`stack`, `pack` or `none`):

```
new SchedulerPro({
  eventLayout: 'stack'
});
```

Grouping events
---------------

By default events are not grouped and are laid out inside the row using start and end dates. Using [groupBy](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout#config-groupBy) config you can group events inside the resource row. Every group will be laid out on its own band, as if layout was applied to each group of events separately.

### By field value

You can specify field name to group events by. The following snippet would put _high_ prio events at the top:

```
new SchedulerPro({
    eventLayout : {
        type    : 'stack',
        groupBy : 'prio'
    },
    project : {
        events : [
            { id : 1, startDate : '2017-02-08', duration : 1, prio : 'low' },
            { id : 2, startDate : '2017-02-09', duration : 1, prio : 'high' },
            { id : 3, startDate : '2017-02-10', duration : 1, prio : 'high' },
        ],
        resources : [
            { id : 1, name : 'Resource 1' }
        ],
        assignments : [
            { id : 1, resource : 1, event : 1 },
            { id : 2, resource : 1, event : 2 },
            { id : 3, resource : 1, event : 3 }
        ]
    }
})
```

### Order of groups

Groups are **always** sorted ascending. In the example above _high_ prio events are above _low_ prio events because:

```
'high' < 'low' // true
```

If you want to group events in a specific order, you can define it in a special [weights](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout#config-weights) config:

```
new SchedulerPro({
    eventLayout : {
        type    : 'stack',
        weights : {
            low  : 100,
            high : 200
        },
        groupBy : 'prio'
    }
});
```

This will put _low_ prio events at the top.

The weight value defaults to `Infinity` unless specified in the weights config explicitly.

### Using a function

You can use a custom function to group events. The group function receives an event record as a single argument and is expected to return a non-null value for the group. This allows you to arrange events in any order you like, including grouping by multiple properties at once.

The snippet below groups events by duration and priority by creating 4 weights:

high prio

low prio

long

2

10

short

3

15

```
new SchedulerPro({
    eventLayout : {
        type    : 'stack',
        groupBy : event => {
            return (event.duration > 2 ? 2 : 3) * (event.prio === 'high' ? 1 : 5);
        }
    }
})
```

This will divide events into 4 groups as seen in this demo:

Manual event layout
-------------------

You can provide a custom function to layout events inside the row and set the row size as required using [layoutFn](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout#config-layoutFn). The function is called with an array of [render data](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#typedef-EventRenderData) objects. The custom function can iterate over those objects and position them inside the row using `top` and `height` attributes. The function should return the total row height in pixels.

Please note that using a custom layout function makes [rowHeight](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro#config-rowHeight) obsolete.

```
new SchedulerPro({
    eventLayout : {
        layoutFn : (items, resourceRecord, scheduler) => {
            // Put event element at random top position
            item.top = 100 * Math.random();
        }
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[type](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#config-type)
Type of horizontal layout. Supported values are `stack`, `pack` and `none`.

[weights](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#config-weights)
The weights config allows you to specify order of the event groups inside the row. Higher weights are placed further down in the row. If field value is not specified in the weights object, it will be assigned `Infinity` value and pushed to the bottom.

Only applicable when [groupBy](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout#config-groupBy) config is not a function:

```
new SchedulerPro({
    eventLayout : {
        type    : 'stack',
        weights : {
            // Events with high prio will be placed at the top, then medium,
            // then low prio events.
            high   : 100,
            medium : 150,
            low    : 200
        },
        groupBy : 'prio'
    }
});
```

Only explicitly defined groups are put in separate bands inside the row:

```
new SchedulerPro({
    eventLayout : {
        // Pack layout is also supported
        type : 'pack',
        weights : {
            // Events with high prio will be placed at the top. All other
            // events will be put to the same group at the bottom
            high : 100
        },
        groupBy : 'prio'
    }
});
```

[groupBy](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#config-groupBy)
Specifies a way to group events inside the row. Can accept either a model field name or a function which is provided with event record as a single argument and is expected to return group for the event.

[layoutFn](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#config-layoutFn)
Supply a function to manually layout events. It accepts event layout data and should set `top` and `height` for every provided data item (left and width are calculated according to the event start date and duration). The function should return the total row height in pixels.

For example, we can arrange events randomly in the row:

```
new SchedulerPro({
    eventLayout : {
        layoutFn : (items, resource, scheduler) => {
            items.forEach(item => {
                item.top = Math.round(Math.random() * 100);
                item.height = Math.round(Math.random() * 100);
            });

            return 50;
        }
    }
})
```

If you need a reference to the scheduler pro instance, you can get that from the function scope (arrow function doesn't work here):

```
new SchedulerPro({
    eventLayout : {
        layoutFn(items, resource, scheduler) {
            items.forEach(item => {
                item.top = Math.round(Math.random() * 100);
                item.height = Math.round(Math.random() * 100);
            });

            return scheduler.rowHeight;
        }
    }
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProHorizontalLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#property-isProHorizontalLayout)
Identifies an object as an instance of [ProHorizontalLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout) class, or subclass thereof.

[isProHorizontalLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#property-isProHorizontalLayout-static)
Identifies an object as an instance of [ProHorizontalLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout) class, or subclass thereof.

[grouped](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#property-grouped)
Returns `true` if event [grouper](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout#config-groupBy) is defined.

## Functions

Functions are methods available for calling on the class

[applyLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#function-applyLayout)
This method performs layout on an array of event render data and returns amount of _bands_. Band is a multiplier of a configured [rowHeight](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-rowHeight) to calculate total row height required to fit all events. This method should not be used directly, it is called by the Scheduler during the row rendering process.

[layoutEventsInBands](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#function-layoutEventsInBands)
This method iterates over events and calculates top position for each of them. Default layouts calculate positions to avoid events overlapping horizontally (except for the 'none' layout). Pack layout will squeeze events to a single row by reducing their height, Stack layout will increase the row height and keep event height intact. This method should not be used directly, it is called by the Scheduler during the row rendering process.

[getGroupValue](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#function-getGroupValue)
Returns group for the passed event render data.

[getEventGroups](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProHorizontalLayout#function-getEventGroups)
Sorts events by group and returns ordered array of groups, or empty array if events are not grouped.
