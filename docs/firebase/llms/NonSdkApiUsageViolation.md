# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApiUsageViolation.md.txt

# NonSdkApiUsageViolation

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApiUsageViolation#SCHEMA_REPRESENTATION)

Additional details for a non-sdk API usage violation.

|                      JSON representation                       |
|----------------------------------------------------------------|
| ``` { "uniqueApis": integer, "apiSignatures": [ string ] } ``` |

|                                   Fields                                   ||
|-------------------|---------------------------------------------------------|
| `uniqueApis`      | `integer` Total number of unique hidden API's accessed. |
| `apiSignatures[]` | `string` Signatures of a subset of those hidden API's.  |