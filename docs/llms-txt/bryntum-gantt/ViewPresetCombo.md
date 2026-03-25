# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/widget/ViewPresetCombo.md

# [ViewPresetCombo](https://bryntum.com/docs/gantt/api/Scheduler/widget/ViewPresetCombo)

A combo for selecting [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) for Scheduler and Gantt. Lets the user select between specified [presets](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ViewPresetCombo#config-presets) available.

By default, a preset change by the ViewPresetCombo will result in that the `startDate` will be calculated to the beginning of the [mainUnit](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-mainUnit) of the [viewportCenterDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#property-viewportCenterDate). If the ViewPreset has a [start](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-start) configured, this will be added to the calculation. The `endDate` will then be calculated by adding the ViewPreset's [defaultSpan](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-defaultSpan) to the `startDate`. Set [useFixedDuration](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ViewPresetCombo#config-useFixedDuration) to `false` to prevent this behaviour.

Add it to the component's toolbar to connect it automatically:

```
new Scheduler({
   tbar : {
       viewPresetCombo: {
           type: 'viewpresetcombo',
           width: '7em'
       }
   }
});
```

Or specify which Scheduler, SchedulerPro or Gantt component instance it should connect to the [client](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ViewPresetCombo#config-client) config:

```
const scheduler = new Scheduler({ ... });
const viewPresetCombo = new ViewPresetCombo({
    appendTo : 'someElementClassName',
    client   : scheduler
});
```

By default, the following presets are shown in the combo:

* [hourAndDay](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager)
* [weekAndDay](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager)
* [dayAndMonth](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager)

Changing selectable presets
---------------------------

To change the default selectable presets specify an array of preset ids. The presets specified must be available to the client.

```
viewPresetCombo: {
   presets: ['weekAndDay', 'dayAndMonth', 'myCustomPreset']
}
```

NOTE: The selectable presets will be arranged in the order provided in the [presets](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ViewPresetCombo#config-presets) config.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[presets](https://bryntum.com/docs/gantt/api/Scheduler/widget/ViewPresetCombo#config-presets)
An array containing string [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) ids available for selection. The specified presets must be [available](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-presets) for the [client](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ViewPresetCombo#config-client) (Scheduler, SchedulerPro or Gantt) for it to work properly. The selectable presets will be arranged in the order provided here.

[client](https://bryntum.com/docs/gantt/api/Scheduler/widget/ViewPresetCombo#config-client)
If not added to a toolbar, provide a Scheduler, SchedulerPro or Gantt component instance to which the ViewPresetCombo should be connected.

[useFixedDuration](https://bryntum.com/docs/gantt/api/Scheduler/widget/ViewPresetCombo#config-useFixedDuration)
As default, a preset change by the ViewPresetCombo will result in that the `startDate` will be calculated to the beginning of the [mainUnit](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-mainUnit) of the [viewportCenterDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#property-viewportCenterDate). If the ViewPreset has a [start](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-start) configured, this will be added to the calculation. The `endDate` will then be calculated by adding the ViewPreset's [defaultSpan](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-defaultSpan) to the `startDate`.

If this is set to `false`, the preset change will result in a call to [zoomToLevel](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomToLevel) without any options. The default behaviour of zoom functionality is to keep the timespan about the same width. If you want to change ViewPreset/Zoom without any changes to the visible timespan, you can set the [zoomKeepsOriginalTimespan](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-zoomKeepsOriginalTimespan) config to `true`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isViewPresetCombo](https://bryntum.com/docs/gantt/api/Scheduler/widget/ViewPresetCombo#property-isViewPresetCombo)
Identifies an object as an instance of [ViewPresetCombo](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ViewPresetCombo) class, or subclass thereof.

[isViewPresetCombo](https://bryntum.com/docs/gantt/api/Scheduler/widget/ViewPresetCombo#property-isViewPresetCombo-static)
Identifies an object as an instance of [ViewPresetCombo](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ViewPresetCombo) class, or subclass thereof.
