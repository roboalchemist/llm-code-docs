# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/EncounteredNonAndroidUiWidgetScreen.md.txt

# EncounteredNonAndroidUiWidgetScreen

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/EncounteredNonAndroidUiWidgetScreen#SCHEMA_REPRESENTATION)

Additional details about encountered screens with elements that are not Android UI widgets.

|                       JSON representation                       |
|-----------------------------------------------------------------|
| ``` { "distinctScreens": integer, "screenIds": [ string ] } ``` |

|                                              Fields                                              ||
|-------------------|-------------------------------------------------------------------------------|
| `distinctScreens` | `integer` Number of encountered distinct screens with non Android UI widgets. |
| `screenIds[]`     | `string` Subset of screens which contain non Android UI widgets.              |