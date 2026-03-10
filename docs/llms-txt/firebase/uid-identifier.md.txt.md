# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/uid-identifier.md.txt

# FirebaseAdmin.Auth.UidIdentifier Class Reference

# FirebaseAdmin.Auth.UidIdentifier

Used for looking up an account by uid.

## Summary

See AbstractFirebaseAuth.GetUsersAsync(IReadOnlyCollection{UserIdentifier}).

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-identifier)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/uid-identifier#class_firebase_admin_1_1_auth_1_1_uid_identifier_1a79f3b20c4c9d6c9201b0629c284bb6f0(string uid)` Initializes a new instance of the [UidIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/uid-identifier#class_firebase_admin_1_1_auth_1_1_uid_identifier) class. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/uid-identifier#class_firebase_admin_1_1_auth_1_1_uid_identifier_1ab14d069ced80d5a5aa10ad34792dae26()` | `override string` |

## Public functions

### ToString

```
override string ToString()
```

### UidIdentifier

```
 UidIdentifier(
  string uid
)
```
Initializes a new instance of the [UidIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/uid-identifier#class_firebase_admin_1_1_auth_1_1_uid_identifier) class.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `uid` | The uid. | |