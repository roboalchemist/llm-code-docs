# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/CalendarHighlight.md

# [CalendarHighlight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight)

This feature temporarily visualizes [calendars](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/CalendarModel) for the event or resource calendar (controlled by the [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/CalendarHighlight#config-calendar) config). The calendars are highlighted while a user is creating, dragging or resizing a task. Enabling this feature makes it easier for the end user to understand the underlying rules of the schedule.

Example usage
-------------

```
new SchedulerPro({
    features : {
        calendarHighlight : {
            // visualize resource calendars while interacting with events
            calendar : 'resource'
        }
    }
})
```

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[calendar](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#config-calendar)
A string defining which calendar(s) to highlight during drag drop, resize or create flows. Valid values are `event` or `resource`.

[collectAvailableResources](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#config-collectAvailableResources)
A callback function which is called when you interact with one or more events (e.g. drag drop) to highlight only available resources.

```
new SchedulerPro({
    features : {
        calendarHighlight : {
            collectAvailableResources({ scheduler, eventRecords }) {
                 const mainEvent = eventRecords[0];
                 return scheduler.resourceStore.query(resource => resource.role === mainEvent.requiredRole || !mainEvent.requiredRole);
             }
        }
    }
});
```

[inflate](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#config-inflate)
A number allowing you to expand or shrink (using a negative number) the highlighted box.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCalendarHighlight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#property-isCalendarHighlight)
Identifies an object as an instance of [CalendarHighlight](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/CalendarHighlight) class, or subclass thereof.

[isCalendarHighlight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#property-isCalendarHighlight-static)
Identifies an object as an instance of [CalendarHighlight](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/CalendarHighlight) class, or subclass thereof.

[inflate](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#property-inflate)
A number allowing you to expand or shrink (using a negative number) the highlighted box.

## Functions

Functions are methods available for calling on the class

[highlightEventCalendars](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#function-highlightEventCalendars)
Highlights the time spans representing the calendars of the passed event records, and resource records.

[highlightResourceCalendarsForEventRecords](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#function-highlightResourceCalendarsForEventRecords)
Highlights the time spans representing the available time for resources that can perform the passed eventRecords. This method will call [collectAvailableResources](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/CalendarHighlight#config-collectAvailableResources) to collect the available resources.

[highlightResourceCalendars](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#function-highlightResourceCalendars)
Highlights the time spans representing the working time calendars of the passed resource records.

[unhighlightCalendars](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#function-unhighlightCalendars)
Removes all highlight elements.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeRenderCalendarHighlights](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/CalendarHighlight#event-beforeRenderCalendarHighlights)
Fires on the owning Scheduler when the CalendarHighlight feature has created highlighting items which are about to be rendered.
