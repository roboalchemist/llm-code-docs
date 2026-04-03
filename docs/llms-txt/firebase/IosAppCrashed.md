# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/IosAppCrashed.md.txt

# IosAppCrashed

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/IosAppCrashed#SCHEMA_REPRESENTATION)

Additional details for an iOS app crash.

|                                                      JSON representation                                                       |
|--------------------------------------------------------------------------------------------------------------------------------|
| ``` { "stackTrace": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/StackTrace) } } ``` |

|                                                                                      Fields                                                                                      ||
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `stackTrace` | `object (`[StackTrace](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/StackTrace)`)` The stack trace, if one is available. Optional. |