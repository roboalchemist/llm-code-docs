# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportresult.md.txt

# UserImportResult interface

Interface representing the response from the [BaseAuth.importUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthimportusers) method for batch importing users to Firebase Auth.

**Signature:**  

    export interface UserImportResult 

## Properties

|                                                                  Property                                                                  |            Type             |                                                                Description                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [errors](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportresult.md#userimportresulterrors)             | FirebaseArrayIndexError\[\] | An array of errors corresponding to the provided users to import. The length of this array is equal to \[`failureCount`\](#failureCount). |
| [failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportresult.md#userimportresultfailurecount) | number                      | The number of user records that failed to import to Firebase Auth.                                                                        |
| [successCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportresult.md#userimportresultsuccesscount) | number                      | The number of user records that successfully imported to Firebase Auth.                                                                   |

## UserImportResult.errors

An array of errors corresponding to the provided users to import. The length of this array is equal to \[`failureCount`\](#failureCount).

**Signature:**  

    errors: FirebaseArrayIndexError[];

## UserImportResult.failureCount

The number of user records that failed to import to Firebase Auth.

**Signature:**  

    failureCount: number;

## UserImportResult.successCount

The number of user records that successfully imported to Firebase Auth.

**Signature:**  

    successCount: number;