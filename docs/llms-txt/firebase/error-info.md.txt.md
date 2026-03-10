# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/error-info.md.txt

# FirebaseAdmin.Auth.ErrorInfo Class Reference

# FirebaseAdmin.Auth.ErrorInfo

Represents an error encountered while performing a batch operation such as AbstractFirebaseAuth.ImportUsersAsync(IEnumerable{ImportUserRecordArgs}) or AbstractFirebaseAuth.DeleteUsersAsync(IReadOnlyList{string}).

## Summary

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/error-info#class_firebase_admin_1_1_auth_1_1_error_info_1ade2488f252f590a9c8779aca6db8d03f` | `int` Gets the index of the entry that caused the error. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/error-info#class_firebase_admin_1_1_auth_1_1_error_info_1ad02f25948dee14e3ec82c4d154b74e36` | `string` Gets a string describing the error. |

## Properties

### Index

```
int Index
```
Gets the index of the entry that caused the error.

### Reason

```
string Reason
```
Gets a string describing the error.