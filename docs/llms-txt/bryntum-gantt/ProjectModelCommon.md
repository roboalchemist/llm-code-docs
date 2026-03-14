# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/mixin/ProjectModelCommon.md

# [ProjectModelCommon](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon)

Mixin that provides helpful methods and properties for a `ProjectModel`. This mixin applies to all Bryntum products.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[json](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#config-json)
Project data as a JSON string, used to populate its stores.

```
const project = new ProjectModel({
    json : '{"events":[...],"resources":[...],...}'
}
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object

[shouldSyncDataOnLoad](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#config-shouldSyncDataOnLoad)
Experimental hook that lets the app determine if a bound dataset needs syncing with the store or not, and if it does - which records that should be processed. Only called for stores that are configured with `syncDataOnLoad: true` (which is the default in the React, Angular and Vue wrappers).

This is an experimental API that might change in any release until it has been finalized.

The main use case for this is for frameworks that update all state on any state change (like React), to not have to reapply the full bound dataset each time (which becomes costly).

If the app has a cheap way of determining (for example using a timestamp) that the dataset has no changes, return `false` from this hook to prevent the store from syncing at all at that time.

```
shouldSyncDataOnLoad({ store, data }) {
  if (store === myEventStore && timestamp <= lastUpdateTimestamp) {
    // Prevent sync when the event store has not changed since last time
    // (pseudocode)
    return false;
  }
}
```

If the app knows that something has changed, return a `Set` with ids for the records that should be further processed by the sync logic.

```
shouldSyncDataOnLoad({ store, data }) {
  if (store === myEventStore && timestamp > lastUpdateTimestamp) {
    // Sync only these records (pseudocode)
    return new Set([6, 110, 586]);
  }
}
```

[toJSONResultFormat](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#config-toJSONResultFormat)
Specifies the output format of [toJSON](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelCommon#function-toJSON).

* `inlineData` - Return all crud store data, plus this project fields (under the `project` key). For example:

```
{
    "project" : {
        "startDate"    : "2024-03-22",
        "endDate"      : "2024-04-22",
        "hoursPerDay"  : 8,
        "daysPerWeek"  : 5,
        "daysPerMonth" : 20
    },
    "events"             : [...],
    "resources"          : [...],
    "assignments"        : [...],
    "dependencies"       : [...],
    "resourceTimeRanges" : [...],
    "timeRanges"         : [...]
}
```

* `model` - Return only the project fields. For example:

```
{
    "startDate"    : "2024-03-22",
    "endDate"      : "2024-04-22",
    "hoursPerDay"  : 8,
    "daysPerWeek"  : 5,
    "daysPerMonth" : 20
}
```

[useRawData](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#config-useRawData)
By default, the stores of a project use the raw data objects passed to them as the data source for their records if data is loaded remotely (using an `AjaxStore` or a `CrudManager`). For data supplied inline, the data objects are instead by default cloned to avoid the original data object being modified by the store.

See [useRawData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-useRawData) for more information on the mechanics of this.

This can be explicitly controlled per store by setting the `useRawData` config on the store:

```
// Opt in for a single store
const project = new ProjectModel({
    eventStore : {
      useRawData : true
    },
    ...
});
```

Or you can control it for all the default stores in the project by setting this config on the project:

```
// Opt in for all stores in the project
const project = new ProjectModel({
   useRawData : true,
   ...
});
```

[includeLegacyDataProperties](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#config-includeLegacyDataProperties)
Whether to include legacy data properties in the JSON / inlineData output. The legacy data properties are the `xxData` (`eventsData`, `resourcesData` etc.) properties that are deprecated and will be removed in the future.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectModelCommon](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#property-isProjectModelCommon)
Identifies an object as an instance of [ProjectModelCommon](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelCommon) class, or subclass thereof.

[isProjectModelCommon](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#property-isProjectModelCommon-static)
Identifies an object as an instance of [ProjectModelCommon](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelCommon) class, or subclass thereof.

[shouldSyncDataOnLoad](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#property-shouldSyncDataOnLoad)
Experimental hook that lets the app determine if a bound dataset needs syncing with the store or not, and if it does - which records that should be processed. Only called for stores that are configured with `syncDataOnLoad: true` (which is the default in the React, Angular and Vue wrappers).

This is an experimental API that might change in any release until it has been finalized.

The main use case for this is for frameworks that update all state on any state change (like React), to not have to reapply the full bound dataset each time (which becomes costly).

If the app has a cheap way of determining (for example using a timestamp) that the dataset has no changes, return `false` from this hook to prevent the store from syncing at all at that time.

```
shouldSyncDataOnLoad({ store, data }) {
  if (store === myEventStore && timestamp <= lastUpdateTimestamp) {
    // Prevent sync when the event store has not changed since last time
    // (pseudocode)
    return false;
  }
}
```

If the app knows that something has changed, return a `Set` with ids for the records that should be further processed by the sync logic.

```
shouldSyncDataOnLoad({ store, data }) {
  if (store === myEventStore && timestamp > lastUpdateTimestamp) {
    // Sync only these records (pseudocode)
    return new Set([6, 110, 586]);
  }
}
```

[includeLegacyDataProperties](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#property-includeLegacyDataProperties)
Whether to include legacy data properties in the JSON / inlineData output. The legacy data properties are the `xxData` (`eventsData`, `resourcesData` etc.) properties that are deprecated and will be removed in the future.

[inlineData](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#property-inlineData)
Get or set data of project stores. The returned data is identical to what [toJSON](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelCommon#function-toJSON) returns:

```
const data = scheduler.project.inlineData;

// data:
{
    project            : { ... },
    events             : [...],
    resources          : [...],
    dependencies       : [...],
    assignments        : [...],
    resourceTimeRanges : [...],
    timeRanges         : [...]
}


// Plug it back in later
scheduler.project.inlineData = data;
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object.

To stop including the legacy data properties, set [includeLegacyDataProperties](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelCommon#config-includeLegacyDataProperties) to `false`.

[json](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#property-json)
Get or set project data (records from its stores) as a JSON string.

Get a JSON string:

```
const project = new ProjectModel({
    events       : [...],
    resources    : [...],
    assignments  : [...],
    dependencies : [...]
});

const jsonString = project.json;

// jsonString:
'{"events":[...],"resources":[...],...}'
```

Set a JSON string (to populate the project stores):

```
project.json = '{"events":[...],"resources":[...],...}'
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object

## Functions

Functions are methods available for calling on the class

[toJSON](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelCommon#function-toJSON)
Returns the data from the records of the projects stores, in a format that can be consumed by `loadInlineData()`.

Used by JSON.stringify to correctly convert this record to json.

The output format is determined by the value of [toJSONResultFormat](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelCommon#config-toJSONResultFormat), as follows:

* `inlineData` - Returns all crud store data, plus the project fields (under the `project` key)
* `model` - Returns only the project fields

```
const project = new ProjectModel({
    // Include both store data and project model fields in toJSON() result
    toJSONResultFormat     : 'inlineData',
    events             : [...],
    resources          : [...],
    assignments        : [...],
    dependencies       : [...],
    resourceTimeRanges : [...],
    timeRanges         : [...]
});

const json = project.toJSON();

// json:
{
    events             : [...],
    resources          : [...],
    assignments        : [...],
    dependencies       : [...],
    ...
    project                : {
        addConstraintOnDateSet : false,
        daysPerMonth           : 13
        daysPerWeek            : 3
        ...
    },
    ...
}
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object

Output can be consumed by `loadInlineData()`:

```
const json = project.toJSON();

// Plug it back in later
project.loadInlineData(json);
```
