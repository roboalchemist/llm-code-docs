# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response.md.txt

# FirebaseAdmin.Messaging.BatchResponse Class Reference

# FirebaseAdmin.Messaging.BatchResponse

Response from an operation that sends FCM messages to multiple recipients.

## Summary

See [FirebaseMessaging.SendMulticastAsync(MulticastMessage)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1ac19b28383fa9217cf44189aaac852613).

|                                                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                                                          ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Responses](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response_1a4818148e343cbd8a3c8b6bed23cba558)    | `IReadOnlyList< `[SendResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/send-response#class_firebase_admin_1_1_messaging_1_1_send_response)` >` Gets information about all responses for the batch.                              |
| [SuccessCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response_1a6f47872a787c5dffcb47da063171d501) | `int` Gets a count of how many of the responses in [Responses](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response_1a4818148e343cbd8a3c8b6bed23cba558) were successful. |

|                                                                                                                                                                                                                                                              ### Public attributes                                                                                                                                                                                                                                                              ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FailureCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response_1a194a70ccc147c494bb64013935d75761)` => this.Responses.Count - this.SuccessCount` | `int` Gets a count of how many of the responses in [Responses](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response_1a4818148e343cbd8a3c8b6bed23cba558) were unsuccessful. |

## Properties

### Responses

```text
IReadOnlyList< SendResponse > Responses
```  
Gets information about all responses for the batch.  

### SuccessCount

```text
int SuccessCount
```  
Gets a count of how many of the responses in [Responses](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response_1a4818148e343cbd8a3c8b6bed23cba558) were successful.

## Public attributes

### FailureCount

```text
int FailureCount => this.Responses.Count - this.SuccessCount
```  
Gets a count of how many of the responses in [Responses](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response_1a4818148e343cbd8a3c8b6bed23cba558) were unsuccessful.