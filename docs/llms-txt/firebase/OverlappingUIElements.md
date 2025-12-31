# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/OverlappingUIElements.md.txt

# OverlappingUIElements

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/OverlappingUIElements#SCHEMA_REPRESENTATION)

A warning that Robo encountered a screen that has overlapping clickable elements; this may indicate a potential UI issue.

|                    JSON representation                     |
|------------------------------------------------------------|
| ``` { "screenId": string, "resourceName": [ string ] } ``` |

|                                    Fields                                    ||
|------------------|------------------------------------------------------------|
| `screenId`       | `string` The screen id of the elements                     |
| `resourceName[]` | `string` Resource names of the overlapping screen elements |