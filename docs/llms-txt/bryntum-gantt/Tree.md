# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Tree.md

# [Tree](https://bryntum.com/docs/gantt/api/Grid/feature/Tree)

Feature that makes the grid work more like a tree. Included by default in [TreeGrid](https://bryntum.com/docs/gantt/api/#Grid/view/TreeGrid). Requires exactly one [TreeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn) among grids columns. That column will have its renderer replaced with a tree renderer that adds padding and icon to give the appearance of a tree. The original renderer is preserved and also called.

This feature is **disabled** by default. When enabled, the feature cannot be disabled during runtime.

Keyboard shortcuts
------------------

This feature has the following default keyboard shortcuts:

Keys

Action

Action description

`Space`

_toggleCollapseByKey_

When focus on a parent node, this expands or collapses it's children

`ArrowRight`

_expandIfSingleColumn_

Expands a focused parent node if grid consist of one column only

`Shift`+`ArrowRight`

_expandByKey_

Expands a focused parent node

`ArrowLeft`

_collapseIfSingleColumn_

Collapses a focused parent node if grid consist of one column only

`Shift`+`ArrowLeft`

_collapseByKey_

Collapses a focused parent node

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[expandOnCellClick](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#config-expandOnCellClick)
Expand parent nodes when clicking on their cell

[keyMap](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Grid/feature/Tree#keyboard-shortcuts) for details

[treeLines](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#config-treeLines)
Show or hide tree lines

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTree](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#property-isTree)
Identifies an object as an instance of [Tree](https://bryntum.com/docs/gantt/api/#Grid/feature/Tree) class, or subclass thereof.

[isTree](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#property-isTree-static)
Identifies an object as an instance of [Tree](https://bryntum.com/docs/gantt/api/#Grid/feature/Tree) class, or subclass thereof.

[expandOnCellClick](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#property-expandOnCellClick)
Expand parent nodes when clicking on their cell

[treeLines](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#property-treeLines)
Show or hide tree lines

## Functions

Functions are methods available for calling on the class

[toggleCollapse](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-toggleCollapse)
Collapse an expanded node or expand a collapsed. Optionally forcing a certain state. This function is exposed on Grid and can thus be called as `grid.toggleCollapse()`

[collapse](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-collapse)
Collapse a single node. This function is exposed on Grid and can thus be called as `grid.collapse()`

[expand](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-expand)
Expand a single node. This function is exposed on Grid and can thus be called as `grid.expand(idOrRecord)`

[expandOrCollapseAll](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-expandOrCollapseAll)
Expand or collapse all nodes, as specified by param, starting at the passed node (which defaults to the root node)

[collapseAll](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-collapseAll)
Collapse all nodes. This function is exposed on Grid and can thus be called as `grid.collapseAll()`

[expandAll](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-expandAll)
Expand all nodes. This function is exposed on Grid and can thus be called as `grid.expandAll()`

[expandTo](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-expandTo)
Expands parent nodes to make this node "visible". This function is exposed on Grid and can thus be called as `grid.expandTo()`

[expandToLevel](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-expandToLevel)
Expands the parent nodes in the tree to the provided depth.

[onElementClick](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-onElementClick)
Called when user clicks somewhere in the grid. Expand/collapse node on icon click.

[toggleCollapseByKey](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#function-toggleCollapseByKey)
Called on key down in grid. Expand/collapse node on \[space\]

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[collapseNode](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#event-collapseNode)
Fired before a parent node record is collapsed.

[expandNode](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#event-expandNode)
Fired after a parent node record is expanded.

[toggleNode](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#event-toggleNode)
Fired after a parent node record toggles its collapsed state.

[beforeToggleNode](https://bryntum.com/docs/gantt/api/Grid/feature/Tree#event-beforeToggleNode)
Fired before a parent node record toggles its collapsed state.
