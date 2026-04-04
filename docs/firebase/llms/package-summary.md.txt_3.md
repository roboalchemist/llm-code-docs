# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/package-summary.md.txt

# com.google.firebase.auth

### Interfaces

|---|---|
| [UserInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo) | A collection of standard profile information for a user. |

### Classes

|---|---|
| [AbstractFirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth) | This is the abstract class for server-side Firebase Authentication actions. |
| [AbstractFirebaseAuth.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<T extends [Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<T\>\> |   |
| [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) | Defines the required continue/state URL with optional Android and iOS settings. |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) |   |
| [DeleteUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult) | Represents the result of the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUsersAsync(java.util.List<java.lang.String>)` API. |
| [EmailIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/EmailIdentifier) | Used for looking up an account by email. |
| [ErrorInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo) | Represents an error encountered while importing an `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord`. |
| [ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord) | Contains metadata associated with a Firebase user account, along with password hash and salt. |
| [FirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuth) | This class is the entry point for all server-side Firebase Authentication actions. |
| [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken) | A decoded and verified Firebase token. |
| [GetUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GetUsersResult) | Represents the result of the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUsersAsync(java.util.Collection<com.google.firebase.auth.UserIdentifier>)` API. |
| [ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord) | Represents a user account to be imported to Firebase Auth via the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)` API. |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) |   |
| [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<T extends [ProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig)\> | Represents a page of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig` instances. |
| [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage) | Represents a page of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord` instances. |
| [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) | Contains metadata associated with an OIDC Auth provider. |
| [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) | A specification class for creating a new OIDC Auth provider. |
| [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) | A specification class for updating an existing OIDC Auth provider. |
| [PhoneIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/PhoneIdentifier) | Used for looking up an account by phone number. |
| [ProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig) | The base class for Auth providers. |
| [ProviderConfig.AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)\<T extends [AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)\<T\>\> | A base specification class for creating a new provider. |
| [ProviderConfig.AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)\<T extends [AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)\<T\>\> | A base class for updating the attributes of an existing provider. |
| [ProviderIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderIdentifier) | Used for looking up an account by provider. |
| [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) | Contains metadata associated with a SAML Auth provider. |
| [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | A specification class for creating a new SAML Auth provider. |
| [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | A specification class for updating an existing SAML Auth provider. |
| [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions) | A set of additional options that can be passed to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSessionCookieAsync(java.lang.String, com.google.firebase.auth.SessionCookieOptions)`. |
| [SessionCookieOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions.Builder) |   |
| [UidIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UidIdentifier) | Used for looking up an account by uid. |
| [UserIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier) | Identifies a user to be looked up. |
| [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) | Represents a hash algorithm and the related configuration parameters used to hash user passwords. |
| [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) | A collection of options that can be passed to the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)` API. |
| [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder) |   |
| [UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult) | Represents the result of the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)` API. |
| [UserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata) | Contains additional metadata associated with a user account. |
| [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider) | Represents a user identity provider that can be associated with a Firebase user. |
| [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder) |   |
| [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) | Contains metadata associated with a Firebase user account. |
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | A specification class for creating new user accounts. |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | A class for updating the attributes of an existing user. |

### Enums

|---|---|
| [AuthErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AuthErrorCode) | Error codes that can be raised by the Firebase Auth APIs. |

### Exceptions

|---|---|
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | Generic exception related to Firebase Authentication. |