# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/Store.md

# [Store](https://bryntum.com/docs/gantt/api/Core/data/Store)

The Store represents a data container which holds flat data or tree structures. An item in the Store is often called a ´record´ and it is simply an instance of the [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) (or any subclass thereof).

Typically, you load data into a store to display it in a Grid or a ComboBox. The Store is the backing data component for any component that is showing data in a list style UI.

The Store offers an API to edit, filter, group and sort the records.

Data is stored in a JSON array

Store with flat data
--------------------

To create a flat store simply provide an array of JavaScript or JSON objects that describe your records

```
const store = new Store({
    data : [
        { id : 1, name : 'ABBA', country : 'Sweden' },
        { id : 2, name : 'Beatles', country : 'UK' }
    ]
});

// retrieve record by id
const beatles = store.getById(2);
```

By default, when using inline data (supplied directly to the store by the app, not loaded remotely by an `AjaxStore` or `CrudManager`) the incoming data objects are cloned by the created records. This means that those objects will not get "polluted" when default values are applied, or when records are manipulated later. But cloning reduces record creation performance a bit, if the raw data objects are not directly used elsewhere you can opt out of cloning by setting the [useRawData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-useRawData) config to `true`.

Note that if the first object in the incoming data is un-extensible (~immutable), the entire incoming dataset will be cloned even if configured with `useRawData: true`.

Store with tree data
--------------------

To create a tree store use `children` property for descendant records

```
const store = new Store({
    tree: true,
    data : [
        { id : 1, name : 'ABBA', country : 'Sweden', children: [
            { id: 2, name: 'Agnetha' },
            { id: 3, name: 'Bjorn' },
            { id: 4, name: 'Benny' },
            { id: 5, name: 'Anni-Frid' }
        ]},
    ]
});

// retrieve record by id
let benny = store.getById(4);
```

Optionally a tree store can consume a flat dataset with nodes that have a `parentId` property. By configuring the store with `tree : true` and `transformFlatData : true`, the flat data is transformed into tree data:

```
const store = new Store({
    tree              : true,
    transformFlatData : true,
    data              : [
        { id : 1, name : 'ABBA', country : 'Sweden' },
        { id : 2, name : 'Agnetha', parentId : 1 },
        { id : 3, name : 'Bjorn', parentId : 1 },
        { id : 4, name : 'Benny', parentId : 1 },
        { id : 5, name : 'Anni-Frid', parentId : 1 }
    ]
});
```

### Retrieving and consuming JSON

For both flat stores or tree stores it is possible to retrieve the data of all records in JSON format:

```
const jsonString = store.json;

// or

const jsonArray = store.toJSON();
```

To plug the JSON data back in later:

```
store.data = JSON.parse(jsonString);

// or

store.data = jsonArray;
```

Lazy loading
------------

A store can be configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad) set to `true`. This will make the store request records when they are needed, rather than the complete dataset at once. The request is intercepted by implementing the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function. Each request will be made up of 1 chunk before and after the requested index (which gives a total of 2 chunks). The chunk size can be configured in the [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad) config.

There is a [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md) for implementing lazy loading in Grid.

Paging
------

A Store can be paged remotely by setting the [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remotePaging) config to `true`. For a non-[AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be requested by the Store by calling the implemented [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function. Data can also be provided by listening to the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-requestData) event, and updating the [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) property with new data.

```
const store = new Store({
   remotePaging : true,
   requestData({ page, pageSize }){
      const start = (page - 1) * pageSize;
      const data = allRecords.splice(start, start + pageSize);

      return {
         data,
         total : allRecords.length
      }
   }
})
```

Remote sorting
--------------

A Store can be sorted remotely by setting the [remoteSort](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteSort) config to `true`. This makes it possible to use the built-in sorting features of the Store and corresponding UI functionality, without using local data. For a non-[AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be requested by the Store by calling a by the app implemented [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function. Data can also be provided by listening to the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-requestData) event, and updating the [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) property with new data.

```
const store = new Store({
   remoteSort   : true,
   remotePaging : true,
   requestData({ sorters, page, pageSize }){
      const sortedRecords = [...allRecords];
      sorters?.forEach(sorter => sortedRecords.sort((a,b) => {
         const { field, ascending } = sorter;

         if (!ascending) {
             ([b, a] = [a, b]);
         }

         return a[field] > b[field] ? 1 : (a[field] < b[field] ? -1 : 0)
      });

      const start = (page - 1) * pageSize;
      const data = sortedRecords.splice(start, start + pageSize);

      return {
         data,
         total : allRecords.length
      }
   }
})
```

For [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be loaded via the configured [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl).

Remote filtering
----------------

A Store can be filtered remotely by setting the [remoteFilter](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter) config to `true`. This makes it possible to use the built-in filtering features of the Store and corresponding UI functionality, without using local data.

For a non-[AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be requested by the Store by calling the implemented [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function. Data can also be provided by listening to the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-requestData) event, and updating the [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) property with new data.

```
const store = new Store({
   remoteFilter : true,
   remoteSort   : true,
   remotePaging : true,
   requestData({ filters, sorters, page, pageSize }){
      let filteredRecords = [...allRecords];

      filters?.forEach(filter => {
         const { field, operator, value, caseSensitive } = filter;

         if(operator === '='){
             filteredRecords = filteredRecords.filter(r => r[field] === value);
         }
         else {
             /// ... implement other filter operators
         }
      });

      sorters?.forEach(sorter => filteredRecords.sort((a,b) => {
         const { field, ascending } = sorter;

         if (!ascending) {
             ([b, a] = [a, b]);
         }

         return a[field] > b[field] ? 1 : (a[field] < b[field] ? -1 : 0)
      }));

      const start = (page - 1) * pageSize;
      const data = filteredRecords.splice(start, start + pageSize);

      return {
         data,
         total : filteredRecords.length
      }
   }
})
```

For [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be loaded via the configured [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl).

Getting record count
--------------------

To get the number of "visible" records in the store (records that would be shown when using the Store as the data source for a Grid or similar), use the [count](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-count) property. This will return the number of records in the store after filtering and grouping has been applied, including the generated group headers and footers but excluding any records inside collapsed parents or group headers:

```
const visibleRecords = store.count;
```

To get other counts, such as the total number of data records in the store including those collapsed away and filtered out, use the more flexible [getCount](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-getCount) method:

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

Sharing stores
--------------

You cannot directly share a Store between widgets, but the data in a Store can be shared. There are two different approaches depending on your needs, sharing data and chaining stores:

### Shared data

To create 2 widgets that share data, you can create 2 separate stores and pass records of the first store as the dataset of the second store.

```
let combo1 = new Combo({
    appendTo : document.body,
    store    : new Store({
        data : [
            { id : 1, name : 'ABBA', country : 'Sweden' },
            { id : 2, name : 'Beatles', country : 'UK' }
        ]
    }),
    valueField   : 'id',
    displayField : 'name'
});

let combo2 = new Combo({
    appendTo : document.body,
    store    : new Store({
        data : combo1.store.records
    }),
    valueField   : 'id',
    displayField : 'name'
});

combo1.store.first.name = 'foo';
combo2.store.first.name; // "foo"
```

### Chained stores

Another more powerful option to share data between widgets is to create [chained](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained) stores. The easiest way to create a chained store is to call [chain](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-chain) function.

```
let combo1 = new Combo({
    appendTo : document.body,
    store    : new Store({
        data : [
            { id : 1, name : 'ABBA', country : 'Sweden' },
            { id : 2, name : 'Beatles', country : 'UK' }
        ]
    }),
    valueField   : 'id',
    displayField : 'name'
});

let combo2 = new Combo({
    appendTo     : document.body,
    store        : combo1.store.chain(),
    valueField   : 'id',
    displayField : 'name'
});

combo1.store.first.name = 'foo';
combo2.store.first.name; // "foo"
```

A chained store can optionally be created with a filtering function, to only contain a subset of the records from the main store. In addition, the chained store will reflect record removals/additions to the master store, something the shared data approach will not.

Non-homogeneous data structures
-------------------------------

You can use different Model classes to represent the records in the store by overriding the [createRecord](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-createRecord) method:

```
const store = new Store ({
    modelClass : Gate,
    readUrl    : 'data/the-airport.json',
    autoLoad   : true,
    // The default model is a Gate (see above) and in this createRecord method, we can decide at runtime based
    // on the data which model class to use. This is useful when your record types aren't homogenous.
    createRecord(data) {
        let modelClass = this.modelClass;
        if (data.type === 'terminal') {
            modelClass = Terminal;
        }
        return new modelClass(data, this);
    }
},
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[id](https://bryntum.com/docs/gantt/api/Core/data/Store#config-id)
Store's unique identifier. When set the store is added to a store map accessible through `Store.getStore(id)`.

[modelClass](https://bryntum.com/docs/gantt/api/Core/data/Store#config-modelClass)
Class used to represent records in the store, should be a subclass of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model). Only applies when supplying data to the store (load, add), any supplied record instances are kept as is.

```
class MyModel extends Model {
    static get fields() {
        return [
            'name',
            'city',
            'company'
        ]
    }
}

const store = new Store({
    modelClass : MyModel,
    data : [
        { id : 1, name : 'Mark', city : 'London', company : 'Cool inc' },
        ...
    ]
});
```

[verifyNoGeneratedIds](https://bryntum.com/docs/gantt/api/Core/data/Store#config-verifyNoGeneratedIds)
Verify that loaded data does not contain any generated ids. If it does, a warning is logged on console.

Set this to `false` to disable the check and give a very minor performance boost.

[lazyLoad](https://bryntum.com/docs/gantt/api/Core/data/Store#config-lazyLoad)
If set to `true`, or a config object, this makes the store load new records when needed. When a record that is not already loaded is requested, the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function is called. Please read the [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md) to learn more on how to configure lazy loading.

LazyLoading is currently not supported in Calendar, Gantt, TaskBoard.

[autoLoad](https://bryntum.com/docs/gantt/api/Core/data/Store#config-autoLoad)
For a non-AjaxStore, the autoLoad config will only take effect if the store is configured as [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), [remoteSort](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteSort), [remoteFilter](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter) or [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remotePaging). In these cases, it will immediately after creation, perform a request by calling the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function.

[requestData](https://bryntum.com/docs/gantt/api/Core/data/Store#config-requestData)
In a non-[AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), [remoteSort](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteSort), [remoteFilter](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter) or [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remotePaging), the function provided here is called when the Store needs new data, which will happen:

* for [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), when a record that has not yet been loaded is requested.
* for [remoteSort](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteSort), on a sort operation.
* for [remoteFilter](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter), on a filter operation.
* for [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remotePaging), when current page is changed.

When implementing this, it is expected that what is returned is an object with a `data` property containing the records requested. What is requested will be specified in the `params` object, which will differ depending on the source of the request.

For [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), the params object will contain `a startIndex` and a `count` param. It is expected for the implementation of this function to provide a `data` property containing the number of records specified in the `count` param starting from the specified `startIndex`.

```
class MyStore extends Store {
   async requestData({startIndex, count}){
      const response = await getData(startIndex, count);
      return {
         data : response.records,
         total : response.totalRecordCount
      }
   }
}
```

For [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remotePaging), the params object will contain a `page` and a `pageSize` param. It is expected for the implementation of this function to provide a `data` property containing the number of records specified in the `pageSize` param starting from the specified `page`.

```
class MyStore extends Store {
   requestData({page, pageSize}){
      const start = (page - 1) * pageSize;
      const data = allRecords.splice(start, start + pageSize);

      return {
         data,
         total : allRecords.length
      }
   }
}
```

For [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad) it is recommended, and for [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remotePaging) it is required, to include a `total` property which reflects the total amount of records available to load. If the `total` property is omitted (when [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad)), certain features and functions are disabled:

* The component (Grid for example) is not aware of the total number of records, which will make the scrollbar's thumb change size and position when new records are loaded.
* The store don't know when to stop requesting new records. The `total` property will be set to the index of the last record loaded after requestData returns with fewer records than requested.

If [remoteSort](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteSort) is active, the params object will contain a `sorters` param, containing a number of sorter objects.The sorter objects will look like this:

```
{
    "field": "name",
    "ascending": true
}
```

If [remoteFilter](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter) is active, the params object will contain a `filters` param, containing a number of filters objects. The filter objects will look like this:

```
{
    "field": "country",
    "operator": "=",
    "value": "sweden",
    "caseSensitive": false
}
```

The Base implementation of this function does nothing, you need to create your own subclass with an implementation.

Configuration parameter to pass a function to be used as [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) in non-AjaxStore.

[useRawData](https://bryntum.com/docs/gantt/api/Core/data/Store#config-useRawData)
Retools the loaded data objects instead of making shallow copies of them. This increases performance but pollutes the incoming data.

This setting is off by default, but is turned on automatically unless explicitly configured when data is loaded using an `AjaxStore` (configured with a `readUrl`) or a `CrudManager` (configured to load data remotely).

```
// No duplicate id checking, no type conversions
new Store({ useRawData : true });
```

Also allows disabling certain steps in data loading, to further improved performance. Either accepts an object with the params described below or `true` which enables `disableDuplicateIdCheck`.

```
new Store({
  // No type conversions only
  useRawData : {
    disableTypeConversion : true
  }
});
```

Note that if the first object in the incoming data is determined to be un-extensible (~immutable), the entire incoming dataset will be cloned.

Also note that since incoming data objects gets polluted with this setting on, reusing the same data objects elsewhere might lead to unexpected behavior.

When binding to data in frameworks with this setting enabled, the same principles as for framework state applies - an object in the incoming data must be replaced instead of mutated for a change to be detected. See for example [React's explanation here](https://bryntum.com/docs/gantt/api/https://react.dev/learn/updating-objects-in-state)

[fields](https://bryntum.com/docs/gantt/api/Core/data/Store#config-fields)
An array of field definitions used to create a [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) (modelClass) subclass. Optional. If the Model already has fields defined, these fields will extend those.

```
const store = new Store({
    fields : ['name', 'city', 'company'],
    data   : [
        { id : 1, name : 'Mark', city : 'London', company : 'Cool inc' },
        ...
    ]
});
```

See [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) for more info on defining fields, changing data source and mapping fields to nested objects.

Note that pre-created record instances supplied to the store are kept as is and thus these fields will not apply to them.

[autoTree](https://bryntum.com/docs/gantt/api/Core/data/Store#config-autoTree)
Automatically detect from set data if used as tree store or flat store. If [tree](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-tree) is explicitly set to `false`, then this value will be overruled and no tree detection performed.

[data](https://bryntum.com/docs/gantt/api/Core/data/Store#config-data)
Raw data to load initially.

Expects an array of JavaScript objects, with properties matching store's fields (defined on its [model](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) or in the [fields](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-fields) config).

```
const store = new Store({
    data : [
        { id : 1, name : 'Linda', city : 'NY' },
        { id : 2, name : 'Olivia', city : 'Paris' },
        ...
    ]
});
```

[tree](https://bryntum.com/docs/gantt/api/Core/data/Store#config-tree)
`true` to act as a tree store.

[storage](https://bryntum.com/docs/gantt/api/Core/data/Store#config-storage)
A [Collection](https://bryntum.com/docs/gantt/api/#Core/util/Collection), or Collection config object to use to contain this Store's constituent records.

[allowNoId](https://bryntum.com/docs/gantt/api/Core/data/Store#config-allowNoId)
Specify `false` to prevent loading records without ids, a good practice to enforce when syncing with a backend.

By default, Store allows loading records without ids, in which case a generated id will be assigned.

[preventSubClassingModel](https://bryntum.com/docs/gantt/api/Core/data/Store#config-preventSubClassingModel)
Prevent dynamically subclassing the modelClass. It does so by default to not pollute it when exposing properties. Should rarely need to be used.

[storeClass](https://bryntum.com/docs/gantt/api/Core/data/Store#config-storeClass)
Store class to use when creating the store when it is a part of a [CrudManager](https://bryntum.com/docs/gantt/api/https://bryntum.com/products/scheduler/docs/api/Scheduler/data/CrudManager).

```
crudManager : {
     eventStore {
         storeClass : MyEventStore
     }
}
```

[createRecord](https://bryntum.com/docs/gantt/api/Core/data/Store#config-createRecord)
Creates a model instance, used internally when data is set/added. Provide this method for your own custom conversion from data to record.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStore](https://bryntum.com/docs/gantt/api/Core/data/Store#property-isStore)
Identifies an object as an instance of [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) class, or subclass thereof.

[isStore](https://bryntum.com/docs/gantt/api/Core/data/Store#property-isStore-static)
Identifies an object as an instance of [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) class, or subclass thereof.

[id](https://bryntum.com/docs/gantt/api/Core/data/Store#property-id)
Store's unique identifier.

[verifyNoGeneratedIds](https://bryntum.com/docs/gantt/api/Core/data/Store#property-verifyNoGeneratedIds)
Verify that loaded data does not contain any generated ids. If it does, a warning is logged on console.

Set this to `false` to disable the check and give a very minor performance boost.

[lazyLoad](https://bryntum.com/docs/gantt/api/Core/data/Store#property-lazyLoad)
If set to `true`, or a config object, this makes the store load new records when needed. When a record that is not already loaded is requested, the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function is called. Please read the [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md) to learn more on how to configure lazy loading.

LazyLoading is currently not supported in Calendar, Gantt, TaskBoard.

[modelClass](https://bryntum.com/docs/gantt/api/Core/data/Store#property-modelClass)
Class used to represent records. Defaults to class Model.

[allRecords](https://bryntum.com/docs/gantt/api/Core/data/Store#property-allRecords)
Returns all locally available records from the store, ignoring any filters and including grouping headers / footers.

[stores](https://bryntum.com/docs/gantt/api/Core/data/Store#property-stores-static)
Get all registered stores

[rootNode](https://bryntum.com/docs/gantt/api/Core/data/Store#property-rootNode)
The invisible root node of this tree.

[data](https://bryntum.com/docs/gantt/api/Core/data/Store#property-data)
Sets data in the store.

Expects an array of JavaScript objects, with properties matching store's fields (defined on its [model](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) or in the [fields](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-fields) config).

Called on initialization if `data` is in the config, otherwise call it yourself after for example using fetch to get remote data:

```
store.data = [
    { id : 1, name : 'Linda', city : 'NY' },
    { id : 2, name : 'Olivia', city : 'Paris' },
    ...
];
```

Can also be used to get an array of the current raw data objects from all records in the store (ignoring filtering and grouping):

```
console.log(store.data);
// [
//     { id : 1, name : 'Linda', city : 'NY' },
//     { id : 2, name : 'Olivia', city : 'Paris' },
//     ...
// ]
```

You should not modify the objects in the array, neither the store nor the record will be aware of the changes.

[count](https://bryntum.com/docs/gantt/api/Core/data/Store#property-count)
Record count, including records added for group headers etc., excluding collapsed or filtered away records. That is, `count` is the "visible record count", if the store is used in a Grid or other component that visualize the records.

Consider the following dataset loaded into a Store:

```
[
  { id : 1, name : 'Linda', city : 'NY' },
  { id : 2, name : 'Olivia', city : 'NY' },
  { id : 3, name : 'John', city : 'Stockholm' }
]

// count === 3
```

Grouping by `city` yields the following records in the Store (pseudocode):

```
store.group('city');

[
  { name : 'Group NY', groupHeader : true, expanded : true },
  { id : 1, name : 'Linda', city : 'NY' },
  { id : 2, name : 'Olivia', city : 'NY' },
  { name : 'Group Stockholm', groupHeader : true },
  { id : 3, name : 'John', city : 'Stockholm', expanded : true }
]

// count === 5
```

Collapsing the `Stockholm` group yields the following records in the Store (pseudocode):

```
store.collapse(store.getAt(3));

[
  { name : 'Group NY', groupHeader : true, expanded : true },
  { id : 1, name : 'Linda', city : 'NY' },
  { id : 2, name : 'Olivia', city : 'NY' },
  { name : 'Group Stockholm', groupHeader : true, expanded : false }
]

// count === 4
```

Applying a filter further affects the count (pseudocode):

```
store.filter('name', 'Linda');

[
  { name : 'Group NY', groupHeader : true, expanded : true },
  { id : 1, name : 'Linda', city : 'NY' }
]

// count === 2
```

If you need a different value for `count` in your app, for example ignoring filters, or including collapsed away records, please use the more flexible [getCount](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-getCount) function instead.

If the store is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), this number is based on the total amount of records specified in the response given to the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function.

[totalCount](https://bryntum.com/docs/gantt/api/Core/data/Store#property-totalCount)
Yields the complete dataset size, ignoring filtering and grouping. If the store [is paged](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-isPaged), it returns the `total` value provided in the page load request response, or manually set.

[records](https://bryntum.com/docs/gantt/api/Core/data/Store#property-records)
Returns all locally available "visible" records. **Note:** The returned value **may not** be mutated!

[first](https://bryntum.com/docs/gantt/api/Core/data/Store#property-first)
Get the first record locally available in the store.

[last](https://bryntum.com/docs/gantt/api/Core/data/Store#property-last)
Get the last record locally available in the store.

[json](https://bryntum.com/docs/gantt/api/Core/data/Store#property-json)
Retrieve or set the data of all records as a JSON string

```
const store = new Store({
    data : [
        { id : 1, name : 'Superman' },
        { id : 2, name : 'Batman' }
    ]
});

const jsonString = store.json;

//jsonString:
'[{"id":1,"name":"Superman"},{"id":2,"name":"Batman"}]
```

[formattedJSON](https://bryntum.com/docs/gantt/api/Core/data/Store#property-formattedJSON)
Pretty printed version of [json](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-json)

## Functions

Functions are methods available for calling on the class

[from](https://bryntum.com/docs/gantt/api/Core/data/Store#function-from-static)
Retrieves/creates a store based on the passed config.

Type

Result

Core.data.Store

Returns supplied store as is

String

Retrieves an existing store by id

Object

Creates a new store using supplied config object

Object\[\]

Creates a new store, populated with records created from supplied data

Core.data.Model\[\]

Creates a new store, populated with supplied records

[beginBatch](https://bryntum.com/docs/gantt/api/Core/data/Store#function-beginBatch)
Stops this store from firing events until [endBatch](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-endBatch) is called. Multiple calls to `beginBatch` stack up, and will require an equal number of `endBatch` calls to resume events.

Upon call of [endBatch](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-endBatch), a [refresh](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-refresh) event is triggered to allow UIs to update themselves based upon the new state of the store.

This is extremely useful when making a large number of changes to a store. It is important not to trigger too many UI updates for performance reasons. Batching the changes ensures that UIs attached to this store are only updated once at the end of the updates.

[endBatch](https://bryntum.com/docs/gantt/api/Core/data/Store#function-endBatch)
Ends event suspension started by [beginBatch](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-beginBatch). Multiple calls to [beginBatch](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-beginBatch) stack up, and will require an equal number of `endBatch` calls to resume events.

Upon call of `endBatch`, a [refresh](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-refresh) event with `action: batch` is triggered to allow UIs to update themselves based upon the new state of the store.

This is extremely useful when making a large number of changes to a store. It is important not to trigger too many UI updates for performance reasons. Batching the changes ensures that UIs attached to this store are only updated once at the end of the updates.

[onIsCreatingToggle](https://bryntum.com/docs/gantt/api/Core/data/Store#function-onIsCreatingToggle)
Called by owned record when the record has its [isCreating](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-isCreating) property toggled.

[onDataChange](https://bryntum.com/docs/gantt/api/Core/data/Store#function-onDataChange)
Responds to mutations of the underlying storage Collection

[onModelChange](https://bryntum.com/docs/gantt/api/Core/data/Store#function-onModelChange)
This is called from Model after mutating any fields so that Stores can take any actions necessary at that point, and distribute mutation event information through events.

[getStore](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getStore-static)
Creates a new Store instance, or retrieves an existing one.

A Store config object may contain a `type` property to identify a specific Store subclass to create. If `type` is not specified, a base Store instance will be created.

Get a store by passing in the `id` of an existing store:

```
// Get a store by id
const store = Store.getStore('myStoreId');
```

Create a store from an array of data objects:

```
const store = Store.getStore([
    { id : 1, name : 'Linda', city : 'NY' },
    { id : 2, name : 'Olivia', city : 'Paris' },
    ...
]);
```

Create a store from a config object using a `type` property to identify a specific Store subclass to create:

```
const store = Store.getStore({
    type       : 'tree',
    modelClass : MyModel,
    data       : [
        { id : 1, name : 'Linda', city : 'NY' },
        { id : 2, name : 'Olivia', city : 'Paris' },
        ...
    ]
});
```

[getRange](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getRange)
Creates an array of records from this store from the `start` to the `end` - 1

[createRecord](https://bryntum.com/docs/gantt/api/Core/data/Store#function-createRecord)
Creates a model instance, used internally when data is set/added. Override this in a subclass to do your own custom conversion from data to record.

[getCount](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getCount)
Counts the number of records in the store. Allows passing an options object to control which records are counted. For example:

```
store.getCount({ filteredOut : true });
store.getCount({ headersFooters : true, collapsed : true });
```

Consider the following dataset loaded into a Store:

```
[
  { id : 1, name : 'Linda', city : 'NY' },
  { id : 2, name : 'Olivia', city : 'NY' },
  { id : 3, name : 'John', city : 'Stockholm' }
]
```

No grouping or filtering is applied, thus all records are accessible ("visible"). Passing the different options below would yield the following results:

Option

Count

Description

`filteredOut`

0

No records are filtered out

`headersFooters`

0

No group headers have been generated

`collapsed`

0

No groups are collapsed

`visibleData`

3

All data records are "visible"

`all`

3

All options combined

Grouping by `city` yields the following records in the Store (pseudocode):

```
store.group('city');

[
  { name : 'Group NY', groupHeader : true, expanded : true },
  { id : 1, name : 'Linda', city : 'NY' },
  { id : 2, name : 'Olivia', city : 'NY' },
  { name : 'Group Stockholm', groupHeader : true },
  { id : 3, name : 'John', city : 'Stockholm', expanded : true }
]
```

Passing the different options below would yield the following results:

Option

Count

Description

`filteredOut`

0

No records are filtered out

`headersFooters`

2

Group headers have been generated

`collapsed`

0

No groups are collapsed

`visibleData`

3

All data records are "visible"

`all`

5

All options combined

Collapsing the `Stockholm` group yields the following records in the Store (pseudocode):

```
store.collapse(store.getAt(3));

[
  { name : 'Group NY', groupHeader : true, expanded : true },
  { id : 1, name : 'Linda', city : 'NY' },
  { id : 2, name : 'Olivia', city : 'NY' },
  { name : 'Group Stockholm', groupHeader : true, expanded : false }
]
```

Passing the different options below would yield the following results:

Option

Count

Description

`filteredOut`

0

No records are filtered out

`headersFooters`

2

Group headers have been generated

`collapsed`

1

A group with one record is collapsed

`visibleData`

2

Not all data records are "visible"

`all`

5

All options combined

Applying a filter further affects the counts (pseudocode):

```
store.filter('name', 'Linda');

[
  { name : 'Group NY', groupHeader : true, expanded : true },
  { id : 1, name : 'Linda', city : 'NY' }
]
```

Passing the different options below would yield the following results:

Option

Count

Description

`filteredOut`

2

Records are filtered out

`headersFooters`

2

Group headers have been generated\*

`collapsed`

1

A group with one record is collapsed

`visibleData`

1

Not all data records are "visible"

`all`

5

All options combined

\* Note that also passing `filteredOut` would include filtered out group headers in the count.

[getAt](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getAt)
Get the record at the specified index.

[getById](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getById)
Get a locally available record by id. Find the record even if filtered out, part of collapsed group or collapsed node

[isAvailable](https://bryntum.com/docs/gantt/api/Core/data/Store#function-isAvailable)
Checks if a record is available, in the sense that it is not filtered out, hidden in a collapsed group or in a collapsed parent node of a tree store.

[getByInternalId](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getByInternalId)
Get a record by internalId.

[includes](https://bryntum.com/docs/gantt/api/Core/data/Store#function-includes)
Checks if the specified record is contained in the store

[indexOf](https://bryntum.com/docs/gantt/api/Core/data/Store#function-indexOf)
Returns the index of the specified record/id, or `-1` if not found.

[getDistinctValues](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getDistinctValues)
Returns an array of distinct values from all locally available records for the specified field.

```
store.getDistinctValues('age'); // Returns an array of the unique age values
```

[getValueCount](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getValueCount)
Counts how many times the specified value appears locally in the store

[toJSON](https://bryntum.com/docs/gantt/api/Core/data/Store#function-toJSON)
Retrieve the data of all (unfiltered) records as an array of JSON objects.

```
const store = new Store({
    data : [
        { id : 1, name : 'Superman' },
        { id : 2, name : 'Batman' }
    ]
});

const jsonArray = store.toJSON();

//jsonArray:
[{id:1,name:"Superman"},{id:2,name:"Batman"}]
```

[forEach](https://bryntum.com/docs/gantt/api/Core/data/Store#function-forEach)
Iterates over all available records in store. Omits group header and footer records if this store is grouped. Does _not_ request new records when store is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad).

[map](https://bryntum.com/docs/gantt/api/Core/data/Store#function-map)
Equivalent to Array.map(). Creates a new array with the results of calling a provided function on every record

[flatMap](https://bryntum.com/docs/gantt/api/Core/data/Store#function-flatMap)
Equivalent to [Array.flatMap()](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap). Creates a new array by spreading the results of calling a provided function on every record

[every](https://bryntum.com/docs/gantt/api/Core/data/Store#function-every)
Equivalent to Array.every(). Returns `true` if every call of the provided function on each record yields a truthy value.

[reduce](https://bryntum.com/docs/gantt/api/Core/data/Store#function-reduce)
Equivalent to Array.reduce(). Applies a function against an accumulator and each record (from left to right) to reduce it to a single value.

[traverse](https://bryntum.com/docs/gantt/api/Core/data/Store#function-traverse)
Traverse all tree nodes (only applicable for Tree Store)

[traverseWhile](https://bryntum.com/docs/gantt/api/Core/data/Store#function-traverseWhile)
Traverse all tree nodes while the passed `fn` returns true

[getNext](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getNext)
Finds the next record locally available.

[getPrev](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getPrev)
Finds the previous record locally available.

[getAdjacent](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getAdjacent)
Gets the next or the previous record locally available. Optionally wraps from first -> last and vice versa

[getNextLeaf](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getNextLeaf)
Finds the next record among leaves (in a tree structure)

[getPrevLeaf](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getPrevLeaf)
Finds the previous record among leaves (in a tree structure)

[getAdjacentLeaf](https://bryntum.com/docs/gantt/api/Core/data/Store#function-getAdjacentLeaf)
Gets the next or the previous record among leaves (in a tree structure). Optionally wraps from first -> last and vice versa

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[formulaError](https://bryntum.com/docs/gantt/api/Core/data/Store#event-formulaError)
Fired when a formula defined on a datafield fails to evaluate.

[idChange](https://bryntum.com/docs/gantt/api/Core/data/Store#event-idChange)
Fired when the id of a record has changed

[beforeUpdate](https://bryntum.com/docs/gantt/api/Core/data/Store#event-beforeUpdate)
Fired before record is modified in this store. Modification may be vetoed by returning `false` from a handler.

[update](https://bryntum.com/docs/gantt/api/Core/data/Store#event-update)
Fired when a record is modified

[batchedUpdate](https://bryntum.com/docs/gantt/api/Core/data/Store#event-batchedUpdate)
Fired when one of this Store's constituent records is modified while in [batched](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-beginBatch) state. This may be used to keep UIs up to date while "tentative" changes are made to a record which must not be synced with a server.

[rootChange](https://bryntum.com/docs/gantt/api/Core/data/Store#event-rootChange)
Fired when the root node is set

[change](https://bryntum.com/docs/gantt/api/Core/data/Store#event-change)
Data in the store was changed. This is a catch-all event which is fired for all changes which take place to the store's data.

This includes mutation of individual records, adding and removal of records, as well as setting a new data payload using the [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-data) property, sorting, filtering, and calling [removeAll](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#function-removeAll).

Simple databound widgets may use to the `change` event to refresh their UI without having to add multiple listeners to the [update](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-update), [add](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#event-add), [remove](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#event-remove), [refresh](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-refresh) and [removeAll](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#event-removeAll) events.

A more complex databound widget such as a grid may use the more granular events to perform less destructive updates more appropriate to each type of change. The properties will depend upon the value of the `action` property.

[refresh](https://bryntum.com/docs/gantt/api/Core/data/Store#event-refresh)
Data in the store has completely changed, such as by a filter, or sort or load operation.

[beginDataUpdate](https://bryntum.com/docs/gantt/api/Core/data/Store#event-beginDataUpdate)
Fired when the store is about to perform an expensive batch data operation.

This event is intended to let listeners suspend expensive processing (such as UI refreshes) until the corresponding [endDataUpdate](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-endDataUpdate) event is fired.

[endDataUpdate](https://bryntum.com/docs/gantt/api/Core/data/Store#event-endDataUpdate)
Fired after a store has finished an expensive batch data operation.

Intended to pair with [beginDataUpdate](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-beginDataUpdate) so listeners can resume processing and perform a single refresh after the batch completes.

[beforeRequest](https://bryntum.com/docs/gantt/api/Core/data/Store#event-beforeRequest)
Fired before any remote request is initiated.

[afterRequest](https://bryntum.com/docs/gantt/api/Core/data/Store#event-afterRequest)
Fired after any remote request has finished whether successfully or unsuccessfully.

[addConfirmed](https://bryntum.com/docs/gantt/api/Core/data/Store#event-addConfirmed)
Fired when a temporary record with the [isCreating](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-isCreating) property set has been confirmed as a part of this store by having its [isCreating](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-isCreating) property cleared.

[move](https://bryntum.com/docs/gantt/api/Core/data/Store#event-move)
Fired when a block of records has been moved within this Store

[requestData](https://bryntum.com/docs/gantt/api/Core/data/Store#event-requestData)
This event only fires in a non-[AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), configured with [remoteSort](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteSort), [remoteFilter](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter) or [remotePaging](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remotePaging), when the Store requests more or new data.

The event will contain same params as described in the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function. This event can be listened to if you want to receive notifications about the Store's data requests, but not _directly_ want to return the requested data. For example, when you got the Store's [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) bound to a data source with the help of an external library/framegrunt docswork.

## Typedefs

Typedefs are type definitions for the class

[LazyLoadRequestParams](https://bryntum.com/docs/gantt/api/Core/data/Store#typedef-LazyLoadRequestParams)
An object containing details about the requested data

[PagingRequestParams](https://bryntum.com/docs/gantt/api/Core/data/Store#typedef-PagingRequestParams)
An object containing details about the requested data

[DataLoadRequestResponse](https://bryntum.com/docs/gantt/api/Core/data/Store#typedef-DataLoadRequestResponse)
An object containing details about the received data used for lazy and paged loading
