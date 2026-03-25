# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/ResourceTimeRanges.md

# [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges)

Feature that draws resource time ranges, shaded areas displayed behind events. These zones are similar to events in that they have a start and end date but different in that they do not take part in the event layout, and they always occupy full row height.

Each time range is represented by an instances of [ResourceTimeRangeModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTimeRangeModel), held in a [ResourceTimeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceTimeRangeStore). Currently they are readonly UI-wise, but can be manipulated on the data level. To style the rendered elements, use the [cls](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-cls) field or use the [timeRangeColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTimeRangeModel#field-timeRangeColor) field.

Data can be provided either using the [resourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-resourceTimeRanges) config on the Scheduler config object:

```
new Scheduler({
    ...
   features :  {
       resourceTimeRanges : true
   },

   // Data specified directly on the Scheduler instance
   resourceTimeRanges : [
       // Either specify startDate & endDate or startDate & duration when defining a range
       { startDate : new Date(2019,0,1), endDate : new Date(2019,0,3), name : 'Occupied', timeRangeColor : 'red' },
       { startDate : new Date(2019,0,3), duration : 2, durationUnit : 'd', name : 'Available' },
   ]
})
```

Or the [resourceTimeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-resourceTimeRangeStore) config on the Scheduler config object:

```
new Scheduler({
    ...
    features :  {
        resourceTimeRanges : true
    },
    resourceTimeRangeStore : new ResourceTimeRangeStore({
        readUrl : './resourceTimeRanges/'
    })
})
```

Or on the project, using the [resourceTimeRangesData](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelMixin#config-resourceTimeRangesData) config.

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

Recurring ranges support
------------------------

Resource time ranges can also be recurring, as seen in the example below:

```
const resourceTimeRangeStore = new ResourceTimeRangeStore({
    data : [{
        id             : 1,
        resourceId     : 'r1',
        startDate      : '2019-01-01T11:00',
        endDate        : '2019-01-01T13:00',
        name           : 'Lunch',
        // this time range will repeat every day
        recurrenceRule : 'FREQ=DAILY'
    }]
});

```

Rendering custom HTML markup
----------------------------

Sometimes it is handy to be able to output custom HTML into the range elements. This can be done using the [resourceTimeRangeRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-resourceTimeRangeRenderer) config method.

```
// You can use a custom renderer method to output the contents of the range elements. The return value should
// be a string or a DOMConfig object defining the markup to generate
new Scheduler({
    resourceTimeRangeRenderer{ resourceTimeRangeRecord, resourceRecord, renderData }) {
        if (resourceTimeRangeRecord.important) {
            // Add a CSS class to the range element
            renderData.cls.important = 1;

            return [
                {
                    tag   : 'i',
                    class : 'fa fa-warning'
                },
                {
                    tag  : 'strong',
                    text : resourceTimeRangeRecord.name
                }
            ];
        }
        return resourceTimeRangeRecord.name;
    }
})
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[enableMouseEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#config-enableMouseEvents)
Set to `true` to allow mouse interactions with the rendered range elements. By default, the range elements are not reachable with the mouse, and only serve as a static background.

[tabIndex](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#config-tabIndex)
Specify value to use for the tabIndex attribute of resource time range elements

[resourceTimeRangeRenderer](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#config-resourceTimeRangeRenderer)
An empty function by default, but provided so that you can override it. This function is called each time a resource time range is rendered into the schedule. It's called with `resourceTimeRangeRecord`, `resourceRecord`, and `renderData` params.

You should never modify any records inside this method.

By default, the DOM markup of a resource time range bar includes placeholders for 'cls' and 'style'. The cls property is a [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList) which will be added to the main element. The style property is an inline style declaration for the main element.

**IMPORTANT:** When returning content, be sure to consider how that content should be encoded to avoid XSS (Cross-Site Scripting) attacks. This is especially important when including user-controlled data such as the event's `name`. The function [encodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-encodeHtml-static) as well as [xss](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-xss-static) can be helpful in these cases.

```
resourceTimeRangeRenderer({ resourceTimeRangeRecord, resourceRecord, renderData }) {
    renderData.style = 'color:white'; // You can use inline styles too.

    // Property names with truthy values are added to the resulting elements CSS class.
    renderData.cls.isModified = resourceTimeRangeRecord.isModified;

    // Or, you can treat it as a string, but this is less efficient, especially
    // if your renderer wants to *remove* classes that may be there.
    renderData.cls += ' extra-class';

    return StringHelper.xss`${DateHelper.format(resourceTimeRangeRecord.startDate, 'YYYY-MM-DD')}:
    ${resourceTimeRangeRecord.name}`;
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#property-isResourceTimeRanges)
Identifies an object as an instance of [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) class, or subclass thereof.

[isResourceTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#property-isResourceTimeRanges-static)
Identifies an object as an instance of [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) class, or subclass thereof.

[enableMouseEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#property-enableMouseEvents)
Set to `true` to allow mouse interactions with the rendered range elements. By default, the range elements are not reachable with the mouse, and only serve as a static background.

## Functions

Functions are methods available for calling on the class

[resolveResourceTimeRangeRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#function-resolveResourceTimeRangeRecord)
Returns a resource time range record from the passed element

[getElementFromResourceTimeRangeRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#function-getElementFromResourceTimeRangeRecord)
Returns the element for the passed resource time range record, if rendered into DOM.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[resourceTimeRangeMouseDown](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#event-resourceTimeRangeMouseDown)
Triggered for mouse down ona resource time range. Only triggered if the ResourceTimeRange feature is configured with `enableMouseEvents: true`.

[resourceTimeRangeMouseUp](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#event-resourceTimeRangeMouseUp)
Triggered for mouse up ona resource time range. Only triggered if the ResourceTimeRange feature is configured with `enableMouseEvents: true`.

[resourceTimeRangeClick](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#event-resourceTimeRangeClick)
Triggered for click on a resource time range. Only triggered if the ResourceTimeRange feature is configured with `enableMouseEvents: true`.

[resourceTimeRangeDblClick](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#event-resourceTimeRangeDblClick)
Triggered for double-click on a resource time range. Only triggered if the ResourceTimeRange feature is configured with `enableMouseEvents: true`.

[resourceTimeRangeContextMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#event-resourceTimeRangeContextMenu)
Triggered for right-click on a resource time range. Only triggered if the ResourceTimeRange feature is configured with `enableMouseEvents: true`.

[resourceTimeRangeMouseOver](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#event-resourceTimeRangeMouseOver)
Triggered for mouse over on a resource time range. Only triggered if the ResourceTimeRange feature is configured with `enableMouseEvents: true`.

[resourceTimeRangeMouseOut](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceTimeRanges#event-resourceTimeRangeMouseOut)
Triggered for mouse out of a resource time range. Only triggered if the ResourceTimeRange feature is configured with `enableMouseEvents: true`.
