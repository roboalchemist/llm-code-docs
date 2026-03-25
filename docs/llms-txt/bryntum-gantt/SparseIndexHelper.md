# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/SparseIndexHelper.md

# [SparseIndexHelper](https://bryntum.com/docs/gantt/api/Core/helper/SparseIndexHelper)

Helpers for working with sparseIndex fields on records.

A sparseIndex is a number field that is used to sort records in a Store. It can have gaps and fractional values. SparseIndexes are unique among all records in a flat Store, i.e. no two records in a Store should have the same sparseIndex value. In case of a TreeStore, sparseIndexes are unique only among sibling records. The main purpose of a sparseIndex is to allow reordering of records without having to update the sparseIndex of every record in the Store. New records can be assigned a sparseIndex that is between the sparseIndexes of two existing records.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[sorter](https://bryntum.com/docs/gantt/api/Core/helper/SparseIndexHelper#property-sorter)
Sort function that can be used to sort records by their sparseIndex field, putting records without a sparseIndex at the end of the collection.

## Functions

Functions are methods available for calling on the class

[nextSiblingIndex](https://bryntum.com/docs/gantt/api/Core/helper/SparseIndexHelper#function-nextSiblingIndex-static)
Calculates the next sparseIndex value from a record's siblings. If the passed record already has a sparseIndex (e.g. because record was already in store and got moved), its sparseIndex is ignored because it will be overwritten.

[addSparseIndexes](https://bryntum.com/docs/gantt/api/Core/helper/SparseIndexHelper#function-addSparseIndexes-static)
Generates sparse indexes on the passed records. `prev` and `next` records are used as boundaries for the sparse indexes. If there is no preceding record, i.e. the records have been prepended, the generated indexes are integers that may be positive or negative. If both `prev` and `next` are present, the generated indexes are fractional numbers evenly distributed between the boundaries.

[consolidateSparseIndexes](https://bryntum.com/docs/gantt/api/Core/helper/SparseIndexHelper#function-consolidateSparseIndexes-static)
Consolidates sparse indexes on the passed records, making them sequential numbers. Use this to avoid having duplicate values. IMPORTANT: Only use this on sorted records, otherwise it might create duplicate sparse indexes again!
