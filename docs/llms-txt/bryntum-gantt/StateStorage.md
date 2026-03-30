# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/state/StateStorage.md

# [StateStorage](https://bryntum.com/docs/gantt/api/Core/state/StateStorage)

Base class representing interface used by the [StateProvider](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider) to actually store the state data. This class is not intended to be used directly.

This class has an interface similar to the [Storage API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Storage).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[data](https://bryntum.com/docs/gantt/api/Core/state/StateStorage#property-data)
Returns an object with all stored keys and their values as its properties

[keys](https://bryntum.com/docs/gantt/api/Core/state/StateStorage#property-keys)
Returns the stored keys as set by [setItem](https://bryntum.com/docs/gantt/api/#Core/state/StateStorage#function-setItem)

## Functions

Functions are methods available for calling on the class

[clear](https://bryntum.com/docs/gantt/api/Core/state/StateStorage#function-clear)
Remove all stored keys

[getItem](https://bryntum.com/docs/gantt/api/Core/state/StateStorage#function-getItem)
Returns key value as set by [setItem](https://bryntum.com/docs/gantt/api/#Core/state/StateStorage#function-setItem)

[removeItem](https://bryntum.com/docs/gantt/api/Core/state/StateStorage#function-removeItem)
Removes the specified key

[setItem](https://bryntum.com/docs/gantt/api/Core/state/StateStorage#function-setItem)
Sets the specified key to the given value
