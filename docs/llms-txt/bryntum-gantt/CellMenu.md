# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/CellMenu.md

# [CellMenu](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu)

Right click to display context menu for cells. To invoke the cell menu in a keyboard-accessible manner, use the `SPACE` key when the cell is focused.

Default cell menu items
-----------------------

The Cell menu feature provides only one item by default:

Reference

Text

Weight

Description

`removeRow`

Delete

100

Delete row record

And all the other items are populated by the other features:

Reference

Text

Weight

Feature

Description

`cut`

Cut record

110

[RowCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste)

Cut row record

`copy`

Copy record

120

[RowCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste)

Copy row record

`paste`

Paste record

130

[RowCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste)

Paste copied row records

`search`

Search for value

200

[Search](https://bryntum.com/docs/gantt/api/#Grid/feature/Search)

Search for the selected cell text

`pinColumn`

Pin column

250

[PinColumns](https://bryntum.com/docs/gantt/api/#Grid/feature/PinColumns)

Shows a submenu to pin/unpin the column

`filterMenu`

Filter

400

[Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter)

Shows a submenu to control filtering. See [Filter submenu](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter#menu-items).

`splitGrid`

Split

500

[Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split)

Shows the "Split grid" sub menu

\> `splitHorizontally`

Horizontally

100

[Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split)

Split horizontally

\> `splitVertically`

Vertically

200

[Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split)

Split vertically

\> `splitBoth`

Both

300

[Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split)

Split both ways

`unsplitGrid`

Split

400

[Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split)

Unsplit a previously split grid

\>

first level of submenu

Customizing the menu items
--------------------------

The menu items in the Cell menu can be customized, existing items can be changed or removed, and new items can be added. This is handled using the `items` config of the feature.

Add extra items for all columns:

```
const grid = new Grid({
    features : {
        cellMenu : {
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

It is also possible to add items using columns config. See examples below.

Add extra items for a single column:

```
const grid = new Grid({
    columns: [
        {
            field         : 'city',
            text          : 'City',
            cellMenuItems : {
                columnItem : {
                    text   : 'My unique cell item',
                    icon   : 'fa fa-beer',
                    onItem : () => ...
                }
            }
        }
    ]
});
```

Remove existing item:

```
const scheduler = new Scheduler({
    features : {
        cellMenu : {
            items : {
                removeRow : false
            }
        }
    }
});
```

Customize existing item:

```
const scheduler = new Scheduler({
    features : {
        cellMenu : {
            items : {
                removeRow : {
                    text : 'Throw away',
                    icon : 'fa fa-dumpster'
                }
            }
        }
    }
});
```

It is also possible to manipulate the default items and add new items in the processing function:

```
const grid = new Grid({
    features : {
        cellMenu : {
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

Full information of the menu customization can be found in the ["Customizing the Cell menu and the Header menu"](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/contextmenu.md) guide.

This feature is **enabled** by default.

Keyboard shortcuts
------------------

This feature has the following default keyboard shortcuts:

Keys

Action

Action description

`Space`

_showContextMenuByKey_

Shows context menu for currently focused cell

`Ctrl+Space`

_showContextMenuByKey_

Shows context menu for currently focused cell

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[processItems](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#config-processItems)
A function called before displaying the menu that allows manipulations of its items. Returning `false` from this function prevents the menu being shown.

```
features : {
    cellMenu : {
        processItems({ items, record, column }) {
            // Add or hide existing items here as needed
            items.myAction = {
                text   : 'Cool action',
                icon   : 'fa fa-fw fa-ban',
                onItem : () => console.log(`Clicked ${record.name}`),
                weight : 1000 // Move to end
            };

            if (!record.allowDelete) {
                items.removeRow.hidden = true;
            }
        }
    }
},
```

[items](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#config-items)
[Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) items object containing named child menu items to apply to the feature's provided context menu.

This may add extra items as below, but you can also configure, or remove any of the default items by configuring the name of the item as `null`:

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
            removeRow : {
                // Change icon for the delete item
                icon : 'fa fa-times'
            },
            secretItem : null
        }
    }
},
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCellMenu](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#property-isCellMenu)
Identifies an object as an instance of [CellMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/CellMenu) class, or subclass thereof.

[isCellMenu](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#property-isCellMenu-static)
Identifies an object as an instance of [CellMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/CellMenu) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[showMenuFor](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#function-showMenuFor)
Shows the context menu for the provided cell.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[cellMenuBeforeShow](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#event-cellMenuBeforeShow)
This event fires on the owning grid before the context menu is shown for a cell. Allows manipulation of the items to show in the same way as in the [processItems](https://bryntum.com/docs/gantt/api/#Grid/feature/CellMenu#config-processItems).

Returning `false` from a listener prevents the menu from being shown.

[cellMenuShow](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#event-cellMenuShow)
This event fires on the owning grid after the context menu is shown for a cell.

[cellMenuItem](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#event-cellMenuItem)
This event fires on the owning grid when an item is selected in the cell context menu.

[cellMenuToggleItem](https://bryntum.com/docs/gantt/api/Grid/feature/CellMenu#event-cellMenuToggleItem)
This event fires on the owning grid when a check item is toggled in the cell context menu.
