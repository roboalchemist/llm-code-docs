# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreProxy.md

# [StoreProxy](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreProxy)

Object-like interaction with a Store by using a Proxy. To enable, configure the store with `objectify : true`.

```
const store = new Store({
   objectify : true,
   data      : [
       { id : 'batman', name : 'Bruce' }
   ]
});
```

Access records using their ids as Store properties:

```
console.log(store.batman.name); // logs Bruce
```

Add records by assigning properties to the Store:

```
store.superman = { name : 'Clark' }; // Id will be 'superman'
```

Remove records by removing their property:

```
delete store.batman;
```

Check if a certain id existing in the store by using `in`:

```
console.log('superman' in store): // logs true
```

Please note that this approach:

* Will affect performance slightly, not recommended for larger datasets.
* Uses native Proxy.
* Preserves predefined Store properties, records cannot use ids that match those.
* Might have other limitations preventing the use of it in some scenarios where a normal Store can be used.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[objectify](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreProxy#config-objectify)
Allow object like interaction with the Store. For example:

```
const store = new Store({
   objectify : true,
   data      : [
       { id : 'batman', name : 'Bruce' }
   ]
});

// retrieve using id as property
const record = store.batman;

// add as property
store.superman = { name : 'Clark' };

// delete to remove
delete store.batman;
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreProxy](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreProxy#property-isStoreProxy)
Identifies an object as an instance of [StoreProxy](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreProxy) class, or subclass thereof.

[isStoreProxy](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreProxy#property-isStoreProxy-static)
Identifies an object as an instance of [StoreProxy](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreProxy) class, or subclass thereof.
