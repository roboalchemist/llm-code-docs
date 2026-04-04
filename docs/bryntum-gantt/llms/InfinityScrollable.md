# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/InfinityScrollable.md

# [InfinityScrollable](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable)

This mixin connects an [InfinityScroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScroller) to a [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[animate](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#config-animate)
Set to `null` to disable smooth scroll animation.

[infinityScroller](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#config-infinityScroller)
The lazily created `InfinityScroller`. For derived classes, see [infinityScrollerDefaults](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScrollable#property-infinityScrollerDefaults).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isInfinityScrollable](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#property-isInfinityScrollable)
Identifies an object as an instance of [InfinityScrollable](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScrollable) class, or subclass thereof.

[isInfinityScrollable](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#property-isInfinityScrollable-static)
Identifies an object as an instance of [InfinityScrollable](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScrollable) class, or subclass thereof.

[animate](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#property-animate)
Set to `null` to disable smooth scroll animation.

[infinityScroller](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#property-infinityScroller)
The lazily created `InfinityScroller`. For derived classes, see [infinityScrollerDefaults](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScrollable#property-infinityScrollerDefaults).

[infinityScrollerDefaults](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#property-infinityScrollerDefaults)
Returns the default config object for the `infinityScroller`. It is likely that a derived class will need to augment this, but be sure to include the value produced by calling `super`.

## Functions

Functions are methods available for calling on the class

[sync](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#function-sync)
This method is called on animation frames to synchronize with the state of the `infinityScroller`. This method is called on the first `onPaint` as well as when the widget resizes.

This method is not called directly. It is only called by [syncSoon](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScrollable#function-syncSoon) which allows calls to aggregate to the next animation frame.

[syncSoon](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityScrollable#function-syncSoon)
Call this method to schedule a synchronization pass for the scroller. This will call [sync](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScrollable#function-sync) on the next animation frame.
