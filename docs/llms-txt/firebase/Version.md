# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version.md.txt

# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/Version.md.txt

Contains all metadata about a particular version of the Remote Config template.

All fields are set at the time the specified Remote Config template was written.

|                                                                                                                                                                                                                                          JSON representation                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "versionNumber": string, "updateTime": string, "updateUser": { object (https://firebase.google.com/docs/reference/remote-config/rest/v1/Version#RemoteConfigUser) }, "description": string, "updateOrigin": enum (https://firebase.google.com/docs/reference/remote-config/rest/v1/Version#RemoteConfigUpdateOrigin), "updateType": enum (https://firebase.google.com/docs/reference/remote-config/rest/v1/Version#RemoteConfigUpdateType), "rollbackSource": string, "isLegacy": boolean } ``` |

|                                                                                                                                                                                                                                  Fields                                                                                                                                                                                                                                  ||
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `versionNumber`  | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Output only. The version number of the version's corresponding Remote Config template.                                                                                                                                                                                                                                                                             |
| `updateTime`     | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the Remote Config template was written to the Remote Config server. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `updateUser`     | `object (`[RemoteConfigUser](https://firebase.google.com/docs/reference/remote-config/rest/v1/Version#RemoteConfigUser)`)` Output only. Aggregation of all metadata fields about the account that performed the update.                                                                                                                                                                                                                                |
| `description`    | `string` Optional. The user-provided description of the corresponding Remote Config template                                                                                                                                                                                                                                                                                                                                                           |
| `updateOrigin`   | `enum (`[RemoteConfigUpdateOrigin](https://firebase.google.com/docs/reference/remote-config/rest/v1/Version#RemoteConfigUpdateOrigin)`)` Output only. Where the update action originated.                                                                                                                                                                                                                                                              |
| `updateType`     | `enum (`[RemoteConfigUpdateType](https://firebase.google.com/docs/reference/remote-config/rest/v1/Version#RemoteConfigUpdateType)`)` Output only. What type of update was made.                                                                                                                                                                                                                                                                        |
| `rollbackSource` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Output only. Only present if this version is the result of a rollback, and will be the version number of the Remote Config template that was rolled-back to.                                                                                                                                                                                                       |
| `isLegacy`       | `boolean` Output only. `True` if this Remote Config template was published before version history was supported.                                                                                                                                                                                                                                                                                                                                       |

## RemoteConfigUser

All the fields associated with the person/service account that wrote a Remote Config template.

|                       JSON representation                       |
|-----------------------------------------------------------------|
| ``` { "name": string, "email": string, "imageUrl": string } ``` |

|                      Fields                      ||
|------------|--------------------------------------|
| `name`     | `string` Output only. Display name.  |
| `email`    | `string` Output only. Email address. |
| `imageUrl` | `string` Output only. Image URL.     |

## RemoteConfigUpdateOrigin

Where the [projects.updateRemoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/updateRemoteConfig#google.firebase.remoteconfig.v1.RemoteConfigService.UpdateRemoteConfig) action originated.

|                                                        Enums                                                        ||
|-------------------------------------------|--------------------------------------------------------------------------|
| `REMOTE_CONFIG_UPDATE_ORIGIN_UNSPECIFIED` | Catch-all for unrecognized values.                                       |
| `CONSOLE`                                 | The update came from the Firebase UI.                                    |
| `REST_API`                                | The update came from the Remote Config REST API.                         |
| `ADMIN_SDK_NODE`                          | This value is used when the update came from the Firebase Admin Node SDK |

## RemoteConfigUpdateType

What type of update was associated with the [Remote Config template version](https://firebase.google.com/docs/reference/remote-config/rest/v1/Version).

|                                                                                            Enums                                                                                            ||
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `REMOTE_CONFIG_UPDATE_TYPE_UNSPECIFIED` | Catch-all for unrecognized enum values.                                                                                                            |
| `INCREMENTAL_UPDATE`                    | A regular incremental update.                                                                                                                      |
| `FORCED_UPDATE`                         | A forced update. The ETag was specified as "\*" in an `UpdateRemoteConfigRequest` request or the "Force Update" button was pressed on the console. |
| `ROLLBACK`                              | A rollback to a previous Remote Config template.                                                                                                   |