# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/ResourceMenu.md

# [ResourceMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu)

Applicable only for Scheduler in `vertical` mode. Right click resource header cells to display a context menu.

To invoke the menu in a keyboard-accessible manner, use the `SPACE` key when a resource cell is focused.

### Default menu items

The ResourceMenu feature provides only one item by default:

Reference

Text

Weight

Description

`remove`

Delete

100

Delete the resource

### Customizing the menu items

The menu items in the resource menu can be customized, existing items can be changed or removed, and new items can be added. This is handled using the `items` config of the feature.

Add extra items for all columns:

```
const scheduler = new Scheduler({
    mode     : 'vertical',
    features : {
        resourceMenu : {
            items : {
                extraItem : {
                    text   : 'My cell item',
                    icon   : 'fa fa-bus',
                    weight : 200,
                    onItem : () => ...
                }
            }
        }
    }
});
```

Remove an existing item:

```
const scheduler = new Scheduler({
    mode     : 'vertical',
    features : {
        resourceMenu : {
            items : {
                remove : null
            }
        }
    }
});
```

Customize existing item:

```
const scheduler = new Scheduler({
    mode     : 'vertical',
    features : {
        resourceMenu : {
            items : {
                remove : {
                    text : 'Remove',
                    icon : 'fa fa-dumpster'
                }
            }
        }
    }
});
```

It is also possible to manipulate the default items and add new items in the processing function:

```
const scheduler = new Scheduler({
    mode     : 'vertical',
    features : {
        resourceMenu : {
            processItems({items, record}) {
                if (record.cost > 5000) {
                    items.myItem = { text : 'Split cost' };
                }
            }
        }
    }
});
```

The `processItems` implementation may be an `async` function which `awaits` a result to mutate the `items` object.

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[processItems](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu#config-processItems)
A function called before displaying the menu that allows manipulations of its items. Returning `false` from this function prevents the menu being shown.

```
features : {
    resourceMenu : {
        processItems({ items, record, column }) {
            // Add or hide existing items here as needed
            items.myAction = {
                text   : 'Cool action',
                icon   : 'fa fa-fw fa-ban',
                onItem : () => console.log(`Clicked ${record.name}`),
                weight : 1000 // Move to end
            };

            if (!record.allowDelete) {
                items.remove.hidden = true;
            }
        }
    }
},
```

[items](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu#config-items)
[Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) items object containing named child menu items to apply to the feature's provided context menu.

This may add extra items as below, but you can also configure, or remove any of the default items by configuring the name of the item as `null`

```
features : {
    resourceMenu : {
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
            remove : {
                // Change icon for the delete item
                icon : 'fa fa-times'
            }
        }
    }
},
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu#property-isResourceMenu)
Identifies an object as an instance of [ResourceMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceMenu) class, or subclass thereof.

[isResourceMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu#property-isResourceMenu-static)
Identifies an object as an instance of [ResourceMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceMenu) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[resourceMenuBeforeShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu#event-resourceMenuBeforeShow)
This event fires on the owning scheduler before the context menu is shown for a resource. Allows manipulation of the items to show in the same way as in the [processItems](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceMenu#config-processItems).

Returning `false` from a listener prevents the menu from being shown.

[resourceMenuShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu#event-resourceMenuShow)
This event fires on the owning scheduler after the context menu is shown for a resource.

[resourceMenuItem](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu#event-resourceMenuItem)
This event fires on the owning scheduler when an item is selected in the context menu.

[resourceMenuToggleItem](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceMenu#event-resourceMenuToggleItem)
This event fires on the owning grid when a check item is toggled in the context menu.
