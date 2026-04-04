# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/layout/Card.md

# [Card](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card)

A helper class for containers which must manage multiple child widgets, of which only one may be visible at once such as a [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel). This class offers an active widget switching API, and optional slide-in, slide-out animations from child to child.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[animateCardChange](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#config-animateCardChange)
Specifies whether to slide tabs in and out of visibility.

[activeItem](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#config-activeItem)
The active child item.

[activeIndex](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#config-activeIndex)
The active child index.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCard](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#property-isCard)
Identifies an object as an instance of [Card](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Card) class, or subclass thereof.

[isCard](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#property-isCard-static)
Identifies an object as an instance of [Card](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Card) class, or subclass thereof.

[isChangingCard](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#property-isChangingCard)
If the layout is set to [animateCardChange](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Card#config-animateCardChange), then this property will be `true` during the animated card change.

## Functions

Functions are methods available for calling on the class

[onBeforeChildShow](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#function-onBeforeChildShow)
Detect external code showing a child. We veto that show and activate it through the API.

[onBeforeChildHide](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#function-onBeforeChildHide)
Detect external code hiding a child. We veto that show and activate an immediate sibling through the API.

[setActiveItem](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#function-setActiveItem)
Get/set active item, using index or the Widget to activate

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeActiveItemChange](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#event-beforeActiveItemChange)
The active item is about to be changed. Return `false` to prevent this.

[activeItemChange](https://bryntum.com/docs/gantt/api/Core/widget/layout/Card#event-activeItemChange)
The active item has changed.
