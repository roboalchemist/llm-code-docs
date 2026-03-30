# Source: https://docs.startree.ai/thirdeye/how-tos/alert/derived-metric-alert.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Derived Metric Alerts

ThirdEye supports monitoring derived metrics. [StarTree templates](/thirdeye/how-tos/alert/use-templates#install-startree-templates) are directly compatible with derived metrics, but a piece of configuration is required for root-cause analysis (RCA) to work.

Here is an example of monitoring the 95th percentile of the difference of 2 metrics `met1` and `met2`, with the `startree-threshold-percentile` template:

<Info>
  You must have StarTree templates [installed and up to date](/thirdeye/how-tos/alert/use-templates#install-startree-templates) to use this template.
</Info>

## Configuration

```json  theme={null}
{
  "name": "derived-metric-95-percentile-threshold",
  "description": "Monitor 95th percentile of met1-met2 with threshold alert.",
  "template": {
    "name": "startree-threshold-percentile"
  },
  "templateProperties": {
    "dataSource": "yourDatasource",
    "dataset": "yourDataset",
    "monitoringGranularity": "P1D",
    "min": "1000",
    "max": "2500",
    "aggregationFunction": "PERCENTILETDIGEST",
    "aggregationParameter": "95",
    "aggregationColumn": "met2-met1",
    "rcaAggregationFunction": "PCT95"
  },
  "cron": "0 0 0 1/1 * ? *"
}
```

*derived\_metric\_percentile\_threshold\_monitoring.json*

Notes:

* `aggregationFunction` calls the Pinot [PERCENTILETDIGEST](https://docs.pinot.apache.org/configuration-reference/functions/percentiletdigest) function
* `aggregationParameter` is the second parameter of the function. It sets the percentile to 95.
* `aggregationColumn` contains the derived metric.
* `rcaAggregationFunction` sets the RCA aggregation function. It binds to `aggregationFunction` in the alert configuration. `PCT95` corresponds to 95th percentile.
  The set of aggregation functions is limited. For more details, see [Aggregation functions](/thirdeye/rca-aggregation-functions).
  **RCA will not work without this configuration**. It is necessary because the derived metric is not registered in ThirdEye, so no default aggregation function is available.

Built with [Mintlify](https://mintlify.com).
