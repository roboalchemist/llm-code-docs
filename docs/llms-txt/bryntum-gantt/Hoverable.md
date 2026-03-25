# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Hoverable.md

# [Hoverable](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable)

This mixin provides mouse hover tracking.

```
 class Tracker extends Base.mixin(Hoverable) {
     hoverEnter(leaving) {
         // this.hoverTarget has been entered from "leaving"
         // this.hoverTarget will never be null, but leaving may be null
     }

     hoverLeave(leaving) {
         // this.hoverTarget has been entered from "leaving"
         // this.hoverTarget may be null, but leaving will never be null
     }

     hoverMove(event) {
         // called when a mousemove is made within a hover target
         // this.hoverTarget will never be null
     }
 }

 let tracker = new Tracker({
     hoverRootElement : document.body,
     hoverSelector    : '.hoverable'
 });
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[hoverCls](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverCls)
A CSS class to add to the [target](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget) element.

[hoverAnimationCls](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverAnimationCls)
A CSS class to add to the [target](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget) element to enable CSS animations. This class is added after calling [hoverEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#function-hoverEnter).

[hoverRootCls](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverRootCls)
A CSS class to add to the [root](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverRootElement) element.

[hoverRootActiveCls](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverRootActiveCls)
A CSS class to add to the [root](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverRootElement) element when there is an active [target](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget).

[hoverDelay](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverDelay)
The number of milliseconds to delay notification of changes in the [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget).

[hoverElement](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverElement)
The current element that the cursor is inside as determined by `mouseover` and `mouseout`. Changes in this config trigger re-evaluation of the [hoverSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverSelector) to determine if there is a [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget).

[hoverIgnoreElement](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverIgnoreElement)
An element to ignore. Mouse entry into this element will not trigger a change in either of the [hoverElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverElement) or [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget) values.

[hoverEdges](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverEdges)
This property is a string containing one character for each edge that is hoverable. For example, a value of "tb" indicates that the top and bottom edges are hoverable.

[hoverEdgeSize](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverEdgeSize)
When [hoverEdges](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverEdges) is used, this value determines the size (in pixels) of the edge. When the cursor is within this number of pixels of an edge listed in `hoverEdges`, the appropriate CSS class is added to the [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget):

* `b-hover-top`
* `b-hover-right`
* `b-hover-bottom`
* `b-hover-left`

Depending on the values of `hoverEdges`, it is possible to have at most two of these classes present at any one time (when the cursor is in a corner).

[hoverRootElement](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverRootElement)
The outer element where hover tracking will operate (attach events to it and use as root limit when looking for ancestors).

A common choice for this will be `document.body`.

[hoverSelector](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverSelector)
A selector for the [closest](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Element/closest) API to determine the actual element of interest. This selector is used to process changes to the [hoverElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverElement) to determine the [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget).

[hoverTarget](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverTarget)
The currently active hover target. This will be the same as [hoverElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverElement) unless there is a [hoverSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverSelector).

[hoverTrack](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverTrack)
Set to `true` to include tracking of `mousemove` events for the active [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget). This is required for the [hoverMove](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#function-hoverMove) method to be called.

[hoverZone](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#config-hoverZone)
A string value containing one character per active edge (e.g., "tr").

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isHoverable](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#property-isHoverable)
Identifies an object as an instance of [Hoverable](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable) class, or subclass thereof.

[isHoverable](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#property-isHoverable-static)
Identifies an object as an instance of [Hoverable](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[hoverEnter](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#function-hoverEnter)
This method is called when the cursor enters the [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget). The `hoverTarget` will not be `null`.

[hoverIgnore](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#function-hoverIgnore)
This method should return true if the given `element` should be ignored. By default, this is `true` if the `element` is contained inside the [hoverIgnoreElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverIgnoreElement).

[hoverLeave](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#function-hoverLeave)
This method is called when the cursor leaves the [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget). The `hoverTarget` may be `null` or refer to the new `hoverTarget`

[hoverMove](https://bryntum.com/docs/gantt/api/Core/mixin/Hoverable#function-hoverMove)
This method is called when the mouse moves within a [hoverTarget](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTarget), but only if enabled by the [hoverTrack](https://bryntum.com/docs/gantt/api/#Core/mixin/Hoverable#config-hoverTrack) config.
