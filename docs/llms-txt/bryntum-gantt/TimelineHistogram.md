# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/TimelineHistogram.md

# [TimelineHistogram](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogram)

This view displays histograms for the provided store records.

A [ScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn) is also added automatically.

To create a standalone histogram, simply configure it with a [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) instance:

```
const store = new Store({
    data : [
        {
            id            : 'r1',
            name          : 'Record 1',
            // data used to render a histogram for this record
            histogramData : [
                { value1 : 200, value2 : 100 },
                { value1 : 150, value2 : 50 },
                { value1 : 175, value2 : 50 },
                { value1 : 175, value2 : 75 }
            ]
        },
        {
            id            : 'r2',
            name          : 'Record 2',
            // data used to render a histogram for this record
            histogramData : [
                { value1 : 100, value2 : 100 },
                { value1 : 150, value2 : 125 },
                { value1 : 175, value2 : 150 },
                { value1 : 175, value2 : 75 }
            ]
        }
    ]
});

const histogram = new TimelineHistogram({
    appendTo  : 'targetDiv',
    startDate : new Date(2022, 11, 26),
    endDate   : new Date(2022, 11, 30),
    store,
    // specify series displayed in the histogram
    series : {
        value1 : {
            type  : 'bar',
            field : 'value1'
        },
        value2 : {
            type  : 'bar',
            field : 'value2'
        }
    },
    columns : [
        {
            field : 'name',
            text  : 'Name'
        }
    ]
});
```

Providing histogram data
------------------------

There are two basic ways to provide histogram data:

* the data can be provided statically in a record field configured as [dataModelField](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogram#config-dataModelField):

```
const store = new Store({
    data : [
        {
            id   : 11,
            name : 'John Smith',
            // data used to render a histogram for this record
            hd   : [
                { weight : 200, price : 100 },
                { weight : 150, price : 105 },
                { weight : 175, price : 90 },
                { weight : 175, price : 95 }
            ]
        }
    ]
});

const histogram = new TimelineHistogram({
    dataModelField : 'hd',
    series : {
        weight : {
            type : 'bar'
        },
        price : {
            type : 'outline'
        }
    },
    ...
});
```

* the data can be collected dynamically with the provided [getRecordData](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogram#config-getRecordData) function:

```
const histogram = new TimelineHistogram({
    dataModelField : 'hd',
    series : {
        weight : {
            type : 'bar'
        },
        price : {
            type : 'outline'
        }
    },
    ...
    async getRecordData(record) {
        // we get record histogram data from the server
        const response = await fetch('https://some.url/to/get/data?' + new URLSearchParams({
            // pass the record identifier and the time span we need data for
            record    : record.id,
            startDate : DateHelper.format(this.startDate),
            endDate   : DateHelper.format(this.endDate),
        }));
        return response.json();
    }
});
```

Please check ["Timeline histogram" guide](https://bryntum.com/docs/gantt/api/#Scheduler/guides/timelinehistogram.md) for more details.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineHistogram](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogram#property-isTimelineHistogram)
Identifies an object as an instance of [TimelineHistogram](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogram) class, or subclass thereof.

[isTimelineHistogram](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogram#property-isTimelineHistogram-static)
Identifies an object as an instance of [TimelineHistogram](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogram) class, or subclass thereof.
