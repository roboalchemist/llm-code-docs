# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/layout/Box.md

# [Box](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box)

A layout that applies `display: flex` to the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) of its container to layout child items. This defaults to a horizontal layout of items, also known as an `'hbox'`.

```
 layout : {
     type : 'box'   // or equivalently, 'hbox'
 }
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[align](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-align)
Sets the [align-items](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) style of the [owner's](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#property-owner) [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).

[contentAlign](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-contentAlign)
Sets the [align-content](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/align-content) style of the [owner's](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#property-owner) [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).

[direction](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-direction)
Sets the [direction](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) style of the [owner's](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#property-owner) [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement). This config is not set directly. Set [horizontal](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#config-horizontal), [vertical](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#config-vertical), and/or [reverse](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#config-reverse) instead.

[horizontal](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-horizontal)
Set this value to `false` to set the [flex-direction](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) style of the [owner's](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#property-owner) [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) to `column`. Or alternatively, set [vertical](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#config-vertical) to `true`.

[justify](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-justify)
Sets the [justify-content](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content) style of the [owner's](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#property-owner) [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).

[reverse](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-reverse)
Set this value to `true` to add `'-reverse'` to the [flex-direction](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) style of the [owner's](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#property-owner) [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement). This config combines with [horizontal](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#config-horizontal) or [vertical](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#config-vertical) to set the `flex-direction` style.

[wrap](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-wrap)
Sets the [flex-wrap](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap) style of the [owner's](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#property-owner) [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).

The value of `true` is equivalent to `'wrap'`, `false` is equivalent to `'nowrap'`, and `'reverse'` is equivalent to `'wrap-reverse'`.

```
 layout : {
     type : 'box',
     wrap : false        // equivalent to 'nowrap'
     wrap : true         // equivalent to 'wrap'
     wrap : 'reverse'    // equivalent to 'wrap-reverse'
 }
```

[gap](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-gap)
The amount of gap between the element of child items.

[vertical](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#config-vertical)
Set this value to `true` to set the [flex-direction](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) style of the [owner's](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#property-owner) [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) to `column`. Or alternatively, set [horizontal](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box#config-horizontal) to `false`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isBox](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#property-isBox)
Identifies an object as an instance of [Box](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box) class, or subclass thereof.

[isBox](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#property-isBox-static)
Identifies an object as an instance of [Box](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box) class, or subclass thereof.

[gap](https://bryntum.com/docs/gantt/api/Core/widget/layout/Box#property-gap)
The amount of gap between the element of child items.
