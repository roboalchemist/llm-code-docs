# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata.md.txt

# FirebaseAdmin.Auth.UserMetadata Class Reference

# FirebaseAdmin.Auth.UserMetadata

Contains additional metadata associated with a user account.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata#class_firebase_admin_1_1_auth_1_1_user_metadata_1ac72ef6530b31155da8f8b42299df5c82(long creationTimestamp, long lastSignInTimestamp, DateTime? lastRefreshTimestamp)` Initializes a new instance of the [UserMetadata](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata#class_firebase_admin_1_1_auth_1_1_user_metadata) class with the specified creation and last sign-in timestamps. ||

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata#class_firebase_admin_1_1_auth_1_1_user_metadata_1a530791c3361ebe07d81f963877a119f2` | `DateTime` Gets a timestamp representing the date and time that the account was created. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata#class_firebase_admin_1_1_auth_1_1_user_metadata_1a91da5fa7a444109377251bb5e3a2b806` | `DateTime` Gets the time at which the user was last active (ID token refreshed), or `null` if the user was never active. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata#class_firebase_admin_1_1_auth_1_1_user_metadata_1afbb2d934af2fcd325bab4d31b8770611` | `DateTime` Gets a timestamp representing the last time that the user has signed in. |

## Properties

### CreationTimestamp

```
DateTime CreationTimestamp
```
Gets a timestamp representing the date and time that the account was created.

If not available this property is `null`.

### LastRefreshTimestamp

```
DateTime LastRefreshTimestamp
```
Gets the time at which the user was last active (ID token refreshed), or `null` if the user was never active.

### LastSignInTimestamp

```
DateTime LastSignInTimestamp
```
Gets a timestamp representing the last time that the user has signed in.

If the user has never signed in this property is `null`.

## Public functions

### UserMetadata

```
 UserMetadata(
  long creationTimestamp,
  long lastSignInTimestamp,
  DateTime? lastRefreshTimestamp
)
```
Initializes a new instance of the [UserMetadata](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata#class_firebase_admin_1_1_auth_1_1_user_metadata) class with the specified creation and last sign-in timestamps.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `creationTimestamp` | A timestamp representing the date and time that the user account was created. | | `lastSignInTimestamp` | A timestamp representing the date and time that the user account was last signed-on to. | | `lastRefreshTimestamp` | A timestamp representing the date and time that the user account was last refreshed. | |