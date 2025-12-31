# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/list-users-options.md.txt

# FirebaseAdmin.Auth.ListUsersOptions Class Reference

# FirebaseAdmin.Auth.ListUsersOptions

Options for the [AbstractFirebaseAuth.ListUsersAsync(ListUsersOptions)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a13c65216fc17ea092225befa7fff4015) API.

## Summary

|                                                                                                                                   ### Properties                                                                                                                                   ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [PageSize](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/list-users-options#class_firebase_admin_1_1_auth_1_1_list_users_options_1a6b89bf4dc94cf4c23bfe81bb5ce0a1c3)  | `int` Gets or sets the number of results to fetch in a single API call. |
| [PageToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/list-users-options#class_firebase_admin_1_1_auth_1_1_list_users_options_1a95e0ecd80bd73daaaa670fd71a47907c) | `string` Gets or sets the page token.                                   |

## Properties

### PageSize

```text
int PageSize
```  
Gets or sets the number of results to fetch in a single API call.

This does not affect the total number of results returned. Must not exceed 1000.  

### PageToken

```text
string PageToken
```  
Gets or sets the page token.

If set, this token is used to indicate a continued list operation.