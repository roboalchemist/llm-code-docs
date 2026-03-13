# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/view/ResourceHistogram.md

# [ResourceHistogram](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram)

This view displays a read-only timeline report of the workload for the resources in a [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel). The resource allocation is visualized as bars along the time axis with an optional line indicating the maximum available time for each resource. A [ScaleColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ScaleColumn) is also added automatically.

To create a standalone histogram, simply configure it with a Project instance:

```
const project = new ProjectModel({
    autoLoad : true,
    loadUrl  : 'examples/schedulerpro/view/data.json'
});

const histogram = new ResourceHistogram({
    project,
    appendTo    : 'targetDiv',
    rowHeight   : 60,
    minHeight   : '20em',
    flex        : '1 1 50%',
    showBarTip  : true,
    columns     : [
        {
            width : 200,
            field : 'name',
            text  : 'Resource'
        }
    ]
});
```

Pairing the component
---------------------

You can also pair the histogram with other timeline views such as the Gantt or Scheduler, using the [partner](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-partner) config.

You can configure (or hide completely) the built-in scale column easily:

```
const histogram = new ResourceHistogram({
   project,
   appendTo    : 'targetDiv',
   columns     : [
       {
           width : 200,
           field : 'name',
           text  : 'Resource'
       },
       // Hide the scale column (or add any other column configs)
       {
           type   : 'scale',
           hidden : true
       }
   ]
});
```

Changing displayed values
-------------------------

To change the histogram bar texts, supply a [getBarText](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-getBarText) function. Here for example the provided function displays resources time **left** instead of allocated time

```
new ResourceHistogram({
    getBarText(datum) {
        const resourceHistogram = this.owner;

        // get default bar text
        let result = resourceHistogram.getBarTextDefault(...arguments);

        // and if some work is done in the tick
        if (result) {

            const unit = resourceHistogram.getBarTextEffortUnit();

            // display the resource available time
            result = resourceHistogram.getEffortText(datum.maxEffort - datum.effort, unit);
        }

        return result;
    },
    ...
})
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[effortFormat](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-effortFormat)
Effort value format string. Must be a template supported by [NumberFormat](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat) class.

[showEffortUnit](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-showEffortUnit)
Specifies whether effort values should display units or not.

[effortUnit](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-effortUnit)
Default time unit to display resources effort values. The value is used as default when displaying effort in tooltips and bars text. Yet the effective time unit used might change dynamically when zooming in the histogram so its ticks unit gets smaller than the default unit. Please use [barTipEffortUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-barTipEffortUnit) to customize default units for tooltips only and [barTextEffortUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-barTextEffortUnit) to customize default units in bar texts.

[barTextEffortUnit](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-barTextEffortUnit)
Default time unit used for displaying resources effort in bars. Yet the effective time unit used might change dynamically when zooming in the histogram so its ticks unit gets smaller than the default unit. Please use [barTipEffortUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-barTipEffortUnit) to customize default units for tooltips (or [effortUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-effortUnit) to customize both texts and tooltips default units).

[barTipEffortUnit](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-barTipEffortUnit)
Default time unit used when displaying resources effort in tooltips. Yet the effective time unit used might change dynamically when zooming in the histogram so its ticks unit gets smaller than the default unit. Please use [barTextEffortUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-barTextEffortUnit) to customize default units for bar texts (or [effortUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-effortUnit) to customize both texts and tooltips default units).

[showMaxEffort](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-showMaxEffort)
Set to `true` if you want to display the maximum resource allocation line.

[barTooltipTemplate](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-barTooltipTemplate)
A Function which returns the tooltip text to display when hovering a bar. The following parameters are passed:

[showBarText](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-showBarText)
Set to `true` if you want to display resources effort values in bars (for example: `24h`, `7d`, `60min` etc.). The text contents can be changed by providing [getBarText](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-getBarText) function.

[getBarClass](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-getBarClass)
A Function which returns a CSS class name to add to a bar's rectangle element. The following parameters are passed:

[getOutlineClass](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-getOutlineClass)
A Function which returns a CSS class name to add to a path element built for an `outline` type series. The following parameters are passed:

[getOutlineDOMConfig](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-getOutlineDOMConfig)
A Function which if provided should return a DOM configuration object for a `path` element built for an `outline` type series. The function accepts a default prepared DOM configuration in an argument which then can be processed and returned.

The following parameters are passed to the function:

[getBarText](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-getBarText)
A Function which returns the text to render inside a bar.

Here for example the provided function displays resources time **left** instead of allocated time

```
new ResourceHistogram({
    getBarText(datum) {
        const resourceHistogram = this.owner;

        const { showBarText } = resourceHistogram;

        let result = '';

        // respect existing API - show bar texts only when "showBarText" is true
        // and if some work is done in the tick
        if (showBarText && datum.effort) {

            const unit = resourceHistogram.getBarTextEffortUnit();

            // display the resource available time
            result = resourceHistogram.getEffortText(datum.maxEffort - datum.effort, unit);
        }

        return result;
    },
})
```

**Please note** that the function will be injected into the underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render actual charts. So `this` will refer to the [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) instance, not this class instance. To access the view please use `this.owner` in the function:

```
new ResourceHistogram({
    getBarText(datum) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const resourceHistogram = this.owner;

        .....
    },
})
```

The following parameters are passed:

[getBarTextDOMConfig](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-getBarTextDOMConfig)
A Function which returns a DOM configuration object for text elements.

```
new ResourceHistogram({
    getBarTextDOMConfig(domConfig, datum, index) {
        // Place text at the top of the "effort" bar
        // so calculate y-position in percents
        domConfig.y = `${100 * (1 - datum.effort / this.topValue)}%`;

        // also let's laid the text lines horizontally
        domConfig.style = 'writing-mode: lr';

        return domConfig;
    },
    ...
})
```

Please note that it's important to return a DOM configuration object. If the function doesn't do that the corresponding text element won't be displayed.

The function will be injected into the underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render actual charts. So `this` will refer to the [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) instance, not this class instance. To access the view please use `this.owner` in the function:

```
new ResourceHistogram({
    getBarTextDOMConfig(domConfig) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const resourceHistogram = this.owner;

        .....

        return domConfig;
    },
    ...
})
```

The following parameters are passed:

[getBarDOMConfig](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-getBarDOMConfig)
A Function which if provided returns DOM configuration object for a bar (a `RECT` element representing a single "bar"-type value). The function accepts default prepared DOM configuration in an argument which then can be processed and returned.

```
new ResourceHistogram({
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
new ResourceHistogram({
    getBarText(datum) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const resourceHistogram = this.owner;

        .....
    },
    ...
})
```

The following parameters are passed:

[includeInactiveEvents](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-includeInactiveEvents)
Set to `true` to include inactive tasks allocation and `false` to not take such tasks into account.

[costFormat](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-costFormat)
Specifies a format to use for displaying cost values. Default value is:

```
costFormat : {
    style    : 'currency',
    currency : 'USD'
},
```

See [NumberFormat](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat) docs for details on the supported config values. Please keep in mind that `currency` value will be automatically set to the loaded project currency.

[respectStoreFilters](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-respectStoreFilters)
Set to `true` to take task and assignment store filters into account when collecting allocation.

```
new ResourceHistogram({
    // skip filtered out events/assignments
    respectStoreFilters : true
    ...
});
```

[assignmentFilterFn](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#config-assignmentFilterFn)
A function that if provided decides whether an assignment should be taken into account or not when collecting allocation.

The function is recommended to be a generator so it can attach to the Engine and track the involved field changes automatically. It accepts two arguments: assignment record and `ResourceAllocationInfo` class instance collecting allocation. The instance has a special `readField` method that should be yielded to read the needed field value. The method also subscribes to further changes of the field triggering automatic allocation recollecting once the field gets changed:

```
new ResourceHistogram({
    // custom filtering function
    * assignmentFilterFn(assignment, allocationInfo) {
        // get the assignment event
        const event = yield assignment.$.event;

        // include only allocation of events having "type" field set to "Meeting"
        if (event) {
            // get "type" field value and bind to its changes
            // to refresh the histogram automatically
            const type = yield* allocationInfo.readField(event, 'type');

            return type === 'Meeting';
        }
    }
    ...
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceHistogram](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#property-isResourceHistogram)
Identifies an object as an instance of [ResourceHistogram](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram) class, or subclass thereof.

[isResourceHistogram](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#property-isResourceHistogram-static)
Identifies an object as an instance of [ResourceHistogram](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[generateScalePoints](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#function-generateScalePoints)
Generates points for the [scale column](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#property-scaleColumn).

**Override the method to customize the scale column points.**

[getEffortText](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#function-getEffortText)
Formats effort value to display in the component bars and tooltips.

[getBarTextEffortUnit](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#function-getBarTextEffortUnit)
Returns unit to display effort values in when rendering the histogram bars. The method by default returns [barTextEffortUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-barTextEffortUnit) value if provided and if not falls back to [effortUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-effortUnit) value. But it also takes zooming into account and when the timeaxis ticks unit gets smaller than the default value the ticks unit is returned.

[getBarTextDefault](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#function-getBarTextDefault)
The default method that returns the text to render inside a bar if no [getBarText](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-getBarText) function was provided.

The method can be used in a [getBarText](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-getBarText) function to invoke the default implementation:

```
new ResourceHistogram({
    getBarText(datum) {
        const resourceHistogram = this.owner;

        // get default bar text
        let result = resourceHistogram.getBarTextDefault();

        // if the resource is overallocated in that tick display "Overallocated! " string
        // before the allocation value
        if (result && datum.maxEffort < datum.effort) {
            result = 'Overallocated! ' + result;
        }

        return result;
    },
})
```

The following parameters are passed:

[getRecordAllocationData](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#function-getRecordAllocationData)
Returns the provided record's allocation data. The process of allocation collecting is asynchronous so the method returns a `Promise` that provides the data once resolved.

The method used as the default value of [getRecordData](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-getRecordData) config.

[initAggregatedAllocationEntry](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#function-initAggregatedAllocationEntry)
The default function that initializes a target group record entry.

The method is used as [initAggregatedDataEntry](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-initAggregatedDataEntry) default value.

[aggregateAllocationEntry](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#function-aggregateAllocationEntry)
The default function used for aggregating a child record histogram data values to its parent entry. The function sums up `effort` and `maxEffort` series values. It also propagates [isOverallocated](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceModel#typedef-ResourceAllocationInterval) and [isUnderallocated](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceModel#typedef-ResourceAllocationInterval) values so if there is a child having the corresponding value as `true` it will be `true` on the parent level as well.

All children [assignments](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceModel#typedef-ResourceAllocationInterval) are united on the parent level [assignments](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceModel#typedef-ResourceAllocationInterval) property.

The method is used as [aggregateDataEntry](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#config-aggregateDataEntry) default value.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[generateScalePoints](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#event-generateScalePoints)
Fires when the component generates points for the [scale column](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceHistogram#property-scaleColumn).

Use a listeners to override the generated scale points:

```
new ResourceHistogram({
    ...
    listeners : {
        generateScalePoints(params) {
            // provide text for each scale point (if not provided already)
            params.scalePoints.forEach(point => {
                point.text = point.text || point.value;
            });
        }
    }
})
```

## Typedefs

Typedefs are type definitions for the class

[ResourceHistogramRenderData](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceHistogram#typedef-ResourceHistogramRenderData)
ResourceHistogram renderer parameters.
