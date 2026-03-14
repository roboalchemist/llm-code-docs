# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/StoreDataField.md

# [StoreDataField](https://bryntum.com/docs/gantt/api/Core/data/field/StoreDataField)

This field class handles fields that accepts an array that is then converted to a store.

```
class Task extends Model {
    static fields = [
        'name',
        // Store field
        { name : 'subTasks', type : 'store', storeClass : Store }
    ];
}
```

A record can be constructed like this:

```
const task = new Task({
    name : 'Task 1',
    subTasks : [
        { text : 'Something', done : false },
        { text : 'Some other thing', done : true }
    ]
};
```

Or by populating a store:

```
const store = new Store({
    modelClass : Task,
    data : [
        {
            name : 'Task 1',
            subTasks : [
                { text : 'Something', done : false },
                { text : 'Some other thing', done : true }
            ]
        },
        ...
    ]
});
```

Whenever the store or its records are manipulated, the field will be marked as modified:

```
// These will all be detected as modifications
task.subTasks.first.done = true;
task.subTasks.last.remove();
task.subTasks.add({ text : 'New task', done : false });
```

Note that the underlying store by default will be configured with `syncDataOnLoad` set to `true`

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[storeClass](https://bryntum.com/docs/gantt/api/Core/data/field/StoreDataField#config-storeClass)
Store class to use when creating the store.

```
class TodoStore extends Store {
    ...
}

const task = new Store({
    static fields = [
        { type : 'store', name: 'todoItems', storeClass : TodoStore }
    ]
});
```

[modelClass](https://bryntum.com/docs/gantt/api/Core/data/field/StoreDataField#config-modelClass)
Model class to use for the store (can also be configured as usual on the store class, this config is for convenience).

```
class TodoItem extends Model {
  ...
}

const task = new Store({
    static fields = [
        { type : 'store', name: 'todoItems', storeClass : Store, modelClass : TodoItem }
    ]
});
```

[store](https://bryntum.com/docs/gantt/api/Core/data/field/StoreDataField#config-store)
Optional store configuration object to apply when creating the store.

```
const task = new Store({
    static fields = [
        {
            type       : 'store',
            name       : 'todoItems',
            storeClass : Store
            store      : {
                 syncDataOnLoad : false
            }
        }
    ]
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreDataField](https://bryntum.com/docs/gantt/api/Core/data/field/StoreDataField#property-isStoreDataField)
Identifies an object as an instance of [StoreDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/StoreDataField) class, or subclass thereof.

[isStoreDataField](https://bryntum.com/docs/gantt/api/Core/data/field/StoreDataField#property-isStoreDataField-static)
Identifies an object as an instance of [StoreDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/StoreDataField) class, or subclass thereof.
