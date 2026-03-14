# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/util/chart/TimelineChartProviderBase.md

# [TimelineChartProviderBase](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartProviderBase)

This class provides a base API for the chart providers. Chart provider is responsible for actually drawing the canvas and the chart. It is provided with data and view details by the timeline chart feature.

Chart canvas (implemented by subclasses) will be sized according to the timeline size. Width will be equal to the time axis size and height - to the timeline subgrid height. Canvas will be scrollable in horizontal direction and will remain at the top of the timeline view on vertical scroll.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[chartVerticalMargin](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartProviderBase#config-chartVerticalMargin)
Defines vertical margins for the chart, set to 0 to fill entire view.

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartProviderBase#config-tooltipTemplate)
Template used to generate tooltip contents when chart point is hovered.

```
const gantt = new Gantt({
    features : {
        timelineChart : {
            chartProvider : {
                tooltipTemplate({ dataset, date }) {
                    return `
                        <div>${dataset.label}: ${dataset.percent}%</div>
                        <div>${DateHelper.format(date, this.gantt.displayDateFormat)}</div>
                    `;
                }
            }
        }
    }
});
```

[tooltip](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartProviderBase#config-tooltip)
Property allowing to customize the tooltip appearance.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineChartProviderBase](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartProviderBase#property-isTimelineChartProviderBase)
Identifies an object as an instance of [TimelineChartProviderBase](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/TimelineChartProviderBase) class, or subclass thereof.

[isTimelineChartProviderBase](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartProviderBase#property-isTimelineChartProviderBase-static)
Identifies an object as an instance of [TimelineChartProviderBase](https://bryntum.com/docs/gantt/api/#Gantt/util/chart/TimelineChartProviderBase) class, or subclass thereof.

[tooltip](https://bryntum.com/docs/gantt/api/Gantt/util/chart/TimelineChartProviderBase#property-tooltip)
Property allowing to customize the tooltip appearance.
