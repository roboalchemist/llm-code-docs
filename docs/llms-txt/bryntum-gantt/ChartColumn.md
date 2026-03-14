# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/ChartColumn.md

# [ChartColumn](https://bryntum.com/docs/gantt/api/Grid/column/ChartColumn)

A column that displays a [Chart](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart) in each cell.

Records for the chart are provided by the `field` defined in the column configuration. Values will be read from that field on the grid record model for a given row. The value of the field should be an array of records of chart data, each containing the fields required by the `chart`'s defined `series` and `labels`.

By default, the chart will update when its `store` fires a `change` event. To disable auto-sync, set the `autoSync` property of the `chart` config to `false`.

```
new Grid({
    columns : [
        {
             type: 'chart',

             chart : {
                 chartType : 'line',
                 series : [{
                     field : 'price'
                 },{
                     field : 'changePct'
                 }],
                 labels : {
                     field : 'symbol'
                 }
             }
        }
    ]
});
```

Note that this column requires using thin bundles or thin npm packages in your application, and importing the `chart` bundle / package. It does not work with normal packages, module or umd bundles.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[chartCls](https://bryntum.com/docs/gantt/api/Grid/column/ChartColumn#config-chartCls)
CSS class name to add to chart.

[chart](https://bryntum.com/docs/gantt/api/Grid/column/ChartColumn#config-chart)
The [Chart](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart) widget configuration. Since charts are imported from a separate module, the chart class will be lazy loaded when this column is used.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChartColumn](https://bryntum.com/docs/gantt/api/Grid/column/ChartColumn#property-isChartColumn)
Identifies an object as an instance of [ChartColumn](https://bryntum.com/docs/gantt/api/#Grid/column/ChartColumn) class, or subclass thereof.

[isChartColumn](https://bryntum.com/docs/gantt/api/Grid/column/ChartColumn#property-isChartColumn-static)
Identifies an object as an instance of [ChartColumn](https://bryntum.com/docs/gantt/api/#Grid/column/ChartColumn) class, or subclass thereof.

[chart](https://bryntum.com/docs/gantt/api/Grid/column/ChartColumn#property-chart)
The [Chart](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart) widget configuration. Since charts are imported from a separate module, the chart class will be lazy loaded when this column is used.
