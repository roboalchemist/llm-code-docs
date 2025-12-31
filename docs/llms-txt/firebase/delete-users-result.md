# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/delete-users-result.md.txt

# FirebaseAdmin.Auth.DeleteUsersResult Class Reference

# FirebaseAdmin.Auth.DeleteUsersResult

Represents the result of the AbstractFirebaseAuth.DeleteUsersAsync(IReadOnlyList{string}) API.

## Summary

|                                                                                                                                                                                                                                                                                                                ### Properties                                                                                                                                                                                                                                                                                                                ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Errors](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/delete-users-result#class_firebase_admin_1_1_auth_1_1_delete_users_result_1a32c2572f6282cf834f78697c51a974eb)       | `IReadOnlyList< `[ErrorInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/error-info#class_firebase_admin_1_1_auth_1_1_error_info)` >` Gets a list of [ErrorInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/error-info#class_firebase_admin_1_1_auth_1_1_error_info) instances describing the errors that were encountered during the deletion. |
| [FailureCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/delete-users-result#class_firebase_admin_1_1_auth_1_1_delete_users_result_1a357a72bc284d76cfd0231eb45d9dae0c) | `int` Gets the number of users that `DeleteUsersAsync` failed to be deleted (possibly zero).                                                                                                                                                                                                                                                                                                                                 |
| [SuccessCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/delete-users-result#class_firebase_admin_1_1_auth_1_1_delete_users_result_1ad6181a3d3ff941b328a337ebfcd33242) | `int` Gets the number of users that were deleted successfully (possibly zero).                                                                                                                                                                                                                                                                                                                                               |

## Properties

### Errors

```text
IReadOnlyList< ErrorInfo > Errors
```  
Gets a list of [ErrorInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/error-info#class_firebase_admin_1_1_auth_1_1_error_info) instances describing the errors that were encountered during the deletion.

Length of this list is equal to the return value of [FailureCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/delete-users-result#class_firebase_admin_1_1_auth_1_1_delete_users_result_1a357a72bc284d76cfd0231eb45d9dae0c).

<br />

|                    Details                     ||
|-------------|-----------------------------------|
| **Returns** | A non-null list (possibly empty). |

### FailureCount

```text
int FailureCount
```  
Gets the number of users that `DeleteUsersAsync` failed to be deleted (possibly zero).  

### SuccessCount

```text
int SuccessCount
```  
Gets the number of users that were deleted successfully (possibly zero).

[Users](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth/users#namespace_firebase_admin_1_1_auth_1_1_users) that did not exist prior to calling AbstractFirebaseAuth.DeleteUsersAsync(IReadOnlyList{string}) are considered to be successfully deleted.