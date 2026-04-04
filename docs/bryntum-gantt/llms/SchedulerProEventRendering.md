# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/view/mixin/SchedulerProEventRendering.md

# [SchedulerProEventRendering](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering)

Functions to handle event rendering in Scheduler Pro (EventModel -> dom elements).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[eventLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering#config-eventLayout)
This config defines how to handle overlapping events. Valid values are:

* `stack`, adjusts row height (only horizontal)
* `pack`, adjusts event height
* `mixed`, allows two events to overlap, more packs (only vertical)
* `none`, allows events to overlap

In horizontal mode, the default value is `stack`, in vertical mode it is `pack`. You can also provide a configuration object accepted by [ProHorizontalLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout) to group events or even take control over the layout (i.e. vertical position and height):

To group events:

```
new SchedulerPro({
    eventLayout : {
        type    : 'stack',
        weights : {
            high   : 100,
            normal : 150,
            low    : 200
        },
        groupBy : 'prio'
    }
});
```

To take control over the layout:

```
new SchedulerPro({
    eventLayout : {
        layoutFn : items => {
            items.forEach(item => {
                item.top = 100 * Math.random();
                item.height = 100 * Math.random();
            });

            return 100;
        }
    }
});
```

For more info on grouping and layout please refer to [ProHorizontalLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout) doc article.

[horizontalLayoutPackClass](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering#config-horizontalLayoutPackClass)
The class responsible for the packing horizontal event layout process. Override this to take control over the layout process.

[horizontalLayoutStackClass](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering#config-horizontalLayoutStackClass)
The class name responsible for the stacking horizontal event layout process. Override this to take control over the layout process.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerProEventRendering](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering#property-isSchedulerProEventRendering)
Identifies an object as an instance of [SchedulerProEventRendering](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/mixin/SchedulerProEventRendering) class, or subclass thereof.

[isSchedulerProEventRendering](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering#property-isSchedulerProEventRendering-static)
Identifies an object as an instance of [SchedulerProEventRendering](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/mixin/SchedulerProEventRendering) class, or subclass thereof.

[eventLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering#property-eventLayout)
This config defines how to handle overlapping events. Valid values are:

* `stack`, adjusts row height (only horizontal)
* `pack`, adjusts event height
* `mixed`, allows two events to overlap, more packs (only vertical)
* `none`, allows events to overlap

In horizontal mode, the default value is `stack`, in vertical mode it is `pack`. You can also provide a configuration object accepted by [ProHorizontalLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout) to group events or even take control over the layout (i.e. vertical position and height):

To group events:

```
new SchedulerPro({
    eventLayout : {
        type    : 'stack',
        weights : {
            high   : 100,
            normal : 150,
            low    : 200
        },
        groupBy : 'prio'
    }
});
```

To take control over the layout:

```
new SchedulerPro({
    eventLayout : {
        layoutFn : items => {
            items.forEach(item => {
                item.top = 100 * Math.random();
                item.height = 100 * Math.random();
            });

            return 100;
        }
    }
});
```

For more info on grouping and layout please refer to [ProHorizontalLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProHorizontalLayout) doc article.

## Functions

Functions are methods available for calling on the class

[getEventLayoutHandler](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering#function-getEventLayoutHandler)
Get event layout handler. The handler decides the vertical placement of events within a resource. Returns null if no eventLayout is used (if [eventLayout](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/mixin/SchedulerProEventRendering#config-eventLayout) is set to "none")

## Typedefs

Typedefs are type definitions for the class

[EventLayoutConfig](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulerProEventRendering#typedef-EventLayoutConfig)
Config for event layout
