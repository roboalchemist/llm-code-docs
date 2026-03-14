# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/plugin/DateStoreLazyLoadPlugin.md

# [DateStoreLazyLoadPlugin](https://bryntum.com/docs/gantt/api/Scheduler/data/plugin/DateStoreLazyLoadPlugin)

Plugin for Store that handles lazy loading of stores that is dependent on the view's visible time span.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[lazyLoad](https://bryntum.com/docs/gantt/api/Scheduler/data/plugin/DateStoreLazyLoadPlugin#config-lazyLoad)
If set to `true`, or a config object, this makes the store load new records when needed. When a record that is not already loaded is requested, the [requestData](https://bryntum.com/docs/gantt/api/#Scheduler/data/plugin/DateStoreLazyLoadPlugin#function-requestData) function is called. Please read the [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md) to learn more on how to configure lazy loading.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDateStoreLazyLoadPlugin](https://bryntum.com/docs/gantt/api/Scheduler/data/plugin/DateStoreLazyLoadPlugin#property-isDateStoreLazyLoadPlugin)
Identifies an object as an instance of [DateStoreLazyLoadPlugin](https://bryntum.com/docs/gantt/api/#Scheduler/data/plugin/DateStoreLazyLoadPlugin) class, or subclass thereof.

[isDateStoreLazyLoadPlugin](https://bryntum.com/docs/gantt/api/Scheduler/data/plugin/DateStoreLazyLoadPlugin#property-isDateStoreLazyLoadPlugin-static)
Identifies an object as an instance of [DateStoreLazyLoadPlugin](https://bryntum.com/docs/gantt/api/#Scheduler/data/plugin/DateStoreLazyLoadPlugin) class, or subclass thereof.

[lazyLoad](https://bryntum.com/docs/gantt/api/Scheduler/data/plugin/DateStoreLazyLoadPlugin#property-lazyLoad)
If set to `true`, or a config object, this makes the store load new records when needed. When a record that is not already loaded is requested, the [requestData](https://bryntum.com/docs/gantt/api/#Scheduler/data/plugin/DateStoreLazyLoadPlugin#function-requestData) function is called. Please read the [guide](https://bryntum.com/docs/gantt/api/#Grid/guides/data/lazyloading.md) to learn more on how to configure lazy loading.

## Functions

Functions are methods available for calling on the class

[requestData](https://bryntum.com/docs/gantt/api/Scheduler/data/plugin/DateStoreLazyLoadPlugin#function-requestData)
In an EventStore or ResourceTimeRangeStore which is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), the function provided here is called when a combination of the visible date range and the visible range of resources has not yet been loaded. If the ResourceStore is not configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), the resource range will include all the loaded resources. When implementing this, it is expected that what is returned is an object with a `data` property containing the records from `startDate` to `endDate` for a range of resources starting at `startIndex` and with the length specified in the `count` param.

Base implementation does nothing, either use AjaxStore which implements it, or create your own subclass with an implementation.

```
class MyEventStore extends EventStore {
   async requestData(params){
      const response = await fetch('https://api.bryntum.com/events/?' + new URLSearchParams(params));
      return await response.json();
   }
}
```

[unload](https://bryntum.com/docs/gantt/api/Scheduler/data/plugin/DateStoreLazyLoadPlugin#function-unload)
Only available if the store is configured as [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad).

The records matching the provided parameters will be removed from the Store and reloaded the next they are needed.

Provide an array of records or record ids, or provide a combination of resource records (or ids) and/or a date range. Do not combine the `records` params with the `resources` and `startDate` and `endDate` params.
