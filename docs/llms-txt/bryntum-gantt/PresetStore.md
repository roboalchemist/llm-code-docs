# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/preset/PresetStore.md

# [PresetStore](https://bryntum.com/docs/gantt/api/Scheduler/preset/PresetStore)

A special Store subclass which holds [ViewPresets](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset). Each ViewPreset in this store represents a zoom level. The store data is sorted in special zoom order. That is zoomed out to zoomed in. The first Preset will produce the narrowest event bars the last one will produce the widest event bars.

To specify view presets (zoom levels) please provide set of view presets to the scheduler:

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

[zoomOrder](https://bryntum.com/docs/gantt/api/Scheduler/preset/PresetStore#config-zoomOrder)
Specifies the sort order of the presets in the store. By default they are in zoomed out to zoomed in order. That is presets which will create widest event bars to presets which will produce narrowest event bars.

Configure this as `-1` to reverse this order.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPresetStore](https://bryntum.com/docs/gantt/api/Scheduler/preset/PresetStore#property-isPresetStore)
Identifies an object as an instance of [PresetStore](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetStore) class, or subclass thereof.

[isPresetStore](https://bryntum.com/docs/gantt/api/Scheduler/preset/PresetStore#property-isPresetStore-static)
Identifies an object as an instance of [PresetStore](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetStore) class, or subclass thereof.
