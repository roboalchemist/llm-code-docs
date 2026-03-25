# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/crud/mixin/LazyLoadCrudManager.md

# [LazyLoadCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager)

Mixin for CrudManager that handles lazy loading.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[lazyLoad](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#config-lazyLoad)
If set to `true`, or a config object, this makes the CrudManager load records only when needed. When a record or a date range that is not already loaded is requested, a load request will be made to the specified URL. More more details about lazy loading, see the [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md)

[remotePaging](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#config-remotePaging)
If set to `true`, this makes the CrudManager load pages of data, instead of loading the complete dataset at once. The requests made to the [loadUrl](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#config-loadUrl) will contain params with info about the current dataset being requested:

* `page` - The resource page
* `pageSize` - The resource page size
* `startDate` - The start date of the calculated timespan
* `endDate` - The end date of the calculated timespan

For more details about paging, see the [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/paging.md)

[pageSize](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#config-pageSize)
The number of Resource records each page should contain, when using [remotePaging](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/LazyLoadCrudManager#config-remotePaging)

[requestData](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#config-requestData)
When the CrudManager/Project is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/LazyLoadCrudManager#config-lazyLoad) set to `true`, you can configure your own data fetching logic by implementing this function. Doing this will override the built-in fetching mechanism using the [loadUrl](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager#config-loadUrl).

When implementing this, it is expected that what is returned is an object fulfilling the [contract](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager) of a regular CrudManager/Project load call.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isLazyLoadCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#property-isLazyLoadCrudManager)
Identifies an object as an instance of [LazyLoadCrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/LazyLoadCrudManager) class, or subclass thereof.

[isLazyLoadCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#property-isLazyLoadCrudManager-static)
Identifies an object as an instance of [LazyLoadCrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/LazyLoadCrudManager) class, or subclass thereof.

[lazyLoad](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#property-lazyLoad)
If set to `true`, or a config object, this makes the CrudManager load records only when needed. When a record or a date range that is not already loaded is requested, a load request will be made to the specified URL. More more details about lazy loading, see the [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md)

## Typedefs

Typedefs are type definitions for the class

[LazyLoadCrudManagerRequestParams](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#typedef-LazyLoadCrudManagerRequestParams)
An object containing details about the requested data

[CrudManagerRequestResponse](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/LazyLoadCrudManager#typedef-CrudManagerRequestResponse)
An object containing details about the received data used for lazy and paged loading
