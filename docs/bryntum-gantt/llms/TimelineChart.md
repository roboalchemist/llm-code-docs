# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TimelineChart.md

# [TimelineChart](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart)

This feature allows drawing line charts on top of the timeline area. Feature consists of two parts: chart and data providers. Chart provider is responsible for rendering the chart, while data provider is responsible for providing data for the chart. Feature itself manages the interaction between them, and tracks lifecycle events of the Gantt chart.

Default implementation uses [SVGChartProvider](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/SVGChartProvider) for rendering the chart using SVG elements, and [GanttDataProvider](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/GanttDataProvider) as a data source. Those can be replaced and customized by setting the `chartProviderClass` and `dataProviderClass` configs. Custom implementation should subclass corresponding base classes: [TimelineChartProviderBase](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/TimelineChartProviderBase), [TimelineChartDataProviderBase](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/TimelineChartDataProviderBase) and implement required methods.

For more information on how to create custom chart provider, see [this guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/customization/scurve.md).

Feature will track timeline element resize and scroll and notify the chart provider about them. Chart element normally would be repositioned vertically to always stay in the view. And horizontally it will be scrollable along with the timeline.

Feature will also track project model and time axis view model changes to request data for the chart from the data provider and pass it to the chart provider for rendering.

Simple usage example:

```
// Simple configuration
const gantt = new Gantt({
    features : {
        timelineChart : true
    }
});
```

Chart and data providers can be configured separately.

```
const gantt = new Gantt({
    features : {
        timelineChart : {
            chartConfig : {
                tooltipTemplate : function({ dataset, date }) {
                    return `
                        <div>${dataset.label}: ${DateHelper.as('d', parseInt(dataset.value))} days</div>
                        <div>${DateHelper.format(date, this.gantt.displayDateFormat)}</div>
                    `;
                }
            },
            dataProviderConfig : {
                defaultDataset : 'progress'
            }
        }
    }
});
```

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[chartProviderClass](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#config-chartProviderClass)
Class providing chart rendering functionality.

[dataProviderClass](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#config-dataProviderClass)
Class providing data for the chart.

[chartProvider](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#config-chartProvider)
Configuration for the chart provider.

[dataProvider](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#config-dataProvider)
Configuration for the data provider.

[selectedDatasets](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#config-selectedDatasets)
Datasets to be displayed on the chart. Available datasets should be returned by the [datasets](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/TimelineChartDataProviderBase#property-datasets) accessor of the data provider. Changing this property will trigger chart repaint with the new dataset. Set to empty array to not draw anything.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineChart](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#property-isTimelineChart)
Identifies an object as an instance of [TimelineChart](https://bryntum.com/docs/gantt/api/#Gantt/feature/TimelineChart) class, or subclass thereof.

[isTimelineChart](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#property-isTimelineChart-static)
Identifies an object as an instance of [TimelineChart](https://bryntum.com/docs/gantt/api/#Gantt/feature/TimelineChart) class, or subclass thereof.

[selectedDatasets](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#property-selectedDatasets)
Datasets to be displayed on the chart. Available datasets should be returned by the [datasets](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/TimelineChartDataProviderBase#property-datasets) accessor of the data provider. Changing this property will trigger chart repaint with the new dataset. Set to empty array to not draw anything.

[datasets](https://bryntum.com/docs/gantt/api/Gantt/feature/TimelineChart#property-datasets)
Returns metadata for datasets available in the data provider.
