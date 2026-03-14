# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StorePaging.md

# [StorePaging](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging)

Mixin for Store that handles paging

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[pageSize](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#config-pageSize)
When the Store is paged by configuring [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#config-remotePaging), this value will be included in the load requests.

**Note:** Setting pageSize at runtime will automatically reload the page.

[pageSizeParamName](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#config-pageSizeParamName)
The name of the parameter to use when requesting pages of data, representing the configured [pageSize](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#config-pageSize) value.

[pageParamName](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#config-pageParamName)
The name of the parameter to use when requesting pages of data using the **zero based** index of the required page's starting record.

[pageStartParamName](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#config-pageStartParamName)
The name of the parameter to use when requesting pages of data using the **one based** page number required.

[remotePaging](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#config-remotePaging)
Set this to `true` to activate remote paging in this Store. Makes it possible to use the [loadPage](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#function-loadPage), [nextPage](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#function-nextPage), and [previousPage](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#function-previousPage) functions. Or add the [PagingToolbar](https://bryntum.com/docs/gantt/api/#Core/widget/PagingToolbar) to control what page to load.

For a non-[AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be requested by the Store by calling a by the app implemented [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function. Data can also be provided by listening to the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-requestData) event, and updating the [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) property with new data.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStorePaging](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#property-isStorePaging)
Identifies an object as an instance of [StorePaging](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging) class, or subclass thereof.

[isStorePaging](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#property-isStorePaging-static)
Identifies an object as an instance of [StorePaging](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging) class, or subclass thereof.

[pageSize](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#property-pageSize)
When the Store is paged by configuring [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#config-remotePaging), this value will be included in the load requests.

**Note:** Setting pageSize at runtime will automatically reload the page.

[currentPage](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#property-currentPage)
**If the store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#property-isPaged)**, yields the current page number.

[isPaged](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#property-isPaged)
Yields `true` if this Store is loaded page by page. See the [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#config-remotePaging) config.

[lastPage](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#property-lastPage)
**If the store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#property-isPaged)**, yields the highest page number in the dataset as calculated from the 'total' returned in the last page data block loaded.

## Functions

Functions are methods available for calling on the class

[loadPage](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#function-loadPage)
Loads a page of data from the implemented [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function.

[nextPage](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#function-nextPage)
If this store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#property-isPaged), and is not already at the [lastPage](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#property-lastPage) then this will load the next page of data.

[previousPage](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#function-previousPage)
If this store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#property-isPaged), and is not already at the first page then this will load the previous page of data.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeLoadPage](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#event-beforeLoadPage)
When the store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#property-isPaged), this is fired before loading a page and is cancelable

[loadPage](https://bryntum.com/docs/gantt/api/Core/data/mixin/StorePaging#event-loadPage)
When the store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StorePaging#property-isPaged), this is fired when a page is loaded.
