# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreSparseIndex.md

# [StoreSparseIndex](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex)

Mixin for Store that handles sparse index generation for its records. Sparse indexes are useful for manually ordering of records. To prevent the necessity to update indexes on a large number of records when inserting or reordering records, sparse indexes are fractional numbers that will be generated inbetween the sparse indexes of the surrounding record.

This mixin is **disabled** by default and needs to be enabled on a per-Store basis.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[useSparseIndex](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#config-useSparseIndex)
Enable sparse index handling. When enabled, the store's model will be augmented with a `sparseIndex` field (unless it already exists) which will be automatically managed by the store. When adding or inserting records into the store, sparse indexes will be generated for those records. When moving records, their sparse index will be updated with a fractional number. They will be used to sort records when no other sorter is defined on the store.

Sparse indexes are a tree-defining property. They will also be used to determine the order of records when persisting the store's data. When using sparse indexes in a tree store, the store's [parentId](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#field-parentId) will also be made persistent to allow reconstruction of the tree structure when loading data.

When using sparse indexes, the other tree-defining properties `parentIndex` and `orderedParentIndex` will no longer be persistent. Their values will still be updated when items are added, removed, or re-ordered, but they won't be marked as dirty and won't be included when persisting the store's data. If it is necessary to persist these fields, use [hierarchyModificationDataToWrite](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#property-hierarchyModificationDataToWrite).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreSparseIndex](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#property-isStoreSparseIndex)
Identifies an object as an instance of [StoreSparseIndex](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSparseIndex) class, or subclass thereof.

[isStoreSparseIndex](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#property-isStoreSparseIndex-static)
Identifies an object as an instance of [StoreSparseIndex](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSparseIndex) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[initSparseIndexes](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#function-initSparseIndexes)
Initialize sparse indexes for existing records which don't have a sparseIndex value. If the store is not sorted, it will first be sorted by sparseIndex; records without one are sorted to the end. After all records have a sparseIndex value, the values will be consolidated to ensure that no duplicates exist.

[createSorterFn](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#function-createSorterFn)
Creates a function used with Array#sort when sorting the store. This override adds a sorter on the sparseIndex field if sparse indexes are used and no other sorters are defined.

[add](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#function-add)
Wrapper for StoreCRUD.add, adding sparse indexes to appended records

[insert](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#function-insert)
Wrapper for StoreCRUD.insert, adding sparse indexes to inserted records

[remove](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#function-remove)
Wrapper for StoreCRUD.remove, clearing sparse indexes on removed records

[move](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSparseIndex#function-move)
Wrapper for StoreCRUD.move, adding sparse indexes to inserted records
