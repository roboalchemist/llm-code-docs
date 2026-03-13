# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreSum.md

# [StoreSum](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSum)

Mixin for Store that handles summaries.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreSum](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSum#property-isStoreSum)
Identifies an object as an instance of [StoreSum](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSum) class, or subclass thereof.

[isStoreSum](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSum#property-isStoreSum-static)
Identifies an object as an instance of [StoreSum](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSum) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[sum](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSum#function-sum)
Returns sum calculated by adding value of specified field for specified records. Defaults to using all locally available records in store

[min](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSum#function-min)
Returns min value for the specified field, can be used with Date or Number values. Defaults to look through all locally available records in store

[max](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSum#function-max)
Returns max value for the specified field, can be used with Date or Number values. Defaults to look through all locally available records in store

[average](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSum#function-average)
Returns the average value for the specified field. Defaults to look through all locally available records in store

[groupSum](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSum#function-groupSum)
Returns sum by adding value of specified field for records in the group with the specified groupValue.
