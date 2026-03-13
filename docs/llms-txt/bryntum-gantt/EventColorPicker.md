# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/widget/EventColorPicker.md

# [EventColorPicker](https://bryntum.com/docs/gantt/api/Scheduler/widget/EventColorPicker)

A color picker that displays a list of available event colors which the user can select by using mouse or keyboard. See Schedulers [eventColor config](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-eventColor) for default available colors.

```
new EventColorPicker({
   appendTo : 'container',
   width    : '10em',
   onColorSelected(...args) {
       console.log(...args);
   }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[records](https://bryntum.com/docs/gantt/api/Scheduler/widget/EventColorPicker#config-records)
Provide an array of [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) instances to update their [eventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-eventColor) field

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventColorPicker](https://bryntum.com/docs/gantt/api/Scheduler/widget/EventColorPicker#property-isEventColorPicker)
Identifies an object as an instance of [EventColorPicker](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorPicker) class, or subclass thereof.

[isEventColorPicker](https://bryntum.com/docs/gantt/api/Scheduler/widget/EventColorPicker#property-isEventColorPicker-static)
Identifies an object as an instance of [EventColorPicker](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorPicker) class, or subclass thereof.
