# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Splitter.md

# [Splitter](https://bryntum.com/docs/gantt/api/Core/widget/Splitter)

A simple splitter widget that resizes the elements next to it or above/below it depending on orientation.

Double click on the splitter to share the space evenly between the two neighboring elements.

CTRL (CMD on Mac) double click to share the space evenly between _all_ siblings in the parent container

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[orientation](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#config-orientation)
The splitter's orientation, configurable with 'auto', 'horizontal' or 'vertical'.

'auto' tries to determine the orientation by either checking the `flex-direction` of the parent element or by comparing the positions of the closest sibling elements to the splitter. If they are above and below 'horizontal' is used, if not it uses 'vertical'.

```
new Splitter({
   orientation : 'horizontal'
});
```

To receive the actually used orientation when configured with 'auto', see [currentOrientation](https://bryntum.com/docs/gantt/api/#Core/widget/Splitter#property-currentOrientation).

[showButtons](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#config-showButtons)
Set to `true` to show the splitter's collapse/expand buttons, or to 'start' or 'end' to only show buttons pointing to the previous or next element respectively.

Setting to `false` will hide the buttons.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSplitter](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#property-isSplitter)
Identifies an object as an instance of [Splitter](https://bryntum.com/docs/gantt/api/#Core/widget/Splitter) class, or subclass thereof.

[isSplitter](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#property-isSplitter-static)
Identifies an object as an instance of [Splitter](https://bryntum.com/docs/gantt/api/#Core/widget/Splitter) class, or subclass thereof.

[orientation](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#property-orientation)
Splitter orientation, see [orientation](https://bryntum.com/docs/gantt/api/#Core/widget/Splitter#config-orientation). When set to 'auto' then actually used orientation can be retrieved using [currentOrientation](https://bryntum.com/docs/gantt/api/#Core/widget/Splitter#property-currentOrientation).

[currentOrientation](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#property-currentOrientation)
Get actually used orientation, which is either the configured value for `orientation` or if configured with 'auto' the currently used orientation.

## Functions

Functions are methods available for calling on the class

[syncState](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#function-syncState)
Determine orientation when set to `'auto'` and detects neighboring widgets to monitor their hidden/collapsed states.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[dragStart](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#event-dragStart)
Fired when a drag starts

[drag](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#event-drag)
Fired while dragging

[drop](https://bryntum.com/docs/gantt/api/Core/widget/Splitter#event-drop)
Fired after a drop
