# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable.md.txt

# Method: projects.releases.getExecutable

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#body.GetReleaseExecutableResponse.SCHEMA_REPRESENTATION)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#body.aspect)
- [ReleaseExecutableVersion](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#ReleaseExecutableVersion)
- [Language](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#Language)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#try-it)

Get the `Release` executable to use when enforcing rules.

### HTTP request

`GET https://firebaserules.googleapis.com/v1/{name=projects/*/releases/**}:getExecutable`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                    Parameters                                                    ||
|--------|----------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. Resource name of the `Release`. Format: `projects/{project_id}/releases/{release_id}` |

### Query parameters

|                                                                                                                            Parameters                                                                                                                             ||
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `executableVersion` | `enum (`[ReleaseExecutableVersion](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#ReleaseExecutableVersion)`)` The requested runtime executable version. Defaults to FIREBASE_RULES_EXECUTABLE_V1. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:
The response for [FirebaseRulesService.GetReleaseExecutable](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#google.firebase.rules.v1.FirebaseRulesService.GetReleaseExecutable)

|                                                                                                                                                                            JSON representation                                                                                                                                                                            ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| ``` { "executable": string, "language": enum (https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#Language), "rulesetName": string, "updateTime": string, "executableVersion": enum (https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#ReleaseExecutableVersion), "syncTime": string } ``` |

|                                                                                                                                                                                                                                             Fields                                                                                                                                                                                                                                              ||
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `executable`        | `string (`[bytes](https://developers.google.com/discovery/v1/type-format)` format)` Executable view of the `Ruleset` referenced by the `Release`. A base64-encoded string.                                                                                                                                                                                                                                                                                                 |
| `language`          | `enum (`[Language](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#Language)`)` `Language` used to generate the executable bytes.                                                                                                                                                                                                                                                                                                 |
| `rulesetName`       | `string` `Ruleset` name associated with the `Release` executable.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `updateTime`        | `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Timestamp for the most recent `Release.update_time`. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.                                                                                            |
| `executableVersion` | `enum (`[ReleaseExecutableVersion](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable#ReleaseExecutableVersion)`)` The Rules runtime version of the executable.                                                                                                                                                                                                                                                                      |
| `syncTime`          | `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Optional, indicates the freshness of the result. The response is guaranteed to be the latest within an interval up to the syncTime (inclusive). A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`
- `https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ReleaseExecutableVersion

The executable versions supported for each language and syntax revision.

|                                                                Enums                                                                ||
|------------------------------------------|-------------------------------------------------------------------------------------------|
| `RELEASE_EXECUTABLE_VERSION_UNSPECIFIED` | Executable format unspecified. Defaults to FIREBASE_RULES_EXECUTABLE_V1                   |
| `FIREBASE_RULES_EXECUTABLE_V1`           | Firebase Rules syntax 'rules2' executable versions: Custom AST for use with Java clients. |
| `FIREBASE_RULES_EXECUTABLE_V2`           | CEL-based executable for use with C++ clients.                                            |

## Language

`Language` set supported within `Source`.

|                                   Enums                                   ||
|------------------------|---------------------------------------------------|
| `LANGUAGE_UNSPECIFIED` | Language unspecified. Defaults to FIREBASE_RULES. |
| `FIREBASE_RULES`       | Firebase Rules language.                          |
| `EVENT_FLOW_TRIGGERS`  | Event Flow triggers.                              |