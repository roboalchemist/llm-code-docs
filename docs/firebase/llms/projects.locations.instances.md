# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances.md.txt

# REST Resource: projects.locations.instances

## Resource: DatabaseInstance

Representation of a Realtime Database instance. Details on interacting with contents of a DatabaseInstance can be found at: <https://firebase.google.com/docs/database/rest/start>.

|                                                                                                                                                                             JSON representation                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "project": string, "databaseUrl": string, "type": enum (https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstanceType), "state": enum (https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State) } ``` |

|                                                                                                                                                         Fields                                                                                                                                                         ||
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | `string` The fully qualified resource name of the database instance, in the form: `projects/{project-number}/locations/{location-id}/instances/{database-id}`.                                                                                                                                          |
| `project`     | `string` Output only. The resource name of the project this instance belongs to. For example: `projects/{project-number}`.                                                                                                                                                                              |
| `databaseUrl` | `string` Output only. Output Only. The globally unique hostname of the database.                                                                                                                                                                                                                        |
| `type`        | `enum (`[DatabaseInstanceType](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstanceType)`)` Immutable. The database instance type. On creation only USER_DATABASE is allowed, which is also the default when omitted. |
| `state`       | `enum (`[State](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State)`)` Output only. The database's lifecycle state. Read-only.                                                                                                 |

## DatabaseInstanceType

The possible types of a database instance.

|                                                                         Enums                                                                         ||
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `DATABASE_INSTANCE_TYPE_UNSPECIFIED` | Unknown state, likely the result of an error on the backend. This is only used for distinguishing unset values. |
| `DEFAULT_DATABASE`                   | The default database that is provisioned when a project is created.                                             |
| `USER_DATABASE`                      | A database that the user created.                                                                               |

## State

Database lifecycle states.

|                                                                       Enums                                                                        ||
|-------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `LIFECYCLE_STATE_UNSPECIFIED` | Unspecified state, likely the result of an error on the backend. This is only used for distinguishing unset values. |
| `ACTIVE`                      | The normal and active state.                                                                                        |
| `DISABLED`                    | The database is in a disabled state. It can be re-enabled later.                                                    |
| `DELETED`                     | The database is in a deleted state.                                                                                 |

|                                                                                                                                                                             ## Methods                                                                                                                                                                              ||
|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ### [create](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/create)     | Requests that a new [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance) be created.                          |
| ### [delete](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/delete)     | Marks a [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance) to be deleted.                                   |
| ### [disable](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/disable)   | Disables a [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance).                                              |
| ### [get](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/get)           | Gets the [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance) identified by the specified resource name.      |
| ### [list](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/list)         | Lists each [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance) associated with the specified parent project. |
| ### [reenable](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/reenable) | Enables a [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance).                                               |
| ### [undelete](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/undelete) | Restores a [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance) that was previously marked to be deleted.     |