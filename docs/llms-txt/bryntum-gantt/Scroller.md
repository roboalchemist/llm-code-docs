# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/Scroller.md

# [Scroller](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller)

Encapsulates scroll functionality for a Widget. All requests for scrolling and scrolling information must go through a Widget's [scrollable](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-scrollable) property.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[widget](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-widget)
The widget which is to scroll.

[element](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-element)
The element which is to scroll. Defaults to the [overflowElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-overflowElement) of the configured [widget](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller#config-widget)

[contentElement](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-contentElement)
The element, or a selector which identifies a descendant element whose size will affect the scroll range.

[overflowX](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-overflowX)
How to handle overflowing in the `X` axis. May be:

* `'auto'`
* `'visible'`
* `'hidden'`
* `'scroll'`
* `'clip'`
* `'hidden-scroll'` Meaning scrollable from the UI but with no scrollbar, for example a grid header. Only on platforms which support this feature.
* `true` - meaning `'auto'`
* `false` - meaning `'hidden'`

[overflowY](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-overflowY)
How to handle overflowing in the `Y` axis. May be:

* `'auto'`
* `'visible'`
* `'hidden'`
* `'scroll'`
* `'clip'`
* `'hidden-scroll'` Meaning scrollable from the UI but with no scrollbar. Only on platforms which support this feature.
* `true` - meaning `'auto'`
* `false` - meaning `'hidden'`

[translate](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-translate)
If configured as `true`, the [element](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller#config-element) is not scrolled but is translated using CSS translate when controlled by this class's API. Scroll events are fired when the element is translated.

[behavior](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-behavior)
Configures the [`scroll-behavior`](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-behavior) for the scrolling element. By default, this is controlled by CSS (i.e., `'auto'`).

[propagateSync](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-propagateSync)
Configure as `true` to immediately sync partner scrollers when being synced by a controlling partner instead of waiting for our own `scroll` event to pass the scroll on to partners.

[stickies](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-stickies)
CSS selector(s) of sticky elements, or the elements themselves which should be taken into account when scrolling.

These are used to identify elements which are sticky and docked to occlude edges of the scrolling element so that the viewport size can be calculated accurately when scrolling.

[scrollingCls](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#config-scrollingCls)
The CSS class to add to the [element](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller#config-element) when it is being scrolled.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isScroller](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-isScroller)
Identifies an object as an instance of [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller) class, or subclass thereof.

[isScroller](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-isScroller-static)
Identifies an object as an instance of [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller) class, or subclass thereof.

[behavior](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-behavior)
Configures the [`scroll-behavior`](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-behavior) for the scrolling element. By default, this is controlled by CSS (i.e., `'auto'`).

[propagateSync](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-propagateSync)
Configure as `true` to immediately sync partner scrollers when being synced by a controlling partner instead of waiting for our own `scroll` event to pass the scroll on to partners.

[overflowX](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-overflowX)
The `overflow-x` setting for the widget. `true` means `'auto'`.

[overflowY](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-overflowY)
The `overflow-y` setting for the widget. `true` means `'auto'`.

[viewport](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-viewport)
A [Rectangle](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle) describing the bounds of the scrolling viewport.

[x](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-x)
The horizontal scroll position of the widget.

Note that this is always positive. Horizontal scrolling using the `X` property always proceeds in the positive direction.

[scrollLeft](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-scrollLeft)
The natural DOM horizontal scroll position of the widget.

Note that this proceeds from 0 into negative space in RTL mode.

[y](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-y)
The vertical scroll position of the widget.

[maxX](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-maxX)
The maximum `X` scrollable position of the widget.

[maxY](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-maxY)
The maximum `Y` scrollable position of the widget.

[lastScrollLeft](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-lastScrollLeft)
The furthest possible `scrollLeft` position of the widget. Will be negative if in writing direction is RTL.

[scrollWidth](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-scrollWidth)
The horizontal scroll range of the widget.

[scrollHeight](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-scrollHeight)
The vertical scroll range of the widget. May be set to larger than the actual data height to enable virtual scrolling. This is how the grid extends its scroll range while only rendering a small subset of the dataset.

[clientWidth](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-clientWidth)
The client width of the widget.

[clientHeight](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-clientHeight)
The client height of the widget.

[id](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#property-id)
The unique ID of this Scroller

## Functions

Functions are methods available for calling on the class

[hasOverflow](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-hasOverflow)
Returns `true` if there is overflow in the specified axis.

[hasScrollbar](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-hasScrollbar)
Returns `true` if there is a _space-consuming_ scrollbar controlling scroll in the specified axis.

[addPartner](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-addPartner)
Partners this Scroller with the passed scroller in order to sync the scrolling position in the passed axes

[removePartner](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-removePartner)
Breaks the link between this Scroller and the passed Scroller set up by the [addPartner](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller#function-addPartner) method.

[clearPartners](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-clearPartners)
Breaks the link between this Scroller and all other Scrollers set up by the [addPartner](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller#function-addPartner) method.

[scrollIntoView](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-scrollIntoView)
Scrolls the passed element or [Rectangle](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle) into view according to the passed options.

[scrollIntoView](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-scrollIntoView-static)
Scrolls the passed element into view according to the passed options.

[scrollBy](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-scrollBy)
Scrolls by the passed deltas according to the passed options.

[scrollTo](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-scrollTo)
Scrolls to the passed position according to the passed options.

[onElMutation](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-onElMutation)
Respond to style changes to monitor scroll _when this Scroller is in `translate: true` mode._

[syncPartners](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-syncPartners)
Syncs all attached scrolling partners with the scroll state of this Scroller.

[getDeltaTo](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-getDeltaTo)
Returns the xDelta and yDelta values in an object from the current scroll position to the passed element or Rectangle.

[getDelta](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-getDelta)
Returns the delta to scroll the target rectangle into view in the specified flow direction, "inline" or "block".

[sync](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#function-sync)
Syncs this Scroller with the passed Scroller in the passed axes.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[scroll](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#event-scroll)
Fired when scrolling happens on this Scroller's element. The event object is a native `scroll` event with the described extra properties injected.

[scrollEnd](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#event-scrollEnd)
Fired when scrolling finished on this Scroller's element. The event object is the last native `scroll` event fires by the element with the described extra properties injected.

[overflowChange](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#event-overflowChange)
Fired when either the X or the Y axis changes from not showing a space-consuming scrollbar to showing a space-consuming scrollbar or vice versa.

__Does not fire on platforms which show overlayed scrollbars__

## Typedefs

Typedefs are type definitions for the class

[AnimateScrollOptions](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#typedef-AnimateScrollOptions)
Animation options for scrolling.

[BryntumScrollOptions](https://bryntum.com/docs/gantt/api/Core/helper/util/Scroller#typedef-BryntumScrollOptions)
Options accepted by some scroll functions. Note that not all options are valid for all functions.
