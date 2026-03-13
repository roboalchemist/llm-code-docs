# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/StickyEvents.md

# [StickyEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/StickyEvents)

This feature applies native `position: sticky` to event contents in horizontal mode, keeping the contents in view as long as possible on scroll. For vertical mode it uses a programmatic solution to achieve the same result.

Assign `eventRecord.stickyContents = false` to disable stickiness on a per event level (docs for [stickyContents](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-stickyContents)).

This feature is **enabled** by default.

If a complex [eventRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-eventRenderer) is used to create a DOM structure within the `.b-sch-event-content` element, then application CSS will need to be written to cancel the stickiness on the `.b-sch-event-content` element, and make some inner content element(s) sticky.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStickyEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/StickyEvents#property-isStickyEvents)
Identifies an object as an instance of [StickyEvents](https://bryntum.com/docs/gantt/api/#Scheduler/feature/StickyEvents) class, or subclass thereof.

[isStickyEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/StickyEvents#property-isStickyEvents-static)
Identifies an object as an instance of [StickyEvents](https://bryntum.com/docs/gantt/api/#Scheduler/feature/StickyEvents) class, or subclass thereof.
