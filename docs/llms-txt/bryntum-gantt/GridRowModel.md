# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/data/GridRowModel.md

# [GridRowModel](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel)

Model extended with some fields related to grid rendering. Used as default model type in the grids store if nothing else is specified.

Using this model is optional. If you use a custom model instead and need the functionality of any of the fields below, you just have to remember to add fields with the same name to your model.

## Fields

Fields belong to a Model class and define the Model data structure

[iconCls](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel#field-iconCls)
Icon for row (used automatically in tree, feel free to use it in renderer in other cases)

[cls](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel#field-cls)
CSS class (or several classes divided by space) to append to row elements

[rowHeight](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel#field-rowHeight)
Used by the default implementation of [getRowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-getRowHeight) to determine row height. Set it to use another height than the default for the records row.

[href](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel#field-href)
A link to use for this record when rendered into a [TreeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn).

[target](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel#field-target)
The target to use if this tree node provides a value for the [href](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-href) field.

[fixed](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel#field-fixed)
A boolean field used by the [LockRows](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows) feature for pinning a row to the top.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridRowModel](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel#property-isGridRowModel)
Identifies an object as an instance of [GridRowModel](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel) class, or subclass thereof.

[isGridRowModel](https://bryntum.com/docs/gantt/api/Grid/data/GridRowModel#property-isGridRowModel-static)
Identifies an object as an instance of [GridRowModel](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel) class, or subclass thereof.
