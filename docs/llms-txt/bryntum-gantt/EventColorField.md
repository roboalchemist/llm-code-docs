# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/widget/EventColorField.md

# [EventColorField](https://bryntum.com/docs/gantt/api/Scheduler/widget/EventColorField)

Color field widget for editing the EventModel's [eventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-eventColor) field. See Schedulers [eventColor config](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-eventColor) for default available colors.

What differs this widget from [ColorField](https://bryntum.com/docs/gantt/api/#Core/widget/ColorField) is that this uses the [EventColorPicker](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorPicker) as its picker. And also that the [name](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorField#config-name) config is set to `eventColor` per default.

This widget may be operated using the keyboard. `ArrowDown` opens the color picker, which itself is keyboard navigable.

```
const eventColorField = new EventColorField();
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventColorField](https://bryntum.com/docs/gantt/api/Scheduler/widget/EventColorField#property-isEventColorField)
Identifies an object as an instance of [EventColorField](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorField) class, or subclass thereof.

[isEventColorField](https://bryntum.com/docs/gantt/api/Scheduler/widget/EventColorField#property-isEventColorField-static)
Identifies an object as an instance of [EventColorField](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorField) class, or subclass thereof.
