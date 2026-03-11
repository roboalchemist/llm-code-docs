# Source: https://docs.startree.ai/thirdeye/how-tos/alert-tuning.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Anomaly Filters to Tune Alerts

Anomaly filters enable you to tune your alerts for improved accuracy. Read [concepts - using Anomaly filters as part of post-processor](/thirdeye/operators/post-processor) for background information.

These filters can be defined during the alert creation. See [how to create alerts](/thirdeye/getting-started/create-your-first-alert) to learn more about alert creation.

The goal of anomaly filters is to reduce false alerts.

## Day of the week filter

This filter enables you to define the day of the week that will be used to filter anomalies to reduce false alarms. These days are usually known to be high volume or low volume.

```json  theme={null}
DaysOfWeek: ["MONDAY", "SATURDAY"],
HoursOfDay: [0,1,2,23],
DayHoursOfWeek: {"FRIDAY": [22, 23], "SATURDAY": [0, 1, 2]}
```

## Offsets filter

This filter enables you to define an offset to ignore anomalies during alert creation/configuration.

```json  theme={null}
Metric Name: "Business KPI", # customize label
Offsets: ["P7D", "P14D"], # parameter of the detector
Aggregation: "MEDIAN" # parameter of the detector
```

## Cold Start filter

Usually model predictions are impacted by low data volume in the beginning. This filter enables you to define from which day/time the model should start learning to predict anomalies accurately.

```json  theme={null}
coldStartPeriod": "P14D", # filter anomalies in the first 14 days of the dataset
tableName: "my_dataset"
```

## Events filter

This filter enables you to define specific holiday periods.

```json  theme={null}
BeforeHolidayMargin: "PT4H",
AfterHolidayMargin: "PT4H"
```

## Threshold filter

This filter enables you to  apply a threshold on the record volume.

```json  theme={null}
Min limit: "100",
Max limit": "10000000",
Metric Name: "controlMetric",   # customize label
Timestamp: "ts",                # time column of the side input
Threshold metric: "sideMetric"  # column to threshold on in the side input
```

## Time of the week filter

This filter enables you to specify day of the week and the time window during which the anomalies will be ignored.

```json  theme={null}
Days Of Week": ["MONDAY", "SATURDAY"],
Hours Of Day": [0,1,2,23],
Day Hours Of Week": {"FRIDAY": [22, 23], "SATURDAY": [0, 1, 2]}
```

Built with [Mintlify](https://mintlify.com).
