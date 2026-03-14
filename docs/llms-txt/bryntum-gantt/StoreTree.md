# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreTree.md

# [StoreTree](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree)

Mixin for store with tree related functionality. To learn more about working with tree nodes please see the [TreeNode](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode) class and [this guide](https://bryntum.com/docs/gantt/api/#Core/guides/data/treedata.md).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[transformFlatData](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#config-transformFlatData)
Set to `true` to on load transform a flat dataset with raw objects containing `parentId` into the format expected for tree data.

Example input format:

```
[
  { id : 1, name : 'Parent' },
  { id : 2, name : 'Child', parentId : 1 }
]
```

Will be transformed into:

```
[
  {
    id       : 1,
    name     : 'Parent',
    children : [
      { id : 2, name : 'Child', parentId : 1 }
    ]
  }
]
```

[fireRemoveEventForMoveAction](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#config-fireRemoveEventForMoveAction)
Set to `true` to fire a 'remove' event when moving a node (to mimic the behavior of versions < 6.0).

[keepExpandedOnLoad](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#config-keepExpandedOnLoad)
When set to `true`, restores the expanded states of tree nodes when reloading data.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreTree](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#property-isStoreTree)
Identifies an object as an instance of [StoreTree](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreTree) class, or subclass thereof.

[isStoreTree](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#property-isStoreTree-static)
Identifies an object as an instance of [StoreTree](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreTree) class, or subclass thereof.

[StopBranch](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#property-StopBranch-static)
A special `Symbol` signalizing treeify method that the current record grouping should be stopped.

```
const newRoot = workerStore.treeify([
    // group workers by company
    worker => {
        // if the worker is unemployed we don't put it in a group
        // we just show such record on the root level
        if (!worker.company) {
            return Store.StopBranch
        }

        return worker.company;
    }
]);
```

[isTree](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#property-isTree)
`true` if this Store is configured to handle tree data (with `tree : true`) or if this is a [chained store](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-chain) and the master store is a tree store.

[leaves](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#property-leaves)
Returns all leaf records in a tree store

## Functions

Functions are methods available for calling on the class

[loadChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-loadChildren)
Loads children for a parent node that uses load on demand (when expanding it). Base implementation does nothing, either use AjaxStore which implements it, create your own subclass with an implementation or listen for `toggleNode` and insert records when you have them available.

[onNodeAddChild](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-onNodeAddChild)
Called from Model when adding children. Not to be called directly, use Model#appendChild() instead.

[getChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-getChildren)
Returns the children of the passed branch node which this store owns. By default, this is the entire `children` array.

**If this store [isChained](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#property-isChained)**, then this returns only the subset of children which are filtered into this store by the [chainedFilterFn](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#config-chainedFilterFn).

[internalToggleTreeSubRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-internalToggleTreeSubRecords)
Includes or excludes all records beneath parentRecord in storage. Used when expanding or collapsing nodes.

[toggleCollapse](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-toggleCollapse)
Collapse an expanded record or expand a collapsed. Optionally forcing a certain state.

[onNodeCollapse](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-onNodeCollapse)
Remove all records beneath parentRecord from storage.

[onNodeExpand](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-onNodeExpand)
Add all records beneath parentRecord from storage.

[transformToTree](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-transformToTree)
Transforms flat data containing parent ids into tree data

[treeifyData](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-treeifyData)
Transforms passed data into a tree with parent levels based on supplied fields.

```
const newRoot = store.treeify(
    [
        { name : "Julia", age : 21 },
        { name : "Macie", age : 12 },
        { name : "Julia", age : 18 },
        { name : "Olivia", age : 8 },
    ],
    ['name', r => r.age % 10]
);
```

Generated parent records are indicated with `generatedParent` and `key` properties. The first one is set to `true` and the latter one has a value for the group the parent represents.

[treeify](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-treeify)
Transforms this store data into a tree with parent levels based on supplied fields.

```
const newRoot = store.treeify(['name', r => r.age % 10]);
```

Generated parent records are indicated with `generatedParent` and `key` properties. The first one is set to `true` and the latter one has a value for the group the parent represents.

[indent](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-indent)
Increase the indentation level of one or more nodes in the tree

[outdent](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#function-outdent)
Decrease the indentation level of one or more nodes in the tree

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeIndent](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#event-beforeIndent)
Fired before nodes in the tree are indented. Return `false` from a listener to prevent the indent.

[indent](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#event-indent)
Fired after tasks in the tree are indented

[beforeOutdent](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#event-beforeOutdent)
Fired before nodes in the tree are outdented. Return `false` from a listener to prevent the outdent.

[outdent](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreTree#event-outdent)
Fired after tasks in the tree are outdented
