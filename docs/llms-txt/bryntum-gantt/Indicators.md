# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/Indicators.md

# [Indicators](https://bryntum.com/docs/gantt/api/Gantt/feature/Indicators)

The Indicators feature displays indicators (icons) for different dates related to a task in its row. Hovering an indicator will show a tooltip with its name and date(s). The owning task `id` is embedded in the indicator element dataset as `taskRecordId` which can be useful if you want to have custom actions when clicking (showing a menu for example).

By default, it includes and displays the following indicators (config name):

* Early start/end dates (earlyDates)
* Late start/end dates (lateDates)
* Constraint date (constraintDate)
* Deadline date (deadlineDate)

This demo shows the default indicators:

This config will display them all:

```
new Gantt({
  features : {
    indicators : true
  }
});
```

To selectively disable indicators:

```
features : {
  indicators : {
    items : {
      earlyDates     : false,
      constraintDate : false
    }
  }
}
```

They can also be toggled at runtime:

```
gantt.features.indicators.items.deadlineDate = true/false;
```

The feature also supports adding custom indicators, by adding properties to the `items` config object:

```
items : {
  lateDates  : false,

  // Custom indicator only shown for tasks more than half done
  myCustomIndicator : taskRecord => taskRecord.percentDone > 50 ? {
     startDate : DateHelper.add(taskRecord.endDate, 2, 'days'),
     name : 'My custom indicator',
     iconCls : 'fa fa-alien'
  } : null
}
```

This demo shows a custom indicator:

These custom indicators are defined as functions, that accept a task record and return a TimeSpan (or a raw data object). The function will be called for each visible task during rendering, to not show the indicator for certain tasks return `null` from it.

When using this feature we recommend that you configure gantt with a larger `rowHeight` + `barMargin` (>15 px), since the indicators are indented to fit below the task bars.

Note: When combined with the `fillTicks` mode, indicators are snapped to the time axis ticks.

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[items](https://bryntum.com/docs/gantt/api/Gantt/feature/Indicators#config-items)
Used to enable/disable built-in indicators and to define custom indicators.

Custom indicators are defined as functions, that accept a task record and return a [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan), or a config object thereof.

```
new Gantt({
  features : {
    indicators : {
      items : {
        // Disable deadlineDate indicators
        deadlineDate : false,

        // Add a custom indicator (called prepare)
        prepare : taskRecord => ({
           startDate : taskRecord.startDate,
           iconCls   : 'fa fa-magnify',
           name      : 'Start task preparations'
        })
      }
    }
  }
});
```

For more information, please see the class description at top.

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Gantt/feature/Indicators#config-tooltipTemplate)
A function which receives data about the indicator and returns a string, or a Promise yielding a string (for async tooltips), to be displayed in the tooltip. This method will be called with an object containing the fields below

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isIndicators](https://bryntum.com/docs/gantt/api/Gantt/feature/Indicators#property-isIndicators)
Identifies an object as an instance of [Indicators](https://bryntum.com/docs/gantt/api/#Gantt/feature/Indicators) class, or subclass thereof.

[isIndicators](https://bryntum.com/docs/gantt/api/Gantt/feature/Indicators#property-isIndicators-static)
Identifies an object as an instance of [Indicators](https://bryntum.com/docs/gantt/api/#Gantt/feature/Indicators) class, or subclass thereof.
