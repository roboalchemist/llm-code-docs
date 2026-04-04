# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreSearch.md

# [StoreSearch](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch)

Mixin for Store that handles searching (multiple records) and finding (single record).

```
// find all records that has a field containing the string john
const hits = store.search('john');
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreSearch](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#property-isStoreSearch)
Identifies an object as an instance of [StoreSearch](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSearch) class, or subclass thereof.

[isStoreSearch](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#property-isStoreSearch-static)
Identifies an object as an instance of [StoreSearch](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSearch) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[search](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#function-search)
Find all hits matching the specified input.

```
const store = new Store({
  fields : ['name', 'kind'],
  data : [
    { id : 1, name : 'Batman', kind : 'hero' },
    { id : 2, name : 'Batkid', kind : 'hero' },
    { id : 3, name : 'Joker', kind : 'villain' },
    { id : 4, name : 'Penguin', kind : 'villain' }
  ]
});

store.search('villain'); // [{ index : 2, data : joker-record }, { index : 3, data : penguin-record }]
```

[findByField](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#function-findByField)
Find occurrences of the specified `value` in the specified `field` on all locally available records in the store

[find](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#function-find)
Finds the first record for which the specified function returns true

[findRecord](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#function-findRecord)
Finds the first record for which the specified field has the specified value

[query](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#function-query)
Searches the Store records using the passed function.

[some](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#function-some)
Returns true if the supplied function returns true for any record in the store

## Typedefs

Typedefs are type definitions for the class

[StoreSearchResult](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSearch#typedef-StoreSearchResult)
Format returned by Store#findByField().
