# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/mixin/ProjectModelTimeZoneMixin.md

# [ProjectModelTimeZoneMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelTimeZoneMixin)

Mixin that holds TimeZone functionality shared between projects in Scheduler, Scheduler Pro, Gantt and Calendar

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[timeZone](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelTimeZoneMixin#config-timeZone)
Set to a IANA time zone (i.e. `Europe/Stockholm`) or a UTC offset in minutes (i.e. `-120`). This will convert all events, tasks and time ranges to the specified time zone or offset. It will also affect the displayed timeline's headers as well at the start and end date of it.

There is currently no built-in time zone support in JavaScript which means that the converted dates technically still are in the local system time zone, but adjusted to match the configured time zone.

### DST

If a IANA time zone is provided, there will be support for DST. But if local system time zone has DST that will affect the time zone conversion at the exact hour when the local system time zone switches DST on and off.

_For example:_

1. The local system time zone is `Europe/Stockholm` (which is UTC+1 or UTC+2 when DST).
2. The date `2022-03-27T07:00:00Z` (which is UTC) is converted to `America/Chicago` (which is UTC-6 or UTC-5 when DST).
3. The converted JS date will be created from `2022-03-27T02:00:00` which is exactly the hour when `Europe/Stockholm` adds an DST hour. This has the effect that the converted date shows up incorrectly as `2022-03-27T03:00` instead.

If a UTC offset is provided, there is no DST support at all.

### Editing

If creating new records or editing existing record dates, the dates will be interpreted as in the selected time zone.

If you want to create new records with dates that either should be interpreted as local system time zone or from any other time zone, specify the [timeZone](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/TimeZonedDatesMixin#field-timeZone) field on the record.

### Saving

When saving or syncing data, the dates will be restored to local system time and converted to JSON ISO formatted. When restoring, it adds or subtracts the time difference accordingly. For instance, if the current timezone is `UTC` and you're in UTC +3, 3 hours will be added to the time.

The `store.toJSON()` and `model.toJSON()` methods also restores the data. For example, `eventStore.toJSON()` will show the dates in local timezone.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectModelTimeZoneMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelTimeZoneMixin#property-isProjectModelTimeZoneMixin)
Identifies an object as an instance of [ProjectModelTimeZoneMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelTimeZoneMixin) class, or subclass thereof.

[isProjectModelTimeZoneMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelTimeZoneMixin#property-isProjectModelTimeZoneMixin-static)
Identifies an object as an instance of [ProjectModelTimeZoneMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelTimeZoneMixin) class, or subclass thereof.

[timeZone](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/ProjectModelTimeZoneMixin#property-timeZone)
Set to a IANA time zone (i.e. `Europe/Stockholm`) or a UTC offset in minutes (i.e. `-120`). This will convert all events, tasks and time ranges to the specified time zone or offset. It will also affect the displayed timeline's headers as well at the start and end date of it.

There is currently no built-in time zone support in JavaScript which means that the converted dates technically still are in the local system time zone, but adjusted to match the configured time zone.

### DST

If a IANA time zone is provided, there will be support for DST. But if local system time zone has DST that will affect the time zone conversion at the exact hour when the local system time zone switches DST on and off.

_For example:_

1. The local system time zone is `Europe/Stockholm` (which is UTC+1 or UTC+2 when DST).
2. The date `2022-03-27T07:00:00Z` (which is UTC) is converted to `America/Chicago` (which is UTC-6 or UTC-5 when DST).
3. The converted JS date will be created from `2022-03-27T02:00:00` which is exactly the hour when `Europe/Stockholm` adds an DST hour. This has the effect that the converted date shows up incorrectly as `2022-03-27T03:00` instead.

If a UTC offset is provided, there is no DST support at all.

### Editing

If creating new records or editing existing record dates, the dates will be interpreted as in the selected time zone.

If you want to create new records with dates that either should be interpreted as local system time zone or from any other time zone, specify the [timeZone](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/TimeZonedDatesMixin#field-timeZone) field on the record.

### Saving

When saving or syncing data, the dates will be restored to local system time and converted to JSON ISO formatted. When restoring, it adds or subtracts the time difference accordingly. For instance, if the current timezone is `UTC` and you're in UTC +3, 3 hours will be added to the time.

The `store.toJSON()` and `model.toJSON()` methods also restores the data. For example, `eventStore.toJSON()` will show the dates in local timezone.
