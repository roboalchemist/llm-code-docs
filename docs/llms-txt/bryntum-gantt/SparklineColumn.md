# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/SparklineColumn.md

# [SparklineColumn](https://bryntum.com/docs/gantt/api/Grid/column/SparklineColumn)

Displays a sparkline (a small inline chart that gives an at-a-glance view of trends in a data series) in a grid cell.

The column's [field](https://bryntum.com/docs/gantt/api/#Grid/column/SparklineColumn#config-field) should be a property on your Grid data model containing an array of numbers that make up the data series to display in the sparkline.

SparklineColumn supports [chartType](https://bryntum.com/docs/gantt/api/#Grid/column/SparklineColumn#config-chartType)s of `line`, `bar`, and `pie`.

```
new Grid({
    columns : [
        {
             type      : 'sparkline',
             chartType : 'line',
             field     : 'values' // field named here should contain
                                  // an array of numbers
        }
    ]
});
```

Note that this column requires using thin bundles or thin npm packages in your application, and importing the `chart` bundle / package. It does not work with normal packages, module or umd bundles.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[chartType](https://bryntum.com/docs/gantt/api/Grid/column/SparklineColumn#config-chartType)
The type of chart.

[highlightMinMax](https://bryntum.com/docs/gantt/api/Grid/column/SparklineColumn#config-highlightMinMax)
Whether to highlight the minimum and maximum values in [highlightColor](https://bryntum.com/docs/gantt/api/#Grid/column/SparklineColumn#config-highlightColor). Applicable for [chartType](https://bryntum.com/docs/gantt/api/#Grid/column/SparklineColumn#config-chartType)s `line` and `bar`.

[highlightColor](https://bryntum.com/docs/gantt/api/Grid/column/SparklineColumn#config-highlightColor)
The hex color to use to highlight the minimum and maximum values when [highlightMinMax](https://bryntum.com/docs/gantt/api/#Grid/column/SparklineColumn#config-highlightMinMax) is `true`. Applicable for [chartType](https://bryntum.com/docs/gantt/api/#Grid/column/SparklineColumn#config-chartType)s `line` and `bar`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSparklineColumn](https://bryntum.com/docs/gantt/api/Grid/column/SparklineColumn#property-isSparklineColumn)
Identifies an object as an instance of [SparklineColumn](https://bryntum.com/docs/gantt/api/#Grid/column/SparklineColumn) class, or subclass thereof.

[isSparklineColumn](https://bryntum.com/docs/gantt/api/Grid/column/SparklineColumn#property-isSparklineColumn-static)
Identifies an object as an instance of [SparklineColumn](https://bryntum.com/docs/gantt/api/#Grid/column/SparklineColumn) class, or subclass thereof.
