# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/ActingUser.md.txt

# ActingUser

Contains metadata about the user who performed an action, such as creating a release or finalizing a version.

|               JSON representation               |
|-------------------------------------------------|
| ``` { "email": string, "imageUrl": string } ``` |

|                                                                     Fields                                                                      ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `email`    | `string` The email address of the user when the user performed the action.                                                          |
| `imageUrl` | `string` A profile image URL for the user. May not be present if the user has changed their email address or deleted their account. |