# Source: https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions.md.txt

# Firebase.Functions.FirebaseFunctions Class Reference

# Firebase.Functions.FirebaseFunctions

[FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) is a service that supports calling Google Cloud [Functions](https://firebase.google.com/docs/reference/unity/namespace/firebase/functions#namespace_firebase_1_1_functions).

## Summary

[FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) is a service that supports calling Google Cloud [Functions](https://firebase.google.com/docs/reference/unity/namespace/firebase/functions#namespace_firebase_1_1_functions). Pass a custom instance of [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) to [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1a76cad8cd258dedddfc5c95af3ecca009) which will use [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) and InstanceID from the app.

Otherwise, if you call [DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1afc75c6fd7ec36d1f7fb4e0c165e8e604) without a [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app), the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) instance will initialize with the default [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) obtainable from [FirebaseApp.DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1abf8fab1b5c3d7a745b7d4fd933e5a0fd).

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1a7d8bc6ef2964da695185e5c4918b941b` | `https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app` The [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) associated with this [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) instance. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1afc75c6fd7ec36d1f7fb4e0c165e8e604` | `static https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions` Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) , initialized with the default [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1a76cad8cd258dedddfc5c95af3ecca009(https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app app)` | `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions` Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) , initialized with a custom [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) |
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1ae27039f40acd584fe6c7366605aa5978(string region)` | `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions` Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) , initialized with the default [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app). |
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1a6aaae074590ae3e5ce52ea21039f064a(https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app app, string region)` | `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions` Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) , initialized with a custom [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) and region. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1aca04dea2afeb17926abfd1403ea46fc2(string name)` | `https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference` Creates a [HttpsCallableReference](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference) given a name. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1a61696624e926f0958d56342011e7eca0(string url)` | `https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference` Creates a [HttpsCallableReference](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference) given a URL. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1af3942a44388ac400515a9f3d0dd513bd(Uri url)` | `https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference` Creates a [HttpsCallableReference](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference) given a URL. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions_1a122a8bd55d97e9eb7a1433daeb4de349(string origin)` | `void` Sets an origin of a Cloud [Functions](https://firebase.google.com/docs/reference/unity/namespace/firebase/functions#namespace_firebase_1_1_functions) Emulator instance to use. |

## Properties

### App

```c#
FirebaseApp App
```
The [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) associated with this [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) instance.

### DefaultInstance

```c#
static FirebaseFunctions DefaultInstance
```
Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) , initialized with the default [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)

a [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) instance.

## Public static functions

### GetInstance

```c#
FirebaseFunctions GetInstance(
  FirebaseApp app
)
```
Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) , initialized with a custom [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | The custom [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) used for initialization. | |
| **Returns** | a [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) instance. |

### GetInstance

```c#
FirebaseFunctions GetInstance(
  string region
)
```
Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) , initialized with the default [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `region` | The region to call Cloud [Functions](https://firebase.google.com/docs/reference/unity/namespace/firebase/functions#namespace_firebase_1_1_functions) in. | |
| **Returns** | a [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) instance. |

### GetInstance

```c#
FirebaseFunctions GetInstance(
  FirebaseApp app,
  string region
)
```
Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) , initialized with a custom [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) and region.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | The custom [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) used for initialization. | |
| **Returns** | a [FirebaseFunctions](https://firebase.google.com/docs/reference/unity/class/firebase/functions/firebase-functions#class_firebase_1_1_functions_1_1_firebase_functions) instance. |

## Public functions

### GetHttpsCallable

```c#
HttpsCallableReference GetHttpsCallable(
  string name
)
```
Creates a [HttpsCallableReference](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference) given a name.

### GetHttpsCallableFromURL

```c#
HttpsCallableReference GetHttpsCallableFromURL(
  string url
)
```
Creates a [HttpsCallableReference](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference) given a URL.

### GetHttpsCallableFromURL

```c#
HttpsCallableReference GetHttpsCallableFromURL(
  Uri url
)
```
Creates a [HttpsCallableReference](https://firebase.google.com/docs/reference/unity/class/firebase/functions/https-callable-reference#class_firebase_1_1_functions_1_1_https_callable_reference) given a URL.

### UseFunctionsEmulator

```c#
void UseFunctionsEmulator(
  string origin
)
```
Sets an origin of a Cloud [Functions](https://firebase.google.com/docs/reference/unity/namespace/firebase/functions#namespace_firebase_1_1_functions) Emulator instance to use.