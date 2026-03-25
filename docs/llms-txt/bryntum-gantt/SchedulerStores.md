# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/SchedulerStores.md

# [SchedulerStores](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores)

Functions for store assignment and store event listeners.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[store](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-store)
Overridden to _not_ auto create a store at the Scheduler level. The store is the [ResourceStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceStore) of the backing project

[startParamName](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-startParamName)
The name of the start date parameter that will be passed to in every `eventStore` load request.

[endParamName](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-endParamName)
The name of the end date parameter that will be passed to in every `eventStore` load request.

[passStartEndParameters](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-passStartEndParameters)
Set to `true` to include `startDate` and `endDate` params indicating the currently viewed date range in `EventStore` load requests (when loading using `AjaxStore` or `CrudManager` functionality).

Dates are formatted using the same format as the `startDate` field on the `EventModel` (e.g. 2023-03-08T00:00:00+01:00).

[crudManagerClass](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-crudManagerClass)
Class that should be used to instantiate a CrudManager in case it's provided as a simple object to [crudManager](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerStores#config-crudManager) config.

[crudManager](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-crudManager)
Supply a [CrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager) instance or a config object if you want to use CrudManager for handling data.

[timeRanges](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-timeRanges)
Inline time ranges, will be loaded into an internally created store if [TimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges) is enabled.

[timeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-timeRangeStore)
The time ranges store instance for [TimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges) feature.

[resourceTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-resourceTimeRanges)
Inline resource time ranges, will be loaded into an internally created store if [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) is enabled.

[resourceTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#config-resourceTimeRangeStore)
Resource time ranges store instance or config object for [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) feature.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerStores](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#property-isSchedulerStores)
Identifies an object as an instance of [SchedulerStores](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerStores) class, or subclass thereof.

[isSchedulerStores](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#property-isSchedulerStores-static)
Identifies an object as an instance of [SchedulerStores](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerStores) class, or subclass thereof.

[crudManager](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#property-crudManager)
Get/set the CrudManager instance

[timeRanges](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#property-timeRanges)
Get/set time ranges, applies to the backing project's TimeRangeStore.

[timeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#property-timeRangeStore)
Get/set the time ranges store instance or config object for [TimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges) feature.

[resourceTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#property-resourceTimeRanges)
Inline resource time ranges, will be loaded into an internally created store if [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) is enabled.

[resourceTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#property-resourceTimeRangeStore)
Get/set the resource time ranges store instance for [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) feature.

## Functions

Functions are methods available for calling on the class

[onEventStoreBatchedUpdate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#function-onEventStoreBatchedUpdate)
Listener to the batchedUpdate event which fires when a field is changed on a record which is batch updating. Occasionally UIs must keep in sync with batched changes. For example, the EventResize feature performs batched updating of the startDate/endDate and it tells its client to listen to batchedUpdate.

[onInternalEventStoreChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#function-onInternalEventStoreChange)
Calls appropriate functions for current event layout when the event store is modified.

[onEventCommit](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#function-onEventCommit)
Refreshes committed events, to remove dirty/committing flag. CSS is added

[onEventCommitStart](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#function-onEventCommitStart)
Adds the committing flag to changed events before commit.

[getResourcesEventsPerTick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerStores#function-getResourcesEventsPerTick)
Get events grouped by timeAxis ticks from resources array
