# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/TreeGrid.md

# [TreeGrid](https://bryntum.com/docs/gantt/api/Grid/view/TreeGrid)

A TreeGrid, a Tree combined with a Grid. Must be configured with exactly one [TreeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn) (`type: tree`), but can also have an arbitrary number of other columns. Most features that can be used with Grid also works with TreeGrid, except the Group feature.

Using a Store configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad) is not supported in TreeGrid.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[store](https://bryntum.com/docs/gantt/api/Grid/view/TreeGrid#config-store)
The store instance or config object that holds the records to be displayed by this TreeGrid. If assigning a store instance, it must be configured with `tree: true`.

A store will be created if none is specified.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTreeGrid](https://bryntum.com/docs/gantt/api/Grid/view/TreeGrid#property-isTreeGrid)
Identifies an object as an instance of [TreeGrid](https://bryntum.com/docs/gantt/api/#Grid/view/TreeGrid) class, or subclass thereof.

[isTreeGrid](https://bryntum.com/docs/gantt/api/Grid/view/TreeGrid#property-isTreeGrid-static)
Identifies an object as an instance of [TreeGrid](https://bryntum.com/docs/gantt/api/#Grid/view/TreeGrid) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[toggleCollapse](https://bryntum.com/docs/gantt/api/Grid/view/TreeGrid#function-toggleCollapse)
Collapse an expanded node or expand a collapsed. Optionally forcing a certain state.

[collapse](https://bryntum.com/docs/gantt/api/Grid/view/TreeGrid#function-collapse)
Collapse a single node.

[expand](https://bryntum.com/docs/gantt/api/Grid/view/TreeGrid#function-expand)
Expand a single node.

[expandTo](https://bryntum.com/docs/gantt/api/Grid/view/TreeGrid#function-expandTo)
Expands parent nodes to make this node "visible".
