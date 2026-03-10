# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId.md.txt

# FirebaseInstanceId

public class **FirebaseInstanceId** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

Firebase Instance ID has been replaced with `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations`
for app instance identifiers and `FirebaseMessaging.getToken()` for FCM
registration tokens.

Firebase Instance ID provides a unique identifier for each app instance and a mechanism to
authenticate and authorize actions (example: sending FCM messages).

Instance ID is stable except when:

- App deletes Instance ID
- App is restored on a new device
- User uninstalls/reinstall the app
- User clears app data

Once an Instance ID is generated, the library periodically sends information about the
application and the device where it's running to the Firebase backend. To stop this, see
`https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()`.

To prove ownership of Instance ID and to allow servers to access data or services
associated with the app, call `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getToken(java.lang.String,%20java.lang.String)`.

### Public Method Summary

|---|---|
| void | [deleteInstanceId](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId())() *This method is deprecated. Use `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#delete()` and `FirebaseMessaging.deleteToken()` instead.* |
| void | [deleteToken](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#deleteToken(java.lang.String,%20java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) senderId, [String](https://developer.android.com/reference/java/lang/String.html) scope) *This method is deprecated. Use `FirebaseMessaging.deleteToken()` instead.* |
| long | [getCreationTime](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getCreationTime())() Returns time when instance ID was created. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getId](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getId())() *This method is deprecated. Use `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#getId()` instead.* |
| static [FirebaseInstanceId](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getInstance())() Returns an instance of this class. |
| static [FirebaseInstanceId](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) app) Returns an instance for the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| Task\<[InstanceIdResult](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/InstanceIdResult)\> | [getInstanceId](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getInstanceId())() *This method is deprecated. For an instance identifier, use `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#getId()` instead. For an FCM registration token, use `FirebaseMessaging.getToken()` instead.* |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getToken](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getToken(java.lang.String,%20java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) senderId, [String](https://developer.android.com/reference/java/lang/String.html) scope) *This method is deprecated. Use `FirebaseMessaging.getToken()` instead.* |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getToken](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getToken())() *This method is deprecated. In favour of `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getInstanceId()`.* |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| [Object](https://developer.android.com/reference/java/lang/Object.html) | clone() |
| boolean | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void | finalize() |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| [String](https://developer.android.com/reference/java/lang/String.html) | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public void **deleteInstanceId** ()

**This method is deprecated.**   

Use `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#delete()` and
`FirebaseMessaging.deleteToken()` instead.
Delete the Instance ID and the data associated with it.

This stops the periodic sending of data to the Firebase backend started when the
Instance ID was generated, unless another library that requires InstanceId (like FCM,
RemoteConfig or Analytics) is used or it's configured to be executed automatically.

A new Instance ID will be generated at next app start if Firebase Cloud Messaging
auto-init is enabled.

This is a blocking function so do not call it on the main thread.

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---|---|

#### public void **deleteToken** ([String](https://developer.android.com/reference/java/lang/String.html) senderId, [String](https://developer.android.com/reference/java/lang/String.html) scope)

**This method is deprecated.**   

Use `FirebaseMessaging.deleteToken()` instead.
Revokes access to a scope (action) for a sender ID previously authorized by
`https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getToken()`.

This is a blocking function so do not call it on the main thread.

##### Parameters

| senderId | ID of the sender that must no longer have access. |
| scope | Action that the sender ID is no longer authorized to perform. Set the scope to `FCM` to revoke the authorization to send messages via FirebaseMessaging. |
|---|---|

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) | if the request fails. |
|---|---|

#### public long **getCreationTime** ()

Returns time when instance ID was created.

##### Returns

- Time when instance ID was created (milliseconds since Epoch).

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getId** ()

**This method is deprecated.**   

Use `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#getId()` instead.
Returns a stable identifier that uniquely identifies the app instance.

Once an Instance ID is generated, the library periodically sends information about
the application and the device where it's running to the Firebase backend. To stop
this, see `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()`.

##### Returns

- The identifier for the application instance.

#### public static [FirebaseInstanceId](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId)
**getInstance** ()

Returns an instance of this class.

##### Returns

- FirebaseInstanceId instance.

#### public static [FirebaseInstanceId](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId)
**getInstance** ([FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) app)

Returns an instance for the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

##### Parameters

| app | FirebaseApp instance. |
|---|---|

##### Returns

- FirebaseInstanceId instance.

#### public Task\<[InstanceIdResult](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/InstanceIdResult)\>
**getInstanceId** ()

**This method is deprecated.**   

For an instance identifier, use `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#getId()` instead. For an FCM registration token, use
`FirebaseMessaging.getToken()` instead.
Returns the ID and automatically generated token for this Firebase project.

This generates an Instance ID if it does not exist yet, which starts periodically
sending information to the Firebase backend (see `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getId()`).

##### Returns

- `https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task` which you can use to see the result via the `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/InstanceIdResult` which holds the ID and token.

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getToken** ([String](https://developer.android.com/reference/java/lang/String.html) senderId, [String](https://developer.android.com/reference/java/lang/String.html) scope)

**This method is deprecated.**   

Use `FirebaseMessaging.getToken()` instead.
Returns a token that authorizes a sender ID to perform an action on behalf of the
application identified by Instance ID.

This generates an Instance ID if it does not exist yet, which starts periodically
sending information to the Firebase backend (see `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getId()`).

This is similar to an OAuth2 token except, it applies to the application instance
instead of a user.

This is a blocking function so do not call it on the main thread.

##### Parameters

| senderId | ID of the sender that is authorized by the token. |
| scope | Action authorized for senderId. Set the scope to `FCM` to get authorization to send messages via FirebaseMessaging. |
|---|---|

##### Returns

- a token that can identify and authorize the instance of the application on the device.

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) | if the request fails. |
|---|---|

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getToken** ()

**This method is deprecated.**   

In favour of `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getInstanceId()`.
Returns the automatically generated token for the default Firebase project.

This generates an Instance ID if it does not exist yet, which starts periodically
sending information to the Firebase backend (see `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#getId()`).

##### Returns

- the master token or null if the token is not yet available