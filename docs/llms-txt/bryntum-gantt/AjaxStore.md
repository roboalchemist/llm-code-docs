# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/AjaxStore.md

# [AjaxStore](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore)

Store that uses the [Fetch API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) to read data from a remote server, and optionally sends synchronization requests to the server containing information about locally created, modified and deleted records.

Create
------

Posts array of JSON data for newly added records to [createUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-createUrl), expects response containing an array of JSON objects in same order with id set (uses Model#idField as id).

Read
----

Reads array of JSON data from the data packet returned from the [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl). Unique id for each row is required.

By default looks in field 'id' but can be configured by setting [idField](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-idField-static).

Update
------

Posts array of JSON data containing modified records to [updateUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-updateUrl). By default, only changed fields and any fields configured with [alwaysWrite](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-alwaysWrite) are sent. If you want all fields to always be sent, please see [writeAllFields](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-writeAllFields)

Delete
------

Posts to [deleteUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-deleteUrl) with removed records ids (for example id=1,4,7).

```
new AjaxStore({
  createUrl  : 'php/create',
  readUrl    : 'php/read',
  updateUrl  : 'php/update',
  deleteUrl  : 'php/delete',
  modelClass : Customer
});
```

Lazy loading
------------

A store can be configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-lazyLoad) set to `true`. This will make the store send a fetch request to the configured [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl) when a range of records is needed, rather than for the complete dataset at once. Each request will be made up of 1 chunk before and after the requested index (which gives a total of 2 chunks). The chunk size can be configured in the [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-lazyLoad) config.

There is a [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md) for implementing lazy loading in Grid.

Pagination
----------

Configuring an `AjaxStore` with [pageParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-pageParamName) or [pageStartParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-pageStartParamName) means that the store requests **pages** of data from the remote source, sending the configured [pageParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-pageParamName) or [pageStartParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-pageStartParamName) to request the page along with the [pageSizeParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-pageSizeParamName).

If `pageParamName` is set, that is passed with the requested page number **(one based)**, along with the [pageSizeParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-pageSizeParamName).

If `pageStartParamName` is set, that is passed with the requested page starting record index **(zero based)**, along with the [pageSizeParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-pageSizeParamName).

The JSON response packet for one page should look like this:

```
{
    "success" : true,
    "total"   : 50000,
    "data"    : [{
        "id"    : 1,
        "title" : "Row 1"
    }, ... for the rest of the pageSize ... ]
}
```

The [`success` property](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-responseSuccessProperty) indicates whether the request succeeded. If this is `false`, an [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) event is fired.

The store needs to know the total dataset size in order to know how many pages it may ask for. This is returned in the [`total` property](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-responseTotalProperty)

Remote filtering
----------------

To specify that filtering is the responsibility of the server, configure the store with `[filterParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-filterParamName): 'nameOfFilterParameter'`

When this is set, any [filter](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#function-filter) operation causes the store to reload itself, encoding the filters as JSON representations in the [filterParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-filterParamName) HTTP parameter.

The filters will look like this:

```
{
    "field": "country",
    "operator": "=",
    "value": "sweden",
    "caseSensitive": false
}
```

If the value of the filter is a date - it is serialized as a local time, using the format: `YYYY-MM-DDThh:mm:ss.ms`

The encoding may be overridden by configuring an implementation of [encodeFilterParams](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#function-encodeFilterParams) into the store which returns the value for the [filterParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-filterParamName) when passed an _Iterable_ of filters.

Remote sorting
--------------

To specify that sorting is the responsibility of the server, configure the store with `[sortParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-sortParamName): 'nameOfSortParameter'`

When this is set, any [sort](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSort#function-sort) operation causes the store to reload itself, encoding the sorters as JSON representations in the [sortParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-sortParamName) HTTP parameter.

The sorters will look like this:

```
{
    "field": "name",
    "ascending": true
}
```

The encoding may be overridden by configuring an implementation of [encodeSorterParams](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#function-encodeSorterParams) into the store which returns the value for the [sortParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-sortParamName) when passed an _Iterable_ of sorters.

Passing HTTP headers
--------------------

As mentioned above `AjaxStore` uses the Fetch API under the hood. Specify [fetchOptions](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-fetchOptions) and/or [headers](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-headers) to have control over the options passed with all fetch calls. For example to pass along an authorization header:

```
const store = new AjaxStore({
   headers : {
       Authorization : 'auth-contents-goes-here'
   }
});
```

Learn more about the Fetch API over at [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

Getting local record count
--------------------------

To get the number of "visible" records locally available in the store (records that would be shown when using the Store as the data source for a Grid or similar), use the [count](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#property-count) property. This will return the number of records in the store after filtering and grouping has been applied, including the generated group headers and footers but excluding any records inside collapsed parents or group headers:

```
const visibleRecords = store.count;
```

To get other local counts, such as the total number of data records in the store including those collapsed away and filtered out (when not using remote filtering), use the more flexible [getCount](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#function-getCount) method:

```
// Include records that have been filtered out,
// as well as any records inside collapsed groups or tree nodes.
const records = store.getCount({
    collapsed   : true,
    filteredOut : true
});

// Including group headers + summary records
const records = store.getCount({
    headersFooters : true
});

// All records, including group headers and filtered out records
const allRecords = store.getCount({
    all : true
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[responseSuccessProperty](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-responseSuccessProperty)
The optional property name in JSON responses from the server that contains a boolean success/fail status.

```
{
  "responseMeta" : {
  {
    "success" : true,
    "count" : 100
  },
  // The property name used here should match that of 'responseDataProperty'
  "data" : [
    ...
  ]
}
```

The store would be configured with:

```
 {
     ...
     successDataProperty : 'responseMeta.success',
     responseTotalProperty : 'responseMeta.count'
     ...
 }

```

[responseDataProperty](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-responseDataProperty)
The property name in JSON responses from the server that contains the data for the records

```
{
  "success" : true,
  // The property name used here should match that of 'responseDataProperty'
  "data" : [
    ...
  ]
}
```

[responseTotalProperty](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-responseTotalProperty)
The property name in JSON responses from the server that contains the dataset total size **when this store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#property-isPaged) or [lazy loaded](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-lazyLoad)**

```
{
  "success" : true,
  // The property name used here should match that of 'responseDataProperty'
  "data" : [
    ...
  ],
  // The property name used here should match that of 'responseTotalProperty'
  "total" : 65535
}
```

[params](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-params)
An object containing key/value pairs that are passed on the request query string, or in the request body if HTTP method allows. See [paramsInBody](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-paramsInBody) config.

[lazyLoad](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-lazyLoad)
If set to `true`, or a config object, this makes the store load new records when needed. When a record that is not already loaded is requested, a request to the configured [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl) will be made.

LazyLoading is currently not supported in Calendar, Gantt, TaskBoard.

[autoCommitTimeout](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-autoCommitTimeout)
The timeout in milliseconds to wait before persisting changes to the server. Used when [autoCommit](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-autoCommit) is set to `true`.

[includeChildrenInRemoveRequest](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-includeChildrenInRemoveRequest)
Set to `false` to only include the id of a removed parent node in the request to the backend, and not the ids of its children. Applies when configured with a [deleteUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-deleteUrl).

Consider the following scenario, removing parent 1:

```
{
  id : 1,
  children : [
    { id : 11 },
    { id : 12 }
  ]
}
```

With `includeChildrenInRemoveRequest : false`, the backend will only receive the removal of id 1.

With `includeChildrenInRemoveRequest : true` (the default), the backend will receive the removal of id 1, 11 and 12.

[transformLoadedData](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-transformLoadedData)
Pass a function to transform data loaded from the backend before it is turned into records and added to the store

```
new AjaxStore({
     transformLoadedData : response => {
         // Transform the loaded data and return the response object
     }
});
```

[transformCreationData](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-transformCreationData)
Pass a function to transform record creation data before it is sent to the backend

```
new AjaxStore({
     transformCreationData : payload => {
         // Transform the data and return the payload
         for (const creationData of payload.data) {
             creationData.timestamp = Date.now();
         }

         return payload;
     }
});
```

[transformModificationData](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-transformModificationData)
Pass a function to transform records modification data before it is sent to the backend

```
new AjaxStore({
     transformModificationData : payload => {
         // Transform the data and return the payload
         for (const recordData of payload.data) {
             // Some kind of transformation here...
             if (recordData.ignore) {
                 ArrayHelper.remove(payload.data, recordData);
             }
         }

         return payload;
     }
});
```

[transformRemovalData](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-transformRemovalData)
Pass a function to transform record removal data before it is sent to the backend

```
new AjaxStore({
     transformRemovalData : payload => {
         // Transform the data and return the payload
         const transformedData = {};
         for (const id of payload.ids) {
             transformedData[id] = true;
         }
         payload.ids = transformedData;

         return payload;
     }
});
```

[ignoreLoadPropagationChanges](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-ignoreLoadPropagationChanges)
This config is taken into account only when store is part of a scheduling project.

If such store loads data via [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl), automatic calculation of the schedule after the load might lead to some data modifications (for example if [syncDataOnLoad](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-syncDataOnLoad) is enabled). Such modifications will then be submitted back to the server, which might not be needed, since the data is already coming from the server.

Enabling this config will ignore data modifications during the propagation stage and nothing will be submitted to server.

[restfulFilter](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-restfulFilter)
Set this flag to true if you are filtering remote using restful URLs (e.g. https://nominatim.openstreetmap.org/search/paris?format=json)

**Note:** When this is set, the filter string is appended to the readUrl.

[headers](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-headers)
A string keyed object containing the HTTP headers to add to each server request issued by this store.

`AjaxStore` uses the Fetch API under the hood, read more about headers on [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#headers)

Example usage:

```
const store = new AjaxStore({
   headers : {
       Authorization : 'auth-contents-goes-here'
   }
});
```

[fetchOptions](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-fetchOptions)
An object containing the Fetch options to pass to each server request issued by this store. Use this to control if credentials are sent and other options, read more at [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#supplying_request_options).

Example usage:

```
const store = new AjaxStore({
   fetchOptions : {
       credentials : 'omit',
       redirect    : 'error'
   }
});
```

[sendAsFormData](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-sendAsFormData)
Specify `true` to send payloads as form data, `false` to send as regular JSON.

[writeAllFields](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-writeAllFields)
Specify `true` to send all model fields when committing modified records (as opposed to just the modified fields)

[parentIdParamName](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-parentIdParamName)
The name of the HTTP parameter passed to this Store's [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl) to indicate the node `id` to load when loading child nodes on demand if the node being expanded was created with data containing `children: true`.

[useRestfulMethods](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-useRestfulMethods)
Set to ´true´ to use restful [httpMethods](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-httpMethods)

[httpMethods](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-httpMethods)
The HTTP methods to use for CRUD requests when [useRestfulMethods](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-useRestfulMethods) is enabled.

```
new AjaxStore({
   useRestfulMethods : true,
   httpMethods : {
       create : 'POST',
       read   : 'POST',
       update : 'PATCH',
       delete : 'DELETE'
   }
});

```

[paramsInBody](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-paramsInBody)
When this config is enabled, the [params](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#property-params) of "read" request are placed in the request body instead of the query string, if the HTTP method allows.

[createUrl](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-createUrl)
Url to post newly created records to.

The response must be in the form:

```
{
    "success": true,
    "data": [{
        "id": 0, "name": "General Motors"
    }, {
        "id": 1, "name": "Apple"
    }]
}
```

Just the array of data may be returned, however that precludes the orderly handling of errors encountered at the server.

If the server encountered an error, the packet would look like this:

```
{
    "success": false,
    "message": "Some kind of database error"
}
```

And that packet would be available in the [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) handler in the `response` property of the event.

The `success` property may be omitted, it defaults to `true`.

[readUrl](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-readUrl)
Url to read data from.

The response must be in the form:

```
{
    "success": true,
    "data": [{
        "id": 0, "name": "General Motors"
    }, {
        "id": 1, "name": "Apple"
    }]
}
```

If the store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#property-isPaged), the total dataset size must be returned in the [responseTotalProperty](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-responseTotalProperty) property:

```
{
    "success": true,
    "data": [{
        "id": 0, "name": "General Motors"
    }, {
        "id": 1, "name": "Apple"
    }],
    "total": 65535
}
```

Just the array of data may be returned, however that precludes the orderly handling of errors encountered at the server.

If the server encountered an error, the packet would look like this:

```
{
    "success": false,
    "message": "Some kind of database error"
}
```

And that packet would be available in the [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) handler in the `response` property of the event.

The `success` property may be omitted, it defaults to `true`.

[updateUrl](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-updateUrl)
Url to post record modifications to.

The response must be in the form:

```
{
    "success": true,
    "data": [{
        "id": 0, "name": "General Motors"
    }, {
        "id": 1, "name": "Apple"
    }]
}
```

Just the array of data may be returned, however that precludes the orderly handling of errors encountered at the server.

If the server encountered an error, the packet would look like this:

```
{
    "success": false,
    "message": "Some kind of database error"
}
```

And that packet would be available in the [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) handler in the `response` property of the event.

The `success` property may be omitted, it defaults to `true`.

[deleteUrl](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-deleteUrl)
Url for deleting records.

The response must be in the form:

```
{
    "success": true
}
```

If the server encountered an error, the packet would look like this:

```
{
    "success": false,
    "message": "Some kind of database error"
}
```

And that packet would be available in the [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) handler in the `response` property of the event.

The `success` property may be omitted, it defaults to `true`.

[autoLoad](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#config-autoLoad)
True to initiate a load when the store is instantiated

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAjaxStore](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-isAjaxStore)
Identifies an object as an instance of [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore) class, or subclass thereof.

[isAjaxStore](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-isAjaxStore-static)
Identifies an object as an instance of [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore) class, or subclass thereof.

[params](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-params)
An object containing key/value pairs that are passed on the request query string, or in the request body if HTTP method allows. See [paramsInBody](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-paramsInBody) config.

[lazyLoad](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-lazyLoad)
If set to `true`, or a config object, this makes the store load new records when needed. When a record that is not already loaded is requested, a request to the configured [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl) will be made.

LazyLoading is currently not supported in Calendar, Gantt, TaskBoard.

[createUrl](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-createUrl)
Url to post newly created records to.

The response must be in the form:

```
{
    "success": true,
    "data": [{
        "id": 0, "name": "General Motors"
    }, {
        "id": 1, "name": "Apple"
    }]
}
```

Just the array of data may be returned, however that precludes the orderly handling of errors encountered at the server.

If the server encountered an error, the packet would look like this:

```
{
    "success": false,
    "message": "Some kind of database error"
}
```

And that packet would be available in the [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) handler in the `response` property of the event.

The `success` property may be omitted, it defaults to `true`.

[readUrl](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-readUrl)
Url to read data from.

The response must be in the form:

```
{
    "success": true,
    "data": [{
        "id": 0, "name": "General Motors"
    }, {
        "id": 1, "name": "Apple"
    }]
}
```

If the store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#property-isPaged), the total dataset size must be returned in the [responseTotalProperty](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-responseTotalProperty) property:

```
{
    "success": true,
    "data": [{
        "id": 0, "name": "General Motors"
    }, {
        "id": 1, "name": "Apple"
    }],
    "total": 65535
}
```

Just the array of data may be returned, however that precludes the orderly handling of errors encountered at the server.

If the server encountered an error, the packet would look like this:

```
{
    "success": false,
    "message": "Some kind of database error"
}
```

And that packet would be available in the [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) handler in the `response` property of the event.

The `success` property may be omitted, it defaults to `true`.

[updateUrl](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-updateUrl)
Url to post record modifications to.

The response must be in the form:

```
{
    "success": true,
    "data": [{
        "id": 0, "name": "General Motors"
    }, {
        "id": 1, "name": "Apple"
    }]
}
```

Just the array of data may be returned, however that precludes the orderly handling of errors encountered at the server.

If the server encountered an error, the packet would look like this:

```
{
    "success": false,
    "message": "Some kind of database error"
}
```

And that packet would be available in the [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) handler in the `response` property of the event.

The `success` property may be omitted, it defaults to `true`.

[deleteUrl](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-deleteUrl)
Url for deleting records.

The response must be in the form:

```
{
    "success": true
}
```

If the server encountered an error, the packet would look like this:

```
{
    "success": false,
    "message": "Some kind of database error"
}
```

And that packet would be available in the [exception](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-exception) handler in the `response` property of the event.

The `success` property may be omitted, it defaults to `true`.

[isLoading](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-isLoading)
Returns a truthy value if the Store is currently loading.

A load operation is initiated by a load call, but the network request is not sent until after a delay until the next event loop because of allowing all operations which may request a load to coalesce into one call.

If the loading request is in this waiting state, the value will be `1`,

If the network request is in flight, the value will be `2`

[isCommitting](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#property-isCommitting)
Returns true if the Store is currently committing

## Functions

Functions are methods available for calling on the class

[performRemoteSort](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-performRemoteSort)
Internal sort method. Should not be used in application code directly.

[performRemoteFilter](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-performRemoteFilter)
Internal filter method. Should not be used in application code directly.

[encodeFilterParams](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-encodeFilterParams)
A provided function which creates an array of values for the [filterParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-filterParamName) to pass any filters to the server upon load.

By default, this creates a JSON string containing the following properties:

```
   [{
       field         : <theFieldName>
       operator      : May be: `'='`, `'!='`, `'>'`, `'>='`, `'<'`, `'<='`, `'*'`, `'startsWith'`, `'endsWith'`
       value         : The value to compare
       caseSensitive : true for case sensitive comparisons
   }]
```

[encodeSorterParams](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-encodeSorterParams)
A provided function which creates an array of values for the {#config-sortParamName} to pass any sorters to the server upon load.

By default, this creates a JSON string containing the following properties:

```
   [{
       field     : <theFieldName>
       ascending : true/false
   }]
```

[internalLoad](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-internalLoad)
Internal data loading method.

[load](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-load)
Load data from the [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl). If configured as [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-lazyLoad), this will load 1 chunk of records starting from index 0. If the store has previously been loaded, it will first be cleared of all records and all lazy load cache.

[loadChildren](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-loadChildren)
Loads children into specified parent record. Parent records id is sent as a param (param name configured with [parentIdParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-parentIdParamName).

[loadPage](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-loadPage)
Loads a page of data from the [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl).

[commit](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-commit)
Commits all changes (added, modified and removed) using corresponding urls ([createUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-createUrl), [updateUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-updateUrl) and [deleteUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-deleteUrl))

[queueCommit](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-queueCommit)
Internally used to handle the commit queue

[performCommit](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-performCommit)
Internally used to perform the actual commit without any queue handling or timeout

[commitAdded](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-commitAdded)
Commits added records by posting to [createUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-createUrl). Server should return a JSON object with a 'success' property indicating whether the operation was successful.

[commitModified](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-commitModified)
Commits modified records by posting to [updateUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-updateUrl). Server should return a JSON object with a 'success' property indicating whether the operation was successful.

[commitRemoved](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#function-commitRemoved)
Commits removed records by posting to [deleteUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-deleteUrl). Server should return a JSON object with a 'success' property indicating whether the operation was successful.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[exception](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-exception)
Fired when a remote request fails, either at the network level, or the server returns a failure, or an invalid response.

Note that when a [commit](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#function-commit) fails, more than one exception event will be triggered. The individual operation, `create`, `update` or `delete` will trigger their own `exception` event, but the encapsulating commit operation will also trigger an `exception` event when all the operations have finished, so if exceptions are going to be handled gracefully, the event's `action` property must be examined, and the constituent operations of the event must be examined.

[commitAdded](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-commitAdded)
Fired after committing added records

[commitModified](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-commitModified)
Fired after committing modified records

[load](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-load)
Fired on successful load

[loadChildren](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-loadChildren)
Fired on successful load of remote child nodes for a tree node.

[commitRemoved](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-commitRemoved)
Fired after committing removed records

[beforeLoad](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-beforeLoad)
Fired before loading starts. Allows altering parameters and is cancelable by returning `false`. For paged stores, instead listen to [beforeLoadPage](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-beforeLoadPage). For remote loading of tree child nodes, listen to [beforeLoadChildren](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#event-beforeLoadChildren).

[beforeLoadChildren](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-beforeLoadChildren)
Fired before loading of remote child nodes of a tree node starts. Allows altering parameters and is cancelable

[loadPageStart](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-loadPageStart)
When the store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#property-isPaged), this is fired when a page load is beginning.

[loadStart](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-loadStart)
Fired when loading is beginning. This is not cancelable. Parameters in the event may still be mutated at this stage.

[loadChildrenStart](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#event-loadChildrenStart)
Fired when loading of remote child nodes into a tree node is beginning. This is not cancelable. Parameters in the event may still be mutated at this stage.

## Typedefs

Typedefs are type definitions for the class

[HttpMethods](https://bryntum.com/docs/gantt/api/Core/data/AjaxStore#typedef-HttpMethods)
Http methods used by the AjaxStore in restful mode.
