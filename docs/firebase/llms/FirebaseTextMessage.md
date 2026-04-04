# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage.md.txt

# FirebaseTextMessage

public final class **FirebaseTextMessage** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Represents a text message from a certain user in a conversation, providing context for
SmartReply to generate reply suggestions.  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage) | [createForLocalUser](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage#createForLocalUser(java.lang.String, long))([String](https://developer.android.com/reference/java/lang/String.html) messageText, long timestampMillis) Creates an instance of [FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage) for a local user.                                                                                                            |
| static [FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage) | [createForRemoteUser](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage#createForRemoteUser(java.lang.String, long, java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) messageText, long timestampMillis, [String](https://developer.android.com/reference/java/lang/String.html) remoteUserId) Creates an instance of [FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage) for a remote user. |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Public Methods

#### public static [FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage) **createForLocalUser** ([String](https://developer.android.com/reference/java/lang/String.html) messageText, long timestampMillis)

Creates an instance of [FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage) for a local user. The local user is the current user of
the app's instance and is the user for which SmartReply is generating a reply.  

##### Parameters

|   messageText   |               the message content. We don't limit the length here, but the API works best for casual conversations with reasonable long messages.                |
| timestampMillis | timestamp of the message in milliseconds since midnight, January 1, 1970 UTC. You can use, for example, `java.lang.System.currentTimeMillis()` to get the value. |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public static [FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage) **createForRemoteUser** ([String](https://developer.android.com/reference/java/lang/String.html) messageText, long timestampMillis, [String](https://developer.android.com/reference/java/lang/String.html) remoteUserId)

Creates an instance of [FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage) for a remote user. Your local user may have a
conversation with one or more remote users and providing context for messages your
local user has received will help the API generate smart replies.  

##### Parameters

|   messageText   |                                                                                                                 the message content. The API does not limit length, but it does function optimally with reasonably long message in casual conversations.                                                                                                                  |
| timestampMillis |                                                                                                     timestamp of the message in milliseconds since midnight, January 1, 1970 UTC. You can use, for example, `java.lang.System.currentTimeMillis()` to get the value.                                                                                                      |
|  remoteUserId   | A unique user ID representing a remote user if the local user is having a conversation with more than one remote user. [FirebaseSmartReply](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply) is a stateless API, so there is no need to guarantee consistent user IDs across different API calls. |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|