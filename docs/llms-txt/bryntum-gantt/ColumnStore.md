# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/data/ColumnStore.md

# [ColumnStore](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore)

A store specialized in handling [columns](https://bryntum.com/docs/gantt/api/#Grid/column/Column). Used by the Grid to hold its columns and used as a chained store by each SubGrid to hold theirs. Should not be instantiated directly, instead access it through `grid.columns` or `subGrid.columns`.

Observing for changes
---------------------

If you want to listen for changes to the columns in the ColumnStore. For example, if you are interested in when a column has been moved, simply use the `on` method to listen for the [move](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore#event-move) event:

```
grid.columns.on({
    move({ records }) {
        // The `records` object contains the moved column records
    }
});
```

Modifying columns in the ColumnStore
------------------------------------

```
// resize first column
grid.columns.first.width = 200;

// remove city column
grid.columns.get('city').remove();

// add new column
grid.columns.add({text : 'New column'});

// add new column to specific region (SubGrid)
grid.columns.add({text : 'New column', region : 'locked'});

// add new column to 'locked' region (SubGrid)
grid.columns.add({text : 'New column', locked : true});
```

Storing column state
--------------------

To store the size and position of columns after a user makes a change, please see [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoAddField](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#config-autoAddField)
Automatically adds a field definition to the store used by the Grid when adding a new Column displaying a non-existing field.

To enable this behaviour:

```
const grid = new Grid({
    columns : {
        autoAddField : true,
        data         : [
            // Column definitions here
        ]
    }
}
```

[syncDataOnLoad](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#config-syncDataOnLoad)
`ColumnStore` uses `syncDataOnLoad` by default (with `threshold : 1`), to ensure good performance when binding to columns in frameworks.

See [syncDataOnLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-syncDataOnLoad) for more information.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColumnStore](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#property-isColumnStore)
Identifies an object as an instance of [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) class, or subclass thereof.

[isColumnStore](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#property-isColumnStore-static)
Identifies an object as an instance of [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) class, or subclass thereof.

[topColumns](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#property-topColumns)
Returns the top level columns. If using grouped columns, this is the top level columns. If no grouped columns are being used, this is the leaf columns.

[visibleColumns](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#property-visibleColumns)
Returns the visible leaf headers which drive the rows' cell content.

[bottomColumns](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#property-bottomColumns)
Bottom columns are the ones displayed in the bottom row of a grouped header, or all columns if not using a grouped header. They are the columns that actually display any data.

[usesAutoHeight](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#property-usesAutoHeight)
Checks if any column uses autoHeight

[usesFlexAutoHeight](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#property-usesFlexAutoHeight)
Checks if any flex column uses autoHeight

## Functions

Functions are methods available for calling on the class

[getById](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-getById)
Get column by id.

[get](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-get)
Get column by field. To be sure that you are getting exactly the intended column, use [Store#getById()](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-getById) with the columns id instead.

[createRecord](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-createRecord)
Used internally to create a new record in the store. Creates a column of the correct type by looking up the specified type among registered columns.

[getTreeMixedClass](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-getTreeMixedClass)
Returns a cached class that combines the given column class with TreeColumnMixin. Uses class caching to avoid recreating mixed classes repeatedly.

[indexOf](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-indexOf)
indexOf extended to also accept a columns field, for backward compatibility.

```
grid.columns.indexOf('name');
```

[removeAll](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-removeAll)
Removes all columns.

[registerColumnType](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-registerColumnType-static)
Call from custom column to register it with ColumnStore. Required to be able to specify type in column config.

[getColumnClass](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-getColumnClass-static)
Returns registered column class for specified type.

[generateColumnForField](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#function-generateColumnForField)
Generates a **new** [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) instance which may be subsequently added to this store to represent the passed [DataField](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField) of the owning Grid's store.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[columnShow](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#event-columnShow)
Fires when a column is shown.

[columnHide](https://bryntum.com/docs/gantt/api/Grid/data/ColumnStore#event-columnHide)
Fires when a column has been hidden.
