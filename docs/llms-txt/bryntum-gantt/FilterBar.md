# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/FilterBar.md

# [FilterBar](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar)

Feature that allows filtering of the grid by entering filters on column headers. The actual filtering is done by the store. For info on programmatically handling filters, see [StoreFilter](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter).

```
// filtering turned on but no initial filter
const grid = new Grid({
  features: {
    filterBar : true
  }
});

// using initial filter
const grid = new Grid({
  features : {
    filterBar : { filter: { property : 'city', value : 'Gavle' } }
  }
});
```

Enabling filtering for a column
-------------------------------

The individual filterability of columns is defined by a `filterable` property on the column which defaults to `true`. If `false`, that column is not filterable. Note: If you have multiple columns configured with the same `field` value, assign an [id](https://bryntum.com/docs/gantt/api/#Core/data/Model#field-id) to the columns to ensure filters work correctly.

The property value may also be a custom filter function.

The property value may also be an object which may contain the following two properties:

* **filterFn** : `Function` A custom filtering function
* **filterField** : `Object` A config object for the filter value input field. See [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField) or the other field widgets for reference.

```
// Custom filtering function for a column
const grid = new Grid({
  features : {
    filterBar : true
  },

  columns: [
     {
       field      : 'age',
       text       : 'Age',
       type       : 'number',
       // Custom filtering function that checks "greater than"
       filterable : ({ record, value }) => record.age > value
     },
     {
       field : 'name',
       // Filterable may specify a filterFn and a config for the filtering input field
       filterable : {
         filterFn : ({ record, value }) => record.name.toLowerCase().indexOf(value.toLowerCase()) !== -1,
         filterField : {
           emptyText : 'Filter name'
         }
       }
     },
     {
       field : 'city',
       text : 'Visited',
       flex : 1,
       // Filterable with multiselect combo to pick several items to filter
       filterable : {
         filterField : {
           type        : 'combo',
           multiSelect : true,
           items       : ['Barcelona', 'Montreal', 'Stockholm']
         }
       }
     }
  ]
});
```

If this feature is configured with `prioritizeColumns : true`, those functions will also be used when filtering programmatically:

```
const grid = new Grid({
   features : {
       filterBar : {
           prioritizeColumns : true
       }
   },

   columns: [
       {
         field      : 'age',
         text       : 'Age',
         type       : 'number',
         // Custom filtering function that checks "greater than" no matter
         // which field user filled in :)
         filterable : ({ record, value, operator }) => record.age > value
       }
   ]
});

// Will be used when filtering programmatically or using the UI
grid.store.filter({
    property : 'age',
    value    : 41
});
```

Filtering using a multiselect combo
-----------------------------------

To filter the grid by choosing values which should match with the store data, use a [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo), and configure your grid like so:

```
const grid = new Grid({
   features : {
       filterBar : true
   },

   columns : [
       {
           id         : 'name',
           field      : 'name',
           text       : 'Name',
           filterable : {
               filterField : {
                   type         : 'combo',
                   multiSelect  : true,
                   valueField   : 'name',
                   displayField : 'name'
               }
           }
       }
   ]
});
```

You can also filter the [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo) values, for example to filter out empty values. Example:

```
const grid = new Grid({
   features : {
       filterBar : true
   },

   columns : [
       {
           text       : 'Airline',
           field      : 'airline',
           flex       : 1,
           filterable : {
               filterField : {
                   type         : 'combo',
                   multiSelect  : true,
                   valueField   : 'airline',
                   displayField : 'airline',
                   store        : {
                       filters : {
                           // Filter out empty values
                           filterBy : record => Boolean(record.airline)
                       }
                   }
               }
           }
       }
   ]
});
```

Remote filtering
----------------

The FilterBar works with remote filtering, either by the use of an [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore) with a configured [filterParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-filterParamName), or a regular [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) with [remoteFilter](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter) activated. Please note that [filterBy](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-filterBy) function is not supported when remote filtering.

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[prioritizeColumns](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#config-prioritizeColumns)
Use custom filtering functions defined on columns also when programmatically filtering by the columns field.

```
const grid = new Grid({
    columns : [
        {
            field : 'age',
            text : 'Age',
            filterable({ record, value }) {
              // Custom filtering, return true/false
            }
        }
    ],

    features : {
        filterBar : {
            prioritizeColumns : true // <--
        }
    }
});

// Because of the prioritizeColumns config above, any custom
// filterable function on a column will be used when
// programmatically filtering by that columns field
grid.store.filter({
    property : 'age',
    value    : 30
});
```

[keyStrokeFilterDelay](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#config-keyStrokeFilterDelay)
The delay in milliseconds to wait after the last keystroke before applying filters. Set to 0 to not trigger filtering from keystrokes, requires pressing ENTER instead

[compactMode](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#config-compactMode)
Specify `true` to enable compact mode for the filter bar. In this mode the filtering fields are styled to transparently overlay the headers, occupying no additional space.

[hidden](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#config-hidden)
Determines `filterBar` visibility. By default it is set to `false` and to hide the `filterBar` set this flag to `true`.

[filter](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#config-filter)
Use to set initial filter.

```
const grid = new Grid({
  features : {
    filterBar : { filter: { property : 'city', value : 'Gavle' } }
  }
});
```

[defaultEnabled](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#config-defaultEnabled)
Whether the feature is enabled on all columns by default. A column's `filterable.filterBar` configuration overrides this setting.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFilterBar](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#property-isFilterBar)
Identifies an object as an instance of [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) class, or subclass thereof.

[isFilterBar](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#property-isFilterBar-static)
Identifies an object as an instance of [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) class, or subclass thereof.

[compactMode](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#property-compactMode)
Toggle compact mode. In this mode the filtering fields are styled to transparently overlay the headers, occupying no additional space.

[clearStoreFiltersOnHide](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#property-clearStoreFiltersOnHide)
By default, column filter is removed when a column is hidden or this feature is disabled. Set this flag to `false` to keep filters in these scenarios.

[hidden](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#property-hidden)
Determines `filterBar` visibility. By default it is set to `false` and to hide the `filterBar` set this flag to `true`.

[defaultEnabled](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#property-defaultEnabled)
Whether the feature is enabled on all columns by default. A column's `filterable.filterBar` configuration overrides this setting.

## Functions

Functions are methods available for calling on the class

[hideFilterBar](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-hideFilterBar)
Hides the filtering fields.

[showFilterBar](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-showFilterBar)
Shows the filtering fields.

[toggleFilterBar](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-toggleFilterBar)
Toggles the filtering fields visibility.

[renderFilterBar](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-renderFilterBar)
Renders the filtering fields for filterable columns.

[renderColumnFilterField](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-renderColumnFilterField)
Renders text field filter in the provided column header.

[updateColumnFilterFields](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-updateColumnFilterFields)
Fills in column filter fields with values from the grid store filters.

[getColumnFilterField](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-getColumnFilterField)
Returns column filter field instance.

[setColumnFilterField](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-setColumnFilterField)
Caches column filter field instance.

[onStoreFilter](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-onStoreFilter)
Fires when store gets filtered. Refreshes field values in column headers.

[renderHeader](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-renderHeader)
Called after headers are rendered, make headers match stores initial sorters

[onColumnFilterFieldChange](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-onColumnFilterFieldChange)
Called when a column text filter field value is changed by user.

[populateHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/FilterBar#function-populateHeaderMenu)
Adds a menu item to toggle filter bar visibility.
