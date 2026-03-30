# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/feature/base/ContextMenuBase.md

# [ContextMenuBase](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase)

Abstract base class used by other context menu features.

Keyboard shortcuts
------------------

This base class has the following default keyboard shortcuts:

Keys

Action

Action description

Space

showContextMenuByKey

Shows context menu for currently focused element

Ctrl+Space

showContextMenuByKey

Shows context menu for currently focused element

For more information on how to customize keyboard shortcuts, please see our guide (Guides/Customization/Keyboard shortcuts)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[type](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#config-type)
This is a type of the context menu used to generate correct names for methods and events. Should be in camel case. Required to be set in subclass.

[menu](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#config-menu)
A config which will be applied when creating the Menu component.

[items](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#config-items)
[Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) items object containing named child menu items to apply to the feature's provided context menu.

This may add extra items as below, but may also remove any of the default items by configuring the name of the item as `null`.

```
features : {
    cellMenu : {
        // This object is applied to the Feature's predefined default items
        items : {
            switchToDog : {
                text : 'Dog',
                icon : 'fa fa-fw fa-dog',
                onItem({record}) {
                    record.dog = true;
                    record.cat = false;
                },
                weight : 500     // Make this second from end
            },
            switchToCat : {
                text : 'Cat',
                icon : 'fa fa-fw fa-cat',
                onItem({record}) {
                    record.dog = false;
                    record.cat = true;
                },
                weight : 510     // Make this sink to end
            },
            add : null // We do not want the "Add" submenu to be available
        }
    }
}
```

[namedItems](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#config-namedItems)
An object containing default config objects which may be referenced by name in the [items](https://bryntum.com/docs/gantt/api/#Core/feature/base/ContextMenuBase#config-items) config. For example, a specialized [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) subclass may have a `namedItems` default value defined like this:

```
 namedItems : {
     removeRow : {
         text : 'Remove row',
         onItem() {
             this.ownerGrid.remove(this.ownerGrid.selectedRecord);
         }
     }
 }
```

Then whenever that subclass is instantiated and configured with an [items](https://bryntum.com/docs/gantt/api/#Core/feature/base/ContextMenuBase#config-items) object, the `items` may use the above defaults like this:

```
 items : {
     removeRow : true,   // The referenced namedItem will be applied to this
     otherItemRef : {
         text : 'Option 2',
         onItem() { }
     }
}
```

If a menu instance (or its class) does not include `removeRow` in its `items`, no menu item will be created.

[triggerEvent](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#config-triggerEvent)
Event which is used to show context menu. Available options are: 'contextmenu', 'click' and 'dblclick'. Default value is used from [contextMenuTriggerEvent](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-contextMenuTriggerEvent)

[clickTriggerSelector](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#config-clickTriggerSelector)
A CSS selector targeting an element, such as an ellipsis icon that when clicked will trigger the menu to show.

[preventNativeMenu](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#config-preventNativeMenu)
Set to `true` to prevent the native menu from showing when there are no menu items to show, or you manually prevent the menu from showing in an event listener.

[keyMap](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Core/feature/base/ContextMenuBase#keyboard-shortcuts) for details

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isContextMenuBase](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#property-isContextMenuBase)
Identifies an object as an instance of [ContextMenuBase](https://bryntum.com/docs/gantt/api/#Core/feature/base/ContextMenuBase) class, or subclass thereof.

[isContextMenuBase](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#property-isContextMenuBase-static)
Identifies an object as an instance of [ContextMenuBase](https://bryntum.com/docs/gantt/api/#Core/feature/base/ContextMenuBase) class, or subclass thereof.

[menu](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#property-menu)
Gets the Menu instance that this feature is using.

[preventNativeMenu](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#property-preventNativeMenu)
Set to `true` to prevent the native menu from showing when there are no menu items to show, or you manually prevent the menu from showing in an event listener.

[menuContext](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#property-menuContext)
An informational object containing contextual information about the last activation of the context menu. The base properties are listed below. Some subclasses may add extra contextual information such as `eventRecord` and `resourceRecord` to the block.

[baseItems](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#property-baseItems)
Returns the base, configured-in menu items set from the configured items, taking into account the namedItems the feature offers.

## Functions

Functions are methods available for calling on the class

[showContextMenu](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#function-showContextMenu)
Shows the context menu.

[hideContextMenu](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#function-hideContextMenu)
Hides the context menu

[shouldShowMenu](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#function-shouldShowMenu)
Override this function and return `false` to prevent the context menu from being shown. Returns `true` by default. Returning false will by default make the native OS menu show, unless you configure [preventNativeMenu](https://bryntum.com/docs/gantt/api/#Core/feature/base/ContextMenuBase#config-preventNativeMenu)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[contextMenuItem](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#event-contextMenuItem)
This event fires on the owning widget when an item is selected in the context menu.

[contextMenuToggleItem](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#event-contextMenuToggleItem)
This event fires on the owning widget when a check item is toggled in the context menu.

## Typedefs

Typedefs are type definitions for the class

[MenuItemEntry](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#typedef-MenuItemEntry)
A value used to configure a menu item in a menu's `items` object. Use an object to configure a menu item. See [MenuItem](https://bryntum.com/docs/gantt/api/#Core/widget/MenuItem) config. Use boolean `false` or `null` value to disable menu item in a preconfigured `items`.

[MenuContext](https://bryntum.com/docs/gantt/api/Core/feature/base/ContextMenuBase#typedef-MenuContext)
A context object passed to any `processItems` method defined for a context menu feature, and also the basis of events fired by context menu features.
