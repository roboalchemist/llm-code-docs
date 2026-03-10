# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app.md.txt

# FirebaseAdmin.FirebaseApp Class Reference

# FirebaseAdmin.FirebaseApp

This is the entry point to the Firebase Admin SDK.

## Summary

It holds configuration and state common to all APIs exposed from the SDK.

Use one of the provided `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1a75ef3fc04488a2a21dc9105f051f6fa1` methods to obtain a new instance. See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for code samples and detailed documentation.

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1abc2b13c8d2c9f17595b13f3d850b8420` | `static https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app` Gets the default app instance. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1ae60685721bd810526b1e473c60846ea2` | `string` Gets the name of this app. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1a78e751cdef6f9bbe34d84edc8f000f26` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options` Gets a copy of the [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options) this app was created with. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1a75ef3fc04488a2a21dc9105f051f6fa1()` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app` Creates the default app instance with Google Application Default Credentials. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1ac9a1c05b7dfab6c6a788eb95ac5026fa(string name)` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app` Creates an app with the specified name, and Google Application Default Credentials. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1a85d901a2ace6d5344ffc1fe4965941ae(https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options options)` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app` Creates the default app instance with the specified options. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1a7dc581d8057f375228c3905aaf68f9d5(https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options options, string name)` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app` Creates an app with the specified name and options. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1af4a68e0717316598f040860da4341970(string name)` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app` Returns the app instance identified by the given name. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app_1a8d7f67403ce16835673a5713fd771485()` | `void` Deletes this app instance and cleans up any state associated with it. |

## Properties

### DefaultInstance

```
static FirebaseApp DefaultInstance
```
Gets the default app instance.

This property is `null` if the default app instance doesn't yet exist.

### Name

```
string Name
```
Gets the name of this app.

### Options

```
AppOptions Options
```
Gets a copy of the [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options) this app was created with.

## Public static functions

### Create

```
FirebaseApp Create()
```
Creates the default app instance with Google Application Default Credentials.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `System.ArgumentException` | If the default app instance already exists. | |
| **Returns** | The newly created [FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app) instance. |

### Create

```
FirebaseApp Create(
  string name
)
```
Creates an app with the specified name, and Google Application Default Credentials.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `System.ArgumentException` | If the default app instance already exists. | |
| Parameters | |---|---| | `name` | Name of the app. | |
| **Returns** | The newly created [FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app) instance. |

### Create

```
FirebaseApp Create(
  AppOptions options
)
```
Creates the default app instance with the specified options.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `System.ArgumentException` | If the default app instance already exists. | |
| Parameters | |---|---| | `options` | Options to create the app with. Must at least contain the `Credential`. | |
| **Returns** | The newly created [FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app) instance. |

### Create

```
FirebaseApp Create(
  AppOptions options,
  string name
)
```
Creates an app with the specified name and options.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `System.ArgumentException` | If the default app instance already exists. | |
| Parameters | |---|---| | `options` | Options to create the app with. Must at least contain the `Credential`. | | `name` | Name of the app. | |
| **Returns** | The newly created [FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app) instance. |

### GetInstance

```
FirebaseApp GetInstance(
  string name
)
```
Returns the app instance identified by the given name.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `System.ArgumentException` | If the name argument is null or empty. | |
| Parameters | |---|---| | `name` | Name of the app to retrieve. | |
| **Returns** | The [FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app) instance with the specified name or null if it doesn't exist. |

## Public functions

### Delete

```
void Delete()
```
Deletes this app instance and cleans up any state associated with it.

Once an app has been deleted, accessing any services related to it will result in an exception. If the app is already deleted, this method is a no-op.