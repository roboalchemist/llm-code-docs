# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.md.txt

# AbstractFirebaseAuth

public abstract class **AbstractFirebaseAuth** extends Object  

|---|---|---|
| Known Direct Subclasses [FirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuth), [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantAwareFirebaseAuth) |----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------| | [FirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuth)                                    | This class is the entry point for all server-side Firebase Authentication actions. | | [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantAwareFirebaseAuth) | The tenant-aware Firebase client.                                                  | |||

This is the abstract class for server-side Firebase Authentication actions.  

### Nested Class Summary

|-------|---|---|---|
| class | [AbstractFirebaseAuth.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<T extends [Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<T\>\> ||   |

### Protected Constructor Summary

|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [AbstractFirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#AbstractFirebaseAuth(com.google.firebase.auth.AbstractFirebaseAuth.Builder<?>))([Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<?\> builder) |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String                                                                                                                                                                                                                                                                                        | [createCustomToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createCustomToken(java.lang.String))(String uid) Creates a Firebase custom token for the given UID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| String                                                                                                                                                                                                                                                                                        | [createCustomToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createCustomToken(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>))(String uid, Map\<String, Object\> developerClaims) Creates a Firebase custom token for the given UID, containing the specified additional claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ApiFuture\<String\>                                                                                                                                                                                                                                                                           | [createCustomTokenAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createCustomTokenAsync(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>))(String uid, Map\<String, Object\> developerClaims) Similar to [createCustomToken(String, Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createCustomToken(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                            |
| ApiFuture\<String\>                                                                                                                                                                                                                                                                           | [createCustomTokenAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createCustomTokenAsync(java.lang.String))(String uid) Similar to [createCustomToken(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createCustomToken(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)                                                                                                                                                             | [createOidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createOidcProviderConfig(com.google.firebase.auth.OidcProviderConfig.CreateRequest))([OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) request) Creates a new OpenID Connect auth provider config with the attributes contained in the specified [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest).                                                                                                                                                                                                           |
| ApiFuture\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>                                                                                                                                                | [createOidcProviderConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createOidcProviderConfigAsync(com.google.firebase.auth.OidcProviderConfig.CreateRequest))([OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) request) Similar to [createOidcProviderConfig(OidcProviderConfig.CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createOidcProviderConfig(com.google.firebase.auth.OidcProviderConfig.CreateRequest)) but performs the operation asynchronously.                                                                                                                                           |
| [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)                                                                                                                                                             | [createSamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSamlProviderConfig(com.google.firebase.auth.SamlProviderConfig.CreateRequest))([SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) request) Creates a new SAML Auth provider config with the attributes contained in the specified [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest).                                                                                                                                                                                                                     |
| ApiFuture\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>                                                                                                                                                | [createSamlProviderConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSamlProviderConfigAsync(com.google.firebase.auth.SamlProviderConfig.CreateRequest))([SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) request) Similar to [createSamlProviderConfig(SamlProviderConfig.CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSamlProviderConfig(com.google.firebase.auth.SamlProviderConfig.CreateRequest)) but performs the operation asynchronously.                                                                                                                                           |
| String                                                                                                                                                                                                                                                                                        | [createSessionCookie](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSessionCookie(java.lang.String, com.google.firebase.auth.SessionCookieOptions))(String idToken, [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions) options) Creates a new Firebase session cookie from the given ID token and options.                                                                                                                                                                                                                                                                                                                                                                                                            |
| ApiFuture\<String\>                                                                                                                                                                                                                                                                           | [createSessionCookieAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSessionCookieAsync(java.lang.String, com.google.firebase.auth.SessionCookieOptions))(String idToken, [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions) options) Similar to [createSessionCookie(String, SessionCookieOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSessionCookie(java.lang.String, com.google.firebase.auth.SessionCookieOptions)) but performs the operation asynchronously.                                                                                                                                                               |
| [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)                                                                                                                                                                             | [createUser](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createUser(com.google.firebase.auth.UserRecord.CreateRequest))([UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) request) Creates a new user account with the attributes contained in the specified [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest).                                                                                                                                                                                                                                                                                                      |
| ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>                                                                                                                                                                | [createUserAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createUserAsync(com.google.firebase.auth.UserRecord.CreateRequest))([UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) request) Similar to [createUser(UserRecord.CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createUser(com.google.firebase.auth.UserRecord.CreateRequest)) but performs the operation asynchronously.                                                                                                                                                                                                                                           |
| void                                                                                                                                                                                                                                                                                          | [deleteOidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteOidcProviderConfig(java.lang.String))(String providerId) Deletes the OpenID Connect auth provider config identified by the specified provider ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ApiFuture\<Void\>                                                                                                                                                                                                                                                                             | [deleteOidcProviderConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteOidcProviderConfigAsync(java.lang.String))(String providerId) Similar to [deleteOidcProviderConfig(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteOidcProviderConfig(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                           |
| void                                                                                                                                                                                                                                                                                          | [deleteSamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteSamlProviderConfig(java.lang.String))(String providerId) Deletes the SAML Auth provider config identified by the specified provider ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ApiFuture\<Void\>                                                                                                                                                                                                                                                                             | [deleteSamlProviderConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteSamlProviderConfigAsync(java.lang.String))(String providerId) Similar to [deleteSamlProviderConfig(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteSamlProviderConfig(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                           |
| void                                                                                                                                                                                                                                                                                          | [deleteUser](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUser(java.lang.String))(String uid) Deletes the user identified by the specified user ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ApiFuture\<Void\>                                                                                                                                                                                                                                                                             | [deleteUserAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUserAsync(java.lang.String))(String uid) Similar to [deleteUser(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUser(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [DeleteUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult)                                                                                                                                                               | [deleteUsers](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUsers(java.util.List<java.lang.String>))(List\<String\> uids) Deletes the users specified by the given identifiers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ApiFuture\<[DeleteUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult)\>                                                                                                                                                  | [deleteUsersAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUsersAsync(java.util.List<java.lang.String>))(List\<String\> uids) Similar to [deleteUsers(List)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUsers(java.util.List<java.lang.String>)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| String                                                                                                                                                                                                                                                                                        | [generateEmailVerificationLink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateEmailVerificationLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings))(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings) Generates the out-of-band email action link for email verification flows for the specified email address, using the action code settings provided.                                                                                                                                                                                                                                                                                                                       |
| String                                                                                                                                                                                                                                                                                        | [generateEmailVerificationLink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateEmailVerificationLink(java.lang.String))(String email) Generates the out-of-band email action link for email verification flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ApiFuture\<String\>                                                                                                                                                                                                                                                                           | [generateEmailVerificationLinkAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateEmailVerificationLinkAsync(java.lang.String, com.google.firebase.auth.ActionCodeSettings))(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings) Similar to [generateEmailVerificationLink(String, ActionCodeSettings)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateEmailVerificationLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings)) but performs the operation asynchronously.                                                                                                                                  |
| ApiFuture\<String\>                                                                                                                                                                                                                                                                           | [generateEmailVerificationLinkAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateEmailVerificationLinkAsync(java.lang.String))(String email) Similar to [generateEmailVerificationLink(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateEmailVerificationLink(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                            |
| String                                                                                                                                                                                                                                                                                        | [generatePasswordResetLink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generatePasswordResetLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings))(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings) Generates the out-of-band email action link for password reset flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                            |
| String                                                                                                                                                                                                                                                                                        | [generatePasswordResetLink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generatePasswordResetLink(java.lang.String))(String email) Generates the out-of-band email action link for password reset flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ApiFuture\<String\>                                                                                                                                                                                                                                                                           | [generatePasswordResetLinkAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generatePasswordResetLinkAsync(java.lang.String, com.google.firebase.auth.ActionCodeSettings))(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings) Similar to [generatePasswordResetLink(String, ActionCodeSettings)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generatePasswordResetLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings)) but performs the operation asynchronously.                                                                                                                                                  |
| ApiFuture\<String\>                                                                                                                                                                                                                                                                           | [generatePasswordResetLinkAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generatePasswordResetLinkAsync(java.lang.String))(String email) Similar to [generatePasswordResetLink(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generatePasswordResetLink(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                            |
| String                                                                                                                                                                                                                                                                                        | [generateSignInWithEmailLink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateSignInWithEmailLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings))(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings) Generates the out-of-band email action link for email link sign-in flows, using the action code settings provided.                                                                                                                                                                                                                                                                                                                                                           |
| ApiFuture\<String\>                                                                                                                                                                                                                                                                           | [generateSignInWithEmailLinkAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateSignInWithEmailLinkAsync(java.lang.String, com.google.firebase.auth.ActionCodeSettings))(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings) Similar to [generateSignInWithEmailLink(String, ActionCodeSettings)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateSignInWithEmailLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings)) but performs the operation asynchronously.                                                                                                                                          |
| [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)                                                                                                                                                             | [getOidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getOidcProviderConfig(java.lang.String))(String providerId) Gets the OpenID Connect auth provider corresponding to the specified provider ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ApiFuture\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>                                                                                                                                                | [getOidcProviderConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getOidcProviderConfigAsync(java.lang.String))(String providerId) Similar to [getOidcProviderConfig(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getOidcProviderConfig(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)                                                                                                                                                             | [getSamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getSamlProviderConfig(java.lang.String))(String providerId) Gets the SAML Auth provider config corresponding to the specified provider ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ApiFuture\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>                                                                                                                                                | [getSamlProviderConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getSamlProviderConfigAsync(java.lang.String))(String providerId) Similar to [getSamlProviderConfig(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getSamlProviderConfig(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)                                                                                                                                                                             | [getUser](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUser(java.lang.String))(String uid) Gets the user data corresponding to the specified user ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>                                                                                                                                                                | [getUserAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserAsync(java.lang.String))(String uid) Similar to [getUser(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUser(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)                                                                                                                                                                             | [getUserByEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserByEmail(java.lang.String))(String email) Gets the user data corresponding to the specified user email.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>                                                                                                                                                                | [getUserByEmailAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserByEmailAsync(java.lang.String))(String email) Similar to [getUserByEmail(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserByEmail(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)                                                                                                                                                                             | [getUserByPhoneNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserByPhoneNumber(java.lang.String))(String phoneNumber) Gets the user data corresponding to the specified user phone number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>                                                                                                                                                                | [getUserByPhoneNumberAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserByPhoneNumberAsync(java.lang.String))(String phoneNumber) Gets the user data corresponding to the specified user phone number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)                                                                                                                                                                             | [getUserByProviderUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserByProviderUid(java.lang.String, java.lang.String))(String providerId, String uid) Gets the user data for the user corresponding to a given provider ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>                                                                                                                                                                | [getUserByProviderUidAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserByProviderUidAsync(java.lang.String, java.lang.String))(String providerId, String uid) Gets the user data for the user corresponding to a given provider ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [GetUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GetUsersResult)                                                                                                                                                                     | [getUsers](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUsers(java.util.Collection<com.google.firebase.auth.UserIdentifier>))(Collection\<[UserIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier)\> identifiers) Gets the user data corresponding to the specified identifiers.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ApiFuture\<[GetUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GetUsersResult)\>                                                                                                                                                        | [getUsersAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUsersAsync(java.util.Collection<com.google.firebase.auth.UserIdentifier>))(Collection\<[UserIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier)\> identifiers) Gets the user data corresponding to the specified identifiers.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult)                                                                                                                                                                 | [importUsers](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>))(List\<[ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)\> users) Imports the provided list of users into Firebase Auth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult)                                                                                                                                                                 | [importUsers](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions))(List\<[ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)\> users, [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) options) Imports the provided list of users into Firebase Auth.                                                                                                                                                                                                                                                                                   |
| ApiFuture\<[UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult)\>                                                                                                                                                    | [importUsersAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>))(List\<[ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)\> users) Similar to [importUsers(List)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>)) but performs the operation asynchronously.                                                                                                                                                                                                                                                     |
| ApiFuture\<[UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult)\>                                                                                                                                                    | [importUsersAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions))(List\<[ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)\> users, [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) options) Similar to [importUsers(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)) but performs the operation asynchronously. |
| [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>              | [listOidcProviderConfigs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listOidcProviderConfigs(java.lang.String))(String pageToken) Gets a page of OpenID Connect auth provider configs starting from the specified `pageToken`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>              | [listOidcProviderConfigs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listOidcProviderConfigs(java.lang.String, int))(String pageToken, int maxResults) Gets a page of OpenID Connect auth provider configs starting from the specified `pageToken`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ApiFuture\<[ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>\> | [listOidcProviderConfigsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listOidcProviderConfigsAsync(java.lang.String))(String pageToken) Similar to [listOidcProviderConfigs(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listOidcProviderConfigs(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                |
| ApiFuture\<[ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>\> | [listOidcProviderConfigsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listOidcProviderConfigsAsync(java.lang.String, int))(String pageToken, int maxResults) Similar to [listOidcProviderConfigs(String, int)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listOidcProviderConfigs(java.lang.String, int)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                 |
| [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>              | [listSamlProviderConfigs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listSamlProviderConfigs(java.lang.String))(String pageToken) Gets a page of SAML Auth provider configs starting from the specified `pageToken`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>              | [listSamlProviderConfigs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listSamlProviderConfigs(java.lang.String, int))(String pageToken, int maxResults) Gets a page of SAML Auth provider configs starting from the specified `pageToken`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ApiFuture\<[ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>\> | [listSamlProviderConfigsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listSamlProviderConfigsAsync(java.lang.String))(String pageToken) Similar to [listSamlProviderConfigs(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listSamlProviderConfigs(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                |
| ApiFuture\<[ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>\> | [listSamlProviderConfigsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listSamlProviderConfigsAsync(java.lang.String, int))(String pageToken, int maxResults) Similar to [listSamlProviderConfigs(String, int)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listSamlProviderConfigs(java.lang.String, int)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                 |
| [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)                                                                                                                                                                       | [listUsers](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listUsers(java.lang.String, int))(String pageToken, int maxResults) Gets a page of users starting from the specified `pageToken`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)                                                                                                                                                                       | [listUsers](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listUsers(java.lang.String))(String pageToken) Gets a page of users starting from the specified `pageToken`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ApiFuture\<[ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)\>                                                                                                                                                          | [listUsersAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listUsersAsync(java.lang.String, int))(String pageToken, int maxResults) Similar to [listUsers(String, int)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listUsers(java.lang.String, int)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ApiFuture\<[ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)\>                                                                                                                                                          | [listUsersAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listUsersAsync(java.lang.String))(String pageToken) Similar to [listUsers(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listUsers(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| void                                                                                                                                                                                                                                                                                          | [revokeRefreshTokens](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#revokeRefreshTokens(java.lang.String))(String uid) Revokes all refresh tokens for the specified user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ApiFuture\<Void\>                                                                                                                                                                                                                                                                             | [revokeRefreshTokensAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#revokeRefreshTokensAsync(java.lang.String))(String uid) Similar to [revokeRefreshTokens(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#revokeRefreshTokens(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| void                                                                                                                                                                                                                                                                                          | [setCustomClaims](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#setCustomClaims(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>))(String uid, Map\<String, Object\> claims) *This method is deprecated. Use [setCustomUserClaims(String, Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#setCustomUserClaims(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>)) instead.*                                                                                                                                                                                                                                                                                                                           |
| void                                                                                                                                                                                                                                                                                          | [setCustomUserClaims](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#setCustomUserClaims(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>))(String uid, Map\<String, Object\> claims) Sets the specified custom claims on an existing user account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ApiFuture\<Void\>                                                                                                                                                                                                                                                                             | [setCustomUserClaimsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#setCustomUserClaimsAsync(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>))(String uid, Map\<String, Object\> claims) Similar to [setCustomUserClaims(String, Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#setCustomUserClaims(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                             |
| [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)                                                                                                                                                             | [updateOidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateOidcProviderConfig(com.google.firebase.auth.OidcProviderConfig.UpdateRequest))([OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) request) Updates an existing OpenID Connect auth provider config with the attributes contained in the specified [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest).                                                                                                                                                                                                     |
| ApiFuture\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>                                                                                                                                                | [updateOidcProviderConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateOidcProviderConfigAsync(com.google.firebase.auth.OidcProviderConfig.UpdateRequest))([OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) request) Similar to [updateOidcProviderConfig(OidcProviderConfig.UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateOidcProviderConfig(com.google.firebase.auth.OidcProviderConfig.UpdateRequest)) but performs the operation asynchronously.                                                                                                                                           |
| [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)                                                                                                                                                             | [updateSamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateSamlProviderConfig(com.google.firebase.auth.SamlProviderConfig.UpdateRequest))([SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) request) Updates an existing SAML Auth provider config with the attributes contained in the specified [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest).                                                                                                                                                                                                               |
| ApiFuture\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>                                                                                                                                                | [updateSamlProviderConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateSamlProviderConfigAsync(com.google.firebase.auth.SamlProviderConfig.UpdateRequest))([SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) request) Similar to [updateSamlProviderConfig(SamlProviderConfig.UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateSamlProviderConfig(com.google.firebase.auth.SamlProviderConfig.UpdateRequest)) but performs the operation asynchronously.                                                                                                                                           |
| [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)                                                                                                                                                                             | [updateUser](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateUser(com.google.firebase.auth.UserRecord.UpdateRequest))([UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) request) Updates an existing user account with the attributes contained in the specified [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest).                                                                                                                                                                                                                                                                                                |
| ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>                                                                                                                                                                | [updateUserAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateUserAsync(com.google.firebase.auth.UserRecord.UpdateRequest))([UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) request) Similar to [updateUser(UserRecord.UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateUser(com.google.firebase.auth.UserRecord.UpdateRequest)) but performs the operation asynchronously.                                                                                                                                                                                                                                           |
| [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)                                                                                                                                                                       | [verifyIdToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdToken(java.lang.String, boolean))(String idToken, boolean checkRevoked) Parses and verifies a Firebase ID Token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)                                                                                                                                                                       | [verifyIdToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdToken(java.lang.String))(String idToken) Parses and verifies a Firebase ID Token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ApiFuture\<[FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)\>                                                                                                                                                          | [verifyIdTokenAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdTokenAsync(java.lang.String))(String idToken) Similar to [verifyIdToken(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdToken(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ApiFuture\<[FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)\>                                                                                                                                                          | [verifyIdTokenAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdTokenAsync(java.lang.String, boolean))(String idToken, boolean checkRevoked) Similar to [verifyIdToken(String, boolean)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdToken(java.lang.String, boolean)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                         |
| [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)                                                                                                                                                                       | [verifySessionCookie](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookie(java.lang.String, boolean))(String cookie, boolean checkRevoked) Parses and verifies a Firebase session cookie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)                                                                                                                                                                       | [verifySessionCookie](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookie(java.lang.String))(String cookie) Parses and verifies a Firebase session cookie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ApiFuture\<[FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)\>                                                                                                                                                          | [verifySessionCookieAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookieAsync(java.lang.String, boolean))(String cookie, boolean checkRevoked) Similar to [verifySessionCookie(String, boolean)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookie(java.lang.String, boolean)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                  |
| ApiFuture\<[FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)\>                                                                                                                                                          | [verifySessionCookieAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookieAsync(java.lang.String))(String cookie) Similar to [verifySessionCookie(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookie(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Protected Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static \<T extends [Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<T\>\> T | [populateBuilderFromApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#populateBuilderFromApp(com.google.firebase.auth.AbstractFirebaseAuth.Builder<T>, com.google.firebase.FirebaseApp, java.lang.String))([Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<T\> builder, [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app, String tenantId) |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Protected Constructors

#### protected
**AbstractFirebaseAuth**
([Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<?\> builder)

<br />

## Public Methods

#### public String
**createCustomToken**
(String uid)

Creates a Firebase custom token for the given UID. This token can then be sent back to a client
application to be used with the [signInWithCustomToken](https://firebase.google.com/docs/auth/admin/create-custom-tokens#sign_in_using_custom_tokens_on_clients)
authentication API.

[FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) must have been initialized with service account credentials to use call
this method.  

##### Parameters

| uid | The UID to store in the token. This identifies the user to other Firebase services (Realtime Database, Firebase Auth, etc.). Should be less than 128 characters. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A Firebase custom token string.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the specified uid is null or empty, or if the app has not been initialized with service account credentials. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                              If an error occurs while generating the custom token.                              |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|

#### public String
**createCustomToken**
(String uid, Map\<String, Object\> developerClaims)

Creates a Firebase custom token for the given UID, containing the specified additional claims.
This token can then be sent back to a client application to be used with the [signInWithCustomToken](https://firebase.google.com/docs/auth/admin/create-custom-tokens#sign_in_using_custom_tokens_on_clients)
authentication API.

This method attempts to generate a token using:

1. the private key of [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)'s service account credentials, if provided at initialization.
2. the [IAM
   service](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts/signBlob) if a service account email was specified via [setServiceAccountId(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setServiceAccountId(java.lang.String)).
3. the [App
   Identity service](https://cloud.google.com/appengine/docs/standard/java/appidentity/) if the code is deployed in the Google App Engine standard environment.
4. the [local
   Metadata server](https://cloud.google.com/compute/docs/storing-retrieving-metadata) if the code is deployed in a different GCP-managed environment like Google Compute Engine.

This method throws an exception when all the above fail.  

##### Parameters

|       uid       |                               The UID to store in the token. This identifies the user to other Firebase services (Realtime Database, Firebase Auth, etc.). Should be less than 128 characters.                                |
| developerClaims | Additional claims to be stored in the token (and made available to security rules in Database, Storage, etc.). These must be able to be serialized to JSON (e.g. contain only Maps, Arrays, Strings, Booleans, Numbers, etc.) |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A Firebase custom token string.  

##### Throws

|                                                        IllegalArgumentException                                                         |               If the specified uid is null or empty.               |
|                                                          IllegalStateException                                                          | If the SDK fails to discover a viable approach for signing tokens. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |       If an error occurs while generating the custom token.        |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|

#### public ApiFuture\<String\>
**createCustomTokenAsync**
(String uid, Map\<String, Object\> developerClaims)

Similar to [createCustomToken(String, Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createCustomToken(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>)) but performs the operation asynchronously.  

##### Parameters

|       uid       |                                  The UID to store in the token. This identifies the user to other Firebase services (Realtime Database, Storage, etc.). Should be less than 128 characters.                                   |
| developerClaims | Additional claims to be stored in the token (and made available to security rules in Database, Storage, etc.). These must be able to be serialized to JSON (e.g. contain only Maps, Arrays, Strings, Booleans, Numbers, etc.) |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the created Firebase custom token, or unsuccessfully with the failure Exception.  

##### Throws

| IllegalArgumentException | If the specified uid is null or empty, or if the app has not been initialized with service account credentials. |
|--------------------------|-----------------------------------------------------------------------------------------------------------------|

#### public ApiFuture\<String\>
**createCustomTokenAsync**
(String uid)

Similar to [createCustomToken(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createCustomToken(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| uid | The UID to store in the token. This identifies the user to other Firebase services (Realtime Database, Firebase Auth, etc.). Should be less than 128 characters. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the created Firebase custom token, or unsuccessfully with the failure Exception.  

##### Throws

| IllegalArgumentException | If the specified uid is null or empty, or if the app has not been initialized with service account credentials. |
|--------------------------|-----------------------------------------------------------------------------------------------------------------|

#### public [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)
**createOidcProviderConfig**
([OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) request)

Creates a new OpenID Connect auth provider config with the attributes contained in the
specified [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest).  

##### Parameters

| request | A non-null [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) instance. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) instance corresponding to the newly created provider config.  

##### Throws

|                                                          NullPointerException                                                           |                       if the provided request is null.                       |
|                                                        IllegalArgumentException                                                         | If the provider ID string is null or empty, or is not prefixed with 'oidc.'. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |            if an error occurs while creating the provider config.            |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|

#### public ApiFuture\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>
**createOidcProviderConfigAsync**
([OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) request)

Similar to [createOidcProviderConfig(OidcProviderConfig.CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createOidcProviderConfig(com.google.firebase.auth.OidcProviderConfig.CreateRequest)) but performs the operation asynchronously.  

##### Parameters

| request | A non-null [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) instance. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) instance corresponding to the newly created provider config. If an error occurs while creating the provider config, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

|   NullPointerException   |                       if the provided request is null.                       |
| IllegalArgumentException | If the provider ID string is null or empty, or is not prefixed with 'oidc.'. |
|--------------------------|------------------------------------------------------------------------------|

#### public [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)
**createSamlProviderConfig**
([SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) request)

Creates a new SAML Auth provider config with the attributes contained in the specified
[SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest).  

##### Parameters

| request | A non-null [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) instance. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) instance corresponding to the newly created provider config.  

##### Throws

|                                                          NullPointerException                                                           |                      if the provided request is null.                       |
|                                                        IllegalArgumentException                                                         | If the provider ID string is null or empty, or is not prefixed with 'saml'. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |           if an error occurs while creating the provider config.            |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|

#### public ApiFuture\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>
**createSamlProviderConfigAsync**
([SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) request)

Similar to [createSamlProviderConfig(SamlProviderConfig.CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSamlProviderConfig(com.google.firebase.auth.SamlProviderConfig.CreateRequest)) but performs the operation asynchronously.  

##### Parameters

| request | A non-null [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) instance. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) instance corresponding to the newly created provider config. If an error occurs while creating the provider config, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

|   NullPointerException   |                      if the provided request is null.                       |
| IllegalArgumentException | If the provider ID string is null or empty, or is not prefixed with 'saml'. |
|--------------------------|-----------------------------------------------------------------------------|

#### public String
**createSessionCookie**
(String idToken, [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions) options)

Creates a new Firebase session cookie from the given ID token and options. The returned JWT can
be set as a server-side session cookie with a custom cookie policy.  

##### Parameters

| idToken | The Firebase ID token to exchange for a session cookie. |
| options |    Additional options required to create the cookie.    |
|---------|---------------------------------------------------------|

##### Returns

- A Firebase session cookie string.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the ID token is null or empty, or if options is null. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while generating the session cookie.  |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|

#### public ApiFuture\<String\>
**createSessionCookieAsync**
(String idToken, [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions) options)

Similar to [createSessionCookie(String, SessionCookieOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSessionCookie(java.lang.String, com.google.firebase.auth.SessionCookieOptions)) but performs the
operation asynchronously.  

##### Parameters

| idToken | The Firebase ID token to exchange for a session cookie. |
| options |    Additional options required to create the cookie.    |
|---------|---------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a session cookie string. If an error occurs while generating the cookie or if the specified ID token is invalid, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the ID token is null or empty, or if options is null. |
|--------------------------|----------------------------------------------------------|

#### public [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)
**createUser**
([UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) request)

Creates a new user account with the attributes contained in the specified [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest).  

##### Parameters

| request | A non-null [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) instance. |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance corresponding to the newly created account.  

##### Throws

|                                                          NullPointerException                                                           |          if the provided request is null.           |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | if an error occurs while creating the user account. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|

#### public ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>
**createUserAsync**
([UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) request)

Similar to [createUser(UserRecord.CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createUser(com.google.firebase.auth.UserRecord.CreateRequest)) but performs the operation asynchronously.  

##### Parameters

| request | A non-null [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) instance. |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance corresponding to the newly created account. If an error occurs while creating the user account, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| NullPointerException | if the provided request is null. |
|----------------------|----------------------------------|

#### public void
**deleteOidcProviderConfig**
(String providerId)

Deletes the OpenID Connect auth provider config identified by the specified provider ID.  

##### Parameters

| providerId | A provider ID string. |
|------------|-----------------------|

##### Throws

|                                                        IllegalArgumentException                                                         | If the provider ID string is null or empty, or is not prefixed with 'oidc'. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |           If an error occurs while deleting the provider config.            |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|

#### public ApiFuture\<Void\>
**deleteOidcProviderConfigAsync**
(String providerId)

Similar to [deleteOidcProviderConfig(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteOidcProviderConfig(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| providerId | A provider ID string. |
|------------|-----------------------|

##### Returns

- An `ApiFuture` which will complete successfully when the specified provider config has been deleted. If an error occurs while deleting the provider config, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the provider ID string is null or empty, or is not prefixed with "oidc.". |
|--------------------------|------------------------------------------------------------------------------|

#### public void
**deleteSamlProviderConfig**
(String providerId)

Deletes the SAML Auth provider config identified by the specified provider ID.  

##### Parameters

| providerId | A provider ID string. |
|------------|-----------------------|

##### Throws

|                                                        IllegalArgumentException                                                         | If the provider ID string is null or empty, or is not prefixed with "saml.". |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |            If an error occurs while deleting the provider config.            |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|

#### public ApiFuture\<Void\>
**deleteSamlProviderConfigAsync**
(String providerId)

Similar to [deleteSamlProviderConfig(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteSamlProviderConfig(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| providerId | A provider ID string. |
|------------|-----------------------|

##### Returns

- An `ApiFuture` which will complete successfully when the specified provider config has been deleted. If an error occurs while deleting the provider config, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the provider ID string is null or empty, or is not prefixed with "saml.". |
|--------------------------|------------------------------------------------------------------------------|

#### public void
**deleteUser**
(String uid)

Deletes the user identified by the specified user ID.  

##### Parameters

| uid | A user ID string. |
|-----|-------------------|

##### Throws

|                                                        IllegalArgumentException                                                         |   If the user ID string is null or empty.   |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while deleting the user. |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|

#### public ApiFuture\<Void\>
**deleteUserAsync**
(String uid)

Similar to [deleteUser(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUser(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| uid | A user ID string. |
|-----|-------------------|

##### Returns

- An `ApiFuture` which will complete successfully when the specified user account has been deleted. If an error occurs while deleting the user account, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the user ID string is null or empty. |
|--------------------------|-----------------------------------------|

#### public [DeleteUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult)
**deleteUsers**
(List\<String\> uids)

Deletes the users specified by the given identifiers.

Deleting a non-existing user does not generate an error (the method is idempotent).
Non-existing users are considered to be successfully deleted and are therefore included in the
DeleteUsersResult.getSuccessCount() value.

A maximum of 1000 identifiers may be supplied. If more than 1000 identifiers are
supplied, this method throws an `IllegalArgumentException`.

This API has a rate limit of 1 QPS. Exceeding the limit may result in a quota exceeded
error. If you want to delete more than 1000 users, we suggest adding a delay to ensure you
don't exceed this limit.  

##### Parameters

| uids | The uids of the users to be deleted. Must have \<= 1000 entries. |
|------|------------------------------------------------------------------|

##### Returns

- The total number of successful/failed deletions, as well as the array of errors that correspond to the failed deletions.  

##### Throws

|                                                        IllegalArgumentException                                                         | If any of the identifiers are invalid or if more than 1000 identifiers are specified. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                       If an error occurs while deleting users.                        |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|

#### public ApiFuture\<[DeleteUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult)\>
**deleteUsersAsync**
(List\<String\> uids)

Similar to [deleteUsers(List)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUsers(java.util.List<java.lang.String>)) but performs the operation asynchronously.  

##### Parameters

| uids | The uids of the users to be deleted. Must have \<= 1000 entries. |
|------|------------------------------------------------------------------|

##### Returns

- An `ApiFuture` that resolves to the total number of successful/failed deletions, as well as the array of errors that correspond to the failed deletions. If an error occurs while deleting the user account, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If any of the identifiers are invalid or if more than 1000 identifiers are specified. |
|--------------------------|---------------------------------------------------------------------------------------|

#### public String
**generateEmailVerificationLink**
(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings)

Generates the out-of-band email action link for email verification flows for the specified
email address, using the action code settings provided.  

##### Parameters

| email | The email of the user to be verified. |
|-------|---------------------------------------|

##### Returns

- An email verification link.  

##### Throws

|                                                        IllegalArgumentException                                                         |    If the email address is null or empty.     |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while generating the link. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|

#### public String
**generateEmailVerificationLink**
(String email)

Generates the out-of-band email action link for email verification flows for the specified
email address.  

##### Parameters

| email | The email of the user to be verified. |
|-------|---------------------------------------|

##### Returns

- An email verification link.  

##### Throws

|                                                        IllegalArgumentException                                                         |    If the email address is null or empty.     |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while generating the link. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|

#### public ApiFuture\<String\>
**generateEmailVerificationLinkAsync**
(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings)

Similar to [generateEmailVerificationLink(String, ActionCodeSettings)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateEmailVerificationLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings)) but performs the
operation asynchronously.  

##### Parameters

|  email   |                                                                The email of the user to be verified.                                                                |
| settings | The action code settings object which defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the generated email action link. If an error occurs while generating the link, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the email address is null or empty. |
|--------------------------|----------------------------------------|

#### public ApiFuture\<String\>
**generateEmailVerificationLinkAsync**
(String email)

Similar to [generateEmailVerificationLink(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateEmailVerificationLink(java.lang.String)) but performs the operation
asynchronously.  

##### Parameters

| email | The email of the user to be verified. |
|-------|---------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the generated email action link. If an error occurs while generating the link, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the email address is null or empty. |
|--------------------------|----------------------------------------|

#### public String
**generatePasswordResetLink**
(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings)

Generates the out-of-band email action link for password reset flows for the specified email
address.  

##### Parameters

|  email   |                                                        The email of the user whose password is to be reset.                                                         |
| settings | The action code settings object which defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A password reset link.  

##### Throws

|                                                        IllegalArgumentException                                                         |    If the email address is null or empty.     |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while generating the link. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|

#### public String
**generatePasswordResetLink**
(String email)

Generates the out-of-band email action link for password reset flows for the specified email
address.  

##### Parameters

| email | The email of the user whose password is to be reset. |
|-------|------------------------------------------------------|

##### Returns

- A password reset link.  

##### Throws

|                                                        IllegalArgumentException                                                         |    If the email address is null or empty.     |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while generating the link. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|

#### public ApiFuture\<String\>
**generatePasswordResetLinkAsync**
(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings)

Similar to [generatePasswordResetLink(String, ActionCodeSettings)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generatePasswordResetLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings)) but performs the
operation asynchronously.  

##### Parameters

|  email   |                                                        The email of the user whose password is to be reset.                                                         |
| settings | The action code settings object which defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the generated email action link. If an error occurs while generating the link, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the email address is null or empty. |
|--------------------------|----------------------------------------|

#### public ApiFuture\<String\>
**generatePasswordResetLinkAsync**
(String email)

Similar to [generatePasswordResetLink(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generatePasswordResetLink(java.lang.String)) but performs the operation
asynchronously.  

##### Parameters

| email | The email of the user whose password is to be reset. |
|-------|------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the generated email action link. If an error occurs while generating the link, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the email address is null or empty. |
|--------------------------|----------------------------------------|

#### public String
**generateSignInWithEmailLink**
(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings)

Generates the out-of-band email action link for email link sign-in flows, using the action code
settings provided.  

##### Parameters

|  email   |                                                                  The email of the user signing in.                                                                  |
| settings | The action code settings object which defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An email verification link.  

##### Throws

|                                                        IllegalArgumentException                                                         |    If the email address is null or empty.     |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while generating the link. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|

#### public ApiFuture\<String\>
**generateSignInWithEmailLinkAsync**
(String email, [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) settings)

Similar to [generateSignInWithEmailLink(String, ActionCodeSettings)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#generateSignInWithEmailLink(java.lang.String, com.google.firebase.auth.ActionCodeSettings)) but performs the
operation asynchronously.  

##### Parameters

|  email   |                                                                  The email of the user signing in.                                                                  |
| settings | The action code settings object which defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the generated email action link. If an error occurs while generating the link, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the email address is null or empty. |
|   NullPointerException   |        If the settings is null.        |
|--------------------------|----------------------------------------|

#### public [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)
**getOidcProviderConfig**
(String providerId)

Gets the OpenID Connect auth provider corresponding to the specified provider ID.  

##### Parameters

| providerId | A provider ID string. |
|------------|-----------------------|

##### Returns

- An [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the provider ID string is null or empty, or is not prefixed with 'oidc'. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |          If an error occurs while retrieving the provider config.           |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|

#### public ApiFuture\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>
**getOidcProviderConfigAsync**
(String providerId)

Similar to [getOidcProviderConfig(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getOidcProviderConfig(java.lang.String)) but performs the operation asynchronously.
Page size is limited to 100 provider configs.  

##### Parameters

| providerId | A provider ID string. |
|------------|-----------------------|

##### Returns

- An `ApiFuture` which will complete successfully with an [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) instance. If an error occurs while retrieving the provider config or if the specified provider ID does not exist, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the provider ID string is null or empty, or is not prefixed with 'oidc.'. |
|--------------------------|------------------------------------------------------------------------------|

#### public [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)
**getSamlProviderConfig**
(String providerId)

Gets the SAML Auth provider config corresponding to the specified provider ID.  

##### Parameters

| providerId | A provider ID string. |
|------------|-----------------------|

##### Returns

- An [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the provider ID string is null or empty, or is not prefixed with 'saml'. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |          If an error occurs while retrieving the provider config.           |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|

#### public ApiFuture\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>
**getSamlProviderConfigAsync**
(String providerId)

Similar to [getSamlProviderConfig(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getSamlProviderConfig(java.lang.String)) but performs the operation asynchronously.
Page size is limited to 100 provider configs.  

##### Parameters

| providerId | A provider ID string. |
|------------|-----------------------|

##### Returns

- An `ApiFuture` which will complete successfully with an [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) instance. If an error occurs while retrieving the provider config or if the specified provider ID does not exist, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the provider ID string is null or empty, or is not prefixed with 'saml'. |
|--------------------------|-----------------------------------------------------------------------------|

#### public [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)
**getUser**
(String uid)

Gets the user data corresponding to the specified user ID.  

##### Parameters

| uid | A user ID string. |
|-----|-------------------|

##### Returns

- A [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         |    If the user ID string is null or empty.     |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while retrieving user data. |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|

#### public ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>
**getUserAsync**
(String uid)

Similar to [getUser(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUser(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| uid | A user ID string. |
|-----|-------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance. If an error occurs while retrieving user data or if the specified user ID does not exist, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the user ID string is null or empty. |
|--------------------------|-----------------------------------------|

#### public [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)
**getUserByEmail**
(String email)

Gets the user data corresponding to the specified user email.  

##### Parameters

| email | A user email address string. |
|-------|------------------------------|

##### Returns

- A [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         |         If the email is null or empty.         |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while retrieving user data. |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|

#### public ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>
**getUserByEmailAsync**
(String email)

Similar to [getUserByEmail(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUserByEmail(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| email | A user email address string. |
|-------|------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance. If an error occurs while retrieving user data or if the email address does not correspond to a user, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the email is null or empty. |
|--------------------------|--------------------------------|

#### public [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)
**getUserByPhoneNumber**
(String phoneNumber)

Gets the user data corresponding to the specified user phone number.  

##### Parameters

| phoneNumber | A user phone number string. |
|-------------|-----------------------------|

##### Returns

- A a [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         |     If the phone number is null or empty.      |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while retrieving user data. |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|

#### public ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>
**getUserByPhoneNumberAsync**
(String phoneNumber)

Gets the user data corresponding to the specified user phone number.  

##### Parameters

| phoneNumber | A user phone number string. |
|-------------|-----------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance. If an error occurs while retrieving user data or if the phone number does not correspond to a user, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the phone number is null or empty. |
|--------------------------|---------------------------------------|

#### public [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)
**getUserByProviderUid**
(String providerId, String uid)

Gets the user data for the user corresponding to a given provider ID.  

##### Parameters

| providerId | Identifier for the given federated provider: for example, "google.com" for the Google provider. |
|    uid     |                          The user identifier with the given provider.                           |
|------------|-------------------------------------------------------------------------------------------------|

##### Returns

- A [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the uid is null or empty, or if the providerId is null, empty, or does not belong to a federated provider. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                                If an error occurs while retrieving user data.                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|

#### public ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>
**getUserByProviderUidAsync**
(String providerId, String uid)

Gets the user data for the user corresponding to a given provider ID.  

##### Parameters

| providerId | Identifer for the given federated provider: for example, "google.com" for the Google provider. |
|    uid     |                          The user identifier with the given provider.                          |
|------------|------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance. If an error occurs while retrieving user data or if the provider ID and uid do not correspond to a user, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the uid is null or empty, or if the provider ID is null, empty, or does not belong to a federated provider. |
|--------------------------|----------------------------------------------------------------------------------------------------------------|

#### public [GetUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GetUsersResult)
**getUsers**
(Collection\<[UserIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier)\> identifiers)

Gets the user data corresponding to the specified identifiers.

There are no ordering guarantees; in particular, the nth entry in the users result list is
not guaranteed to correspond to the nth entry in the input parameters list.

A maximum of 100 identifiers may be specified. If more than 100 identifiers are
supplied, this method throws an `IllegalArgumentException`.  

##### Parameters

| identifiers | The identifiers used to indicate which user records should be returned. Must have 100 or fewer entries. |
|-------------|---------------------------------------------------------------------------------------------------------|

##### Returns

- The corresponding user records.  

##### Throws

|                                                        IllegalArgumentException                                                         | If any of the identifiers are invalid or if more than 100 identifiers are specified. |
|                                                          NullPointerException                                                           |                        If the identifiers parameter is null.                         |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                    If an error occurs while retrieving user data.                    |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|

#### public ApiFuture\<[GetUsersResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GetUsersResult)\>
**getUsersAsync**
(Collection\<[UserIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier)\> identifiers)

Gets the user data corresponding to the specified identifiers.

There are no ordering guarantees; in particular, the nth entry in the users result list is
not guaranteed to correspond to the nth entry in the input parameters list.

A maximum of 100 identifiers may be specified. If more than 100 identifiers are
supplied, this method throws an `IllegalArgumentException`.  

##### Parameters

| identifiers | The identifiers used to indicate which user records should be returned. Must have 100 or fewer entries. |
|-------------|---------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` that resolves to the corresponding user records.  

##### Throws

| IllegalArgumentException | If any of the identifiers are invalid or if more than 100 identifiers are specified. |
|   NullPointerException   |                        If the identifiers parameter is null.                         |
|--------------------------|--------------------------------------------------------------------------------------|

#### public [UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult)
**importUsers**
(List\<[ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)\> users)

Imports the provided list of users into Firebase Auth. At most 1000 users can be imported at a
time. This operation is optimized for bulk imports and will ignore checks on identifier
uniqueness which could result in duplications.

[UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) is required to import users with passwords. See [importUsers(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)).  

##### Parameters

| users | A non-empty list of users to be imported. Length must not exceed 1000. |
|-------|------------------------------------------------------------------------|

##### Returns

- A [UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the users list is null, empty or has more than 1000 elements. Or if at least one user specifies a password. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                                   If an error occurs while importing users.                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|

#### public [UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult)
**importUsers**
(List\<[ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)\> users, [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) options)

Imports the provided list of users into Firebase Auth. At most 1000 users can be imported at a
time. This operation is optimized for bulk imports and will ignore checks on identifier
uniqueness which could result in duplications.  

##### Parameters

|  users  |                                                              A non-empty list of users to be imported. Length must not exceed 1000.                                                               |
| options | a [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) instance or null. Required when importing users with passwords. |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the users list is null, empty or has more than 1000 elements. Or if at least one user specifies a password, and options is null. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                                              If an error occurs while importing users.                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|

#### public ApiFuture\<[UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult)\>
**importUsersAsync**
(List\<[ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)\> users)

Similar to [importUsers(List)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>)) but performs the operation asynchronously.  

##### Parameters

| users | A non-empty list of users to be imported. Length must not exceed 1000. |
|-------|------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully when the user accounts are imported. If an error occurs while importing the users, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the users list is null, empty or has more than 1000 elements. Or if at least one user specifies a password. |
|--------------------------|----------------------------------------------------------------------------------------------------------------|

#### public ApiFuture\<[UserImportResult](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult)\>
**importUsersAsync**
(List\<[ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)\> users, [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) options)

Similar to [importUsers(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)) but performs the operation
asynchronously.  

##### Parameters

|  users  |                                                              A non-empty list of users to be imported. Length must not exceed 1000.                                                               |
| options | a [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) instance or null. Required when importing users with passwords. |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully when the user accounts are imported. If an error occurs while importing the users, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the users list is null, empty or has more than 1000 elements. Or if at least one user specifies a password, and options is null. |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------|

#### public [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>
**listOidcProviderConfigs**
(String pageToken)

Gets a page of OpenID Connect auth provider configs starting from the specified
`pageToken`. Page size is limited to 100 provider configs.  

##### Parameters

| pageToken | A non-empty page token string, or null to retrieve the first page of provider configs. |
|-----------|----------------------------------------------------------------------------------------|

##### Returns

- A [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         |           If the specified page token is empty            |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while retrieving provider config data. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|

#### public [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>
**listOidcProviderConfigs**
(String pageToken, int maxResults)

Gets a page of OpenID Connect auth provider configs starting from the specified
`pageToken`.  

##### Parameters

| pageToken  |    A non-empty page token string, or null to retrieve the first page of provider configs.    |
| maxResults | Maximum number of provider configs to include in the returned page. This may not exceed 100. |
|------------|----------------------------------------------------------------------------------------------|

##### Returns

- A [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the specified page token is empty, or max results value is invalid. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |       If an error occurs while retrieving provider config data.        |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|

#### public ApiFuture\<[ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>\>
**listOidcProviderConfigsAsync**
(String pageToken)

Similar to [listOidcProviderConfigs(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listOidcProviderConfigs(java.lang.String)) but performs the operation asynchronously.
Page size is limited to 100 provider configs.  

##### Parameters

| pageToken | A non-empty page token string, or null to retrieve the first page of provider configs. |
|-----------|----------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance. If an error occurs while retrieving provider config data, the future throws an exception.  

##### Throws

| IllegalArgumentException | If the specified page token is empty. |
|--------------------------|---------------------------------------|

#### public ApiFuture\<[ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>\>
**listOidcProviderConfigsAsync**
(String pageToken, int maxResults)

Similar to [listOidcProviderConfigs(String, int)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listOidcProviderConfigs(java.lang.String, int)) but performs the operation
asynchronously.  

##### Parameters

| pageToken  |    A non-empty page token string, or null to retrieve the first page of provider configs.    |
| maxResults | Maximum number of provider configs to include in the returned page. This may not exceed 100. |
|------------|----------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance. If an error occurs while retrieving provider config data, the future throws an exception.  

##### Throws

| IllegalArgumentException | If the specified page token is empty, or max results value is invalid. |
|--------------------------|------------------------------------------------------------------------|

#### public [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>
**listSamlProviderConfigs**
(String pageToken)

Gets a page of SAML Auth provider configs starting from the specified `pageToken`. Page
size is limited to 100 provider configs.  

##### Parameters

| pageToken | A non-empty page token string, or null to retrieve the first page of provider configs. |
|-----------|----------------------------------------------------------------------------------------|

##### Returns

- A [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         |           If the specified page token is empty.           |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while retrieving provider config data. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|

#### public [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>
**listSamlProviderConfigs**
(String pageToken, int maxResults)

Gets a page of SAML Auth provider configs starting from the specified `pageToken`.  

##### Parameters

| pageToken  |    A non-empty page token string, or null to retrieve the first page of provider configs.    |
| maxResults | Maximum number of provider configs to include in the returned page. This may not exceed 100. |
|------------|----------------------------------------------------------------------------------------------|

##### Returns

- A [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the specified page token is empty, or max results value is invalid. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |       If an error occurs while retrieving provider config data.        |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|

#### public ApiFuture\<[ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>\>
**listSamlProviderConfigsAsync**
(String pageToken)

Similar to [listSamlProviderConfigs(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listSamlProviderConfigs(java.lang.String)) but performs the operation asynchronously.
Page size is limited to 100 provider configs.  

##### Parameters

| pageToken | A non-empty page token string, or null to retrieve the first page of provider configs. |
|-----------|----------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance. If an error occurs while retrieving provider config data, the future throws an exception.  

##### Throws

| IllegalArgumentException | If the specified page token is empty. |
|--------------------------|---------------------------------------|

#### public ApiFuture\<[ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>\>
**listSamlProviderConfigsAsync**
(String pageToken, int maxResults)

Similar to [listSamlProviderConfigs(String, int)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listSamlProviderConfigs(java.lang.String, int)) but performs the operation
asynchronously.  

##### Parameters

| pageToken  |    A non-empty page token string, or null to retrieve the first page of provider configs.    |
| maxResults | Maximum number of provider configs to include in the returned page. This may not exceed 100. |
|------------|----------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance. If an error occurs while retrieving provider config data, the future throws an exception.  

##### Throws

| IllegalArgumentException | If the specified page token is empty, or max results value is invalid. |
|--------------------------|------------------------------------------------------------------------|

#### public [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)
**listUsers**
(String pageToken, int maxResults)

Gets a page of users starting from the specified `pageToken`.  

##### Parameters

| pageToken  |    A non-empty page token string, or null to retrieve the first page of users.     |
| maxResults | Maximum number of users to include in the returned page. This may not exceed 1000. |
|------------|------------------------------------------------------------------------------------|

##### Returns

- A [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the specified page token is empty, or max results value is invalid. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |             If an error occurs while retrieving user data.             |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|

#### public [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)
**listUsers**
(String pageToken)

Gets a page of users starting from the specified `pageToken`. Page size is limited to
1000 users.  

##### Parameters

| pageToken | A non-empty page token string, or null to retrieve the first page of users. |
|-----------|-----------------------------------------------------------------------------|

##### Returns

- A [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         |     If the specified page token is empty.      |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while retrieving user data. |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|

#### public ApiFuture\<[ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)\>
**listUsersAsync**
(String pageToken, int maxResults)

Similar to [listUsers(String, int)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listUsers(java.lang.String, int)) but performs the operation asynchronously.  

##### Parameters

| pageToken  |    A non-empty page token string, or null to retrieve the first page of users.     |
| maxResults | Maximum number of users to include in the returned page. This may not exceed 1000. |
|------------|------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage) instance. If an error occurs while retrieving user data, the future throws an exception.  

##### Throws

| IllegalArgumentException | If the specified page token is empty, or max results value is invalid. |
|--------------------------|------------------------------------------------------------------------|

#### public ApiFuture\<[ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)\>
**listUsersAsync**
(String pageToken)

Similar to [listUsers(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#listUsers(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| pageToken | A non-empty page token string, or null to retrieve the first page of users. |
|-----------|-----------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage) instance. If an error occurs while retrieving user data, the future throws an exception.  

##### Throws

| IllegalArgumentException | If the specified page token is empty. |
|--------------------------|---------------------------------------|

#### public void
**revokeRefreshTokens**
(String uid)

Revokes all refresh tokens for the specified user.

Updates the user's tokensValidAfterTimestamp to the current UTC time expressed in
milliseconds since the epoch and truncated to 1 second accuracy. It is important that the
server on which this is called has its clock set correctly and synchronized.

While this will revoke all sessions for a specified user and disable any new ID tokens for
existing sessions from getting minted, existing ID tokens may remain active until their natural
expiration (one hour). To verify that ID tokens are revoked, use [verifyIdTokenAsync(String, boolean)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdTokenAsync(java.lang.String, boolean)).  

##### Parameters

| uid | The user id for which tokens are revoked. |
|-----|-------------------------------------------|

##### Throws

|                                                        IllegalArgumentException                                                         |     If the user ID is null or empty.      |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while revoking tokens. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|

#### public ApiFuture\<Void\>
**revokeRefreshTokensAsync**
(String uid)

Similar to [revokeRefreshTokens(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#revokeRefreshTokens(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| uid | The user id for which tokens are revoked. |
|-----|-------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully or fail with a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) in the event of an error.  

##### Throws

| IllegalArgumentException | If the user ID is null or empty. |
|--------------------------|----------------------------------|

#### public void
**setCustomClaims**
(String uid, Map\<String, Object\> claims)


**This method is deprecated.**   
Use [setCustomUserClaims(String, Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#setCustomUserClaims(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>)) instead.

<br />

##### Throws

| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |   |
|-----------------------------------------------------------------------------------------------------------------------------------------|---|

#### public void
**setCustomUserClaims**
(String uid, Map\<String, Object\> claims)

Sets the specified custom claims on an existing user account. A null claims value removes any
claims currently set on the user account. The claims should serialize into a valid JSON string.
The serialized claims must not be larger than 1000 characters.  

##### Parameters

|  uid   |        A user ID string.        |
| claims | A map of custom claims or null. |
|--------|---------------------------------|

##### Throws

| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                    If an error occurs while updating custom claims.                    |
|                                                        IllegalArgumentException                                                         | If the user ID string is null or empty, or the claims payload is invalid or too large. |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|

#### public ApiFuture\<Void\>
**setCustomUserClaimsAsync**
(String uid, Map\<String, Object\> claims)

Similar to [setCustomUserClaims(String, Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#setCustomUserClaims(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>)) but performs the operation asynchronously.  

##### Parameters

|  uid   |        A user ID string.        |
| claims | A map of custom claims or null. |
|--------|---------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully when the user account has been updated. If an error occurs while deleting the user account, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the user ID string is null or empty. |
|--------------------------|-----------------------------------------|

#### public [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)
**updateOidcProviderConfig**
([OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) request)

Updates an existing OpenID Connect auth provider config with the attributes contained in the
specified [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest).  

##### Parameters

| request | A non-null [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) instance. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) instance corresponding to the updated provider config.  

##### Throws

|                                                          NullPointerException                                                           |        if the provided update request is null.         |
|                                                        IllegalArgumentException                                                         |       If the provided update request is invalid.       |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | if an error occurs while updating the provider config. |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|

#### public ApiFuture\<[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig)\>
**updateOidcProviderConfigAsync**
([OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) request)

Similar to [updateOidcProviderConfig(OidcProviderConfig.UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateOidcProviderConfig(com.google.firebase.auth.OidcProviderConfig.UpdateRequest)) but performs the operation asynchronously.  

##### Parameters

| request | A non-null [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) instance. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) instance corresponding to the updated provider config. If an error occurs while updating the provider config, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

|   NullPointerException   |  if the provided update request is null.   |
| IllegalArgumentException | If the provided update request is invalid. |
|--------------------------|--------------------------------------------|

#### public [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)
**updateSamlProviderConfig**
([SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) request)

Updates an existing SAML Auth provider config with the attributes contained in the specified
[SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest).  

##### Parameters

| request | A non-null [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) instance. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) instance corresponding to the updated provider config.  

##### Throws

|                                                          NullPointerException                                                           |        if the provided update request is null.         |
|                                                        IllegalArgumentException                                                         |       If the provided update request is invalid.       |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | if an error occurs while updating the provider config. |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|

#### public ApiFuture\<[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig)\>
**updateSamlProviderConfigAsync**
([SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) request)

Similar to [updateSamlProviderConfig(SamlProviderConfig.UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateSamlProviderConfig(com.google.firebase.auth.SamlProviderConfig.UpdateRequest)) but performs the operation asynchronously.  

##### Parameters

| request | A non-null [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) instance. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) instance corresponding to the updated provider config. If an error occurs while updating the provider config, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

|   NullPointerException   |  if the provided update request is null.   |
| IllegalArgumentException | If the provided update request is invalid. |
|--------------------------|--------------------------------------------|

#### public [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)
**updateUser**
([UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) request)

Updates an existing user account with the attributes contained in the specified [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest).  

##### Parameters

| request | A non-null [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) instance. |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance corresponding to the updated user account.  

##### Throws

|                                                          NullPointerException                                                           |       if the provided update request is null.       |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | if an error occurs while updating the user account. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|

#### public ApiFuture\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>
**updateUserAsync**
([UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) request)

Similar to [updateUser(UserRecord.UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateUser(com.google.firebase.auth.UserRecord.UpdateRequest)) but performs the operation asynchronously.  

##### Parameters

| request | A non-null [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) instance. |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) instance corresponding to the updated user account. If an error occurs while updating the user account, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

#### public [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)
**verifyIdToken**
(String idToken, boolean checkRevoked)

Parses and verifies a Firebase ID Token.

A Firebase application can identify itself to a trusted backend server by sending its
Firebase ID Token (accessible via the `getToken` API in the Firebase Authentication
client) with its requests. The backend server can then use the `verifyIdToken()` method
to verify that the token is valid. This method ensures that the token is correctly signed, has
not expired, and it was issued to the Firebase project associated with this [FirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuth) instance.

If `checkRevoked` is set to true, this method performs an additional check to see if
the ID token has been revoked since it was issues. This requires making an additional remote
API call.  

##### Parameters

|   idToken    |                      A Firebase ID token string to parse and verify.                       |
| checkRevoked | A boolean denoting whether to check if the tokens were revoked or if the user is disabled. |
|--------------|--------------------------------------------------------------------------------------------|

##### Returns

- A [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken) representing the verified and decoded token.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the token is null, empty, or if the [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) instance does not have a project ID associated with it. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                                                             If an error occurs while parsing or validating the token, or if the user is disabled.                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)
**verifyIdToken**
(String idToken)

Parses and verifies a Firebase ID Token.

A Firebase application can identify itself to a trusted backend server by sending its
Firebase ID Token (accessible via the `getToken` API in the Firebase Authentication
client) with its requests. The backend server can then use the `verifyIdToken()` method
to verify that the token is valid. This method ensures that the token is correctly signed, has
not expired, and it was issued to the Firebase project associated with this [FirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuth) instance.

This method does not check whether a token has been revoked. Use [verifyIdToken(String, boolean)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdToken(java.lang.String, boolean)) to perform an additional revocation check.  

##### Parameters

| idToken | A Firebase ID token string to parse and verify. |
|---------|-------------------------------------------------|

##### Returns

- A [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken) representing the verified and decoded token.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the token is null, empty, or if the [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) instance does not have a project ID associated with it. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |                                                                           If an error occurs while parsing or validating the token.                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public ApiFuture\<[FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)\>
**verifyIdTokenAsync**
(String idToken)

Similar to [verifyIdToken(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdToken(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| idToken | A Firebase ID Token to verify and parse. |
|---------|------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the parsed token, or unsuccessfully with a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the token is null, empty, or if the [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) instance does not have a project ID associated with it. |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public ApiFuture\<[FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)\>
**verifyIdTokenAsync**
(String idToken, boolean checkRevoked)

Similar to [verifyIdToken(String, boolean)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifyIdToken(java.lang.String, boolean)) but performs the operation asynchronously.  

##### Parameters

|   idToken    |            A Firebase ID Token to verify and parse.             |
| checkRevoked | A boolean denoting whether to check if the tokens were revoked. |
|--------------|-----------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the parsed token, or unsuccessfully with a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the token is null, empty, or if the [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) instance does not have a project ID associated with it. |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)
**verifySessionCookie**
(String cookie, boolean checkRevoked)

Parses and verifies a Firebase session cookie.

If `checkRevoked` is true, additionally verifies that the cookie has not been revoked.

If verified successfully, returns a parsed version of the cookie from which the UID and the
other claims can be read. If the cookie is invalid or has been revoked while `checkRevoked` is true, throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Parameters

|    cookie    |                         A Firebase session cookie string to verify and parse.                          |
| checkRevoked | A boolean indicating whether to check if the cookie was explicitly revoked or if the user is disabled. |
|--------------|--------------------------------------------------------------------------------------------------------|

##### Returns

- A [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken) representing the verified and decoded cookie.  

##### Throws

| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while parsing or validating the token, or if the user is disabled. |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|

#### public [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)
**verifySessionCookie**
(String cookie)

Parses and verifies a Firebase session cookie.

If verified successfully, returns a parsed version of the cookie from which the UID and the
other claims can be read. If the cookie is invalid, throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).

This method does not check whether the cookie has been revoked. See [verifySessionCookie(String, boolean)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookie(java.lang.String, boolean)).  

##### Parameters

| cookie | A Firebase session cookie string to verify and parse. |
|--------|-------------------------------------------------------|

##### Returns

- A [FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken) representing the verified and decoded cookie.  

##### Throws

| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |   |
|-----------------------------------------------------------------------------------------------------------------------------------------|---|

#### public ApiFuture\<[FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)\>
**verifySessionCookieAsync**
(String cookie, boolean checkRevoked)

Similar to [verifySessionCookie(String, boolean)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookie(java.lang.String, boolean)) but performs the operation
asynchronously.  

##### Parameters

|    cookie    |            A Firebase session cookie string to verify and parse.            |
| checkRevoked | A boolean indicating whether to check if the cookie was explicitly revoked. |
|--------------|-----------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the parsed cookie, or unsuccessfully with the failure Exception.  

#### public ApiFuture\<[FirebaseToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseToken)\>
**verifySessionCookieAsync**
(String cookie)

Similar to [verifySessionCookie(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#verifySessionCookie(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| cookie | A Firebase session cookie string to verify and parse. |
|--------|-------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with the parsed cookie, or unsuccessfully with the failure Exception.

## Protected Methods

#### protected static T
**populateBuilderFromApp**
([Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder)\<T\> builder, [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app, String tenantId)

<br />