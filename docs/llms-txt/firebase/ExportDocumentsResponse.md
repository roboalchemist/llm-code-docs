# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/ExportDocumentsResponse.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ExportDocumentsResponse.md.txt

# ExportDocumentsResponse

Returned in the [google.longrunning.Operation](https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation) response field.

|          JSON representation          |
|---------------------------------------|
| ``` { "outputUriPrefix": string } ``` |

|                                                                                              Fields                                                                                              ||
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `outputUriPrefix` | `string` Location of the output files. This can be used to begin an import into Cloud Firestore (this project or another project) after the operation completes successfully. |