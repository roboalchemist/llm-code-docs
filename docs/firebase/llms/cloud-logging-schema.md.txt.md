# Source: https://firebase.google.com/docs/crashlytics/cloud-logging-schema.md.txt

<br />

This page provides the log schema for exported
Crashlytics data and Firebase sessions data in Cloud Logging.

- [Crashlytics schema](https://firebase.google.com/docs/crashlytics/cloud-logging-schema#crashlytics)

- [Firebase sessions schema](https://firebase.google.com/docs/crashlytics/cloud-logging-schema#sessions) (if sessions data is enabled for export)

- [Device log schema](https://firebase.google.com/docs/crashlytics/cloud-logging-schema#device-log)

<br />

*** ** * ** ***

## Crashlytics schema

### `Event`

The message describing a single Crashlytics event.

JSON representation

    {
      "name": string,
      "platform": string,
      "bundleOrPackage": string,
      "eventId": string,
      "sessionId": string,
      "eventTime": string,
      "receivedTime": string,
      "issue": {
        object (Issue)
      },
      "issueVariant": {
        object (IssueVariant)
      },
      "device": {
        object (Device)
      },
      "memory": {
        object (Memory)
      },
      "storage": {
        object (Storage)
      },
      "operatingSystem": {
        object (OperatingSystem)
      },
      "browser": {
        object (Browser)
      },
      "version": {
        object (Version)
      },
      "user": {
        object (User)
      },
      "customKeys": {
        string: string,
        ...
      },
      "installationUuid": string,
      "crashlyticsSdkVersion": string,
      "appOrientation": string,
      "deviceOrientation": string,
      "logs": [
        {
          object (Log)
        }
      ],
      "breadcrumbs": [
        {
          object (Breadcrumb)
        }
      ],
      "blameFrame": {
        object (Frame)
      },
      "exceptions": [
        {
          object (Exception)
        }
      ],
      "errors": [
        {
          object (Error)
        }
      ],
      "threads": [
        {
          object (Thread)
        }
      ],
      "processState": string,
      "issueTitle": string,
      "issueSubtitle": string,
      "buildStamp": string
    }

| Fields | Description |
|---|---|
| `name` | `string` **Required.** **Output only.** **Immutable.** **Identifier.** The name of the event resource. Format: `projects/{project}/apps/{app_id}/events/{event}`. |
| `platform` | `string` Mobile platform (Android or iOS). |
| `bundleOrPackage` | `string` The bundle name for iOS apps or the package name of Android apps. Format: `com.mycompany.myapp`. |
| `eventId` | `string` **Output only.** **Immutable.** The unique event identifier is assigned during processing. |
| `sessionId` | `string` Unique identifier for the Firebase session. |
| `eventTime` | `string (Timestamp format)` Device timestamp at which the event was recorded. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30". |
| `receivedTime` | `string (Timestamp format)` Server timestamp at which the event was received by Crashlytics. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30". |
| `state_update_time` | `string (Timestamp format)` The time that the issue state was last changed. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30". |
| `first_seen_version` | `string` The first app display_version in which this issue was seen, populated for mobile issues only. |
| `last_seen_version` | `string` The most recent app display_version in which this issue was seen, populated for mobile issues only. |
| `first_time_seen` | `string (Timestamp format)` The first time this issue was seen. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30". |
| `last_time_seen` | `string (Timestamp format)` The most recent time the issue was seen. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30". |
| `issue` | `object (Issue)` Details for the \[Issue\] assigned to this \[Event\]. |
| `issueVariant` | `object (IssueVariant)` Details for the \[IssueVariant\] assigned to this \[Event\]. |
| `device` | `object (Device)` Mobile device metadata. |
| `memory` | `object (Memory)` Mobile device memory usage. |
| `storage` | `object (Storage)` Mobile device disk/flash usage. |
| `operatingSystem` | `object (OperatingSystem)` Operating system and version. |
| `browser` | `object (Browser)` Browser and version. |
| `version` | `object (Version)` Mobile application version. |
| `user` | `object (User)` End user identifiers for the device owner. |
| `customKeys` | `map (key: string, value: string)` Custom keys set by the developer during the session. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. |
| `installationUuid` | `string` Unique identifier for the device-app installation. This field is used to compute the unique number of impacted users. |
| `crashlyticsSdkVersion` | `string` Crashlytics SDK version. |
| `appOrientation` | `string` App orientation at the time of the crash (portrait or landscape). |
| `deviceOrientation` | `string` Device orientation at the time of the crash (portrait or landscape). |
| `logs[]` | `object (Log)` Log messages recorded by the developer during the session. |
| `breadcrumbs[]` | `object (Breadcrumb)` Analytics events recorded by the analytics SDK during the session. |
| `blameFrame` | `object (Frame)` The stack trace frame blamed by Crashlytics processing. May not be present in future analyzer. |
| `exceptions[]` | `object (Exception)` Android only. Exceptions that occurred during this event. Nested exceptions are presented in reverse chronological order, so that the last record is the first exception thrown. |
| `errors[]` | `object (Error)` Apple only. A non-fatal error captured by the iOS SDK and its stacktrace. |
| `threads[]` | `object (Thread)` Application threads present at the time the event was recorded. Each contains a stacktrace. One thread will be blamed for the error. |
| `processState` | `string` The state of the app process at the time of the event. |
| `issueTitle` | `string` The title of the issue in which the event was grouped. This is usually a source file or method name. |
| `issueSubtitle` | `string` The subtitle of the issue in which the event was grouped. This is usually a symbol or an exception message. |
| `buildStamp` | `string` Metadata provided by the app's build system, including version control repository info. |

### `Memory`

Mobile device memory usage.

JSON representation

    {
      "used": string,
      "free": string
    }

| Fields | Description |
|---|---|
| `used` | `string (int64 format)` Bytes in use. |
| `free` | `string (int64 format)` Bytes free. |

### `Storage`

Mobile device disk/flash usage. Not reported for all devices.

JSON representation

    {
      "used": string,
      "free": string
    }

| Fields | Description |
|---|---|
| `used` | `string (int64 format)` Bytes used. |
| `free` | `string (int64 format)` Bytes free. |

### `User`

Developer-provided end user identifiers.

JSON representation

    {
      "id": string
    }

| Fields | Description |
|---|---|
| `id` | `string` User id if provided by the app developer. |

### `Frame`

A frame in a stacktrace.

JSON representation

    {
      "line": string,
      "file": string,
      "symbol": string,
      "offset": string,
      "address": string,
      "library": string,
      "owner": string,
      "blamed": boolean
    }

| Fields | Description |
|---|---|
| `line` | `string (int64 format)` The line number in the file of the frame. |
| `file` | `string` The name of the source file in which the frame is found. |
| `symbol` | `string` The frame symbol after it has been deobfuscated or symbolicated. The raw symbol from the device if it could not be hydrated. |
| `offset` | `string (int64 format)` The byte offset into the binary image that contains the code. Present for native frames. |
| `address` | `string (int64 format)` The address in the binary image which contains the code. Present for native frames. |
| `library` | `string` The display name of the library that includes the frame. |
| `owner` | `string` One of DEVELOPER, VENDOR, RUNTIME, PLATFORM, or SYSTEM. |
| `blamed` | `boolean` True when the Crashlytics analysis has determined that this frame is likely to be the cause of the error. |

### `Exception`

A Java exception and its stacktrace, only from Android apps.

JSON representation

    {
      "type": string,
      "exceptionMessage": string,
      "nested": boolean,
      "title": string,
      "subtitle": string,
      "blamed": boolean,
      "frames": [
        {
          object (Frame)
        }
      ]
    }

| Fields | Description |
|---|---|
| `type` | `string` The exception type e.g. java.lang.IllegalStateException. |
| `exceptionMessage` | `string` A message associated with the exception. |
| `nested` | `boolean` True for all but the last-thrown exception (i.e. the first record). |
| `title` | `string` The title of the exception. |
| `subtitle` | `string` The subtitle of the exception. |
| `blamed` | `boolean` True when the Crashlytics analysis has determined that this thread is where the fault occurred. |
| `frames[]` | `object (Frame)` The frames in the exception's stacktrace. |

### `Error`

A non-fatal error and its stacktrace, only from Apple apps.

JSON representation

    {
      "queue": string,
      "code": string,
      "title": string,
      "subtitle": string,
      "blamed": boolean,
      "frames": [
        {
          object (Frame)
        }
      ]
    }

| Fields | Description |
|---|---|
| `queue` | `string` The queue on which the thread was running. |
| `code` | `string (int64 format)` Error code associated with the app's custom logged NSError. |
| `title` | `string` The title of the error. |
| `subtitle` | `string` The subtitle of the error. |
| `blamed` | `boolean` True when the Crashlytics analysis has determined that the stacktrace in this error is where the fault occurred. |
| `frames[]` | `object (Frame)` The frames in the error's stacktrace. |

### `Thread`

An application thread.

    JSON representation</code></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>{
      "crashed": boolean,
      "name": string,
      "queue": string,
      "signal": string,
      "signalCode": string,
      "crashAddress": string,
      "title": string,
      "subtitle": string,
      "blamed": boolean,
      "frames": [
        {
          object (Frame)
        }
      ],
      "threadId": string,
      "sysThreadId": string,
      "threadState": enum (State)
    }

| Fields | Description |
|---|---|
| `crashed` | `boolean` True when the thread has crashed. |
| `name` | `string` The name of the thread. |
| `queue` | `string` The queue on which the thread was running. |
| `signal` | `string` The name of the signal that caused the app to crash. Only present on crashed native threads. |
| `signalCode` | `string` The code of the signal that caused the app to crash. Only present on crashed native threads. |
| `crashAddress` | `string (int64 format)` The address of the signal that caused the application to crash. Only present on crashed native threads. |
| `title` | `string` The title of the thread. |
| `subtitle` | `string` The subtitle of the thread. |
| `blamed` | `boolean` True when the Crashlytics analysis has determined that the stacktrace in this thread is where the fault occurred. |
| `frames[]` | `object (Frame)` The frames in the thread's stacktrace. |
| `threadId` | `string (int64 format)` The id of the thread, only available for ANR threads. |
| `sysThreadId` | `string (int64 format)` The system id of the thread, only available for ANR threads. |
| `threadState` | `enum (State)` **Output only.** The state of the thread at the time the ANR occurred. |

### `State`

The state of a thread when the ANR occurred.

| Enums | Description |
|---|---|
| `STATE_UNSPECIFIED` | Thread state unspecified. |
| `THREAD_STATE_TERMINATED` | Thread was terminated. |
| `THREAD_STATE_RUNNABLE` | Thread was runnable. |
| `THREAD_STATE_TIMED_WAITING` | Thread was waiting with a timeout. |
| `THREAD_STATE_BLOCKED` | Thread was blocked. |
| `THREAD_STATE_WAITING` | Thread was waiting. |
| `THREAD_STATE_NEW` | Thread was started, yet to run anything. |
| `THREAD_STATE_NATIVE_RUNNABLE` | The thread was native and we could not heuristically determine that it was was waiting, so assume it's runnable. |
| `THREAD_STATE_NATIVE_WAITING` | We heuristically determined that the thread is waiting. |

<br />

*** ** * ** ***

## Firebase sessions schema

### `FirebaseSessionEvent`

Sessions recorded by the Firebase App Quality Sessions SDK.

JSON representation

    {
      "sessionId": string,
      "eventType": enum (SessionEventType),
      "firstSessionId": string,
      "sessionIndex": integer,
      "firebaseInstallationId": string,
      "eventTime": string,
      "version": {
        object (Version)
      },
      "device": {
        object (Device)
      },
      "operatingSystem": {
        object (OperatingSystem)
      }
    }

| Fields | Description |
|---|---|
| `sessionId` | `string` Unique identifier for the Firebase session. |
| `eventType` | `enum (SessionEventType)` Session event type. The SDK only supports SESSION_START events at this time. |
| `firstSessionId` | `string` The identifier of the first session since the last cold start. This id and the sessionId will be the same for app launches. |
| `sessionIndex` | `integer` Indicates the number of sessions since the last cold start. |
| `firebaseInstallationId` | `string` Uniquely identifies a device with Firebase apps installed. |
| `eventTime` | `string (Timestamp format)` The start timestamp for the session event. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30". |
| `version` | `object (Version)` Mobile application version numbers. |
| `device` | `object (Device)` Mobile device metadata. |
| `operatingSystem` | `object (OperatingSystem)` Operating system and version. |

### `SessionEventType`

Types of `SessionEvent` that are recorded.

| Enums | Description |
|---|---|
| `SESSION_EVENT_TYPE_UNKNOWN` | Unknown. |
| `SESSION_START` | Application session started. |

<br />

*** ** * ** ***

## Device Log schema

### `DeviceLog`

Represents the structure of the deviceLog entries.

JSON representation

    {
      "eventId": string,
      "sessionId": string,

      // Union field payload can be only one of the following:
      "log": {
        object (Log)
      },
      "breadcrumb": {
        object (Breadcrumb)
      }
      // End of list of possible types for union field payload.
    }

| Fields | Description |
|---|---|
| `eventId` | `string` **Output only.** **Immutable.** The identifier of the event to which this is associated. |
| `sessionId` | `string` Unique identifier for the Firebase session. |
| Union field `payload`. Payload can either be a Crashlytics log or a Breadcrumb. `payload` can be only one of the following: ||
| `log` | `object (Log)` Crashlytics log. |
| `breadcrumb` | `object (Breadcrumb)` Crashlytics breadcrumb. |

### `Log`

Developer-provided log lines recorded during the session.

JSON representation

    {
      "logTime": string,
      "message": string
    }

| Fields | Description |
|---|---|
| `logTime` | `string (Timestamp format)` Device timestamp when the line was logged. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30". |
| `message` | `string` Log message. |

### `Breadcrumb`

Analytics events recorded during the session.

JSON representation

    {
      "eventTime": string,
      "title": string,
      "params": {
        string: string,
        ...
      }
    }

| Fields | Description |
|---|---|
| `eventTime` | `string (Timestamp format)` Device timestamp for the event. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30". |
| `title` | `string` Analytic event name. |
| `params` | `map (key: string, value: string)` Event parameters. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. |