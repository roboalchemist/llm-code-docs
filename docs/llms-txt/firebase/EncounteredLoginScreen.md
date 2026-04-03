# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/EncounteredLoginScreen.md.txt

# EncounteredLoginScreen

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/EncounteredLoginScreen#SCHEMA_REPRESENTATION)

Additional details about encountered login screens.

|                       JSON representation                       |
|-----------------------------------------------------------------|
| ``` { "distinctScreens": integer, "screenIds": [ string ] } ``` |

|                                   Fields                                   ||
|-------------------|---------------------------------------------------------|
| `distinctScreens` | `integer` Number of encountered distinct login screens. |
| `screenIds[]`     | `string` Subset of login screens.                       |