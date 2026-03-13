# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/Grid.md

# [Grid](https://bryntum.com/docs/gantt/api/Grid/view/Grid)

The Grid component is a very powerful and performant UI component that shows tabular data (or tree data using the [TreeGrid](https://bryntum.com/docs/gantt/api/#Grid/view/TreeGrid)).

Intro
-----

The Grid widget has a wide range of features and a large API to allow users to work with data efficiently in the browser. The two most important configs are [store](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-store) and [columns](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-columns). With the store config, you decide which data to load into the grid. You can work with both in-memory arrays or load data using ajax. See the [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) class to learn more about loading data into stores.

The columns config accepts an array of [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) descriptors defining which fields that will be displayed in the grid. The [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) property in the column descriptor maps to a field in your dataset. The simplest grid configured with inline data and two columns would look like this:

```
 const grid = new Grid({
      appendTo : document.body,

      columns: [
          { field: 'name', text: 'Name' },
          { field: 'job', text: 'Job', renderer: ({value}) => value || 'Unemployed' }
      ],

      data: [
          { name: 'Bill', job: 'Retired' },
          { name: 'Elon', job: 'Visionary' },
          { name: 'Me' }
      ]
});
```

```
const App = props => {
    const [columns, setColumns] = useState([
         { field: 'name', text: 'Name' },
         { field: 'job', text: 'Job', renderer: ({value}) => value || 'Unemployed' }
    ]);

    const [data, setData] = useState([
         { name: 'Bill', job: 'Retired' },
         { name: 'Elon', job: 'Visionary' },
         { name: 'Me' }
    ]);

    return <BryntumGrid column={columns} data={data} />
}
```

```
<bryntum-grid :columns="columns" :data="data" />
```

```
export default {
   setup() {
     return {
       columns : [
         { field: 'name', text: 'Name' },
         { field: 'job', text: 'Job', renderer: ({value}) => value || 'Unemployed' }
       ]
       data : reactive([
         { name: 'Bill', job: 'Retired' },
         { name: 'Elon', job: 'Visionary' },
         { name: 'Me' }
       ])
     };
   }
}
```

```
<bryntum-grid [columns]="columns" [data]="data"></bryntum-grid>
```

```
export class AppComponent {
     columns = [
         { field: 'name', text: 'Name' },
         { field: 'job', text: 'Job', renderer: ({value}) => value || 'Unemployed' }
     ]

     data = [
         { name: 'Bill', job: 'Retired' },
         { name: 'Elon', job: 'Visionary' },
         { name: 'Me' }
     ]
 }
```

Features
--------

To avoid the Grid core being bloated, its main features are implemented in separate \`feature\` classes. You can find the Grid features listed in the navigation tree (on the left) under **API docs > Grid > feature**. You can also find them listed and described in [this guide](https://bryntum.com/docs/gantt/api/#Grid/guides/basics/features.md). These can be turned on and off based on your requirements. To configure (or disable) a feature, use the [features](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-features) object to provide your desired configuration for the features you want to use. Each feature has an ´id´ that you use as a key in the features object:

```
const grid = new Grid({
    features : {
        cellEdit     : false,
        regionResize : true,
        cellTooltip  : {
            tooltipRenderer : (data) => {
            }
        },
        ...
    }
});
```

Column configuration options
----------------------------

A grid contains a number of columns stored in a [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) that control how your data is rendered. The simplest option is to point a Column to a field in your dataset, or define a custom [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer). The renderer function receives one object parameter containing rendering data for the current cell being rendered.

```
const grid = new Grid({
    columns: [
        {
            field: 'task',
            text: 'Task',
            renderer(renderData) {
                const record = renderData.record;

                if (record.percentDone === 100) {
                    renderData.cellElement.classList.add('taskDone');
                    renderData.cellElement.style.background = 'green';
                }

                return renderData.value;
            }
        }
    ]
});
```

You can modify columns programmatically easily:

```
// resize first column
grid.columns.first.width = 200;

// Change text
grid.columns.first.text = 'New text';

```

To learn more about modifying individual columns, please see the docs for [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) and [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column).

Grid sections (aka "locked" or "frozen" columns)
------------------------------------------------

The grid can be divided horizontally into individually scrollable sections. This is great if you have lots of columns that don't fit the available width of the screen. To enable this feature, simply mark the columns you want to `lock`. Locked columns are then displayed in their own section to the left of the other columns:

```
const grid = new Grid({
    width    : 500,
    subGridConfigs : {
        // set a fixed locked section width if desired
        locked : { width: 300 }
    },
    columns : [
        { field : 'name', text : 'Name', width : 200, locked : true },
        { field : 'firstName', text : 'First name', width : 100, locked : true },
        { field : 'surName', text : 'Last name', width : 100, locked : true },
        { field : 'city', text : 'City', width : 100 },
        { type : 'number', field : 'age', text : 'Age', width : 200 },
        { field : 'food', text : 'Food', width : 200 }
    ]
});
```

You can also move columns between sections by using drag and drop, or use the built-in header context menu. If you want to be able to resize the locked grid section, enable the [RegionResize](https://bryntum.com/docs/gantt/api/#Grid/feature/RegionResize) feature.

Filtering
---------

One important requirement of a good Grid component is the ability to filter large datasets to quickly find what you are looking for. To enable filtering (through the context menu), add the [Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter) feature:

```
const grid = new Grid({
    features: {
        filter: true
    }
});
```

Or activate a default filter at initial rendering:

```
const grid = new Grid({
    features: {
        filter: { property : 'city', value : 'New York' }
    }
});
```

Tooltips
--------

If you have a data models with many fields, and you want to show additional data when hovering over a cell, use the [CellTooltip](https://bryntum.com/docs/gantt/api/#Grid/feature/CellTooltip) feature. To show a tooltip for all cells:

```
const grid = new Grid({
    features: {
        cellTooltip: ({value}) => value
    }
});
```

Inline Editing (default **on**)
-------------------------------

To enable inline cell editing in the grid, simply add the [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature:

```
const grid = new Grid({
    features : {
        cellEdit : true
    },
    columns: [
        {
            field: 'task',
            text: 'Task'
        }
    ]
});
```

Context Menu
------------

Use [CellMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/CellMenu) and [HeaderMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/HeaderMenu) features if you want your users to be able to interact with the data through the context menu:

```
const grid = new Grid({
    features : {
        headerMenu : {
            items : {
                showInfo : {
                    text   : 'Show info',
                    icon   : 'fa fa-info-circle',
                    weight : 200,
                    onItem : ({ item }) => console.log(item.text)
                }
            }
        },
        cellMenu :  {
            items : {
                showOptions : {
                    text   : 'Show options',
                    icon   : 'fa fa-gear',
                    weight : 200
                }
            }
        }
    }
});
```

Grouping
--------

To group rows by a field in your dataset, use the [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) feature.

Searching
---------

When working with lots of data, a quick alternative to filtering is the [Search](https://bryntum.com/docs/gantt/api/#Grid/feature/Search) feature. It highlights matching values in the grid as you type.

Loading and saving data
-----------------------

The grid keeps all its data in a [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store), which is essentially an Array of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) items. You define your own Model representing your data entities and use the Model API to get and set values.

```
class Person extends Model {}

const person = new Person({
    name: 'Steve',
    age: 38
});

person.name = 'Linda'; // person object is now `dirty`

const store = new Store({
    data : [
        { name : 'Don', age : 40 }
    ]
});

store.add(person);

console.log(store.count); // === 2

store.remove(person); // Remove from store
```

When you update a record in a store, it's considered dirty, until you call [commit](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#function-commit) on the containing Store. You can also configure your Store to commit automatically (like Google docs). If you use an AjaxStore, it will send changes to your server when commit is called.

Any changes you make to the Store or its records are immediately reflected in the Grid, so there is no need to tell it to refresh manually.

To create a custom load mask, subscribe to the grid's store events and [mask](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-masked) on [beforeRequest](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-beforeRequest) and unmask on [afterRequest](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-afterRequest). The mask can also be used to display error messages if an [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) occurs.

```
 const grid = new Grid({
     loadMask : null
 });

 grid.store.on({
     beforeRequest() {
         grid.masked = {
             text : 'Data is loading...'
         };
     },
     afterRequest() {
         grid.masked = null;
     },
     exception({ response }) {
         grid.masked.error = response.message || 'Load failed';
     }
 });

 store.load();
```

To learn more about loading and saving data, please refer to [this guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/displayingdata.md).

Lazy loading (infinite scroll)
------------------------------

Enabling lazy loading of Grid records makes it possible to load the dataset in chunks when records are scrolled into view, instead of loading the complete dataset at once.

Set the [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad) config on the Store to `true` to enable this behaviour. You will also need something that initiates the first load, either use [autoLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-autoLoad) or call the [load](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-load) function manually.

**Using an AjaxStore**

```
new Grid({
    store: {
        // This will create an AjaxStore
        readUrl: 'backend/read',
        // This will activate the lazy load functionality
        lazyLoad: true,
        // This will load the Store initially upon creation
        autoLoad: true
    }
});
```

**Using a regular Store**

```
class MyStore extends Store {
    static configurable = {
        lazyLoad: true,
        autoLoad: true
    };

    async requestData({
        startIndex,
        count
    }) {
        const response = await fetchData({
            startIndex,
            count
        });

        // The requestData function is expected to return an object
        // with a data property, whose value contains all the records
        return {
            data: response.data,
            // And optionally, but recommended, is to provide a total
            // count of all available records
            total: response.totalCount
        }
    }
}

new Grid({
    store: new MyStore()
});
```

Please note that, when using a lazy loaded Store, there is a number of Grid features, functions and configs that are either not supported at all or only works in a limited way. Such information is available in the corresponding documentation.

There is also a [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md) on how to use lazy loading in your Grid's store.

Default configs
---------------

There is a myriad of configs and features available for Grid, some of them on by default and some of them requiring extra configuration. The code below tries to illustrate the major things that are used by default:

```
const grid = new Grid({
   // The following features are enabled by default:
   features : {
       cellEdit      : true,
       columnPicker  : true,
       columnReorder : true,
       columnResize  : true,
       cellMenu      : true,
       headerMenu    : true,
       group         : true,
       rowCopyPaste  : true, // Allow using [Ctrl/CMD + C/X] and [Ctrl/CMD + V] to copy/cut and paste rows
       sort          : true
   },

   autoHeight                : false, // Grid needs to have a height supplied through CSS (strongly recommended) or by specifying `height`
   columnLines               : true,  // Themes might override it to hide lines anyway
   emptyText                 : 'No rows to display',
   enableTextSelection       : false, // Not allowed to select text in cells by default,
   fillLastColumn            : true,  // By default the last column is stretched to fill the grid
   fullRowRefresh            : true,  // Refreshes entire row when a cell value changes
   loadMask                  : 'Loading...',
   resizeToFitIncludesHeader : true,  // Also measure header when auto resizing columns
   responsiveLevels : {
     small : 400,
     medium : 600,
     large : '*'
   },
   rowHeight                  : null,  // Determined using CSS, it will measure rowHeight
   showDirty                  : false, // No indicator for changed cells
});
```

Keyboard shortcuts
------------------

Grid has the following default keyboard shortcuts:

Keys

Action

Weight ¹

Action description

`ArrowUp`

_navigateUp_

10

Focuses the cell above currently focused cell.

`ArrowRight`

_navigateRight_

10

Focuses the cell to the right of currently focused cell

`ArrowDown`

_navigateDown_

10

Focuses the cell below currently focused cell

`ArrowLeft`

_navigateLeft_

10

Focuses the cell to the left of currently focused cell

`Shift`+`ArrowUp`

_extendSelectionUp_

Extends the selection one row up from currently focused cell

`Shift`+`ArrowRight`

_extendSelectionRight_

Extends the selection one column to the right from currently focused cell

`Shift`+`ArrowDown`

_extendSelectionDown_

Extends the selection one row down from currently focused cell

`Shift`+`ArrowLeft`

_extendSelectionLeft_

Extends the selection one column to the left from currently focused cell

`Space`

_toggleSelection_

10

Toggles selection of currently focused cell if selectionMode.selectOnKeyboardNavigation is `false`

injects `contextmenu` event into the cell.

`Ctrl`+`Home`

_navigateFirstCell_

Focuses the first cell at the first row (including header)

`Home`

_navigateFirstColumn_

Focuses the first cell of current focused row

`Ctrl`+`End`

_navigateLastCell_

Focuses the last cell of the last row

`End`

_navigateLastColumn_

Focuses the last cell of current focused row

`PageUp`

_navigatePrevPage_

Displays previous page

`PageDown`

_navigateNextPage_

Displays next page

`Enter`

_activateCell_

Clicks header when focused on a header. Activates the cell if cell element focused.

Activation means activating cell editing or focusing the first focusable element in the cell.

`Escape`

_deactivateCell_

Deactivates cell when focus is inside the cell. Cancels cell editing. Focuses cell element

`F2`

_toggleCellActivate_

Toggles cell activation. Enters and exits cell editing or focuses into and out of the cell.

`Ctrl`+`Z`

_undoRedoKeyPress_

Undo/redo (when using [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager))

`Ctrl`+`Shift`+`Z`

_undoRedoKeyPress_

Undo/redo (when using [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager))

**¹** Customization of keyboard shortcuts that has a `weight` can affect other features that also uses that particular keyboard shortcut. Read more in [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md).

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

The following Grid features has their own keyboard shortcuts. Follow the links for details.

* [CellCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste#keyboard-shortcuts)
* [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit#keyboard-shortcuts)
* [CellMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/CellMenu#keyboard-shortcuts)
* [ColumnRename](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnRename#keyboard-shortcuts)
* [Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter#keyboard-shortcuts)
* [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#keyboard-shortcuts)
* [HeaderMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/HeaderMenu#keyboard-shortcuts)
* [QuickFind](https://bryntum.com/docs/gantt/api/#Grid/feature/QuickFind#keyboard-shortcuts)
* [RowCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste#keyboard-shortcuts)
* [Search](https://bryntum.com/docs/gantt/api/#Grid/feature/Search#keyboard-shortcuts)
* [Tree](https://bryntum.com/docs/gantt/api/#Grid/feature/Tree#keyboard-shortcuts)

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md)

Performance
-----------

In general the Grid widget has very good performance and you can try loading any amount of data in the [bigdataset](https://bryntum.com/docs/gantt/api/../examples/bigdataset/) demo. The overall rendering performance is naturally affected by many other things than the data volume. Other important factors that can impact performance: number of columns, complex cell renderers, locked columns, the number of features enabled and of course the browser (Chrome fastest).

Accessibility
-------------

As far as possible, the grid is accessible to WAI-ARIA standards. Every cell, including column header cells is visitable. The arrow keys navigate, and if a cell contains focusable content, navigating to that cell focuses the content. `Escape` will exit from that and focus the encapsulating cell.

When tabbing back into a grid that has previously been entered, focus moves to the last focused cell.

The column menu is invoked using the `Space` key when focused on a column header.

The cell menu is invoked using the `Space` key when focused on a data cell.

Saving state
------------

The grid supports saving its UI [state](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) to ensure end users will see the same column sizes, sorting, grouping settings as they reload the page / app. Please refer to the [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) and [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) documentation for more information on state management.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGrid](https://bryntum.com/docs/gantt/api/Grid/view/Grid#property-isGrid)
Identifies an object as an instance of [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) class, or subclass thereof.

[isGrid](https://bryntum.com/docs/gantt/api/Grid/view/Grid#property-isGrid-static)
Identifies an object as an instance of [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) class, or subclass thereof.
