# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/Split.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Split.md

# [Split](https://bryntum.com/docs/gantt/api/Grid/feature/Split)

This feature allows splitting the Grid into multiple views, either by using the cell context menu, or programmatically by calling [split()](https://bryntum.com/docs/gantt/api/#Grid/feature/Split#function-split).

It handles splitting in 3 "directions":

* `'horizontal'` - Splitting the grid into 2 sub-views, one above the other.
* `'vertical'` - Splitting the grid into 2 sub-views, one to the left of the other.
* `'both'` - Splitting the grid into 4 sub-views, one in each corner.

Or, by supplying a record and/or a column to split by.

The first sub-view (top, left or top-left depending on split direction) is the original grid, and the others are clones of the original. The clones share the same store, columns and selection.

Sub-views in the same column sync their scrolling horizontally, and sub-views in the same row sync their scrolling vertically.

Sub-views are separated by splitters, that can be dragged to resize the views.

Splitting a multi-region grid (two regions supported) only includes the region in which the split was performed in the split view.

Splitting works best on grids that use fixed column widths, since flexed columns will resize when the grid is split.

Splitting programmatically
--------------------------

The split feature assigns two methods to the owning grid:

* [split()](https://bryntum.com/docs/gantt/api/#Grid/feature/Split#function-split) - Splits the grid into sub-views.
* [unsplit()](https://bryntum.com/docs/gantt/api/#Grid/feature/Split#function-unsplit) - Re-joins the sub-views into a single grid.

Use them to split programmatically in your app.

```
// Split horizontally (eg. at the row in the center of the grid)
await grid.split({ direction : 'horizontal' });

// Split both ways by a specific column and record
await grid.split({
   atRecord : grid.store.getById(10),
   atColumn : grid.columns.get('city')
});

// Remove splits, returning to a single grid
grid.unsplit();
```

Splitting using the cell context menu
-------------------------------------

The feature also adds a new sub-menu to the cell context menu, allowing the user to split (or un-split) the grid. See the API documentation for the [CellMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/CellMenu) feature for more information on how to customize the sub-menu.

Accessing a sub-view
--------------------

The sub-views are accessed by index. The original grid is at index 0, and the others are as shown below. For 'horizontal' splits:

0 - Original

1 - Sub-view

For 'vertical' splits:

0 - Original

1 - Sub-view

For 'both' splits:

0 - Original

1 - Sub-view

2 - Sub-view

3 - Sub-view

The [subViews](https://bryntum.com/docs/gantt/api/#Grid/feature/Split#property-subViews) property returns an array containing all sub-views, including the original. Note that the property is also exposed on the owning Grid. Access a specific sub-view by index (see illustrations above). For example to access the bottom right sub-view in a 'both' split:

```
await grid.split({ direction : 'both' });
const bottomRight = grid.subViews[3];
await bottomRight.scrollRowIntoView(100);
```

Troubleshooting
---------------

The splits are inserted into a container element (which has the `.b-split-container` CSS class), replacing the original grid. If it does not render correctly out of the box, you should make sure that any CSS rules you have that apply size to the grid also applies to the container element.

For example if you use a CSS flex rule to size the grid:

```
.b-grid {
    // Size grid using flex
    flex : 3;
}
```

Then you should also apply the same rule to the container element:

```
.b-grid,
.b-split-container {
    flex : 3;
}
```

Note that configuration changes at runtime, when already split, are not automatically propagated to the sub-views. If you need to change a config at runtime, either first unsplit the grid, or change it on each sub-view individually. A notable exception from this is that enabling / disabling features at runtime is reflected in the sub-views.

Please note that this feature will not work with the [LockRows](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows) feature.

This feature will not work properly when Store uses [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad)

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[relayProperties](https://bryntum.com/docs/gantt/api/Grid/feature/Split#config-relayProperties)
Properties whose changes should be relayed to sub-views at runtime.

Supply an object with property names as keys, and a truthy value to relay the change, or a falsy value to not relay it. The object will be merged with the default values.

By default, these properties are relayed:

* [readOnly](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#property-readOnly)
* [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#property-rowHeight)

Example of supplying a custom set of properties to relay:

```
const grid = new Grid({
    features : {
        split : {
            relayProperties : {
                readOnly : false, // Do not relay readOnly changes
                myConfig : true   // Relay changes to the myConfig property
            }
        }
    }
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSplit](https://bryntum.com/docs/gantt/api/Grid/feature/Split#property-isSplit)
Identifies an object as an instance of [Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split) class, or subclass thereof.

[isSplit](https://bryntum.com/docs/gantt/api/Grid/feature/Split#property-isSplit-static)
Identifies an object as an instance of [Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split) class, or subclass thereof.

[subViews](https://bryntum.com/docs/gantt/api/Grid/feature/Split#property-subViews)
An array of sub-views. The first sub-view is the original grid, and the others are clones of the original. See the "Accessing a sub-view" section above for more information.

```
await grid.split('vertical');
const bottom = grid.subViews[1];
await bottom.scrollRowIntoView(100);
```

Note that this property is accessible directly on the grid instance.

## Functions

Functions are methods available for calling on the class

[split](https://bryntum.com/docs/gantt/api/Grid/feature/Split#function-split)
Split the grid into two or four parts.

* Splits into two when passed `direction : 'vertical'`, `direction : 'horizontal'` or `atColumn` or `atRecord`.
* Splits into four when passed `direction : 'both'` or `atColumn` and `atRecord`.

```
// Split horizontally (at the row in the center of the grid)
await grid.split({ direction : 'horizontal' });

// Split both ways by a specific column and record
await grid.split({
   atRecord : grid.store.getById(10),
   atColumn : grid.columns.get('city')
});
```

To return to a single grid, call [unsplit](https://bryntum.com/docs/gantt/api/#Grid/feature/Split#function-unsplit).

Note that this function is callable directly on the grid instance.

[unsplit](https://bryntum.com/docs/gantt/api/Grid/feature/Split#function-unsplit)
Remove splits, returning to a single grid.

Note that this function is callable directly on the grid instance.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[split](https://bryntum.com/docs/gantt/api/Grid/feature/Split#event-split)
Fires when splitting the Grid.

[unsplit](https://bryntum.com/docs/gantt/api/Grid/feature/Split#event-unsplit)
Fires when un-splitting the Grid.
