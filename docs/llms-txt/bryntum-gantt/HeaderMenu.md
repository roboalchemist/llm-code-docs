# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/HeaderMenu.md

# [HeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu)

Right click column header or focus it and press SPACE key to show the context menu for headers.

### Default header menu items

The Header menu has no default items provided by the `HeaderMenu` feature, but there are other features that populate the header menu with the following items:

Reference

Text

Weight

Feature

Description

`filter`

Filter

100

[Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter)

Shows the filter popup to add a filter

`filterEdit`

Edit filter

100

[Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter)

Shows the filter popup to change/remove a filter

`filterRemove`

Remove filter

110

[Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter)

Stops filtering by selected column field

`toggleFilterBar`

Hide filter bar / Show filter bar

120

[FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar)

Toggles filter bar visibility

`columnPicker`

Columns

200

[ColumnPicker](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnPicker)

Shows a submenu to control columns visibility

\>`column.id`\*

column.text\*

[ColumnPicker](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnPicker)

Check item to hide/show corresponding column

`pinColumn`

Pin column

250

[PinColumns](https://bryntum.com/docs/gantt/api/#Grid/feature/PinColumns)

Shows a submenu to pin/unpin the column

`hideColumn`

Hide column

210

[ColumnPicker](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnPicker)

Hides selected column

`rename`

Rename column text

215

[ColumnRename](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnRename)

Edits the header text of the column

`toggleCollapse`

Collapse column / Expand column

215

This feature

Expands or collapses a collapsible column

`movePrev`

Move previous

220

This feature

Moves selected column before its previous sibling

`moveNext`

Move next

230

This feature

Moves selected column after its next sibling

`sortAsc`

Sort ascending

300

[Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort)

Sort by the column field in ascending order

`sortDesc`

Sort descending

310

[Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort)

Sort by the column field in descending order

`multiSort`

Multi sort

320

[Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort)

Shows a submenu to control multi-sorting

\>`addSortAsc`

Add ascending sorting

330

[Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort)

Adds ascending sorter using the column field

\>`addSortDesc`

Add descending sorting

340

[Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort)

Adds descending sorter using the column field

\>`removeSorter`

Remove sorter

350

[Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort)

Stops sorting by selected column field

`groupAsc`

Group ascending

400

[Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group)

Group by the column field in ascending order

`groupDesc`

Group descending

410

[Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group)

Group by the column field in descending order

`groupRemove`

Stop grouping

420

[Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group)

Stops grouping

`mergeCells`

Merge cells

500

[MergeCells](https://bryntum.com/docs/gantt/api/#Grid/feature/MergeCells)

Merge cells with same value in a sorted column

\*

items that are generated dynamically

\>

first level of submenu

### Customizing the menu items

The menu items in the Header menu can be customized, existing items can be changed or removed, and new items can be added. This is handled using the `items` config of the feature.

Add extra items for all columns:

```
const grid = new Grid({
  features : {
    headerMenu : {
      items : {
        extraItem : { text: 'My header item', icon: 'fa fa-car', weight: 200, onItem : () => ... }
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
      field: 'name',
      text: 'Name',
      headerMenuItems: {
        columnItem : { text: 'My unique header item', icon: 'fa fa-flask', onItem : () => ... }
      }
    }
  ]
});
```

Remove built-in item:

```
const grid = new Grid({
  features : {
    headerMenu : {
      items : {
         // Hide 'Stop grouping'
         groupRemove : false
      }
    }
  }
});
```

Customize built-in item:

```
const grid = new Grid({
  features : {
    headerMenu : {
      items : {
         hideColumn : {
             text : 'Bye bye column'
         }
      }
    }
  }
});
```

Remove nested menu item:

```
const grid = new Grid({
    features : {
        headerMenu : {
            items : {
                multiSort : {
                    menu : { removeSorter : false }
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
    headerMenu : {
      processItems({items, record}) {
          if (record.cost > 5000) {
             items.myItem = { text : 'Split cost' };
          }
      }
    }
  }
});
```

The \`processItems\` implementation may be an \`async\` function which \`awaits\` a result to mutate the \`items\` object.

Full information of the menu customization can be found in the "Customizing the Cell menu and the Header menu" guide.

This feature is **enabled** by default.

Keyboard shortcuts
------------------

This feature has the following default keyboard shortcuts:

Keys

Action

Action description

`Space`

_showContextMenuByKey_

Shows context menu for currently focused header

`Ctrl`+`Space`

_showContextMenuByKey_

Shows context menu for currently focused header

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[items](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#config-items)
This is a preconfigured set of items used to create the default context menu.

The `items` provided by this feature are listed in the intro section of this class. You can configure existing items by passing a configuration object to the keyed items.

To remove existing items, set corresponding keys to `null`:

```
const scheduler = new Scheduler({
    features : {
        headerMenu : {
            items : {
                filter        : null,
                columnPicker  : null
            }
        }
    }
});
```

See the feature config in the above example for details.

[moveColumns](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#config-moveColumns)
Configure as `true` to show two extra menu options to move the selected column to either before its previous sibling, or after its next sibling.

This is a keyboard-accessible version of drag/drop column reordering.

[keyMap](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Grid/feature/HeaderMenu#keyboard-shortcuts) for details

[processItems](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#config-processItems)
A function called before displaying the menu that allows manipulations of its items. Returning `false` from this function prevents the menu being shown.

```
  features         : {
      headerMenu : {
          processItems({ column, items }) {
              // Add or hide existing items here as needed
              items.myAction = {
                  text   : 'Cool action',
                  icon   : 'fa fa-fw fa-ban',
                  onItem : () => console.log('Some coolness'),
                  weight : 300 // Move to end
              };

              // Hide column picker
              items.columnPicker.hidden = true;
          }
      }
  },
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#property-isHeaderMenu)
Identifies an object as an instance of [HeaderMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/HeaderMenu) class, or subclass thereof.

[isHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#property-isHeaderMenu-static)
Identifies an object as an instance of [HeaderMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/HeaderMenu) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[headerMenuBeforeShow](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#event-headerMenuBeforeShow)
This event fires on the owning Grid before the context menu is shown for a header. Allows manipulation of the items to show in the same way as in the [processItems](https://bryntum.com/docs/gantt/api/#Grid/feature/HeaderMenu#config-processItems).

Returning `false` from a listener prevents the menu from being shown.

[headerMenuShow](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#event-headerMenuShow)
This event fires on the owning Grid after the context menu is shown for a header

[headerMenuItem](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#event-headerMenuItem)
This event fires on the owning Grid when an item is selected in the header context menu.

[headerMenuToggleItem](https://bryntum.com/docs/gantt/api/Grid/feature/HeaderMenu#event-headerMenuToggleItem)
This event fires on the owning Grid when a check item is toggled in the header context menu.
