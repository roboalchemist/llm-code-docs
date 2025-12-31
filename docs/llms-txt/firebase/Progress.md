# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Progress.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Progress.md.txt

# Progress

Describes the progress of the operation. Unit of work is generic and must be interpreted based on where [Progress](https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Progress) is used.

|                     JSON representation                      |
|--------------------------------------------------------------|
| ``` { "estimatedWork": string, "completedWork": string } ``` |

|                                                               Fields                                                               ||
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| `estimatedWork` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` The amount of work estimated. |
| `completedWork` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` The amount of work completed. |