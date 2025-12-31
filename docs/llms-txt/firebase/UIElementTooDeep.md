# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/UIElementTooDeep.md.txt

# UIElementTooDeep

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/UIElementTooDeep#SCHEMA_REPRESENTATION)

A warning that the screen hierarchy is deeper than the recommended threshold.

|                            JSON representation                            |
|---------------------------------------------------------------------------|
| ``` { "screenId": string, "screenStateId": string, "depth": integer } ``` |

|                            Fields                            ||
|-----------------|---------------------------------------------|
| `screenId`      | `string` The screen id of the element       |
| `screenStateId` | `string` The screen state id of the element |
| `depth`         | `integer` The depth of the screen element   |