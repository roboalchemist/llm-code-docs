# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/GridBase.md

# [GridBase](https://bryntum.com/docs/gantt/api/Grid/view/GridBase)

A thin base class for [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid). Does not include any features by default, allowing smaller custom-built bundles if used in place of [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid).

**NOTE:** In most scenarios you probably want to use Grid instead of GridBase.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[readOnly](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-readOnly)
Set to `true` to make the grid read-only, by disabling any UIs for modifying data.

**Note that checks MUST always also be applied at the server side.**

[autoHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-autoHeight)
Automatically set grids height to fit all rows (no scrolling in the grid). In general you should avoid using `autoHeight: true`, since it will bypass Grids virtual rendering and render all rows at once, which in a larger grid is really bad for performance.

[enableSticky](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-enableSticky)
Configure this as `true` to allow elements within cells to be styled as `position: sticky`.

Columns which contain sticky content will need to be configured with

```
   cellCls : 'b-sticky-cell',
```

Or a custom renderer can add the class to the passed cell element.

It is up to the application author how to style the cell content. It is recommended that a custom renderer create content with CSS class names which the application author will use to apply the `position`, and matching `margin-top` and `top` styles to keep the content stuck at the grid's top.

Note that not all browsers support this CSS feature. A cross browser alternative is to use the {link Grid.feature.StickyCells StickyCells} Feature.

[enableTextSelection](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-enableTextSelection)
Set to `true` to allow text selection in the grid cells. Note, this cannot be used simultaneously with the `RowReorder` feature.

[fillLastColumn](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-fillLastColumn)
Set to `true` to stretch the last column in a grid with all fixed width columns to fill extra available space if the grid's width is wider than the sum of all configured column widths.

[keyMap](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#keyboard-shortcuts) for details

[showDirty](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-showDirty)
Configure as `true` to have the grid show a red "changed" tag in cells whose field value has changed and not yet been committed.

Set `showDirty.duringEdit` to `true` to show the red tag while editing a cell

```
showDirty : {
    duringEdit : true
}
```

Set `showDirty.newRecord` to `true` to show the red tag for all the cells of the new record

```
showDirty : {
    newRecord : true
}
```

[subGridConfigs](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-subGridConfigs)
An object containing sub grid configuration objects keyed by a `region` property. By default, grid has a 'locked' region (if configured with locked columns) and a 'normal' region. The 'normal' region defaults to use `flex: 1`.

This config can be used to reconfigure the "built-in" sub grids or to define your own.

Redefining the default regions:

```
new Grid({
  subGridConfigs : {
    locked : { flex : 1 },
    normal : { width : 100 }
  }
});
```

```
const App = props => {
    const subGridConfigs = {
        locked : { flex : 1 },
        normal : { width : 100 }
    };

    return <bryntum-grid subGridConfigs={subGridConfigs} />
}
```

```
<bryntum-grid :sub-grid-configs="subGridConfigs" />
```

```
export default {
    setup() {
        return {
            subGridConfigs : [
                locked : { flex : 1 },
                normal : { width : 100 }
            ]
        };
    }
}
```

```
<bryntum-grid [subGridConfigs]="subGridConfigs"></bryntum-grid>
```

```
export class AppComponent {
     subGridConfigs = [
         locked : { flex : 1 },
         normal : { width : 100 }
     ]
 }
```

Defining your own multi region grid:

```
new Grid({
  subGridConfigs : {
    left   : { width : 100 },
    middle : { flex : 1 },
    right  : { width  : 100 }
  },

  columns : [
    { field : 'manufacturer', text: 'Manufacturer', region : 'left' },
    { field : 'model', text: 'Model', region : 'middle' },
    { field : 'year', text: 'Year', region : 'middle' },
    { field : 'sales', text: 'Sales', region : 'right' }
  ]
});
```

[store](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-store)
Store that holds records to display in the grid, or a store config object. If the configuration contains a `readUrl`, an `AjaxStore` will be created.

Note that a store will be created during initialization if none is specified.

Supplying a store config object at initialization time:

```
const grid = new Grid({
    store : {
        fields : ['name', 'powers'],
        data   : [
            { id : 1, name : 'Aquaman', powers : 'Decent swimmer' },
            { id : 2, name : 'Flash', powers : 'Pretty fast' },
        ]
    }
});
```

Accessing the store at runtime:

```
grid.store.sort('powers');
```

[scrollManager](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-scrollManager)
Configuration values for the [ScrollManager](https://bryntum.com/docs/gantt/api/#Core/util/ScrollManager) class on initialization. Returns the [ScrollManager](https://bryntum.com/docs/gantt/api/#Core/util/ScrollManager) at runtime.

[columns](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-columns)
Accepts column definitions for the grid during initialization. They will be used to create [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) instances that are added to a [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore).

At runtime it returns the [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore).

Initialization using column config objects:

```
new Grid({
  columns : [
    { text : 'Alias', field : 'alias' },
    { text : 'Superpower', field : 'power' }
  ]
});
```

Also accepts a store config object:

```
new Grid({
  columns : {
    data : [
      { text : 'Alias', field : 'alias' },
      { text : 'Superpower', field : 'power' }
    ],
    listeners : {
      update() {
        // Some update happened
      }
    }
  }
});
```

Access the [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) at runtime to manipulate columns:

```
grid.columns.add({ field : 'column', text : 'New column' });
```

Replacing the columns fully at runtime:

```
grid.columns = [{ field : 'column', text : 'New column' }];
```

[minHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-minHeight)
Grid's `min-height`. Defaults to `10em` to be sure that the Grid always has a height wherever it is inserted.

Can be either a String or a Number (which will have 'px' appended).

Note that _reading_ the value will return the numeric value in pixels.

[hideHeaders](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-hideHeaders)
Set to `true` to hide the column header elements

[hideFooters](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-hideFooters)
Set to `true` to hide the footer elements

[cellEllipsis](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-cellEllipsis)
Set to `false` to crop text in grid cells without ellipsis (...). When enabled, cells containing pure use `display : block`, instead of `display : flex` to allow ellipsis to work. **NOTE** Only supported in browsers that support `:has()` CSS selector

[hideHorizontalScrollbar](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-hideHorizontalScrollbar)
Set to `true` to hide the Grid's horizontal scrollbar(s)

[emptyText](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-emptyText)
Text or HTML, or a [EmptyTextDomConfig](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#typedef-EmptyTextDomConfig) block to display when there is no data to display in the grid. When using multiple Grid regions, provide the `region` property to decide where the text is shown. By default, it is shown in the first region.

```
new Grid({
    emptyText : {
        region : 'locked',
        text   : 'No data available'
    }
})
```

[rowHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-rowHeight)
Row height in pixels. This allows the default height for rows to be controlled. Note that it may be overriden by specifying a [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-rowHeight) on a per record basis, or from a column [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer).

When initially configured as `null`, an empty row will be measured and its height will be used as default row height, enabling it to be controlled using CSS

[preserveScroll](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-preserveScroll)
Preserve the grid's vertical scroll position when changesets are applied, as in the case of remote changes, or when stores are configured with [syncDataOnLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-syncDataOnLoad).

[animateTreeNodeToggle](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-animateTreeNodeToggle)
When the [Tree](https://bryntum.com/docs/gantt/api/#Grid/feature/Tree) feature is in use and the Store is a tree store, this config may be set to `true` to visually animate branch node expand and collapse operations.

This is not supported in Scheduler and Gantt

[columnLines](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-columnLines)
Set to `false` to not show column lines. End result might be overruled by/differ between themes.

[rowLines](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-rowLines)
Set to `false` to not show row lines. End result might be overruled by/differ between themes.

[fixedRowHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-fixedRowHeight)
Use fixed row height. Setting this to `true` will configure the underlying RowManager to use fixed row height, which sacrifices the ability to use rows with variable height to gain a fraction better performance.

Using this setting also ignores the [getRowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-getRowHeight) function, and thus any row height set in data. Only Grids configured [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-rowHeight) is used.

[formulaProviders](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-formulaProviders)
An object which names formula prefixes which will be applied to all columns configured with `formula : true`.

Each entry is keyed by a formula prefix, and each value is how to instantiate and configure a [FormulaProvider](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider) when that prefix is used in the typed vale, eg: `=XXX(`

If the configured value contains a `type` property, that is used to determine a registered formula provider subclass to instantiate.

```
fields : [{
    name             : 'review',
    formulaProviders : {
       AI : {
         type : 'remote',
         url  : 'https://my-ai-service.com'
       },
       SUM : {
          type : 'sum'
       }
    }
}]
```

Formula providers may be added to dynamically:

```
// Enable registered MYFormula class to be used as a formula provider in the Grid
grid.store.modelClass.fieldMap.review.formulaProviders.MY = { ... };
```

[transition](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-transition)
Configure UI transitions for various actions in the grid.

[getRowHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-getRowHeight)
A function called for each row to determine its height. It is passed a [record](https://bryntum.com/docs/gantt/api/#Core/data/Model) and expected to return the desired height of that records row. If the function returns a falsy value, Grids configured [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-rowHeight) is used.

The default implementation of this function returns the row height from the records [rowHeight field](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-rowHeight).

Override this function to take control over how row heights are determined:

```
new Grid({
   getRowHeight(record) {
       if (record.low) {
           return 20;
       }
       else if (record.high) {
           return 60;
       }

       // Will use grids configured rowHeight
       return null;
   }
});
```

NOTE: Height set in a Column renderer takes precedence over the height returned by this function.

[fullRowRefresh](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-fullRowRefresh)
Refresh entire row when a record changes (`true`) or, if possible, only the cells affected (`false`).

When this is set to `false`, then if a column uses a renderer, cells in that column will still be updated because it is impossible to know whether the cells value will be affected.

If a standard, provided Column class is used with no custom renderer, its cells will only be updated if the column's [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) is changed.

[preserveScrollOnDatasetChange](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-preserveScrollOnDatasetChange)
Specify `true` to preserve vertical scroll position after store actions that trigger a `refresh` event, such as loading new data and filtering.

[preserveFocusOnDatasetChange](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-preserveFocusOnDatasetChange)
True to preserve focused cell after loading new data

[data](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-data)
Convenient shortcut to set data in grids store both during initialization and at runtime. Can also be used to retrieve data at runtime, although we do recommend interacting with Grids store instead using the [store](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#property-store) property.

Setting initial data during initialization:

```
const grid = new Grid({
    data : [
      { id : 1, name : 'Batman' },
      { id : 2, name : 'Robin' },
      ...
    ]
});
```

Setting data at runtime:

```
grid.data = [
    { id : 3, name : 'Joker' },
    ...
];
```

Getting data at runtime:

```
const records = store.data;
```

Note that a Store will be created during initialization if none is specified.

[defaultRegion](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-defaultRegion)
Region to which columns are added when they have none specified

[destroyStore](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-destroyStore)
Set to `true` to destroy the store when the grid is destroyed.

[maskDefaults](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-maskDefaults)
Grids change the `maskDefaults` to cover only their `body` element.

[resizeToFitIncludesHeader](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-resizeToFitIncludesHeader)
Set to `false` to only measure cell contents when double-clicking the edge between column headers.

[animateRemovingRows](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-animateRemovingRows)
Controls if removing and inserting rows should be animated. Set to `false` to prevent those animations, removing the related delays.

[animateFilterRemovals](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-animateFilterRemovals)
Set to `true` to animate row removals caused by filtering.

[disableGridRowModelWarning](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-disableGridRowModelWarning)
Set to `true` to not get a warning when using another base class than GridRowModel for your grid data. If you do, and would like to use the full feature set of the grid then include the fields from GridRowModel in your model definition.

[disableGridColumnIdWarning](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-disableGridColumnIdWarning)
Set to `true` to not get a warning when calling [getState](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#function-getState) when there is a column configured without an `id`. But the recommended action is to always configure columns with an `id` when using states.

[monitorResize](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-monitorResize)
Grid monitors window resize by default.

[features](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-features)
An object containing Feature configuration objects (or `true` if no configuration is required) keyed by the Feature class name in all lowercase.

[scrollable](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-scrollable)
Configures whether the grid is scrollable in the `Y` axis. This is used to configure a [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller). See the [scrollerClass](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-scrollerClass) config option.

By default the grid is scrollable in the `Y` axis. If your platform shows scrollbars, they will appear when the content of the grid overflows.

To always show a scrollbar - even an empty one when there is no overflow - configure this as:

```
   scrollable : {
       overflowY : 'scroll'
   }
```

[scrollerClass](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-scrollerClass)
The class to instantiate to use as the [scrollable](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-scrollable). Defaults to [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller).

[transitionDuration](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-transitionDuration)
Animation transition duration in milliseconds.

[contextMenuTriggerEvent](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#config-contextMenuTriggerEvent)
Event which is used to show context menus. Available options are: 'contextmenu', 'click', 'dblclick'.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridBase](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-isGridBase)
Identifies an object as an instance of [GridBase](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase) class, or subclass thereof.

[isGridBase](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-isGridBase-static)
Identifies an object as an instance of [GridBase](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase) class, or subclass thereof.

[readOnly](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-readOnly)
Set to `true` to make the grid read-only, by disabling any UIs for modifying data.

**Note that checks MUST always also be applied at the server side.**

[store](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-store)
Store that holds records to display in the grid, or a store config object. If the configuration contains a `readUrl`, an `AjaxStore` will be created.

Note that a store will be created during initialization if none is specified.

Supplying a store config object at initialization time:

```
const grid = new Grid({
    store : {
        fields : ['name', 'powers'],
        data   : [
            { id : 1, name : 'Aquaman', powers : 'Decent swimmer' },
            { id : 2, name : 'Flash', powers : 'Pretty fast' },
        ]
    }
});
```

Accessing the store at runtime:

```
grid.store.sort('powers');
```

[scrollManager](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-scrollManager)
Configuration values for the [ScrollManager](https://bryntum.com/docs/gantt/api/#Core/util/ScrollManager) class on initialization. Returns the [ScrollManager](https://bryntum.com/docs/gantt/api/#Core/util/ScrollManager) at runtime.

[columns](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-columns)
Accepts column definitions for the grid during initialization. They will be used to create [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) instances that are added to a [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore).

At runtime it returns the [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore).

Initialization using column config objects:

```
new Grid({
  columns : [
    { text : 'Alias', field : 'alias' },
    { text : 'Superpower', field : 'power' }
  ]
});
```

Also accepts a store config object:

```
new Grid({
  columns : {
    data : [
      { text : 'Alias', field : 'alias' },
      { text : 'Superpower', field : 'power' }
    ],
    listeners : {
      update() {
        // Some update happened
      }
    }
  }
});
```

Access the [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) at runtime to manipulate columns:

```
grid.columns.add({ field : 'column', text : 'New column' });
```

Replacing the columns fully at runtime:

```
grid.columns = [{ field : 'column', text : 'New column' }];
```

[hideHeaders](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-hideHeaders)
Set to `true` to hide the column header elements

[hideFooters](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-hideFooters)
Set to `true` to hide the footer elements

[cellEllipsis](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-cellEllipsis)
Set to `false` to crop text in grid cells without ellipsis (...). When enabled, cells containing pure use `display : block`, instead of `display : flex` to allow ellipsis to work. **NOTE** Only supported in browsers that support `:has()` CSS selector

[emptyText](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-emptyText)
Text or HTML, or a [EmptyTextDomConfig](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#typedef-EmptyTextDomConfig) block to display when there is no data to display in the grid. When using multiple Grid regions, provide the `region` property to decide where the text is shown. By default, it is shown in the first region.

```
new Grid({
    emptyText : {
        region : 'locked',
        text   : 'No data available'
    }
})
```

[rowHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-rowHeight)
Row height in pixels. This allows the default height for rows to be controlled. Note that it may be overriden by specifying a [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-rowHeight) on a per record basis, or from a column [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer).

When initially configured as `null`, an empty row will be measured and its height will be used as default row height, enabling it to be controlled using CSS

[preserveScroll](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-preserveScroll)
Preserve the grid's vertical scroll position when changesets are applied, as in the case of remote changes, or when stores are configured with [syncDataOnLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-syncDataOnLoad).

[animateTreeNodeToggle](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-animateTreeNodeToggle)
When the [Tree](https://bryntum.com/docs/gantt/api/#Grid/feature/Tree) feature is in use and the Store is a tree store, this config may be set to `true` to visually animate branch node expand and collapse operations.

This is not supported in Scheduler and Gantt

[columnLines](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-columnLines)
Set to `false` to not show column lines. End result might be overruled by/differ between themes.

[rowLines](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-rowLines)
Set to `false` to not show row lines. End result might be overruled by/differ between themes.

[transition](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-transition)
Configure UI transitions for various actions in the grid.

[data](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-data)
Convenient shortcut to set data in grids store both during initialization and at runtime. Can also be used to retrieve data at runtime, although we do recommend interacting with Grids store instead using the [store](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#property-store) property.

Setting initial data during initialization:

```
const grid = new Grid({
    data : [
      { id : 1, name : 'Batman' },
      { id : 2, name : 'Robin' },
      ...
    ]
});
```

Setting data at runtime:

```
grid.data = [
    { id : 3, name : 'Joker' },
    ...
];
```

Getting data at runtime:

```
const records = store.data;
```

Note that a Store will be created during initialization if none is specified.

[transitionDuration](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-transitionDuration)
Animation transition duration in milliseconds.

[firstVisibleRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-firstVisibleRow)
Get the topmost visible grid row

[lastVisibleRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-lastVisibleRow)
Get the last visible grid row

[topRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-topRow)
Get the Row that is currently displayed at top.

[bottomRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-bottomRow)
Get the Row currently displayed furthest down.

[bodyHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-bodyHeight)
Body height

[headerHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-headerHeight)
Header height

[footerHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-footerHeight)
Footer height

[contentHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#property-contentHeight)
Returns content height calculated from row manager

## Functions

Functions are methods available for calling on the class

[doDestroy](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-doDestroy)
Cleanup

[setGridClassList](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-setGridClassList)
Adds extra classes to the Grid element after it's been configured. Also iterates through features, thus ensuring they have been initialized.

[getRowById](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getRowById)
Get Row for specified record id.

[getRecordCoords](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getRecordCoords)
Returns top and bottom for rendered row or estimated coordinates for unrendered.

[getRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getRow)
Get the Row at specified index. "Wraps" index if larger than available rows.

[getRowFor](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getRowFor)
Get a Row for either a record, a record id or an HTMLElement

[getRowFromElement](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getRowFromElement)
Get a Row from an HTMLElement

[bindStore](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-bindStore)
Hooks up data store listeners

[onStoreUpdateRecord](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreUpdateRecord)
Rerenders a cell if a record is updated in the store

[onStoreAdd](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreAdd)
Refreshes rows when data is added to the store

[onStoreException](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreException)
Responds to exceptions signalled by the store

[onStoreDataChange](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreDataChange)
Refreshes rows when data is changed in the store

[onStoreRecordIdChange](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreRecordIdChange)
The hook is called when the id of a record has changed.

[onStoreBeforeRequest](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreBeforeRequest)
Shows a load mask while the connected store is loading

[onStoreAfterRequest](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreAfterRequest)
Hides load mask after a load request ends either in success or failure

[onStoreRemove](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreRemove)
Animates removal of record.

[onStoreRemoveAll](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onStoreRemoveAll)
Rerenders grid when all records have been removed

[captureScrollTargetRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-captureScrollTargetRow)
Remember scroll position when store is about to apply a changeset

[restoreScrollTargetRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-restoreScrollTargetRow)
Restore scroll position. Go to the topmost row formerly in the view that is still present in the dataset.

[populateHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-populateHeaderMenu)
Populates the header context menu. Chained in features to add menu items.

[populateCellMenu](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-populateCellMenu)
Populates the cell context menu. Chained in features to add menu items.

[getCell](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getCell)
Returns a cell if rendered or null if not found.

[getHeaderElement](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getHeaderElement)
Returns the header element for the column

[getFooterElement](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getFooterElement)
Returns the footer element for the column (only relevant when using the Summary feature)

[getRecordFromElement](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getRecordFromElement)
Searches up from the specified element for a grid row and returns the record associated with that row.

[getColumnFromElement](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-getColumnFromElement)
Searches up from specified element for a grid cell or a header and returns the column which the cell belongs to

[fixSizes](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-fixSizes)
Sets widths and heights for headers, rows and other parts of the grid as needed

[refreshTotalHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-refreshTotalHeight)
Makes height of vertical scroller match estimated total height of grid. Called when scrolling vertically and when showing/hiding rows.

[enableScrollingCloseToEdges](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-enableScrollingCloseToEdges)
Activates automatic scrolling of a subGrid when mouse is moved closed to the edges. Useful when dragging DOM nodes from outside this grid and dropping on the grid.

[disableScrollingCloseToEdges](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-disableScrollingCloseToEdges)
Deactivates automatic scrolling of a subGrid when mouse is moved closed to the edges

[onRowManagerRequestScrollChange](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onRowManagerRequestScrollChange)
Responds to request from RowManager to adjust scroll position. Happens when jumping to a scroll position with variable row height.

[initScroll](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-initScroll)
Scroll syncing for normal headers & grid + triggers virtual rendering for vertical scroll

[scrollRowIntoView](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-scrollRowIntoView)
Scrolls a locally available record's row into view. If row isn't rendered it tries to calculate position. Accepts the [BryntumScrollOptions](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller#typedef-BryntumScrollOptions) `column` property

[scrollColumnIntoView](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-scrollColumnIntoView)
Scrolls a column into view (if it is not already)

[scrollCellIntoView](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-scrollCellIntoView)
Scrolls a locally available record's cell into view (if it is not already).

[scrollToBottom](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-scrollToBottom)
Scroll all the way down

[scrollToTop](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-scrollToTop)
Scroll all the way up

[highlightCells](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-highlightCells)
Highlights the specified cells. If `scroll` is set to `true` (which it is by default), the highlighted cell closest to the viewport center will be scrolled into view.

By default, the highlighting will fade out non-highlighted cells. Use the `mode` option to change the highlight style to apply a background color to the highlighted cells instead.

```
// Highlight single cell (default fade mode)
grid.highlightCells({ cells : { id : 1, field : 'name' } });
// Highlight with background color
grid.highlightCells({ cells : { id : 1, field : 'name' }, mode : 'color' });
// Highlight multiple cells
grid.highlightCells({ cells : [{ id : 1, field : 'name' }, { id : 2, field : 'age' }] });
// Don't scroll to highlighted cell, and don't un-highlight on click
grid.highlightCells({ cells : { id : 1, field : 'name' }, scroll : false, unhighlightOnClick : false });
// Auto-unhighlight after 2 seconds
grid.highlightCells({ cells : { id : 1, field : 'name' }, unhighlightAfter : 2000 });
```

[unhighlightCells](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-unhighlightCells)
Removes highlighting from the specified cells. If no cells are passed, all highlighted cells will be un-highlighted.

```
grid.unhighlightCells({ cells : { id : 1, columnId : 'name' } }); // single cell
grid.unhighlightCells({ cells : [{ id : 1, columnId : 'name' }, { id : 2, columnId : 'age' }] }); // multiple cells
grid.unhighlightCells(); // all cells
```

[storeScroll](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-storeScroll)
Stores the scroll state. Returns an objects with a `scrollTop` number value for the entire grid and a `scrollLeft` object containing a left position scroll value per sub grid.

[restoreScroll](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-restoreScroll)
Restore scroll state. If state is not specified, restores the last stored state.

[measureRowHeight](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-measureRowHeight)
Creates a fake subgrid with one row and measures its height. Result is used as rowHeight.

[onThemeChange](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-onThemeChange)
Handler for global theme change event (triggered by shared.js). Remeasures row height.

[refreshRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-refreshRow)
Triggers a render of all the cells in the row for the passed record.

Since Grid uses virtualized rows, calling this method for a record that is not currently displayed in a row will not have any effect.

Manipulating records and Grid settings refreshes the Grid automatically. You should only need to call this function if you have outside data/settings unknown to the Grid that has changed and requires Grid to update the row to reflect the changes

[refreshRows](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-refreshRows)
Triggers a render of all the cells in the rows for the passed records. Leave the argument out to refresh all rows.

Since Grid uses virtualized rows, calling this method for records that are not currently displayed in rows will not have any effect.

Manipulating records and Grid settings refreshes the Grid automatically. You should only need to call this function if you have outside data/settings unknown to the Grid that has changed and requires Grid to update rows to reflect the changes

[refreshColumn](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-refreshColumn)
Triggers a render of all the cells in a column.

[refreshVirtualScrollbars](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-refreshVirtualScrollbars)
Recalculates virtual scrollbars widths and scrollWidth

[suspendRefresh](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-suspendRefresh)
Suspends UI refreshes after updates to the underlying data.

Multiple calls to `suspendRefresh` stack up, and will require an equal number of `resumeRefresh` calls to actually resume UI refresh.

[resumeRefresh](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-resumeRefresh)
Resumes UI refreshes after updates to the underlying data.

Multiple calls to `suspendRefresh` stack up, and will require an equal number of `resumeRefresh` calls to actually resume UI refresh.

Specify `false` as the first param to not refresh if this call unblocked the refresh suspension.

[renderRows](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-renderRows)
Rerenders all grid rows, completely replacing all row elements with new ones

[renderContents](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-renderContents)
Rerenders the grids rows, headers and footers, completely replacing all row elements with new ones

[refreshHeaders](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-refreshHeaders)
Rerenders all grid headers

[refreshHeader](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-refreshHeader)
Rerender a single grid header

[renderHeader](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-renderHeader)
Called after headers have been rendered to the headerContainer. This does not do anything, it's just for Features to hook in to.

[renderFooter](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-renderFooter)
Called after footers have been rendered to the footerContainer. This does not do anything, it's just for Features to hook in to.

[maskBody](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-maskBody)
Show a load mask with a spinner and the specified message. When using an AjaxStore masking and unmasking is handled automatically, but if you are loading data in other ways you can call this function manually when your load starts.

```
myLoadFunction() {
  // Show mask before initiating loading
  grid.maskBody('Loading data');
  // Your custom loading code
  load.then(() => {
     // Hide the mask when loading is finished
     grid.unmaskBody();
  });
}
```

[unmaskBody](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-unmaskBody)
Hide the load mask.

[suspendAnimations](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-suspendAnimations)
Suspends CSS transitions after a row / event has been updated

Multiple calls to `suspendAnimations` stack up, and will require an equal number of `resumeAnimations` calls to actually resume animations.

[resumeAnimations](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-resumeAnimations)
Resumes CSS transitions after a row / event has been updated

[runWithTransition](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#function-runWithTransition)
Runs a function with transitions enabled (row height, event size etc.). Useful if you want to alter the UI state with a transition.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[subGridCollapse](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-subGridCollapse)
Fires after a sub grid is collapsed.

[subGridExpand](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-subGridExpand)
Fires after a sub grid is expanded.

[beforeColumnCollapseToggle](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-beforeColumnCollapseToggle)
This event is triggered before a parent column is collapsed or expanded.

[columnCollapseToggle](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-columnCollapseToggle)
This event is triggered after a parent column has been collapsed or expanded.

[beforeRenderRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-beforeRenderRow)
Fires before a row is rendered.

[renderRow](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-renderRow)
Fires after a row is rendered.

[dataChange](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-dataChange)
Fired when data in the store changes.

Basically a relayed version of the store's own change event, decorated with a `store` property. See the [store change event](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-change) documentation for more information.

[scroll](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-scroll)
Grid has scrolled vertically

[beforeRenderRows](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-beforeRenderRows)
Grid rows are about to be rendered

[renderRows](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#event-renderRows)
Grid rows have been rendered

## Typedefs

Typedefs are type definitions for the class

[PreserveScrollOptions](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#typedef-PreserveScrollOptions)
Additional options for the [preserveScroll](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-preserveScroll) configuration.

[EmptyTextDomConfig](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#typedef-EmptyTextDomConfig)
Config object that specifies empty text configuration.

[GridScrollOptions](https://bryntum.com/docs/gantt/api/Grid/view/GridBase#typedef-GridScrollOptions)
