# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/TreeGroup.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TreeGroup.md

# [TreeGroup](https://bryntum.com/docs/gantt/api/Gantt/feature/TreeGroup)

Extends Grid's [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) (follow the link for more info) feature to enable using it with Gantt. Allows generating a new task tree where parents are determined by the values of specified task fields/functions:

Important information
---------------------

Using the TreeGroup feature comes with some caveats:

* Grouping replaces the store Gantt uses to display tasks with a temporary "display store". The original task store is left intact, when grouping stops Gantt will revert to using it to display tasks.
* `gantt.taskStore` points to the original store when this feature is enabled. To apply sorting or filtering programmatically, you should instead interact with the "display store" directly, using `gantt.store`.
* Generated parents are read-only, they cannot be edited using the default UI.
* Leaves in the new tree are still editable as usual, and any changes to them survives the grouping operation.
* Moving tasks in the tree (rearranging rows) is not supported while it is grouped.

This feature is **disabled** by default.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTreeGroup](https://bryntum.com/docs/gantt/api/Gantt/feature/TreeGroup#property-isTreeGroup)
Identifies an object as an instance of [TreeGroup](https://bryntum.com/docs/gantt/api/#Gantt/feature/TreeGroup) class, or subclass thereof.

[isTreeGroup](https://bryntum.com/docs/gantt/api/Gantt/feature/TreeGroup#property-isTreeGroup-static)
Identifies an object as an instance of [TreeGroup](https://bryntum.com/docs/gantt/api/#Gantt/feature/TreeGroup) class, or subclass thereof.
