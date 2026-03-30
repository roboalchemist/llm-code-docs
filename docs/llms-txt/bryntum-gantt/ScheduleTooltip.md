# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/ScheduleTooltip.md

# [ScheduleTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleTooltip)

Feature that displays a tooltip containing the time at the mouse position when hovering empty parts of the schedule.

To hide the schedule tooltip, just disable this feature:

```
const scheduler = new Scheduler({
    features : {
        scheduleTooltip : false
    }
});
```

You can also output a message along with the default time indicator (to indicate resource availability etc)

```
const scheduler = new Scheduler({
   features : {
      scheduleTooltip : {
          getText(date, event, resource) {
              return 'Hovering ' + resource.name;
          }
      }
  }
});
```

To take full control over the markup shown in the tooltip you can override the [generateTipContent](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleTooltip#function-generateTipContent) method:

```
const scheduler = new Scheduler({
    features : {
        scheduleTooltip : {
            generateTipContent({ date, event, resourceRecord }) {
                return `
                    <dl>
                        <dt>Date</dt><dd>${date}</dd>
                        <dt>Resource</dt><dd>${resourceRecord.name}</dd>
                    </dl>
                `;
            }
        }
    }
});
```

Configuration properties from the feature are passed down into the resulting [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip) instance.

```
const scheduler = new Scheduler({
    features : {
        scheduleTooltip : {
            // Don't show the tip until the mouse has been over the schedule for three seconds
            hoverDelay : 3000
        }
    }
});
```

This feature is **enabled** by default in `Scheduler` and **disabled** in `ResourceUtilization`. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[hideForNonWorkingTime](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleTooltip#config-hideForNonWorkingTime)
Set to `true` to hide this tooltip when hovering non-working time. Defaults to `false` for Scheduler, `true` for SchedulerPro

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isScheduleTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleTooltip#property-isScheduleTooltip)
Identifies an object as an instance of [ScheduleTooltip](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleTooltip) class, or subclass thereof.

[isScheduleTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleTooltip#property-isScheduleTooltip-static)
Identifies an object as an instance of [ScheduleTooltip](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleTooltip) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[onInternalPaint](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleTooltip#function-onInternalPaint)
Set up drag and drop and hover tooltip.

[getHoverTipHtml](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleTooltip#function-getHoverTipHtml)

[generateTipContent](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleTooltip#function-generateTipContent)
Called as mouse pointer is moved over a new resource or time block. You can override this to show custom HTML in the tooltip.

[getText](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleTooltip#function-getText)
Override this to render custom text to default hover tip
