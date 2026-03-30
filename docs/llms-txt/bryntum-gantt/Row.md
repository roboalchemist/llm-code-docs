# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/row/Row.md

# [Row](https://bryntum.com/docs/gantt/api/Grid/row/Row)

Represents a single rendered row in the grid. Consists of one row element for each SubGrid in use. The grid only creates as many rows as needed to fill the current viewport (and a buffer). As the grid scrolls the rows are repositioned and reused, there is not a one-to-one relation between rows and records.

For normal use cases you should not have to use this class directly. Rely on using renderers instead.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[cls](https://bryntum.com/docs/gantt/api/Grid/row/Row#config-cls)
The class name to initially add to all row elements

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRow](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-isRow)
Identifies an object as an instance of [Row](https://bryntum.com/docs/gantt/api/#Grid/row/Row) class, or subclass thereof.

[isRow](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-isRow-static)
Identifies an object as an instance of [Row](https://bryntum.com/docs/gantt/api/#Grid/row/Row) class, or subclass thereof.

[cls](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-cls)
When **read**, this a [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList) of class names to be applied to this Row's elements.

It can be **set** using Object notation where each property name with a truthy value is added as a class, or as a regular space-separated string.

[index](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-index)
Get index in RowManagers rows array

[dataIndex](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-dataIndex)
Get/set this rows current index in grids store

[id](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-id)
Get/set id for currently rendered record

[elements](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-elements)
An object, keyed by region name (for example `locked` and `normal`) containing the elements which comprise the full row.

[element](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-element)
The row element, only applicable when not using multiple grid sections (see [elements](https://bryntum.com/docs/gantt/api/#Grid/row/Row#property-elements))

[cells](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-cells)
Row cell elements

[height](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-height)
Get/set row height

[offsetHeight](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-offsetHeight)
Get row height including border

[isFirst](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-isFirst)
Is this the very first row?

[top](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-top)
Row top coordinate

[bottom](https://bryntum.com/docs/gantt/api/Grid/row/Row#property-bottom)
Row bottom coordinate

## Functions

Functions are methods available for calling on the class

[constructor](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-constructor)
Constructs a Row setting its index.

[addElement](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-addElement)
Add a row element for specified region.

[getElement](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-getElement)
Get the element for the specified region.

[getRectangle](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-getRectangle)
Get the [element bounds](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle) for the specified region of this Row.

[eachElement](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-eachElement)
Execute supplied function for each regions element.

[eachCell](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-eachCell)
Execute supplied function for each cell.

[getCells](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-getCells)
Get cell elements for specified region.

[getCell](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-getCell)
Get the cell element for the specified column.

[updateElementsHeight](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-updateElementsHeight)
Sync elements height to rows height

[addCls](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-addCls)
Add CSS classes to each element.

[removeCls](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-removeCls)
Remove CSS classes from each element.

[toggleCls](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-toggleCls)
Toggle CSS classes for each element.

[assignCls](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-assignCls)
Adds/removes class names according to the passed object's properties.

Properties with truthy values are added. Properties with false values are removed.

[setTop](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-setTop)
Sets top coordinate, translating elements position.

[setBottom](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-setBottom)
Sets bottom coordinate, translating elements position.

[positionElements](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-positionElements)
Sets css top to position elements at correct top position

[offset](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-offset)
Moves all row elements up or down and updates model.

[renderPlaceholder](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-renderPlaceholder)
When the Store has `lazyLoad` set to `true` and the record is waiting to be loaded, a "skeleton" placeholder is rendered while waiting.

[render](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-render)
Renders a record into this row´s elements (trigger event that subgrids catch to do the actual rendering).

[renderCell](https://bryntum.com/docs/gantt/api/Grid/row/Row#function-renderCell)
Renders a single cell, calling features to allow them to hook
