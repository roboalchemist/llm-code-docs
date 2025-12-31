# Source: https://firebase.google.com/docs/reference/fcm/rest/v1/ApnsError.md.txt

# ApnsError

Error details directly from the [Apple Push Notification service (APNs)](https://goo.gl/MXRTPa).

|                 JSON representation                  |
|------------------------------------------------------|
| ``` { "status_code": integer, "reason": string } ``` |

|                                                                       Fields                                                                        ||
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `status_code` | `integer` Status code in the response from APNs. See [APNs status codes](https://goo.gl/BtPJLj) for explanations of possible values. |
| `reason`      | `string` Failure reason in the response from APNs. See [values](https://goo.gl/oFSRPg) for explanations of possible values.          |