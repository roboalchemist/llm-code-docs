# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportoptions.md.txt

# UserImportOptions interface

Interface representing the user import options needed for [BaseAuth.importUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthimportusers) method. This is used to provide the password hashing algorithm information.

**Signature:**  

    export interface UserImportOptions 

## Properties

|                                                           Property                                                           |                                                                                                                                           Type                                                                                                                                           |            Description            |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| [hash](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportoptions.md#userimportoptionshash) | { algorithm: [HashAlgorithmType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#hashalgorithmtype); key?: Buffer; saltSeparator?: Buffer; rounds?: number; memoryCost?: number; parallelization?: number; blockSize?: number; derivedKeyLength?: number; } | The password hashing information. |

## UserImportOptions.hash

The password hashing information.

**Signature:**  

    hash: {
            algorithm: HashAlgorithmType;
            key?: Buffer;
            saltSeparator?: Buffer;
            rounds?: number;
            memoryCost?: number;
            parallelization?: number;
            blockSize?: number;
            derivedKeyLength?: number;
        };