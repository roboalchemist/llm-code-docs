# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/CollectionSorter.md

# [CollectionSorter](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter)

A class which encapsulates a single sorter operation which may be applied to a [Collection](https://bryntum.com/docs/gantt/api/#Core/util/Collection) to order its elements in a specific way.

A CollectionSorter generally has two properties:

* `property` - The name of a property in collection objects by which to sort
* `direction` - The sort direction, `'ASC'` or `'DESC'`.

It may also be configured with just a [sortFn](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-sortFn) function which returns the desired comparison result when passed two objects to compare. Note that this does _not_ require or use the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-property) config. Two collection items are passed for comparison.

Further configurations may affect how the sorter is applied:

* `convert` - A function which, when passed the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-property) value from a collection object, returns the value to sort by.

A CollectionSorter may be configured to encapsulate a [sortFn](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-sortFn) by passing that function as the sole parameter to the constructor:

```
    new CollectionSorter((lhs, rhs) => {
        lhs = lhs.customerDetails.companyName.toLowerCase();
        rhs = rhs.customerDetails.companyName.toLowerCase();

        if (lhs < rhs) {
            return -1;
        }
        else if (lhs > rhs) {
            return 1;
        }
        else {
            return 0;
        }
    });
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[property](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#config-property)
The name of a property of collection objects which yields the value to sort by.

[caseSensitive](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#config-caseSensitive)
Configure as `false` to have string comparisons case-insensitive.

[direction](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#config-direction)
The direction to sort in, `'ASC'` or `'DESC'`

[sortFn](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#config-sortFn)
A function which takes the place of using [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-property) and [direction](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-direction). The function is passed two objects from the collection to compare and must return the comparison result.

[convert](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#config-convert)
When using [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-property), this may be specified as a function which takes the raw property value and returns the value to actually sort by.

[id](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#config-id)
The `id` of this Sorter for when used by a [Collection](https://bryntum.com/docs/gantt/api/#Core/util/Collection) Collection. By default the `id` is the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-property) value.

[useLocaleSort](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#config-useLocaleSort)
Use `localeCompare()` when sorting, which lets the browser sort in a locale specific order. Set to `true`, a locale string or a locale config to enable.

Enabling this has big negative impact on sorting performance. For more info on `localeCompare()`, see [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare).

```
collection.addSorter({ property : 'name', useLocaleSort : 'sv-SE' });
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[id](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#property-id)
When in a Collection (A Collection holds its Sorters in a Collection), we need an id.

## Functions

Functions are methods available for calling on the class

[defaultSortFn](https://bryntum.com/docs/gantt/api/Core/util/CollectionSorter#function-defaultSortFn)
Default sortFn used when no sortFn specified. Uses the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-property), [direction](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-direction), and [convert](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter#config-convert).
