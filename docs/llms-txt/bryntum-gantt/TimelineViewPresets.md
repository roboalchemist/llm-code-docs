# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineViewPresets.md

# [TimelineViewPresets](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets)

View preset handling.

A Scheduler's [presets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-presets) are loaded with a default set of [ViewPresets](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) which are defined by the system in the [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager).

The zooming feature works by reconfiguring the Scheduler with a new [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) selected from the [presets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-presets) store.

[ViewPresets](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) can be added and removed from the store to change the amount of available steps. Range of zooming in/out can be also modified with [maxZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-maxZoomLevel) / [minZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-minZoomLevel) properties.

This mixin adds additional methods to the column : [maxZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#property-maxZoomLevel), [minZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#property-minZoomLevel), [zoomToLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomToLevel), [zoomIn](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomIn), [zoomOut](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomOut), [zoomInFull](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomInFull), [zoomOutFull](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomOutFull).

**Notice**: Zooming is not supported when `forceFit` option is set to `true` for the Scheduler or for filtered timeaxis.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[viewPreset](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#config-viewPreset)
A string key used to lookup a predefined [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) (e.g. 'weekAndDay', 'hourAndDay'), managed by [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager). See [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager) for more information. Or a config object for a viewPreset.

Options:

* 'secondAndMinute'
* 'minuteAndHour'
* 'hourAndDay'
* 'dayAndWeek'
* 'dayAndMonth'
* 'weekAndDay'
* 'weekAndMonth',
* 'monthAndYear'
* 'year'
* 'manyYears'
* 'weekAndDayLetter'
* 'weekDateAndMonth'
* 'day'
* 'week'

If passed as a config object, the settings from the viewPreset with the provided `base` property will be used along with any overridden values in your object.

To override:

```
viewPreset : {
  base    : 'hourAndDay',
  id      : 'myHourAndDayPreset',
  headers : [
      {
          unit      : "hour",
          increment : 12,
          renderer  : (startDate, endDate, headerConfig, cellIdx) => {
              return "";
          }
      }
  ]
}
```

or set a new valid preset config if the preset is not registered in the [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager).

When you use scheduler in weekview mode, this config is used to pick view preset. If passed view preset is not supported by weekview (only 2 supported by default - 'day' and 'week') default preset will be used - 'week'.

[presets](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#config-presets)
An array of [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) config objects which describes the available timeline layouts for this scheduler.

By default, a predefined set is loaded from the [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager).

A [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) describes the granularity of the timeline view and the layout and subdivisions of the timeline header.

[displayDateFormat](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#config-displayDateFormat)
Defines how dates will be formatted in tooltips etc. This config has priority over similar config on the view preset. For allowed values see [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static).

By default, this is ingested from [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) upon change of [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) (Such as when zooming in or out). But Setting this to your own value, overrides that behaviour.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineViewPresets](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#property-isTimelineViewPresets)
Identifies an object as an instance of [TimelineViewPresets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets) class, or subclass thereof.

[isTimelineViewPresets](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#property-isTimelineViewPresets-static)
Identifies an object as an instance of [TimelineViewPresets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets) class, or subclass thereof.

[presets](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#property-presets)
Get the [PresetStore](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetStore) created for the Scheduler, or set an array of [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) config objects.

[displayDateFormat](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#property-displayDateFormat)
Defines how dates will be formatted in tooltips etc. This config has priority over similar config on the view preset. For allowed values see [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static).

By default, this is ingested from [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) upon change of [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) (Such as when zooming in or out). But Setting this to your own value, overrides that behaviour.

[viewPreset](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#property-viewPreset)
Get/set the current view preset

## Functions

Functions are methods available for calling on the class

[getFormattedDate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#function-getFormattedDate)
Method to get a formatted display date

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforePresetChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#event-beforePresetChange)
Fired before the [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-viewPreset) is changed.

[presetChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineViewPresets#event-presetChange)
Fired after the [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-viewPreset) has changed.
