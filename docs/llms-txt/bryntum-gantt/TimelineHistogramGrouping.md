# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineHistogramGrouping.md

# [TimelineHistogramGrouping](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping)

Mixin for [TimelineHistogram](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogram) that provides record grouping support. The class implements an API to work with groups and their members and allows to rollup group members data to their parents.

The _groups_ here are either group headers built with the [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) feature or parent nodes built with the [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature.

Parent histogram data aggregating
---------------------------------

The mixin provides a [aggregateHistogramDataForGroups](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping#config-aggregateHistogramDataForGroups) config which enables automatically rolling up child records histogram data to their parents. By default all registered [series](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping#config-series)' values are just summed up on parents level, but that can be changed by providing `aggregate` config to [series](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping#config-series):

```
new TimelineHistogram({
    series : {
        salary : {
           type : 'bar',
           // show maximum value on the parent level
           aggregate : 'max'
        }
    },
    ...
})
```

Here is the list of supported `aggregate` values:

* `sum` or `add` - sum of values in the group (default)
* `min` - minimum value in the group
* `max` - maximum value in the group
* `count` - number of child records in the group
* `avg` - average of the child values in the group

There are a few hooks allowing customization of the rolling up process: [aggregateDataEntry](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping#config-aggregateDataEntry), [getDataEntryForAggregating](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping#config-getDataEntryForAggregating) and [initAggregatedDataEntry](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping#config-initAggregatedDataEntry).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[aggregateHistogramDataForGroups](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#config-aggregateHistogramDataForGroups)
When `true` the component will automatically calculate data for group records based on the groups members data by calling [getGroupRecordHistogramData](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping#function-getGroupRecordHistogramData) method.

[aggregateDataEntry](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#config-aggregateDataEntry)
A function used for aggregating child records histogram data entries to their parent entry.

It's called for each child entry and is meant to apply the child entry values to the target parent entry (provided in `aggregated` parameter). The function must return the resulting aggregated entry that will be passed as `aggregated` parameter to the next **aggregating** step.

Should be provided as a function, or name of a function in the ownership hierarchy which may be called.

[getDataEntryForAggregating](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#config-getDataEntryForAggregating)
Function that extracts a record histogram data entry for aggregating. By default it returns the entry as is. Override the function if you need a more complex way to retrieve the value for aggregating.

Should be provided as a function, or the name of a function in the ownership hierarchy which may be called.

[initAggregatedDataEntry](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#config-initAggregatedDataEntry)
A function that initializes a target group record entry.

Should be provided as a function, or name of a function in the ownership hierarchy which may be called.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineHistogramGrouping](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#property-isTimelineHistogramGrouping)
Identifies an object as an instance of [TimelineHistogramGrouping](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping) class, or subclass thereof.

[isTimelineHistogramGrouping](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#property-isTimelineHistogramGrouping-static)
Identifies an object as an instance of [TimelineHistogramGrouping](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineHistogramGrouping) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[resetGeneratedRecordsHistogramDataCache](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#function-resetGeneratedRecordsHistogramDataCache)
Resets generated records (parents and links) data cache

[getGroupRecordHistogramData](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#function-getGroupRecordHistogramData)
Aggregates the provided group record children histogram data. If some of the provided records data is not ready yet the method returns a `Promise` that's resolved once the data is ready and aggregated.

```
// get parent record aggregated histogram data
const aggregatedData = await histogram.getGroupRecordHistogramData(record);
```

[aggregateRecordsHistogramData](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#function-aggregateRecordsHistogramData)
Aggregates multiple records histogram data. If some of the provided records data is not ready yet the method returns a `Promise` that's resolved once the data is ready and aggregated.

[isGroupRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#function-isGroupRecord)
Indicates if the passed record represents a group header built by [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) feature or a group built by [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature.

[getGroupChildren](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#function-getGroupChildren)
For a record representing a group built by [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) or [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature returns the group members.

[getRecordParent](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#function-getRecordParent)
For a record belonging to a group built by [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) or [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature returns the group header or parent respectively.

[scheduleRecordParentsRefresh](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#function-scheduleRecordParentsRefresh)
Schedules refresh of the provided record's parents. The method iterates up from the provided record parent to the root node and schedules the iterated node rows refresh.

[aggregateHistogramData](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineHistogramGrouping#function-aggregateHistogramData)
Aggregates collected child records data to its parent. The method is synchronous and is called when all the child records data is ready. Override the method if you need to preprocess or postprocess parent records aggregated data:

```
class MyHistogramView extends TimelineHistogram({

    aggregateHistogramData(recordsData, records, aggregationContext) {
        const result = super.aggregateHistogramData(recordsData, records, aggregationContext);

        // postprocess averageSalary series values collected for a parent record
        result.forEach(entry => {
            entry.averageSalary = entry.averageSalary / records.length;
        });

        return result;
    }

});
```
