# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups.md.txt

# REST Resource: projects.groups

- [Resource: Group](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#Group)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#Group.SCHEMA_REPRESENTATION)
- [Methods](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#METHODS_SUMMARY)

## Resource: Group

A group which can contain testers. A group can be invited to test apps in a Firebase project.

|                                                      JSON representation                                                       |
|--------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "displayName": string, "testerCount": integer, "releaseCount": integer, "inviteLinkCount": integer } ``` |

|                                                         Fields                                                          ||
|-----------------------|--------------------------------------------------------------------------------------------------|
| `name`                | `string` The name of the group resource. Format: `projects/{projectNumber}/groups/{group_alias}` |
| `display``Name`       | `string` Required. The display name of the group.                                                |
| `tester``Count`       | `integer` Output only. The number of testers who are members of this group.                      |
| `release``Count`      | `integer` Output only. The number of releases this group is permitted to access.                 |
| `invite``Link``Count` | `integer` Output only. The number of invite links for this group.                                |

|                                                                      ## Methods                                                                       ||
|------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| ### [batchJoin](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchJoin)   | Batch adds members to a group.      |
| ### [batchLeave](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave) | Batch removed members from a group. |
| ### [create](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create)         | Create a group.                     |
| ### [delete](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete)         | Delete a group.                     |
| ### [get](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/get)               | Get a group.                        |
| ### [list](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list)             | List groups.                        |
| ### [patch](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch)           | Update a group.                     |