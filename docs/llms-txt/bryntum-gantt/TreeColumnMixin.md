# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/mixin/TreeColumnMixin.md

# [TreeColumnMixin](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin)

A mixin that adds tree rendering capabilities to any column type. Applied automatically when a column config includes `tree: true`.

This mixin extracts all tree rendering logic from TreeColumn, allowing any column type (e.g., `ResourceInfoColumn`, `CheckColumn`) to display tree structure when configured with `tree: true`.

Usage
-----

```
const grid = new TreeGrid({
    columns : [
        // Any column type can now be a tree column
        { type : 'resourceInfo', tree : true, field : 'name' },
        { type : 'check', tree : true, field : 'done' }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[expandIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#config-expandIconCls)
The icon to use for the expand / collapse button icon in collapsed state

[collapseIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#config-collapseIconCls)
The icon to use for the expand / collapse button in expanded state

[collapsedFolderIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#config-collapsedFolderIconCls)
The icon to use for a parent node in collapsed state

[expandedFolderIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#config-expandedFolderIconCls)
The icon to use for a parent node in expanded state

[indentSize](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#config-indentSize)
Size of the child indent in em. Resulting indent is indentSize multiplied by child level.

Sets the `--b-tree-indent-size` CSS variable. By default, the value of the variable set by the theme is used.

[leafIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#config-leafIconCls)
The icon to use for the leaf nodes in the tree

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTreeColumnMixin](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-isTreeColumnMixin)
Identifies an object as an instance of [TreeColumnMixin](https://bryntum.com/docs/gantt/api/#Grid/column/mixin/TreeColumnMixin) class, or subclass thereof.

[isTreeColumnMixin](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-isTreeColumnMixin-static)
Identifies an object as an instance of [TreeColumnMixin](https://bryntum.com/docs/gantt/api/#Grid/column/mixin/TreeColumnMixin) class, or subclass thereof.

[expandIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-expandIconCls)
The icon to use for the expand / collapse button icon in collapsed state

[collapseIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-collapseIconCls)
The icon to use for the expand / collapse button in expanded state

[collapsedFolderIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-collapsedFolderIconCls)
The icon to use for a parent node in collapsed state

[expandedFolderIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-expandedFolderIconCls)
The icon to use for a parent node in expanded state

[indentSize](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-indentSize)
Size of the child indent in em. Resulting indent is indentSize multiplied by child level.

Sets the `--b-tree-indent-size` CSS variable. By default, the value of the variable set by the theme is used.

[leafIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-leafIconCls)
The icon to use for the leaf nodes in the tree

[isTreeColumn](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-isTreeColumn-static)
Identifies this column as a tree column

[isTreeColumn](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#property-isTreeColumn)
Identifies this column as a tree column

## Functions

Functions are methods available for calling on the class

[buildTreeLineBlocks](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#function-buildTreeLineBlocks)
Generates tree line blocks for hierarchical indentation

[getTreeIconCls](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#function-getTreeIconCls)
Determines the appropriate icon class for a tree node

[processRendererValue](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#function-processRendererValue)
Processes the renderer value and calls the original renderer if present

[handleWidgetColumnRendering](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#function-handleWidgetColumnRendering)
Handles widget column rendering by relocating widgets into tree structure

[configureInnerElement](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#function-configureInnerElement)
Configures the inner tree cell value element

[treeRenderer](https://bryntum.com/docs/gantt/api/Grid/column/mixin/TreeColumnMixin#function-treeRenderer)
A column renderer that is automatically added to the column with { tree: true }. It adds padding and node icons to the cell to make the grid appear to be a tree. The original renderer is called in the process.
