# Source: https://firebase.google.com/docs/reference/rest/auth.md.txt

# Firebase Auth REST API

## API Usage


You can query the Firebase Auth backend through a REST API. This can be used for various operations such
as creating new users, signing in existing ones and editing or deleting these users.


Throughout this document, `API_KEY` refers to the Web API Key,
which can be obtained on the
[project settings](https://console.firebase.google.com/project/_/settings/general/)
page in your admin console.

> [!IMPORTANT]
> HTTPS is required. Firebase only responds to encrypted traffic so that your data remains safe.

### Exchange custom token for an ID and refresh token


You can exchange a custom Auth token for an ID and refresh token by issuing an HTTP
`POST` request to the Auth `verifyCustomToken` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| token | string | A Firebase Auth custom token from which to create an ID and refresh token pair. |
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. Should always be true. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | A Firebase Auth ID token generated from the provided custom token. |
| refreshToken | string | A Firebase Auth refresh token generated from the provided custom token. |
| expiresIn | string | The number of seconds in which the ID token expires. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"token":"[CUSTOM_TOKEN]","returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[CUSTOM_TOKEN]` with the generated custom Auth token.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the custom token.


**Sample response**

```
{
  "idToken": "[ID_TOKEN]",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600"
}
```


**Common error codes**

- INVALID_CUSTOM_TOKEN: The custom token format is incorrect or the token is invalid for some reason (e.g. expired, invalid signature etc.)
- CREDENTIAL_MISMATCH: The custom token corresponds to a different Firebase project.

### Exchange a refresh token for an ID token


You can refresh a Firebase ID token by issuing an HTTP
`POST` request to the `securetoken.googleapis.com` endpoint.

> [!NOTE]
> **Note:** By default, Google validates the project number of your refresh token to ensure it matches that of your API key. If the project number doesn't match, you will receive the `PROJECT_NUMBER_MISMATCH` error code. This validation mitigates the potential risk of abusers collecting your API keys to generate refresh tokens for their own projects. If you understand the risk and want to opt out of this behavior, you can submit an exemption request by filing a Google Cloud [support case](https://cloud.google.com/support/docs/customer-care-procedures).


**Method:** POST


**Content-Type:** application/x-www-form-urlencoded
**Endpoint**

```
https://securetoken.googleapis.com/v1/token?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| grant_type | string | The refresh token's grant type, always "refresh_token". |
| refresh_token | string | A Firebase Auth refresh token. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| expires_in | string | The number of seconds in which the ID token expires. |
| token_type | string | The type of the refresh token, always "Bearer". |
| refresh_token | string | The Firebase Auth refresh token provided in the request or a new refresh token. |
| id_token | string | A Firebase Auth ID token. |
| user_id | string | The uid corresponding to the provided ID token. |
| project_id | string | Your Firebase project ID. |


**Sample request**

```
curl 'https://securetoken.googleapis.com/v1/token?key=[API_KEY]' \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data 'grant_type=refresh_token&refresh_token=[REFRESH_TOKEN]'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[REFRESH_TOKEN]` with the Firebase refresh token.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the new Firebase ID token and refresh token.


**Sample response**

```
{
  "expires_in": "3600",
  "token_type": "Bearer",
  "refresh_token": "[REFRESH_TOKEN]",
  "id_token": "[ID_TOKEN]",
  "user_id": "tRcfmLH7o2XrNELi...",
  "project_id": "1234567890"
}
```


**Common error codes**

- TOKEN_EXPIRED: The user's credential is no longer valid. The user must sign in again.
- USER_DISABLED: The user account has been disabled by an administrator.
- USER_NOT_FOUND: The user corresponding to the refresh token was not found. It is likely the user was deleted.
- API key not valid. Please pass a valid API key. (invalid API key provided)
- INVALID_REFRESH_TOKEN: An invalid refresh token is provided.
- Invalid JSON payload received. Unknown name \\"refresh_tokens\\": Cannot bind query parameter. Field 'refresh_tokens' could not be found in request message.
- INVALID_GRANT_TYPE: The grant type specified is invalid.
- MISSING_REFRESH_TOKEN: No refresh token provided.
- PROJECT_NUMBER_MISMATCH: The project number of the refresh token does not match that of the API key provided.

### Sign up with email / password


You can create a new email and password user by issuing an HTTP
`POST` request to the Auth `signupNewUser` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| email | string | The email for the user to create. |
| password | string | The password for the user to create. |
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. Should always be true. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | A Firebase Auth ID token for the newly created user. |
| email | string | The email for the newly created user. |
| refreshToken | string | A Firebase Auth refresh token for the newly created user. |
| expiresIn | string | The number of seconds in which the ID token expires. |
| localId | string | The uid of the newly created user. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"email":"[user@example.com]","password":"[PASSWORD]","returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[user@example.com]` with the new user's email, and `[PASSWORD]` with the new user's password.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the new account.


**Sample response**

```
{
  "idToken": "[ID_TOKEN]",
  "email": "[user@example.com]",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "localId": "tRcfmLH7..."
}
```


**Common error codes**

- EMAIL_EXISTS: The email address is already in use by another account.
- OPERATION_NOT_ALLOWED: Password sign-in is disabled for this project.
- TOO_MANY_ATTEMPTS_TRY_LATER: We have blocked all requests from this device due to unusual activity. Try again later.

### Sign in with email / password


You can sign in a user with an email and password by issuing an HTTP
`POST` request to the Auth `verifyPassword` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| email | string | The email the user is signing in with. |
| password | string | The password for the account. |
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. Should always be true. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | A Firebase Auth ID token for the authenticated user. |
| email | string | The email for the authenticated user. |
| refreshToken | string | A Firebase Auth refresh token for the authenticated user. |
| expiresIn | string | The number of seconds in which the ID token expires. |
| localId | string | The uid of the authenticated user. |
| registered | boolean | Whether the email is for an existing account. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"email":"[user@example.com]","password":"[PASSWORD]","returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[user@example.com]` with the user's email and `[PASSWORD]` with the user's password.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the existing email/password account.


**Sample response**

```
{
  "localId": "ZY1rJK0eYLg...",
  "email": "[user@example.com]",
  "displayName": "",
  "idToken": "[ID_TOKEN]",
  "registered": true,
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600"
}
```


**Common error codes**

- EMAIL_NOT_FOUND: There is no user record corresponding to this identifier. The user may have been deleted.
- INVALID_PASSWORD: The password is invalid or the user does not have a password.
- USER_DISABLED: The user account has been disabled by an administrator.

### Sign in anonymously


You can sign in a user anonymously by issuing an HTTP
`POST` request to the Auth `signupNewUser` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. Should always be true. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | A Firebase Auth ID token for the newly created user. |
| email | string | Since the user is anonymous, this should be empty. |
| refreshToken | string | A Firebase Auth refresh token for the newly created user. |
| expiresIn | string | The number of seconds in which the ID token expires. |
| localId | string | The uid of the newly created user. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=[API_KEY]' \
-H 'Content-Type: application/json' --data-binary '{"returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the anonymous user.


**Sample response**

```
{
  "idToken": "[ID_TOKEN]",
  "email": "",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "localId": "Jws4SVjpT..."
}
```


**Common error codes**

- OPERATION_NOT_ALLOWED: Anonymous user sign-in is disabled for this project.

### Sign in with OAuth credential


You can sign in a user with an OAuth credential by issuing an HTTP
`POST` request to the Auth `verifyAssertion` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| requestUri | string | The URI to which the IDP redirects the user back. |
| postBody | string | Contains the OAuth credential (an ID token or access token) and provider ID which issues the credential. |
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. Should always be true. |
| returnIdpCredential | boolean | Whether to force the return of the OAuth credential on the following errors: FEDERATED_USER_ID_ALREADY_LINKED and EMAIL_EXISTS. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| federatedId | string | The unique ID identifies the IdP account. |
| providerId | string | The linked provider ID (e.g. "google.com" for the Google provider). |
| localId | string | The uid of the authenticated user. |
| emailVerified | boolean | Whether the sign-in email is verified. |
| email | string | The email of the account. |
| oauthIdToken | string | The OIDC id token if available. |
| oauthAccessToken | string | The OAuth access token if available. |
| oauthTokenSecret | string | The OAuth 1.0 token secret if available. |
| rawUserInfo | string | The stringified JSON response containing all the IdP data corresponding to the provided OAuth credential. |
| firstName | string | The first name for the account. |
| lastName | string | The last name for the account. |
| fullName | string | The full name for the account. |
| displayName | string | The display name for the account. |
| photoUrl | string | The photo Url for the account. |
| idToken | string | A Firebase Auth ID token for the authenticated user. |
| refreshToken | string | A Firebase Auth refresh token for the authenticated user. |
| expiresIn | string | The number of seconds in which the ID token expires. |
| needConfirmation | boolean | Whether another account with the same credential already exists. The user will need to sign in to the original account and then link the current credential to it. |


**Sample request with OAuth ID token**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"postBody":"id_token=[GOOGLE_ID_TOKEN]&providerId=[google.com]","requestUri":"[http://localhost]","returnIdpCredential":true,"returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[GOOGLE_ID_TOKEN]` with the Google OAuth ID token, `[google.com]` with the provider ID corresponding to the OAuth credential and `[http://localhost]` with the request URI.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the authenticated user.


**Sample response with OAuth ID token**

```
{
  "federatedId": "https://accounts.google.com/1234567890",
  "providerId": "google.com",
  "localId": "5xwsPCWYo...",
  "emailVerified": true,
  "email": "user@example.com",
  "oauthIdToken": "[GOOGLE_ID_TOKEN]",
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "displayName": "John Doe",
  "idToken": "[ID_TOKEN]",
  "photoUrl": "https://lh5.googleusercontent.com/.../photo.jpg",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "rawUserInfo": "{\"updated_time\":\"2017-02-22T01:10:57+0000\",\"gender\":\"male\", ...}"
}
```


**Sample request with OAuth access token**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"postBody":"access_token=[FACEBOOK_ACCESS_TOKEN]&providerId=[facebook.com]","requestUri":"[http://localhost]","returnIdpCredential":true,"returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[FACEBOOK_ACCESS_TOKEN]` with the Facebook access token, `[facebook.com]` with the provider ID corresponding to the OAuth credential and `[http://localhost]` with the request URI.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the authenticated user.


**Sample response with OAuth access token**

```
{
  "federatedId": "http://facebook.com/1234567890",
  "providerId": "facebook.com",
  "localId": "5xwsPCWYo...",
  "emailVerified": true,
  "email": "user@example.com",
  "oauthAccessToken": "[FACEBOOK_ACCESS_TOKEN]",
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "displayName": "John Doe",
  "idToken": "[ID_TOKEN]",
  "photoUrl": "https://scontent.xx.fbcdn.net/v/...",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "rawUserInfo": "{\"updated_time\":\"2017-02-22T01:10:57+0000\",\"gender\":\"male\", ...}"
}
```


**Sample request with Twitter OAuth 1.0 credential**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"postBody":"access_token=[TWITTER_ACCESS_TOKEN]&oauth_token_secret=[TWITTER_TOKEN_SECRET]&providerId=[twitter.com]","requestUri":"[http://localhost]","returnIdpCredential":true,"returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[TWITTER_ACCESS_TOKEN]` with the Twitter OAuth access token, `[TWITTER_TOKEN_SECRET]` with the Twitter OAuth token secret, `[twitter.com]` with the provider ID corresponding to the OAuth credential and `[http://localhost]` with the request URI.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the authenticated user.


**Sample response with Twitter OAuth 1.0 credential**

```
{
  "federatedId": "http://twitter.com/1234567890",
  "providerId": "twitter.com",
  "localId": "5xwsPCWYo...",
  "emailVerified": true,
  "email": "user@example.com",
  "oauthAccessToken": "[OAUTH_ACCESS_TOKEN]",
  "oauthTokenSecret": "[OAUTH_TOKEN_SECRET]",
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "displayName": "John Doe",
  "idToken": "[ID_TOKEN]",
  "photoUrl": "http://abs.twimg.com/sticky/...",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "rawUserInfo": "{\"updated_time\":\"2017-02-22T01:10:57+0000\",\"gender\":\"male\", ...}"
}
```


**Common error codes**

- OPERATION_NOT_ALLOWED: The corresponding provider is disabled for this project.
- INVALID_IDP_RESPONSE: The supplied auth credential is malformed or has expired.

### Fetch providers for email


You can look all providers associated with a specified email by issuing an HTTP
`POST` request to the Auth `createAuthUri` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:createAuthUri?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| identifier | string | User's email address |
| continueUri | string | The URI to which the IDP redirects the user back. For this use case, this is just the current URL. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| allProviders | List of strings | The list of providers that the user has previously signed in with. |
| registered | boolean | Whether the email is for an existing account |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:createAuthUri?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"identifier":"[user@example.com]","continueUri":"[http://localhost:8080/app]"}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[user@example.com]` with the email to lookup and `[http://localhost:8080/app]` with the current URL.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the list of providers associated with the email.


**Sample response**

```
{
  "allProviders": [
    "password",
    "google.com"
  ],
  "registered": true
}
```


**Common error codes**

- INVALID_EMAIL: The email address is badly formatted.

### Send password reset email


You can send a password reset email by issuing an HTTP
`POST` request to the Auth `getOobConfirmationCode` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=[API_KEY]
```
**Optional Headers**

| Property Name | Description |
|---|---|
| X-Firebase-Locale | The language code corresponding to the user's locale. Passing this will localize the password reset email sent to the user. |

**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| requestType | string | The kind of OOB code to return. Should be "PASSWORD_RESET" for password reset. |
| email | string | User's email address. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| email | string | User's email address. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"requestType":"PASSWORD_RESET","email":"[user@example.com]"}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[user@example.com]` with the email to send the password reset to.


A successful request is indicated by a `200 OK` HTTP
status code.


**Sample response**

```
{
 "email": "[user@example.com]"
}
```


**Common error codes**

- EMAIL_NOT_FOUND: There is no user record corresponding to this identifier. The user may have been deleted.

### Verify password reset code


You can verify a password reset code by issuing an HTTP
`POST` request to the Auth `resetPassword` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:resetPassword?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| oobCode | string | The email action code sent to the user's email for resetting the password. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| email | string | User's email address. |
| requestType | string | Type of the email action code. Should be "PASSWORD_RESET". |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:resetPassword?key=[API_KEY]' \
-H 'Content-Type: application/json' --data-binary '{"oobCode":"[PASSWORD_RESET_CODE]"}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[PASSWORD_RESET_CODE]` with the password reset action code.


A successful request is indicated by a `200 OK` HTTP
status code.


**Sample response**

```
{
  "email": "[user@example.com]",
  "requestType": "PASSWORD_RESET"
}
```


**Common error codes**

- OPERATION_NOT_ALLOWED: Password sign-in is disabled for this project.
- EXPIRED_OOB_CODE: The action code has expired.
- INVALID_OOB_CODE: The action code is invalid. This can happen if the code is malformed, expired, or has already been used.

### Confirm password reset


You can apply a password reset change by issuing an HTTP
`POST` request to the Auth `resetPassword` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:resetPassword?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| oobCode | string | The email action code sent to the user's email for resetting the password. |
| newPassword | string | The user's new password. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| email | string | User's email address. |
| requestType | string | Type of the email action code. Should be "PASSWORD_RESET". |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:resetPassword?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"oobCode":"[PASSWORD_RESET_CODE]","newPassword":"[NEW_PASSWORD]"}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[PASSWORD_RESET_CODE]` with the password reset action code and `[NEW_PASSWORD]` with the user's new password.


A successful request is indicated by a `200 OK` HTTP
status code.


**Sample response**

```
{
  "email": "[user@example.com]",
  "requestType": "PASSWORD_RESET"
}
```


**Common error codes**

- OPERATION_NOT_ALLOWED: Password sign-in is disabled for this project.
- EXPIRED_OOB_CODE: The action code has expired.
- INVALID_OOB_CODE: The action code is invalid. This can happen if the code is malformed, expired, or has already been used.
- USER_DISABLED: The user account has been disabled by an administrator.

### Change email


You can change a user's email by issuing an HTTP
`POST` request to the Auth `setAccountInfo` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]
```
**Optional Headers**

| Property Name | Description |
|---|---|
| X-Firebase-Locale | The language code corresponding to the user's locale. Passing this will localize the email change revocation sent to the user. |

**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | A Firebase Auth ID token for the user. |
| email | string | The user's new email. |
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| localId | string | The uid of the current user. |
| email | string | User's email address. |
| passwordHash | string | Hash version of the password. |
| providerUserInfo | List of JSON objects | List of all linked provider objects which contain "providerId" and "federatedId". |
| idToken | string | New Firebase Auth ID token for user. |
| refreshToken | string | A Firebase Auth refresh token. |
| expiresIn | string | The number of seconds in which the ID token expires. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary \
'{"idToken":"[FIREBASE_ID_TOKEN]","email":"[user@example2.com]","returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[FIREBASE_ID_TOKEN]` with the user's Firebase ID token and `[user@example2.com]` with the user's new email.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the new Firebase ID token and refresh token associated
with the user.


**Sample response**

```
{
  "localId": "tRcfmLH7o2...",
  "email": "[user@example2.com]",
  "passwordHash": "...",
  "providerUserInfo": [
    {
      "providerId": "password",
      "federatedId": "[user@example2.com]"
    }
  ],
  "idToken": "[NEW_ID_TOKEN]",
  "refreshToken": "[NEW_REFRESH_TOKEN]",
  "expiresIn": "3600"
}
```


**Common error codes**

- EMAIL_EXISTS: The email address is already in use by another account.
- INVALID_ID_TOKEN:The user's credential is no longer valid. The user must sign in again.

### Change password


You can change a user's password by issuing an HTTP
`POST` request to the Auth `setAccountInfo` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | A Firebase Auth ID token for the user. |
| password | string | User's new password. |
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| localId | string | The uid of the current user. |
| email | string | User's email address. |
| passwordHash | string | Hash version of password. |
| providerUserInfo | List of JSON objects | List of all linked provider objects which contain "providerId" and "federatedId". |
| idToken | string | New Firebase Auth ID token for user. |
| refreshToken | string | A Firebase Auth refresh token. |
| expiresIn | string | The number of seconds in which the ID token expires. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary \
'{"idToken":"[FIREBASE_ID_TOKEN]","password":"[NEW_PASSWORD]","returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[FIREBASE_ID_TOKEN]` with the user's Firebase ID token and `[NEW_PASSWORD]` with the user's new password.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the new Firebase ID token and refresh token associated
with the user.


**Sample response**

```
{
  "localId": "tRcfmLH7o2...",
  "email": "[user@example.com]",
  "passwordHash": "...",
  "providerUserInfo": [
    {
      "providerId": "password",
      "federatedId": "[user@example.com]"
    }
  ],
  "idToken": "[NEW_ID_TOKEN]",
  "refreshToken": "[NEW_REFRESH_TOKEN]",
  "expiresIn": "3600"
}
```


**Common error codes**

- INVALID_ID_TOKEN:The user's credential is no longer valid. The user must sign in again.
- WEAK_PASSWORD: The password must be 6 characters long or more.

### Update profile


You can update a user's profile (display name / photo URL) by issuing an HTTP
`POST` request to the Auth `setAccountInfo` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | A Firebase Auth ID token for the user. |
| displayName | string | User's new display name. |
| photoUrl | string | User's new photo url. |
| deleteAttribute | List of strings | List of attributes to delete, "DISPLAY_NAME" or "PHOTO_URL". This will nullify these values. |
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| localId | string | The uid of the current user. |
| email | string | User's email address. |
| displayName | string | User's new display name. |
| photoUrl | string | User's new photo url. |
| passwordHash | string | Hash version of password. |
| providerUserInfo | List of JSON objects | List of all linked provider objects which contain "providerId" and "federatedId". |
| idToken | string | New Firebase Auth ID token for user. |
| refreshToken | string | A Firebase Auth refresh token. |
| expiresIn | string | The number of seconds in which the ID token expires. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary \
'{"idToken":"[ID_TOKEN]","displayName":"[NAME]","photoUrl":"[URL]","returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[ID_TOKEN]` with the user's Firebase ID token, `[NAME]` with the user's new display name and `[URL]` with the user's new photo URL.


A successful request is indicated by a `200 OK` HTTP
status code.


**Sample response**

```
{
  "localId": "tRcfmLH...",
  "email": "user@example2.com",
  "displayName": "John Doe",
  "photoUrl": "[http://localhost:8080/img1234567890/photo.png]",
  "passwordHash": "...",
  "providerUserInfo": [
    {
      "providerId": "password",
      "federatedId": "user@example2.com",
      "displayName": "John Doe",
      "photoUrl": "http://localhost:8080/img1234567890/photo.png"
    }
  ],
  "idToken": "[NEW_ID_TOKEN]",
  "refreshToken": "[NEW_REFRESH_TOKEN]",
  "expiresIn": "3600"
}
```


**Common error codes**

- INVALID_ID_TOKEN:The user's credential is no longer valid. The user must sign in again.

### Get user data


You can get a user's data by issuing an HTTP
`POST` request to the Auth `getAccountInfo` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | The Firebase ID token of the account. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| users | List of JSON objects | The account associated with the given Firebase ID token. Check below for more details. |

**Response Payload (`users` array content)**

| Property Name | Type | Description |
|---|---|---|
| localId | string | The uid of the current user. |
| email | string | The email of the account. |
| emailVerified | boolean | Whether or not the account's email has been verified. |
| displayName | string | The display name for the account. |
| providerUserInfo | List of JSON objects | List of all linked provider objects which contain "providerId" and "federatedId". |
| photoUrl | string | The photo Url for the account. |
| passwordHash | string | Hash version of password. |
| passwordUpdatedAt | double | The timestamp, in milliseconds, that the account password was last changed. |
| validSince | string | The timestamp, in seconds, which marks a boundary, before which Firebase ID token are considered revoked. |
| disabled | boolean | Whether the account is disabled or not. |
| lastLoginAt | string | The timestamp, in milliseconds, that the account last logged in at. |
| createdAt | string | The timestamp, in milliseconds, that the account was created at. |
| customAuth | boolean | Whether the account is authenticated by the developer. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=[API_KEY]' \
-H 'Content-Type: application/json' --data-binary '{"idToken":"[FIREBASE_ID_TOKEN]"}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project and `[FIREBASE_ID_TOKEN]` with the user's Firebase ID token.


A successful request is indicated by a `200 OK` HTTP
status code. The response will contain all the user information associated with the account.


**Sample response**

```
{
  "users": [
    {
      "localId": "ZY1rJK0...",
      "email": "user@example.com",
      "emailVerified": false,
      "displayName": "John Doe",
      "providerUserInfo": [
        {
          "providerId": "password",
          "displayName": "John Doe",
          "photoUrl": "http://localhost:8080/img1234567890/photo.png",
          "federatedId": "user@example.com",
          "email": "user@example.com",
          "rawId": "user@example.com",
          "screenName": "user@example.com"
        }
      ],
      "photoUrl": "https://lh5.googleusercontent.com/.../photo.jpg",
      "passwordHash": "...",
      "passwordUpdatedAt": 1.484124177E12,
      "validSince": "1484124177",
      "disabled": false,
      "lastLoginAt": "1484628946000",
      "createdAt": "1484124142000",
      "customAuth": false
    }
  ]
}
```


**Common error codes**

- INVALID_ID_TOKEN:The user's credential is no longer valid. The user must sign in again.
- USER_NOT_FOUND: There is no user record corresponding to this identifier. The user may have been deleted.

### Link with email/password


You can link an email/password to a current user by issuing an HTTP
`POST` request to the Auth `setAccountInfo` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | The Firebase ID token of the account you are trying to link the credential to. |
| email | string | The email to link to the account. |
| password | string | The new password of the account. |
| returnSecureToken | string | Whether or not to return an ID and refresh token. Should always be true. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| localId | string | The uid of the current user. |
| email | string | The email of the account. |
| displayName | string | The display name for the account. |
| photoUrl | string | The photo Url for the account. |
| passwordHash | string | Hash version of password. |
| providerUserInfo | List of JSON objects | List of all linked provider objects which contain "providerId" and "federatedId". |
| emailVerified | boolean | Whether or not the account's email has been verified. |
| idToken | string | New Firebase Auth ID token for user. |
| refreshToken | string | A Firebase Auth refresh token. |
| expiresIn | string | The number of seconds in which the ID token expires. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary \
'{"idToken":"[ID_TOKEN]","email":"[user@example.com]","password":"[PASS]","returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[ID_TOKEN]` with the user's Firebase ID token, `[user@example.com]` with the user's email that needs to be linked and `[PASS]` with the password that needs to be linked.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated with the
authenticated user.


**Sample response**

```
{
  "localId": "huDwUz...",
  "email": "user@example.com",
  "displayName": "John Doe",
  "photoUrl": "https://lh5.googleusercontent.com/.../photo.jpg",
  "passwordHash": "...",
  "providerUserInfo": [
    {
      "providerId": "password",
      "federatedId": "user@example.com"
    }
  ],
  "idToken": "[ID_TOKEN]",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "emailVerified": false
}
```


**Common error codes**

- CREDENTIAL_TOO_OLD_LOGIN_AGAIN: The user's credential is no longer valid. The user must sign in again.
- TOKEN_EXPIRED: The user's credential is no longer valid. The user must sign in again.
- INVALID_ID_TOKEN:The user's credential is no longer valid. The user must sign in again.
- WEAK_PASSWORD: The password must be 6 characters long or more.

### Link with OAuth credential


You can link an OAuth credential to a user by issuing an HTTP
`POST` request to the Auth `verifyAssertion` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | The Firebase ID token of the account you are trying to link the credential to. |
| requestUri | string | The URI to which the IDP redirects the user back. |
| postBody | string | Contains the OAuth credential (an ID token or access token) and provider ID which issues the credential. |
| returnSecureToken | boolean | Whether or not to return an ID and refresh token. Should always be true. |
| returnIdpCredential | boolean | Whether to force the return of the OAuth credential on the following errors: FEDERATED_USER_ID_ALREADY_LINKED and EMAIL_EXISTS. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| federatedId | string | The unique ID identifies the IdP account. |
| providerId | string | The linked provider ID (e.g. "google.com" for the Google provider). |
| localId | string | The uid of the authenticated user. |
| emailVerified | boolean | Whether the signin email is verified. |
| email | string | The email of the account. |
| oauthIdToken | string | The OIDC id token if available. |
| oauthAccessToken | string | The OAuth access token if available. |
| oauthTokenSecret | string | The OAuth 1.0 token secret if available. |
| rawUserInfo | string | The stringified JSON response containing all the IdP data corresponding to the provided OAuth credential. |
| firstName | string | The first name for the account. |
| lastName | string | The last name for the account. |
| fullName | string | The full name for the account. |
| displayName | string | The display name for the account. |
| photoUrl | string | The photo Url for the account. |
| idToken | string | A Firebase Auth ID token for the authenticated user. |
| refreshToken | string | A Firebase Auth refresh token for the authenticated user. |
| expiresIn | string | The number of seconds in which the ID token expires. |


**Sample request with OAuth ID token**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"postBody":"id_token=[GOOGLE_ID_TOKEN]&providerId=[google.com]","requestUri":"[http://localhost]","idToken":"[FIREBASE_ID_TOKEN]","returnIdpCredential":true,"returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[FIREBASE_ID_TOKEN]` with the current user's Firebase ID token, `[GOOGLE_ID_TOKEN]` with the Google OAuth ID token, `[google.com]` with the provider ID corresponding to the OAuth credential and `[http://localhost]` with the request URI.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the authenticated user.


**Sample response with OAuth ID token**

```
{
  "federatedId": "https://accounts.google.com/1234567890",
  "providerId": "google.com",
  "localId": "5xwsPCWYo...",
  "emailVerified": true,
  "email": "user@example.com",
  "oauthIdToken": "[GOOGLE_ID_TOKEN]",
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "displayName": "John Doe",
  "idToken": "[ID_TOKEN]",
  "photoUrl": "https://lh5.googleusercontent.com/.../photo.jpg",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "rawUserInfo": "{\"updated_time\":\"2017-02-22T01:10:57+0000\",\"gender\":\"male\", ...}"
}
```


**Sample request with OAuth access token**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"postBody":"access_token=[FACEBOOK_ACCESS_TOKEN]&providerId=[facebook.com]","idToken":"[FIREBASE_ID_TOKEN]","requestUri":"[http://localhost]","returnIdpCredential":true,"returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[FIREBASE_ID_TOKEN]` with the current user's Firebase ID token, `[FACEBOOK_ACCESS_TOKEN]` with the Facebook access token, `[facebook.com]` with the provider ID corresponding to the OAuth credential and `[http://localhost]` with the request URI.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the authenticated user.


**Sample response with OAuth access token**

```
{
  "federatedId": "http://facebook.com/1234567890",
  "providerId": "facebook.com",
  "localId": "5xwsPCWYo...",
  "emailVerified": true,
  "email": "user@example.com",
  "oauthAccessToken": "[FACEBOOK_ACCESS_TOKEN]",
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "displayName": "John Doe",
  "idToken": "[ID_TOKEN]",
  "photoUrl": "https://scontent.xx.fbcdn.net/v/...",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "rawUserInfo": "{\"updated_time\":\"2017-02-22T01:10:57+0000\",\"gender\":\"male\", ...}"
}
```


**Sample request with Twitter OAuth 1.0 credential**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"postBody":"access_token=[TWITTER_ACCESS_TOKEN]&oauth_token_secret=[TWITTER_TOKEN_SECRET]&providerId=[twitter.com]","requestUri":"[http://localhost]","idToken":"[FIREBASE_ID_TOKEN]","returnIdpCredential":true,"returnSecureToken":true}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[FIREBASE_ID_TOKEN]` with the current user's Firebase ID token, `[TWITTER_ACCESS_TOKEN]` with the Twitter OAuth access token, `[TWITTER_TOKEN_SECRET]` with the Twitter OAuth token secret, `[twitter.com]` with the provider ID corresponding to the OAuth credential and `[http://localhost]` with the request URI.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the Firebase ID token and refresh token associated
with the authenticated user.


**Sample response with Twitter OAuth 1.0 credential**

```
{
  "federatedId": "http://twitter.com/1234567890",
  "providerId": "twitter.com",
  "localId": "5xwsPCWYo...",
  "emailVerified": true,
  "email": "user@example.com",
  "oauthAccessToken": "[OAUTH_ACCESS_TOKEN]",
  "oauthTokenSecret": "[OAUTH_TOKEN_SECRET]",
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "displayName": "John Doe",
  "idToken": "[ID_TOKEN]",
  "photoUrl": "http://abs.twimg.com/sticky/...",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "rawUserInfo": "{\"updated_time\":\"2017-02-22T01:10:57+0000\",\"gender\":\"male\", ...}"
}
```


**Common error codes**

- OPERATION_NOT_ALLOWED: The corresponding provider is disabled for this project.
- INVALID_IDP_RESPONSE: The supplied auth credential is malformed or has expired.
- INVALID_ID_TOKEN:The user's credential is no longer valid. The user must sign in again.
- EMAIL_EXISTS: The email address is already in use by another account.
- FEDERATED_USER_ID_ALREADY_LINKED: This credential is already associated with a different user account.

### Unlink provider


You can unlink a provider from a current user by issuing an HTTP
`POST` request to the Auth `setAccountInfo` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | The Firebase ID token of the account. |
| deleteProvider | List of strings | The list of provider IDs to unlink, eg: 'google.com', 'password', etc. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| localId | string | The uid of the current user. |
| email | string | The email of the account. |
| displayName | string | The display name for the account. |
| photoUrl | string | The photo Url for the account. |
| passwordHash | string | Hash version of the password. |
| providerUserInfo | List of JSON objects | List of all linked provider objects which contain "providerId" and "federatedId". |
| emailVerified | boolean | Whether or not the account's email has been verified. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"idToken":"[FIREBASE_ID_TOKEN]","deleteProvider":["[facebook.com]"]}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project, `[FIREBASE_ID_TOKEN]` with the user's Firebase ID token and `[facebook.com]` with the provider ID to unlink.


A successful request is indicated by a `200 OK` HTTP
status code.


**Sample response**

```
{
  "localId": "huDwUz...",
  "email": "user@example.com",
  "displayName": "John Doe",
  "photoUrl": "https://lh5.googleusercontent.com/.../photo.jpg",
  "passwordHash": "...",
  "providerUserInfo": [
    {
      "providerId": "google.com",
      "federatedId": "1234567890",
      "displayName": "John Doe",
      "photoUrl": "https://lh5.googleusercontent.com/.../photo.jpg"
    },
    {
      "providerId": "password",
      "federatedId": "user@example.com"
    }
  ],
  "emailVerified": "true"
}
```


**Common error codes**

- INVALID_ID_TOKEN: The user's credential is no longer valid. The user must sign in again.

### Send email verification


You can send an email verification for the current user by issuing an HTTP
`POST` request to the Auth `getOobConfirmationCode` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=[API_KEY]
```
**Optional Headers**

| Property Name | Description |
|---|---|
| X-Firebase-Locale | The language code corresponding to the user's locale. Passing this will localize the email verification sent to the user. |

**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| requestType | string | The type of confirmation code to send. Should always be "VERIFY_EMAIL". |
| idToken | string | The Firebase ID token of the user to verify. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| email | string | The email of the account. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=[API_KEY]' \
-H 'Content-Type: application/json' \
--data-binary '{"requestType":"VERIFY_EMAIL","idToken":"[FIREBASE_ID_TOKEN]"}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project and `[FIREBASE_ID_TOKEN]` with the current user's Firebase ID token.


A successful request is indicated by a `200 OK` HTTP
status code.


**Sample response**

```
{
  "email": "user@example.com"
}
```


**Common error codes**

- INVALID_ID_TOKEN: The user's credential is no longer valid. The user must sign in again.
- USER_NOT_FOUND: There is no user record corresponding to this identifier. The user may have been deleted.

### Confirm email verification


You can confirm an email verification code by issuing an HTTP
`POST` request to the Auth `setAccountInfo` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| oobCode | string | The action code sent to user's email for email verification. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| email | string | The email of the account. |
| displayName | string | The display name for the account. |
| photoUrl | string | The photo Url for the account. |
| passwordHash | string | The password hash. |
| providerUserInfo | List of JSON objects | List of all linked provider objects which contain "providerId" and "federatedId". |
| emailVerified | boolean | Whether or not the account's email has been verified. |


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:update?key=[API_KEY]' \
-H 'Content-Type: application/json' --data-binary '{"oobCode":"[VERIFICATION_CODE]"}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project and `[VERIFICATION_CODE]` with the email verification code.


A successful request is indicated by a `200 OK` HTTP
status code.


**Sample response**

```
{
  "localId": "FhyStE...",
  "email": "user@example.com",
  "passwordHash": "...",
  "providerUserInfo": [
    {
      "providerId": "password",
      "federatedId": "user@example.com"
    }
  ]
}
```


**Common error codes**

- EXPIRED_OOB_CODE: The action code has expired.
- INVALID_OOB_CODE: The action code is invalid. This can happen if the code is malformed, expired, or has already been used.
- USER_DISABLED: The user account has been disabled by an administrator.
- EMAIL_NOT_FOUND: There is no user record corresponding to this identifier. The user may have been deleted.

### Delete account


You can delete a current user by issuing an HTTP
`POST` request to the Auth `deleteAccount` endpoint.


**Method:** POST


**Content-Type:** application/json
**Endpoint**

```
https://identitytoolkit.googleapis.com/v1/accounts:delete?key=[API_KEY]
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| idToken | string | The Firebase ID token of the user to delete. |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|


**Sample request**

```
curl 'https://identitytoolkit.googleapis.com/v1/accounts:delete?key=[API_KEY]' \
-H 'Content-Type: application/json' --data-binary '{"idToken":"[FIREBASE_ID_TOKEN]"}'
```

> [!IMPORTANT]
> In the example above, you would replace `[API_KEY]` with the Web API Key of your Firebase project and `[FIREBASE_ID_TOKEN]` with the user's Firebase ID token.


A successful request is indicated by a `200 OK` HTTP
status code.


**Common error codes**

- INVALID_ID_TOKEN:The user's credential is no longer valid. The user must sign in again.
- USER_NOT_FOUND: There is no user record corresponding to this identifier. The user may have been deleted.

## Firebase Authentication Emulator


The Firebase Local Emulator Suite includes an [Authentication emulator](https://firebase.google.com/docs/emulator-suite/connect_auth), which can be used for
local prototyping and testing of authentication flows. The emulator exposes the following REST
endpoints.

> [!IMPORTANT]
> HTTP is required. Connections to the emulator are on `localhost`, and the emulator does not support encryption.

### Clear user accounts


Remove all accounts in the specified project, regardless of state.


**Method:** DELETE
**Endpoint**


Note that `9099` is the default port for the Authentication emulator. Check terminal
output for the actual port being used.

```
http://localhost:9099/emulator/v1/projects/{project-id}/accounts
```

### Get emulator configuration


Get emulator-specific configuration for the specified project.


**Method:** GET
**Endpoint**


Note that `9099` is the default port for the Authentication emulator. Check terminal
output for the actual port being used.

```
http://localhost:9099/emulator/v1/projects/{project-id}/config
```
**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| signIn | object | signIn configuration object containing a single key, `allowDuplicateEmails` (boolean). |

### Patch emulator configuration


Update emulator-specific configuration for the specified project.


**Method:** PATCH
**Endpoint**


Note that `9099` is the default port for the Authentication emulator. Check terminal
output for the actual port being used.


**Content-Type:** application/json

```
http://localhost:9099/emulator/v1/projects/{project-id}/config
```
**Request Body Payload**

| Property Name | Type | Description |
|---|---|---|
| signIn | object | Desired signIn configuration object with single key, `allowDuplicateEmails` (boolean). |

**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| signIn | object | Post-request signIn configuration object with single key, `allowDuplicateEmails` (boolean). |

### Retrieve out-of-band authentication codes


If the authentication flows you are testing would normally generate out-of-band codes (e.g.,
email verification codes, password reset codes), the emulator stores such codes internally until
they are used.


**Method:** GET
**Endpoint**


Note that `9099` is the default port for the Authentication emulator. Check terminal
output for the actual port being used.

```
http://localhost:9099/emulator/v1/projects/{project-id}/oobCodes
```
**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| oobCodes | array | An array of objects containing details of all pending confirmation codes. Each object contains `email` (string), `oobCode` (string), `oobLink` (string), and `requestType` (string) |

### Retrieve SMS verification codes


If you are testing phone/SMS authentication flows, the emulator stores such SMS codes internally
until they are used.


**Method:** GET
**Endpoint**


Note that `9099` is the default port for the Authentication emulator. Check terminal
output for the actual port being used.

```
http://localhost:9099/emulator/v1/projects/{project-id}/verificationCodes
```
**Response Payload**

| Property Name | Type | Description |
|---|---|---|
| verificationCodes | array | An array of objects containing details of all pending verification codes. Each object contains `phoneNumber` (string) and `sessionCode` (string). |

## Error Response

### Error response format


Anytime an error is returned from the backend server for any of the APIs above, the response
will have the following format.


**Sample response**

```
{
  "error": {
    "errors": [
      {
        "domain": "global",
        "reason": "invalid",
        "message": "CREDENTIAL_TOO_OLD_LOGIN_AGAIN"
      }
    ],
    "code": 400,
    "message": "CREDENTIAL_TOO_OLD_LOGIN_AGAIN"
  }
}
```


The error code is obtained from the message field. All of the above error codes refer to the
message field content.