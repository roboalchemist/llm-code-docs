# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds.md.txt

# REST Resource: projects.databases.userCreds

## Resource: UserCreds

A Cloud Firestore User Creds.

|                                                                                                                                                                                                                                            JSON representation                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "createTime": string, "updateTime": string, "state": enum (https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds#State), "securePassword": string, // Union field `UserCredsIdentity` can be only one of the following: "resourceIdentity": { object (https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds#ResourceIdentity) } // End of list of possible types for union field `UserCredsIdentity`. } ``` |

|                                                                                                                                                                                                                    Fields                                                                                                                                                                                                                    ||
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`             | `string` Identifier. The resource name of the UserCreds. Format: `projects/{project}/databases/{database}/userCreds/{userCreds}`                                                                                                                                                                                                                                                                                         |
| `createTime`       | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the user creds were created. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.      |
| `updateTime`       | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the user creds were last updated. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `state`            | `enum (`[State](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds#State)`)` Output only. Whether the user creds are enabled or disabled. Defaults to ENABLED on creation.                                                                                                                                                                                                        |
| `securePassword`   | `string` Output only. The plaintext server-generated password for the user creds. Only populated in responses for userCreds.create and userCreds.resetPassword.                                                                                                                                                                                                                                                          |
| Union field `UserCredsIdentity`. Identity associated with this User Creds. `UserCredsIdentity` can be only one of the following:                                                                                                                                                                                                                                                                                                             ||
| `resourceIdentity` | `object (`[ResourceIdentity](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds#ResourceIdentity)`)` Resource Identity descriptor.                                                                                                                                                                                                                                                |

## State

The state of the user creds (ENABLED or DISABLED).

|                            Enums                            ||
|---------------------|----------------------------------------|
| `STATE_UNSPECIFIED` | The default value. Should not be used. |
| `ENABLED`           | The user creds are enabled.            |
| `DISABLED`          | The user creds are disabled.           |

## ResourceIdentity

Describes a Resource Identity principal.

|       JSON representation       |
|---------------------------------|
| ``` { "principal": string } ``` |

|                                                             Fields                                                             ||
|-------------|-------------------------------------------------------------------------------------------------------------------|
| `principal` | `string` Output only. Principal identifier string. See: <https://cloud.google.com/iam/docs/principal-identifiers> |

|                                                                             ## Methods                                                                             ||
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| ### [create](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/create)               | Create a user creds.                 |
| ### [delete](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/delete)               | Deletes a user creds.                |
| ### [disable](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/disable)             | Disables a user creds.               |
| ### [enable](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/enable)               | Enables a user creds.                |
| ### [get](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/get)                     | Gets a user creds resource.          |
| ### [list](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/list)                   | List all user creds in the database. |
| ### [resetPassword](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/resetPassword) | Resets the password of a user creds. |