# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result.md.txt

# FirebaseAdmin.Auth.UserImportResult Class Reference

# FirebaseAdmin.Auth.UserImportResult

Represents the result of the AbstractFirebaseAuth.ImportUsersAsync(IEnumerable{ImportUserRecordArgs}) API.

## Summary

|                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                         ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Errors](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result_1a21519945d662b2ae2c43caa6d9439c60) | `IReadOnlyList< `[ErrorInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/error-info#class_firebase_admin_1_1_auth_1_1_error_info)` >` Gets errors associated with a user import. |

|                                                                                                                                               ### Public attributes                                                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [FailureCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result_1ab7d372de61a29a892dc28cc82237eb9f)` => this.Errors?.Count ?? 0`        | `int` Gets the number of users that failed to be imported.      |
| [SuccessCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result_1af11c308dbc049175e3c31d205e942292)` => this.users - this.FailureCount` | `int` Gets the number of users that were imported successfully. |

## Properties

### Errors

```text
IReadOnlyList< ErrorInfo > Errors
```  
Gets errors associated with a user import.

Empty list if there were no errors.

## Public attributes

### FailureCount

```text
int FailureCount => this.Errors?.Count ?? 0
```  
Gets the number of users that failed to be imported.  

### SuccessCount

```text
int SuccessCount => this.users - this.FailureCount
```  
Gets the number of users that were imported successfully.