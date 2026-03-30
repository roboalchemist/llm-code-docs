# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreCRUD.md

# [StoreCRUD](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD)

Mixin for Store that handles modifying records (add, remove etc).

```
// add new record to store
store.add({ id: 1, team: 'FC Krasnodar' });

// remove a record from store, using id
store.remove(1);
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoCommit](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#config-autoCommit)
Commit changes automatically

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreCRUD](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#property-isStoreCRUD)
Identifies an object as an instance of [StoreCRUD](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD) class, or subclass thereof.

[isStoreCRUD](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#property-isStoreCRUD-static)
Identifies an object as an instance of [StoreCRUD](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD) class, or subclass thereof.

[changes](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#property-changes)
Get uncommitted changes as an object of added/modified/removed arrays of records.

```
// Format:
{
     added: [], // array of Core.data.Model
     modified: [], // array of Core.data.Model
     removed: [] // array of Core.data.Model
}
```

[hasChanges](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#property-hasChanges)
Boolean flag, indicating whether the store has any data changes (its [changes](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#property-changes) accessor returns a non-empty object). Cheaper than [changes](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#property-changes) accessor itself, because it does not clone some internal data structures.

[autoCommit](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#property-autoCommit)
Setting `autoCommit` to `true` automatically commits changes to records.

## Functions

Functions are methods available for calling on the class

[remove](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-remove)
Removes a record from this store. Fires a single [remove](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#event-remove) event passing the removed records.

[clear](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-clear)
Clears store data. Used by removeAll, separate function for using with chained stores.

[removeAll](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-removeAll)
Removes all records from the store.

If called on a lazy-loaded store, it removes all the loaded records. And if a backend is configured, then those deletions will also be synced with the backend.

[add](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-add)
Add records to store.

[insert](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-insert)
Insert records into the store.

[move](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-move)
Moves a record, or block of records to another location.

[acceptChanges](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-acceptChanges)
Accepts all changes, resets the modification tracking:

* Clears change tracking for all records
* Clears added
* Clears modified
* Clears removed Leaves the store in an "unmodified" state.

[commit](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-commit)
Commits changes, per default only returns changes and resets tracking.

[revertChanges](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-revertChanges)
Reverts all changes in the store (adds removed records back, and removes newly added records).

[suspendAutoCommit](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-suspendAutoCommit)
Suspends automatic commits upon store changes. Can be called multiple times (it uses an internal counter).

[resumeAutoCommit](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#function-resumeAutoCommit)
Resumes automatic commits upon store changes. Will trigger commit if the internal counter is 0.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[removeAll](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-removeAll)
Fired after removing all records

[beforeCommit](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-beforeCommit)
Fired before committing changes. Return false from handler to abort commit

[commit](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-commit)
Fired after committing changes

[beforeRemove](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-beforeRemove)
Fired before records are removed from this store by the [remove](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#function-remove) or [removeAll](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#function-removeAll). Also fired when removing a child record in a tree store using [removeChild](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#function-removeChild). The remove may be vetoed by returning `false` from a handler.

[beforeAdd](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-beforeAdd)
Fired before records are added to this store by the [add](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#function-add) or [insert](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreCRUD#function-insert). In a tree store, also fired by [appendChild](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#function-appendChild) and [insertChild](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#function-insertChild). The add or insert may be vetoed by returning `false` from a handler.

[add](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-add)
Fired after adding/inserting record(s). If the record was added to a parent, the `isChild` flag is set on the event. If it was inserted, event contains `index`

[remove](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-remove)
Fired when one or more records are removed

[change](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-change)
Fired when Data in the store was changed. See [change](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-change) event for the details.

[refresh](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreCRUD#event-refresh)
Data in the store has completely changed, such as by a filter, or sort or load operation.
