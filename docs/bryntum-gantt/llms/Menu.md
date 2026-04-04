# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Menu.md

# [Menu](https://bryntum.com/docs/gantt/api/Core/widget/Menu)

Menu widget, displays a list of items which the user can select from using mouse or keyboard. A menu can also have submenus by configuring the [menu](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem#config-menu) config of a `MenuItem`. A menu is typically only shown when right-clicking an element in the DOM. Try right-clicking the `DIV` rectangle below.

A common usecase is to attach a `menu` to a [Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button), which is supported via the [menu config](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-menu).

Menu item interaction handling in a complex widget
--------------------------------------------------

In the case of a menu which is part of a complex UI within a larger Bryntum widget, use of the string form for handlers is advised. A handler which starts with `'up.'` will be resolved by looking in owning widgets of the Menu. For example a Calendar may have handlers for its MenuItems configured in:

```
new Calendar({
    appendTo : document.body,
    project  : myProjectConfig,
    tbar  : {
        items : {
            settings : {
                type : 'button',
                text : 'Settings',

                // High weight so it goes at the end
                weight : 800,
                menu   : [{
                    text     : 'Hide non-working days',
                    checked  : false,

                     // The Menu's ownership will be traversed to find this function name.
                    onToggle : 'up.toggleHideNonWorkingDays'
                }, {
                    text    : 'Clear changes',

                     // The Menu's ownership will be traversed to find this function name.
                    onItem : 'up.clearUncommittedChanges'
                }]
            }
        }
    },

    // Menu handlers found here
    toggleHideNonWorkingDays({ checked }) {
        // Use Calendar API which creates event in the selected date
        this.hideNonWorkingDays = checked;
    },

    clearUncommittedChanges() {
        // Clear changes to our event store which are not yet synced to the server
        this.eventStore.revertChanges();
    }
});
```

```
let menu = new Menu({
    forElement : btn.element,
    items      : [
        {
            icon : 'b-icon b-icon-add',
            text : 'Add'
        },
        {
            icon : 'b-icon b-icon-trash',
            text : 'Remove'
        },
        {
            icon     : 'b-icon b-icon-lock',
            disabled : true,
            text     : 'I am disabled'
        },
        {
            text : 'Sub menu',
            menu : [{
                icon : 'fa fa-play',
                text : 'Play'
            }]
        }
    ],
    // Method is called for all ancestor levels
    onItem({ item }) {
        Toast.show('You clicked ' + item.text);
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[focusOnHover](https://bryntum.com/docs/gantt/api/Core/widget/Menu#config-focusOnHover)
Specify false to prevent the menu from getting focus when hovering items

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMenu](https://bryntum.com/docs/gantt/api/Core/widget/Menu#property-isMenu)
Identifies an object as an instance of [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) class, or subclass thereof.

[isMenu](https://bryntum.com/docs/gantt/api/Core/widget/Menu#property-isMenu-static)
Identifies an object as an instance of [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) class, or subclass thereof.

[currentSubMenu](https://bryntum.com/docs/gantt/api/Core/widget/Menu#property-currentSubMenu)
Currently open sub menu, if any

[isSubMenu](https://bryntum.com/docs/gantt/api/Core/widget/Menu#property-isSubMenu)
Returns true if this menu is a sub menu. To find out which menu is the parent, check [parentMenu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu#property-parentMenu).

[selectedElement](https://bryntum.com/docs/gantt/api/Core/widget/Menu#property-selectedElement)
Get/set focused menu item. Shows submenu if newly focused item has a menu and is not disabled.

[parentMenu](https://bryntum.com/docs/gantt/api/Core/widget/Menu#property-parentMenu)
Gets the parent Menu if this Menu is a submenu, or `undefined`.

[rootMenu](https://bryntum.com/docs/gantt/api/Core/widget/Menu#property-rootMenu)
Gets this menus root menu, the very first menu shown in a sub menu hierarchy

## Functions

Functions are methods available for calling on the class

[onMouseClick](https://bryntum.com/docs/gantt/api/Core/widget/Menu#function-onMouseClick)
Activates a menu item if user clicks on it

[onMouseOver](https://bryntum.com/docs/gantt/api/Core/widget/Menu#function-onMouseOver)
Activates menu items on hover. On real mouse hover, not on a touchstart.

[onInternalKeyDown](https://bryntum.com/docs/gantt/api/Core/widget/Menu#function-onInternalKeyDown)
Keyboard navigation. Up/down, close with esc, activate with enter

[triggerElement](https://bryntum.com/docs/gantt/api/Core/widget/Menu#function-triggerElement)
Activate a menu item (from its element)

[openSubMenu](https://bryntum.com/docs/gantt/api/Core/widget/Menu#function-openSubMenu)
Opens a submenu anchored to a menu item

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[item](https://bryntum.com/docs/gantt/api/Core/widget/Menu#event-item)
A descendant menu item has been activated.

Note that this event bubbles up through parents and can be listened for on a top level [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) for convenience.

[toggle](https://bryntum.com/docs/gantt/api/Core/widget/Menu#event-toggle)
The checked state of a descendant menu item has changed.

Note that this event bubbles up through parents and can be listened for on a top level [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) for convenience.
