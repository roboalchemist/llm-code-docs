# Source: https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema.md.txt

<br />

This page provides the dataset schema for exported
Crashlytics data and Firebase sessions data in BigQuery.

Firebase creates new datasets in BigQuery for your exported data:

- [Crashlytics dataset](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema#dataset-schema-crashlytics)

- [Firebase sessions dataset](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema#dataset-schema-sessions) (if sessions data is
  enabled for export)

<br />

*** ** * ** ***

## Crashlytics dataset

Crashlytics data is exported into a BigQuery dataset named
`firebase_crashlytics`. The dataset covers your entire project, even if it has
multiple apps.

### Tables

By default, Firebase creates individual tables inside the Crashlytics
dataset for each app in your project that's linked to BigQuery.

The tables are named based on the app's identifier (with periods converted to
underscores) and appended with the app's platform (`_IOS` or `_ANDROID`). For
example, data for an Android app with the package name `com.google.test` would
be in a table named `com_google_test_ANDROID`.

> [!NOTE]
> **Note:** You may also choose to opt out of exporting data into BigQuery for specific apps in your project from within the Firebase console.

- If streaming export to BigQuery is enabled, then data will also be
  streamed in realtime to a table appended with `_REALTIME`
  (for example, `com_google_test_ANDROID_REALTIME`).

- Each row in a table represents an event that occurred in the app, including
  crashes, non-fatal errors, and ANRs.

- The tables contain a standard set of Crashlytics data in addition to any
  custom Crashlytics keys defined by you in your app
  ([iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#add-keys) \|
  [Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#add-keys) \|
  [Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#add-keys) \|
  [Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#add-keys)
  ).

### Rows

Each row in a table represents an error the app encountered.

### Columns

The columns in a table are identical for crashes, non-fatal errors, and ANRs.

- If streaming export to BigQuery is enabled, then the realtime table
  will have the same columns as the batch table.

- You might have columns in rows that represent events that don't have
  stack traces.

Here are the columns in the table for the exported Crashlytics data:

| Field name | Data type | Description |
|---|---|---|
| `app_orientation` | STRING | For example, `PORTRAIT`, `LANDSCAPE`, `FACE_UP`, `FACE_DOWN`, etc. |
| `application` | RECORD | The app that generated the event |
| `application.build_version` | STRING | The app's build version |
| `application.display_version` | STRING |   |
| `blame_frame` | RECORD | The frame identified as the root cause of the crash or error |
| `blame_frame.address` | INT64 | The address in the binary image which contains the code Unset for Java frames |
| `blame_frame.blamed` | BOOLEAN | Whether Crashlytics determined that this frame is the cause of the crash or error |
| `blame_frame.file` | STRING | The name of the frame file |
| `blame_frame.library` | STRING | The display name of the library that includes the frame |
| `blame_frame.line` | INT64 | The line number of the file of the frame |
| `blame_frame.offset` | INT64 | The byte offset into the binary image that contains the code Unset for Java exceptions |
| `blame_frame.owner` | STRING | For example, `DEVELOPER`, `VENDOR`, `RUNTIME`, `PLATFORM`, or `SYSTEM` |
| `blame_frame.symbol` | STRING | The hydrated symbol, or raw symbol if it's unhydrateable |
| `breadcrumbs` | REPEATED RECORD | Timestamped [Google Analytics breadcrumbs](https://firebase.google.com/docs/crashlytics/customize-crash-reports#get-breadcrumb-logs), if enabled |
| `breadcrumbs.name` | STRING | The name associated with the breadcrumb |
| `breadcrumbs.params` | REPEATED RECORD | Parameters associated with the breadcrumb |
| `breadcrumbs.params.key` | STRING | A parameter key associated with the breadcrumb |
| `breadcrumbs.params.value` | STRING | A parameter value associated with the breadcrumb |
| `breadcrumbs.timestamp` | TIMESTAMP | The timestamp associated with the breadcrumb |
| `bundle_identifier` | STRING | The unique identifier for the app as registered in the Firebase project (for example, `com.google.gmail`) For Apple platform apps, this is the bundle ID of the app. For Android apps, this is the package name of the app. |
| `crashlytics_sdk_versions` | STRING | The Crashlytics SDK version that generated the event |
| `custom_keys` | REPEATED RECORD | Developer-defined key-value pairs |
| `custom_keys.key` | STRING | A developer-defined key |
| `custom_keys.value` | STRING | A developer-defined value |
| `device` | RECORD | The device the event occurred on |
| `device_orientation` | STRING | For example, `PORTRAIT`, `LANDSCAPE`, `FACE_UP`, `FACE_DOWN`, etc. |
| `device.architecture` | STRING | For example, `X86_32`, `X86_64`, `ARMV7`, `ARM64`, `ARMV7S`, or `ARMV7K` |
| `device.manufacturer` | STRING | The device manufacturer |
| `device.model` | STRING | The device model |
| `error` | REPEATED RECORD | *(Apple apps only)* non-fatal errors |
| `error_type` | STRING | The error type of the event (for example, `FATAL`, `NON_FATAL`, `ANR`, etc.) |
| `error.blamed` | BOOLEAN | Whether Crashlytics determined that this frame is the cause of the error |
| `error.code` | INT64 | Error code associated with the app's custom logged NSError |
| `error.frames` | REPEATED RECORD | The frames of the stacktrace |
| `error.frames.address` | INT64 | The address in the binary image which contains the code |
| `error.frames.blamed` | BOOLEAN | Whether Crashlytics determined that this frame is the cause of the error |
| `error.frames.file` | STRING | The name of the frame file |
| `error.frames.library` | STRING | The display name of the library that includes the frame |
| `error.frames.line` | INT64 | The line number of the file of the frame |
| `error.frames.offset` | INT64 | The byte offset into the binary image that contains the code |
| `error.frames.owner` | STRING | For example, `DEVELOPER`, `VENDOR`, `RUNTIME`, `PLATFORM`, or `SYSTEM` |
| `error.frames.symbol` | STRING | The hydrated symbol, or raw symbol if it's unhydrateable |
| `error.queue_name` | STRING | The queue the thread was running on |
| `error.subtitle` | STRING | The subtitle of the thread |
| `error.title` | STRING | The title of the thread |
| `event_id` | STRING | The unique ID for the event |
| `event_timestamp` | TIMESTAMP | When the event occurred |
| `exceptions` | REPEATED RECORD | *(Android only)* Exceptions that occurred during this event. Nested exceptions are presented in reverse chronological order, which means that the last record is the first exception thrown |
| `exceptions.blamed` | BOOLEAN | True if Crashlytics determines the exception is responsible for the error or crash |
| `exceptions.exception_message` | STRING | A message associated with the exception |
| `exceptions.frames` | REPEATED RECORD | The frames associated with the exception |
| `exceptions.frames.address` | INT64 | The address in the binary image which contains the code Unset for Java frames |
| `exceptions.frames.blamed` | BOOLEAN | Whether Crashlytics determined that this frame is the cause of the crash or error |
| `exceptions.frames.file` | STRING | The name of the frame file |
| `exceptions.frames.library` | STRING | The display name of the library that includes the frame |
| `exceptions.frames.line` | INT64 | The line number of the file of the frame |
| `exceptions.frames.offset` | INT64 | The byte offset into the binary image that contains the code Unset for Java exceptions |
| `exceptions.frames.owner` | STRING | For example, `DEVELOPER`, `VENDOR`, `RUNTIME`, `PLATFORM`, or `SYSTEM` |
| `exceptions.frames.symbol` | STRING | The hydrated symbol, or raw symbol if it's unhydrateable |
| `exceptions.nested` | BOOLEAN | True for all but the last-thrown exception (meaning the first record) |
| `exceptions.subtitle` | STRING | The subtitle of the thread |
| `exceptions.title` | STRING | The title of the thread |
| `exceptions.type` | STRING | The exception type (for example, `java.lang.IllegalStateException)` |
| `firebase_session_id` | STRING | The automatically generated ID for the Firebase session mapped to the event from Crashlytics |
| `installation_uuid` | STRING | An ID that identifies a unique app and device installation |
| `is_fatal` | BOOLEAN | > [!NOTE] > This field is deprecated. Use `error_type` instead. Whether the app crashed |
| `issue_id` | STRING | The issue associated with the event |
| `logs` | REPEATED RECORD | Timestamped log messages generated by the Crashlytics logger, if enabled |
| `logs.message` | STRING | The logged message |
| `logs.timestamp` | TIMESTAMP | When the log was made |
| `memory` | RECORD | The device's memory status |
| `memory.free` | INT64 | Bytes of memory remaining |
| `memory.used` | INT64 | Bytes of memory used |
| `operating_system` | RECORD | The details of the OS on the device |
| `operating_system.device_type` | STRING | The type of device (for example, `MOBILE`, `TABLET`, `TV`, etc.); also known as "device category" |
| `operating_system.display_version` | STRING | The version of the OS on the device |
| `operating_system.modification_state` | STRING | Whether the device has been modified (for example, a jailbroken app is `MODIFIED` and a rooted app is `UNMODIFIED`) |
| `operating_system.name` | STRING | The name of the OS on the device |
| `operating_system.type` | STRING | *(Apple apps only)* The type of OS running on the device (for example, `IOS`, `MACOS`, etc.) |
| `platform` | STRING | The platform of the app as registered in the Firebase project (valid values: `IOS` or `ANDROID`) |
| `process_state` | STRING | `BACKGROUND` or `FOREGROUND` |
| `storage` | RECORD | The device's persistent storage |
| `storage.free` | INT64 | Bytes of storage remaining |
| `storage.used` | INT64 | Bytes of storage used |
| `threads` | REPEATED RECORD | Threads present at the time of the event |
| `threads.blamed` | BOOLEAN | Whether Crashlytics determined that this frame is the cause of the crash or error |
| `threads.code` | INT64 | *(Apple apps only)* Error code of the application's custom logged NSError |
| `threads.crash_address` | INT64 | The address of the signal that caused the application to crash; only present on crashed native threads |
| `threads.crashed` | BOOLEAN | Whether the thread crashed |
| `threads.frames` | REPEATED RECORD | The frames of the thread |
| `threads.frames.address` | INT64 | The address in the binary image which contains the code |
| `threads.frames.blamed` | BOOLEAN | Whether Crashlytics determined that this frame is the cause of the error |
| `threads.frames.file` | STRING | The name of the frame file |
| `threads.frames.library` | STRING | The display name of the library that includes the frame |
| `threads.frames.line` | INT64 | The line number of the file of the frame |
| `threads.frames.offset` | INT64 | The byte offset into the binary image that contains the code |
| `threads.frames.owner` | STRING | For example, `DEVELOPER`, `VENDOR`, `RUNTIME`, `PLATFORM`, or `SYSTEM` |
| `threads.frames.symbol` | STRING | The hydrated symbol, or raw symbol if it's unhydreatable |
| `threads.queue_name` | STRING | *(Apple apps only)* The queue the thread was running on |
| `threads.signal_code` | STRING | The code of the signal that caused the app to crash; only present on crashed native threads |
| `threads.signal_name` | STRING | The name of the signal that caused the app to crash, only present on crashed native threads |
| `threads.subtitle` | STRING | The subtitle of the thread |
| `threads.thread_name` | STRING | The thread's name |
| `threads.title` | STRING | The title of the thread |
| `unity_metadata.debug_build` | BOOLEAN | If this is a debug build |
| `unity_metadata.graphics_copy_texture_support` | STRING | Support for copying graphics texture as defined in the [Unity API](https://docs.unity3d.com/ScriptReference/Rendering.CopyTextureSupport.html) |
| `unity_metadata.graphics_device_id` | INT64 | The identifier of the graphics device |
| `unity_metadata.graphics_device_name` | STRING | The name of the graphics device |
| `unity_metadata.graphics_device_type` | STRING | The type of the graphics device |
| `unity_metadata.graphics_device_vendor_id` | INT64 | The identifier of the graphics processor's vendor |
| `unity_metadata.graphics_device_vendor` | STRING | The vendor of the graphics device |
| `unity_metadata.graphics_device_version` | STRING | The version of the graphics device |
| `unity_metadata.graphics_max_texture_size` | INT64 | The maximum size dedicated to rendering texture |
| `unity_metadata.graphics_memory_size_mb` | INT64 | The graphics memory in MB |
| `unity_metadata.graphics_render_target_count` | INT64 | The number of graphical rendering targets |
| `unity_metadata.graphics_shader_level` | INT64 | The shader level of the graphics |
| `unity_metadata.processor_count` | INT64 | The number of processors (cores) |
| `unity_metadata.processor_frequency_mhz` | INT64 | The frequency of the processor(s) in MHz |
| `unity_metadata.processor_type` | STRING | The type of processor |
| `unity_metadata.screen_refresh_rate_hz` | INT64 | The refresh rate of the screen in Hz |
| `unity_metadata.screen_resolution_dpi` | STRING | The DPI of the screen as a floating point number |
| `unity_metadata.screen_size_px` | STRING | The size of the screen in pixels, formatted as width x height |
| `unity_metadata.system_memory_size_mb` | INT64 | The size of the system's memory in Mb |
| `unity_metadata.unity_version` | STRING | The version of Unity running on this device |
| `user` | RECORD | *(Optional)* Info collected about the app's user |
| `user.email` | STRING | > [!NOTE] > This field is deprecated; do not use this field. *(Optional)* The user's email address |
| `user.id` | STRING | *(Optional)* An app-specific ID associated with the user |
| `user.name` | STRING | > [!NOTE] > This field is deprecated; do not use this field. *(Optional)* The user's name |
| `variant_id` | STRING | The issue variant associated with this event Note that not all events have an associated issue variant. |

<br />

*** ** * ** ***

## Firebase sessions dataset

Firebase sessions data is exported into a BigQuery dataset named
`firebase_sessions`. The dataset covers your entire project, even if it has
multiple apps.

### Tables

By default, Firebase creates individual tables inside the Firebase sessions
dataset for each app in your project that's linked to BigQuery.

The tables are named based on the app's identifier (with periods converted to
underscores) and appended with the app's platform (`_IOS` or `_ANDROID`).
For example, data for an Android app with the package name `com.google.test`
would be in a table named `com_google_test_ANDROID`.

### Rows

Each row in a table represents a session event that happened.

### Columns

If streaming export to BigQuery is enabled, then the realtime table
will have the same columns as the batch table.

Here are the columns within the table for the exported Firebase sessions data:

| Field name | Data type | Description |
|---|---|---|
| `instance_id` | STRING | The Firebase installation ID (FID) from the device. Identifies a unique app + device installation |
| `session_id` | STRING | The unique ID of this session |
| `first_session_id` | STRING | The first ID of a series of sessions this session is in since the app was cold started. This can be used to group all sessions that have occurred since a cold start. If this session is the first session, this field will be the same as `session_id`. |
| `session_index` | INTEGER | The order this session came in after the app was cold started. For the first session after a cold start, this will be `0`. The index will be incremented every time a session is generated without a cold start occurring (for example, after 30 mins of inactivity). |
| `event_type` | STRING | The type of event that happened in the session (for example, `SESSION_START`) |
| `event_timestamp` | TIMESTAMP | The time of the event's occurrence |
| `received_timestamp` | TIMESTAMP | The time the event was received by the server from the device |
| `performance_data_collection_enabled` | BOOLEAN | Whether the Firebase Performance Monitoring SDK data collection was enabled at the time of the session |
| `crashlytics_data_collection_enabled` | BOOLEAN | Whether the Firebase Crashlytics SDK data collection was enabled at the time of the session |
| `application` | RECORD | Describes the application |
| `application.build_version` | STRING | The build version of the application (for example, `1523456`) |
| `application.display_version` | STRING | The display version of the application (for example, `4.1.7`) |
| `device` | RECORD | The device on which the event occurred |
| `device.model` | STRING | The model of the device |
| `device.manufacturer` | STRING | The manufacturer of the device. For Apple platform apps, this will be `NULL`. |
| `operating_system` | RECORD | Describes the OS of the device |
| `operating_system.display_version` | STRING | The display version of the operating system (for example, `10.2.1`) |
| `operating_system.name` | STRING | The name of the operating system |
| `operating_system.type` | STRING | The type of the operating system (for example, `IOS`). This field is only set for Apple devices. |
| `operating_system.device_type` | STRING | The type of device (for example, `MOBILE`, `TABLET`, `TV`) |