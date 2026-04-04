# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/RTL.md

# [RTL](https://bryntum.com/docs/gantt/api/Core/widget/mixin/RTL)

Mixin for RTL operation

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[rtl](https://bryntum.com/docs/gantt/api/Core/widget/mixin/RTL#config-rtl)
This may be configured as `true` to make the widget's element use the `direction:rtl` style.

All descendant widgets, including any [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) widgets will inherit this setting.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRTL](https://bryntum.com/docs/gantt/api/Core/widget/mixin/RTL#property-isRTL)
Identifies an object as an instance of [RTL](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/RTL) class, or subclass thereof.

[isRTL](https://bryntum.com/docs/gantt/api/Core/widget/mixin/RTL#property-isRTL-static)
Identifies an object as an instance of [RTL](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/RTL) class, or subclass thereof.

[rtl](https://bryntum.com/docs/gantt/api/Core/widget/mixin/RTL#property-rtl)
If a widget is rendered into an element which has computed style `direction:rtl`, this property will be set to `true`

Rendering a widget into an element which, either by a CSS rule, or by its inline `style` has an explicit direction will cause the widget to use that direction regardless of the owning document's direction.

In this way, an RTL widget may operate normally inside an LTR page and vice versa.
