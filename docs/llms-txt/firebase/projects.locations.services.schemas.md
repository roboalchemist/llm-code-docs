# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas.md.txt

# REST Resource: projects.locations.services.schemas

## Resource: Schema

The application schema of a Firebase Data Connect service.

|                                                                                                                                                                                                                                  JSON representation                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "createTime": string, "updateTime": string, "labels": { string: string, ... }, "annotations": { string: string, ... }, "datasources": [ { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#Datasource) } ], "source": { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/Source) }, "uid": string, "reconciling": boolean, "displayName": string, "etag": string } ``` |

|                                                                                                                                                                         Fields                                                                                                                                                                         ||
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`          | `string` Identifier. The relative resource name of the schema, in the format: projects/{project}/locations/{location}/services/{service}/schemas/{schema} Right now, the only supported schema is "main".                                                                                                                             |
| `createTime`    | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. \[Output only\] Create time stamp. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |
| `updateTime`    | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. \[Output only\] Update time stamp. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |
| `labels`        | `map (key: string, value: string)` Optional. Labels as key value pairs. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.                                                                                                                                          |
| `annotations`   | `map (key: string, value: string)` Optional. Stores small amounts of arbitrary data. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.                                                                                                                             |
| `datasources[]` | `object (`[Datasource](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#Datasource)`)` Required. The data sources linked in the schema.                                                                                                                                        |
| `source`        | `object (`[Source](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/Source)`)` Required. The source files that comprise the application schema.                                                                                                                                                                    |
| `uid`           | `string` Output only. System-assigned, unique identifier.                                                                                                                                                                                                                                                                             |
| `reconciling`   | `boolean` Output only. A field that if true, indicates that the system is working to compile and deploy the schema.                                                                                                                                                                                                                   |
| `displayName`   | `string` Optional. Mutable human-readable name. 63 character limit.                                                                                                                                                                                                                                                                   |
| `etag`          | `string` Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. [AIP-154](https://google.aip.dev/154)                                                                                 |

## Datasource

A data source that backs Firebase Data Connect services.

|                                                                                                                                     JSON representation                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { // Union field `configuration` can be only one of the following: "postgresql": { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#PostgreSql) } // End of list of possible types for union field `configuration`. } ``` |

|                                                                                         Fields                                                                                         ||
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Union field `configuration`. Settings and configurations of the underlying data source. `configuration` can be only one of the following:                                              ||
| `postgresql` | `object (`[PostgreSql](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#PostgreSql)`)` PostgreSQL configurations. |

## PostgreSql

Settings for PostgreSQL data source.

|                                                                                                                                                                                                                             JSON representation                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "database": string, "schemaValidation": enum (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#SqlSchemaValidation), // Union field `configuration` can be only one of the following: "cloudSql": { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#CloudSqlInstance) } // End of list of possible types for union field `configuration`. } ``` |

|                                                                                                                                            Fields                                                                                                                                             ||
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `database`         | `string` Required. Name of the PostgreSQL database.                                                                                                                                                                                                                       |
| `schemaValidation` | `enum (`[SqlSchemaValidation](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#SqlSchemaValidation)`)` Optional. Configure how much Postgresql schema validation to perform. Default to `STRICT` if not specified. |
| Union field `configuration`. Settings and configurations of the underlying database. `configuration` can be only one of the following:                                                                                                                                                        ||
| `cloudSql`         | `object (`[CloudSqlInstance](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#CloudSqlInstance)`)` Cloud SQL configurations.                                                                                       |

## CloudSqlInstance

Settings for CloudSQL instance configuration.

|      JSON representation       |
|--------------------------------|
| ``` { "instance": string } ``` |

|                                                                  Fields                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| `instance` | `string` Required. Name of the CloudSQL instance, in the format: projects/{project}/locations/{location}/instances/{instance} |

## SqlSchemaValidation

Configure how much SQL Schema to perform for the given schema.

|                                                                                                                                                                  Enums                                                                                                                                                                   ||
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SQL_SCHEMA_VALIDATION_UNSPECIFIED` | Unspecified SQL schema validation. Default to STRICT.                                                                                                                                                                                                                                               |
| `NONE`                              | Skip no SQL schema validation. Use it with extreme caution. schemas.create or schemas.patch will succeed even if SQL database is unavailable or SQL schema is incompatible. Generated SQL may fail at execution time.                                                                               |
| `STRICT`                            | Connect to the SQL database and validate that the SQL DDL matches the schema exactly. Surface any discrepancies as `FAILED_PRECONDITION` with an `IncompatibleSqlSchemaError` error detail.                                                                                                         |
| `COMPATIBLE`                        | Connect to the SQL database and validate that the SQL DDL has all the SQL resources used in the given Firebase Data Connect Schema. Surface any missing resources as `FAILED_PRECONDITION` with an `IncompatibleSqlSchemaError` error detail. Succeed even if there are unknown tables and columns. |

|                                                                                                             ## Methods                                                                                                             ||
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| ### [create](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/create) | Creates a new Schema in a given project and location.                                                |
| ### [delete](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/delete) | Deletes a single Schema.                                                                             |
| ### [get](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/get)       | Gets details of a single Schema.                                                                     |
| ### [list](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/list)     | Lists Schemas in a given project and location.                                                       |
| ### [patch](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/patch)   | Updates the parameters of a single Schema, and creates a new SchemaRevision with the updated Schema. |