# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/TimeSelection.md

# [TimeSelection](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection)

Feature that allows selection of a time span in the time axis header. When a time span is selected in the header, a [timeSelectionChange](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeSelection#event-timeSelectionChange) event is fired.

Configuration
-------------

You can configure the content of the header element using the [headerRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeSelection#config-headerRenderer) function.

Not compatible with the [HeaderZoom](https://bryntum.com/docs/gantt/api/#Scheduler/feature/HeaderZoom) feature.

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#config-tooltipTemplate)
Template used to generate the tooltip contents when hovering the time selection header element.

```
const scheduler = new Scheduler({
  features : {
    timeSelection : {
      tooltipTemplate({ startDate, endDate }) {
          const count = this.client.getAvailableResources(startDate, endDate).length;
          return `${count || 'No'} available resource(s)`;
      }
    }
  }
});
```

[enableDragSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#config-enableDragSelect)
Specify `true` to enable a drag-drop gesture to select the time span.

[headerRenderer](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#config-headerRenderer)
Function used to generate the HTML content for the selected time span's header element.

If you want to include an icon or similar to clear the selection on click, make sure to set `date-ref="closeButton"` on it.

```
const scheduler = new Scheduler({
    features : {
        timeSelection : {
            headerRenderer({ timeRange }) {
                return `
                    ${DateHelper.format(timeRange.startDate, 'LL')}
                    <div class="close" data-ref="closeButton></div>
                `;
            }
        }
    }
});
```

[selectedTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#config-selectedTimeSpan)
The selected time span, which can be set using simple `startDate` and `endDate` properties

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeSelection](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#property-isTimeSelection)
Identifies an object as an instance of [TimeSelection](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeSelection) class, or subclass thereof.

[isTimeSelection](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#property-isTimeSelection-static)
Identifies an object as an instance of [TimeSelection](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeSelection) class, or subclass thereof.

[enableDragSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#property-enableDragSelect)
Specify `true` to enable a drag-drop gesture to select the time span.

[selectedTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#property-selectedTimeSpan)
The selected time span, which can be set using simple `startDate` and `endDate` properties

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[timeSelectionElementClick](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#event-timeSelectionElementClick)
Triggered when clicking the time selection header element

[timeSelectionChange](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeSelection#event-timeSelectionChange)
Triggered when time selection changes
