# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/FilterField.md

# [FilterField](https://bryntum.com/docs/gantt/api/Core/widget/FilterField)

A simple text field for filtering a store.

Allows filtering by [field](https://bryntum.com/docs/gantt/api/#Core/widget/FilterField#config-field):

```
const filterField = new FilterField({
   store : eventStore,
   field : 'name'
});
```

Or by using a [filter function](https://bryntum.com/docs/gantt/api/#Core/widget/FilterField#config-filterFunction) for greater control/custom logic:

```
const filterField = new FilterField({
   store          : eventStore,
   filterFunction : (record, value) => record.name.includes(value)
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[field](https://bryntum.com/docs/gantt/api/Core/widget/FilterField#config-field)
The model field name to filter by. Can optionally be replaced by [filterFunction](https://bryntum.com/docs/gantt/api/#Core/widget/FilterField#config-filterFunction)

[store](https://bryntum.com/docs/gantt/api/Core/widget/FilterField#config-store)
The store to filter.

[filterFunction](https://bryntum.com/docs/gantt/api/Core/widget/FilterField#config-filterFunction)
Optional filter function to be called with record and value as parameters for store filtering.

```
{
    type           : 'filterfield',
    store          : myStore,
    filterFunction : (record, value)  => {
       return record.text.includes(value);
    }
}
```

[filterId](https://bryntum.com/docs/gantt/api/Core/widget/FilterField#config-filterId)
In case the `filterId` that is used in the store needs to be referenced elsewhere, it can be configured. This applies to a passed [filterFunction](https://bryntum.com/docs/gantt/api/#Core/widget/FilterField#config-filterFunction) as well as for an internally generated filter. If no value is configured, an internal ID will be generated.

```
{
    type     : 'filterfield',
    store    : myStore,
    filterId : 'ColumnFilter'
}
```

[internalFilter](https://bryntum.com/docs/gantt/api/Core/widget/FilterField#config-internalFilter)
Set this flag to mark the filter as `internal` when adding it to the associated [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store). This prevents the filter from being removed when [Store.clearFilters()](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-clearFilters) is called.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFilterField](https://bryntum.com/docs/gantt/api/Core/widget/FilterField#property-isFilterField)
Identifies an object as an instance of [FilterField](https://bryntum.com/docs/gantt/api/#Core/widget/FilterField) class, or subclass thereof.

[isFilterField](https://bryntum.com/docs/gantt/api/Core/widget/FilterField#property-isFilterField-static)
Identifies an object as an instance of [FilterField](https://bryntum.com/docs/gantt/api/#Core/widget/FilterField) class, or subclass thereof.
