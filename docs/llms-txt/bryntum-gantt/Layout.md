# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/layout/Layout.md

# [Layout](https://bryntum.com/docs/gantt/api/Core/widget/layout/Layout)

A helper class used by [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container)s which renders child widgets to their [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement). It also adds the Container's [itemCls](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-itemCls) class to child items.

Subclasses may modify the way child widgets are rendered, or may offer APIs for manipulating the child widgets.

The [Card](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Card) layout class offers slide-in, slide-out animation of multiple child widgets. [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel) uses Card layout.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[owner](https://bryntum.com/docs/gantt/api/Core/widget/layout/Layout#config-owner)

[containerCls](https://bryntum.com/docs/gantt/api/Core/widget/layout/Layout#config-containerCls)
The CSS class which should be added to the owning [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container)'s. [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).

[itemCls](https://bryntum.com/docs/gantt/api/Core/widget/layout/Layout#config-itemCls)
The CSS class which should be added to the encapsulating element of child items.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[owner](https://bryntum.com/docs/gantt/api/Core/widget/layout/Layout#property-owner)
The owning Widget.

## Functions

Functions are methods available for calling on the class

[syncConfigLater](https://bryntum.com/docs/gantt/api/Core/widget/layout/Layout#function-syncConfigLater)
Registers a layout `config` property that cannot be acted upon at this time but must wait for the `owner` to fully render its elements (in particular the `contentElement`).

[syncConfigStyle](https://bryntum.com/docs/gantt/api/Core/widget/layout/Layout#function-syncConfigStyle)
Sets the specified `style` to the value of the config given its `name`.
