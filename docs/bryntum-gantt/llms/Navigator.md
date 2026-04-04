# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/Navigator.md

# [Navigator](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator)

A helper class which allows keyboard navigation within the [target](https://bryntum.com/docs/gantt/api/#Core/helper/util/Navigator#config-target) element.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[ownerCmp](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-ownerCmp)
The owning Widget which is using this Navigator.

[itemsTabbable](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-itemsTabbable)
If the items in the owning widget are naturally tabbable, then the Navigator does not need to listen for navigation keys and move focus. It just reacts to natural focus movement.

[target](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-target)
The encapsulating element in which navigation takes place.

[keyEventTarget](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-keyEventTarget)
The element which provides key events for navigation. Optional. Defaults to the [target](https://bryntum.com/docs/gantt/api/#Core/helper/util/Navigator#config-target) element.

[processEvent](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-processEvent)
An optional key event processor which may preprocess the key event. Returning `null` prevents processing of the event.

[itemSelector](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-itemSelector)
A query selector which identifies descendant elements within the [target](https://bryntum.com/docs/gantt/api/#Core/helper/util/Navigator#config-target) which are navigable.

[activeItem](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-activeItem)
The currently focused element within the [target](https://bryntum.com/docs/gantt/api/#Core/helper/util/Navigator#config-target).

[focusCls](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-focusCls)
A CSS class name to add to focused elements.

[keys](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-keys)
An object containing key definitions keyed by the key name eg:

```
 keys : {
     "CTRL+Space" : 'onCtrlSpace',
     Enter        : 'onEnterKey'
 }
```

The [ownerCmp](https://bryntum.com/docs/gantt/api/#Core/helper/util/Navigator#config-ownerCmp) is used as the `this` reference and to resolve string method names.

The following arguments are passed to the handling method:

* keyEvent : The key event.
* navigator : This Navigator instance.
* activeItem : The currently focused element.

Modified key names must be created prepending one or more `'CTRL+'`, `'SHIFT+'`, `'ALT+'` in that order, for example `"CTRL+SHIFT+Enter" : 'showMenu'`

[allowCtrlKey](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-allowCtrlKey)
Configure as `true` to also navigate when the `CTRL` modifier key is used along with navigation keys.

[allowShiftKey](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-allowShiftKey)
Configure as `true` to also navigate when the `SHIFT` modifier key is used along with navigation keys.

[activateOnMouseover](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-activateOnMouseover)
Configure as `true` to activate items on mouseover. This is used by the Combo field when using a List as its dropdown.

[disabled](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-disabled)
Configure as, or set to `true` to disable the processing of keys.

[columnCount](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#config-columnCount)
The number of columns if the navigable items are in a flexbox or grid layout.

This is used to determine the action taken when using UP and DOWN arrow keys.

This is calculated automatically from the `grid-template-columns` style of the item container if possible. If using a flexbox layout, and there is a regular number of columns on every row, specify the number of columns there will be in each row.

## Functions

Functions are methods available for calling on the class

[getAdjacent](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#function-getAdjacent)
Returns the next or previous navigable element starting from the passed `from` element, navigating in the passed direction.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[navigate](https://bryntum.com/docs/gantt/api/Core/helper/util/Navigator#event-navigate)
Fired when a user gesture causes the active item to change _or become `null`_.
