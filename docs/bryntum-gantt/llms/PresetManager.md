# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/preset/PresetManager.md

# [PresetManager](https://bryntum.com/docs/gantt/api/Scheduler/preset/PresetManager)

Intro
-----

This is a global Store of [ViewPresets](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset), required to supply initial data to Scheduler's [presets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-presets).

You can provide new view presets globally or for a specific scheduler.

**NOTE:** You **cannot** modify existing records in the PresetManager store. You can either remove preset records from the store or add new records to the store. Also please keep in mind, all changes provided to the PresetManager store are not reflected to the [presets](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-presets) of schedulers that already exist!

If you want to have just a few presets (also known as zoom levels) in your Scheduler, you can slice corresponding records from the `PresetManager` and apply them to the Scheduler `presets` config.

```
const newPresets = PresetManager.records.slice(10, 12);

const scheduler = new Scheduler({
    presets    : newPresets, // Only 2 zoom levels are available
    viewPreset : newPresets[0].id
});
```

If you want to adjust all default presets and assign to a specific scheduler you are going to create, you can extend them and pass as an array to the Scheduler `presets` config. Here is an example of how to set the same `timeResolution` to all `ViewPresets`.

```
const newPresets = PresetManager.map(preset => {
    return {
        id             : 'my_' + preset.id,
        base           : preset.id, // Based on an existing preset
        timeResolution : {
            unit      : 'day',
            increment : 1
        }
    };
});

const scheduler = new Scheduler({
    presets     : newPresets,
    viewPreset : 'my_hourAndDay'
});
```

If you want to do the same for **all** schedulers which will be created next, you can register new presets in a loop.

```
PresetManager.records.forEach(preset => {
    // Pass the same ID, so when a new preset is added to the store,
    // it will replace the current one.
    PresetManager.registerPreset(preset.id, {
       id             : preset.id,
       base           : preset.id,
       timeResolution : {
           unit      : 'day',
           increment : 1
       }
   });
});
```

Here is an example of how to add a new `ViewPreset` to the global `PresetManager` store and to the already created scheduler `presets`.

```
const scheduler = new Scheduler({...});

const newGlobalPresets = PresetManager.add({
    id              : 'myNewPreset',
    base            : 'hourAndDay', // Based on an existing preset
    columnLinesFor  : 0,
    // Override headers
    headers : [
        {
            unit       : 'day',
            // Use different date format for top header 01.10.2020
            dateFormat : 'DD.MM.YYYY'
        },
        {
            unit       : 'hour',
            dateFormat : 'LT'
        }
    ]
});

// Add new presets to the scheduler that has been created before changes
// to PresetManager are applied
scheduler.presets.add(newGlobalPresets);
```

Predefined presets
------------------

Predefined presets are:

* `secondAndMinute` - creates a 2 level header - minutes and seconds:

* `minuteAndHour` - creates a 2 level header - hours and minutes:

* `hourAndDay` - creates a 2 level header - days and hours:

* `dayAndWeek` - creates a 2 level header - weeks and days:

* `dayAndMonth` - creates a 2 level header - months and days:

* `weekAndDay` - just like `dayAndWeek` but with different formatting:

* `weekAndDayLetter` - creates a 2 level header - weeks and day letters:

* `weekAndMonth` - creates a 2 level header - months and weeks:

* `weekDateAndMonth` - creates a 2 level header - months and weeks (weeks shown by first day only):

* `monthAndYear` - creates a 2 level header - years and months:

* `year` - creates a 2 level header - years and quarters:

* `manyYears` - creates a 2 level header - 5-years and years:

See the [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) and [ViewPresetHeaderRow](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPresetHeaderRow) classes for a description of the view preset properties.

Localizing View Presets
-----------------------

Bryntum Scheduler uses locales for translations including date formats for view presets.

To translate date format for view presets just define the date format for the specified region for your locale file, like this:

```
const locale = {

    localeName : 'En',

    // ... Other translations here ...

    PresetManager : {
        // Translation for the "weekAndDay" ViewPreset
        weekAndDay : {
            // Change the date format for the top and middle levels
            topDateFormat    : 'MMM',
            middleDateFormat : 'D'
        },
        // Translation for the "dayAndWeek" ViewPreset
        dayAndWeek : {
            // Change the date format for the top level
            topDateFormat : 'MMMM YYYY'
        }
    }
}

LocaleManager.applyLocale(locale);
```

Check the [localization demo](https://bryntum.com/docs/gantt/api/../examples/localization/) and [this guide](https://bryntum.com/docs/gantt/api/#Scheduler/guides/customization/localization.md) for more details.

## Functions

Functions are methods available for calling on the class

[registerPreset](https://bryntum.com/docs/gantt/api/Scheduler/preset/PresetManager#function-registerPreset)
Registers a new view preset base to be used by any scheduler grid or tree on the page.

[normalizePreset](https://bryntum.com/docs/gantt/api/Scheduler/preset/PresetManager#function-normalizePreset)
Applies preset customizations or fetches a preset view preset using its name.

[deletePreset](https://bryntum.com/docs/gantt/api/Scheduler/preset/PresetManager#function-deletePreset)
Deletes a view preset
