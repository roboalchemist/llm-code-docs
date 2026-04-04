# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Sort.md

# [Sort](https://bryntum.com/docs/gantt/api/Grid/feature/Sort)

Allows sorting of grid by clicking (or tapping) headers, also displays which columns grid is sorted by (numbered if using multisort). Use modifier keys for multisorting: \[Ctrl/CMD + click\] to add sorter, \[Ctrl/CMD + Alt + click\] to remove sorter. The actual sorting is done by the store, see [Store.sort()](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSort#function-sort).

```
// sorting feature is enabled, no default value though
const grid = new Grid({
    features : {
        sort : true
    }
});

// use initial sorting
const grid = new Grid({
    features : {
        sort : 'name'
    }
});

// can also be specified on the store
const grid = new Grid({
    store : {
        sorters : [
            { field : 'name', ascending : false }
        ]
    }
});

// custom sorting function can also be specified on the store
const grid = new Grid({
    store : {
        sorters : [{
            fn : (recordA, recordB) => {
                // apply custom logic, for example:
                return recordA.name.length < recordB.name.length ? -1 : 1;
            }
        }]
    }
});
```

For info on programmatically handling sorting, see [StoreSort](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSort):

```
const grid = new Grid({ });
// Programmatic sorting of the store, Grids rows and UI will be updated
grid.store.sort('age');
```

Grid columns can define custom sorting functions (see [Column.sortable](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-sortable)). If this feature is configured with `prioritizeColumns: true`, those functions will also be used when sorting programmatically:

```
const grid = new Grid({
    columns : [
        {
            field : 'age',
            text : 'Age',
+           sortable(lhs, rhs) {
+             // Custom sorting, see Array#sort
+           }
        }
    ],

    features : {
        sort : {
+            prioritizeColumns : true
        }
    }
});

// Sortable fn will also be used when sorting programmatically
grid.store.sort('age');
```

This feature is **enabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[multiSort](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#config-multiSort)
Enable multi sort

[prioritizeColumns](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#config-prioritizeColumns)
Use custom sorting functions defined on columns also when programmatically sorting by the columns field.

```
const grid = new Grid({
    columns : [
        {
            field : 'age',
            text : 'Age',
            sortable(lhs, rhs) {
              // Custom sorting, see Array#sort
            }
        }
    ],

    features : {
        sort : {
            prioritizeColumns : true
        }
    }
});

grid.store.sort('age');
```

[showIconOnColumnHover](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#config-showIconOnColumnHover)
Set to `false` to not show the sort icon when hovering a Column header.

[toggleOnHeaderClick](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#config-toggleOnHeaderClick)
By default, clicking anywhere on the header text toggles the sorting state of a column.

Configure this as `false` to only toggle the sorting state of a column on click of the "arrow" icon within the grid header.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSort](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#property-isSort)
Identifies an object as an instance of [Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort) class, or subclass thereof.

[isSort](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#property-isSort-static)
Identifies an object as an instance of [Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort) class, or subclass thereof.

[showIconOnColumnHover](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#property-showIconOnColumnHover)
Set to `false` to not show the sort icon when hovering a Column header.

## Functions

Functions are methods available for calling on the class

[syncHeaderSortState](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#function-syncHeaderSortState)
Update headers to match stores sorters (displays sort icon in correct direction on them)

[populateHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#function-populateHeaderMenu)
Adds sort menu items to header context menu.

[getColumnDragToolbarItems](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#function-getColumnDragToolbarItems)
Supply items to ColumnDragToolbar

[onElementClick](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#function-onElementClick)
Clicked on header, sort Store.

[renderHeader](https://bryntum.com/docs/gantt/api/Grid/feature/Sort#function-renderHeader)
Called when grid headers are rendered, make headers match current sorters.
