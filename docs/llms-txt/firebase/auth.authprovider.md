# Source: https://firebase.google.com/docs/reference/js/auth.authprovider.md.txt

# AuthProvider interface

Interface that represents an auth provider, used to facilitate creating [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class).

**Signature:**  

    export interface AuthProvider 

## Properties

|                                                Property                                                 |  Type  |                    Description                     |
|---------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------|
| [providerId](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authproviderproviderid) | string | Provider for which credentials can be constructed. |

## AuthProvider.providerId

Provider for which credentials can be constructed.

**Signature:**  

    readonly providerId: string;