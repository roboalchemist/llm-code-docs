# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listusersresult.md.txt

# ListUsersResult interface

Interface representing the object returned from a [BaseAuth.listUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistusers) operation. Contains the list of users for the current batch and the next page token if available.

**Signature:**  

    export interface ListUsersResult 

## Properties

|                                                              Property                                                              |                                                            Type                                                            |                                                                                 Description                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [pageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listusersresult.md#listusersresultpagetoken) | string                                                                                                                     | The next page token if available. This is needed for the next batch download.                                                                                                |
| [users](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listusersresult.md#listusersresultusers)         | [UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class)\[\] | The list of [UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class) objects for the current downloaded batch. |

## ListUsersResult.pageToken

The next page token if available. This is needed for the next batch download.

**Signature:**  

    pageToken?: string;

## ListUsersResult.users

The list of [UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class) objects for the current downloaded batch.

**Signature:**  

    users: UserRecord[];