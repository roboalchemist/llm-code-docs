# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Tool.md

# [Tool](https://bryntum.com/docs/gantt/api/Core/widget/Tool)

Base class for tools.

May be configured with a `cls` and a `handler` which is a function (or name of a function) in the owning Panel.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[align](https://bryntum.com/docs/gantt/api/Core/widget/Tool#config-align)
Specify `'start'` to place the tool before the owner's central element (e.g., the `title` of the panel).

[href](https://bryntum.com/docs/gantt/api/Core/widget/Tool#config-href)
If provided, turns the tool into a link

[handler](https://bryntum.com/docs/gantt/api/Core/widget/Tool#config-handler)
The function to call when this tool is clicked. May be a function or function name prepended by `"up."` that is resolvable in an ancestor component (such as an owning Grid, Scheduler, Calendar, Gantt or TaskBoard)

[repeat](https://bryntum.com/docs/gantt/api/Core/widget/Tool#config-repeat)
A [ClickRepeater](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater) config object to specify how click-and-hold gestures repeat the click action.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTool](https://bryntum.com/docs/gantt/api/Core/widget/Tool#property-isTool)
Identifies an object as an instance of [Tool](https://bryntum.com/docs/gantt/api/#Core/widget/Tool) class, or subclass thereof.

[isTool](https://bryntum.com/docs/gantt/api/Core/widget/Tool#property-isTool-static)
Identifies an object as an instance of [Tool](https://bryntum.com/docs/gantt/api/#Core/widget/Tool) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[click](https://bryntum.com/docs/gantt/api/Core/widget/Tool#event-click)
Fires when the tool is clicked

[action](https://bryntum.com/docs/gantt/api/Core/widget/Tool#event-action)
Fires when the default action is performed (the button is clicked)
