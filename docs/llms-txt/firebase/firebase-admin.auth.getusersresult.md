# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.getusersresult.md.txt

# GetUsersResult interface

Represents the result of the [BaseAuth.getUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgetusers) API.

**Signature:**  

    export interface GetUsersResult 

## Properties

|                                                            Property                                                            |                                                            Type                                                            |                                                                     Description                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [notFound](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.getusersresult.md#getusersresultnotfound) | [UserIdentifier](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#useridentifier)\[\]          | Set of identifiers that were requested, but not found.                                                                                               |
| [users](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.getusersresult.md#getusersresultusers)       | [UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class)\[\] | Set of user records, corresponding to the set of users that were requested. Only users that were found are listed here. The result set is unordered. |

## GetUsersResult.notFound

Set of identifiers that were requested, but not found.

**Signature:**  

    notFound: UserIdentifier[];

## GetUsersResult.users

Set of user records, corresponding to the set of users that were requested. Only users that were found are listed here. The result set is unordered.

**Signature:**  

    users: UserRecord[];