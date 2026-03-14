# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/AbstractTimeRanges.md

# [AbstractTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges)

Abstract base class, you should not use this class directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[enableResizing](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#config-enableResizing)
Set to `true` to enable dragging and resizing of range elements in the header. Note that enabling dragging/resizing also enables [showHeaderElements](https://bryntum.com/docs/gantt/api/#Scheduler/feature/AbstractTimeRanges#config-showHeaderElements) automatically.

[showTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#config-showTooltip)
A Boolean specifying whether to show tooltip while resizing range elements, or a [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip) config object which is applied to the tooltip

[hoverTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#config-hoverTooltip)
A [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip) config object which is applied to the tooltip shown when hovering a TimeRange header element

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#config-tooltipTemplate)
Template used to generate the tooltip contents when hovering a time range header element.

```
const scheduler = new Scheduler({
  features : {
    timeRanges : {
      tooltipTemplate({ timeRange }) {
        return `${timeRange.name}`
      }
    }
  }
});
```

[headerRenderer](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#config-headerRenderer)
Function used to generate the HTML content for a time range header element.

```
const scheduler = new Scheduler({
  features : {
    timeRanges : {
      headerRenderer({ timeRange }) {
        return `${timeRange.name}`
      }
    }
  }
});
```

[bodyRenderer](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#config-bodyRenderer)
Function used to generate the HTML content for a time range body element.

```
const scheduler = new Scheduler({
  features : {
    timeRanges : {
      bodyRenderer({ timeRange }) {
        return `${timeRange.name}`
      }
    }
  }
});
```

[showHeaderElements](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#config-showHeaderElements)
Set to `false` to not render range elements into the time axis header. Note that header elements are required for interaction such as dragging/resizing, so enabling [enableResizing](https://bryntum.com/docs/gantt/api/#Scheduler/feature/AbstractTimeRanges#config-enableResizing) will automatically enable this setting.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAbstractTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#property-isAbstractTimeRanges)
Identifies an object as an instance of [AbstractTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/AbstractTimeRanges) class, or subclass thereof.

[isAbstractTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#property-isAbstractTimeRanges-static)
Identifies an object as an instance of [AbstractTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/AbstractTimeRanges) class, or subclass thereof.

[hoverTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#property-hoverTooltip)
The Tooltip instance shown when hovering a TimeRange header element

[showHeaderElements](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#property-showHeaderElements)
Set to `false` to not render range elements into the time axis header. Note that header elements are required for interaction such as dragging/resizing, so enabling [enableResizing](https://bryntum.com/docs/gantt/api/#Scheduler/feature/AbstractTimeRanges#config-enableResizing) will automatically enable this setting.

## Functions

Functions are methods available for calling on the class

[shouldRenderRange](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#function-shouldRenderRange)
Based on this method result the feature decides whether the provided range should be rendered or not. The method checks that the range intersects the current viewport.

Override the method to implement your custom range rendering vetoing logic.

[populateTimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#function-populateTimeAxisHeaderMenu)
Adds menu items for the context menu, and may mutate the menu configuration.

[getTipHtml](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#function-getTipHtml)
Generates the html to display in the tooltip during drag drop. If you want to customize the contents of the tooltip, supply a [dragTipTemplate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges#config-dragTipTemplate) instead of overriding this function.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[timeRangeHeaderClick](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#event-timeRangeHeaderClick)
Fired on the owning Scheduler or Gantt widget when a click happens on a time range header element

[timeRangeHeaderDblClick](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#event-timeRangeHeaderDblClick)
Fired on the owning Scheduler or Gantt widget when a double click happens on a time range header element

[timeRangeHeaderContextMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/AbstractTimeRanges#event-timeRangeHeaderContextMenu)
Fired on the owning Scheduler or Gantt widget when a right click happens on a time range header element
