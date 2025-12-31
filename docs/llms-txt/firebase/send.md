# Source: https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send.md.txt

# Method: projects.messages.send

Send a message to specified target (a registration token, topic or condition).

### HTTP request

`POST https://fcm.googleapis.com/v1/{parent=projects/*}/messages:send`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                  Parameters                                                                                                                                   ||
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parent` | `string` Required. It contains the Firebase project id (i.e. the unique identifier for your Firebase project), in the format of `projects/{project_id}`. The numeric project number with no padding is also supported in the format of `projects/{project_number}`. |

### Request body

The request body contains data with the following structure:

|                                                              JSON representation                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "validate_only": boolean, "message": { object (https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Message) } } ``` |

|                                                                        Fields                                                                        ||
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `validate_only` | `boolean` Flag for testing the request without actually delivering the message.                                                     |
| `message`       | `object (`[Message](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Message)`)` Required. Message to send. |

### Response body

If successful, the response body contains an instance of [Message](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Message).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.messaging`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).