# Source: https://firebase.google.com/docs/reference/unity/class/firebase/app-options.md.txt

# Firebase.AppOptions Class Reference

# Firebase.AppOptions

Options that control the creation of a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App.

## Summary


**See also:**
[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)

### Inheritance

Inherits from: SystemIDisposable

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1afba46f20dddd29f422a03d2ae5cca59e()` Create `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options`. ||

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1acb63ab64777e2e1a9adc658a941cd4a3` | `string` Gets or sets the API key used to authenticate requests from your app. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1aeb6d92b58b2ad249b4b88453894dcc4f` | `string` Gets or sets the App Id. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1a502e57bbaa790a62e134345032bf9373` | `System.Uri` The database root URL, e.g. "<http://abc-xyz-123.firebaseio.com>". |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1a6ee92e470cdb8db54931eae2c716f90a` | `string` Gets or sets the messaging sender Id. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1acbfb31765c163b29c404228c5531f301` | `string` Gets or sets the Google Cloud project ID. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1ae4076f95925babcf7946ce8300c11485` | `string` Gets or sets the Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) bucket name, e.g. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1a9e8809f8ce31da543cb2bbbe8ad17d74()` | `void` |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1ade70dfe8cfd4e23d3e70fc4dd098268c(string json_config)` | `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options` Load options from a JSON string. |

## Properties

### ApiKey

```c#
string ApiKey
```
Gets or sets the API key used to authenticate requests from your app.

For example, "AIzaSyDdVgKwhZl0sTTTLZ7iTmt1r3N2cJLnaDk" used to identify your app to Google servers.

This only needs to be specified if your application does not include google-services.json or GoogleService-Info.plist in its resources.

### AppId

```c#
string AppId
```
Gets or sets the App Id.

This is the mobilesdk_app_id in the Android google-services.json config file or GOOGLE_APP_ID in the GoogleService-Info.plist.

This only needs to be specified if your application does not include google-services.json or GoogleService-Info.plist in its resources.

### DatabaseUrl

```c#
System.Uri DatabaseUrl
```
The database root URL, e.g. "<http://abc-xyz-123.firebaseio.com>".

### MessageSenderId

```c#
string MessageSenderId
```
Gets or sets the messaging sender Id.

This only needs to be specified if your application does not include google-services.json or GoogleService-Info.plist in its resources.

### ProjectId

```c#
string ProjectId
```
Gets or sets the Google Cloud project ID.

This is the project_id in the Android google-services.json config file or PROJECT_ID in the GoogleService-Info.plist.

### StorageBucket

```c#
string StorageBucket
```
Gets or sets the Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) bucket name, e.g.

"abc-xyz-123.storage.firebase.com".

## Public functions

### AppOptions

```c#
 AppOptions()
```
Create `https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options`.

To create a [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) object, the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) application identifier and API key should be set using AppId and ApiKey respectively.

**See also:** [FirebaseApp.Create()](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1adc52b81c47e472234af52e44c8e9d696).

### Dispose

```c#
void Dispose()
```

## Public static functions

### LoadFromJsonConfig

```c#
AppOptions LoadFromJsonConfig(
  string json_config
)
```
Load options from a JSON string.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `json_config` | JSON string to read options from. | |
| **Returns** | Returns an [AppOptions](https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options) instance if successful, null otherwise. |