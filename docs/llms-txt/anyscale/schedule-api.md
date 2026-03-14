# Source: https://docs.anyscale.com/reference/schedule-api.md

# Source: https://docs.anyscale.com/archive/ref/schedule-api.md

# Schedule API Reference (Legacy)

[View Markdown](/archive/ref/schedule-api.md)

# Schedule API Reference (Legacy)

warning

These methods are deprecated and will be fully removed from the Anyscale platform on January 29, 2026. To continue using these methods, install Anyscale CLI version 0.26.72 or earlier. Please use the [current APIs](/reference/schedule-api.md) instead.

## Schedule CLI[​](#schedule-cli "Direct link to Schedule CLI")

### `anyscale schedule create` Deprecated[​](#anyscale-schedule-create-deprecated "Direct link to anyscale-schedule-create-deprecated")

Deprecated

`anyscale schedule create` has been deprecated. and will be removed on 2025-10-01. Please use `anyscale schedule apply` instead.

**Usage**

`anyscale schedule create [OPTIONS] SCHEDULE_CONFIG_FILE`

\[DEPRECATED - use 'apply' instead] Create a schedule.

**Options**

* **`--name/-n`**: Name of the schedule.
* **`--description`**: Description of schedule.

### `anyscale schedule update` Deprecated[​](#anyscale-schedule-update-deprecated "Direct link to anyscale-schedule-update-deprecated")

Deprecated

`anyscale schedule update` has been deprecated. and will be removed on 2025-10-01. Please use `anyscale schedule apply` instead.

**Usage**

`anyscale schedule update [OPTIONS] SCHEDULE_CONFIG_FILE`

\[DEPRECATED - use 'apply' instead] Update a schedule.

**Options**

* **`--name/-n`**: Name of the schedule.
* **`--description`**: Description of schedule.

## Schedule SDK[​](#schedule-sdk "Direct link to Schedule SDK")

The AnyscaleSDK class must be constructed in order to make calls to the SDK. This class allows you to create an authenticated client in which to use the SDK.

| Param        | Type            | Description                                                                                                                                                                                                                                                                   |
| ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_token` | Optional String | Authentication token used to verify you have permissions to access Anyscale. If not provided, permissions default to the credentials set for your current user. Credentials can be set by following the instructions on this page: <https://console.anyscale.com/credentials> |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK()
```

### `create_or_update_schedule`[​](#create_or_update_schedule "Direct link to create_or_update_schedule")

Create or update a Schedule

Parameters

| Name              | Type           | Description | Notes |
| ----------------- | -------------- | ----------- | ----- |
| `create_schedule` | CreateSchedule |             |       |

Returns ScheduleapimodelResponse

### `get_schedule`[​](#get_schedule "Direct link to get_schedule")

Get Schedules

Parameters

| Name          | Type | Description | Notes            |
| ------------- | ---- | ----------- | ---------------- |
| `schedule_id` | str  |             | Defaults to null |

Returns ScheduleapimodelResponse

### `pause_schedule`[​](#pause_schedule "Direct link to pause_schedule")

Pause a Schedule

Parameters

| Name             | Type          | Description | Notes            |
| ---------------- | ------------- | ----------- | ---------------- |
| `schedule_id`    | str           |             | Defaults to null |
| `pause_schedule` | PauseSchedule |             |                  |

Returns ScheduleapimodelResponse

### `run_schedule`[​](#run_schedule "Direct link to run_schedule")

Run a Schedule manually

Parameters

| Name          | Type | Description | Notes            |
| ------------- | ---- | ----------- | ---------------- |
| `schedule_id` | str  |             | Defaults to null |

Returns ProductionjobResponse

### `list_schedules`[​](#list_schedules "Direct link to list_schedules")

List Schedules

Parameters

| Name         | Type         | Description              | Notes            |
| ------------ | ------------ | ------------------------ | ---------------- |
| `project_id` | optional str | project\_id to filter by | Defaults to null |
| `name`       | optional str | name to filter by        | Defaults to null |
| `creator_id` | optional str | filter by creator id     | Defaults to null |

Returns ScheduleapimodelListResponse
