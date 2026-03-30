# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/MergeCells.md

# [MergeCells](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells)

This feature merges cells that have the same value in sorted (or [optionally](https://bryntum.com/docs/gantt/api/#Grid/feature/MergeCells#config-sortedOnly) any) columns configured to [mergeCells](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-mergeCells).

The content of merged cells is sticky for Grids with a single subgrid section when all columns fit in view (content stays in view until the cell is scrolled fully out of view).

Support for sticky content is limited because of how `position: sticky` works. Grid scrolls vertically in one element, and horizontally in another (to support multiple regions in the grid), and this setup is not supported by current browsers implementation of sticky positioning

Try scrolling in the demo below. As mentioned above, cells are by default merged only in sorted columns - try sorting by the other columns ("City" and "Favorite food" are configured to merge cells):

By configuring the feature with `sortedOnly : false`, cells can be merged in any column:

This feature is **disabled** by default.

This feature will not work properly when Store uses [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[passthrough](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells#config-passthrough)
By default, merged cells allow pointer events to pass through to the underlying row/cell, to allow selecting a row and editing an individual cell even when they are merged. Configure as `false` to allow merged cells to catch and react to the pointer events instead.

```
const grid = new Grid({
    features : {
        mergeCells : {
            // Let merged cells react to pointer events
            passthrough : false
        }
    }
});
```

[sortedOnly](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells#config-sortedOnly)
Configure as `false` to allow merging cells in columns that are not sorted.

Note that this will have a slight negative impact on performance, since cells in all columns configured to merge cells have to be iterated.

[shouldMerge](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells#config-shouldMerge)
Hook used to control which cells should be included in a merged range of cells.

The feature first determines the range using its default logic. It then calls this hook for each cell in the range except the first, and if the hook returns `false`, the cell is not included in the range but instead a new range is started. The hook thus controls if a cell should be merged with the cell above it or not.

Example usage:

```
const grid = new Grid({
   features : {
       mergeCells : {
           shouldMerge({ column, record, previousRecord, value }) {
               // Only merge cells in the "Age" column as long as the "Name" matches the previous record
               if (column.field === 'age') {
                   return record.name === previousRecord.name;
               }

               // Merge other cells as usual
               return true;
           }
       }
   }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMergeCells](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells#property-isMergeCells)
Identifies an object as an instance of [MergeCells](https://bryntum.com/docs/gantt/api/#Grid/feature/MergeCells) class, or subclass thereof.

[isMergeCells](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells#property-isMergeCells-static)
Identifies an object as an instance of [MergeCells](https://bryntum.com/docs/gantt/api/#Grid/feature/MergeCells) class, or subclass thereof.

[passthrough](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells#property-passthrough)
By default, merged cells allow pointer events to pass through to the underlying row/cell, to allow selecting a row and editing an individual cell even when they are merged. Configure as `false` to allow merged cells to catch and react to the pointer events instead.

```
const grid = new Grid({
    features : {
        mergeCells : {
            // Let merged cells react to pointer events
            passthrough : false
        }
    }
});
```

[sortedOnly](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells#property-sortedOnly)
Configure as `false` to allow merging cells in columns that are not sorted.

Note that this will have a slight negative impact on performance, since cells in all columns configured to merge cells have to be iterated.

[shouldMerge](https://bryntum.com/docs/gantt/api/Grid/feature/MergeCells#property-shouldMerge)
Hook used to control which cells should be included in a merged range of cells.

The feature first determines the range using its default logic. It then calls this hook for each cell in the range except the first, and if the hook returns `false`, the cell is not included in the range but instead a new range is started. The hook thus controls if a cell should be merged with the cell above it or not.

Example usage:

```
const grid = new Grid({
   features : {
       mergeCells : {
           shouldMerge({ column, record, previousRecord, value }) {
               // Only merge cells in the "Age" column as long as the "Name" matches the previous record
               if (column.field === 'age') {
                   return record.name === previousRecord.name;
               }

               // Merge other cells as usual
               return true;
           }
       }
   }
});
```
