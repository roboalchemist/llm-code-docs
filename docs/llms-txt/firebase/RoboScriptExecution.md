# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/RoboScriptExecution.md.txt

# RoboScriptExecution

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/RoboScriptExecution#SCHEMA_REPRESENTATION)

Execution stats for a user-provided Robo script.

|                        JSON representation                        |
|-------------------------------------------------------------------|
| ``` { "totalActions": integer, "successfulActions": integer } ``` |

|                                         Fields                                          ||
|---------------------|--------------------------------------------------------------------|
| `totalActions`      | `integer` The total number of actions in the Robo script.          |
| `successfulActions` | `integer` The number of Robo script actions executed successfully. |