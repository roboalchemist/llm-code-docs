# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/TimelineHistogramBase.md

# [TimelineHistogramBase](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase)

Base class for [TimelineHistogram](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogram) class.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showBarTip](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-showBarTip)
Set to `true` if you want to display a tooltip when hovering an allocation bar. You can also pass a [Tooltip#configs](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#configs) config object. Please use [barTooltipTemplate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-barTooltipTemplate) function to customize the tooltip contents.

[showBarTipWhenNavigatingTimeAxis](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-showBarTipWhenNavigatingTimeAxis)
Set to `true` to display the [bar tooltip](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-showBarTip) when navigating the timeaxis cells using [ScheduleContext](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext) feature. The tooltip is disabled by default when navigating to make the navigation easier.

[series](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-series)
Object enumerating data series for the histogram. The object keys are treated as the series identifiers and values are objects that must contain two properties:

* `type` A String, either `'bar'` or `'outline'`
* `field` A String, the name of the property to use from the data objects in the [data](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-data) option.

```
histogram = new TimelineHistogram({
    ...
    series : {
        s1 : {
            type  : 'bar',
            field : 's1'
        },
        s2 : {
            type  : 'outline',
            field : 's2'
        }
    },
    store : new Store({
        data : [
            {
                id            : 'r1',
                name          : 'Record 1',
                histogramData : [
                    { s1 : 200, s2 : 100 },
                    { s1 : 150, s2 : 50 },
                    { s1 : 175, s2 : 50 },
                    { s1 : 175, s2 : 75 }
                ]
            },
            {
                id            : 'r2',
                name          : 'Record 2',
                histogramData : [
                    { s1 : 100, s2 : 100 },
                    { s1 : 150, s2 : 125 },
                    { s1 : 175, s2 : 150 },
                    { s1 : 175, s2 : 75 }
                ]
            }
        ]
    })
});
```

[dataModelField](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-dataModelField)
Record field from which the histogram data will be collected.

```
histogram = new TimelineHistogram({
    ...
    series : {
        s1 : {
            type : 'bar'
        }
    },
    dataModelField : 'foo',
    store : new Store({
        data : [
            {
                id   : 'r1',
                name : 'Record 1',
                foo  : [
                    { s1 : 200 },
                    { s1 : 150 },
                    { s1 : 175 },
                    { s1 : 175 }
                ]
            },
            {
                id   : 'r2',
                name : 'Record 2',
                foo  : [
                    { s1 : 100 },
                    { s1 : 150 },
                    { s1 : 175 },
                    { s1 : 175 }
                ]
            }
        ]
    })
});
```

Alternatively [getRecordData](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-getRecordData) function can be used to build a record's histogram data dynamically.

[getRecordData](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-getRecordData)
A function, or name of a function which builds histogram data for the provided record.

See also [dataModelField](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-dataModelField) allowing to load histogram data from a record field.

[hardRefreshOnTimeAxisReconfigure](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-hardRefreshOnTimeAxisReconfigure)
When set to `true` (default) the component reacts on time axis changes (zooming or changing the displayed time span), clears the histogram data cache of the records and then refreshes the view.

[getBarClass](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-getBarClass)
A Function which returns a CSS class name to add to a rectangle element. The following parameters are passed:

[getOutlineClass](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-getOutlineClass)
A Function which returns a CSS class name to add to a path element built for an `outline` type series. The following parameters are passed:

[getOutlineDOMConfig](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-getOutlineDOMConfig)
A Function which if provided should return a DOM configuration object for a `path` element built for an `outline` type series. The function accepts a default prepared DOM configuration in an argument which then can be processed and returned.

The following parameters are passed to the function:

[barTooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-barTooltipTemplate)
A Function which returns the tooltip text to display when hovering a bar. The following parameters are passed:

[getBarText](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-getBarText)
A Function which returns the text to render inside a bar.

```
new TimelineHistogram({
    series : {
        foo : {
            type  : 'bar',
            field : 'foo'
        }
    },
    getBarText(datum) {
        // display the value in the bar
        return datum.foo;
    },
    ...
})
```

**Please note** that the function will be injected into the underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render actual charts. So `this` will refer to the [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) instance, not this class instance. To access the view please use `this.owner` in the function:

```
new TimelineHistogram({
    getBarText(datum) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const timelineHistogram = this.owner;

        .....
    },
    ...
})
```

The following parameters are passed:

[getBarDOMConfig](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-getBarDOMConfig)
A Function which if provided should return a DOM configuration object for a bar (a `RECT` element representing a single "bar"-type value). The function is passed a default prepared DOM configuration in an argument which then can be processed and returned.

```
new TimelineHistogram({
    series : {
        foo : {
            type  : 'bar',
            field : 'foo'
        }
    },
    // Let's add left & right margins to bars
    getBarDOMConfig(series, domConfig) {
        // margin size is 10% of the bar width
        const xMargin = 0.1 * domConfig.width;

        // adjust the bar x-coordinate
        domConfig.x += xMargin;
        // reduce the bar width respectively
        domConfig.width -= 2 * xMargin;

        // return the edited domConfig
        return domConfig;
    },
    ...
})
```

Please note that it's important to return a DOM configuration object. If the function doesn't do that the corresponding bar won't be displayed.

The function will be injected into the underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render charts. So `this` will refer to the [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) instance, not this class instance. To access the view please use `this.owner` in the function:

```
new TimelineHistogram({
    getBarText(datum) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const timelineHistogram = this.owner;

        .....
    },
    ...
})
```

The following parameters are passed:

[getBarTextDOMConfig](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-getBarTextDOMConfig)
A Function which returns a DOM configuration object for text elements.

```
new TimelineHistogram({
    series : {
        foo : {
            type  : 'bar',
            field : 'foo'
        }
    },
    // display "foo" bar value as text
    getBarText(datum) {
        return datum.foo;
    },

    // Place text at the top of the "foo" bar
    getBarTextDOMConfig(domConfig, datum, index) {
        // to do that we calculate y-position in percents
        domConfig.y = `${100 * (1 - datum.foo / this.topValue)}%`;

        return domConfig;
    },
    ...
})
```

Please note that it's important to return a DOM configuration object. If the function doesn't do that the corresponding text element won't be displayed.

The function will be injected into the underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render actual charts. So `this` will refer to the [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) instance, not this class instance. To access the view please use `this.owner` in the function:

```
new TimelineHistogram({
    getBarTextDOMConfig(domConfig) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const timelineHistogram = this.owner;

        .....

        return domConfig;
    },
    ...
})
```

The following parameters are passed:

[histogramWidgetClass](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-histogramWidgetClass)
The class used for building the [histogram widget](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#property-histogramWidget)

[histogramWidget](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#config-histogramWidget)
An instance or a configuration object of the underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render actual charts. In case a configuration object is provided the built class is defined with [histogramWidgetClass](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-histogramWidgetClass) config.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineHistogramBase](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#property-isTimelineHistogramBase)
Identifies an object as an instance of [TimelineHistogramBase](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase) class, or subclass thereof.

[isTimelineHistogramBase](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#property-isTimelineHistogramBase-static)
Identifies an object as an instance of [TimelineHistogramBase](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase) class, or subclass thereof.

[showBarTip](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#property-showBarTip)
Set to `true` if you want to display a tooltip when hovering an allocation bar. You can also pass a [Tooltip#configs](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#configs) config object. Please use [barTooltipTemplate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-barTooltipTemplate) function to customize the tooltip contents.

[histogramWidget](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#property-histogramWidget)
The underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render actual charts.

## Functions

Functions are methods available for calling on the class

[scheduleRefreshRows](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-scheduleRefreshRows)
Schedules the component rows refresh on the next animation frame. However many time it is called in one event run, it will only be scheduled to run once.

[clearHistogramDataCache](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-clearHistogramDataCache)
Clears the histogram data cache for the provided record (if provided). If the record is not provided clears the cache for all records.

[setHistogramDataCache](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-setHistogramDataCache)
Caches the provided histogram data for the given record.

[getHistogramDataCache](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-getHistogramDataCache)
Returns entire histogram data cache if no record provided, or cached data for the provided record.

[hasHistogramDataCache](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-hasHistogramDataCache)
Returns `true` if there is cached histogram data for the provided record.

[getGettingRecordDataPromise](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-getGettingRecordDataPromise)
Returns a `Promise` resolved once the provided record data collecting is finished. This works only if the record data is being collected with an async [getRecordData](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-getRecordData) function. Otherwise the method returns 'undefined' value.

[setGettingRecordDataPromise](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-setGettingRecordDataPromise)
Sets a `Promise` resolved once the provided record data collecting is finished.

[getRecordHistogramData](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-getRecordHistogramData)
Retrieves the histogram data for the provided record.

The method first checks if there is cached data for the record and returns it if found. Otherwise it starts collecting data by calling [getRecordData](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-getRecordData) (if provided) or by reading it from [dataModelField](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-dataModelField) record field.

The method can be asynchronous depending on the provided [getRecordData](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#config-getRecordData) function. If the function returns a `Promise` then the method will return a wrapping `Promise` in turn that will resolve with the collected histogram data.

The method triggers [histogramDataCacheSet](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#event-histogramDataCacheSet) event when a record data is ready.

[renderRecordHistogram](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-renderRecordHistogram)
Renders a histogram for a row. The method applies passed data to the underlying [histogramWidget](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#property-histogramWidget) component. Then the component renders charts and the method injects them into the corresponding column cell.

[histogramRenderer](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-histogramRenderer)
TimeAxis column renderer used by this view to render row histograms. It first calls [getRecordHistogramData](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#function-getRecordHistogramData) method to retrieve the histogram data for the renderer record. If the record data is ready the method renders the record histogram. And in case the method returns a `Promise` the renderer just schedules the record refresh for later and exits.

[buildGroupHeader](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#function-buildGroupHeader)
Group feature hook triggered by the feature to render group headers

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeHistogramDataCacheSet](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#event-beforeHistogramDataCacheSet)
Fires before the component stores a record's histogram data into the cache.

A listener can be used to transform the collected data dynamically before it's cached:

```
new TimelineHistogram({
    series : {
        foo : {
            type  : 'bar',
            field : 'f1'
        }
    },
    ...
    listeners : {
        beforeHistogramDataCacheSet(eventData) {
            // completely replace the data for a specific record
            if (eventData.record.id === 123) {
                eventData.data = [
                    { f1 : 10 },
                    { f1 : 20 },
                    { f1 : 30 },
                    { f1 : 40 },
                    { f1 : 50 },
                    { f1 : 60 }
                ];
            }
        }
    }
})
```

[histogramDataCacheSet](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#event-histogramDataCacheSet)
Fires after the component retrieves a record's histogram data and stores it into the cache.

Unlike similar [beforeHistogramDataCacheSet](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#event-beforeHistogramDataCacheSet) event this event is triggered after the data is put into the cache.

A listener can be used to transform the collected data dynamically:

```
new TimelineHistogram({
    series : {
        bar : {
            type : 'bar',
            field : 'bar'
        },
        halfOfBar : {
            type  : 'outline',
            field : 'half'
        }
    },
    ...
    listeners : {
        histogramDataCacheSet({ data }) {
            // add extra entries to collected data
            data.forEach(entry => {
                entry.half = entry.bar / 2;
            });
        }
    }
})
```

[beforeRenderHistogramRow](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#event-beforeRenderHistogramRow)
Fires before the component renders a row.

This event is recommended to use instead of generic [beforeRenderRow](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#event-beforeRenderRow) event since the component bails out of rendering rows for which histogram data is not ready yet (happens in case of async data collecting). The generic [beforeRenderRow](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineHistogramBase#event-beforeRenderRow) is triggered in such cases too while this event is triggered only when the data is ready and the row is actually about to be rendered.

Use a listener to adjust histograms rendering dynamically for individual rows:

```
new TimelineHistogram({
    ...
    listeners : {
        beforeRenderHistogramRow({ record, histogramConfig }) {
            // display an extra line for some specific record
            if (record.id == 111) {
                histogramConfig.series.extraLine = {
                    type  : 'outline',
                    field : 'foo'
                };
            }
        }
    }
})
```

[beforeRenderRecordHistogram](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#event-beforeRenderRecordHistogram)
Fires before the component renders a histogram in a cell.

## Typedefs

Typedefs are type definitions for the class

[HistogramRenderData](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineHistogramBase#typedef-HistogramRenderData)
Histogram renderer parameters.
