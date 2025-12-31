# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-records.md.txt

# FirebaseAdmin.Auth.ExportedUserRecords Class Reference

# FirebaseAdmin.Auth.ExportedUserRecords

Contains a collection of Firebase user accounts.

## Summary

|                                                                                                                                                                                                                              ### Properties                                                                                                                                                                                                                              ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NextPageToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-records#class_firebase_admin_1_1_auth_1_1_exported_user_records_1af91a754e206a6f2c53873fce15163f09) | `string` Gets the token representing the next page of users.                                                                                                                                                                                        |
| [Users](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-records#class_firebase_admin_1_1_auth_1_1_exported_user_records_1a97be73fb7964f91888d5c647b251344d)         | `IEnumerable< `[ExportedUserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-record#class_firebase_admin_1_1_auth_1_1_exported_user_record)` >` Gets the users included in the current page. |

## Properties

### NextPageToken

```text
string NextPageToken
```  
Gets the token representing the next page of users.

Null if there are no more pages.  

### Users

```text
IEnumerable< ExportedUserRecord > Users
```  
Gets the users included in the current page.