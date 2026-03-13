# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/Column.md

# [Column](https://bryntum.com/docs/gantt/api/Grid/column/Column)

The base class for all other grid column types, used if no type is specified on a column.

Default editor is a [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField).

```
const grid = new Grid({
  columns : [{
    field : 'name',
    text  : 'Name'
  }, {
    text  : 'Hobby',
    field : 'others.hobby', // reading nested field data
  }, {
    type  : 'number', // Will use NumberColumn
    field : 'age',
    text  : 'Age'
  }]
});
```

Column types
------------

Grid ships with multiple different column types. Which type to use for a column is specified by the `type` config. The built-in types are:

* [action](https://bryntum.com/docs/gantt/api/#Grid/column/ActionColumn) - displays actions (clickable icons) in the cell.
* [aggregate](https://bryntum.com/docs/gantt/api/#Grid/column/AggregateColumn) - a column, which, when used as part of a Tree, aggregates the values of this column's descendants using a configured function which defaults to `sum`.
* [check](https://bryntum.com/docs/gantt/api/#Grid/column/CheckColumn) - displays a checkbox in the cell.
* [date](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn) - displays a date in the specified format.
* [number](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn) - a column for showing/editing numbers.
* [percent](https://bryntum.com/docs/gantt/api/#Grid/column/PercentColumn) - displays a basic progress bar.
* [rating](https://bryntum.com/docs/gantt/api/#Grid/column/RatingColumn) - displays a star rating.
* [rownumber](https://bryntum.com/docs/gantt/api/#Grid/column/RowNumberColumn) - displays the row number in each cell.
* [template](https://bryntum.com/docs/gantt/api/#Grid/column/TemplateColumn) - uses a template for cell content.
* [time](https://bryntum.com/docs/gantt/api/#Grid/column/TimeColumn) - displays a time in the specified format.
* [tree](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn) - displays a tree structure when using the [tree](https://bryntum.com/docs/gantt/api/#Grid/feature/Tree) feature.
* [widget](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn) - displays widgets in the cells.

Tree columns
------------

You can add tree rendering to any column type by configuring it with `tree : true`:

```
const grid = new TreeGrid({
   columns : [
       // These are equivalent:
       { type: 'tree', field: 'name' },
       { field: 'name', tree: true },

       // Any column type can be a tree column:
       { type: 'check', tree: true, field: 'done' }
   ]
});
```

Grouped columns / headers
-------------------------

You can group headers by defining parent and children columns. A group can be dragged as a whole, or users can drag individual columns between groups. The same applies to column visibility using the column picker in the header menu, a group can be toggled as a whole or each column individually.

```
const grid = new Grid({
    {
            text     : 'Parent',
            children : [
                { text : 'Child 1', field : 'field1', flex : 1 },
                { text : 'Child 2', field : 'field2', flex : 1 }
            ]
        },
        ...
}
```

Collapsible columns
-------------------

By configuring a parent column with `collapsible: true` it is made collapsible. When collapsing all child columns except the first one are hidden. This behaviour is configurable using the [collapseMode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-collapseMode) config. To make a column start collapsed, set the [collapsed](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-collapsed) config to `true`.

Adding widgets to the column header
-----------------------------------

You can add custom [widgets](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) to the column header element using the [headerWidgets](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-headerWidgets) config.

Cell renderers and customizing cell content
-------------------------------------------

### Completely controlling cell contents

To completely control what is rendered into a cell, provide a [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) function which returns a string or a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) DOM configuration object.

```
const grid = new Grid({
  columns : [
  ...
    {
      field      : 'approved',
      text       : 'Approved',
      htmlEncode : false, // allow to use HTML code
      renderer({ value }) {
        return value === true ? '<b>Yes</b>' : '<i>No</i>';
      }
    }
    ...
    ]
});
```

### Augmenting the default rendering

To augment the default rendering of Column types which have their own special renderer, you can call the [built-in renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#function-defaultRenderer) from your custom renderer, and use the result. For example, to highlight modified dates in a DateColumn:

```
new Grid({
    columns : [
        ...
        {
            type  : 'date',
            field : 'startDate',
            text  : 'Start Date',
            renderer({ record, value }) {
                const result = this.defaultRenderer({ value });

                return record.isFieldModified('startDate') ? `<span class="modified">${result}</span>` : result;
            }
        }
    ]
});
```

### Mutating the cell element after the default rendering

You can also use the [afterRenderCell](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-afterRenderCell) callback to mutate the cell element after the default rendering.

```
new Grid({
    columns : [
        {
            text     : 'Name',
            afterRenderCell : ({ record, row, cellElement }) => {
                cellElement.classList.toggle('myClass', true);
                // Add special CSS class to new rows that have not yet been saved
                row.cls.newRow = record.isPhantom;
            }
        }
    ]
});
```

### Using JSX in renderers (React)

When using the Bryntum React wrapper, renderers can return JSX elements instead of strings or [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) objects:

```
// In your React component's column config:
const columns = [
    {
        text     : 'Name',
        field    : 'name',
        renderer({ record }) {
            return <MyCustomComponent name={record.name} />;
        }
    }
];

// Then pass to the wrapper:
<BryntumGrid columns={columns} />
```

Using JSX in renderers creates a React portal for each rendered cell. For grids with many rows or frequently re-rendered views, this may impact scrolling performance compared to returning plain strings or [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) objects. Consider using JSX renderers primarily for cells that require complex interactive React components.

Menus
-----

You can add custom items to the context menu for a columns header and for its cells, using [headerMenuItems](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-headerMenuItems) and [cellMenuItems](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-cellMenuItems). Here is an example:

```
const grid = new Grid({
  columns : [
    ...
    {
      type  : 'number',
      field : 'age',
      text  : 'Age',
      headerMenuItems: [{
          text : 'My unique header item',
          icon : 'fa fa-paw',
          onItem() { console.log('item clicked'); }
      }],
      cellMenuItems: [{
          text : 'My unique cell item',
          icon : 'fa fa-plus',
          onItem() { console.log('item clicked'); }
      }]
    }
  ...
  ]
});
```

Columns without a [width](https://bryntum.com/docs/gantt/api/#Grid/column/Column#property-width) will shrink or expand to the [pinnedWidth](https://bryntum.com/docs/gantt/api/#Grid/column/Column#property-pinnedWidth) value when pinned.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[text](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-text)
The text to show in the column header. You can display text vertically by setting the [headerWritingMode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#property-headerWritingMode) property.

[field](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-field)
The [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-name) of the [data model](https://bryntum.com/docs/gantt/api/#Core/data/Model) field to read a cells value from.

Also accepts dot notation to read nested or related data, for example `'address.city'`.

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-renderer)
Renderer function, used to format and style the content displayed in the cell. Return the cell text you want to display. Can also affect other aspects of the cell, such as styling.

You should never modify any records inside this method.

If you provide a `renderer` to a built-in Column such as [DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn), it will completely replace the native rendering. In these cases, you may want to call that column class's [built-in renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#function-defaultRenderer) from your custom renderer to access the default rendered value.

If you mutate `cellElement`, and you want to prevent cell content from being reset during rendering, please return `undefined` from the renderer (or just omit the `return` statement) and make sure that the [alwaysClearCell](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-alwaysClearCell) config is set to `false`.

```
new Grid({
    columns : [
        { text : 'Status', renderer : ({ record }) => record.status }
    ]
});
```

You can also return a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object describing the markup:

```
new Grid({
    columns : [
        {
             text : 'Status',
             renderer : ({ record }) => {
                 return {
                     class : 'myClass',
                     children : [
                         {
                             tag : 'i',
                             class : 'fa fa-pen'
                         },
                         {
                             tag : 'span',
                             text : record.name
                         }
                     ]
                 };
             }
        }
    ]
});
```

You can modify the row element too from inside a renderer to add custom CSS classes:

```
new Grid({
    columns : [
        {
            text     : 'Name',
            renderer : ({ record, row }) => {
               // Add special CSS class to new rows that have not yet been saved
              row.cls.newRow = record.isPhantom;

              return record.name;
        }
    ]
});
```

If you are adding a renderer to a column that has a built in renderer (like [DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn) or [NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn)), you may call the [built-in renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#function-defaultRenderer) from your custom renderer if you want to use the default content and modify it. For example, to highlight modified dates in a DateColumn:

```
new Grid({
    columns : [
        {
            type     : 'date',
            field    : 'startDate',
            text     : 'Start Date',
            renderer : ({ record, column }) => {
                let result = this.defaultRenderer(...arguments);

                // Highlight modified start dates
                if (record.isFieldModified('startDate')) {
                    result = `<span class="modified">${result}</span>`;
                }
                return result;
            }
        }
    ]
});
```

### Using JSX (React)

When using the Bryntum React wrapper, renderers can return JSX elements:

```
renderer({ record, value }) {
    return <MyComponent value={value} record={record} />;
}
```

Using JSX in renderers creates a React portal for each rendered cell. For grids with many rows or frequently re-rendered views, this may impact scrolling performance compared to returning plain strings or [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) objects. Consider using JSX renderers primarily for cells that require complex interactive React components.

[afterRenderCell](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-afterRenderCell)
A callback function called after every cell has been rendered, which lets you mutate the cell/row or contents. This is useful when you want to mutate contents of a pre-configured column (e.g. `CheckColumn`, `WidgetColumn` etc.) without overwriting the built-in `renderer`.

In the method, you can modify the cell / row elements, e.g. to add custom CSS classes:

```
new Grid({
    columns : [
        {
            text     : 'Name',
            afterRenderCell : ({ record, row, cellElement }) => {
                cellElement.classList.toggle('myClass', true);
                // Add special CSS class to new rows that have not yet been saved
                row.cls.newRow = record.isPhantom;
            }
        }
    ]
});
```

[width](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-width)
Column width. If value is Number then width is in pixels

[flex](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-flex)
Column width as a flex weight. All columns with flex specified divide the available space (after subtracting fixed widths) between them according to the flex value. Columns that have `flex : 2` will be twice as wide as those with `flex : 1` (and so on)

[autoWidth](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-autoWidth)
This config sizes a column to fits its content. It is used instead of `width` or `flex`.

This config requires the [ColumnAutoWidth](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnAutoWidth) feature which responds to changes in the grid's store and synchronizes the widths' of all `autoWidth` columns.

If this config is not a Boolean value, it is passed as the only argument to the `resizeToFitContent` method to constrain the column's width.

[autoHeight](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-autoHeight)
This config enables automatic height for all cells in this column. It is achieved by measuring the height a cell after rendering it to DOM, and then sizing the row using that height (if it is greater than other heights used for the row).

Heads up if you render your Grid on page load, if measurement happens before the font you are using is loaded you might get slightly incorrect heights. For browsers that support it we detect that and remeasure when fonts are available.

**NOTE:** Enabling this config comes with a pretty big performance hit. To maintain good performance, we recommend not using it. You can still set the height of individual rows manually, either through [data](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-rowHeight) or via [renderers](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer).

Also note that this setting only works fully as intended with non-flex columns.

Rows will always be at least [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-rowHeight) pixels tall even if an autoHeight cell contains no data.

Manually setting a height from a [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) in this column will take precedence over this config.

[fitMode](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-fitMode)
Mode to use when measuring the contents of this column in calls to [resizeToFitContent](https://bryntum.com/docs/gantt/api/#Grid/column/Column#function-resizeToFitContent). Available modes are:

* 'exact' - Most precise, renders and measures all cells (Default, slowest)
* 'textContent' - Renders all cells but only measures the one with the longest `textContent`
* 'value' - Renders and measures only the cell with the longest data (Fastest)
* 'none'/falsy - Resize to fit content not allowed, a call does nothing

[readOnly](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-readOnly)
Set this to `true` to not allow any type of editing in this column.

[editor](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-editor)
A config object used to create the input field which will be used for editing cells in the column. Used when [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature is enabled. The Editor refers to [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) for a data source.

Configure this as `false` or `null` to prevent cell editing in this column.

All subclasses of [Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field) can be used as editors. The most popular are:

* [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)
* [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)
* [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)
* [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField)
* [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

If record has method set + capitalized field, method will be called, e.g. if record has method named `setFoobar` and the [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) is `foobar`, then instead of `record.foobar = value`, `record.setFoobar(value)` will be called.

`Function` may be used for React application parameter for using JSX components as editors.

```
 columns : [
        {
            type   : 'name',
            field  : 'name',
            width  : 250,
            editor : ref => <TextEditor ref={ref}/>
        },
        ...
]
```

where passing `ref` to the React editor is essential for the editor to work.

NOTE: React editor component must implement `setValue` method which usually internally calls `setState`. React `setState` is asynchronous so we need to return Promise which will be resolved when `setState` finishes. A typical example of `setValue` method implemented in a React editor is:

```
setValue(value) {
    return new Promise(resolve => this.setState({ value }, () => resolve(value)));
}
```

Please consult the [React Integration Guide](https://bryntum.com/docs/gantt/api/#Grid/guides/integration/react/guide.md#using-react-as-cell-editor) for details on usage of React cell editors.

Note that for Column subclasses which have a default editor, the editor config is merged with the Column class's default editor config. This allows an application to reconfigure the default editor to conform to requirements for a specific column:

```
new Grid({
    columns : [{
        type  : 'date',
        field : 'date',
        // Override defaults for the date editor
        editor : {
            step : null // disable back/forward stepping
        }
    }]
});
```

[cellEditor](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-cellEditor)
A config object used to configure an [Editor](https://bryntum.com/docs/gantt/api/#Core/widget/Editor) which contains this Column's [input field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) if [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature is enabled.

[finalizeCellEdit](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-finalizeCellEdit)
A function which is called when a cell edit is requested to finish.

This may be an `async` function which performs complex validation. The return value should be:

* `false` - To indicate a generic validation error
* `true` - To indicate a successful validation, which will complete the editing
* a string - To indicate an error message of the failed validation. This error message will be cleared upon any subsequent user input.

The action for the failed validation is defined with the [invalidAction](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-invalidAction) config.

For example for synchronous validation:

```
const grid = new Grid({
   columns : [
      {
         type : 'text',
         text : 'The column',
         field : 'someField',
         flex : 1,
         finalizeCellEdit : ({ value }) => {
             return value.length < 4 ? 'Value length should be at least 4 characters' : true;
         }
      }
   ]
});
```

Here we've defined a validation `finalizeCellEdit` function, which marks all edits with new value less than 4 characters length as invalid.

For asynchronous validation you can make the validation function async:

```
finalizeCellEdit : async ({ value }) => {
    return await performRemoteValidation(value);
}
```

[managedCellEditing](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-managedCellEditing)
By default, cell editing is finalized when the editor is blurred or if the user taps outside the editor. For complex custom editors, focus or tapping might be expected outside the Bryntum owned editor. In such cases, supply `false` for this config to take manual control over when cell editing in the column should be finalized.

To accept changes, call [finishEditing](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit#function-finishEditing). To reject, call [cancelEditing](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit#function-cancelEditing).

```
// Setup
const grid = new Grid({
  columns : [
    {
      text               : 'Skills',
      field              : 'skills',
      managedCellEditing : false
    }
  ]
});

// From your custom editor, when you are ready to accept changes
grid.finishEditing();
```

[revertOnEscape](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-revertOnEscape)
Setting this option means that pressing the `ESCAPE` key after editing the field will revert the field to the value it had when the edit began. If the value is _not_ changed from when the edit started, the input field's [clearable](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-clearable) behaviour will be activated. Finally, the edit will be canceled.

[invalidAction](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-invalidAction)
How to handle a request to complete a cell edit in this column if the field is invalid. There are three choices:

* `block` The default. The edit is not exited, the field remains focused.
* `allow` Allow the edit to be completed.
* `revert` The field value is reverted and the edit is completed.

[sortable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-sortable)
Allow sorting of data in the column. You can pass true/false to enable/disable sorting, or provide a custom sorting function, or a config object for a [CollectionSorter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter)

```
const grid = new Grid({
    columns : [
         {
             // Disable sorting for this column
             sortable : false
         },
         {
             field : 'name',
             // Custom sorting for this column
             sortable(user1, user2) {
                 return user1.name < user2.name ? -1 : 1;
             }
         },
         {
             // A config object for a Core.util.CollectionSorter
             sortable : {
                 property         : 'someField',
                 direction        : 'DESC',
                 useLocaleCompare : 'sv-SE'
             }
         }
    ]
});
```

When providing a custom sorting function, if the sort feature is configured with `prioritizeColumns : true` that function will also be used for programmatic sorting of the store:

```
const grid = new Grid({
    features : {
      sort : {
          prioritizeColumns : true
      }
    },

    columns : [
         {
             field : 'name',
             // Custom sorting for this column
             sortable(user1, user2) {
                 return user1.name < user2.name ? -1 : 1;
             }
         }
    ]
});

// Will use sortable() from the column definition above
grid.store.sort('name');
```

Also, any custom sorter function is called with an additional parameter indicating the sort direction. Please note that is an informative parameter, the result of the sort function is already reversed if needed depending on direction.

```
const grid = new Grid({
    columns : [
         {
             field : 'name',
             // direction will be ASC or DESC
             sortable(user1, user2, direction) {
                 return user1.name < user2.name ? -1 : 1;
             }
         }
    ]
});
```

[searchable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-searchable)
Allow searching in the column (respected by QuickFind and Search features)

[collapsible](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-collapsible)
If `true`, this column will show a collapse/expand icon in its header, only applicable for parent columns

[collapsed](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-collapsed)
The collapsed state of this column, only applicable for parent columns

[collapseMode](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-collapseMode)
The collapse behavior when collapsing a parent column. Specify `"toggleAll"` or `"showFirst"`.

* `"showFirst"` toggles visibility of all but the first columns.

* `"toggleAll"` toggles all children, useful if you have a special initially hidden column which gets shown in collapsed state. To specify which columns are initially hidden, configure them with [toggleAllHidden](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-toggleAllHidden).

In the snippet below, the first two child columns are initially shown, while the third is initially hidden. When collapsing the parent column, the visibility of all three children will be toggled, so the third column will be shown and the first two hidden.

```
new Grid({
   columns : [{
         text        : 'Parent',
         collapsible : true,
         collapseMode : 'toggleAll',
         children    : [
             { text : 'Shown initially', field : 'field1', flex : 1 },
             { text : 'Shown initially', field : 'field2', flex : 1 },
             { text : 'Hidden initially', field : 'field3', flex : 1, toggleAllHidden : true }
         ]
   }]
});
```

{@note}Note that when using `toggleAll` mode, at least one child column must be configured with `toggleAllHidden: true` and at least one must not.{@/note}

[filterable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-filterable)
Allow filtering data in the column (if [Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter) or [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) feature is enabled).

Also allows passing a custom filtering function that will be called for each record with a single argument of format `{ value, record, [operator] }`. Returning `true` from the function includes the record in the filtered set.

Configuration object may be used for [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) feature to specify `filterField`. See an example in the code snippet below or check [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) page for more details.

```
const grid = new Grid({
    columns : [
         {
             field : 'name',
             // Disable filtering for this column
             filterable : false
         },
         {
             field : 'age',
             // Custom filtering for this column
             filterable: ({ value, record }) => Math.abs(record.age - value) < 10
         },
         {
             field : 'start',
             // Changing default field type
             filterable: {
                 filterField : {
                     type : 'datetime'
                 }
             }
         },
         {
             field : 'city',
             // Filtering for a value out of a list of values
             filterable: {
                 filterField : {
                     type  : 'combo',
                     value : '',
                     items : [
                         'Paris',
                         'Dubai',
                         'Montreal',
                         'London',
                         'New York'
                     ]
                 }
             }
         },
         {
             field : 'score',
             filterable : {
                 // This filter fn doesn't return 0 values as matching filter 'less than'
                 filterFn : ({ record, value, operator, property }) => {
                     switch (operator) {
                         case '<':
                             return record[property] === 0 ? false : record[property] < value;
                         case '=':
                             return record[property] == value;
                         case '>':
                             return record[property] > value;
                     }
                 }
             }
         }
    ]
});
```

When providing a custom filtering function, if the filter feature is configured with `prioritizeColumns : true` that function will also be used for programmatic filtering of the store:

```
const grid = new Grid({
    features : {
        filter : {
            prioritizeColumns : true
        }
    },

    columns : [
         {
             field : 'age',
             // Custom filtering for this column
             filterable: ({ value, record }) => Math.abs(record.age - value) < 10
         }
    ]
});

// Will use filterable() from the column definition above
grid.store.filter({
    property : 'age',
    value    : 50
});
```

To use custom `FilterField` combo `store` it should contain one of these [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) or [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl) configs. Otherwise combo will get data from owner Grid store.

```
const grid = new Grid({
    columns : [
         {
             field : 'name',
             filterable: {
                 filterField {
                     type  : 'combo',
                     store : new Store({
                         data : ['Adam', 'Bob', 'Charlie']
                     })
                 }
             }
         }
    ]
});
```

or

```
const grid = new Grid({
    columns : [
         {
             field : 'name',
             filterable: {
                 filterField : {
                    type  : 'combo',
                    store : new AjaxStore({
                        readUrl  : 'data/names.json',
                        autoLoad : true
                    })
                 }
             }
         }
    ]
});
```

[sealed](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-sealed)
Setting this flag to `true` will prevent dropping child columns into a group column

[hideable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-hideable)
Allow column visibility to be toggled through UI

[draggable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-draggable)
Set to `false` to prevent this column header from being dragged

[groupable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-groupable)
Set to `false` to prevent grouping by this column

[resizable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-resizable)
Set to `false` to prevent the column from being drag-resized when the ColumnResize plugin is enabled.

[groupRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-groupRenderer)
Renderer function for group headers (when using Group feature).

You should never modify any records inside this method.

```
const grid = new Grid({
    columns : [
        {
            text : 'ABC',
            groupRenderer(renderData) {
                return {
                     class : {
                         big   : true,
                         small : false
                     },
                     children : [
                         { tag : 'img', src : 'img.png' },
                         renderData.groupRowFor
                     ]
                };
            }
        }
    ]
});
```

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[headerRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-headerRenderer)
Renderer function for the column header.

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[tooltip](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-tooltip)
A tooltip string to show when hovering the column header, or a config object which can reconfigure the shared tooltip by setting boolean, numeric and string config values.

[tooltipRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-tooltipRenderer)
Renderer function for the cell tooltip (used with [CellTooltip](https://bryntum.com/docs/gantt/api/#Grid/feature/CellTooltip) feature). Specify `false` to disable tooltip for this column.

You should never modify any records inside this method.

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[cellCls](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-cellCls)
CSS class added to each cell in this column

[cls](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-cls)
CSS class added to the header of this column

[icon](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-icon)
Icon to display in header. Specifying an icon will render a `<i>` element with the icon as value for the class attribute

[align](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-align)
Text align. Accepts `'left'`/`'center'`/`'right'` or direction neutral `'start'`/`'end'`

[minWidth](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-minWidth)
Column minimum width. If value is `Number`, then minimal width is in pixels

[maxWidth](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-maxWidth)
Column maximal width. If value is Number, then maximal width is in pixels

[hidden](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-hidden)
Columns hidden state. Specify `true` to hide the column, `false` to show it.

[toggleAllHidden](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-toggleAllHidden)
Only applies for leaf columns in a collapsible group configured with `collapseMode : 'toggleAll'`. Specify `true` to show the column when the group is collapsed, `false` to hide it.

See [collapseMode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-collapseMode) for more details and an example.

[locked](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-locked)
Convenient way of putting a column in the "locked" region. Same effect as specifying region: 'locked'. If you have defined your own regions (using [subGridConfigs](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-subGridConfigs)) you should use [region](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-region) instead of this one.

[region](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-region)
Region (part of the grid, it can be configured with multiple) where to display the column. Defaults to [defaultRegion](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-defaultRegion).

A column under a grouped header automatically belongs to the same region as the grouped header.

[mergeCells](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-mergeCells)
Specify `true` to merge cells within the column whose value match between rows, making the first occurrence of the value span multiple rows.

Only applies when using the [MergeCells feature](https://bryntum.com/docs/gantt/api/#Grid/feature/MergeCells).

This setting can also be toggled using the column header menu.

[mergeable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-mergeable)
Set to `false` to prevent merging cells in this column using the column header menu.

Only applies when using the [MergeCells feature](https://bryntum.com/docs/gantt/api/#Grid/feature/MergeCells).

[mergedRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-mergedRenderer)
An empty function by default, but provided so that you can override it. This function is called each time a merged cell is rendered. It allows you to manipulate the DOM config object used before it is synced to DOM, thus giving you control over styling and contents.

NOTE: The function is intended for formatting, you should not update records in it since updating records triggers another round of rendering.

```
const grid = new Grid({
  columns : [
    {
      field      : 'project',
      text       : 'Project',
      mergeCells : 'true,
      mergedRenderer({ domConfig, value, fromIndex, toIndex }) {
        domConfig.className.highlight = value === 'Important project';
      }
   }
 ]
});
```

[showColumnPicker](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-showColumnPicker)
Show column picker for the column

[enableHeaderContextMenu](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-enableHeaderContextMenu)
false to prevent showing a context menu on the column header element

[enableCellContextMenu](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-enableCellContextMenu)
Set to `false` to prevent showing a context menu on the cell elements in this column

[headerMenuItems](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-headerMenuItems)
Extra items to show in the header context menu for this column.

```
// A rank column, which displays its header text vertically and offers a menu item to toggle that
{
    text              : 'Rank',
    field             : 'rank',
    width             : 30,
    type              : 'number',
    headerWritingMode : 'sideways-lr',
    align             : 'center',
    headerMenuItems   : {
        toggleVerticalText : {
            text    : 'Vertical header text',
            checked : true,
            weight  : 10,
            onItem  : ({ column }) => {
                column.headerWritingMode = column.headerWritingMode ? null : 'sideways-lr';
            }
        }
    }
},
```

[cellMenuItems](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-cellMenuItems)
Extra items to show in the cell context menu for this column, `null` or `false` to not show any menu items for this column.

```
cellMenuItems : {
    customItem : { text : 'Custom item' }
}
```

[sum](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-sum)
Summary type (when using Summary feature). Valid types are:

* `'sum'` - Sum of all values in the column
* `'add'` - Alias for sum
* `'count'` - Number of rows
* `'countNotEmpty'` - Number of rows containing a value
* `'average'` - Average of all values in the column
* `callbackFn` - A custom function, used with `store.reduce`. Its return value becomes the value of the accumulator parameter on the next invocation of callbackFn

[summaries](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-summaries)
Summary configs, use if you need multiple summaries per column. Replaces [sum](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-sum) and [summaryRenderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-summaryRenderer) configs.

[summaryRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-summaryRenderer)
Renderer function for summary (when using Summary feature). The renderer is called with an object having the calculated summary `sum` parameter. Function returns a string value to be rendered.

Example:

```
columns : [{
    type            : 'number',
    text            : 'Score',
    field           : 'score',
    sum             : 'sum',
    summaryRenderer : ({ sum }) => `Total amount: ${sum}`
}]
```

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[responsiveLevels](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-responsiveLevels)
Column settings at different responsive levels, see responsive demo under examples/

[tags](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-tags)
Tags, may be used by ColumnPicker feature for grouping columns by tag in the menu

[touchConfig](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-touchConfig)
Column config to apply to normal config if viewed on a touch device

[tree](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-tree)
When using the tree feature, exactly one column should specify { tree: true }

[filterType](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-filterType)
Determines which type of filtering to use for the column. Usually determined by the column type used, but may be overridden by setting this field.

[headerWritingMode](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-headerWritingMode)
Applies a CSS class that controls the CSS `writing-mode` property for the column header text element.

```
{
    text              : 'Rank',
    field             : 'rank',
    width             : 30,
    type              : 'number',
    headerWritingMode : 'sideways-lr'
}
```

[htmlEncode](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-htmlEncode)
By default, any rendered column cell content is HTML-encoded. Set this flag to `false` disable this and allow rendering html elements

[htmlEncodeHeaderText](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-htmlEncodeHeaderText)
By default, the header text is HTML-encoded. Set this flag to `false` disable this and allow html elements in the column header

[autoSyncHtml](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-autoSyncHtml)
Set to `true`to automatically call DomHelper.sync for html returned from a renderer. Should in most cases be more performant than replacing entire innerHTML of cell and also allows CSS transitions to work. Has no effect unless [htmlEncode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-htmlEncode) is disabled. Returned html must contain a single root element (that can have multiple children). See PercentColumn for example usage.

[alwaysClearCell](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-alwaysClearCell)
Set to `false` to not always clear cell content if the [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) returns `undefined` or has no `return` statement. This is useful when you mutate the cellElement, and want to prevent cell content from being reset during rendering.

Set to `true` to always clear cell content regardless of renderer return value.

[headerWidgets](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-headerWidgets)
An array of the widgets to append to the column header. These widgets have this Column instance as their `owner` which can be used to reference the column, and the owning Grid via `this.owner.grid`.

```
columns : [
{
    text          : 'Name',
    field         : 'name',
    flex          : 1,
    headerWidgets : [
        {
            type      : 'button',
            text      : 'Add row',
            rendition : 'filled',
            async onAction() {
                const
                     grid = this.owner.grid,
                     [newRecord] = grid.store.add({
                         name : 'New user'
                     });

                await grid.scrollRowIntoView(newRecord);

                await grid.features.cellEdit.startEditing({
                    record : newRecord,
                    field  : 'name'
                });
            }
        }
    ]
}]
```

[instantUpdate](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-instantUpdate)
Set to `true` to have the [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature update the record being edited live upon field edit instead of when editing is finished by using `TAB` or `ENTER`

[editTargetSelector](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-editTargetSelector)
An optional query selector to select a sub element within the cell being edited to align a cell editor's `X` position and `width` to.

[exportable](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-exportable)
Used by the Export feature. Set to `false` to omit a column from an exported dataset

[exportedType](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-exportedType)
Column type which will be used by [TableExporter](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter). See list of available types in TableExporter docs. Returns undefined by default, which means column type should be read from the record field.

[ariaLabel](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-ariaLabel)
The `aria-label` to use for this Column\`s header element

[cellAriaLabel](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-cellAriaLabel)
The `aria-label` to use for cells in this Column

[vue](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-vue)
Flag to enable vue component rendering

[formula](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-formula)
Set to `true` to have the cell editor for this column inherit formula providers from the Grid's configured [formulaProviders](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-formulaProviders).

[pinned](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-pinned)
Set to `'end'` or `'start'` to pin the column to the respective side of the grid when [PinColumns](https://bryntum.com/docs/gantt/api/#Grid/feature/PinColumns) feature is enabled.

[pinnedWidth](https://bryntum.com/docs/gantt/api/Grid/column/Column#config-pinnedWidth)
When a column is pinned and it does not have a `width` specified, `pinnedWidth` will be used instead.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColumn](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-isColumn)
Identifies an object as an instance of [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) class, or subclass thereof.

[isColumn](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-isColumn-static)
Identifies an object as an instance of [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) class, or subclass thereof.

[type](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-type-static)
Column name alias which you can use in the `columns` array of a Grid.

```
class MyColumn extends Column {
    static get type() {
       return 'mycolumn';
    }
}
```

```
const grid = new Grid({
   columns : [
      { type : 'mycolumn', text : 'The column', field : 'someField', flex : 1 }
   ]
});
```

[type](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-type)
Column name alias, which you can use in the `columns` array of a Grid. See [type](https://bryntum.com/docs/gantt/api/#Grid/column/Column#property-type-static)

[defaults](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-defaults)
Default settings for the column, applied in constructor. None by default, override in subclass.

[text](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-text)
The text to show in the column header. You can display text vertically by setting the [headerWritingMode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#property-headerWritingMode) property.

[field](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-field)
The [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-name) of the [data model](https://bryntum.com/docs/gantt/api/#Core/data/Model) field to read a cells value from.

Also accepts dot notation to read nested or related data, for example `'address.city'`.

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-renderer)
Renderer function, used to format and style the content displayed in the cell. Return the cell text you want to display. Can also affect other aspects of the cell, such as styling.

You should never modify any records inside this method.

If you provide a `renderer` to a built-in Column such as [DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn), it will completely replace the native rendering. In these cases, you may want to call that column class's [built-in renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#function-defaultRenderer) from your custom renderer to access the default rendered value.

If you mutate `cellElement`, and you want to prevent cell content from being reset during rendering, please return `undefined` from the renderer (or just omit the `return` statement) and make sure that the [alwaysClearCell](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-alwaysClearCell) config is set to `false`.

```
new Grid({
    columns : [
        { text : 'Status', renderer : ({ record }) => record.status }
    ]
});
```

You can also return a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object describing the markup:

```
new Grid({
    columns : [
        {
             text : 'Status',
             renderer : ({ record }) => {
                 return {
                     class : 'myClass',
                     children : [
                         {
                             tag : 'i',
                             class : 'fa fa-pen'
                         },
                         {
                             tag : 'span',
                             text : record.name
                         }
                     ]
                 };
             }
        }
    ]
});
```

You can modify the row element too from inside a renderer to add custom CSS classes:

```
new Grid({
    columns : [
        {
            text     : 'Name',
            renderer : ({ record, row }) => {
               // Add special CSS class to new rows that have not yet been saved
              row.cls.newRow = record.isPhantom;

              return record.name;
        }
    ]
});
```

If you are adding a renderer to a column that has a built in renderer (like [DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn) or [NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn)), you may call the [built-in renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#function-defaultRenderer) from your custom renderer if you want to use the default content and modify it. For example, to highlight modified dates in a DateColumn:

```
new Grid({
    columns : [
        {
            type     : 'date',
            field    : 'startDate',
            text     : 'Start Date',
            renderer : ({ record, column }) => {
                let result = this.defaultRenderer(...arguments);

                // Highlight modified start dates
                if (record.isFieldModified('startDate')) {
                    result = `<span class="modified">${result}</span>`;
                }
                return result;
            }
        }
    ]
});
```

### Using JSX (React)

When using the Bryntum React wrapper, renderers can return JSX elements:

```
renderer({ record, value }) {
    return <MyComponent value={value} record={record} />;
}
```

Using JSX in renderers creates a React portal for each rendered cell. For grids with many rows or frequently re-rendered views, this may impact scrolling performance compared to returning plain strings or [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) objects. Consider using JSX renderers primarily for cells that require complex interactive React components.

[afterRenderCell](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-afterRenderCell)
A callback function called after every cell has been rendered, which lets you mutate the cell/row or contents. This is useful when you want to mutate contents of a pre-configured column (e.g. `CheckColumn`, `WidgetColumn` etc.) without overwriting the built-in `renderer`.

In the method, you can modify the cell / row elements, e.g. to add custom CSS classes:

```
new Grid({
    columns : [
        {
            text     : 'Name',
            afterRenderCell : ({ record, row, cellElement }) => {
                cellElement.classList.toggle('myClass', true);
                // Add special CSS class to new rows that have not yet been saved
                row.cls.newRow = record.isPhantom;
            }
        }
    ]
});
```

[width](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-width)
Column width. If value is Number then width is in pixels

[flex](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-flex)
Column width as a flex weight. All columns with flex specified divide the available space (after subtracting fixed widths) between them according to the flex value. Columns that have `flex : 2` will be twice as wide as those with `flex : 1` (and so on)

[autoWidth](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-autoWidth)
This config sizes a column to fits its content. It is used instead of `width` or `flex`.

This config requires the [ColumnAutoWidth](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnAutoWidth) feature which responds to changes in the grid's store and synchronizes the widths' of all `autoWidth` columns.

If this config is not a Boolean value, it is passed as the only argument to the `resizeToFitContent` method to constrain the column's width.

[autoHeight](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-autoHeight)
This config enables automatic height for all cells in this column. It is achieved by measuring the height a cell after rendering it to DOM, and then sizing the row using that height (if it is greater than other heights used for the row).

Heads up if you render your Grid on page load, if measurement happens before the font you are using is loaded you might get slightly incorrect heights. For browsers that support it we detect that and remeasure when fonts are available.

**NOTE:** Enabling this config comes with a pretty big performance hit. To maintain good performance, we recommend not using it. You can still set the height of individual rows manually, either through [data](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-rowHeight) or via [renderers](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer).

Also note that this setting only works fully as intended with non-flex columns.

Rows will always be at least [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-rowHeight) pixels tall even if an autoHeight cell contains no data.

Manually setting a height from a [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) in this column will take precedence over this config.

[fitMode](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-fitMode)
Mode to use when measuring the contents of this column in calls to [resizeToFitContent](https://bryntum.com/docs/gantt/api/#Grid/column/Column#function-resizeToFitContent). Available modes are:

* 'exact' - Most precise, renders and measures all cells (Default, slowest)
* 'textContent' - Renders all cells but only measures the one with the longest `textContent`
* 'value' - Renders and measures only the cell with the longest data (Fastest)
* 'none'/falsy - Resize to fit content not allowed, a call does nothing

[readOnly](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-readOnly)
Set this to `true` to not allow any type of editing in this column.

[editor](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-editor)
A config object used to create the input field which will be used for editing cells in the column. Used when [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature is enabled. The Editor refers to [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) for a data source.

Configure this as `false` or `null` to prevent cell editing in this column.

All subclasses of [Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field) can be used as editors. The most popular are:

* [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)
* [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)
* [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)
* [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField)
* [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

If record has method set + capitalized field, method will be called, e.g. if record has method named `setFoobar` and the [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) is `foobar`, then instead of `record.foobar = value`, `record.setFoobar(value)` will be called.

`Function` may be used for React application parameter for using JSX components as editors.

```
 columns : [
        {
            type   : 'name',
            field  : 'name',
            width  : 250,
            editor : ref => <TextEditor ref={ref}/>
        },
        ...
]
```

where passing `ref` to the React editor is essential for the editor to work.

NOTE: React editor component must implement `setValue` method which usually internally calls `setState`. React `setState` is asynchronous so we need to return Promise which will be resolved when `setState` finishes. A typical example of `setValue` method implemented in a React editor is:

```
setValue(value) {
    return new Promise(resolve => this.setState({ value }, () => resolve(value)));
}
```

Please consult the [React Integration Guide](https://bryntum.com/docs/gantt/api/#Grid/guides/integration/react/guide.md#using-react-as-cell-editor) for details on usage of React cell editors.

Note that for Column subclasses which have a default editor, the editor config is merged with the Column class's default editor config. This allows an application to reconfigure the default editor to conform to requirements for a specific column:

```
new Grid({
    columns : [{
        type  : 'date',
        field : 'date',
        // Override defaults for the date editor
        editor : {
            step : null // disable back/forward stepping
        }
    }]
});
```

[cellEditor](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-cellEditor)
A config object used to configure an [Editor](https://bryntum.com/docs/gantt/api/#Core/widget/Editor) which contains this Column's [input field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) if [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature is enabled.

[finalizeCellEdit](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-finalizeCellEdit)
A function which is called when a cell edit is requested to finish.

This may be an `async` function which performs complex validation. The return value should be:

* `false` - To indicate a generic validation error
* `true` - To indicate a successful validation, which will complete the editing
* a string - To indicate an error message of the failed validation. This error message will be cleared upon any subsequent user input.

The action for the failed validation is defined with the [invalidAction](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-invalidAction) config.

For example for synchronous validation:

```
const grid = new Grid({
   columns : [
      {
         type : 'text',
         text : 'The column',
         field : 'someField',
         flex : 1,
         finalizeCellEdit : ({ value }) => {
             return value.length < 4 ? 'Value length should be at least 4 characters' : true;
         }
      }
   ]
});
```

Here we've defined a validation `finalizeCellEdit` function, which marks all edits with new value less than 4 characters length as invalid.

For asynchronous validation you can make the validation function async:

```
finalizeCellEdit : async ({ value }) => {
    return await performRemoteValidation(value);
}
```

[managedCellEditing](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-managedCellEditing)
By default, cell editing is finalized when the editor is blurred or if the user taps outside the editor. For complex custom editors, focus or tapping might be expected outside the Bryntum owned editor. In such cases, supply `false` for this config to take manual control over when cell editing in the column should be finalized.

To accept changes, call [finishEditing](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit#function-finishEditing). To reject, call [cancelEditing](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit#function-cancelEditing).

```
// Setup
const grid = new Grid({
  columns : [
    {
      text               : 'Skills',
      field              : 'skills',
      managedCellEditing : false
    }
  ]
});

// From your custom editor, when you are ready to accept changes
grid.finishEditing();
```

[revertOnEscape](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-revertOnEscape)
Setting this option means that pressing the `ESCAPE` key after editing the field will revert the field to the value it had when the edit began. If the value is _not_ changed from when the edit started, the input field's [clearable](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-clearable) behaviour will be activated. Finally, the edit will be canceled.

[invalidAction](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-invalidAction)
How to handle a request to complete a cell edit in this column if the field is invalid. There are three choices:

* `block` The default. The edit is not exited, the field remains focused.
* `allow` Allow the edit to be completed.
* `revert` The field value is reverted and the edit is completed.

[sortable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-sortable)
Allow sorting of data in the column. You can pass true/false to enable/disable sorting, or provide a custom sorting function, or a config object for a [CollectionSorter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter)

```
const grid = new Grid({
    columns : [
         {
             // Disable sorting for this column
             sortable : false
         },
         {
             field : 'name',
             // Custom sorting for this column
             sortable(user1, user2) {
                 return user1.name < user2.name ? -1 : 1;
             }
         },
         {
             // A config object for a Core.util.CollectionSorter
             sortable : {
                 property         : 'someField',
                 direction        : 'DESC',
                 useLocaleCompare : 'sv-SE'
             }
         }
    ]
});
```

When providing a custom sorting function, if the sort feature is configured with `prioritizeColumns : true` that function will also be used for programmatic sorting of the store:

```
const grid = new Grid({
    features : {
      sort : {
          prioritizeColumns : true
      }
    },

    columns : [
         {
             field : 'name',
             // Custom sorting for this column
             sortable(user1, user2) {
                 return user1.name < user2.name ? -1 : 1;
             }
         }
    ]
});

// Will use sortable() from the column definition above
grid.store.sort('name');
```

Also, any custom sorter function is called with an additional parameter indicating the sort direction. Please note that is an informative parameter, the result of the sort function is already reversed if needed depending on direction.

```
const grid = new Grid({
    columns : [
         {
             field : 'name',
             // direction will be ASC or DESC
             sortable(user1, user2, direction) {
                 return user1.name < user2.name ? -1 : 1;
             }
         }
    ]
});
```

[searchable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-searchable)
Allow searching in the column (respected by QuickFind and Search features)

[collapsible](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-collapsible)
If `true`, this column will show a collapse/expand icon in its header, only applicable for parent columns

[collapsed](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-collapsed)
The collapsed state of this column, only applicable for parent columns

[collapseMode](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-collapseMode)
The collapse behavior when collapsing a parent column. Specify `"toggleAll"` or `"showFirst"`.

* `"showFirst"` toggles visibility of all but the first columns.

* `"toggleAll"` toggles all children, useful if you have a special initially hidden column which gets shown in collapsed state. To specify which columns are initially hidden, configure them with [toggleAllHidden](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-toggleAllHidden).

In the snippet below, the first two child columns are initially shown, while the third is initially hidden. When collapsing the parent column, the visibility of all three children will be toggled, so the third column will be shown and the first two hidden.

```
new Grid({
   columns : [{
         text        : 'Parent',
         collapsible : true,
         collapseMode : 'toggleAll',
         children    : [
             { text : 'Shown initially', field : 'field1', flex : 1 },
             { text : 'Shown initially', field : 'field2', flex : 1 },
             { text : 'Hidden initially', field : 'field3', flex : 1, toggleAllHidden : true }
         ]
   }]
});
```

{@note}Note that when using `toggleAll` mode, at least one child column must be configured with `toggleAllHidden: true` and at least one must not.{@/note}

[filterable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-filterable)
Allow filtering data in the column (if [Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter) or [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) feature is enabled).

Also allows passing a custom filtering function that will be called for each record with a single argument of format `{ value, record, [operator] }`. Returning `true` from the function includes the record in the filtered set.

Configuration object may be used for [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) feature to specify `filterField`. See an example in the code snippet below or check [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) page for more details.

```
const grid = new Grid({
    columns : [
         {
             field : 'name',
             // Disable filtering for this column
             filterable : false
         },
         {
             field : 'age',
             // Custom filtering for this column
             filterable: ({ value, record }) => Math.abs(record.age - value) < 10
         },
         {
             field : 'start',
             // Changing default field type
             filterable: {
                 filterField : {
                     type : 'datetime'
                 }
             }
         },
         {
             field : 'city',
             // Filtering for a value out of a list of values
             filterable: {
                 filterField : {
                     type  : 'combo',
                     value : '',
                     items : [
                         'Paris',
                         'Dubai',
                         'Montreal',
                         'London',
                         'New York'
                     ]
                 }
             }
         },
         {
             field : 'score',
             filterable : {
                 // This filter fn doesn't return 0 values as matching filter 'less than'
                 filterFn : ({ record, value, operator, property }) => {
                     switch (operator) {
                         case '<':
                             return record[property] === 0 ? false : record[property] < value;
                         case '=':
                             return record[property] == value;
                         case '>':
                             return record[property] > value;
                     }
                 }
             }
         }
    ]
});
```

When providing a custom filtering function, if the filter feature is configured with `prioritizeColumns : true` that function will also be used for programmatic filtering of the store:

```
const grid = new Grid({
    features : {
        filter : {
            prioritizeColumns : true
        }
    },

    columns : [
         {
             field : 'age',
             // Custom filtering for this column
             filterable: ({ value, record }) => Math.abs(record.age - value) < 10
         }
    ]
});

// Will use filterable() from the column definition above
grid.store.filter({
    property : 'age',
    value    : 50
});
```

To use custom `FilterField` combo `store` it should contain one of these [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) or [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl) configs. Otherwise combo will get data from owner Grid store.

```
const grid = new Grid({
    columns : [
         {
             field : 'name',
             filterable: {
                 filterField {
                     type  : 'combo',
                     store : new Store({
                         data : ['Adam', 'Bob', 'Charlie']
                     })
                 }
             }
         }
    ]
});
```

or

```
const grid = new Grid({
    columns : [
         {
             field : 'name',
             filterable: {
                 filterField : {
                    type  : 'combo',
                    store : new AjaxStore({
                        readUrl  : 'data/names.json',
                        autoLoad : true
                    })
                 }
             }
         }
    ]
});
```

[sealed](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-sealed)
Setting this flag to `true` will prevent dropping child columns into a group column

[hideable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-hideable)
Allow column visibility to be toggled through UI

[draggable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-draggable)
Set to `false` to prevent this column header from being dragged

[groupable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-groupable)
Set to `false` to prevent grouping by this column

[resizable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-resizable)
Set to `false` to prevent the column from being drag-resized when the ColumnResize plugin is enabled.

[groupRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-groupRenderer)
Renderer function for group headers (when using Group feature).

You should never modify any records inside this method.

```
const grid = new Grid({
    columns : [
        {
            text : 'ABC',
            groupRenderer(renderData) {
                return {
                     class : {
                         big   : true,
                         small : false
                     },
                     children : [
                         { tag : 'img', src : 'img.png' },
                         renderData.groupRowFor
                     ]
                };
            }
        }
    ]
});
```

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[headerRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-headerRenderer)
Renderer function for the column header.

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[tooltip](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-tooltip)
A tooltip string to show when hovering the column header, or a config object which can reconfigure the shared tooltip by setting boolean, numeric and string config values.

[tooltipRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-tooltipRenderer)
Renderer function for the cell tooltip (used with [CellTooltip](https://bryntum.com/docs/gantt/api/#Grid/feature/CellTooltip) feature). Specify `false` to disable tooltip for this column.

You should never modify any records inside this method.

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[cellCls](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-cellCls)
CSS class added to each cell in this column

[cls](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-cls)
CSS class added to the header of this column

[icon](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-icon)
Icon to display in header. Specifying an icon will render a `<i>` element with the icon as value for the class attribute

[align](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-align)
Text align. Accepts `'left'`/`'center'`/`'right'` or direction neutral `'start'`/`'end'`

[minWidth](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-minWidth)
Column minimum width. If value is `Number`, then minimal width is in pixels

[maxWidth](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-maxWidth)
Column maximal width. If value is Number, then maximal width is in pixels

[hidden](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-hidden)
Columns hidden state. Specify `true` to hide the column, `false` to show it.

[toggleAllHidden](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-toggleAllHidden)
Only applies for leaf columns in a collapsible group configured with `collapseMode : 'toggleAll'`. Specify `true` to show the column when the group is collapsed, `false` to hide it.

See [collapseMode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-collapseMode) for more details and an example.

[locked](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-locked)
Convenient way of putting a column in the "locked" region. Same effect as specifying region: 'locked'. If you have defined your own regions (using [subGridConfigs](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-subGridConfigs)) you should use [region](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-region) instead of this one.

[region](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-region)
Region (part of the grid, it can be configured with multiple) where to display the column. Defaults to [defaultRegion](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-defaultRegion).

A column under a grouped header automatically belongs to the same region as the grouped header.

[mergeCells](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-mergeCells)
Specify `true` to merge cells within the column whose value match between rows, making the first occurrence of the value span multiple rows.

Only applies when using the [MergeCells feature](https://bryntum.com/docs/gantt/api/#Grid/feature/MergeCells).

This setting can also be toggled using the column header menu.

[mergeable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-mergeable)
Set to `false` to prevent merging cells in this column using the column header menu.

Only applies when using the [MergeCells feature](https://bryntum.com/docs/gantt/api/#Grid/feature/MergeCells).

[mergedRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-mergedRenderer)
An empty function by default, but provided so that you can override it. This function is called each time a merged cell is rendered. It allows you to manipulate the DOM config object used before it is synced to DOM, thus giving you control over styling and contents.

NOTE: The function is intended for formatting, you should not update records in it since updating records triggers another round of rendering.

```
const grid = new Grid({
  columns : [
    {
      field      : 'project',
      text       : 'Project',
      mergeCells : 'true,
      mergedRenderer({ domConfig, value, fromIndex, toIndex }) {
        domConfig.className.highlight = value === 'Important project';
      }
   }
 ]
});
```

[showColumnPicker](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-showColumnPicker)
Show column picker for the column

[enableHeaderContextMenu](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-enableHeaderContextMenu)
false to prevent showing a context menu on the column header element

[enableCellContextMenu](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-enableCellContextMenu)
Set to `false` to prevent showing a context menu on the cell elements in this column

[headerMenuItems](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-headerMenuItems)
Extra items to show in the header context menu for this column.

```
// A rank column, which displays its header text vertically and offers a menu item to toggle that
{
    text              : 'Rank',
    field             : 'rank',
    width             : 30,
    type              : 'number',
    headerWritingMode : 'sideways-lr',
    align             : 'center',
    headerMenuItems   : {
        toggleVerticalText : {
            text    : 'Vertical header text',
            checked : true,
            weight  : 10,
            onItem  : ({ column }) => {
                column.headerWritingMode = column.headerWritingMode ? null : 'sideways-lr';
            }
        }
    }
},
```

[cellMenuItems](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-cellMenuItems)
Extra items to show in the cell context menu for this column, `null` or `false` to not show any menu items for this column.

```
cellMenuItems : {
    customItem : { text : 'Custom item' }
}
```

[sum](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-sum)
Summary type (when using Summary feature). Valid types are:

* `'sum'` - Sum of all values in the column
* `'add'` - Alias for sum
* `'count'` - Number of rows
* `'countNotEmpty'` - Number of rows containing a value
* `'average'` - Average of all values in the column
* `callbackFn` - A custom function, used with `store.reduce`. Its return value becomes the value of the accumulator parameter on the next invocation of callbackFn

[summaries](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-summaries)
Summary configs, use if you need multiple summaries per column. Replaces [sum](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-sum) and [summaryRenderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-summaryRenderer) configs.

[summaryRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-summaryRenderer)
Renderer function for summary (when using Summary feature). The renderer is called with an object having the calculated summary `sum` parameter. Function returns a string value to be rendered.

Example:

```
columns : [{
    type            : 'number',
    text            : 'Score',
    field           : 'score',
    sum             : 'sum',
    summaryRenderer : ({ sum }) => `Total amount: ${sum}`
}]
```

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[responsiveLevels](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-responsiveLevels)
Column settings at different responsive levels, see responsive demo under examples/

[tags](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-tags)
Tags, may be used by ColumnPicker feature for grouping columns by tag in the menu

[touchConfig](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-touchConfig)
Column config to apply to normal config if viewed on a touch device

[tree](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-tree)
When using the tree feature, exactly one column should specify { tree: true }

[filterType](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-filterType)
Determines which type of filtering to use for the column. Usually determined by the column type used, but may be overridden by setting this field.

[headerWritingMode](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-headerWritingMode)
Applies a CSS class that controls the CSS `writing-mode` property for the column header text element.

```
{
    text              : 'Rank',
    field             : 'rank',
    width             : 30,
    type              : 'number',
    headerWritingMode : 'sideways-lr'
}
```

[htmlEncode](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-htmlEncode)
By default, any rendered column cell content is HTML-encoded. Set this flag to `false` disable this and allow rendering html elements

[htmlEncodeHeaderText](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-htmlEncodeHeaderText)
By default, the header text is HTML-encoded. Set this flag to `false` disable this and allow html elements in the column header

[autoSyncHtml](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-autoSyncHtml)
Set to `true`to automatically call DomHelper.sync for html returned from a renderer. Should in most cases be more performant than replacing entire innerHTML of cell and also allows CSS transitions to work. Has no effect unless [htmlEncode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-htmlEncode) is disabled. Returned html must contain a single root element (that can have multiple children). See PercentColumn for example usage.

[alwaysClearCell](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-alwaysClearCell)
Set to `false` to not always clear cell content if the [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) returns `undefined` or has no `return` statement. This is useful when you mutate the cellElement, and want to prevent cell content from being reset during rendering.

Set to `true` to always clear cell content regardless of renderer return value.

[headerWidgets](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-headerWidgets)
An array of the widgets to append to the column header. These widgets have this Column instance as their `owner` which can be used to reference the column, and the owning Grid via `this.owner.grid`.

```
columns : [
{
    text          : 'Name',
    field         : 'name',
    flex          : 1,
    headerWidgets : [
        {
            type      : 'button',
            text      : 'Add row',
            rendition : 'filled',
            async onAction() {
                const
                     grid = this.owner.grid,
                     [newRecord] = grid.store.add({
                         name : 'New user'
                     });

                await grid.scrollRowIntoView(newRecord);

                await grid.features.cellEdit.startEditing({
                    record : newRecord,
                    field  : 'name'
                });
            }
        }
    ]
}]
```

[instantUpdate](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-instantUpdate)
Set to `true` to have the [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature update the record being edited live upon field edit instead of when editing is finished by using `TAB` or `ENTER`

[editTargetSelector](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-editTargetSelector)
An optional query selector to select a sub element within the cell being edited to align a cell editor's `X` position and `width` to.

[exportable](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-exportable)
Used by the Export feature. Set to `false` to omit a column from an exported dataset

[exportedType](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-exportedType)
Column type which will be used by [TableExporter](https://bryntum.com/docs/gantt/api/#Grid/util/TableExporter). See list of available types in TableExporter docs. Returns undefined by default, which means column type should be read from the record field.

[ariaLabel](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-ariaLabel)
The `aria-label` to use for this Column\`s header element

[cellAriaLabel](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-cellAriaLabel)
The `aria-label` to use for cells in this Column

[vue](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-vue)
Flag to enable vue component rendering

[formula](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-formula)
Set to `true` to have the cell editor for this column inherit formula providers from the Grid's configured [formulaProviders](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-formulaProviders).

[pinned](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-pinned)
Set to `'end'` or `'start'` to pin the column to the respective side of the grid when [PinColumns](https://bryntum.com/docs/gantt/api/#Grid/feature/PinColumns) feature is enabled.

[pinnedWidth](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-pinnedWidth)
When a column is pinned and it does not have a `width` specified, `pinnedWidth` will be used instead.

[headerWidgetMap](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-headerWidgetMap)
An object which contains a map of the widgets contained in this column header keyed by their [ref](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref).

[editor](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-editor)
The Field to use as editor for this column

[defaultEditor](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-defaultEditor)
A config object specifying the editor to use to edit this column.

[grid](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-grid)
Get the Grid instance to which this column belongs

[subGrid](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-subGrid)
Get the SubGrid to which this column belongs

[subGridElement](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-subGridElement)
Get the element for the SubGrid to which this column belongs

[element](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-element)
The header element for this Column. _Only available after the grid has been rendered_.

**Note that column headers are rerendered upon mutation of Column values, so this value is volatile and should not be cached, but should be read whenever needed.**

[textWrapper](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-textWrapper)
The text wrapping element for this Column. _Only available after the grid has been rendered_.

This is the full-width element which _contains_ the text-bearing element and any icons.

**Note that column headers are rerendered upon mutation of Column values, so this value is volatile and should not be cached, but should be read whenever needed.**

[textElement](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-textElement)
The text containing element for this Column. _Only available after the grid has been rendered_.

**Note that column headers are rerendered upon mutation of Column values, so this value is volatile and should not be cached, but should be read whenever needed.**

[contentElement](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-contentElement)
The child element into which content should be placed. This means where any contained widgets such as filter input fields should be rendered. _Only available after the grid has been rendered_.

**Note that column headers are rerendered upon mutation of Column values, so this value is volatile and should not be cached, but should be read whenever needed.**

[headerText](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-headerText)
Returns header text based on [htmlEncodeHeaderText](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-htmlEncodeHeaderText) config value.

[isVisible](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-isVisible)
An object which contains a map of the header widgets keyed by their [ref](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref).

[allIndex](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-allIndex)
Index among all flattened columns

[width](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-width)
Get/set columns width in px. If column uses flex, width will be undefined. Setting a width on a flex column cancels out flex.

**NOTE:** Grid might be configured to always stretch the last column, in which case the columns actual width might deviate from the configured width.

```
let grid = new Grid({
    appendTo : 'container',
    height   : 200,
    width    : 400,
    columns  : [{
        text  : 'First column',
        width : 100
    }, {
        text  : 'Last column',
        width : 100 // last column in the grid is always stretched to fill the free space
    }]
});

grid.columns.last.element.offsetWidth; // 300 -> this points to the real element width
```

[visible](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-visible)
Set this column to be visible or not

[editorField](https://bryntum.com/docs/gantt/api/Grid/column/Column#property-editorField)
Yields the name of the record field which the [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature edits when invoked on this column. This is usually this Column's [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field), but Column subclasses may implement this property.

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-defaultRenderer)
This property only exists if this column has its own specialized renderer, such as [DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn), [NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn) etc.

Call this function from inside your custom [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) to get the default rendered value of the column. For example:

```
new Grid({
    columns : [
        {
            type     : 'date',
            field    : 'startDate',
            text     : 'Start Date',
            renderer : ({ record, column }) => {
                let result = this.defaultRenderer(...arguments);

                // Highlight modified start dates
                if (record.isFieldModified('startDate')) {
                    result = `<span class="modified">${result}</span>`;
                }
                return result;
            }
        }
    ]
});
```

[shouldSync](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-shouldSync)
Checks whether the other column is in the same position and configured the same as this Column.

[isCellDirty](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-isCellDirty)
Determines if the column cell should be marked as `dirty`.

[getCellClass](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-getCellClass)
Returns the full CSS class set for a cell at the passed [GridLocation](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation) as an object where property keys with truthy values denote a class to be added to the cell.

[getFilterableValue](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-getFilterableValue)
Extracts the value from the record specified by this Column's [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) specification in a format that can be used as a value to match by a [filtering](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter) operation.

The default implementation returns the [getRawValue](https://bryntum.com/docs/gantt/api/#Grid/column/Column#function-getRawValue) value, but this may be overridden in subclasses.

[hide](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-hide)
Hides this column.

[show](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-show)
Shows this column.

[toggle](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-toggle)
Toggles the column visibility.

[toggleChildren](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-toggleChildren)
Toggles the column visibility of all children of a parent column.

[onCollapseChange](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-onCollapseChange)
Toggles the collapsed state of the column. Based on the [collapseMode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-collapseMode), this either hides all but the first child column, or toggles the visibility state of all children (if you want to have a special column shown in collapsed mode).

Only applicable for columns with child columns.

[generateId](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-generateId)
Generates an id for the column when none is set. Generated ids are 'col1', 'col2' and so on. If a field is specified (as it should be in most cases) the field name is used instead: 'name1', 'age2' ...

[resizeToFitContent](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-resizeToFitContent)
Resizes the column to match the widest string in it. By default it also measures the column header, this behaviour can be configured by setting [resizeToFitIncludesHeader](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-resizeToFitIncludesHeader).

Called internally when you double-click the edge between column headers, but can also be called programmatically. For performance reasons it is limited to checking 1000 rows surrounding the current viewport.

[getState](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-getState)
Get column state, used by State mixin

[applyState](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-applyState)
Apply state to column, used by State mixin

[getRawValue](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-getRawValue)
Extracts the value from the record specified by this Column's [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) specification.

This will work if the field is a dot-separated path to access fields in associated records, eg

```
 field : 'resource.calendar.name'
```

**Note:** This is the raw field value, not the value returned by the [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer).

[refreshCell](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-refreshCell)
Refresh the cell for supplied record in this column, if that cell is rendered.

[refreshCells](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-refreshCells)
Refreshes all the cells for this column

[refreshHeader](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-refreshHeader)
Rerender the header for this column

[clearCell](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-clearCell)
Clear cell contents. Base implementation which just sets innerHTML to blank string. Should be overridden in subclasses to clean up for examples widgets.

[canEdit](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-canEdit)
Override in subclasses to allow/prevent editing of certain rows.

[insertChild](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-insertChild)
Insert a child column(s) before an existing child column. Returns `null` if the parent column is [sealed](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-sealed)

[canFillValue](https://bryntum.com/docs/gantt/api/Grid/column/Column#function-canFillValue)
Override in subclasses to prevent this column from being filled with the [FillHandle](https://bryntum.com/docs/gantt/api/#Grid/feature/FillHandle) feature
