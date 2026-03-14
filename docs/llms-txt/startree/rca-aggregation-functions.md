# Source: https://docs.startree.ai/thirdeye/rca-aggregation-functions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Aggregation Functions

Unlike the detection pipeline, root cause analysis (RCA) algorithms have a limited set of aggregation functions available.

If the [metric used for RCA](/thirdeye/alert-configuration) is onboarded in ThirdEye, a default aggregation function is available. If the metric is a derived metric or is not onboarded in ThirdEye, the aggregation function should be set in the alert configuration [aggregationFunction](/thirdeye/alert-configuration#aggregationfunction) field.

## Available aggregation functions

| name             | description                   |
| ---------------- | ----------------------------- |
| `SUM`            | Sum of the metric             |
| `AVG`            | Average of the metric         |
| `COUNT`          | Count of the lines            |
| `COUNT_DISTINCT` | Distinct count of the lines   |
| `MAX`            | Maximum of the metric         |
| `MIN`            | Minimum of the metric         |
| `PCT50`          | 50th percentile of the metric |
| `PCT90`          | 90th percentile of the metric |
| `PCT95`          | 95th percentile of the metric |
| `PCT99`          | 99th percentile of the metric |

See [source code](https://github.com/startreedata/thirdeye/blob/master/thirdeye-spi/src/main/java/ai/startree/thirdeye/spi/metric/MetricAggFunction.java).

## Datasource compatibility

Some datasources may not be compatible with all aggregation functions.

#### Compatibility matrix

| function         | [Pinot](https://github.com/startreedata/thirdeye/blob/f987a621e4fd23a41d13671ca82b26d12f751a7f/thirdeye-plugins/thirdeye-pinot/src/main/java/ai/startree/thirdeye/plugins/datasource/pinot/PinotSqlExpressionBuilder.java#L179) |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SUM`            | YES                                                                                                                                                                                                                             |
| `AVG`            | YES                                                                                                                                                                                                                             |
| `COUNT`          | YES                                                                                                                                                                                                                             |
| `COUNT_DISTINCT` | YES                                                                                                                                                                                                                             |
| `MAX`            | YES                                                                                                                                                                                                                             |
| `MIN`            | YES                                                                                                                                                                                                                             |
| `PCT50`          | YES                                                                                                                                                                                                                             |
| `PCT90`          | YES                                                                                                                                                                                                                             |
| `PCT95`          | YES                                                                                                                                                                                                                             |
| `PCT99`          | YES                                                                                                                                                                                                                             |

Built with [Mintlify](https://mintlify.com).
