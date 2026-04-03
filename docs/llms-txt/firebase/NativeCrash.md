# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NativeCrash.md.txt

# NativeCrash

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NativeCrash#SCHEMA_REPRESENTATION)

Additional details for a native crash.

|                                                      JSON representation                                                       |
|--------------------------------------------------------------------------------------------------------------------------------|
| ``` { "stackTrace": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/StackTrace) } } ``` |

|                                                                                     Fields                                                                                      ||
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `stackTrace` | `object (`[StackTrace](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/StackTrace)`)` The stack trace of the native crash. Optional. |