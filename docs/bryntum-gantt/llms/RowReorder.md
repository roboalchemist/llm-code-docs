# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/RowReorder.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/RowReorder.md

# [RowReorder](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder)

Allows user to reorder rows by dragging them. To get notified about row reorder listen to `change` event on the grid [store](https://bryntum.com/docs/gantt/api/#Core/data/Store).

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures). This feature is **enabled** by default for Gantt.

If the grid is set to [readOnly](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-readOnly), reordering is disabled. Inside all event listeners you have access a `context` object which has a `record` property (the dragged record).

Usage when grouping
-------------------

When the [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature is active, note that row reordering is only possible for leaf rows and only when grouping is done using Model fields (not function-based grouping).

Row reordering is also disabled when the store is grouped using the [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) feature and the "group by" field is an array value. In this case records may also be present in more than one group and so some records will be linked records, **not** the real records.

Validation
----------

You can validate the drag drop flow by listening to the `gridrowdrag` event. Inside this listener you have access to the `index` property which is the target drop position. For trees you get access to the `parent` record and `index`, where index means the child index inside the parent.

You can also have an async finalization step using the [gridRowBeforeDropFinalize](https://bryntum.com/docs/gantt/api/#Grid/feature/RowReorder#event-gridRowBeforeDropFinalize), for showing a confirmation dialog or making a network request to decide if drag operation is valid (see code snippet below)

```
features : {
    rowReorder : {
        showGrip : true
    },
    listeners : {
       gridRowDrag : ({ context }) => {
          // Here you have access to context.insertBefore, and additionally context.parent for trees
       },

       gridRowBeforeDropFinalize : async ({ context }) => {
          const result = await MessageDialog.confirm({
              title   : 'Please confirm',
              message : 'Did you want the row here?'
          });

          // true to accept the drop or false to reject
          return result === MessageDialog.yesButton;
       }
   }
}
```

Note, that this feature uses the concept of "insert before" when choosing a drop point in the data. So the dropped record's position is _before the visual next record's position_.

This may look like a pointless distinction, but consider the case when a Store is filtered. The record _above_ the drop point may have several filtered out records below it. When unfiltered, the dropped record will be _below_ these because of the "insert before" behaviour.

Behavior with multiple subgrids
-------------------------------

For grids with multiple subgrids, row reordering is only enabled for the first subgrid.

Dragging rows between different grids
-------------------------------------

You can enable dragging to different `Grid` instances by enabling the [allowCrossGridDrag](https://bryntum.com/docs/gantt/api/#Grid/feature/RowReorder#config-allowCrossGridDrag). This lets you both move and copy (using Ctrl/Meta key) records to other grids. You can also configure a special `transferData` method to take full control over what happens on drop onto another grid.

NOTE: This feature cannot be used simultaneously with the `enableTextSelection` config.

Reordering rows in a chained store
----------------------------------

When using a chained flat store (created using [chain](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-chain)), reordering rows will by default not change the order of the records in the original store. This behavior can be changed by setting the [syncOrder](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-syncOrder) config to `true` on the chained store.

When on the other hand using a chained tree store (created using [chainTree](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-chainTree)), the order of the records in the original store will always be changed.

When Store has [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), row reordering might cause data inconsistency and is not recommended.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showGrip](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-showGrip)
Set to `true` to show a grip icon on the left side of each row. Or set to `'hover'` to reserve space for the grip but only show it when hovering over the row.

[gripOnly](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-gripOnly)
Set to `true` to only allow reordering by the [showGrip](https://bryntum.com/docs/gantt/api/#Grid/feature/RowReorder#config-showGrip) config.

[hoverExpandTimeout](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-hoverExpandTimeout)
If hovering over a parent node for this period of a time in a tree, the node will expand.

[touchStartDelay](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-touchStartDelay)
The amount of milliseconds to wait after a touchstart, before a drag gesture will be allowed to start.

[dropOnLeaf](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-dropOnLeaf)
Enables creation of parents by dragging a row and dropping it onto a leaf row. Only works in a Grid with a tree store. This option is `true` by default in the Gantt product.

[copyIconCls](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-copyIconCls)
The CSS class to add to the icon element indicating it is a copy operation.

[allowCrossGridDrag](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-allowCrossGridDrag)
Enables dragging rows to other grid instances. By default, this will remove from the source grid `store` and add the dragged record(s) to the target grid `store`. If you would like to implement another transfer of the data (e.g. to copy instead of move), you can provide an object with a `transferData` method.

```
features : {
    rowReorder : {
         allowCrossGridDrag : {
             async transferData({ records, insertBefore, parent }) {
                 records = records.map((rec) => rec.copy());
                 await parent.insertChild(records, this.over ? parent.children?.[0] : insertBefore);
             }
        }
    }
}
```

[dragHelperConfig](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-dragHelperConfig)
An object used to configure the internal [DragHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper) class

[preserveSorters](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#config-preserveSorters)
Set to `true` to preserve sorters after a drop operation, if that operation leads to the store still being sorted.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRowReorder](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#property-isRowReorder)
Identifies an object as an instance of [RowReorder](https://bryntum.com/docs/gantt/api/#Grid/feature/RowReorder) class, or subclass thereof.

[isRowReorder](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#property-isRowReorder-static)
Identifies an object as an instance of [RowReorder](https://bryntum.com/docs/gantt/api/#Grid/feature/RowReorder) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[init](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#function-init)
Initialize drag & drop (called on first paint)

[onDrop](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#function-onDrop)
Handle drop

[onReset](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#function-onReset)
Clean up on reset

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[gridRowBeforeDragStart](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#event-gridRowBeforeDragStart)
Fired before dragging starts, return false to prevent the drag operation.

[gridRowDragStart](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#event-gridRowDragStart)
Fired when dragging starts.

[gridRowDrag](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#event-gridRowDrag)
Fired while the row is being dragged, in the listener function you have access to `context.insertBefore` a grid / tree record, and additionally `context.parent` (a TreeNode) for trees. You can signal that the drop position is valid or invalid by setting `context.valid = false;`

[gridRowBeforeDropFinalize](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#event-gridRowBeforeDropFinalize)
Fired before the row drop operation is finalized. You can return false to abort the drop operation, or a Promise yielding `true` / `false` which allows for asynchronous abort (e.g. first show user a confirmation dialog).

[gridRowDrop](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#event-gridRowDrop)
Fired after the row drop operation has completed, regardless of validity

[gridRowDragAbort](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#event-gridRowDragAbort)
Fired when a row drag operation is aborted

## Typedefs

Typedefs are type definitions for the class

[RecordPositionContext](https://bryntum.com/docs/gantt/api/Grid/feature/RowReorder#typedef-RecordPositionContext)
Object with information about a tree position
