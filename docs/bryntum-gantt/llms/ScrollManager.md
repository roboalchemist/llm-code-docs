# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/ScrollManager.md

# [ScrollManager](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager)

Monitors the mouse position over an element and scrolls the element if the cursor is close to edges. This is used by various features to scroll the grid section element, for example dragging elements close to edges.

```
// Instantiate manager for the container element having overflowing content
const manager = new ScrollManager({ element : document.querySelector('.container') });

// Start monitoring. When pointer approaches 50px region within monitored element edge, scrolling begins
manager.startMonitoring();

// Stop monitoring.
manager.stopMonitoring();
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[element](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#config-element)
Default element to use for scrolling. Can be overridden in calls to `startMonitoring()`.

[zoneWidth](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#config-zoneWidth)
Width in pixels of the area at the edges of an element where scrolling should be triggered

[scrollSpeed](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#config-scrollSpeed)
Scroll speed, higher number is slower. Calculated as "distance from zone edge / scrollSpeed"

[direction](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#config-direction)
The direction(s) to scroll ('horizontal', 'vertical' or 'both')

[startScrollDelay](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#config-startScrollDelay)
Number of milliseconds to wait before scroll starts when the mouse is moved close to an edge monitored by this scroll manager

[stopScrollWhenPointerOut](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#config-stopScrollWhenPointerOut)
Set to `true` to stop scrolling when pointing device leaves the scrollable element.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isScrolling](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#property-isScrolling)
Returns true if some of the monitored elements is being scrolled at the moment.

## Functions

Functions are methods available for calling on the class

[startMonitoring](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#function-startMonitoring)
Starts monitoring an element. It will be scrolled if mouse is pressed and within `zoneWidth` pixels from element edge. Supports monitoring multiple elements using `scrollables` option:

```
new ScrollManager({ element : '.item' }).startMonitoring({
    scrollables : [
        {
            // Applies config to all elements matching `.item .child-item`
            // selector
            element : '.child-item',
            // Only manage vertical scroll
            direction : 'vertical',
            // Specific callback for this scrollable. Shared callback is
            // ignored.
            callback : () => console.log('Specific callback')
        },
        {
            // Instance can be used
            element : document.querySelector('.item .child2')
            // Direction and callback are not provided, so element will
            // be scrollable in horizontal direction and will use shared
            // callback
        }
    ],
    direction : 'horizontal',
    callback  : () => console.log('Shared callback')
})
```

[stopMonitoring](https://bryntum.com/docs/gantt/api/Core/util/ScrollManager#function-stopMonitoring)
Stops monitoring an element. If no particular element is given, stop monitoring everything.
