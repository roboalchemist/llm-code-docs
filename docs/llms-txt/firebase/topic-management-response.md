# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/topic-management-response.md.txt

# FirebaseAdmin.Messaging.TopicManagementResponse Class Reference

# FirebaseAdmin.Messaging.TopicManagementResponse

The response produced by FCM topic management operations.

## Summary

|                                                                                                                                                                                                                                                ### Properties                                                                                                                                                                                                                                                 ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Errors](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/topic-management-response#class_firebase_admin_1_1_messaging_1_1_topic_management_response_1ae9730fe440566caf40f03b6864a53e47)       | `IReadOnlyList< `[ErrorInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/error-info#class_firebase_admin_1_1_messaging_1_1_error_info)` >` Gets a list of errors encountered while executing the topic management operation. |
| [SuccessCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/topic-management-response#class_firebase_admin_1_1_messaging_1_1_topic_management_response_1aa4a4e030323de63e991f1fee52872023) | `int` Gets the number of registration tokens that were successfully subscribed or unsubscribed.                                                                                                                                                                         |

|                                                                                                                                                                               ### Public attributes                                                                                                                                                                               ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [FailureCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/topic-management-response#class_firebase_admin_1_1_messaging_1_1_topic_management_response_1a6ff8ccf69e02a867f1e6444a755891e8)` => this.Errors.Count` | `int` Gets the number of registration tokens that could not be subscribed or unsubscribed, and resulted in an error. |

## Properties

### Errors

```text
IReadOnlyList< ErrorInfo > Errors
```  
Gets a list of errors encountered while executing the topic management operation.

<br />

|            Details            ||
|-------------|------------------|
| **Returns** | A non-null list. |

### SuccessCount

```text
int SuccessCount
```  
Gets the number of registration tokens that were successfully subscribed or unsubscribed.

<br />

|                                              Details                                              ||
|-------------|--------------------------------------------------------------------------------------|
| **Returns** | The number of registration tokens that were successfully subscribed or unsubscribed. |

## Public attributes

### FailureCount

```text
int FailureCount => this.Errors.Count
```  
Gets the number of registration tokens that could not be subscribed or unsubscribed, and resulted in an error.

<br />

|               Details                ||
|-------------|-------------------------|
| **Returns** | The number of failures. |