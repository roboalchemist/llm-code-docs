# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Charts.md

# [Charts](https://bryntum.com/docs/gantt/api/Grid/feature/Charts)

Adds interactive charting to a Grid. [Charts](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart) can be created from a selection of Grid data and updated in realtime as data changes. Supports many common chart types with extensive styling and customization options.

A context menu item `New Chart` is added that opens a popup containing a [ChartDesigner](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner) using the data in the grid's current selection.

For an explanation of the various options available in the editor popup, see [Chart](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart).

This feature is **disabled** by default.

```
const grid = new Grid({
    features : {
        charts : true
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[popup](https://bryntum.com/docs/gantt/api/Grid/feature/Charts#config-popup)
(Optional) Configuration options to provide to the [Popup](https://bryntum.com/docs/gantt/api/#Core/widget/Popup).

[chartDesigner](https://bryntum.com/docs/gantt/api/Grid/feature/Charts#config-chartDesigner)
(Optional) Configuration options to provide to the [ChartDesigner](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner)

[minimal](https://bryntum.com/docs/gantt/api/Grid/feature/Charts#config-minimal)
Whether to display in minimal mode, where popup title is hidden, chart preview occupies full area, and settings panel is minimized. Setting this to `true` also sets `minimal : true` on the child [ChartDesigner](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCharts](https://bryntum.com/docs/gantt/api/Grid/feature/Charts#property-isCharts)
Identifies an object as an instance of [Charts](https://bryntum.com/docs/gantt/api/#Grid/feature/Charts) class, or subclass thereof.

[isCharts](https://bryntum.com/docs/gantt/api/Grid/feature/Charts#property-isCharts-static)
Identifies an object as an instance of [Charts](https://bryntum.com/docs/gantt/api/#Grid/feature/Charts) class, or subclass thereof.

[minimal](https://bryntum.com/docs/gantt/api/Grid/feature/Charts#property-minimal)
Whether to display in minimal mode, where popup title is hidden, chart preview occupies full area, and settings panel is minimized. Setting this to `true` also sets `minimal : true` on the child [ChartDesigner](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner).

## Functions

Functions are methods available for calling on the class

[openPopup](https://bryntum.com/docs/gantt/api/Grid/feature/Charts#function-openPopup)
Open the chart designer popup with the current Grid selection as data source.
