# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth.md.txt

# FirebaseAdmin.Auth.AbstractFirebaseAuth Class Reference

# FirebaseAdmin.Auth.AbstractFirebaseAuth

Exposes Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) operations that are available in both tenant-aware and tenant-unaware contexts.

## Summary

### Inheritance

Inherits from: FirebaseAdmin.IFirebaseService  
Direct Known Subclasses:[FirebaseAdmin.Auth.FirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth), [FirebaseAdmin.Auth.Multitenancy.TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-aware-firebase-auth)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CreateCustomTokenAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a55552c2470c8625f61ea186c42dcbe56)`(string uid)`                                                                                                                                                                                                                                                                                                                                                                                                                                    | `async Task< string >` Creates a Firebase custom token for the given user ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [CreateCustomTokenAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1ab3ad6f4edbffeaf35f5e3dc203da9e12)`(string uid, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                               | `async Task< string >` Creates a Firebase custom token for the given user ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [CreateCustomTokenAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a3ce3aa1db4285b00678d8e53be25f36f)`(string uid, IDictionary< string, object > developerClaims)`                                                                                                                                                                                                                                                                                                                                                                                     | `async Task< string >` Creates a Firebase custom token for the given user ID containing the specified additional claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [CreateCustomTokenAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1aa92bd3877ff53667f6a3f9b9b591ee9b)`(string uid, IDictionary< string, object > developerClaims, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                | `async Task< string >` Creates a Firebase custom token for the given user ID containing the specified additional claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [CreateProviderConfigAsync< T >](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1acbee0f2181488cb4793bf9657259b5da)`(AuthProviderConfigArgs< T > args)`                                                                                                                                                                                                                                                                                                                                                                                                      | `async Task< T >` Creates a new auth provider configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [CreateProviderConfigAsync< T >](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1aa017b0e29bb2ebbe7fc94fab057d11bf)`(AuthProviderConfigArgs< T > args, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                 | `async Task< T >` Creates a new auth provider configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [CreateUserAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a1d76d0fa59f9a921499713fa31701222)`(`[UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args)` args)`                                                                                                                                                                                                                                                                       | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Creates a new user account with the attributes contained in the specified [UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args).                                                                                                                                                                         |
| [CreateUserAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a598943fc4397cfd51f0c963de5518743)`(`[UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args)` args, CancellationToken cancellationToken)`                                                                                                                                                                                                                                  | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Creates a new user account with the attributes contained in the specified [UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args).                                                                                                                                                                         |
| [DeleteProviderConfigAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1aa4e8cdb39fd938a4beac6268e271b99d)`(string providerId)`                                                                                                                                                                                                                                                                                                                                                                                                                          | `async Task` Deletes the specified auth provider configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [DeleteProviderConfigAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a9d23801ac8527bfed7bb61ae2eb10e6e)`(string providerId, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                     | `async Task` Deletes the specified auth provider configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [DeleteUserAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a5b5a0e644ed722c88334b00d39aaffe1)`(string uid)`                                                                                                                                                                                                                                                                                                                                                                                                                                           | `async Task` Deletes the user identified by the specified *uid* .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [DeleteUserAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a082d31ce74d51a5c02651fff4d57dff6)`(string uid, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                                      | `async Task` Deletes the user identified by the specified *uid* .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [DeleteUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1ac72ec9a481f6b48f4edb884fdc8097c8)`(IReadOnlyList< string > uids)`                                                                                                                                                                                                                                                                                                                                                                                                                        | `async Task< `[DeleteUsersResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/delete-users-result#class_firebase_admin_1_1_auth_1_1_delete_users_result)` >` Deletes the users specified by the given identifiers.                                                                                                                                                                                                                                                                                                                                               |
| [DeleteUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a21de74fb3a4546e7515107cceee7092e)`(IReadOnlyList< string > uids, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                   | `async Task< `[DeleteUsersResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/delete-users-result#class_firebase_admin_1_1_auth_1_1_delete_users_result)` >` Deletes the users specified by the given identifiers.                                                                                                                                                                                                                                                                                                                                               |
| [GenerateEmailVerificationLinkAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a79818a31ca6d3de66a1a482d54260f42)`(string email)`                                                                                                                                                                                                                                                                                                                                                                                                                      | `async Task< string >` Generates the out-of-band email action link for email verification flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [GenerateEmailVerificationLinkAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1adbd80905db20add8c968c0a9b483b205)`(string email, `[ActionCodeSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings)` settings)`                                                                                                                                                                                                                      | `async Task< string >` Generates the out-of-band email action link for email verification flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [GenerateEmailVerificationLinkAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1abaa9680f6e41f1b76ff80bd0e0deb41d)`(string email, `[ActionCodeSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings)` settings, CancellationToken cancellationToken)`                                                                                                                                                                                 | `async Task< string >` Generates the out-of-band email action link for email verification flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [GeneratePasswordResetLinkAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a64c59fa408389e06bc026e5e0bf4e7d9)`(string email)`                                                                                                                                                                                                                                                                                                                                                                                                                          | `async Task< string >` Generates the out-of-band email action link for password reset flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [GeneratePasswordResetLinkAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1ac43e2d6e0944af61ab212bf64e865a29)`(string email, `[ActionCodeSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings)` settings)`                                                                                                                                                                                                                          | `async Task< string >` Generates the out-of-band email action link for password reset flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [GeneratePasswordResetLinkAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a48ff8e3d88cf90186c891e3286b275b5)`(string email, `[ActionCodeSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings)` settings, CancellationToken cancellationToken)`                                                                                                                                                                                     | `async Task< string >` Generates the out-of-band email action link for password reset flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [GenerateSignInWithEmailLinkAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a6f18ee67e5dfcb781516655be1819551)`(string email, `[ActionCodeSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings)` settings)`                                                                                                                                                                                                                        | `async Task< string >` Generates the out-of-band email action link for email link sign-in flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [GenerateSignInWithEmailLinkAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a63e332dd9149190054a819a6b7c6817a)`(string email, `[ActionCodeSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings)` settings, CancellationToken cancellationToken)`                                                                                                                                                                                   | `async Task< string >` Generates the out-of-band email action link for email link sign-in flows for the specified email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [GetOidcProviderConfigAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a155053cdcbdf3d9b937c96a1177206c7)`(string providerId)`                                                                                                                                                                                                                                                                                                                                                                                                                         | `async Task< `[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config)` >` Looks up an OIDC auth provider configuration by the provided ID.                                                                                                                                                                                                                                                                                                         |
| [GetOidcProviderConfigAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a677f77b5f2254d18f4273bef27fa55d6)`(string providerId, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                    | `async Task< `[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config)` >` Looks up an OIDC auth provider configuration by the provided ID.                                                                                                                                                                                                                                                                                                         |
| [GetSamlProviderConfigAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1adf37e54df49161ec945b5ca810ca0dbe)`(string providerId)`                                                                                                                                                                                                                                                                                                                                                                                                                         | `async Task< `[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config)` >` Looks up a SAML auth provider configuration by the provided ID.                                                                                                                                                                                                                                                                                                          |
| [GetSamlProviderConfigAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a853c4f3502b9eab0e48a80e3f2a4439b)`(string providerId, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                    | `async Task< `[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config)` >` Looks up a SAML auth provider configuration by the provided ID.                                                                                                                                                                                                                                                                                                          |
| [GetUserAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a044b68e9a16d03909d27f5ecb956e32c)`(string uid)`                                                                                                                                                                                                                                                                                                                                                                                                                                              | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user who's user ID was specified in *uid* .                                                                                                                                                                       |
| [GetUserAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a153dc9189b32ee3a92d61069ceabe393)`(string uid, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                                         | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user who's user ID was specified in *uid* .                                                                                                                                                                       |
| [GetUserByEmailAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a03b7591c213a420f5330aebcc15425c2)`(string email)`                                                                                                                                                                                                                                                                                                                                                                                                                                     | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user identified by *email* .                                                                                                                                                                                      |
| [GetUserByEmailAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a18f8a1bbca0f1ea392f03ab5ed838bd2)`(string email, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                                | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user identified by *email* .                                                                                                                                                                                      |
| [GetUserByPhoneNumberAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a97b1cdcfbe86d129f5e341b46423b40d)`(string phoneNumber)`                                                                                                                                                                                                                                                                                                                                                                                                                         | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user identified by *phoneNumber* .                                                                                                                                                                                |
| [GetUserByPhoneNumberAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a7f8d8c487e11e5126e23933907c79145)`(string phoneNumber, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                    | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user identified by *phoneNumber* .                                                                                                                                                                                |
| [GetUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a6e428036889c462a9b0f08bc72a985f2)`(IReadOnlyCollection< `[UserIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-identifier#class_firebase_admin_1_1_auth_1_1_user_identifier)` > identifiers)`                                                                                                                                                                                                                                             | `async Task< `[GetUsersResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/get-users-result#class_firebase_admin_1_1_auth_1_1_get_users_result)` >` Gets the user data corresponding to the specified identifiers.                                                                                                                                                                                                                                                                                                                                               |
| [GetUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a9d0b27144228fd67d7c77372592c1da5)`(IReadOnlyCollection< `[UserIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-identifier#class_firebase_admin_1_1_auth_1_1_user_identifier)` > identifiers, CancellationToken cancellationToken)`                                                                                                                                                                                                        | `async Task< `[GetUsersResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/get-users-result#class_firebase_admin_1_1_auth_1_1_get_users_result)` >` Gets the user data corresponding to the specified identifiers.                                                                                                                                                                                                                                                                                                                                               |
| [ImportUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a0c827bb70808807d470f463e7badec98)`(IEnumerable< `[ImportUserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args)` > users)`                                                                                                                                                                                                                                  | `async Task< `[UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result)` >` Imports the provided list of users into Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth).                                                                                                                                                                                                                      |
| [ImportUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a5e6bf3f0a0a7c4bb2befdc92b8ce812e)`(IEnumerable< `[ImportUserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args)` > users, CancellationToken cancellationToken)`                                                                                                                                                                                             | `async Task< `[UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result)` >` Imports the provided list of users into Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth).                                                                                                                                                                                                                      |
| [ImportUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a11f8b424b8919391ee61d0536eb81cc2)`(IEnumerable< `[ImportUserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args)` > users, `[UserImportOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-options#class_firebase_admin_1_1_auth_1_1_user_import_options)` options)`                                      | `async Task< `[UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result)` >` Imports the provided list of users into Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth).                                                                                                                                                                                                                      |
| [ImportUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a2d2af62643dac04e92b18e0d0bf9209e)`(IEnumerable< `[ImportUserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args)` > users, `[UserImportOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-options#class_firebase_admin_1_1_auth_1_1_user_import_options)` options, CancellationToken cancellationToken)` | `async Task< `[UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result)` >` Imports the provided list of users into Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth).                                                                                                                                                                                                                      |
| [ListOidcProviderConfigsAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1aac16647326c0764f00c26a3379119156)`(`[ListProviderConfigsOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/list-provider-configs-options#class_firebase_admin_1_1_auth_1_1_providers_1_1_list_provider_configs_options)` options)`                                                                                                                                                                                         | `PagedAsyncEnumerable< AuthProviderConfigs< `[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config)` >, `[OidcProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config)` >` Gets an async enumerable to iterate or page through OIDC provider configurations starting from the specified page token. |
| [ListSamlProviderConfigsAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1adf0fb6adbdccd1f46d6f3d24da258d23)`(`[ListProviderConfigsOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/list-provider-configs-options#class_firebase_admin_1_1_auth_1_1_providers_1_1_list_provider_configs_options)` options)`                                                                                                                                                                                         | `PagedAsyncEnumerable< AuthProviderConfigs< `[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config)` >, `[SamlProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config)` >` Gets an async enumerable to iterate or page through SAML provider configurations starting from the specified page token. |
| [ListUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a13c65216fc17ea092225befa7fff4015)`(`[ListUsersOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/list-users-options#class_firebase_admin_1_1_auth_1_1_list_users_options)` options)`                                                                                                                                                                                                                                                               | `PagedAsyncEnumerable< `[ExportedUserRecords](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-records#class_firebase_admin_1_1_auth_1_1_exported_user_records)`, `[ExportedUserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-record#class_firebase_admin_1_1_auth_1_1_exported_user_record)` >` Gets an async enumerable to iterate or page through users starting from the specified page token.                                                                                            |
| [RevokeRefreshTokensAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a9e5b0df42082cba9e7981e40a5bd1d5a)`(string uid)`                                                                                                                                                                                                                                                                                                                                                                                                                                  | `async Task` Revokes all refresh tokens for the specified user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [RevokeRefreshTokensAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1ae9a2e8cb374b1ff76ab5ddf58a5bb1ed)`(string uid, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                             | `async Task` Revokes all refresh tokens for the specified user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [SetCustomUserClaimsAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a5feacd2d2251b4a9d9023c9ab7a18553)`(string uid, IReadOnlyDictionary< string, object > claims)`                                                                                                                                                                                                                                                                                                                                                                                    | `async Task` Sets the specified custom claims on an existing user account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [SetCustomUserClaimsAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a33bada99cbfbdb414540612e0e194f39)`(string uid, IReadOnlyDictionary< string, object > claims, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                               | `async Task` Sets the specified custom claims on an existing user account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [UpdateProviderConfigAsync< T >](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a1e2957499d06c0a63adce21d0476e370)`(AuthProviderConfigArgs< T > args)`                                                                                                                                                                                                                                                                                                                                                                                                      | `async Task< T >` Updates an existing auth provider configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [UpdateProviderConfigAsync< T >](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a81a3ae5bed9ee72a4df7f61874c3a7d4)`(AuthProviderConfigArgs< T > args, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                 | `async Task< T >` Updates an existing auth provider configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [UpdateUserAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a6d60a81e27ccce97a9f144a6cac7b22f)`(`[UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args)` args)`                                                                                                                                                                                                                                                                       | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Updates an existing user account with the attributes contained in the specified [UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args).                                                                                                                                                                   |
| [UpdateUserAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1adecd11dfaadfb83f709f1b7c855e3d0e)`(`[UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args)` args, CancellationToken cancellationToken)`                                                                                                                                                                                                                                  | `async Task< `[UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record)` >` Updates an existing user account with the attributes contained in the specified [UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args).                                                                                                                                                                   |
| [VerifyIdTokenAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a57e0a8e549cd252cb78257c9d5e5c0cc)`(string idToken)`                                                                                                                                                                                                                                                                                                                                                                                                                                    | `async Task< `[FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token)` >` Parses and verifies a Firebase ID token.                                                                                                                                                                                                                                                                                                                                                                          |
| [VerifyIdTokenAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1ae94c03540450b3215fa9359944b70f0e)`(string idToken, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                                               | `async Task< `[FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token)` >` Parses and verifies a Firebase ID token.                                                                                                                                                                                                                                                                                                                                                                          |
| [VerifyIdTokenAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a9cf8c3671140f2d4ef8e7199c3b5dd63)`(string idToken, bool checkRevoked)`                                                                                                                                                                                                                                                                                                                                                                                                                 | `async Task< `[FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token)` >` Parses and verifies a Firebase ID token.                                                                                                                                                                                                                                                                                                                                                                          |
| [VerifyIdTokenAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a2f90aa3d7adf444cc0cc90e5215f2e62)`(string idToken, bool checkRevoked, CancellationToken cancellationToken)`                                                                                                                                                                                                                                                                                                                                                                            | `async Task< `[FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token)` >` Parses and verifies a Firebase ID token.                                                                                                                                                                                                                                                                                                                                                                          |

|                                                                                                                                                                                                                     ### Protected functions                                                                                                                                                                                                                     ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| [IfNotDeleted< TResult >](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a68b0137ad162fb6a95b1328a3c423bf1)`(Func< TResult > func)`                                                                                                                                                                                   | `TResult`            |
| [IsRevokedAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a2fb06ab00ab47147c87a38cff74d8fb7)`(`[FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token)` token, CancellationToken cancellationToken)` | `async Task< bool >` |

## Public functions

### CreateCustomTokenAsync

```text
async Task< string > CreateCustomTokenAsync(
  string uid
)
```  
Creates a Firebase custom token for the given user ID.

This token can then be sent back to a client application to be used with the [signInWithCustomToken](https://firebase.google.com/docs/auth/admin/create-custom-tokens#sign_in_using_custom_tokens_on_clients) authentication API.

This method attempts to generate a token using:

1. the private key of [FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app)'s service account credentials, if provided at initialization.
2. the IAM service if a service accound ID was specified via [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options)
3. the local metadata server if the code is deployed in a GCP-managed environment.

<br />

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentException`         | If *uid* is null, empty or longer than 128 characters.                                                                                                                                                                             | | `InvalidOperationException` | If no service account can be discovered from either the [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options) or the deployment environment. | | `FirebaseAuthException`     | If an error occurs while creating a custom token.                                                                                                                                                                                  | |
| Parameters  | |-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `uid` | The UID to store in the token. This identifies the user to other Firebase services (Realtime Database, Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth), etc.). Must not be longer than 128 characters. |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Returns** | A task that completes with a Firebase custom token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### CreateCustomTokenAsync

```text
async Task< string > CreateCustomTokenAsync(
  string uid,
  CancellationToken cancellationToken
)
```  
Creates a Firebase custom token for the given user ID.

This token can then be sent back to a client application to be used with the [signInWithCustomToken](https://firebase.google.com/docs/auth/admin/create-custom-tokens#sign_in_using_custom_tokens_on_clients) authentication API.

This method attempts to generate a token using:

1. the private key of [FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app)'s service account credentials, if provided at initialization.
2. the IAM service if a service accound ID was specified via [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options)
3. the local metadata server if the code is deployed in a GCP-managed environment.

<br />

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentException`         | If *uid* is null, empty or longer than 128 characters.                                                                                                                                                                             | | `InvalidOperationException` | If no service account can be discovered from either the [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options) or the deployment environment. | | `FirebaseAuthException`     | If an error occurs while creating a custom token.                                                                                                                                                                                  | |
| Parameters  | |---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `uid`               | The UID to store in the token. This identifies the user to other Firebase services (Realtime Database, Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth), etc.). Must not be longer than 128 characters. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                                                                                                                     |                                                                                                       |
| **Returns** | A task that completes with a Firebase custom token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### CreateCustomTokenAsync

```text
async Task< string > CreateCustomTokenAsync(
  string uid,
  IDictionary< string, object > developerClaims
)
```  
Creates a Firebase custom token for the given user ID containing the specified additional claims.

This token can then be sent back to a client application to be used with the [signInWithCustomToken](https://firebase.google.com/docs/auth/admin/create-custom-tokens#sign_in_using_custom_tokens_on_clients) authentication API.

This method uses the same mechanisms as [CreateCustomTokenAsync(string)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a55552c2470c8625f61ea186c42dcbe56) to sign custom tokens.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentException`         | If *uid* is null, empty or longer than 128 characters. Or, if *developerClaims* contains any standard JWT claims.                                                                                                                  | | `InvalidOperationException` | If no service account can be discovered from either the [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options) or the deployment environment. | | `FirebaseAuthException`     | If an error occurs while creating a custom token.                                                                                                                                                                                  | |
| Parameters  | |-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `uid`             | The UID to store in the token. This identifies the user to other Firebase services (Realtime Database, Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth), etc.). Must not be longer than 128 characters. | | `developerClaims` | Additional claims to be stored in the token, and made available to Firebase security rules. These must be serializable to JSON, and must not contain any standard JWT claims.                                                                                                                   |                                                                                                             |
| **Returns** | A task that completes with a Firebase custom token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### CreateCustomTokenAsync

```text
async Task< string > CreateCustomTokenAsync(
  string uid,
  IDictionary< string, object > developerClaims,
  CancellationToken cancellationToken
)
```  
Creates a Firebase custom token for the given user ID containing the specified additional claims.

This token can then be sent back to a client application to be used with the [signInWithCustomToken](https://firebase.google.com/docs/auth/admin/create-custom-tokens#sign_in_using_custom_tokens_on_clients) authentication API.

This method uses the same mechanisms as [CreateCustomTokenAsync(string)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a55552c2470c8625f61ea186c42dcbe56) to sign custom tokens.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentException`         | If *uid* is null, empty or longer than 128 characters. Or, if *developerClaims* contains any standard JWT claims.                                                                                                                  | | `InvalidOperationException` | If no service account can be discovered from either the [AppOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options#class_firebase_admin_1_1_app_options) or the deployment environment. | | `FirebaseAuthException`     | If an error occurs while creating a custom token.                                                                                                                                                                                  |                                                                                                                                                                                                                     |
| Parameters  | |---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `uid`               | The UID to store in the token. This identifies the user to other Firebase services (Realtime Database, Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth), etc.). Must not be longer than 128 characters. | | `developerClaims`   | Additional claims to be stored in the token, and made available to Firebase security rules. These must be serializable to JSON, and must not contain any standard JWT claims.                                                                                                                   | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                                                                                                                     | |
| **Returns** | A task that completes with a Firebase custom token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### CreateProviderConfigAsync\< T \>

```text
async Task< T > CreateProviderConfigAsync< T >(
  AuthProviderConfigArgs< T > args
)
```  
Creates a new auth provider configuration.

<br />

|                                                                                                                                                                  Details                                                                                                                                                                  ||
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions          | |-------------------------|--------------------------------------------------------------------------| | `ArgumentException`     | If *args* is null or invalid.                                            | | `FirebaseAuthException` | If an unexpected error occurs while creating the provider configuration. | |
| Parameters          | |--------|---------------------------------------------------------| | `args` | Arguments that describe the new provider configuration. |                                                                                                                                                                            |
| Template Parameters | |-----|---------------------------------------| | `T` | Type of AuthProviderConfig to create. |                                                                                                                                                                                                                      |
| **Returns**         | A task that completes with an AuthProviderConfig.                                                                                                                                                                                                                                                                    |

### CreateProviderConfigAsync\< T \>

```text
async Task< T > CreateProviderConfigAsync< T >(
  AuthProviderConfigArgs< T > args,
  CancellationToken cancellationToken
)
```  
Creates a new auth provider configuration.

<br />

|                                                                                                                                                                  Details                                                                                                                                                                  ||
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions          | |-------------------------|--------------------------------------------------------------------------| | `ArgumentException`     | If *args* is null or invalid.                                            | | `FirebaseAuthException` | If an unexpected error occurs while creating the provider configuration. | |
| Parameters          | |---------------------|-------------------------------------------------------------| | `args`              | Arguments that describe the new provider configuration.     | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                    |
| Template Parameters | |-----|---------------------------------------| | `T` | Type of AuthProviderConfig to create. |                                                                                                                                                                                                                      |
| **Returns**         | A task that completes with an AuthProviderConfig.                                                                                                                                                                                                                                                                    |

### CreateUserAsync

```text
async Task< UserRecord > CreateUserAsync(
  UserRecordArgs args
)
```  
Creates a new user account with the attributes contained in the specified [UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args).

<br />

|                                                                                                                                                                       Details                                                                                                                                                                        ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|--------------------------------------------| | `args` | Attributes to add to the new user account. |                                                                                                                                                                                                                         |
| Exceptions  | |-------------------------|-----------------------------------------------------| | `ArgumentNullException` | If *args* is null.                                  | | `ArgumentException`     | If any of the values in *args* are invalid.         | | `FirebaseAuthException` | If an error occurs while creating the user account. | |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing the newly created user account.                                                                                                     |

### CreateUserAsync

```text
async Task< UserRecord > CreateUserAsync(
  UserRecordArgs args,
  CancellationToken cancellationToken
)
```  
Creates a new user account with the attributes contained in the specified [UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args).

<br />

|                                                                                                                                                                       Details                                                                                                                                                                        ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `args`              | Attributes to add to the new user account.                  | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                                       |
| Exceptions  | |-------------------------|-----------------------------------------------------| | `ArgumentNullException` | If *args* is null.                                  | | `ArgumentException`     | If any of the values in *args* are invalid.         | | `FirebaseAuthException` | If an error occurs while creating the user account. | |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing the newly created user account.                                                                                                     |

### DeleteProviderConfigAsync

```text
async Task DeleteProviderConfigAsync(
  string providerId
)
```  
Deletes the specified auth provider configuration.

<br />

|                                                                                                                                                                                          Details                                                                                                                                                                                           ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|---------------------------------------------------------------------------------------------| | `ArgumentException`     | If the provider ID is null, empty or does not contain either the `oidc.` or `saml.` prefix. | | `FirebaseAuthException` | If the specified provider config does not exist.                                            | |
| Parameters  | |--------------|---------------------------------------------| | `providerId` | ID of the provider configuration to delete. |                                                                                                                                                                                                                                                 |
| **Returns** | A task that completes when the provider configuration is deleted.                                                                                                                                                                                                                                                                                                             |

### DeleteProviderConfigAsync

```text
async Task DeleteProviderConfigAsync(
  string providerId,
  CancellationToken cancellationToken
)
```  
Deletes the specified auth provider configuration.

<br />

|                                                                                                                                                                                          Details                                                                                                                                                                                           ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|---------------------------------------------------------------------------------------------| | `ArgumentException`     | If the provider ID is null, empty or does not contain either the `oidc.` or `saml.` prefix. | | `FirebaseAuthException` | If the specified provider config does not exist.                                            | |
| Parameters  | |---------------------|-------------------------------------------------------------| | `providerId`        | ID of the provider configuration to delete.                 | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                                                                             |
| **Returns** | A task that completes when the provider configuration is deleted.                                                                                                                                                                                                                                                                                                             |

### DeleteUserAsync

```text
async Task DeleteUserAsync(
  string uid
)
```  
Deletes the user identified by the specified *uid* .

<br />

|                                                                                                                  Details                                                                                                                   ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|-------------------| | `uid` | A user ID string. |                                                                                                                                                                   |
| Exceptions  | |-------------------------|---------------------------------------------| | `ArgumentException`     | If the user ID argument is null or empty.   | | `FirebaseAuthException` | If an error occurs while deleting the user. | |
| **Returns** | A task that completes when the user account has been deleted.                                                                                                                                                                 |

### DeleteUserAsync

```text
async Task DeleteUserAsync(
  string uid,
  CancellationToken cancellationToken
)
```  
Deletes the user identified by the specified *uid* .

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `uid`               | A user ID string.                                           | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| Exceptions  | |-------------------------|---------------------------------------------| | `ArgumentException`     | If the user ID argument is null or empty.   | | `FirebaseAuthException` | If an error occurs while deleting the user. |                                     |
| **Returns** | A task that completes when the user account has been deleted.                                                                                                                                                                                                     |

### DeleteUsersAsync

```text
async Task< DeleteUsersResult > DeleteUsersAsync(
  IReadOnlyList< string > uids
)
```  
Deletes the users specified by the given identifiers.

Deleting a non-existing user won't generate an error. (i.e. this method is idempotent.) Non-existing users will be considered to be successfully deleted, and will therefore be counted in the `DeleteUserResult.SuccessCount` value.

A maximum of 1000 identifiers may be supplied. If more than 1000 identifiers are specified, this method throws an `ArgumentException`.

This API is currently rate limited at the server to 1 QPS. If you exceed this, you may get a quota exceeded error. Therefore, if you want to delete more than 1000 users, you may need to add a delay to ensure you don't go over this limit.

<br />

|                                                                                                                   Details                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|-----------------------------------------------------------------------| | `uids` | The uids of the users to be deleted. Must have 1000 or fewer entries. |                                                           |
| Exceptions  | |---------------------|---------------------------------------------------------------------------------------| | `ArgumentException` | If any of the identifiers are invalid or if more than 1000 identifiers are specified. | |
| **Returns** | A task that resolves to the total number of successful/failed deletions, as well as the array of errors that correspond to the failed deletions.                                                                                |

### DeleteUsersAsync

```text
async Task< DeleteUsersResult > DeleteUsersAsync(
  IReadOnlyList< string > uids,
  CancellationToken cancellationToken
)
```  
Deletes the users specified by the given identifiers.

Deleting a non-existing user won't generate an error. (i.e. this method is idempotent.) Non-existing users will be considered to be successfully deleted, and will therefore be counted in the `DeleteUserResult.SuccessCount` value.

A maximum of 1000 identifiers may be supplied. If more than 1000 identifiers are specified, this method throws an `ArgumentException`.

This API is currently rate limited at the server to 1 QPS. If you exceed this, you may get a quota exceeded error. Therefore, if you want to delete more than 1000 users, you may need to add a delay to ensure you don't go over this limit.

<br />

|                                                                                                                                                   Details                                                                                                                                                    ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-----------------------------------------------------------------------| | `uids`              | The uids of the users to be deleted. Must have 1000 or fewer entries. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.           | |
| Exceptions  | |---------------------|---------------------------------------------------------------------------------------| | `ArgumentException` | If any of the identifiers are invalid or if more than 1000 identifiers are specified. |                                                                 |
| **Returns** | A task that resolves to the total number of successful/failed deletions, as well as the array of errors that correspond to the failed deletions.                                                                                                                                                |

### GenerateEmailVerificationLinkAsync

```text
async Task< string > GenerateEmailVerificationLinkAsync(
  string email
)
```  
Generates the out-of-band email action link for email verification flows for the specified email address.

<br />

|                                                                               Details                                                                                ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-----------------------------------------------| | `FirebaseAuthException` | If an error occurs while generating the link. | |
| Parameters  | |---------|---------------------------------------| | `email` | The email of the user to be verified. |                                                 |
| **Returns** | A task that completes with the email verification link.                                                                                                 |

### GenerateEmailVerificationLinkAsync

```text
async Task< string > GenerateEmailVerificationLinkAsync(
  string email,
  ActionCodeSettings settings
)
```  
Generates the out-of-band email action link for email verification flows for the specified email address.

<br />

|                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-----------------------------------------------| | `FirebaseAuthException` | If an error occurs while generating the link. |                                                                                                                                                                                                                                                                                                                                                                                                     |
| Parameters  | |------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `email`    | The email of the user to be verifed.                                                                                                                               | | `settings` | The action code settings object that defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. | |
| **Returns** | A task that completes with the email verification link.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### GenerateEmailVerificationLinkAsync

```text
async Task< string > GenerateEmailVerificationLinkAsync(
  string email,
  ActionCodeSettings settings,
  CancellationToken cancellationToken
)
```  
Generates the out-of-band email action link for email verification flows for the specified email address.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-----------------------------------------------| | `FirebaseAuthException` | If an error occurs while generating the link. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `email`             | The email of the user to be verified.                                                                                                                              | | `settings`          | The action code settings object that defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                        | |
| **Returns** | A task that completes with the email verification reset link.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### GeneratePasswordResetLinkAsync

```text
async Task< string > GeneratePasswordResetLinkAsync(
  string email
)
```  
Generates the out-of-band email action link for password reset flows for the specified email address.

<br />

|                                                                                 Details                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-------------------------------------------------| | `FirebaseAuthException` | If an error occurs while setting custom claims. | |
| Parameters  | |---------|------------------------------------------------------| | `email` | The email of the user whose password is to be reset. |                       |
| **Returns** | A task that completes with the password reset link.                                                                                                         |

### GeneratePasswordResetLinkAsync

```text
async Task< string > GeneratePasswordResetLinkAsync(
  string email,
  ActionCodeSettings settings
)
```  
Generates the out-of-band email action link for password reset flows for the specified email address.

<br />

|                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-------------------------------------------------| | `FirebaseAuthException` | If an error occurs while setting custom claims. |                                                                                                                                                                                                                                                                                                                                                                                                 |
| Parameters  | |------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `email`    | The email of the user whose password is to be reset.                                                                                                               | | `settings` | The action code settings object that defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. | |
| **Returns** | A task that completes with the password reset link.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### GeneratePasswordResetLinkAsync

```text
async Task< string > GeneratePasswordResetLinkAsync(
  string email,
  ActionCodeSettings settings,
  CancellationToken cancellationToken
)
```  
Generates the out-of-band email action link for password reset flows for the specified email address.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-------------------------------------------------| | `FirebaseAuthException` | If an error occurs while setting custom claims. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `email`             | The email of the user whose password is to be reset.                                                                                                               | | `settings`          | The action code settings object that defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                        | |
| **Returns** | A task that completes with the password reset link.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### GenerateSignInWithEmailLinkAsync

```text
async Task< string > GenerateSignInWithEmailLinkAsync(
  string email,
  ActionCodeSettings settings
)
```  
Generates the out-of-band email action link for email link sign-in flows for the specified email address.

<br />

|                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-----------------------------------------------| | `FirebaseAuthException` | If an error occurs while generating the link. |                                                                                                                                                                                                                                                                                                                                                                                                     |
| Parameters  | |------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `email`    | The email of the user signing in.                                                                                                                                  | | `settings` | The action code settings object that defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. | |
| **Returns** | A task that completes with the email sign in link.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### GenerateSignInWithEmailLinkAsync

```text
async Task< string > GenerateSignInWithEmailLinkAsync(
  string email,
  ActionCodeSettings settings,
  CancellationToken cancellationToken
)
```  
Generates the out-of-band email action link for email link sign-in flows for the specified email address.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-----------------------------------------------| | `FirebaseAuthException` | If an error occurs while generating the link. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `email`             | The email of the user signing in.                                                                                                                                  | | `settings`          | The action code settings object that defines whether the link is to be handled by a mobile app and the additional state information to be passed in the deep link. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                        | |
| **Returns** | A task that completes with the email sign in link.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### GetOidcProviderConfigAsync

```text
async Task< OidcProviderConfig > GetOidcProviderConfigAsync(
  string providerId
)
```  
Looks up an OIDC auth provider configuration by the provided ID.

<br />

|                                                                                                                                                               Details                                                                                                                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|---------------------------------------------------------------------------| | `ArgumentException`     | If the provider ID is null, empty or does not contain the `oidc.` prefix. | | `FirebaseAuthException` | If the specified provider config does not exist.                          | |
| Parameters  | |--------------|-----------------------------------------------| | `providerId` | The ID of the OIDC provider config to return. |                                                                                                                                                                                       |
| **Returns** | A task that completes with a OidcProviderConfig.                                                                                                                                                                                                                                                                        |

### GetOidcProviderConfigAsync

```text
async Task< OidcProviderConfig > GetOidcProviderConfigAsync(
  string providerId,
  CancellationToken cancellationToken
)
```  
Looks up an OIDC auth provider configuration by the provided ID.

<br />

|                                                                                                                                                               Details                                                                                                                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|---------------------------------------------------------------------------| | `ArgumentException`     | If the provider ID is null, empty or does not contain the `oidc.` prefix. | | `FirebaseAuthException` | If the specified provider config does not exist.                          | |
| Parameters  | |---------------------|-------------------------------------------------------------| | `providerId`        | The ID of the OIDC provider config to return.               | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                       |
| **Returns** | A task that completes with a OidcProviderConfig.                                                                                                                                                                                                                                                                        |

### GetSamlProviderConfigAsync

```text
async Task< SamlProviderConfig > GetSamlProviderConfigAsync(
  string providerId
)
```  
Looks up a SAML auth provider configuration by the provided ID.

<br />

|                                                                                                                                                               Details                                                                                                                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|---------------------------------------------------------------------------| | `ArgumentException`     | If the provider ID is null, empty or does not contain the `saml.` prefix. | | `FirebaseAuthException` | If the specified provider config does not exist.                          | |
| Parameters  | |--------------|-----------------------------------------------| | `providerId` | The ID of the SAML provider config to return. |                                                                                                                                                                                       |
| **Returns** | A task that completes with a SamlProviderConfig.                                                                                                                                                                                                                                                                        |

### GetSamlProviderConfigAsync

```text
async Task< SamlProviderConfig > GetSamlProviderConfigAsync(
  string providerId,
  CancellationToken cancellationToken
)
```  
Looks up a SAML auth provider configuration by the provided ID.

<br />

|                                                                                                                                                               Details                                                                                                                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|---------------------------------------------------------------------------| | `ArgumentException`     | If the provider ID is null, empty or does not contain the `saml.` prefix. | | `FirebaseAuthException` | If the specified provider config does not exist.                          | |
| Parameters  | |---------------------|-------------------------------------------------------------| | `providerId`        | The ID of the SAML provider config to return.               | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                       |
| **Returns** | A task that completes with a SamlProviderConfig.                                                                                                                                                                                                                                                                        |

### GetUserAsync

```text
async Task< UserRecord > GetUserAsync(
  string uid
)
```  
Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user who's user ID was specified in *uid* .

<br />

|                                                                                                                                 Details                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------------------------------| | `uid` | The user ID for the user who's data is to be retrieved. |                                                                                                                     |
| Exceptions  | |-------------------------|-------------------------------------------------------| | `ArgumentException`     | If user ID argument is null or empty.                 | | `FirebaseAuthException` | If a user cannot be found with the specified user ID. | |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing a user with the specified user ID.                      |

### GetUserAsync

```text
async Task< UserRecord > GetUserAsync(
  string uid,
  CancellationToken cancellationToken
)
```  
Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user who's user ID was specified in *uid* .

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `uid`               | The user ID for the user who's data is to be retrieved.     | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| Exceptions  | |-------------------------|-------------------------------------------------------| | `ArgumentException`     | If user ID argument is null or empty.                 | | `FirebaseAuthException` | If a user cannot be found with the specified user ID. |       |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing a user with the specified user ID.                            |

### GetUserByEmailAsync

```text
async Task< UserRecord > GetUserByEmailAsync(
  string email
)
```  
Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user identified by *email* .

<br />

|                                                                                                                              Details                                                                                                                               ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------| | `email` | The email of the user who's data is to be retrieved. |                                                                                                                 |
| Exceptions  | |-------------------------|-----------------------------------------------------| | `ArgumentException`     | If the email argument is null or empty.             | | `FirebaseAuthException` | If a user cannot be found with the specified email. | |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing a user with the specified email.                  |

### GetUserByEmailAsync

```text
async Task< UserRecord > GetUserByEmailAsync(
  string email,
  CancellationToken cancellationToken
)
```  
Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user identified by *email* .

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `email`             | The email of the user who's data is to be retrieved.        | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| Exceptions  | |-------------------------|-----------------------------------------------------| | `ArgumentException`     | If the email argument is null or empty.             | | `FirebaseAuthException` | If a user cannot be found with the specified email. |             |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing a user with the specified email.                              |

### GetUserByPhoneNumberAsync

```text
async Task< UserRecord > GetUserByPhoneNumberAsync(
  string phoneNumber
)
```  
Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user identified by *phoneNumber* .

<br />

|                                                                                                                                         Details                                                                                                                                         ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|-------------------------------------------------------------| | `phoneNumber` | The phone number of the user who's data is to be retrieved. |                                                                                                            |
| Exceptions  | |-------------------------|------------------------------------------------------------| | `ArgumentException`     | If the phone number argument is null or empty.             | | `FirebaseAuthException` | If a user cannot be found with the specified phone number. | |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing a user with the specified phone number.                                |

### GetUserByPhoneNumberAsync

```text
async Task< UserRecord > GetUserByPhoneNumberAsync(
  string phoneNumber,
  CancellationToken cancellationToken
)
```  
Gets a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) object containing information about the user identified by *phoneNumber* .

<br />

|                                                                                                                                         Details                                                                                                                                         ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `phoneNumber`       | The phone number of the user who's data is to be retrieved. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |          |
| Exceptions  | |-------------------------|------------------------------------------------------------| | `ArgumentException`     | If the phone number argument is null or empty.             | | `FirebaseAuthException` | If a user cannot be found with the specified phone number. | |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing a user with the specified phone number.                                |

### GetUsersAsync

```text
async Task< GetUsersResult > GetUsersAsync(
  IReadOnlyCollection< UserIdentifier > identifiers
)
```  
Gets the user data corresponding to the specified identifiers.

There are no ordering guarantees; in particular, the nth entry in the users result list is not guaranteed to correspond to the nth entry in the input parameters list.

A maximum of 100 identifiers may be supplied. If more than 100 identifiers are specified, this method throws an `ArgumentException`.

<br />

|                                                                                                                               Details                                                                                                                                ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|---------------------------------------------------------------------------------------------------------| | `identifiers` | The identifiers used to indicate which user records should be returned. Must have 100 entries or fewer. | |
| Exceptions  | |---------------------|--------------------------------------------------------------------------------------| | `ArgumentException` | If any of the identifiers are invalid or if more than 100 identifiers are specified. |                           |
| **Returns** | A task that resolves to the corresponding user records.                                                                                                                                                                                                 |

### GetUsersAsync

```text
async Task< GetUsersResult > GetUsersAsync(
  IReadOnlyCollection< UserIdentifier > identifiers,
  CancellationToken cancellationToken
)
```  
Gets the user data corresponding to the specified identifiers.

There are no ordering guarantees; in particular, the nth entry in the users result list is not guaranteed to correspond to the nth entry in the input parameters list.

A maximum of 100 identifiers may be supplied. If more than 100 identifiers are specified, this method throws an `ArgumentException`.

<br />

|                                                                                                                                                                                                      Details                                                                                                                                                                                                       ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|---------------------------------------------------------------------------------------------------------| | `identifiers`       | The identifiers used to indicate which user records should be returned. Must have 100 entries or fewer. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                             | |
| Exceptions  | |---------------------|--------------------------------------------------------------------------------------| | `ArgumentException` | If any of the identifiers are invalid or if more than 100 identifiers are specified. |                                                                                                                                                                         |
| **Returns** | A task that resolves to the corresponding user records.                                                                                                                                                                                                                                                                                                                                               |

### ImportUsersAsync

```text
async Task< UserImportResult > ImportUsersAsync(
  IEnumerable< ImportUserRecordArgs > users
)
```  
Imports the provided list of users into Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth).

You can import a maximum of 1000 users at a time. This operation is optimized for bulk imports and does not check identifier uniqueness, which could result in duplications.

[UserImportOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-options#class_firebase_admin_1_1_auth_1_1_user_import_options) is required to import users with passwords. See [FirebaseAuth.ImportUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a0c827bb70808807d470f463e7badec98).

<br />

|                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------| | `users` | A non-empty list of users to be imported. Length must not exceed 1000. |                                                                                                                                                                                                                                                                                                                                                           |
| Exceptions  | |-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentException`     | If the users list is null, empty or has more than 1000 elements. Or if at least one user specifies a password, with no hashing algorithm set. | | `FirebaseAuthException` | If an error occurs while importing users.                                                                                                     | |
| **Returns** | A [UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result) instance.                                                                                                                                                                                                                                                                                                                                           |

### ImportUsersAsync

```text
async Task< UserImportResult > ImportUsersAsync(
  IEnumerable< ImportUserRecordArgs > users,
  CancellationToken cancellationToken
)
```  
Imports the provided list of users into Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth).

You can import a maximum of 1000 users at a time. This operation is optimized for bulk imports and does not check identifier uniqueness, which could result in duplications.

[UserImportOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-options#class_firebase_admin_1_1_auth_1_1_user_import_options) is required to import users with passwords. See [FirebaseAuth.ImportUsersAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth#class_firebase_admin_1_1_auth_1_1_abstract_firebase_auth_1a0c827bb70808807d470f463e7badec98).

<br />

|                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|------------------------------------------------------------------------| | `users`             | A non-empty list of users to be imported. Length must not exceed 1000. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.            |                                                                                                                                                                                                                                  |
| Exceptions  | |-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentException`     | If the users list is null, empty or has more than 1000 elements. Or if at least one user specifies a password, with no hashing algorithm set. | | `FirebaseAuthException` | If an error occurs while importing users.                                                                                                     | |
| **Returns** | A [UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result) instance.                                                                                                                                                                                                                                                                                                                                           |

### ImportUsersAsync

```text
async Task< UserImportResult > ImportUsersAsync(
  IEnumerable< ImportUserRecordArgs > users,
  UserImportOptions options
)
```  
Imports the provided list of users into Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth).

You can import a maximum of 1000 users at a time. This operation is optimized for bulk imports and does not check identifier uniqueness, which could result in duplications.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                        Details                                                                                                                                                                                                                                                                                                                                                                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `users`   | A non-empty list of users to be imported. Length must not exceed 1000.                                                                                                                                                                             | | `options` | A [UserImportOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-options#class_firebase_admin_1_1_auth_1_1_user_import_options) instance or null. Required when importing users with passwords. | |
| Exceptions  | |-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentException`     | If the users list is null, empty or has more than 1000 elements. Or if at least one user specifies a password, with no hashing algorithm set. | | `FirebaseAuthException` | If an error occurs while importing users.                                                                                                     |                                                                                                                                                                                                                                                                      |
| **Returns** | A [UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result) instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### ImportUsersAsync

```text
async Task< UserImportResult > ImportUsersAsync(
  IEnumerable< ImportUserRecordArgs > users,
  UserImportOptions options,
  CancellationToken cancellationToken
)
```  
Imports the provided list of users into Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth).

You can import a maximum of 1000 users at a time. This operation is optimized for bulk imports and does not check identifier uniqueness, which could result in duplications.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `users`             | A non-empty list of users to be imported. Length must not exceed 1000.                                                                                                                                                                             | | `options`           | A [UserImportOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-options#class_firebase_admin_1_1_auth_1_1_user_import_options) instance or null. Required when importing users with passwords. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                                                                        | |
| Exceptions  | |-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentException`     | If the users list is null, empty or has more than 1000 elements. Or if at least one user specifies a password, with no hashing algorithm set. | | `FirebaseAuthException` | If an error occurs while importing users.                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Returns** | A [UserImportResult](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-result#class_firebase_admin_1_1_auth_1_1_user_import_result) instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### ListOidcProviderConfigsAsync

```text
PagedAsyncEnumerable< AuthProviderConfigs< OidcProviderConfig >, OidcProviderConfig > ListOidcProviderConfigsAsync(
  ListProviderConfigsOptions options
)
```  
Gets an async enumerable to iterate or page through OIDC provider configurations starting from the specified page token.

If the page token is null or unspecified, iteration starts from the first page. See [Page Streaming](https://googleapis.github.io/google-cloud-dotnet/docs/guides/page-streaming.html) for more details on how to use this API.

<br />

|                                                                                                                                        Details                                                                                                                                         ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|----------------------------------------------------------------------------------------------------------------------| | `options` | The options to control the starting point and page size. Pass null to list from the beginning with default settings. | |
| **Returns** | A PagedAsyncEnumerable{AuthProviderConfigs, OidcProviderConfig} instance.                                                                                                                                                                                                 |

### ListSamlProviderConfigsAsync

```text
PagedAsyncEnumerable< AuthProviderConfigs< SamlProviderConfig >, SamlProviderConfig > ListSamlProviderConfigsAsync(
  ListProviderConfigsOptions options
)
```  
Gets an async enumerable to iterate or page through SAML provider configurations starting from the specified page token.

If the page token is null or unspecified, iteration starts from the first page. See [Page Streaming](https://googleapis.github.io/google-cloud-dotnet/docs/guides/page-streaming.html) for more details on how to use this API.

<br />

|                                                                                                                                        Details                                                                                                                                         ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|----------------------------------------------------------------------------------------------------------------------| | `options` | The options to control the starting point and page size. Pass null to list from the beginning with default settings. | |
| **Returns** | A PagedAsyncEnumerable{AuthProviderConfigs, SamlProviderConfig} instance.                                                                                                                                                                                                 |

### ListUsersAsync

```text
PagedAsyncEnumerable< ExportedUserRecords, ExportedUserRecord > ListUsersAsync(
  ListUsersOptions options
)
```  
Gets an async enumerable to iterate or page through users starting from the specified page token.

If the page token is null or unspecified, iteration starts from the first page. See [Page Streaming](https://googleapis.github.io/google-cloud-dotnet/docs/guides/page-streaming.html) for more details on how to use this API.

<br />

|                                                                                                                                        Details                                                                                                                                         ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|----------------------------------------------------------------------------------------------------------------------| | `options` | The options to control the starting point and page size. Pass null to list from the beginning with default settings. | |
| **Returns** | A PagedAsyncEnumerable{ExportedUserRecords, ExportedUserRecord} instance.                                                                                                                                                                                                 |

### RevokeRefreshTokensAsync

```text
async Task RevokeRefreshTokensAsync(
  string uid
)
```  
Revokes all refresh tokens for the specified user.

Updates the user's `tokensValidAfterTimestamp` to the current UTC time expressed in seconds since the epoch and truncated to 1 second accuracy. It is important that the server on which this is called has its clock set correctly and synchronized.

While this will revoke all sessions for a specified user and disable any new ID tokens for existing sessions from getting minted, existing ID tokens may remain active until their natural expiration (one hour).

<br />

|                                                                                                                     Details                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|-------------------| | `uid` | A user ID string. |                                                                                                                                                                         |
| Exceptions  | |-------------------------|-----------------------------------------------| | `ArgumentException`     | If the user ID argument is null or empty.     | | `FirebaseAuthException` | If an error occurs while revoking the tokens. | |
| **Returns** | A task that completes when the user's refresh tokens have been revoked.                                                                                                                                                             |

### RevokeRefreshTokensAsync

```text
async Task RevokeRefreshTokensAsync(
  string uid,
  CancellationToken cancellationToken
)
```  
Revokes all refresh tokens for the specified user.

Updates the user's `tokensValidAfterTimestamp` to the current UTC time expressed in seconds since the epoch and truncated to 1 second accuracy. It is important that the server on which this is called has its clock set correctly and synchronized.

While this will revoke all sessions for a specified user and disable any new ID tokens for existing sessions from getting minted, existing ID tokens may remain active until their natural expiration (one hour).

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `uid`               | A user ID string.                                           | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| Exceptions  | |-------------------------|-----------------------------------------------| | `ArgumentException`     | If the user ID argument is null or empty.     | | `FirebaseAuthException` | If an error occurs while revoking the tokens. |                               |
| **Returns** | A task that completes when the user's refresh tokens have been revoked.                                                                                                                                                                                           |

### SetCustomUserClaimsAsync

```text
async Task SetCustomUserClaimsAsync(
  string uid,
  IReadOnlyDictionary< string, object > claims
)
```  
Sets the specified custom claims on an existing user account.

A null claims value removes any claims currently set on the user account. The claims must serialize into a valid JSON string. The serialized claims must not be larger than 1000 characters.

<br />

|                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-----------------------------------------------------------------------------------------------------------------------| | `ArgumentException`     | If *uid* is null, empty or longer than 128 characters. Or, if the serialized *claims* is larger than 1000 characters. | | `FirebaseAuthException` | If an error occurs while setting custom claims.                                                                       |                                                                                                                                                                                                 |
| Parameters  | |----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `uid`    | The user ID string for the custom claims will be set. Must not be null or longer than 128 characters.                                                                                                | | `claims` | The claims to be stored on the user account, and made available to Firebase security rules. These must be serializable to JSON, and the serialized claims should not be larger than 1000 characters. | |
| **Returns** | A task that completes when the claims have been set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### SetCustomUserClaimsAsync

```text
async Task SetCustomUserClaimsAsync(
  string uid,
  IReadOnlyDictionary< string, object > claims,
  CancellationToken cancellationToken
)
```  
Sets the specified custom claims on an existing user account.

A null claims value removes any claims currently set on the user account. The claims should serialize into a valid JSON string. The serialized claims must not be larger than 1000 characters.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|-----------------------------------------------------------------------------------------------------------------------| | `ArgumentException`     | If *uid* is null, empty or longer than 128 characters. Or, if the serialized *claims* is larger than 1000 characters. | | `FirebaseAuthException` | If an error occurs while setting custom claims.                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Parameters  | |---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `uid`               | The user ID string for the custom claims will be set. Must not be null or longer than 128 characters.                                                                                                 | | `claims`            | The claims to be stored on the user account, and made available to Firebase security rules. These must be serializable to JSON, and after serialization it should not be larger than 1000 characters. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                           | |
| **Returns** | A task that completes when the claims have been set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### UpdateProviderConfigAsync\< T \>

```text
async Task< T > UpdateProviderConfigAsync< T >(
  AuthProviderConfigArgs< T > args
)
```  
Updates an existing auth provider configuration.

<br />

|                                                                                                                                                                                                                         Details                                                                                                                                                                                                                          ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions          | |-------------------------|---------------------------------------------------------------------------------------------------------------| | `ArgumentException`     | If *args* is null or invalid.                                                                                 | | `FirebaseAuthException` | If the specified provider config does not exist or if an unexpected error occurs while performing the update. | |
| Parameters          | |--------|---------------------------------------------------------| | `args` | Properties to be updated in the provider configuration. |                                                                                                                                                                                                                                                                                           |
| Template Parameters | |-----|---------------------------------------| | `T` | Type of AuthProviderConfig to update. |                                                                                                                                                                                                                                                                                                                                     |
| **Returns**         | A task that completes with the updated AuthProviderConfig.                                                                                                                                                                                                                                                                                                                                                                          |

### UpdateProviderConfigAsync\< T \>

```text
async Task< T > UpdateProviderConfigAsync< T >(
  AuthProviderConfigArgs< T > args,
  CancellationToken cancellationToken
)
```  
Updates an existing auth provider configuration.

<br />

|                                                                                                                                                                                                                         Details                                                                                                                                                                                                                          ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions          | |-------------------------|---------------------------------------------------------------------------------------------------------------| | `ArgumentException`     | If *args* is null or invalid.                                                                                 | | `FirebaseAuthException` | If the specified provider config does not exist or if an unexpected error occurs while performing the update. | |
| Parameters          | |---------------------|-------------------------------------------------------------| | `args`              | Properties to be updated in the provider configuration.     | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                                                                                                                                   |
| Template Parameters | |-----|---------------------------------------| | `T` | Type of AuthProviderConfig to update. |                                                                                                                                                                                                                                                                                                                                     |
| **Returns**         | A task that completes with the updated AuthProviderConfig.                                                                                                                                                                                                                                                                                                                                                                          |

### UpdateUserAsync

```text
async Task< UserRecord > UpdateUserAsync(
  UserRecordArgs args
)
```  
Updates an existing user account with the attributes contained in the specified [UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args).

The [UserRecordArgs.Uid](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args_1a9bdf5f5f65290dd168021d52b916d9d1) property must be specified.

<br />

|                                                                                                                                                                       Details                                                                                                                                                                        ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|---------------------------| | `args` | The attributes to update. |                                                                                                                                                                                                                                                           |
| Exceptions  | |-------------------------|-----------------------------------------------------| | `ArgumentNullException` | If *args* is null.                                  | | `ArgumentException`     | If any of the values in *args* are invalid.         | | `FirebaseAuthException` | If an error occurs while updating the user account. | |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing the updated user account.                                                                                                           |

### UpdateUserAsync

```text
async Task< UserRecord > UpdateUserAsync(
  UserRecordArgs args,
  CancellationToken cancellationToken
)
```  
Updates an existing user account with the attributes contained in the specified [UserRecordArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args).

The [UserRecordArgs.Uid](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record-args#class_firebase_admin_1_1_auth_1_1_user_record_args_1a9bdf5f5f65290dd168021d52b916d9d1) property must be specified.

<br />

|                                                                                                                                                                       Details                                                                                                                                                                        ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `args`              | The attributes to update.                                   | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                                       |
| Exceptions  | |-------------------------|-----------------------------------------------------| | `ArgumentNullException` | If *args* is null.                                  | | `ArgumentException`     | If any of the values in *args* are invalid.         | | `FirebaseAuthException` | If an error occurs while updating the user account. | |
| **Returns** | A task that completes with a [UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record) representing the updated user account.                                                                                                           |

### VerifyIdTokenAsync

```text
async Task< FirebaseToken > VerifyIdTokenAsync(
  string idToken
)
```  
Parses and verifies a Firebase ID token.

A Firebase client app can identify itself to a trusted backend server by sending its Firebase ID Token (accessible via the `getIdToken()` API in the Firebase client SDK) with its requests. The backend server can then use this method to verify that the token is valid. This method ensures that the token is correctly signed, has not expired, and it was issued against the Firebase project associated with this [FirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth) instance.

See [Verify ID Tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) for code samples and detailed documentation.

<br />

|                                                                                                                           Details                                                                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|----------------------------------------| | `ArgumentException`     | If ID token argument is null or empty. | | `FirebaseAuthException` | If the ID token fails to verify.       |                                  |
| Parameters  | |-----------|-------------------------------------------------| | `idToken` | A Firebase ID token string to parse and verify. |                                                                                                                 |
| **Returns** | A task that completes with a [FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token) representing the verified and decoded ID token. |

### VerifyIdTokenAsync

```text
async Task< FirebaseToken > VerifyIdTokenAsync(
  string idToken,
  CancellationToken cancellationToken
)
```  
Parses and verifies a Firebase ID token.

A Firebase client app can identify itself to a trusted backend server by sending its Firebase ID Token (accessible via the `getIdToken()` API in the Firebase client SDK) with its requests. The backend server can then use this method to verify that the token is valid. This method ensures that the token is correctly signed, has not expired, and it was issued against the Firebase project associated with this [FirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth) instance.

See [Verify ID Tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) for code samples and detailed documentation.

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|----------------------------------------| | `ArgumentException`     | If ID token argument is null or empty. | | `FirebaseAuthException` | If the ID token fails to verify.       |                                                    |
| Parameters  | |---------------------|-------------------------------------------------------------| | `idToken`           | A Firebase ID token string to parse and verify.             | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| **Returns** | A task that completes with a [FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token) representing the verified and decoded ID token.                   |

### VerifyIdTokenAsync

```text
async Task< FirebaseToken > VerifyIdTokenAsync(
  string idToken,
  bool checkRevoked
)
```  
Parses and verifies a Firebase ID token.

A Firebase client app can identify itself to a trusted backend server by sending its Firebase ID Token (accessible via the `getIdToken()` API in the Firebase client SDK) with its requests. The backend server can then use this method to verify that the token is valid. This method ensures that the token is correctly signed, has not expired, and it was issued against the Firebase project associated with this [FirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth) instance.

If `checkRevoked` is set to true, this method performs an additional check to see if the ID token has been revoked since it was issued. This requires making an additional remote API call.

See [Verify ID Tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) for code samples and detailed documentation.

<br />

|                                                                                                                                      Details                                                                                                                                      ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|----------------------------------------| | `ArgumentException`     | If ID token argument is null or empty. | | `FirebaseAuthException` | If the ID token fails to verify.       |                                                       |
| Parameters  | |----------------|-------------------------------------------------------------------| | `idToken`      | A Firebase ID token string to parse and verify.                   | | `checkRevoked` | A boolean indicating whether to check if the tokens were revoked. | |
| **Returns** | A task that completes with a [FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token) representing the verified and decoded ID token.                      |

### VerifyIdTokenAsync

```text
async Task< FirebaseToken > VerifyIdTokenAsync(
  string idToken,
  bool checkRevoked,
  CancellationToken cancellationToken
)
```  
Parses and verifies a Firebase ID token.

A Firebase client app can identify itself to a trusted backend server by sending its Firebase ID Token (accessible via the `getIdToken()` API in the Firebase client SDK) with its requests. The backend server can then use this method to verify that the token is valid. This method ensures that the token is correctly signed, has not expired, and it was issued against the Firebase project associated with this [FirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth) instance.

If `checkRevoked` is set to true, this method performs an additional check to see if the ID token has been revoked since it was issued. This requires making an additional remote API call.

See [Verify ID Tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) for code samples and detailed documentation.

<br />

|                                                                                                                                                                                           Details                                                                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |-------------------------|----------------------------------------| | `ArgumentException`     | If ID token argument is null or empty. | | `FirebaseAuthException` | If the ID token fails to verify.       |                                                                                                                                                                  |
| Parameters  | |---------------------|-------------------------------------------------------------------| | `idToken`           | A Firebase ID token string to parse and verify.                   | | `checkRevoked`      | A boolean indicating whether to check if the tokens were revoked. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.       | |
| **Returns** | A task that completes with a [FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token) representing the verified and decoded ID token.                                                                                                                                 |

## Protected functions

### IfNotDeleted\< TResult \>

```text
TResult IfNotDeleted< TResult >(
  Func< TResult > func
)
```  

### IsRevokedAsync

```text
async Task< bool > IsRevokedAsync(
  FirebaseToken token,
  CancellationToken cancellationToken
)
```