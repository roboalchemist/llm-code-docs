# Source: https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations.md.txt

# Firebase.Installations.FirebaseInstallations Class Reference

# Firebase.Installations.FirebaseInstallations

[Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) provides a unique identifier for each app instance and a mechanism to authenticate and authorize actions (for example, sending an FCM message).

## Summary

Provides a unique identifier for a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) installation. Provides an auth token for a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) installation. Provides a API to perform data deletion for a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) installation.

### Inheritance

Inherits from: SystemIDisposable

|                                                                                                                                                                                                                                                                                                                                             ### Properties                                                                                                                                                                                                                                                                                                                                             ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [App](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations_1a51a5c2a7c6c30b498c2cdd55285ebd06)             | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) App object associated with this [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations).                                                                                                                                                                           |
| [DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations_1a2e8b9b6238d5ee0302a816ab8d53b4ca) | `static `[FirebaseInstallations](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations) [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) associated with the default [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App. |

|                                                                                                                                                                                                                                                         ### Public functions                                                                                                                                                                                                                                                          ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DeleteAsync](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations_1a5be978641b0812d4f2736bbf62c25a5e)`()`                    | `System.Threading.Tasks.Task` Delete the ID associated with the app, revoke all tokens, and allocate a new ID.                                                                                                                                                                             |
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations_1af10b2448b3b86d7797afebcf4651bcf2)`()`                        | `void`                                                                                                                                                                                                                                                                                     |
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations_1a8210239bebfc599c164ec593f3f80392)`(bool disposing)`          | `virtual void`                                                                                                                                                                                                                                                                             |
| [GetIdAsync](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations_1aea42b56928b40871d59c40a8f2bbe8b0)`()`                     | `System.Threading.Tasks.Task< string >` Returns a stable identifier that uniquely identifies the app instance.                                                                                                                                                                             |
| [GetTokenAsync](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations_1a0638822be6ddac13c651a2a7c38ad45c)`(bool forceRefresh)` | `System.Threading.Tasks.Task< string >` Returns a token that authorizes an Entity to perform an action on behalf of the application identified by [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations). |

|                                                                                                                                                                                                                                                                                                                                                                                                                                 ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations_1a899fb3fd5c08928afc0f618f304234b3)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app)` | [FirebaseInstallations](https://firebase.google.com/docs/reference/unity/class/firebase/installations/firebase-installations#class_firebase_1_1_installations_1_1_firebase_installations) Returns the [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) object for an `App` creating the [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) if required. |

## Properties

### App

```c#
FirebaseApp App
```  
App object associated with this [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations).  

### DefaultInstance

```c#
static FirebaseInstallations DefaultInstance
```  
[Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) associated with the default [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App.

<br />

|                                                                                                                                              Details                                                                                                                                               ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | An [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) object associated with the default [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App. |

## Public functions

### DeleteAsync

```c#
System.Threading.Tasks.Task DeleteAsync()
```  
Delete the ID associated with the app, revoke all tokens, and allocate a new ID.  

### Dispose

```c#
void Dispose()
```  

### Dispose

```c#
virtual void Dispose(
  bool disposing
)
```  

### GetIdAsync

```c#
System.Threading.Tasks.Task< string > GetIdAsync()
```  
Returns a stable identifier that uniquely identifies the app instance.

<br />

|                       Details                        ||
|-------------|-----------------------------------------|
| **Returns** | Unique identifier for the app instance. |

### GetTokenAsync

```c#
System.Threading.Tasks.Task< string > GetTokenAsync(
  bool forceRefresh
)
```  
Returns a token that authorizes an Entity to perform an action on behalf of the application identified by [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations).

This is similar to an OAuth2 token except it applies to the application instance instead of a user.

For example, to get a token that can be used to send messages to an application via [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Cloud [Messaging](https://firebase.google.com/docs/reference/unity/namespace/firebase/messaging#namespace_firebase_1_1_messaging), set entity to the sender ID, and set scope to "FCM".

<br />

|                                               Details                                               ||
|-------------|----------------------------------------------------------------------------------------|
| **Returns** | A token that can identify and authorize the instance of the application on the device. |

## Public static functions

### GetInstance

```c#
FirebaseInstallations GetInstance(
  FirebaseApp app
)
```  
Returns the [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) object for an `App` creating the [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) if required.

<br />

|                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                  ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `app` | The `App` to create an [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) object from. On **iOS and tvOS** this must be the default [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)`App`. | |
| **Returns** | [Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) object if successful, null otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |