# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/Bag.md

# [Bag](https://bryntum.com/docs/gantt/api/Core/util/Bag)

A simple collection class to contain unique, keyed items.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[count](https://bryntum.com/docs/gantt/api/Core/util/Bag#property-count)
The number of items in this Bag.

[values](https://bryntum.com/docs/gantt/api/Core/util/Bag#property-values)
The set of values of this Bag.

Setting this property replaces the data set.

## Functions

Functions are methods available for calling on the class

[get](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-get)
Returns the item with the passed `id`.

[add](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-add)
Adds the passed item(s) to this Bag. Existing items with the same ID will be replaced.

[at](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-at)
Returns `nth` item in this Bag.

[remove](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-remove)
Removes the passed item(s) from this Bag.

[countOf](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-countOf)
Returns the number of items in this Bag which elicits a truthy return value from the passed function.

[changeId](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-changeId)
Change the id of an existing member by mutating its idProperty.

[filter](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-filter)
Extracts the matching items from this Bag into an array based upon the passed value filter function.

[includes](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-includes)
Returns `true` if this Collection includes an item with the same `id` as the passed item.

[map](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-map)
Extracts the content of this Bag into an array based upon the passed value extraction function.

[forEach](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-forEach)
Executes the passed function for each item in this Bag, passing in the item.

[find](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-find)
Returns `nth` item in this Bag which elicits a truthy return value from the provided matcher function `fn`.

[sort](https://bryntum.com/docs/gantt/api/Core/util/Bag#function-sort)
Sort the values of this Bag using the passed comparison function.

Setting this property replaces the data set.
