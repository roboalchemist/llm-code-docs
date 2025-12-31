# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/provider-identifier.md.txt

# FirebaseAdmin.Auth.ProviderIdentifier Class Reference

# FirebaseAdmin.Auth.ProviderIdentifier

Used for looking up an account by provider.

## Summary

See AbstractFirebaseAuth.GetUsersAsync(IReadOnlyCollection{UserIdentifier}).

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-identifier)

| ### Constructors and Destructors ||
|---|---|
| [ProviderIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/provider-identifier#class_firebase_admin_1_1_auth_1_1_provider_identifier_1aa5f38bb5bda2849333eb9b6f7aa98cdb)`(string providerId, string providerUid)` Initializes a new instance of the [ProviderIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/provider-identifier#class_firebase_admin_1_1_auth_1_1_provider_identifier) class. ||

|                                                                                                       ### Public functions                                                                                                        ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| [ToString](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/provider-identifier#class_firebase_admin_1_1_auth_1_1_provider_identifier_1a689d70eeef0fdceaa545cc13f758de92)`()` | `override string` |

## Public functions

### ProviderIdentifier

```text
 ProviderIdentifier(
  string providerId,
  string providerUid
)
```  
Initializes a new instance of the [ProviderIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/provider-identifier#class_firebase_admin_1_1_auth_1_1_provider_identifier) class.

<br />

|                                                          Details                                                           ||
|------------|----------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|------------------| | `providerId`  | The providerId.  | | `providerUid` | The providerUid. | |

### ToString

```text
override string ToString()
```