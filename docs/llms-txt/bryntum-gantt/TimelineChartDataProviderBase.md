# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/util/chart/TimelineChartDataProviderBase.md

# [TimelineChartDataProviderBase](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase)

Interface for chart data provider.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[defaultDataset](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#config-defaultDataset)
Default dataset to show.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineChartDataProviderBase](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#property-isTimelineChartDataProviderBase)
Identifies an object as an instance of [TimelineChartDataProviderBase](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/TimelineChartDataProviderBase) class, or subclass thereof.

[isTimelineChartDataProviderBase](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#property-isTimelineChartDataProviderBase-static)
Identifies an object as an instance of [TimelineChartDataProviderBase](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/TimelineChartDataProviderBase) class, or subclass thereof.

[datasets](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#property-datasets)
Returns list of supported datasets.

## Functions

Functions are methods available for calling on the class

[getDataset](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#function-getDataset)
Returns dataset for the chart

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[refresh](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#event-refresh)
[TimelineChart](https://bryntum.com/docs/gantt/api/#Gantt/feature/TimelineChart) listens to this event to refresh the chart. Trigger this event if data is changed from within the data provider.

## Typedefs

Typedefs are type definitions for the class

[TimelineChartViewConfig](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#typedef-TimelineChartViewConfig)
Timeline view parameters

[TimelineChartLineData](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#typedef-TimelineChartLineData)
Defines line points. Line point is measured from the top left corner of the SVG canvas. Actual position should be determined by the chart provider.

[TimelineChartDataset](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#typedef-TimelineChartDataset)
Dataset for the chart

[DatasetMetaData](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartDataProviderBase#typedef-DatasetMetaData)
Data series meta data
