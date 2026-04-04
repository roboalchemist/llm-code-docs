# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options.md.txt

# FirebaseAdmin.AppOptions Class Reference

# FirebaseAdmin.AppOptions

Configurable options that can be specified when creating a [FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app).

## Summary

See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for code samples and detailed documentation.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options_1a1cd8c12a6a89e8ff00a3f61fe7f9475c()` Initializes a new instance of the [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options) class. ||

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options_1abec3725984337eb9889e2eae43a53c4e` | `GoogleCredential` Gets or sets the GoogleCredential used to authorize an app. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options_1a828e351aeabd2bb4ea99c39601273e4d` | `HttpClientFactory` Gets or sets the HttpClientFactory to use when making Firebase requests. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options_1a885e4a6403916377769897aef4265dcb` | `string` Gets or sets the Google Cloud Platform project ID that should be associated with an app. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options_1a9ce2d2b4a024bd706677dbceeebaf7d1` | `string` Gets or sets the unique ID of the service account that should be associated with an app. |

## Properties

### Credential

```
GoogleCredential Credential
```
Gets or sets the GoogleCredential used to authorize an app.

All service calls made by the app will be authorized using this.

### HttpClientFactory

```
HttpClientFactory HttpClientFactory
```
Gets or sets the HttpClientFactory to use when making Firebase requests.

### ProjectId

```
string ProjectId
```
Gets or sets the Google Cloud Platform project ID that should be associated with an app.

### ServiceAccountId

```
string ServiceAccountId
```
Gets or sets the unique ID of the service account that should be associated with an app.

This is used to [create custom auth tokens](https://firebase.google.com/docs/auth/admin/create-custom-tokens) when service account credentials are not available. The service account ID can be found in the `client_email` field of the service account JSON.

## Public functions

### AppOptions

```
 AppOptions()
```
Initializes a new instance of the [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options) class.