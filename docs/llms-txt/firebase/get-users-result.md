# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/get-users-result.md.txt

# FirebaseAdmin.Auth.GetUsersResult Class Reference

# FirebaseAdmin.Auth.GetUsersResult

Represents the result of the AbstractFirebaseAuth.GetUsersAsync(IReadOnlyCollection{UserIdentifier}) API.

## Summary

|                                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                                         ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NotFound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/get-users-result#class_firebase_admin_1_1_auth_1_1_get_users_result_1a23a901765796d0017f89d1ba2b29f2e9) | `IEnumerable< `[UserIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-identifier#class_firebase_admin_1_1_auth_1_1_user_identifier)` >` Gets the set of identifiers that were requested, but not found. |
| [Users](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/get-users-result#class_firebase_admin_1_1_auth_1_1_get_users_result_1af87d23f2570314ac24402c8976fa93b9)    | `IEnumerable< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Gets user records corresponding to the set of users that were requested.    |

## Properties

### NotFound

```text
IEnumerable< UserIdentifier > NotFound
```  
Gets the set of identifiers that were requested, but not found.  

### Users

```text
IEnumerable< UserRecord > Users
```  
Gets user records corresponding to the set of users that were requested.

Only users that were found are listed here. The result set is unordered.