# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/customization/scurve.md

# Using Timeline Chart feature

[Timeline Chart feature](#Gantt/feature/TimelineChart) allows drawing charts over the time axis view. Default
implementation includes 2 datasets and an SVG canvas. In this guide we show how to extend default list of datasets with
a custom one.

## Custom dataset

To configure a custom data set using the Timeline Chart feature in Gantt, follow these steps:

### Step 1: Initialize Gantt with Timeline Chart Feature

First, initialize the Gantt chart with the `timelineChart` feature enabled.

```javascript
new Gantt({
    features : {
        timelineChart : {
            // Configuration object for the data provider
            dataProvider : {}
        }
    }
});
```

### Step 2: Configure Meta Information for Data Series

Next, configure the meta information for the data series. You can override the default series or add new ones.

```javascript
new Gantt({
    features : {
        timelineChart : {
            dataProvider : {
                meta : {
                    // Override color of the default data series
                    duration : {
                        color : 'green'
                    },
                    // Add new series
                    customSeries : {
                        text : 'Custom Series',
                        color : '#00FF00',
                        callback : (task, start, end, durationDoneToDate, doneDuration, durationInInterval) => {
                            // Custom calculation logic
                            return someCustomCalculation(task, start, end, durationDoneToDate, doneDuration, durationInInterval);
                        }
                    }
                }
            }
        }
    }
});
```

### Step 3: Implement Custom Calculation Logic

Implement the custom calculation logic in the `callback` function. This function should return the calculated value for
the custom data series. In this case we return effort for all the tasks in the given time span.

```javascript
function someCustomCalculation(task, start, end, durationDoneToDate, doneDuration, durationInInterval) {
    // Example custom calculation
    if (durationInInterval > 0) {
        return Math.round(
            DateHelper.as('ms', task.customField, task.customUnit) *
            (durationInInterval / task.durationMS)
        );
    }
    return 0;
}
```

## Complete Example

Here is the complete example of configuring a custom data set using the Timeline Chart feature:

```javascript
new Gantt({
    features : {
        timelineChart : {
            dataProvider : {
                meta : {
                    duration : {
                        color : 'green'
                    },
                    customSeries : {
                        text : 'Custom Series',
                        color : '#00FF00',
                        callback : (task, start, end, durationDoneToDate, doneDuration, durationInInterval) => {
                            return someCustomCalculation(task, start, end, durationDoneToDate, doneDuration, durationInInterval);
                        }
                    }
                }
            }
        }
    }
});

function someCustomCalculation(task, start, end, durationDoneToDate, doneDuration, durationInInterval) {
    if (durationInInterval > 0) {
        return Math.round(
            DateHelper.as('ms', task.customField, task.customUnit) *
            (durationInInterval / task.durationMS)
        );
    }
    return 0;
}
```
