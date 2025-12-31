# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/send-response.md.txt

# FirebaseAdmin.Messaging.SendResponse Class Reference

# FirebaseAdmin.Messaging.SendResponse

The result of an individual send operation that was executed as part of a batch.

## Summary

See [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) for more details.

|                                                                                                                                                                                                                                  ### Properties                                                                                                                                                                                                                                  ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Exception](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/send-response#class_firebase_admin_1_1_messaging_1_1_send_response_1a210c31efe20b5cb38b83c2f1484b540d) | [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging-exception#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_exception) Gets an exception if the send operation failed. |
| [MessageId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/send-response#class_firebase_admin_1_1_messaging_1_1_send_response_1a27ad0698981d9603318a178c8a98e0fa) | `string` Gets a message ID string if the send operation was successful.                                                                                                                                                                                               |

|                                                                                                                                                         ### Public attributes                                                                                                                                                          ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [IsSuccess](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/send-response#class_firebase_admin_1_1_messaging_1_1_send_response_1a7f52d657e09f9b857b5189d5e60f1f77)` => !string.IsNullOrEmpty(this.MessageId)` | `bool` Gets a value indicating whether the send operation was successful or not. |

## Properties

### Exception

```text
FirebaseMessagingException Exception
```  
Gets an exception if the send operation failed.

Otherwise returns null.  

### MessageId

```text
string MessageId
```  
Gets a message ID string if the send operation was successful.

Otherwise returns null.

## Public attributes

### IsSuccess

```text
bool IsSuccess => !string.IsNullOrEmpty(this.MessageId)
```  
Gets a value indicating whether the send operation was successful or not.

When this property is `true`, [MessageId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/send-response#class_firebase_admin_1_1_messaging_1_1_send_response_1a27ad0698981d9603318a178c8a98e0fa) is guaranteed to return a non-null value. When this property is `false`, [Exception](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/send-response#class_firebase_admin_1_1_messaging_1_1_send_response_1a210c31efe20b5cb38b83c2f1484b540d) is guaranteed to return a non-null value.