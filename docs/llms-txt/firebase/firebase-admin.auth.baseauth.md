# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md.txt

# BaseAuth class

Common parent interface for both `Auth` and `TenantAwareAuth` APIs.

**Signature:**  

    export declare abstract class BaseAuth 

## Methods

|                                                                                                 Method                                                                                                  | Modifiers |                                                                                                                                                                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [createCustomToken(uid, developerClaims)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthcreatecustomtoken)                                              |           | Creates a new Firebase custom token (JWT) that can be sent back to a client device to use to sign in with the client SDKs' `signInWithCustomToken()` methods. (Tenant-aware instances will also embed the tenant ID in the token.)See [Create Custom Tokens](https://firebase.google.com/docs/auth/admin/create-custom-tokens) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [createProviderConfig(config)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthcreateproviderconfig)                                                      |           | Returns a promise that resolves with the newly created `AuthProviderConfig` when the new provider configuration is created.SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [createSessionCookie(idToken, sessionCookieOptions)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthcreatesessioncookie)                                 |           | Creates a new Firebase session cookie with the specified options. The created JWT string can be set as a server-side session cookie with a custom cookie policy, and be used for session management. The session cookie JWT will have the same payload claims as the provided ID token.See [Manage Session Cookies](https://firebase.google.com/docs/auth/admin/manage-cookies) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                |
| [createUser(properties)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthcreateuser)                                                                      |           | Creates a new user.See [Create a user](https://firebase.google.com/docs/auth/admin/manage-users#create_a_user) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [deleteProviderConfig(providerId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthdeleteproviderconfig)                                                  |           | Deletes the provider configuration corresponding to the provider ID passed. If the specified ID does not exist, an `auth/configuration-not-found` error is thrown.SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [deleteUser(uid)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthdeleteuser)                                                                             |           | Deletes an existing user.See [Delete a user](https://firebase.google.com/docs/auth/admin/manage-users#delete_a_user) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [deleteUsers(uids)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthdeleteusers)                                                                          |           | Deletes the users specified by the given uids.Deleting a non-existing user won't generate an error (i.e. this method is idempotent.) Non-existing users are considered to be successfully deleted, and are therefore counted in the `DeleteUsersResult.successCount` value.Only a maximum of 1000 identifiers may be supplied. If more than 1000 identifiers are supplied, this method throws a FirebaseAuthError.This API is currently rate limited at the server to 1 QPS. If you exceed this, you may get a quota exceeded error. Therefore, if you want to delete more than 1000 users, you may need to add a delay to ensure you don't go over this limit.                                                                                                                                             |
| [generateEmailVerificationLink(email, actionCodeSettings)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgenerateemailverificationlink)                 |           | Generates the out of band email action link to verify the user's ownership of the specified email. The [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) object provided as an argument to this method defines whether the link is to be handled by a mobile app or browser along with additional state information to be passed in the deep link, etc.                                                                                                                                                                                                                                                                                                                                                    |
| [generatePasswordResetLink(email, actionCodeSettings)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgeneratepasswordresetlink)                         |           | Generates the out of band email action link to reset a user's password. The link is generated for the user with the specified email address. The optional [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) object defines whether the link is to be handled by a mobile app or browser and the additional state information to be passed in the deep link, etc.                                                                                                                                                                                                                                                                                                                                           |
| [generateSignInWithEmailLink(email, actionCodeSettings)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgeneratesigninwithemaillink)                     |           | Generates the out of band email action link to verify the user's ownership of the specified email. The [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) object provided as an argument to this method defines whether the link is to be handled by a mobile app or browser along with additional state information to be passed in the deep link, etc.                                                                                                                                                                                                                                                                                                                                                    |
| [generateVerifyAndChangeEmailLink(email, newEmail, actionCodeSettings)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgenerateverifyandchangeemaillink) |           | Generates an out-of-band email action link to verify the user's ownership of the specified email. The [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) object provided as an argument to this method defines whether the link is to be handled by a mobile app or browser along with additional state information to be passed in the deep link, etc.                                                                                                                                                                                                                                                                                                                                                     |
| [getProviderConfig(providerId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgetproviderconfig)                                                        |           | Looks up an Auth provider configuration by the provided ID. Returns a promise that resolves with the provider configuration corresponding to the provider ID specified. If the specified ID does not exist, an `auth/configuration-not-found` error is thrown.SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).                                                                                                                                                                                                                                                                                                                          |
| [getUser(uid)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgetuser)                                                                                   |           | Gets the user data for the user corresponding to a given `uid`.See [Retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [getUserByEmail(email)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgetuserbyemail)                                                                   |           | Gets the user data for the user corresponding to a given email.See [Retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [getUserByPhoneNumber(phoneNumber)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgetuserbyphonenumber)                                                 |           | Gets the user data for the user corresponding to a given phone number. The phone number has to conform to the E.164 specification.See [Retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [getUserByProviderUid(providerId, uid)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgetuserbyprovideruid)                                             |           | Gets the user data for the user corresponding to a given provider id.See [Retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [getUsers(identifiers)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthgetusers)                                                                         |           | Gets the user data corresponding to the specified identifiers.There are no ordering guarantees; in particular, the nth entry in the result list is not guaranteed to correspond to the nth entry in the input parameters list.Only a maximum of 100 identifiers may be supplied. If more than 100 identifiers are supplied, this method throws a FirebaseAuthError.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [importUsers(users, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthimportusers)                                                                |           | Imports the provided list of users into Firebase Auth. A maximum of 1000 users are allowed to be imported one at a time. When importing users with passwords, [UserImportOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportoptions.md#userimportoptions_interface) are required to be specified. This operation is optimized for bulk imports and will ignore checks on `uid`, `email` and other identifier uniqueness which could result in duplications.                                                                                                                                                                                                                                                                                                       |
| [listProviderConfigs(options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistproviderconfigs)                                                       |           | Returns the list of existing provider configurations matching the filter provided. At most, 100 provider configs can be listed at a time.SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [listUsers(maxResults, pageToken)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistusers)                                                             |           | Retrieves a list of users (single batch only) with a size of `maxResults` starting from the offset as specified by `pageToken`. This is used to retrieve all the users of a specified project in batches.See [List all users](https://firebase.google.com/docs/auth/admin/manage-users#list_all_users) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [revokeRefreshTokens(uid)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthrevokerefreshtokens)                                                           |           | Revokes all refresh tokens for an existing user.This API will update the user's [UserRecord.tokensValidAfterTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordtokensvalidaftertime) to the current UTC. It is important that the server on which this is called has its clock set correctly and synchronized.While this will revoke all sessions for a specified user and disable any new ID tokens for existing sessions from getting minted, existing ID tokens may remain active until their natural expiration (one hour). To verify that ID tokens are revoked, use [BaseAuth.verifyIdToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthverifyidtoken) where `checkRevoked` is set to true. |
| [setCustomUserClaims(uid, customUserClaims)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthsetcustomuserclaims)                                         |           | Sets additional developer claims on an existing user identified by the provided `uid`, typically used to define user roles and levels of access. These claims should propagate to all devices where the user is already signed in (after token expiration or when token refresh is forced) and the next time the user signs in. If a reserved OIDC claim name is used (sub, iat, iss, etc), an error is thrown. They are set on the authenticated user's ID token JWT.See [Defining user roles and access levels](https://firebase.google.com/docs/auth/admin/custom-claims) for code samples and detailed documentation.                                                                                                                                                                                   |
| [updateProviderConfig(providerId, updatedConfig)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthupdateproviderconfig)                                   |           | Returns a promise that resolves with the updated `AuthProviderConfig` corresponding to the provider ID specified. If the specified ID does not exist, an `auth/configuration-not-found` error is thrown.SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).                                                                                                                                                                                                                                                                                                                                                                                |
| [updateUser(uid, properties)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthupdateuser)                                                                 |           | Updates an existing user.See [Update a user](https://firebase.google.com/docs/auth/admin/manage-users#update_a_user) for code samples and detailed documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [verifyIdToken(idToken, checkRevoked)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthverifyidtoken)                                                     |           | Verifies a Firebase ID token (JWT). If the token is valid, the promise is fulfilled with the token's decoded claims; otherwise, the promise is rejected.If `checkRevoked` is set to true, first verifies whether the corresponding user is disabled. If yes, an `auth/user-disabled` error is thrown. If no, verifies if the session corresponding to the ID token was revoked. If the corresponding user's session was invalidated, an `auth/id-token-revoked` error is thrown. If not specified the check is not applied.See [Verify ID Tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) for code samples and detailed documentation.                                                                                                                                                |
| [verifySessionCookie(sessionCookie, checkRevoked)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthverifysessioncookie)                                   |           | Verifies a Firebase session cookie. Returns a Promise with the cookie claims. Rejects the promise if the cookie could not be verified.If `checkRevoked` is set to true, first verifies whether the corresponding user is disabled: If yes, an `auth/user-disabled` error is thrown. If no, verifies if the session corresponding to the session cookie was revoked. If the corresponding user's session was invalidated, an `auth/session-cookie-revoked` error is thrown. If not specified the check is not performed.See [Verify Session Cookies](https://firebase.google.com/docs/auth/admin/manage-cookies#verify_session_cookie_and_check_permissions) for code samples and detailed documentation                                                                                                     |

## BaseAuth.createCustomToken()

Creates a new Firebase custom token (JWT) that can be sent back to a client device to use to sign in with the client SDKs' `signInWithCustomToken()` methods. (Tenant-aware instances will also embed the tenant ID in the token.)

See [Create Custom Tokens](https://firebase.google.com/docs/auth/admin/create-custom-tokens) for code samples and detailed documentation.

**Signature:**  

    createCustomToken(uid: string, developerClaims?: object): Promise<string>;

### Parameters

|    Parameter    |  Type  |                             Description                              |
|-----------------|--------|----------------------------------------------------------------------|
| uid             | string | The `uid` to use as the custom token's subject.                      |
| developerClaims | object | Optional additional claims to include in the custom token's payload. |

**Returns:**

Promise\<string\>

A promise fulfilled with a custom token for the provided `uid` and payload.

## BaseAuth.createProviderConfig()

Returns a promise that resolves with the newly created `AuthProviderConfig` when the new provider configuration is created.

SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

**Signature:**  

    createProviderConfig(config: AuthProviderConfig): Promise<AuthProviderConfig>;

### Parameters

| Parameter |                                                         Type                                                          |              Description              |
|-----------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| config    | [AuthProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#authproviderconfig) | The provider configuration to create. |

**Returns:**

Promise\<[AuthProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#authproviderconfig)\>

A promise that resolves with the created provider configuration.

## BaseAuth.createSessionCookie()

Creates a new Firebase session cookie with the specified options. The created JWT string can be set as a server-side session cookie with a custom cookie policy, and be used for session management. The session cookie JWT will have the same payload claims as the provided ID token.

See [Manage Session Cookies](https://firebase.google.com/docs/auth/admin/manage-cookies) for code samples and detailed documentation.

**Signature:**  

    createSessionCookie(idToken: string, sessionCookieOptions: SessionCookieOptions): Promise<string>;

### Parameters

|      Parameter       |                                                                           Type                                                                           |                            Description                             |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| idToken              | string                                                                                                                                                   | The Firebase ID token to exchange for a session cookie.            |
| sessionCookieOptions | [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.sessioncookieoptions.md#sessioncookieoptions_interface) | The session cookie options which includes custom session duration. |

**Returns:**

Promise\<string\>

A promise that resolves on success with the created session cookie.

## BaseAuth.createUser()

Creates a new user.

See [Create a user](https://firebase.google.com/docs/auth/admin/manage-users#create_a_user) for code samples and detailed documentation.

**Signature:**  

    createUser(properties: CreateRequest): Promise<UserRecord>;

### Parameters

| Parameter  |                                                                Type                                                                 |                         Description                         |
|------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| properties | [CreateRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createrequest.md#createrequest_interface) | The properties to set on the new user record to be created. |

**Returns:**

Promise\<[UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class)\>

A promise fulfilled with the user data corresponding to the newly created user.

## BaseAuth.deleteProviderConfig()

Deletes the provider configuration corresponding to the provider ID passed. If the specified ID does not exist, an `auth/configuration-not-found` error is thrown.

SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

**Signature:**  

    deleteProviderConfig(providerId: string): Promise<void>;

### Parameters

| Parameter  |  Type  |                           Description                           |
|------------|--------|-----------------------------------------------------------------|
| providerId | string | The provider ID corresponding to the provider config to delete. |

**Returns:**

Promise\<void\>

A promise that resolves on completion.

## BaseAuth.deleteUser()

Deletes an existing user.

See [Delete a user](https://firebase.google.com/docs/auth/admin/manage-users#delete_a_user) for code samples and detailed documentation.

**Signature:**  

    deleteUser(uid: string): Promise<void>;

### Parameters

| Parameter |  Type  |                  Description                   |
|-----------|--------|------------------------------------------------|
| uid       | string | The `uid` corresponding to the user to delete. |

**Returns:**

Promise\<void\>

An empty promise fulfilled once the user has been deleted.

## BaseAuth.deleteUsers()

Deletes the users specified by the given uids.

Deleting a non-existing user won't generate an error (i.e. this method is idempotent.) Non-existing users are considered to be successfully deleted, and are therefore counted in the `DeleteUsersResult.successCount` value.

Only a maximum of 1000 identifiers may be supplied. If more than 1000 identifiers are supplied, this method throws a FirebaseAuthError.

This API is currently rate limited at the server to 1 QPS. If you exceed this, you may get a quota exceeded error. Therefore, if you want to delete more than 1000 users, you may need to add a delay to ensure you don't go over this limit.

**Signature:**  

    deleteUsers(uids: string[]): Promise<DeleteUsersResult>;

### Parameters

| Parameter |    Type    |                   Description                    |
|-----------|------------|--------------------------------------------------|
| uids      | string\[\] | The `uids` corresponding to the users to delete. |

**Returns:**

Promise\<[DeleteUsersResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.deleteusersresult.md#deleteusersresult_interface)\>

A Promise that resolves to the total number of successful/failed deletions, as well as the array of errors that corresponds to the failed deletions.

## BaseAuth.generateEmailVerificationLink()

Generates the out of band email action link to verify the user's ownership of the specified email. The [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) object provided as an argument to this method defines whether the link is to be handled by a mobile app or browser along with additional state information to be passed in the deep link, etc.

**Signature:**  

    generateEmailVerificationLink(email: string, actionCodeSettings?: ActionCodeSettings): Promise<string>;

### Parameters

|     Parameter      |                                                                        Type                                                                        |                                                                                                                                                                                                                                                                                                                                                             Description                                                                                                                                                                                                                                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| email              | string                                                                                                                                             | The email account to verify.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| actionCodeSettings | [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) | The action code settings. If specified, the state/continue URL is set as the "continueUrl" parameter in the email verification link. The default email verification landing page will use this to display a link to go back to the app if it is installed. If the actionCodeSettings is not specified, no URL is appended to the action URL. The state URL provided must belong to a domain that is whitelisted by the developer in the console. Otherwise an error is thrown. Mobile app redirects are only applicable if the developer configures and accepts the Firebase Dynamic Links terms of service. The Android package name and iOS bundle ID are respected only if they are configured in the same Firebase Auth project. |

**Returns:**

Promise\<string\>

A promise that resolves with the generated link.

### Example

    var actionCodeSettings = {
      url: 'https://www.example.com/cart?email=user@example.com&cartId=123',
      iOS: {
        bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true,
      linkDomain: 'project-id.firebaseapp.com'
    };
    admin.auth()
        .generateEmailVerificationLink('user@example.com', actionCodeSettings)
        .then(function(link) {
          // The link was successfully generated.
        })
        .catch(function(error) {
          // Some error occurred, you can inspect the code: error.code
        });

## BaseAuth.generatePasswordResetLink()

Generates the out of band email action link to reset a user's password. The link is generated for the user with the specified email address. The optional [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) object defines whether the link is to be handled by a mobile app or browser and the additional state information to be passed in the deep link, etc.

**Signature:**  

    generatePasswordResetLink(email: string, actionCodeSettings?: ActionCodeSettings): Promise<string>;

### Parameters

|     Parameter      |                                                                        Type                                                                        |                                                                                                                                                                                                                                                                                                                                                         Description                                                                                                                                                                                                                                                                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| email              | string                                                                                                                                             | The email address of the user whose password is to be reset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| actionCodeSettings | [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) | The action code settings. If specified, the state/continue URL is set as the "continueUrl" parameter in the password reset link. The default password reset landing page will use this to display a link to go back to the app if it is installed. If the actionCodeSettings is not specified, no URL is appended to the action URL. The state URL provided must belong to a domain that is whitelisted by the developer in the console. Otherwise an error is thrown. Mobile app redirects are only applicable if the developer configures and accepts the Firebase Dynamic Links terms of service. The Android package name and iOS bundle ID are respected only if they are configured in the same Firebase Auth project. |

**Returns:**

Promise\<string\>

A promise that resolves with the generated link.

### Example

    var actionCodeSettings = {
      url: 'https://www.example.com/?email=user@example.com',
      iOS: {
        bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true,
      linkDomain: 'project-id.firebaseapp.com'
    };
    admin.auth()
        .generatePasswordResetLink('user@example.com', actionCodeSettings)
        .then(function(link) {
          // The link was successfully generated.
        })
        .catch(function(error) {
          // Some error occurred, you can inspect the code: error.code
        });

## BaseAuth.generateSignInWithEmailLink()

Generates the out of band email action link to verify the user's ownership of the specified email. The [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) object provided as an argument to this method defines whether the link is to be handled by a mobile app or browser along with additional state information to be passed in the deep link, etc.

**Signature:**  

    generateSignInWithEmailLink(email: string, actionCodeSettings: ActionCodeSettings): Promise<string>;

### Parameters

|     Parameter      |                                                                        Type                                                                        |                                                                                                                                                                                                                                                                                                                                                             Description                                                                                                                                                                                                                                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| email              | string                                                                                                                                             | The email account to verify.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| actionCodeSettings | [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) | The action code settings. If specified, the state/continue URL is set as the "continueUrl" parameter in the email verification link. The default email verification landing page will use this to display a link to go back to the app if it is installed. If the actionCodeSettings is not specified, no URL is appended to the action URL. The state URL provided must belong to a domain that is whitelisted by the developer in the console. Otherwise an error is thrown. Mobile app redirects are only applicable if the developer configures and accepts the Firebase Dynamic Links terms of service. The Android package name and iOS bundle ID are respected only if they are configured in the same Firebase Auth project. |

**Returns:**

Promise\<string\>

A promise that resolves with the generated link.

### Example

    var actionCodeSettings = {
      url: 'https://www.example.com/cart?email=user@example.com&cartId=123',
      iOS: {
        bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true,
      linkDomain: 'project-id.firebaseapp.com'
    };
    admin.auth()
        .generateEmailVerificationLink('user@example.com', actionCodeSettings)
        .then(function(link) {
          // The link was successfully generated.
        })
        .catch(function(error) {
          // Some error occurred, you can inspect the code: error.code
        });

## BaseAuth.generateVerifyAndChangeEmailLink()

Generates an out-of-band email action link to verify the user's ownership of the specified email. The [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) object provided as an argument to this method defines whether the link is to be handled by a mobile app or browser along with additional state information to be passed in the deep link, etc.

**Signature:**  

    generateVerifyAndChangeEmailLink(email: string, newEmail: string, actionCodeSettings?: ActionCodeSettings): Promise<string>;

### Parameters

|     Parameter      |                                                                        Type                                                                        |                                                                                                                                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                                                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| email              | string                                                                                                                                             | The current email account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| newEmail           | string                                                                                                                                             | The email address the account is being updated to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| actionCodeSettings | [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettings_interface) | The action code settings. If specified, the state/continue URL is set as the "continueUrl" parameter in the email verification link. The default email verification landing page will use this to display a link to go back to the app if it is installed. If the actionCodeSettings is not specified, no URL is appended to the action URL. The state URL provided must belong to a domain that is authorized in the console, or an error will be thrown. Mobile app redirects are only applicable if the developer configures and accepts the Firebase Dynamic Links terms of service. The Android package name and iOS bundle ID are respected only if they are configured in the same Firebase Auth project. |

**Returns:**

Promise\<string\>

A promise that resolves with the generated link.

## BaseAuth.getProviderConfig()

Looks up an Auth provider configuration by the provided ID. Returns a promise that resolves with the provider configuration corresponding to the provider ID specified. If the specified ID does not exist, an `auth/configuration-not-found` error is thrown.

SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

**Signature:**  

    getProviderConfig(providerId: string): Promise<AuthProviderConfig>;

### Parameters

| Parameter  |  Type  |                           Description                           |
|------------|--------|-----------------------------------------------------------------|
| providerId | string | The provider ID corresponding to the provider config to return. |

**Returns:**

Promise\<[AuthProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#authproviderconfig)\>

A promise that resolves with the configuration corresponding to the provided ID.

## BaseAuth.getUser()

Gets the user data for the user corresponding to a given `uid`.

See [Retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data) for code samples and detailed documentation.

**Signature:**  

    getUser(uid: string): Promise<UserRecord>;

### Parameters

| Parameter |  Type  |                       Description                        |
|-----------|--------|----------------------------------------------------------|
| uid       | string | The `uid` corresponding to the user whose data to fetch. |

**Returns:**

Promise\<[UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class)\>

A promise fulfilled with the user data corresponding to the provided `uid`.

## BaseAuth.getUserByEmail()

Gets the user data for the user corresponding to a given email.

See [Retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data) for code samples and detailed documentation.

**Signature:**  

    getUserByEmail(email: string): Promise<UserRecord>;

### Parameters

| Parameter |  Type  |                       Description                        |
|-----------|--------|----------------------------------------------------------|
| email     | string | The email corresponding to the user whose data to fetch. |

**Returns:**

Promise\<[UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class)\>

A promise fulfilled with the user data corresponding to the provided email.

## BaseAuth.getUserByPhoneNumber()

Gets the user data for the user corresponding to a given phone number. The phone number has to conform to the E.164 specification.

See [Retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data) for code samples and detailed documentation.

**Signature:**  

    getUserByPhoneNumber(phoneNumber: string): Promise<UserRecord>;

### Parameters

|  Parameter  |  Type  |                           Description                           |
|-------------|--------|-----------------------------------------------------------------|
| phoneNumber | string | The phone number corresponding to the user whose data to fetch. |

**Returns:**

Promise\<[UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class)\>

A promise fulfilled with the user data corresponding to the provided phone number.

## BaseAuth.getUserByProviderUid()

Gets the user data for the user corresponding to a given provider id.

See [Retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data) for code samples and detailed documentation.

**Signature:**  

    getUserByProviderUid(providerId: string, uid: string): Promise<UserRecord>;

### Parameters

| Parameter  |  Type  |                             Description                             |
|------------|--------|---------------------------------------------------------------------|
| providerId | string | The provider ID, for example, "google.com" for the Google provider. |
| uid        | string | The user identifier for the given provider.                         |

**Returns:**

Promise\<[UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class)\>

A promise fulfilled with the user data corresponding to the given provider id.

## BaseAuth.getUsers()

Gets the user data corresponding to the specified identifiers.

There are no ordering guarantees; in particular, the nth entry in the result list is not guaranteed to correspond to the nth entry in the input parameters list.

Only a maximum of 100 identifiers may be supplied. If more than 100 identifiers are supplied, this method throws a FirebaseAuthError.

**Signature:**  

    getUsers(identifiers: UserIdentifier[]): Promise<GetUsersResult>;

### Parameters

|  Parameter  |                                                       Type                                                        |                                                 Description                                                  |
|-------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| identifiers | [UserIdentifier](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#useridentifier)\[\] | The identifiers used to indicate which user records should be returned. Must not have more than 100 entries. |

**Returns:**

Promise\<[GetUsersResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.getusersresult.md#getusersresult_interface)\>

A promise that resolves to the corresponding user records.

### Exceptions

FirebaseAuthError If any of the identifiers are invalid or if more than 100 identifiers are specified.

## BaseAuth.importUsers()

Imports the provided list of users into Firebase Auth. A maximum of 1000 users are allowed to be imported one at a time. When importing users with passwords, [UserImportOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportoptions.md#userimportoptions_interface) are required to be specified. This operation is optimized for bulk imports and will ignore checks on `uid`, `email` and other identifier uniqueness which could result in duplications.

**Signature:**  

    importUsers(users: UserImportRecord[], options?: UserImportOptions): Promise<UserImportResult>;

### Parameters

| Parameter |                                                                       Type                                                                       |                                       Description                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| users     | [UserImportRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecord_interface)\[\] | The list of user records to import to Firebase Auth.                                    |
| options   | [UserImportOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportoptions.md#userimportoptions_interface)  | The user import options, required when the users provided include password credentials. |

**Returns:**

Promise\<[UserImportResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportresult.md#userimportresult_interface)\>

A promise that resolves when the operation completes with the result of the import. This includes the number of successful imports, the number of failed imports and their corresponding errors.

## BaseAuth.listProviderConfigs()

Returns the list of existing provider configurations matching the filter provided. At most, 100 provider configs can be listed at a time.

SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

**Signature:**  

    listProviderConfigs(options: AuthProviderConfigFilter): Promise<ListProviderConfigResults>;

### Parameters

| Parameter |                                                                                 Type                                                                                 |             Description              |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| options   | [AuthProviderConfigFilter](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfigfilter.md#authproviderconfigfilter_interface) | The provider config filter to apply. |

**Returns:**

Promise\<[ListProviderConfigResults](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listproviderconfigresults.md#listproviderconfigresults_interface)\>

A promise that resolves with the list of provider configs meeting the filter requirements.

## BaseAuth.listUsers()

Retrieves a list of users (single batch only) with a size of `maxResults` starting from the offset as specified by `pageToken`. This is used to retrieve all the users of a specified project in batches.

See [List all users](https://firebase.google.com/docs/auth/admin/manage-users#list_all_users) for code samples and detailed documentation.

**Signature:**  

    listUsers(maxResults?: number, pageToken?: string): Promise<ListUsersResult>;

### Parameters

| Parameter  |  Type  |                                    Description                                    |
|------------|--------|-----------------------------------------------------------------------------------|
| maxResults | number | The page size, 1000 if undefined. This is also the maximum allowed limit.         |
| pageToken  | string | The next page token. If not specified, returns users starting without any offset. |

**Returns:**

Promise\<[ListUsersResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listusersresult.md#listusersresult_interface)\>

A promise that resolves with the current batch of downloaded users and the next page token.

## BaseAuth.revokeRefreshTokens()

Revokes all refresh tokens for an existing user.

This API will update the user's [UserRecord.tokensValidAfterTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordtokensvalidaftertime) to the current UTC. It is important that the server on which this is called has its clock set correctly and synchronized.

While this will revoke all sessions for a specified user and disable any new ID tokens for existing sessions from getting minted, existing ID tokens may remain active until their natural expiration (one hour). To verify that ID tokens are revoked, use [BaseAuth.verifyIdToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthverifyidtoken) where `checkRevoked` is set to true.

**Signature:**  

    revokeRefreshTokens(uid: string): Promise<void>;

### Parameters

| Parameter |  Type  |                                 Description                                 |
|-----------|--------|-----------------------------------------------------------------------------|
| uid       | string | The `uid` corresponding to the user whose refresh tokens are to be revoked. |

**Returns:**

Promise\<void\>

An empty promise fulfilled once the user's refresh tokens have been revoked.

## BaseAuth.setCustomUserClaims()

Sets additional developer claims on an existing user identified by the provided `uid`, typically used to define user roles and levels of access. These claims should propagate to all devices where the user is already signed in (after token expiration or when token refresh is forced) and the next time the user signs in. If a reserved OIDC claim name is used (sub, iat, iss, etc), an error is thrown. They are set on the authenticated user's ID token JWT.

See [Defining user roles and access levels](https://firebase.google.com/docs/auth/admin/custom-claims) for code samples and detailed documentation.

**Signature:**  

    setCustomUserClaims(uid: string, customUserClaims: object | null): Promise<void>;

### Parameters

|    Parameter     |      Type      |                                                                                                                                                                             Description                                                                                                                                                                             |
|------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| uid              | string         | The `uid` of the user to edit.                                                                                                                                                                                                                                                                                                                                      |
| customUserClaims | object \| null | The developer claims to set. If null is passed, existing custom claims are deleted. Passing a custom claims payload larger than 1000 bytes will throw an error. Custom claims are added to the user's ID token which is transmitted on every authenticated request. For profile non-access related user attributes, use database or other separate storage systems. |

**Returns:**

Promise\<void\>

A promise that resolves when the operation completes successfully.

## BaseAuth.updateProviderConfig()

Returns a promise that resolves with the updated `AuthProviderConfig` corresponding to the provider ID specified. If the specified ID does not exist, an `auth/configuration-not-found` error is thrown.

SAML and OIDC provider support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

**Signature:**  

    updateProviderConfig(providerId: string, updatedConfig: UpdateAuthProviderRequest): Promise<AuthProviderConfig>;

### Parameters

|   Parameter   |                                                                Type                                                                 |                           Description                           |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| providerId    | string                                                                                                                              | The provider ID corresponding to the provider config to update. |
| updatedConfig | [UpdateAuthProviderRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#updateauthproviderrequest) | The updated configuration.                                      |

**Returns:**

Promise\<[AuthProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#authproviderconfig)\>

A promise that resolves with the updated provider configuration.

## BaseAuth.updateUser()

Updates an existing user.

See [Update a user](https://firebase.google.com/docs/auth/admin/manage-users#update_a_user) for code samples and detailed documentation.

**Signature:**  

    updateUser(uid: string, properties: UpdateRequest): Promise<UserRecord>;

### Parameters

| Parameter  |                                                                Type                                                                 |                  Description                   |
|------------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| uid        | string                                                                                                                              | The `uid` corresponding to the user to update. |
| properties | [UpdateRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequest_interface) | The properties to update on the provided user. |

**Returns:**

Promise\<[UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecord_class)\>

A promise fulfilled with the updated user data.

## BaseAuth.verifyIdToken()

Verifies a Firebase ID token (JWT). If the token is valid, the promise is fulfilled with the token's decoded claims; otherwise, the promise is rejected.

If `checkRevoked` is set to true, first verifies whether the corresponding user is disabled. If yes, an `auth/user-disabled` error is thrown. If no, verifies if the session corresponding to the ID token was revoked. If the corresponding user's session was invalidated, an `auth/id-token-revoked` error is thrown. If not specified the check is not applied.

See [Verify ID Tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) for code samples and detailed documentation.

**Signature:**  

    verifyIdToken(idToken: string, checkRevoked?: boolean): Promise<DecodedIdToken>;

### Parameters

|  Parameter   |  Type   |                                                                                                               Description                                                                                                                |
|--------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| idToken      | string  | The ID token to verify.                                                                                                                                                                                                                  |
| checkRevoked | boolean | Whether to check if the ID token was revoked. This requires an extra request to the Firebase Auth backend to check the `tokensValidAfterTime` time for the corresponding user. When not specified, this additional check is not applied. |

**Returns:**

Promise\<[DecodedIdToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtoken_interface)\>

A promise fulfilled with the token's decoded claims if the ID token is valid; otherwise, a rejected promise.

## BaseAuth.verifySessionCookie()

Verifies a Firebase session cookie. Returns a Promise with the cookie claims. Rejects the promise if the cookie could not be verified.

If `checkRevoked` is set to true, first verifies whether the corresponding user is disabled: If yes, an `auth/user-disabled` error is thrown. If no, verifies if the session corresponding to the session cookie was revoked. If the corresponding user's session was invalidated, an `auth/session-cookie-revoked` error is thrown. If not specified the check is not performed.

See [Verify Session Cookies](https://firebase.google.com/docs/auth/admin/manage-cookies#verify_session_cookie_and_check_permissions) for code samples and detailed documentation

**Signature:**  

    verifySessionCookie(sessionCookie: string, checkRevoked?: boolean): Promise<DecodedIdToken>;

### Parameters

|   Parameter   |  Type   |          Description          |
|---------------|---------|-------------------------------|
| sessionCookie | string  | The session cookie to verify. |
| checkRevoked  | boolean |                               |

**Returns:**

Promise\<[DecodedIdToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtoken_interface)\>

A promise fulfilled with the session cookie's decoded claims if the session cookie is valid; otherwise, a rejected promise.