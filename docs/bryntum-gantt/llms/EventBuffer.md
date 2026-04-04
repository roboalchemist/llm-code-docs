# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/EventBuffer.md

# [EventBuffer](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer)

Feature that allows showing additional time before & after an event, to visualize things like travel time - or the time you need to prepare a room for a meeting + clean it up after. You can configure whether the buffer time intervals should be considered busy time or available time using [bufferIsUnavailableTime](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventBuffer#property-bufferIsUnavailableTime).

The feature relies on two model fields: [preamble](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-preamble) and [postamble](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-postamble) which are used to calculate overall start and end dates used to position the event. Buffer time overlaps the same way events overlap (as you can see in the inline demo below). It should also be noted that buffer time is ignored for milestones.

This feature is **disabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showDuration](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#config-showDuration)
Show buffer duration labels

[bufferIsUnavailableTime](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#config-bufferIsUnavailableTime)
Set to `true` to treat buffer time spans as unavailable time (will effect the resource's availability).

[renderer](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#config-renderer)
A function which lets you customize the visual appearance of the preamble and postamble elements.

```
const schedulerPro = new SchedulerPro({
    features : {
        eventBuffer : {
            renderer({ eventRecord, resourceRecord, preambleConfig, postambleConfig }) {
                preambleConfig.cls  = 'before';
                preambleConfig.icon = 'fa fa-car';
                preambleConfig.text = 'Car';

                postambleConfig.cls  = 'after';
                postambleConfig.icon = 'fa fa-bicycle';
                postambleConfig.text = 'Bike';
            }
        }
    }
});
```

[tooltipTemplate](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#config-tooltipTemplate)
A function that receives data about the buffer time and returns a HTML string to show in a tooltip when hovering a buffer time element

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventBuffer](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#property-isEventBuffer)
Identifies an object as an instance of [EventBuffer](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventBuffer) class, or subclass thereof.

[isEventBuffer](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#property-isEventBuffer-static)
Identifies an object as an instance of [EventBuffer](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventBuffer) class, or subclass thereof.

[showDuration](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#property-showDuration)
Show buffer duration labels

[bufferIsUnavailableTime](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#property-bufferIsUnavailableTime)
Set to `true` to treat buffer time spans as unavailable time (will effect the resource's availability).

[tooltipTemplate](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventBuffer#property-tooltipTemplate)
A function that receives data about the buffer time and returns a HTML string to show in a tooltip when hovering a buffer time element
