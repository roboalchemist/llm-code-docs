# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/DomDataStore.md

# [DomDataStore](https://bryntum.com/docs/gantt/api/Core/data/DomDataStore)

Stores data on a dom element (by setting element.\_domData). Instead of using HTML5:s element.dataset, which turned out to be slow.

## Functions

Functions are methods available for calling on the class

[get](https://bryntum.com/docs/gantt/api/Core/data/DomDataStore#function-get-static)
Get the data that is connected to a specified `element` or just a specific `key`.

[remove](https://bryntum.com/docs/gantt/api/Core/data/DomDataStore#function-remove-static)
Remove the specified `key` from the data connected to a given `element`.

[set](https://bryntum.com/docs/gantt/api/Core/data/DomDataStore#function-set-static)
Sets all data connected to specified element (completely replacing any existing) or just a specific key. To update data, use DomDataStore#assign instead.

[assign](https://bryntum.com/docs/gantt/api/Core/data/DomDataStore#function-assign-static)
Updates data connected to specified element.
