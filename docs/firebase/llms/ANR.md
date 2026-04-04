# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ANR.md.txt

# ANR

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ANR#SCHEMA_REPRESENTATION)

Additional details for an ANR crash.

|                                                      JSON representation                                                       |
|--------------------------------------------------------------------------------------------------------------------------------|
| ``` { "stackTrace": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/StackTrace) } } ``` |

|                                                                                    Fields                                                                                    ||
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `stackTrace` | `object (`[StackTrace](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/StackTrace)`)` The stack trace of the ANR crash. Optional. |