# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/util/chart/SVGChartProvider.md

# [SVGChartProvider](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider)

Implementation of the chart provider using SVG elements.

It will draw SVG path with optional dots for each dataset and axis lines. Axis lines could be drawn across entire chart area or only on the left side. Distance between axis lines is calculated based on the chart height.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showAxisLines](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#config-showAxisLines)
When `true`, axis lines will be drawn across entire chart area.

[showLineDetails](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#config-showLineDetails)
When `true`, points on the chart path will be shown separately.

[minAxisTickDistance](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#config-minAxisTickDistance)
Defines minimum distance in pixels between two axis lines. Based on this value chart will calculate how many lines to draw. See corresponding config [axisTicksCount](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/SVGChartProvider#config-axisTicksCount).

[axisTicksCount](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#config-axisTicksCount)
Defines zoom levels for chart axis lines. By default, axis is split into 10 sections. When lines are closer than [minAxisTickDistance](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/SVGChartProvider#config-minAxisTickDistance) next zoom level will be used. Default values are \[10, 5, 4, 2, 1\] which mean "draw line every 10% of the axis, if too close, then every 20%, 25%, 50% and 100% of the axis".

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSVGChartProvider](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#property-isSVGChartProvider)
Identifies an object as an instance of [SVGChartProvider](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/SVGChartProvider) class, or subclass thereof.

[isSVGChartProvider](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#property-isSVGChartProvider-static)
Identifies an object as an instance of [SVGChartProvider](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/SVGChartProvider) class, or subclass thereof.

[showAxisLines](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#property-showAxisLines)
When `true`, axis lines will be drawn across entire chart area.

[showLineDetails](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#property-showLineDetails)
When `true`, points on the chart path will be shown separately.

[minAxisTickDistance](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#property-minAxisTickDistance)
Defines minimum distance in pixels between two axis lines. Based on this value chart will calculate how many lines to draw. See corresponding config [axisTicksCount](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/SVGChartProvider#config-axisTicksCount).

[axisTicksCount](https://bryntum.com/docs/gantt/api/Gantt/util/chart/SVGChartProvider#property-axisTicksCount)
Defines zoom levels for chart axis lines. By default, axis is split into 10 sections. When lines are closer than [minAxisTickDistance](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/SVGChartProvider#config-minAxisTickDistance) next zoom level will be used. Default values are \[10, 5, 4, 2, 1\] which mean "draw line every 10% of the axis, if too close, then every 20%, 25%, 50% and 100% of the axis".
