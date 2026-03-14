# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Carousel.md

# [Carousel](https://bryntum.com/docs/gantt/api/Core/widget/Carousel)

A virtualized container of items that can be scrolled either horizontally or vertically. As scrolling occurs, a configured number of visible items ([slots](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-slots)) are dynamically positioned and reconfigured to give the appearance that all items in the specified [range](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-range) are present.

To create a carousel, a [configureSlot](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-configureSlot) function must be provided that will return the configuration object for a given slot index. Slot index 0 is special, and whenever the [range](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-range) is not empty, 0 must be included in the range. The meaning of a slot index, however, is defined by the developer and only interpreted by the developer-provided [configureSlot](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-configureSlot) function.

Slot indexes are converted into virtual scroll positions and given to an [InfinityScroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScroller). This special scroller allows for negative scroll positioning as well as unbounded scroll range.

This widget is not intended to be used standalone, but as part of higher-level widgets such as [MultiDatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/MultiDatePicker).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[configureSlot](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-configureSlot)
A callback function that must be provided by the developer to produce configuration objects for the slots in the carousel.

Derived classes may set this config to the name of the instance method to call. The `this` pointer will be the carousel instance.

[disableReserveSlots](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-disableReserveSlots)
The value to set for the [disabled](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-disabled) config on reserve slots. These slots are not visible to the user but can be tabbed into from visible slots.

When set to `'inert'`, the `inert` DOM attribute is also set. This prevents tabbing from a visible slot to a reserved slot.

[emptyHtml](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-emptyHtml)
The HTML to render when the carousel's [range](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-range) is empty. To avoid XSS attacks, it is safer to use [emptyText](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-emptyText) instead.

[emptyText](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-emptyText)
The text to render when the carousel's [range](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-range) is empty. This text is automatically encoded and is safe from XSS issues. To render markup when the carousel is empty, see [emptyHtml](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-emptyHtml).

[range](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-range)
The range of slot indexes to be presented in the carousel. Slot indexes greater than or equal to `range[0]` and less than `range[1]` will be rendered.

If this value is `null` or `[0, 0]`, the carousel will render no items (i.e., it will be empty). See [emptyText](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-emptyText).

By default, the carousel's range is unlimited, i.e., `range = [-Infinity, Infinity]`.

[reserveSlots](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-reserveSlots)
The number of slots to render beyond what is visible in the carousel. These reserve items are critical to giving the appearance of continuity as the carousel is being scrolled. A minimum of 1 is required and is generally sufficient for slots that are reasonably large. If slots are small (maybe less than 100px), it may be helpful to provide additional reserve slots.

[scrollOnTab](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-scrollOnTab)
Set to `true` to use [trapFocus](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-trapFocus) to scroll the carousel when tabbing to slots that are not currently visible.

NOTE: This only works when [configureSlot](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-configureSlot) produces [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel) instances.

[shrinkWrap](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-shrinkWrap)
Due to the `position: absolute` nature of carousel items, a carousel does not have a natural size. When the carousel is being sized by its container, this is not a problem, but can be an issue if the carousel is being used in a layout where its natural size would be important.

Specify `true` for the carousel to provide a natural size based on the size of its slots. This is done by setting `min-width` and/or `min-height` on the internal elements that contain the absolutely positioned slots. This may have a modest performance impact due to the required measuring of the slots to provide these minimums.

By default (`shrinkWrap = 'auto'`), the carousel enables shrinkWrap support when the carousel's main element is `position: absolute`. This can be disabled by setting `shrinkWrap = false`.

[slots](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-slots)
The number of slots to present in the carousel. When set to a number, each slot is given a percentage size (e.g., "50%" for `slots = 2`) so they fill the carousel. This is typically required when the carousel is using [shrinkWrap](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-shrinkWrap) (note: shrink wrapping is enabled by default for `position: absolute` carousels).

When `null`, as many slots as needed to fill the carousel are created. This can produce partially visible slots.

Setting this value to `'auto'` will similarly fill the available space, but once the required number of slots is determined, they are assigned a percentage size so that they completely fill the carousel.

[snap](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-snap)
Set to `false` to disable scroll snapping and allow free scrolling through the carousel.

[vertical](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-vertical)
Set to `true` to enable vertical mode. By default, carousels scroll horizontally.

[currentIndex](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#config-currentIndex)
The first visible slot index. This first visible slot can be read or written using this property. Setting `currentIndex` will determine if the transition can be animated by the distance being traveled.

See [goto](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#function-goto).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCarousel](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-isCarousel)
Identifies an object as an instance of [Carousel](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel) class, or subclass thereof.

[isCarousel](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-isCarousel-static)
Identifies an object as an instance of [Carousel](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel) class, or subclass thereof.

[configureSlot](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-configureSlot)
A callback function that must be provided by the developer to produce configuration objects for the slots in the carousel.

Derived classes may set this config to the name of the instance method to call. The `this` pointer will be the carousel instance.

[emptyHtml](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-emptyHtml)
The HTML to render when the carousel's [range](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-range) is empty. To avoid XSS attacks, it is safer to use [emptyText](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-emptyText) instead.

[emptyText](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-emptyText)
The text to render when the carousel's [range](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-range) is empty. This text is automatically encoded and is safe from XSS issues. To render markup when the carousel is empty, see [emptyHtml](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-emptyHtml).

[range](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-range)
The range of slot indexes to be presented in the carousel. Slot indexes greater than or equal to `range[0]` and less than `range[1]` will be rendered.

If this value is `null` or `[0, 0]`, the carousel will render no items (i.e., it will be empty). See [emptyText](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-emptyText).

By default, the carousel's range is unlimited, i.e., `range = [-Infinity, Infinity]`.

[reserveSlots](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-reserveSlots)
The number of slots to render beyond what is visible in the carousel. These reserve items are critical to giving the appearance of continuity as the carousel is being scrolled. A minimum of 1 is required and is generally sufficient for slots that are reasonably large. If slots are small (maybe less than 100px), it may be helpful to provide additional reserve slots.

[scrollOnTab](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-scrollOnTab)
Set to `true` to use [trapFocus](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-trapFocus) to scroll the carousel when tabbing to slots that are not currently visible.

NOTE: This only works when [configureSlot](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-configureSlot) produces [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel) instances.

[shrinkWrap](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-shrinkWrap)
Due to the `position: absolute` nature of carousel items, a carousel does not have a natural size. When the carousel is being sized by its container, this is not a problem, but can be an issue if the carousel is being used in a layout where its natural size would be important.

Specify `true` for the carousel to provide a natural size based on the size of its slots. This is done by setting `min-width` and/or `min-height` on the internal elements that contain the absolutely positioned slots. This may have a modest performance impact due to the required measuring of the slots to provide these minimums.

By default (`shrinkWrap = 'auto'`), the carousel enables shrinkWrap support when the carousel's main element is `position: absolute`. This can be disabled by setting `shrinkWrap = false`.

[slots](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-slots)
The number of slots to present in the carousel. When set to a number, each slot is given a percentage size (e.g., "50%" for `slots = 2`) so they fill the carousel. This is typically required when the carousel is using [shrinkWrap](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#config-shrinkWrap) (note: shrink wrapping is enabled by default for `position: absolute` carousels).

When `null`, as many slots as needed to fill the carousel are created. This can produce partially visible slots.

Setting this value to `'auto'` will similarly fill the available space, but once the required number of slots is determined, they are assigned a percentage size so that they completely fill the carousel.

[snap](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-snap)
Set to `false` to disable scroll snapping and allow free scrolling through the carousel.

[vertical](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-vertical)
Set to `true` to enable vertical mode. By default, carousels scroll horizontally.

[currentIndex](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-currentIndex)
The first visible slot index. This first visible slot can be read or written using this property. Setting `currentIndex` will determine if the transition can be animated by the distance being traveled.

See [goto](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#function-goto).

[scrolling](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#property-scrolling)
This will yield `true` when the carousel is currently scrolling.

## Functions

Functions are methods available for calling on the class

[ensurePlan](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-ensurePlan)
Decodes any `options` specified to a derived class that may be passed to [ensureVisible](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#function-ensureVisible). This method ensures the `options` object has the properties needed by [ensureVisible](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#function-ensureVisible).

[ensureVisible](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-ensureVisible)
Ensures that the given slot `index` is visible, scrolling if necessary to make it so.

[indexFromPos](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-indexFromPos)
Returns the carousel slot index given a logical scroll position (see [InfinityScroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScroller)).

[posFromIndex](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-posFromIndex)
Returns the logical scroll position (see [InfinityScroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScroller)) given a carousel slot index.

[backward](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-backward)
Step the carousel back one slot index.

[forward](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-forward)
Step the carousel forward one slot index. See [go](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#function-go).

[go](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-go)
Steps the slot index of the carousel forward or backward by the given `increment`.

[goto](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-goto)
Sets the slot index of the carousel to the given `index`.

[sync](https://bryntum.com/docs/gantt/api/Core/widget/Carousel#function-sync)
Synchronizes the scroll range and child items based on the current configuration and scroll position. This is called in response to scroll events and when the carousel is reconfigured.
