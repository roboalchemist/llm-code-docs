# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse.md.txt

# BatchResponse

public interface **BatchResponse**  
Response from an operation that sends FCM messages to multiple recipients.
See [sendAll(List)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>)) and [sendMulticast(MulticastMessage)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticast(com.google.firebase.messaging.MulticastMessage)).  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract int                                                                                                                                | [getFailureCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getFailureCount())() |
| abstract List\<[SendResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse)\> | [getResponses](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses())()       |
| abstract int                                                                                                                                | [getSuccessCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getSuccessCount())() |

## Public Methods

#### public abstract int
**getFailureCount**
()

<br />

#### public abstract List\<[SendResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse)\>
**getResponses**
()

<br />

#### public abstract int
**getSuccessCount**
()

<br />