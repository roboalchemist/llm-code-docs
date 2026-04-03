# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.deleteusersresult.md.txt

# DeleteUsersResult interface

Represents the result of the [BaseAuth.deleteUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthdeleteusers). API.

**Signature:**  

    export interface DeleteUsersResult 

## Properties

|                                                                   Property                                                                   |            Type             |                                                                                                                                                            Description                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [errors](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.deleteusersresult.md#deleteusersresulterrors)             | FirebaseArrayIndexError\[\] | A list of `FirebaseArrayIndexError` instances describing the errors that were encountered during the deletion. Length of this list is equal to the return value of [DeleteUsersResult.failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.deleteusersresult.md#deleteusersresultfailurecount). |
| [failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.deleteusersresult.md#deleteusersresultfailurecount) | number                      | The number of user records that failed to be deleted (possibly zero).                                                                                                                                                                                                                                                              |
| [successCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.deleteusersresult.md#deleteusersresultsuccesscount) | number                      | The number of users that were deleted successfully (possibly zero). Users that did not exist prior to calling `deleteUsers()` are considered to be successfully deleted.                                                                                                                                                           |

## DeleteUsersResult.errors

A list of `FirebaseArrayIndexError` instances describing the errors that were encountered during the deletion. Length of this list is equal to the return value of [DeleteUsersResult.failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.deleteusersresult.md#deleteusersresultfailurecount).

**Signature:**  

    errors: FirebaseArrayIndexError[];

## DeleteUsersResult.failureCount

The number of user records that failed to be deleted (possibly zero).

**Signature:**  

    failureCount: number;

## DeleteUsersResult.successCount

The number of users that were deleted successfully (possibly zero). Users that did not exist prior to calling `deleteUsers()` are considered to be successfully deleted.

**Signature:**  

    successCount: number;