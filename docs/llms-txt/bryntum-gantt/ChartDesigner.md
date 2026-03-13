# Source: https://bryntum.com/products/gantt/docs-llm/api/Chart/widget/ChartDesigner.md

# [ChartDesigner](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner)

Provides a settings panel to configure a [Chart](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart), with a live preview.

Requires one or more data [series](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner#config-series) to be configured, as well as one or more [data objects](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner#config-data) to provide data for the preview. See [Chart](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart) for details on chart setup.

The designer is organized into three tabs:

* **Layout**: Choose the major chart type (line, bar, etc.) and chart components (title, legend).
* **Data**: Specify which data series will be used in the chart, and how.
* **Appearance**: Customize the look and feel of various chart components, including colors, fonts, and spacing.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[slider](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-slider)
Optional configuration for the [Slider](https://bryntum.com/docs/gantt/api/#Core/widget/Slider).

[field](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-field)
Optional configuration for the [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField).

[chartTitle](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-chartTitle)
Get/set the [title](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-title).

[chartSubtitle](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-chartSubtitle)
Get/set the [subtitle](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-subtitle).

[series](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-series)
The available series that can be chosen as the data [series](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-series) for the chart.

[data](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-data)
The sample data to use as data in the chart preview.

[selectedSeriesIds](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-selectedSeriesIds)
The currently selected series IDs (field names) for inclusion in the chart. See [series](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-series).

[labelsSeriesOptions](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-labelsSeriesOptions)
The available series (drawn from [series](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner#config-series)) that can be chosen as the [labels](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-labels) series.

[selectedLabelsSeriesId](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-selectedLabelsSeriesId)
The series ID (field name) of the series currently selected for use as the [labels](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-labels) series.

[chartType](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-chartType)
Get/set which predefined chart type is selected in the designer. Options include all types in [chartType](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-chartType) and additional pre-configured subtypes such as `lineWithPoints` and `barHorizontal`.

[fontFamilies](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-fontFamilies)
Set the font families available for selection.

[minimal](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#config-minimal)
Whether to display in minimal mode, where chart preview occupies full area and settings panel is minimized.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChartDesigner](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-isChartDesigner)
Identifies an object as an instance of [ChartDesigner](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner) class, or subclass thereof.

[isChartDesigner](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-isChartDesigner-static)
Identifies an object as an instance of [ChartDesigner](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner) class, or subclass thereof.

[slider](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-slider)
Optional configuration for the [Slider](https://bryntum.com/docs/gantt/api/#Core/widget/Slider).

[field](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-field)
Optional configuration for the [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField).

[chartTitle](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-chartTitle)
Get/set the [title](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-title).

[chartSubtitle](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-chartSubtitle)
Get/set the [subtitle](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-subtitle).

[series](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-series)
The available series that can be chosen as the data [series](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-series) for the chart.

[data](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-data)
The sample data to use as data in the chart preview.

[selectedSeriesIds](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-selectedSeriesIds)
The currently selected series IDs (field names) for inclusion in the chart. See [series](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-series).

[labelsSeriesOptions](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-labelsSeriesOptions)
The available series (drawn from [series](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner#config-series)) that can be chosen as the [labels](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-labels) series.

[selectedLabelsSeriesId](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-selectedLabelsSeriesId)
The series ID (field name) of the series currently selected for use as the [labels](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-labels) series.

[chartType](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-chartType)
Get/set which predefined chart type is selected in the designer. Options include all types in [chartType](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-chartType) and additional pre-configured subtypes such as `lineWithPoints` and `barHorizontal`.

[fontFamilies](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-fontFamilies)
Set the font families available for selection.

[minimal](https://bryntum.com/docs/gantt/api/Chart/widget/ChartDesigner#property-minimal)
Whether to display in minimal mode, where chart preview occupies full area and settings panel is minimized.
