# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/MenuItem.md

# [MenuItem](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem)

A widget representing a single menu item in a [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu). May be configured with a [checked](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#config-checked) state which creates a checkbox which may be toggled. Can also be [disabled](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-disabled), which affects item appearance and blocks interactions.

Fires events when activated which bubble up through the parent hierarchy and may be listened for on an ancestor. See [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) for more details on usage.

To add a border above a menu item, you can set [separator](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#config-separator) to `true`. The separator is automatically hidden if the menu item is the first visible item in the menu.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[checked](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-checked)
If configured with a `Boolean` value, a checkbox is displayed as the start icon, and the [toggle](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#event-toggle) event is fired when the checked state changes. `String` value allows to link value by reference name.

Example:

```
menu : {
    items : {
        fill : {
            text    : 'Fill width',
            checked : 'up.resourceColumns.fillWidth'
        },
        fit : {
            text        : 'Fit width',
            checked     : false,
            closeParent : true
        }
    }
}
```

[separator](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-separator)
Set to `true` to display a border above this menu item, if there are other visible menu items before it.

[toggleGroup](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-toggleGroup)
Indicates that this menu item is part of a group where only one can be checked. Assigning a value also sets `toggleable` to `true`.

```
const yesButton = new Button({
   toggleGroup : 'yesno',
   text        : 'Yes'
});

const noButton = new Button({
   toggleGroup : 'yesno',
   text        : 'No'
});
```

[menu](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-menu)
A submenu configuration object, or an array of MenuItem configuration objects from which to create a submenu.

Configuration object example:

```
new Menu({
    // Menu items
    items : {
        move : {
            text : 'Main item',
            menu : {
                // Submenu items
                firstItem : {
                    text : 'Sub-item 1',
                    onItem({ eventRecord }) {}
                },
                secondItem : {
                    text : 'Sub-item 2',
                    onItem({ eventRecord }) {}
                }
            }
        }
    }
});
```

Array of items example:

```
new Menu({
    // Menu items
    items : {
        move : {
            text : 'Main item',
            // Submenu items
            menu : [
                {
                    text : 'Sub-item 1',
                    onItem({ eventRecord }) {}
                },
                {
                    text : 'Sub-item 2',
                    onItem({ eventRecord }) {}
                }
            ]
        }
    }
});
```

Note that this does not have to be a Menu. The `type` config can be used to specify any widget as the submenu.

```
new Menu({
    // Menu items
    items : {
        move : {
            text : 'Main item',
            // Submenu items
            menu : [
                {
                    type  : 'textfield',
                    label : 'Type here'
                },
                {
                    type : 'button',
                    text : 'Confirm'
                }
            ]
        }
    }
});
```

[icon](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-icon)
Item icon class.

All [Font Awesome](https://bryntum.com/docs/gantt/api/https://fontawesome.com/cheatsheet) icons may also be specified as `'fa-' + iconName`.

Otherwise this is a developer-defined CSS class string which results in the desired icon.

[text](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-text)
The text to be displayed in the item. The text is automatically HTML encoded.

[closeParent](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-closeParent)
By default, upon activate, non-checkbox menu items will collapse the owning menu hierarchy.

Configure this as `false` to cause the menu to persist after activating an item

[href](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-href)
If provided, turns the menu item into a link

[target](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#config-target)
The `target` attribute for the [href](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#config-href) config

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMenuItem](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#property-isMenuItem)
Identifies an object as an instance of [MenuItem](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem) class, or subclass thereof.

[isMenuItem](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#property-isMenuItem-static)
Identifies an object as an instance of [MenuItem](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem) class, or subclass thereof.

[toggleGroup](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#property-toggleGroup)
Indicates that this menu item is part of a group where only one can be checked. Assigning a value also sets `toggleable` to `true`.

```
const yesButton = new Button({
   toggleGroup : 'yesno',
   text        : 'Yes'
});

const noButton = new Button({
   toggleGroup : 'yesno',
   text        : 'No'
});
```

[menu](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#property-menu)
Returns the instantiated menu widget as configured by [menu](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#config-menu).

[text](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#property-text)
The text to be displayed in the item. The text is automatically HTML encoded.

[checked](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#property-checked)
Get/sets the checked state of this `MenuItem` and fires the [toggle](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#event-toggle) event upon change.

Note that this must be configured as a `Boolean` to enable the checkbox UI.

## Functions

Functions are methods available for calling on the class

[doAction](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#function-doAction)
Actions this item. Fires the [item](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#event-item) event, and if this is a [checked](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#config-checked) item, toggles the checked state, firing the [toggle](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#event-toggle) event.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[item](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#event-item)
This menu item has been activated.

Note that this event bubbles up through parents and can be listened for on a top level [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) for convenience.

[toggle](https://bryntum.com/docs/gantt/api/Core/widget/MenuItem#event-toggle)
The checked state of this menu item has changed.

Note that this event bubbles up through parents and can be listened for on a top level [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) for convenience.
