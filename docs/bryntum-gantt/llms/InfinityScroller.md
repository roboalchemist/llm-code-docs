# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/InfinityScroller.md

# [InfinityScroller](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller)

This class virtualizes a DOM [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller) to allow scroll ranges that exceed browser limits and also allow negative scroll positions. These are managed by instances of [InfinityAxis](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityAxis) named `x` and `y`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[animate](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-animate)
Set to `null` to disable smooth scroll animation.

[client](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-client)
The owning container. Because position virtualization is only implemented for [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget), the `client` must be a [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container).

[safetyMargin](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-safetyMargin)
The proportional amount of the browser's true [scrollLimit](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#property-scrollLimit-static) to not use in order to reduce likelihood of browser anomalies. By default, 99% of the limit is used (this value being 1%, by default).

[scrollIdle](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-scrollIdle)
The number of consecutive animation frames with no scroll motion that must occur before the scroll is declared complete. After this time, the [scrollEnd](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScroller#event-scrollEnd) event is fired.

[scrolling](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-scrolling)
This config is used to track the current scrolling state. As it changes, various side-effects ensue.

[snap](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-snap)
If not null, this config determines which axis to use for scroll snapping.

[snapThreshold](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-snapThreshold)
The minimum number of pixels or the minimum proportion of the item that must be scrolled to initiate a snap to reveal the whole item. A completed scroll of less than this amount is reversed. If this value is less-than 1, then this is the decimal fraction of the item's size. By default, this value is 0.1, which is 10% of the item's width. Otherwise, this value is an absolute number of pixels.

[x](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-x)
The [InfinityAxis](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityAxis) instance managing the x-axis.

[y](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#config-y)
The [InfinityAxis](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityAxis) instance managing the y-axis.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[animate](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-animate)
Set to `null` to disable smooth scroll animation.

[safetyMargin](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-safetyMargin)
The proportional amount of the browser's true [scrollLimit](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#property-scrollLimit-static) to not use in order to reduce likelihood of browser anomalies. By default, 99% of the limit is used (this value being 1%, by default).

[scrollIdle](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-scrollIdle)
The number of consecutive animation frames with no scroll motion that must occur before the scroll is declared complete. After this time, the [scrollEnd](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScroller#event-scrollEnd) event is fired.

[scrolling](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-scrolling)
This config is used to track the current scrolling state. As it changes, various side-effects ensue.

[scrollLimit](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-scrollLimit)
Used for unit testing. Ignores the browser scroll limit in favor of a consistent, predictable value.

[snap](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-snap)
If not null, this config determines which axis to use for scroll snapping.

[snapThreshold](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-snapThreshold)
The minimum number of pixels or the minimum proportion of the item that must be scrolled to initiate a snap to reveal the whole item. A completed scroll of less than this amount is reversed. If this value is less-than 1, then this is the decimal fraction of the item's size. By default, this value is 0.1, which is 10% of the item's width. Otherwise, this value is an absolute number of pixels.

[x](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-x)
The [InfinityAxis](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityAxis) instance managing the x-axis.

[y](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#property-y)
The [InfinityAxis](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityAxis) instance managing the y-axis.

## Functions

Functions are methods available for calling on the class

[pushEvent](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#function-pushEvent)
Tracks the given `event` and a small number of prior events. These are used to determine direction of scroll in the scroll axis, as well as to always have access to the `lastEvent` responsible for scrolling.

[scrollTo](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#function-scrollTo)
Scrolls to the specified `x` and `y` positions, or by the specified `dx` and `dy`. Only one of these values is required. It is invalid to pass `x` and `dx`, or `y` and `dy` at the same time, however, it is valid to pass `x` and `dy`, or `y` and `dx`.

This method returns a Promise that resolves to a boolean value. This value indicates that the desired scroll adjustment was made. It is `false` if the scroll ends at a different position. This can happen if the user interferes with the scroll, or another call to this method is made before the first call completes.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[scroll](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#event-scroll)
Fired when scrolling happens on this InfinityScroller's element.

[scrollEnd](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScroller#event-scrollEnd)
Fired when scrolling finished on this InfinityScroller's element.
