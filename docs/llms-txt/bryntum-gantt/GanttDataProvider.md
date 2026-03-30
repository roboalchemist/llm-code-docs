# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/util/chart/GanttDataProvider.md

# [GanttDataProvider](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider)

Data source for the timeline chart

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[defaultDataset](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#config-defaultDataset)
Default dataset to show.

[unit](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#config-unit)
Defines intervals to fill date map. One day by default.

[meta](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#config-meta)
This object configures available data series, metadata and a function to calculate the values. Every key is a dataset name, and every value is an [SeriesMetaData](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/GanttDataProvider#typedef-SeriesMetaData) object with the following properties:

* text - the text to display in the legend
* total - the total value of the series
* color - the color of the series
* callback - the function to calculate the value of the series

```
// Metadata object example
duration : {
    text : 'Duration',
    total : 0,
    color : '#CC0033',
    callback : this.prototype.getTaskDuration
}
```

### Color

Color is an optional parameter. If not provided, the default color will be used. Series color can be styles with CSS using attribute selector:

```
.b-timeline-overlay-chart path[data-series="name"] { stroke: #FF0000; }
.b-timeline-overlay-chart circle[data-series="name"] { fill: #FF0000; }
```

### Callback

[Callback](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/GanttDataProvider#typedef-GanttDataProviderSeriesCallback) is used to generate series data. It is called for every leaf task for every interval, specified by [unit](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/GanttDataProvider#config-unit), between project start and end dates. For example, to calculate working time of the task in the given period:

```
new Gantt({
  features : {
    timelineChart : {
      dataProvider : {
        meta : {
          duration : {
            callback : (task, start, end) {
              // default implementation
              return task.effectiveCalendar.calculateDurationMs(start, end);
            }
          }
        }
      }
    }
  }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGanttDataProvider](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#property-isGanttDataProvider)
Identifies an object as an instance of [GanttDataProvider](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/GanttDataProvider) class, or subclass thereof.

[isGanttDataProvider](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#property-isGanttDataProvider-static)
Identifies an object as an instance of [GanttDataProvider](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/GanttDataProvider) class, or subclass thereof.

[unit](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#property-unit)
Defines intervals to fill date map. One day by default.

## Functions

Functions are methods available for calling on the class

[shouldReturnDataset](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#function-shouldReturnDataset)
Returns true if data should be provided with a given view config.

[getDataset](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#function-getDataset)
Returns dataset for the chart

## Typedefs

Typedefs are type definitions for the class

[GanttDataProviderSeriesCallback](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#typedef-GanttDataProviderSeriesCallback)

[SeriesMetaData](https://bryntum.com/docs/gantt/api/Gantt/util/chart/GanttDataProvider#typedef-SeriesMetaData)
