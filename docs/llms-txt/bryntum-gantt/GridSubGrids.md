# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/mixin/GridSubGrids.md

# [GridSubGrids](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids)

Mixin for grid that handles SubGrids. Each SubGrid is scrollable horizontally separately from the other SubGrids. Having two SubGrids allows you to achieve what is usually called locked or frozen columns.

By default a Grid has two SubGrids, one named 'locked' and one 'normal'. The `locked` region has fixed width, while the `normal` region grows to fill all available width (flex).

Which SubGrid a column belongs to is determined using its [region](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-region) config. For example to put a column into the locked region, specify `{ region: 'locked' }`. For convenience, a column can be put in the locked region using `{ locked: true }`.

```
new Grid({
  columns : [
    // These two columns both end up in the "locked" region
    { field: 'name', text: 'Name', locked: true }
    { field: 'age', text: 'Age', region: 'locked' }
  ]
});
```

To customize the SubGrids, use [subGridConfigs](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-subGridConfigs):

```
// change the predefined subgrids
new Grid({
  subGridConfigs : {
      locked : { flex : 1 } ,
      normal : { flex : 3 }
  }
})

// or define your own entirely
new Grid({
  subGridConfigs : {
      a : { width : 150 } ,
      b : { flex  : 1 },
      c : { width : 150 }
  },

  columns : [
      { field : 'name', text : 'Name', region : 'a' },
      ...
  ]
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridSubGrids](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#property-isGridSubGrids)
Identifies an object as an instance of [GridSubGrids](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSubGrids) class, or subclass thereof.

[isGridSubGrids](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#property-isGridSubGrids-static)
Identifies an object as an instance of [GridSubGrids](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSubGrids) class, or subclass thereof.

[subGrids](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#property-subGrids)
An object containing the [SubGrid](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid) region instances, indexed by subGrid id ('locked', normal'...)

## Functions

Functions are methods available for calling on the class

[eachSubGrid](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#function-eachSubGrid)
Iterate over all subGrids, calling the supplied function for each.

[callEachSubGrid](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#function-callEachSubGrid)
Call a function by name for all subGrids (that have the function).

[getLastRegions](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#function-getLastRegions)
This method should return names of the two last regions in the grid as they are visible in the UI. In case `regions` property cannot be trusted, use different approach. Used by SubGrid and RegionResize to figure out which region should collapse or expand.

[getNextRegion](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#function-getNextRegion)
This method should return right neighbour for passed region, or left neighbour in case last visible region is passed. This method is used to decide which subgrid should take space of the collapsed one.

[getSubGrid](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#function-getSubGrid)
Returns the subGrid for the specified region.

[getSubGridFromColumn](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#function-getSubGridFromColumn)
Get the SubGrid that contains specified column

[resolveSplitter](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSubGrids#function-resolveSplitter)
Returns splitter element for subgrid
