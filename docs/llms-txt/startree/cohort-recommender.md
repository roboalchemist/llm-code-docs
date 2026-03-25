# Source: https://docs.startree.ai/thirdeye/cohort-recommender.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ThirdEye Dimensions Recommender

The ThirdEye dimensions recommender uses an API call to recommend a list of dimensions which are metrics drivers.

## Problem Context

Working with a large dataset containing various metrics (measurements) and dimensions (categories that classify the data).  Understanding what factors most influence your metrics can be challenging.  For example, one might want to know which user demographics (country, device type) have the biggest impact on website pageviews.

## Use Case

The ThirdEye Dimensions Recommender is a tool that helps you identify the key dimensions driving a specific metric.  This can be valuable for:

* Optimizing marketing campaigns: See which demographics or channels contribute most to conversions.
* Troubleshooting performance issues: Identify dimensions associated with unexpected dips or spikes in metrics.
* Understanding user behavior: Discover which user segments have the most significant influence on key metrics.

## Example

Analyze website traffic. One wants to know which user characteristics (dimensions) most affect total pageviews (metric). Here's how to use the ThirdEye Dimensions Recommender:

* Metric Selection: Specify the metric you want to analyze, for example, by providing its ID or name (e.g., "pageviews").
* Filtering: Define a timeframe (start and end date) for the analysis. You can optionally set a threshold (minimum metric value) or a percentage contribution for the dimensions you're interested in.
* Additional Criteria: You can add a "where" clause to filter data based on specific dimension values (e.g., only users from the US) or a "having" clause to filter based on the number of data points (e.g., only dimensions with over 1 million rows).
  Customization:
* Max Depth: Set the maximum number of dimensions the recommender should consider when identifying contributing factors (e.g., country, device, browser version).
* Limit: Specify the maximum number of top recommendations to return for each dimension combination.
* Run the Analysis: The API will return a list of dimensions that significantly impact your chosen metric within the specified timeframe and criteria.

<br />

<img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/DIMENSIONRECOMMEND.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=a813117ffb503440f5e6187f469a0596" width="80%" data-path="img/thirdeye/DIMENSIONRECOMMEND.png" />

## API reference

The recommender API is accessible at `/api/rca/metrics/cohorts`.

Here's an example:

```http  theme={null}
POST https://thirdeye.yournamespace.domain.com/api/rca/metrics/cohorts
accept: application/json
```

This endpoint accepts a JSON payload and can be leveraged using the following parameters.

### Parameters

| Name                            | Description                                                                                                                                                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start                           | The starting time in epoch milliseconds (millis). Example: 1623110400000 means Tue Jun 08 2021 00:00:00 UTC                                                                                                                                 |
| end                             | The end time in epoch millis . Example: 1623283200000 means Thu Jun 10 2021 00:00:00 UTC                                                                                                                                                    |
| threshold                       | Exact value of metric. Dimensions Recommender which contribute more than this will be included.                                                                                                                                             |
| percentage                      | If threshold is not provided, then percentage is used. Example: setting percentage to 10 means that threshold = 10% of overall aggregate.                                                                                                   |
| generateEnumerationItems (beta) | If set to true, ThirdEye will also try to generate the list of enumeration items in addition to dimensions recommender                                                                                                                      |
| where                           | This is an additional where clause that can be added to the query in the form of a SQL expression. Example:  `""where": "country LIKE 'US%' AND \"device\" = 'phone'""`                                                                     |
| having                          | Similar to where, having clause is a SQL expression that can be added to the query. Example: `"COUNT(*) > 1000000"`                                                                                                                         |
| maxDepth                        | The max depth in dimensions that the recommendation engine will dive to. Example: maxDepth = 3 means all dimensions reported will have a max of 3 dimensions. like `country = 'US', device = 'phone', version='0.3.0'`. Default value is 10 |
| dimensions                      | If set, this is the list of dimensions that the dimensions recommender will iterate through. Example: if the dataset has 5 dimensions and  `"dimensions": ["country", "device"]`. ThirdEye will only iterate on these 2 dimensions         |
| limit                           | If set, this behaves like top N. The number of results are trimmed to limit and the results are sorted in descending order by contribution. The default value is 100                                                                        |

#### Metric

A metric can be mentioned in multiple ways in the API.

#### Using ID

```json  theme={null}
{
  "metric": {
    "id": 12746
  }
}
```

#### Using name

```json  theme={null}
{
  "metric": {
    "name": "pageviews"
  }
}
```

#### Specifying the column name, aggregation function and table name

```json  theme={null}
{
  "metric": {
    "aggregationColumn": "views",
    "aggregationFunction": "SUM",
    "dataset": {
      "name": "pageviews"
    }
  }
}
```

## Payload examples

Return recommended dimensions with more than 10% contribution to the overall metric having more than n rows in a given timeframe.

```json  theme={null}
{
  "metric": {
    "aggregationColumn": "views",
    "aggregationFunction": "SUM",
    "dataset": {
      "name": "pageviews"
    }
  },
  "percentage": 10,
  "having": "COUNT(*) > 1000000",
  "start": "1623110400000",
  "end": "1623283200000"
}
```

Return recommended dimensions that are above 40k page views showing only the top 5 for every dimension combination.

```json  theme={null}
{
  "metric": {
    "id": 12746
  },
  "threshold": 400000,
  "maxDepth": 3,
  "limit": 5,
  "start": "1623110400000",
  "end": "1623283200000"
}
```

Built with [Mintlify](https://mintlify.com).
