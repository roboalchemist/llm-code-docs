# Source: https://docs.startree.ai/thirdeye/how-tos/manage-holiday-effect.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Holiday Effects with StarTree ETS

Some StarTree ThirdEye models can learn the impact of special events like holidays. Here is an example configuration.

```json  theme={null}
{  
"name": "pageviews-ets-with-holiday",  
"description": "",  
"template": {  
 "name": "startree-ets"  
 },  
"templateProperties": {  
 "dataSource": "pinot",  
 "dataset": "pageviews",  
 "aggregationFunction": "sum",  
 "seasonalityPeriod": "P7D",  
 "lookback": "P90D",  
 "monitoringGranularity": "P1D",  
 "sensitivity": "3",  
 "aggregationColumn": "views",  
 "eventSqlFilter": "'US' member of dimensionMap['countryCode']", 
 "eventTypes": [
  "HOLIDAY" 
  ]
 },  
"cron": "0 0 5 ? * * *"  
}
```

*pageviews\_ets\_holiday.json*

The `eventSqlFilter` and `eventTypes` are described [here](/thirdeye/operators/event-fetcher).

### Compatible templates

```
startree-ets
startree-ets-percentile
```

For templates that cannot learn the effect of holidays, it is possible to use a filter to ignore anomalies that happen during special events.\
Use the optional parameters:

```json  theme={null}
{
  ...
  "templateProperties": {
    "eventFilterIgnore": true,
    "eventFilterSqlFilter": "",
    "eventFilterTypes": [],
    "eventFilterBeforeHolidayMargin": "P0D",
    "eventFilterAfterHolidayMargin": "P0D"  
  }
}
```

Built with [Mintlify](https://mintlify.com).
