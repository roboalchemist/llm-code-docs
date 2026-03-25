# Source: https://docs.snowflake.com/en/sql-reference/functions/system_estimate_query_acceleration.md

Categories:
:   [System functions](../functions-system.md)

# SYSTEM$ESTIMATE_QUERY_ACCELERATION

For a previously executed query, this function returns a JSON object that specifies if the query is eligible to benefit from the
[query acceleration service](../../user-guide/query-acceleration-service.md). If the query is eligible for query acceleration, the output
includes the estimated query execution time for different query acceleration scale factors.

See also:
:   [QUERY_ACCELERATION_ELIGIBLE view](../account-usage/query_acceleration_eligible.md)

## Syntax

```sqlsyntax
SYSTEM$ESTIMATE_QUERY_ACCELERATION( '<query_id>' )
```

## Parameters

`query_id`
:   Query ID. Query ID must be for a query executed within the last 14 days; otherwise, the `status` is `invalid`.

## Output

The function returns a JSON object with the properties described below:

| Property | Description |
| --- | --- |
| `estimatedQueryTimes` | Object that contains the estimated query execution time in seconds for different query acceleration scale factors. If the `status` for the query is not `eligible` for query acceleration, this object is empty. |
| `ineligibleReason` | Explanation of why Snowflake didn’t use QAS for the query. For example, if the query doesn’t perform any table scans, or if it doesn’t scan a large enough amount of data to make QAS worthwhile, the reason is listed as `NO_LARGE_ENOUGH_SCAN`. |
| `originalQueryTime` | Execution time of the original query in seconds. |
| `queryUUID` | Query ID. |
| `status` | One of the following values that indicates whether or not the query is eligible to benefit from the query acceleration service:   |  |  | | --- | --- | | `eligible` | The query can benefit from query acceleration. | | `ineligible` | The query cannot benefit from query acceleration. | | `accelerated` | The query has already been accelerated. | | `invalid` | The query with the specified ID was not found. | |
| `upperLimitScaleFactor` | Number of the highest query acceleration scale factor in the `estimatedQueryTimes` object. If the `status` for the query is not `eligible` for query acceleration, this field is set to `0`. |

In the `estimatedQueryTimes` object, each name / value pair specifies a query acceleration [scale factor](../sql/create-warehouse.md) and the estimated query execution time at that scale factor.

The following example lists the estimated query execution time for the scale factors `1`, `2`, `4` and
`8`:

```sqljson
...
"estimatedQueryTimes" : {
  "1" : 171,
  "2": 152,
  "4": 133,
  "8": 120
}
...
```

## Usage notes

* Estimated query times are for analysis purposes only and are not guaranteed.
* Estimated query times are calculated based on the assumption that the query is serviced by all the compute resources allocated by the
  query acceleration service based on scale factor.
* Estimated query times do not factor in concurrency.

## Examples

For example queries, see [Identifying queries with the SYSTEM$ESTIMATE_QUERY_ACCELERATION function](../../user-guide/query-acceleration-service.md).
