# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/FatalException.md.txt

# FatalException

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/FatalException#SCHEMA_REPRESENTATION)

Additional details for a fatal exception.

|                                                      JSON representation                                                       |
|--------------------------------------------------------------------------------------------------------------------------------|
| ``` { "stackTrace": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/StackTrace) } } ``` |

|                                                                                       Fields                                                                                       ||
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `stackTrace` | `object (`[StackTrace](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/StackTrace)`)` The stack trace of the fatal exception. Optional. |