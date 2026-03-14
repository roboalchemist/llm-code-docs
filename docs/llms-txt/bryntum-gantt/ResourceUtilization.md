# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/view/ResourceUtilization.md

# [ResourceUtilization](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization)

View showing the utilization levels of the project resources. The resources are displayed in a summary list where each row can be expanded to show the events assigned for the resource.

This demo shows the Resource utilization widget:

The view requires a [Project instance](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization#config-project) to be provided:

```
const project = new ProjectModel({
    autoLoad  : true,
    transport : {
        load : {
            url : 'examples/schedulerpro/view/data.json'
        }
    }
});

const resourceUtilization = new ResourceUtilization({
    project,
    appendTo    : 'targetDiv',
    rowHeight   : 60,
    minHeight   : '20em',
    flex        : '1 1 50%',
    showBarTip  : true
});
```

Pairing the component
---------------------

You can also pair the view with other timeline views such as the Gantt or Scheduler, using the [partner](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization#config-partner) config.

Changing displayed values
-------------------------

To change the displayed bar texts, supply a [getBarText](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization#config-getBarText) function. Here for example the provided function displays resources time **left** instead of allocated time

```
new ResourceUtilization({
    getBarText(datum) {
        const view = this.owner;

        // get default bar text
        let result = view.getBarTextDefault(...arguments);

        // For resource records we will display the time left for allocation
        if (result && datum.resource) {

            const unit = view.getBarTextEffortUnit();

            // display the resource available time
            result = view.getEffortText(datum.maxEffort - datum.effort, unit);
        }

        return result;
    },
})
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[getBarText](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#config-getBarText)
A Function which returns the text to render inside a bar.

Here for example the provided function displays resources time **left** instead of allocated time

```
new ResourceUtilization({
    getBarText(datum) {
        const resourceUtilization = this.owner;

        // get default bar text
        let result = view.getBarTextDefault();

        // For resource records we will display the time left for allocation
        if (result && datum.resource) {

            const unit = resourceUtilization.getBarTextEffortUnit();

            // display the resource available time
            result = resourceUtilization.getEffortText(datum.maxEffort - datum.effort, unit);
        }

        return result;
    },
})
```

**Please note** that the function will be injected into the underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render actual charts. So `this` in the function will refer to the [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) instance. To access the `ResourceUtilization` instance please use `this.owner` in the function body:

```
new ResourceUtilization({
    getBarText(datum) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const view = this.owner;

        .....
    },
})
```

The following parameters are passed:

[getBarClass](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#config-getBarClass)
A Function which returns a CSS class name to add to a rectangle element. The following parameters are passed:

[getBarTextDOMConfig](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#config-getBarTextDOMConfig)
A Function which returns a DOM configuration object for text elements.

```
new ResourceUtilization({
    getBarTextDOMConfig(domConfig, datum, index) {
        // change text vertical location
        domConfig.y = '10%';

        return domConfig;
    },
    ...
})
```

Please note that it's important to return a DOM configuration object. If the function doesn't do that the corresponding text element won't be displayed.

The function will be injected into the underlying [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) component that is used under the hood to render actual charts. So `this` will refer to the [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) instance, not this class instance. To access the view please use `this.owner` in the function:

```
new ResourceUtilization({
    getBarTextDOMConfig(domConfig) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const resourceUtilization = this.owner;

        .....

        return domConfig;
    },
    ...
})
```

The following parameters are passed:

[getBarDOMConfig](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#config-getBarDOMConfig)
A Function which if provided returns DOM configuration object for a bar (a `RECT` element representing a single "bar"-type value). The function accepts default prepared DOM configuration in an argument which then can be processed and returned.

```
new ResourceUtilization({
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
new ResourceUtilization({
    getBarText(datum) {
        // "this" in the method refers core Histogram instance
        // get the view instance
        const resourceUtilization = this.owner;

        .....
    },
    ...
})
```

The following parameters are passed:

[project](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#config-project)
A ProjectModel instance (or a config object) to display resource allocation of.

Note: This config is mandatory.

[showBarText](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#config-showBarText)
Set to `true` if you want to display resources effort values in bars (for example: `24h`, `7d`, `60min` etc.). The text contents can be changed by providing [getBarText](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization#config-getBarText) function.

[barTooltipTemplate](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#config-barTooltipTemplate)
A Function which returns the tooltip text to display when hovering a bar. The following parameters are passed:

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceUtilization](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#property-isResourceUtilization)
Identifies an object as an instance of [ResourceUtilization](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization) class, or subclass thereof.

[isResourceUtilization](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#property-isResourceUtilization-static)
Identifies an object as an instance of [ResourceUtilization](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[resolveRecordToOrigin](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#function-resolveRecordToOrigin)
The view store records wrap "real" resources and assignments. This method resolves a record to its original record resource or assignment. If the record does not wrap any record (happens for example for parent records when using [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature) then the method returns the record itself.

## Typedefs

Typedefs are type definitions for the class

[ResourceUtilizationRenderData](https://bryntum.com/docs/gantt/api/SchedulerPro/view/ResourceUtilization#typedef-ResourceUtilizationRenderData)
ResourceUtilization renderer parameters.
