# Source: https://docs.startree.ai/thirdeye/operators/data-fetcher.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# DataFetcher

Fetches data from a datasource.

## Inputs

None.

## Outputs

One output. No naming constraint for `outputKey` and `outputName`.

## Parameters

| name                   | description                                            | default value |
| ---------------------- | ------------------------------------------------------ | ------------- |
| `component.dataSource` | ThirdEye datasource to use.                            |               |
| `component.query`      | Query to execute. The query can use [macros](#macros). |               |

## Example

```json  theme={null}
{
  "name": "currentDataFetcher",
  "type": "DataFetcher",
  "params": {
    "component.dataSource": "pinot",     # ThirdEye datasource
    "component.query": "SELECT __timeGroup(timeColumn, 'EPOCH', 'P1D') as ts, sum(views) as met FROM pageviews WHERE __timeFilter(timeColumn, 'EPOCH') GROUP BY ts ORDER BY ts LIMIT 10000"
  },
  "inputs": [],
  "outputs": [
    {
      "outputKey": "currentData",        # no constraint
      "outputName": "currentOutput"      # no constraint
    }
  ]
}
```

## Macros

Macros are special functions that are translated by ThirdEye to SQL before the query is sent to the database. Macros have access to detection runtime information, like the start and the end time of the detection, the timezone.

| Macro example                                                                                                    | description                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `__timeFilter(`  `timeColumn,`   `'timeFormat'`  `)`                                                             | Replaced by a time range filter on the timeframe   `[detectionStart, detectionEnd[`   using the specified column name and the specified timeFormat.   For example,   `__timeFilter(timeColumn, 'EPOCH_MILLIS')`   is replaced by   `timeColumn >= 1494410242000 AND timeColumn < 1494410242000)`                                                                                |
| `__timeFilter(`  `timeColumn,`   `'timeFormat,'`   `'lookbackFromStartPeriod'`  `)`                              | Replaced by a time range filter on the timeframe   `[detectionStart-lookbackFromStartPeriod, detectionEnd[`.   For example, for a detection between January 14 and January 15,   `__timeFilter(timeColumn, 'yyyyMMdd', 'P7D')`   is replaced by   `timeColumn >= '20220107' AND timeColumn < '20220115')`                                                                       |
| `__timeFilter(`  `timeColumn,`   `'timeFormat,'`   `'lookbackFromStartPeriod,'`   `'lookbackFromEndPeriod'`  `)` | Replaced by a time range filter on the timeframe   `[detectionStart-lookbackFromStartPeriod, detectionEnd-lookbackFromEndPeriod[`.   For example, for a detection between January 14 and January 15,   `__timeFilter(timeColumn, 'yyyyMMdd', 'P7D', 'P7D')`   is replaced by   `timeColumn >= '20220107' AND timeColumn < '20220108')`                                          |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |
| `__timeGroup(`  `timeColumn,`   `'timeFormat',`   `'granularity'`  `)`                                           | Replaced by a transformation of the timeColumn in bins of the given granularity, in milliseconds.   Respects the [timezone](/thirdeye/alert-configuration#timezone) of the alert.   For example,   `__timeGroup(timeColumn, 'yyyyMMddhh', 'P1D')`    is replaced by    `DATETIMECONVERT(timeColumn, '1:DAYS:SIMPLE_DATE_FORMAT:yyyyMMddhh', '1:MILLISECONDS:EPOCH', '1:DAYS')` |

### AUTO keyword

If the `timeColumn` value is `AUTO`, the macro resolves to the primary time column of the table.\
`timeFormat` is obtained internally and can be left blank.

For example:

* `__timeFilter(AUTO,'')`
* `__timeGroup(AUTO,'','P1D')`

### timeFormat strings

Available timeformat strings are:

| String                      | description                                                                                                                                                  | aliases                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| `EPOCH_MILLIS`              | time column is in milliseconds since [unix epoch](https://en.wikipedia.org/wiki/Unix_time)                                                                   | `1:MILLISECONDS:EPOCH`                           |
| `EPOCH`                     | time column is in seconds since unix epoch                                                                                                                   | `1:SECONDS:EPOCH`                                |
| `EPOCH_MINUTES`             | time column is in minutes since unix epoch                                                                                                                   | `1:MINUTES:EPOCH`                                |
| `EPOCH_HOURS`               | time column is in hours since unix epoch                                                                                                                     | `1:HOURS:EPOCH`                                  |
| `EPOCH_DAYS`                | time column is in days since unix epoch                                                                                                                      | `1:DAYS:EPOCH`                                   |
| any SimpleDateFormat string | See [SimpleDateFormat documentation](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html). Eg `yyyyMMdd`, `yyyy-MM-dd'T'HH:mm:ss.SSSZ` | `1:DAYS:SIMPLE_DATE_FORMAT:[SIMPLE_DATE_FORMAT]` |

### period strings

Period strings uses the [ISO-8601 format](https://en.wikipedia.org/wiki/ISO_8601#Durations). Examples:

* `'P7D'`: 7 days
* `'PT1H'`: 1 hour

Built with [Mintlify](https://mintlify.com).
