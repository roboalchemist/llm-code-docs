# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.md.txt

# REST Resource: projects.histories

- [Resource: History](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories#History)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories#History.SCHEMA_REPRESENTATION)
- [TestPlatform](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories#TestPlatform)
- [Methods](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories#METHODS_SUMMARY)

## Resource: History

A History represents a sorted list of Executions ordered by the start_timestamp_millis field (descending). It can be used to group all the Executions of a continuous build.

Note that the ordering only operates on one-dimension. If a repository has multiple branches, it means that multiple histories will need to be used in order to order Executions per branch.

|                                                                                             JSON representation                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "historyId": string, "name": string, "displayName": string, "testPlatform": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories#TestPlatform) } ``` |

|                                                                                                                                   Fields                                                                                                                                    ||
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `historyId`    | `string` A unique identifier within a project for this History. Returns INVALID_ARGUMENT if this field is set or overwritten by the caller. - In response always set - In create request: never set                                                         |
| `name`         | `string` A name to uniquely identify a history within a project. Maximum of 200 characters. - In response always set - In create request: always set                                                                                                        |
| `displayName`  | `string` A short human-readable (plain text) name to display in the UI. Maximum of 100 characters. - In response: present if set during create. - In create request: optional                                                                               |
| `testPlatform` | `enum (`[TestPlatform](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories#TestPlatform)`)` The platform of the test history. - In response: always set. Returns the platform of the last execution if unknown. |

## TestPlatform

The platform of the test.

|        Enums         ||
|-------------------|---|
| `unknownPlatform` |   |
| `android`         |   |
| `ios`             |   |

|                                                                         ## Methods                                                                         ||
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| ### [create](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/create) | Creates a History.                   |
| ### [get](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get)       | Gets a History.                      |
| ### [list](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/list)     | Lists Histories for a given Project. |