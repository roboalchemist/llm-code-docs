# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/RegionResize.md

# [RegionResize](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize)

Makes the splitter between grid [sections](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid) draggable, to let users resize, and collapse/expand the sections.

```
// enable RegionResize
const grid = new Grid({
  features: {
    regionResize: true
  }
});
```

If you use two regions, and you would like to prevent resizing/expanding the first (left section, rightmost in RTL), set [maxWidth](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid#config-maxWidth) and [width](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid#config-width) to the same value.

```
// enable RegionResize
const grid = new Grid({
  features: {
    regionResize: true
  },
  subGridConfigs : {
        locked : {
            width : 400,
            // prevent making the left section wider than 400px
            maxWidth : 400
        },
        normal : {
            flex : 1
        }
    }
});
```

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showSplitterButtons](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#config-showSplitterButtons)
Set to `false` to hide the splitter's collapse/expand buttons

[animateCollapseExpand](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#config-animateCollapseExpand)
Set to `false` to not use transitions when expanding or collapsing a sub grid

[enableDragging](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#config-enableDragging)
This flag prevents dragging if set to `false` but the collapse / expand buttons will still be functional.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRegionResize](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#property-isRegionResize)
Identifies an object as an instance of [RegionResize](https://bryntum.com/docs/gantt/api/#Grid/feature/RegionResize) class, or subclass thereof.

[isRegionResize](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#property-isRegionResize-static)
Identifies an object as an instance of [RegionResize](https://bryntum.com/docs/gantt/api/#Grid/feature/RegionResize) class, or subclass thereof.

[showSplitterButtons](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#property-showSplitterButtons)
Set to `false` to hide the splitter's collapse/expand buttons

[animateCollapseExpand](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#property-animateCollapseExpand)
Set to `false` to not use transitions when expanding or collapsing a sub grid

[enableDragging](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#property-enableDragging)
This flag prevents dragging if set to `false` but the collapse / expand buttons will still be functional.

## Functions

Functions are methods available for calling on the class

[startMove](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#function-startMove)
Begin moving splitter.

[endMove](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#function-endMove)
Stop moving splitter.

[updateMove](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#function-updateMove)
Update splitter position.

[onElementPointerDown](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#function-onElementPointerDown)
Start moving splitter on mouse down (on splitter).

[onPointerMove](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#function-onPointerMove)
Move splitter on mouse move.

[toggleTouchSplitter](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#function-toggleTouchSplitter)
Adds b-touching CSS class to splitterElements when touched. Removes when touched outside.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[splitterDragStart](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#event-splitterDragStart)
Fired by the Grid when a sub-grid resize gesture starts

[splitterDragEnd](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#event-splitterDragEnd)
Fired by the Grid after a sub-grid has been resized using the splitter

[splitterCollapseClick](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#event-splitterCollapseClick)
Fired by the Grid when the collapse icon is clicked. Return `false` to prevent the default collapse action, if you want to implement your own behavior.

[splitterExpandClick](https://bryntum.com/docs/gantt/api/Grid/feature/RegionResize#event-splitterExpandClick)
Fired by the Grid when the expand icon is clicked. Return `false` to prevent the default expand action, if you want to implement your own behavior.
