# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/TreeNode.md

# [TreeNode](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode)

Mixin for Model with tree node related functionality. This class is mixed into the [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) class.

Adding and removing child nodes
-------------------------------

```
const parent = store.getById(1),

firstBorn = parent.insertChild({
    name : 'Child node'
}, parent.children[0]); // Insert a child at a specific place in the children array

parent.removeChild(parent.children[0]); // Removes a child node
parent.appendChild({ name : 'New child node' }); // Appends a child node
```

## Fields

Fields belong to a Model class and define the Model data structure

[parentId](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#field-parentId)
This is a read-only field provided in server synchronization packets to specify which record id is the parent of the record.

[parentIndex](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#field-parentIndex)
This is a read-only field provided in server synchronization packets to specify which position the node takes in the parent's children array. This index is set on load and gets updated automatically after row reordering, sorting, etc. To save the order, need to persist the field on the server and when data is fetched to be loaded, need to sort by this field.

[orderedParentIndex](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#field-orderedParentIndex)
This is a read-only field provided in server synchronization packets to specify which position the node takes in the parent's ordered children array. This index is set on load and gets updated on reordering nodes in tree. Sorting and filtering have no effect on it.

[remoteChildCount](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#field-remoteChildCount)
This field is added to the class at runtime when the Store is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad). The number specified should reflect the **total** amount of children of a parent node, including nested descendants.

[isFullyLoaded](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#field-isFullyLoaded)
This field is added to the class at runtime when the Store is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad). If set on a parent record at load time, that parent will not cause any more child load requests. If omitted, it will be automatically set to `true` when a load request receives fewer child records than requested.

To specifically set this field for a parent at its children load request, provide it as a property in the data response object:

```
return {
   data : [ ... ],
   isFullyLoaded : true
   total : 123
}
```

Or to include grandchildren for a parent, it can be provided as a property on the record data object:

```
return {
   data : [{
      id : 1,
      name : 'My Parent',
      isFullyLoaded : true,
      expanded : true,
      children : [{
         id : 2,
         name : 'My Child'
     }]
   }],
   total : 123
}
```

[children](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#field-children)
Child nodes. To allow loading children on demand, specify `children : true` in your data. Omit the field for leaf tasks.

Note, if the tree store loads data from a remote origin, make sure [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl) is specified, and optionally [parentIdParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-parentIdParamName) is set, otherwise [loadChildren](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-loadChildren) has to be implemented.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTreeNode](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-isTreeNode)
Identifies an object as an instance of [TreeNode](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode) class, or subclass thereof.

[isTreeNode](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-isTreeNode-static)
Identifies an object as an instance of [TreeNode](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode) class, or subclass thereof.

[convertEmptyParentToLeaf](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-convertEmptyParentToLeaf-static)
This static configuration option allows you to control whether an empty parent task should be converted into a leaf. Enable/disable it for a whole class:

```
Model.convertEmptyParentToLeaf = false;
```

By specifying `true`, all empty parents will be considered leafs. Can also be assigned a configuration object with the following Boolean properties to customize the behaviour:

```
Model.convertEmptyParentToLeaf = {
    onLoad   : false,
    onRemove : true
}
```

[parent](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-parent)
This is a read-only property providing access to the parent node.

[unfilteredChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-unfilteredChildren)
Array of tree nodes without any filter applied. On first filter, will take order from sorted `children`, but is not thereafter kept in sorted order, so order should not be relied upon.

[orderedChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-orderedChildren)
Array of children unaffected by sorting and filtering, keeps original tree structure

[childLevel](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-childLevel)
Depth in the tree at which this node exists. First visual level of nodes are at level 0, their direct children at level 1 and so on.

[isLeaf](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-isLeaf)
Is a leaf node in a tree structure?

[isRoot](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-isRoot)
Returns `true` if this node is the root of the tree

[isParent](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-isParent)
Is a parent node in a tree structure?

[isLoaded](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-isLoaded)
Returns true for parent nodes with children loaded (there might still be no children)

[hierarchyModificationDataToWrite](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-hierarchyModificationDataToWrite)
Returns values of the persistable tree-defining fields: parentId, orderedParentIndex, and parentIndex or sparseIndex. parentIndex is omitted when sparseIndex is used.

[descendantCount](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-descendantCount)
Count all children (including sub-children) for a node (in its \`firstStore´)

[visibleDescendantCount](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-visibleDescendantCount)
Count visible (expanded) children (including sub-children) for a node (in its `firstStore`)

[allChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-allChildren)
Retrieve all children, excluding filtered out nodes (by traversing sub nodes)

[allUnfilteredChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-allUnfilteredChildren)
Retrieve all children, including filtered out nodes (by traversing sub nodes)

[firstChild](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-firstChild)
Get the first child of this node

[lastChild](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-lastChild)
Get the last child of this node

[previousSibling](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-previousSibling)
Get the previous sibling of this node

[nextSibling](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-nextSibling)
Get the next sibling of this node

[previousSiblingsTotalCount](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-previousSiblingsTotalCount)
Returns count of all preceding sibling nodes (including their children).

[parentId](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#property-parentId)
Reading this property returns the id of the parent node, if this record is a child of a node.

Setting this property appends this record to the record with the passed id **in the same store that this record is already in**.

Note that setting this property is **only valid if this record is already part of a tree store**.

This is not intended for general use. This is for when a server responds to a record mutation and the server decides to move a record to a new parent. If a `parentId` property is passed in the response data for a record, that record will be moved.

## Functions

Functions are methods available for calling on the class

[processChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-processChildren)
Called during creation to also turn any children into Models joined to the same stores as this model

[ancestorsExpanded](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-ancestorsExpanded)
This method returns `true` if this record has all expanded ancestors and is therefore eligible for inclusion in a UI.

[isExpanded](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-isExpanded)
Used by stores to assess the record's collapsed/expanded state in that store.

[getDescendantCount](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-getDescendantCount)
Count visible (expanded)/all children for this node, optionally specifying for which store.

[traverse](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-traverse)
Traverses all child nodes recursively calling the passed function on a target node **before** iterating the child nodes.

[traverseBefore](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-traverseBefore)
Traverses all child nodes recursively calling the passed function on child nodes of a target **before** calling it on the node.

[traverseWhile](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-traverseWhile)
Traverses child nodes recursively while fn returns true

[bubble](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-bubble)
Bubbles up from this node, calling the specified function with each node.

[bubbleWhile](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-bubbleWhile)
Bubbles up from this node, calling the specified function with each node, while the function returns true.

[contains](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-contains)
Checks if this model contains another model as one of it's descendants

[appendChild](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-appendChild)
Append a child record(s) to any current children.

[insertChild](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-insertChild)
Insert a child record(s) before an existing child record.

[convertToParent](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-convertToParent)
Converts a leaf node to a parent node, assigning an empty array as its children

[removeChild](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-removeChild)
Remove a child record. Only direct children of this node can be removed, others are ignored.

[replaceChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-replaceChildren)
Replaces all child nodes with the new node set.

[clearChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-clearChildren)
Removes all child nodes from this node.

[clear](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-clear)
Removes all records from the rootNode

[sortOrderedChildren](https://bryntum.com/docs/gantt/api/Core/data/mixin/TreeNode#function-sortOrderedChildren)
Iterates orderedChildren array to apply sorting order according to `orderedParentIndex`. Normally sorting is not required because order is maintained on append/insert. But is useful when pasting number of records to restore their original order.
