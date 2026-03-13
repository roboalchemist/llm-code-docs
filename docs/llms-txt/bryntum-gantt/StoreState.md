# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreState.md

# [StoreState](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreState)

A Mixin for Store that manages its state.

* **sorters**
* **groupers**
* **collapsedGroups** Data about which groups are collapsed
* **filters**: Only serializable filters are saved (filters defined with `property` and `value`).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreState](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreState#property-isStoreState)
Identifies an object as an instance of [StoreState](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreState) class, or subclass thereof.

[isStoreState](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreState#property-isStoreState-static)
Identifies an object as an instance of [StoreState](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreState) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getState](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreState#function-getState)
Get store state. Used by State-plugin to serialize state

[applyState](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreState#function-applyState)
Apply store state. Used by State-plugin to restore a previously serialized state
