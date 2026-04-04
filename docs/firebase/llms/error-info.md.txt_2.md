# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/error-info.md.txt

# FirebaseAdmin.Messaging.ErrorInfo Class Reference

# FirebaseAdmin.Messaging.ErrorInfo

A topic management error.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/error-info#class_firebase_admin_1_1_messaging_1_1_error_info_1a3915df534288b241aae592763bcb5e1f(int index, string reason)` Initializes a new instance of the [ErrorInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/error-info#class_firebase_admin_1_1_messaging_1_1_error_info) class. ||

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/error-info#class_firebase_admin_1_1_messaging_1_1_error_info_1a217e58ae61499b61f0869fbb11d5ac01` | `int` Gets the registration token to which this error is related to. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/error-info#class_firebase_admin_1_1_messaging_1_1_error_info_1a788f0c339c4634b812f63c437661850c` | `string` Gets the nature of the error. |

## Properties

### Index

```
int Index
```
Gets the registration token to which this error is related to.

<br />

| Details ||
|---|---|
| **Returns** | An index into the original registration token list. |

### Reason

```
string Reason
```
Gets the nature of the error.

<br />

| Details ||
|---|---|
| **Returns** | A non-null, non-empty error message. |

## Public functions

### ErrorInfo

```
 ErrorInfo(
  int index,
  string reason
)
```
Initializes a new instance of the [ErrorInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/error-info#class_firebase_admin_1_1_messaging_1_1_error_info) class.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `index` | Index of the error in the error codes. | | `reason` | Reason for the error. | |