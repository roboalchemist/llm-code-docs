# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineZoomable.md

# [TimelineZoomable](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable)

Mixin providing "zooming" functionality.

The zoom levels are stored as instances of [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset)s, and are cached centrally in the [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager).

The default presets are loaded into the [presets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-presets) store upon Scheduler instantiation. Preset selection is covered in the [TimelineViewPresets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets) mixin.

To specify custom zoom levels please provide a set of view presets to the global PresetManager store **before** scheduler creation, or provide a set of view presets to a specific scheduler only:

```
const myScheduler = new Scheduler({
    presets : [
        {
            base : 'hourAndDay',
            id   : 'MyHourAndDay',
            // other preset configs....
        },
        {
            base : 'weekAndMonth',
            id   : 'MyWeekAndMonth',
            // other preset configs....
        }
    ],
    viewPreset : 'MyHourAndDay',
    // other scheduler configs....
    });
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[zoomOnMouseWheel](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#config-zoomOnMouseWheel)
If true, you can zoom in and out on the time axis using CTRL-key + mouse wheel.

[zoomOnTimeAxisDoubleClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#config-zoomOnTimeAxisDoubleClick)
True to zoom to time span when double-clicking a time axis cell.

[minZoomLevel](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#config-minZoomLevel)
The minimum zoom level to which [zoomOut](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomOut) will work. Defaults to 0 (year ticks)

[maxZoomLevel](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#config-maxZoomLevel)
The maximum zoom level to which [zoomIn](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomIn) will work. Defaults to the number of [ViewPresets](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) available, see [presets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#property-presets) for information. Unless you have modified the collection of available presets, the max zoom level is milliseconds.

[visibleZoomFactor](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#config-visibleZoomFactor)
Integer number indicating the size of timespan during zooming. When zooming, the timespan is adjusted to make the scrolling area `visibleZoomFactor` times wider than the timeline area itself. Used in [zoomToSpan](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomToSpan) and [zoomToLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomToLevel) functions.

[zoomKeepsOriginalTimespan](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#config-zoomKeepsOriginalTimespan)
Whether the originally rendered timespan should be preserved while zooming. By default, it is set to `false`, meaning the timeline panel will adjust the currently rendered timespan to limit the amount of HTML content to render. When setting this option to `true`, be careful not to allow to zoom a big timespan in seconds resolution for example. That will cause **a lot** of HTML content to be rendered and affect performance. You can use [minZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-minZoomLevel) and [maxZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-maxZoomLevel) config options for that.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineZoomable](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#property-isTimelineZoomable)
Identifies an object as an instance of [TimelineZoomable](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable) class, or subclass thereof.

[isTimelineZoomable](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#property-isTimelineZoomable-static)
Identifies an object as an instance of [TimelineZoomable](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable) class, or subclass thereof.

[maxZoomLevel](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#property-maxZoomLevel)
Get/set the [maxZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-maxZoomLevel) value

[minZoomLevel](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#property-minZoomLevel)
Sets the [minZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-minZoomLevel) value

[zoomLevel](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#property-zoomLevel)
Current zoom level, which is equal to the [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) index in the provided array of [zoom levels](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-presets).

## Functions

Functions are methods available for calling on the class

[getMilliSecondsPerPixelForZoomLevel](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-getMilliSecondsPerPixelForZoomLevel)
Returns number of milliseconds per pixel.

[zoomTo](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-zoomTo)
Zooms to passed view preset, saving center date. Method accepts config object as a first argument, which can be reduced to primitive type (string,number) when no additional options required. e.g.:

```
// zooming to preset
scheduler.zoomTo({ preset : 'hourAndDay' })
// shorthand
scheduler.zoomTo('hourAndDay')

// zooming to level
scheduler.zoomTo({ level : 0 })
// shorthand
scheduler.zoomTo(0)
```

It is also possible to zoom to a time span by omitting `preset` and `level` configs, in which case scheduler sets the time frame to a specified range and applies zoom level which allows to fit all columns to this range. The given time span will be centered in the scheduling view (unless `centerDate` config provided). In the same time, the start/end date of the whole time axis will be extended to allow scrolling for user.

```
// zooming to time span
scheduler.zoomTo({
    startDate : new Date(..),
    endDate : new Date(...)
});
```

[zoomToLevel](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-zoomToLevel)
Allows zooming to certain level of [presets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-presets) array. Automatically limits zooming between [maxZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-maxZoomLevel) and [minZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-minZoomLevel). Can also set time axis timespan to the supplied start and end dates.

[zoomToFit](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-zoomToFit)
Changes the range of the scheduling chart to fit all the events in its event store.

[zoomToSpan](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-zoomToSpan)
Sets time frame to specified range and applies zoom level which allows to fit all columns to this range.

The given time span will be centered in the scheduling view, in the same time, the start/end date of the whole time axis will be extended in the same way as [zoomToLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomToLevel) method does, to allow scrolling for user.

[zoomIn](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-zoomIn)
Zooms in the timeline according to the array of zoom levels. If the amount of levels to zoom is given, the view will zoom in by this value. Otherwise, a value of `1` will be used.

[zoomOut](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-zoomOut)
Zooms out the timeline according to the array of zoom levels. If the amount of levels to zoom is given, the view will zoom out by this value. Otherwise, a value of `1` will be used.

[zoomInFull](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-zoomInFull)
Zooms in the timeline to the [maxZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-maxZoomLevel) according to the array of zoom levels.

[zoomOutFull](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-zoomOutFull)
Zooms out the timeline to the [minZoomLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-minZoomLevel) according to the array of zoom levels.

[shift](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-shift)
Moves the time axis by the passed amount and unit.

NOTE: If using a filtered time axis, see [shift](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis#function-shift) for more information.

[shiftNext](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-shiftNext)
Moves the time axis forward in time in units specified by the view preset `shiftUnit`, and by the amount specified by the `shiftIncrement` config of the current view preset.

NOTE: If using a filtered time axis, see [shiftNext](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis#function-shiftNext) for more information.

[shiftPrevious](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#function-shiftPrevious)
Moves the time axis backward in time in units specified by the view preset `shiftUnit`, and by the amount specified by the `shiftIncrement` config of the current view preset.

NOTE: If using a filtered time axis, see [shiftPrevious](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis#function-shiftPrevious) for more information.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[noZoomChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#event-noZoomChange)
Fires when the requested date range cannot fit into any zoom level higher than the current level.

## Typedefs

Typedefs are type definitions for the class

[ChangePresetOptions](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineZoomable#typedef-ChangePresetOptions)
Options which may be used when changing the [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#property-viewPreset) property.
