# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventTooltip.md

# [EventTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventTooltip)

Displays a tooltip when hovering events. The template used to render the tooltip can be customized, see [template](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventTooltip#config-template). Config options are also applied to the tooltip shown, see [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip) for available options.

This feature is **enabled** by default.

Showing local data
------------------

To show a basic "local" tooltip (with data available in the Event record) upon hover:

```
new Scheduler({
  features : {
    eventTooltip : {
        // Tooltip configs can be used here
        align : 'l-r' // Align left to right,
        // A custom HTML template
        template : ({ eventRecord }) => `<dl>
             <dt>Assigned to:</dt>
             <dd>
                 ${eventRecord.resource.name}
             </dd>
             <dt>Time:</dt>
             <dd>
                 ${DateHelper.format(eventRecord.startDate, 'LT')} - ${DateHelper.format(eventRecord.endDate, 'LT')}
             </dd>
             ${eventRecord.note ? `<dt>Note:</dt><dd>${eventRecord.note}</dd>` : ''}

             ${eventRecord.image ? `<dt>Image:</dt><dd><img class="image" src="${eventRecord.image}"/></dd>` : ''}
         </dl>`
    }
  }
});
```

Showing remotely loaded data
----------------------------

Loading remote data into the event tooltip is easy. Simply use the [template](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventTooltip#config-template) and return a Promise which yields the content to show.

```
new Scheduler({
  features : {
    eventTooltip : {
       template : ({ eventRecord }) => AjaxHelper.get(`./fakeServer?name=${eventRecord.name}`).then(response => response.text())
    }
  }
});
```

By default, the tooltip [realigns on scroll](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-scrollAction) meaning that it will stay aligned with its target should a scroll interaction make the target move.

If this is causing performance issues in a Scheduler, such as if there are many dozens of events visible, you can configure this feature with `scrollAction: 'hide'`. This feature's configuration is applied to the tooltip, so that will mean that the tooltip will hide if its target is moved by a scroll interaction.

Keeping tooltip visible after mouse exits target element
--------------------------------------------------------

By default, a Tooltip is transient, and will [hide](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventTooltip#function-hide) when the mouse leaves the target element. Configure this feature with [autoHide](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventTooltip#config-autoHide) set to `false` to make the Tooltip stay visible.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoHide](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventTooltip#config-autoHide)
Set this value to `false` to keep Tooltip visible after mouse leaves the target element.

[template](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventTooltip#config-template)
A function which receives data about the event and returns a string, or a Promise yielding a string (for async tooltips), to be displayed in the tooltip. This method will be called with an object containing the fields below

[scrollAction](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventTooltip#config-scrollAction)
Defines what to do if document is scrolled while the tooltip is visible.

Valid values: ´null´: do nothing, ´hide´: hide the tooltip or ´realign´: realign to the target if possible.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventTooltip#property-isEventTooltip)
Identifies an object as an instance of [EventTooltip](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventTooltip) class, or subclass thereof.

[isEventTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventTooltip#property-isEventTooltip-static)
Identifies an object as an instance of [EventTooltip](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventTooltip) class, or subclass thereof.

[eventRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventTooltip#property-eventRecord)
The event which the tooltip feature has been activated for.

## Functions

Functions are methods available for calling on the class

[resolveData](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventTooltip#function-resolveData)
Augment tooltip with extra data
