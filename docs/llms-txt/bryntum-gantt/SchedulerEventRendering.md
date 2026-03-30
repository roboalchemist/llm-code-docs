# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/SchedulerEventRendering.md

# [SchedulerEventRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering)

Functions to handle event rendering (EventModel -> dom elements).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[milestoneTextPosition](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-milestoneTextPosition)
Position of the milestone text:

* 'inside' - for short 1-char text displayed inside the diamond, not applicable when using [milestoneLayoutMode](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneLayoutMode))
* 'outside' - for longer text displayed outside the diamond, but inside it when using [milestoneLayoutMode](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneLayoutMode)
* 'always-outside' - outside even when combined with [milestoneLayoutMode](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneLayoutMode)

[milestoneAlign](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-milestoneAlign)
How to align milestones in relation to their startDate. Only applies when using a `milestoneLayoutMode` other than `default`. Valid values are:

* start
* center (default)
* end

[milestoneCharWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-milestoneCharWidth)
Factor representing the average char width in pixels used to determine milestone width when configured with `milestoneLayoutMode: 'estimate'`.

[milestoneLayoutMode](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-milestoneLayoutMode)
How to handle milestones during event layout. How the milestones are displayed when part of the layout are controlled using [milestoneTextPosition](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneTextPosition).

Options are:

* default - Milestones do not affect event layout
* estimate - Milestone width is estimated by multiplying text length with Scheduler#milestoneCharWidth
* data - Milestone width is determined by checking EventModel#milestoneWidth
* measure - Milestone width is determined by measuring label width Please note that currently text width is always determined using EventModel#name. Also note that only 'default' is supported by eventStyles line, dashed and minimal.

[eventLayout](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-eventLayout)
Defines how to handle overlapping events. Valid values are:

* `stack`, adjusts row height (only horizontal)
* `pack`, adjusts event height in horizontal mode, (width in vertical mode) to fit all events
* `mixed`, allows two events to overlap, more packs (only vertical)
* `none`, allows events to overlap

In horizontal mode, the default value is `stack`, in vertical mode it is `pack`. This config can also accept an object:

```
new Scheduler({
    eventLayout : { type : 'stack' }
})
```

[overlappingEventSorter](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-overlappingEventSorter)
Override this method to provide a custom sort function to sort any overlapping events. This only applies to the horizontal mode, where the order the events are sorted in determines their vertical placement within a resource.

By default, overlapping events are laid out based on the start date. If the start date is equal, events with earlier end date go first. And lastly the name of events is taken into account.

Here's a sample sort function, sorting on start- and end date. If this function returns -1, then event `a` is placed above event `b`:

```
overlappingEventSorter(a, b) {

  const startA = a.startDate, endA = a.endDate;
  const startB = b.startDate, endB = b.endDate;

  const sameStart = (startA - startB === 0);

  if (sameStart) {
    return endA > endB ? -1 : 1;
  } else {
    return (startA < startB) ? -1 : 1;
  }
}
```

NOTE: The algorithms (stack, pack) that lay the events out expects them to be served in chronological order, be sure to first sort by `startDate` to get predictable results.

[useInitialAnimation](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-useInitialAnimation)
By default, scheduler fade events in on load. Specify `false` to prevent this animation or specify one of the available animation types to use it (`true` equals `'fade-in'`):

* fade-in (default)
* slide-from-left
* slide-from-top

```
// Slide events in from the left on load
scheduler = new Scheduler({
    useInitialAnimation : 'slide-from-left'
});
```

[eventRenderer](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-eventRenderer)
An empty function by default, but provided so that you can override it. This function is called each time an event is rendered into the schedule to render the contents of the event. It's called with the event, its resource and a `renderData` object which allows you to populate data placeholders inside the event template.

You should never modify any records inside this method.

By default, the DOM markup of an event bar includes placeholders for 'cls' and 'style'. The cls property is a [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList) which will be added to the event element. The style property is an inline style declaration for the event element.

When returning content, be sure to consider how that content should be encoded to avoid XSS (Cross-Site Scripting) attacks. This is especially important when including user-controlled data such as the event's `name`. The function [encodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-encodeHtml-static) as well as [xss](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-xss-static) can be helpful in these cases.

```
 eventRenderer({ eventRecord, resourceRecord, renderData }) {
     renderData.style = 'color:white';                 // You can use inline styles too.

     // Property names with truthy values are added to the resulting elements CSS class.
     renderData.cls.isImportant = this.isImportant(eventRecord);
     renderData.cls.isModified = eventRecord.isModified;

     // Remove a class name by setting the property to false
     renderData.cls[scheduler.generatedIdCls] = false;

     // Or, you can treat it as a string, but this is less efficient, especially
     // if your renderer wants to *remove* classes that may be there.
     renderData.cls += ' extra-class';

     return StringHelper.xss`${DateHelper.format(eventRecord.startDate, 'YYYY-MM-DD')}: ${eventRecord.name}`;
 }
```

[eventRendererThisObj](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-eventRendererThisObj)
`this` reference for the [eventRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-eventRenderer) function

[eventBarTextField](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-eventBarTextField)
Field from EventModel displayed as text in the bar when rendering

[horizontalLayoutPackClass](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-horizontalLayoutPackClass)
The class responsible for the packing horizontal event layout process. Override this to take control over the layout process.

[horizontalLayoutStackClass](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-horizontalLayoutStackClass)
The class name responsible for the stacking horizontal event layout process. Override this to take control over the layout process.

[barMargin](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-barMargin)
Controls how much space to leave between stacked event bars in px.

Can be configured per resource by setting [resource.barMargin](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-barMargin).

[initialAnimationDuration](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-initialAnimationDuration)
Maximum duration (in milliseconds) for the initial animation controlled by [useInitialAnimation](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-useInitialAnimation).

[narrowEventWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-narrowEventWidth)
When an event bar has a width less than this value, it gets the CSS class `b-sch-event-narrow` added. You may apply custom CSS rules using this class.

In vertical mode, this class causes the text to be rotated so that it runs vertically.

[eventReleaseThreshold](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-eventReleaseThreshold)
An advanced setting that controls the maximum number of released event bars to keep in the DOM.

Schedulers virtualization releases event bars that go out of view, which means they are hidden but not removed from the DOM. When another event bar enters view, a released one is reused. This is faster than removing and re-adding the event bars from the DOM.

By default, all released event bars are kept around, and you should in general not need to adjust this setting. But if you have an app in which the scheduler sometimes displays a very large number of events on the screen at the same time, and sometimes only a few, you can experiment with tweaking this setting to free up some memory in the sparse case.

[minPackSize](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#config-minPackSize)
_Experimental_ Minimum size that events should be allowed to shrink to when using `pack` layout. If packing leads to any event being smaller than this value, the row will grow in height instead to maintain this minimum size.

When combined with `barMargin`, events can still shrink below the limit. Adjust the value to suite your needs

```
new Scheduler({
  eventLayout : 'pack',
  minPackSize : 10
});
```

This setting is currently only used in horizontal mode.

Being experimental, this API might be removed or adjusted with short notice in the future.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerEventRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-isSchedulerEventRendering)
Identifies an object as an instance of [SchedulerEventRendering](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering) class, or subclass thereof.

[isSchedulerEventRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-isSchedulerEventRendering-static)
Identifies an object as an instance of [SchedulerEventRendering](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering) class, or subclass thereof.

[milestoneTextPosition](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-milestoneTextPosition)
Position of the milestone text:

* 'inside' - for short 1-char text displayed inside the diamond, not applicable when using [milestoneLayoutMode](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneLayoutMode))
* 'outside' - for longer text displayed outside the diamond, but inside it when using [milestoneLayoutMode](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneLayoutMode)
* 'always-outside' - outside even when combined with [milestoneLayoutMode](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneLayoutMode)

[milestoneAlign](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-milestoneAlign)
How to align milestones in relation to their startDate. Only applies when using a `milestoneLayoutMode` other than `default`. Valid values are:

* start
* center (default)
* end

[milestoneCharWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-milestoneCharWidth)
Factor representing the average char width in pixels used to determine milestone width when configured with `milestoneLayoutMode: 'estimate'`.

[milestoneLayoutMode](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-milestoneLayoutMode)
How to handle milestones during event layout. How the milestones are displayed when part of the layout are controlled using [milestoneTextPosition](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneTextPosition).

Options are:

* default - Milestones do not affect event layout
* estimate - Milestone width is estimated by multiplying text length with Scheduler#milestoneCharWidth
* data - Milestone width is determined by checking EventModel#milestoneWidth
* measure - Milestone width is determined by measuring label width Please note that currently text width is always determined using EventModel#name. Also note that only 'default' is supported by eventStyles line, dashed and minimal.

[eventLayout](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-eventLayout)
Defines how to handle overlapping events. Valid values are:

* `stack`, adjusts row height (only horizontal)
* `pack`, adjusts event height in horizontal mode, (width in vertical mode) to fit all events
* `mixed`, allows two events to overlap, more packs (only vertical)
* `none`, allows events to overlap

In horizontal mode, the default value is `stack`, in vertical mode it is `pack`. This config can also accept an object:

```
new Scheduler({
    eventLayout : { type : 'stack' }
})
```

[overlappingEventSorter](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-overlappingEventSorter)
Override this method to provide a custom sort function to sort any overlapping events. See [overlappingEventSorter](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-overlappingEventSorter) for more details.

[useInitialAnimation](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-useInitialAnimation)
By default, scheduler fade events in on load. Specify `false` to prevent this animation or specify one of the available animation types to use it (`true` equals `'fade-in'`):

* fade-in (default)
* slide-from-left
* slide-from-top

```
// Slide events in from the left on load
scheduler = new Scheduler({
    useInitialAnimation : 'slide-from-left'
});
```

[initialAnimationDuration](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-initialAnimationDuration)
Maximum duration (in milliseconds) for the initial animation controlled by [useInitialAnimation](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-useInitialAnimation).

[eventReleaseThreshold](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-eventReleaseThreshold)
An advanced setting that controls the maximum number of released event bars to keep in the DOM.

Schedulers virtualization releases event bars that go out of view, which means they are hidden but not removed from the DOM. When another event bar enters view, a released one is reused. This is faster than removing and re-adding the event bars from the DOM.

By default, all released event bars are kept around, and you should in general not need to adjust this setting. But if you have an app in which the scheduler sometimes displays a very large number of events on the screen at the same time, and sometimes only a few, you can experiment with tweaking this setting to free up some memory in the sparse case.

[minPackSize](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#property-minPackSize)
_Experimental_ Minimum size that events should be allowed to shrink to when using `pack` layout. If packing leads to any event being smaller than this value, the row will grow in height instead to maintain this minimum size.

When combined with `barMargin`, events can still shrink below the limit. Adjust the value to suite your needs

```
new Scheduler({
  eventLayout : 'pack',
  minPackSize : 10
});
```

This setting is currently only used in horizontal mode.

Being experimental, this API might be removed or adjusted with short notice in the future.

## Functions

Functions are methods available for calling on the class

[getEventLayoutHandler](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#function-getEventLayoutHandler)
Get event layout handler. The handler decides the vertical placement of events within a resource. Returns null if no eventLayout is used (if [eventLayout](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-eventLayout) is set to "none")

[repaintEventsForResource](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#function-repaintEventsForResource)
Rerenders events for specified resource (by rerendering the entire row).

[repaintEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#function-repaintEvent)
Rerenders the events for all resources connected to the specified event

[generateRenderData](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#function-generateRenderData)
Generates data used in the template when rendering an event. For example which css classes to use. Also calls the [eventRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-eventRenderer).

[onEventDataGenerated](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#function-onEventDataGenerated)
A method which may be chained by features. It is called when an event's render data is calculated so that features may update the style, class list or body.

[restartInitialAnimation](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#function-restartInitialAnimation)
Restarts initial events animation with new value [useInitialAnimation](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-useInitialAnimation).

[getMilestoneLabelWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#function-getMilestoneLabelWidth)
Determines width of a milestones label. How width is determined is decided by configuring [milestoneLayoutMode](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-milestoneLayoutMode). Please note that text width is always determined using the events [name](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-name).

## Typedefs

Typedefs are type definitions for the class

[EventRenderData](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerEventRendering#typedef-EventRenderData)
Layout data object used to lay out an event record.
