# Source: https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth.md.txt

# FirebaseAdmin.Auth Namespace

# FirebaseAdmin.Auth

## Summary

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2{ https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a03d4776243d313c7540f22b6b8be7137, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a09a6a3c50e38fba5a58fe4e9fe6b99e7, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2ac2ee95a0c756d9349a66d7722b38df25, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a18d8260ce6fcb3674e527612470e000e, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a1e9af3cd140f39e1cc7c5731cec720bf, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2aba001751dfc8a4c2cd1887581ade6eac, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a8d28361cc3863be8ef512d04b63e66b0, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a5e349b2189e271e32f633c077d4ff028, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a3c850b10b03e95a176dc1d135ec6b111, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a596868b8ac0985b533eec02417cf78d1, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2ab7646b3d96c9e8d2d97566c34be447ca, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2acf79f41b0de01f838ad11f17010951dc, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a69e598f6929720a9e61f3756077f7829, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a3570be559701c8486e9371c7979295d5, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a3a4758ff767a24a3e0c90df1cc78abe5, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a4cff48fa41008914a897bf7ae9c7d611, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2a80fc5ffd12b4245c899cb91672d5680e, https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth_1acbdb7a54fd4b744f296881a3e77b29b2ae15961d49173d58de531d38dd66814dc }` | enumError codes that can be raised by the Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) APIs. |

| ### Classes ||
|---|---|
| [FirebaseAdmin.Auth.AbstractFirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth) | Exposes Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) operations that are available in both tenant-aware and tenant-unaware contexts. |
| [FirebaseAdmin.Auth.ActionCodeSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings) | Defines the required continue/state URL with optional Android and iOS settings. |
| [FirebaseAdmin.Auth.DeleteUsersResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/delete-users-result) | Represents the result of the AbstractFirebaseAuth.DeleteUsersAsync(IReadOnlyList{string}) API. |
| [FirebaseAdmin.Auth.EmailIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/email-identifier) | Used for looking up an account by email. |
| [FirebaseAdmin.Auth.ErrorInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/error-info) | Represents an error encountered while performing a batch operation such as AbstractFirebaseAuth.ImportUsersAsync(IEnumerable{ImportUserRecordArgs}) or AbstractFirebaseAuth.DeleteUsersAsync(IReadOnlyList{string}). |
| [FirebaseAdmin.Auth.ExportedUserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-record) | Contains metadata associated with a Firebase user account, along with password hash and salt. |
| [FirebaseAdmin.Auth.ExportedUserRecords](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-records) | Contains a collection of Firebase user accounts. |
| [FirebaseAdmin.Auth.FirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth) | This is the entry point to all server-side Firebase Authentication operations. |
| [FirebaseAdmin.Auth.FirebaseAuthException](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth-exception) | Exception type raised by Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) APIs. |
| [FirebaseAdmin.Auth.FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token) | Represents a valid, decoded Firebase ID token. |
| [FirebaseAdmin.Auth.GetUsersResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/get-users-result) | Represents the result of the AbstractFirebaseAuth.GetUsersAsync(IReadOnlyCollection{UserIdentifier}) API. |
| [FirebaseAdmin.Auth.ImportUserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args) | Represents a user account to be imported to Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) via the AbstractFirebaseAuth.ImportUsersAsync(IEnumerable{ImportUserRecordArgs}) API. |
| [FirebaseAdmin.Auth.ListUsersOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/list-users-options) | Options for the [AbstractFirebaseAuth.ListUsersAsync(ListUsersOptions)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a13c65216fc17ea092225befa7fff4015) API. |
| [FirebaseAdmin.Auth.PhoneIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/phone-identifier) | Used for looking up an account by phone number. |
| [FirebaseAdmin.Auth.ProviderIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/provider-identifier) | Used for looking up an account by provider. |
| [FirebaseAdmin.Auth.SessionCookieOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/session-cookie-options) | Options for the [FirebaseAuth.CreateSessionCookieAsync(string, SessionCookieOptions)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1adc3b86778805979f1936b726940159fb) API. |
| [FirebaseAdmin.Auth.UidIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/uid-identifier) | Used for looking up an account by uid. |
| [FirebaseAdmin.Auth.UserIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-identifier) | Identifies a user to be looked up. |
| [FirebaseAdmin.Auth.UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash) | Represents a hash algorithm and the related configuration parameters used to hash user passwords. |
| [FirebaseAdmin.Auth.UserImportOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-options) | A collection of options that can be passed to the [FirebaseAuth.ImportUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a0c827bb70808807d470f463e7badec98) API. |
| [FirebaseAdmin.Auth.UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result) | Represents the result of the AbstractFirebaseAuth.ImportUsersAsync(IEnumerable{ImportUserRecordArgs}) API. |
| [FirebaseAdmin.Auth.UserMetadata](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata) | Contains additional metadata associated with a user account. |
| [FirebaseAdmin.Auth.UserProvider](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-provider) | Represents a user identity provider that can be associated with a Firebase user. |
| [FirebaseAdmin.Auth.UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record) | Contains metadata associated with a Firebase user account. |
| [FirebaseAdmin.Auth.UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args) | A specification for creating or updating user accounts. |

| ### Interfaces ||
|---|---|
| [FirebaseAdmin.Auth.IUserInfo](https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info) | A collection of standard profile information for a user. |

| ### Namespaces ||
|---|---|
| [FirebaseAdmin.Auth.Hash](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth/hash) |   |
| [FirebaseAdmin.Auth.Jwt](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth/jwt) |   |
| [FirebaseAdmin.Auth.Multitenancy](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth/multitenancy) |   |
| [FirebaseAdmin.Auth.Providers](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth/providers) |   |
| [FirebaseAdmin.Auth.Users](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth/users) |   |

## Enumerations

### AuthErrorCode

```
 AuthErrorCode
```
Error codes that can be raised by the Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) APIs.

| Properties ||
|---|---|
| `CertificateFetchFailed` | Failed to retrieve required public key certificates. |
| `ConfigurationNotFound` | No identity provider configuration found for the given identifier. |
| `EmailAlreadyExists` | The user with the provided email already exists. |
| `EmailNotFound` | No user record found for the given email, typically raised when generating a password reset link using an email for a user that is not already registered. |
| `ExpiredIdToken` | The specified ID token is expired. |
| `ExpiredSessionCookie` | The specified session cookie is expired. |
| `InvalidDynamicLinkDomain` | Dynamic link domain specified in [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings) is not authorized. |
| `InvalidHostingLinkDomain` | The provided hosting link domain is not configured in Firebase Hosting or is not owned by the current project. |
| `InvalidIdToken` | The specified ID token is invalid. |
| `InvalidSessionCookie` | The specified session cookie is invalid. |
| `PhoneNumberAlreadyExists` | The user with the provided phone number already exists. |
| `RevokedIdToken` | The specified ID token has been revoked. |
| `RevokedSessionCookie` | The specified session cookie has been revoked. |
| `TenantIdMismatch` | Tenant ID in a token does not match. |
| `TenantNotFound` | No tenant found for the given identifier. |
| `UidAlreadyExists` | The user with the provided uid already exists. |
| `UnexpectedResponse` | Backend API responded with an unexpected message. |
| `UserNotFound` | No user record found for the given identifier. |