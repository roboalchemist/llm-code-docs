# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Toolbar.md

# [Toolbar](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar)

A container widget that can contain Buttons or other widgets, and is docked to the bottom or top of a [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel).

Arranging widgets
-----------------

When passing an object (the approach we recommend for defining items), you can use `->` as the property value to push widgets to the right side (in LTR):

```
items    : {
    leftButton1  : { text : 'Left button 1', icon : 'fa fa-plus' },
    leftButton2  : { text : 'Left button 2', icon : 'fa fa-minus' },
    spacer       : '->',
    rightButton1 : { text : 'Right button 1', icon : 'fa fa-gear'}
}
```

When passing an array of items, you can similarly use the special `->` item to push widgets to the right side:

```
items    : [
    { text : 'Left button 1', icon : 'fa fa-plus' },
    { text : 'Left button 2', icon : 'fa fa-minus' },
    '->',
    { text : 'Right button 1', icon : 'fa fa-gear'}
]
```

Toolbar items can be drag-dropped
---------------------------------

You can let users reorder the toolbar items by setting [enableReordering](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar#config-enableReordering) to `true`.

This is not supported if you use `weight` to order the items.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[enableReordering](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#config-enableReordering)
Set to `true` to allow users to reorder items in this toolbar using drag-drop

[items](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#config-items)
An object containing typed child widget config objects or [Widgets](https://bryntum.com/docs/gantt/api/#Core/widget/Widget). Can also be specified as an array.

If configured as an Object, the property names are used as the child component's [ref](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) name, and the value is the child component's config object.

```
 new Toolbar({
     appendTo : document.body
     items    : {
         button : {
             type : 'button',
             onClick() { ... }
         }
     }
 })
```

Some special items can also be added:

* `->` Pushes following items to the other side
* `|` Adds a vertical separator

```
 new Toolbar({
     appendTo : document.body
     items    : {
         button : {
             type : 'button',
             text : 'Click me',
             onClick() { ... }
         },
         separator : '|',
         name : {
             type : 'textfield',
             label : 'Enter name'
         },
         // Align following items to the end of the toolbar
         spacer : '->',
         saveButton : {
             type : 'button',
             text : 'Save',
             onClick() { ... }
         }
     }
 })
```

[overflow](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#config-overflow)
How this Toolbar should deal with items that overflow its main axis.

Values may be:

* `'menu'` A button with a menu is shown and the menu contains the overflowing items.
* `'scroll'` The items overflow and mey be scrolled into view using the mouse or scroll buttons.
* `null` Disable overflow handling

When mode is `'menu'`, clones of overflowing toolbar item are created and added to a Menu. Any config changes to the original toolbar item are propagated to the menu's clone, so disabling a toolbar item will make the clone in the menu disabled.

The clone of an input field will propagate its `value` changes back to the original. The overflow button, its menu, and the clones should not be accessed or manipulated by application code.

Note that cloned items will be allocated a unique, generated ID because all IDs must be unique, so CSS targeting an element ID will not apply to a clone in the overflow menu.

Values may also be specified in object form containing the following properties:

[widgetCls](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#config-widgetCls)
Custom CSS class to add to toolbar widgets

[ignoreParentReadOnly](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#config-ignoreParentReadOnly)
Determines if the toolbars read-only state should be controlled by its parent.

When set to `true`, setting a parent container to read-only will not affect the widget. When set to `false`, it will affect the widget.

[labelPosition](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#config-labelPosition)
Toolbars override the default `labelPosition` for containers, placing labels before the input fields independent of which theme is used.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isToolbar](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#property-isToolbar)
Identifies an object as an instance of [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar) class, or subclass thereof.

[isToolbar](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#property-isToolbar-static)
Identifies an object as an instance of [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar) class, or subclass thereof.

[enableReordering](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#property-enableReordering)
Set to `true` to allow users to reorder items in this toolbar using drag-drop

[labelPosition](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#property-labelPosition)
Toolbars override the default `labelPosition` for containers, placing labels before the input fields independent of which theme is used.

## Functions

Functions are methods available for calling on the class

[getEvictionList](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#function-getEvictionList-static)
Returns the Core.widget.Widget\[\] of items to hide to clear an overflow. The `visibleItems` array should be in order of the `items` in the container.

[onDrop](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#function-onDrop)
Handle drop

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeItemDragStart](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#event-beforeItemDragStart)
This event is fired on the owning Toolbar prior to starting a drag gesture. The drag is canceled if a listener returns `false`.

[itemDragStart](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#event-itemDragStart)
This event is fired when a drag gesture has started.

[itemDrop](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#event-itemDrop)
This event is fired when an item is dropped

## Typedefs

Typedefs are type definitions for the class

[ToolbarItems](https://bryntum.com/docs/gantt/api/Core/widget/Toolbar#typedef-ToolbarItems)
Toolbar items:

* `'->'` - push widgets to the right side
* `'|'` - add toolbar separator
* `WidgetConfig` - object with widget configuration
