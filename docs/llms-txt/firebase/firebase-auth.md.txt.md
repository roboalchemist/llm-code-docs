# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth.md.txt

# FirebaseAdmin.Auth.FirebaseAuth Class Reference

# FirebaseAdmin.Auth.FirebaseAuth

This is the entry point to all server-side Firebase Authentication operations.

## Summary

You can get an instance of this class via `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a8815159193202ba698230e7e6943fb32`.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.AbstractFirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/abstract-firebase-auth)

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a8815159193202ba698230e7e6943fb32` | `static https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth` Gets the auth instance associated with the default Firebase app. |

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a343bd2db15e2a59f087df8542b5350b9 => this.IfNotDeleted(() => this.tenantManager.Value)` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager` Gets the [TenantManager](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a343bd2db15e2a59f087df8542b5350b9) instance associated with the current project. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1afd29ad35723781c2a40d199c43b81a26(https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app app)` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth` Returns the auth instance for the specified app. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1adc3b86778805979f1936b726940159fb(string idToken, https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/session-cookie-options#class_firebase_admin_1_1_auth_1_1_session_cookie_options options)` | `async Task< string >` Creates a new Firebase session cookie from the given ID token and options. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1ad78f0abefe2ecefedbca0ef1d182dac5(string idToken, https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/session-cookie-options#class_firebase_admin_1_1_auth_1_1_session_cookie_options options, CancellationToken cancellationToken)` | `async Task< string >` Creates a new Firebase session cookie from the given ID token and options. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a02a32f82a48e029874cca9817a169be8(string sessionCookie)` | `async Task< https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token >` Parses and verifies a Firebase session cookie. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a3797b22879456b7037bf1cb1c8012d13(string sessionCookie, CancellationToken cancellationToken)` | `async Task< https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token >` Parses and verifies a Firebase session cookie. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a1a32fe7b2bd914ad3f30705797aa4f4a(string sessionCookie, bool checkRevoked)` | `async Task< https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token >` Parses and verifies a Firebase session cookie. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a010812c3d6b3a70578761265830703f5(string sessionCookie, bool checkRevoked, CancellationToken cancellationToken)` | `async Task< https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token >` Parses and verifies a Firebase session cookie. |

## Properties

### DefaultInstance

```
static FirebaseAuth DefaultInstance
```
Gets the auth instance associated with the default Firebase app.

This property is `null` if the default app doesn't yet exist.

## Public attributes

### TenantManager

```
TenantManager TenantManager => this.IfNotDeleted(() => this.tenantManager.Value)
```
Gets the [TenantManager](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth_1a343bd2db15e2a59f087df8542b5350b9) instance associated with the current project.

## Public static functions

### GetAuth

```
FirebaseAuth GetAuth(
  FirebaseApp app
)
```
Returns the auth instance for the specified app.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `System.ArgumentNullException` | If the app argument is null. | |
| Parameters | |---|---| | `app` | An app instance. | |
| **Returns** | The [FirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth) instance associated with the specified app. |

## Public functions

### CreateSessionCookieAsync

```
async Task< string > CreateSessionCookieAsync(
  string idToken,
  SessionCookieOptions options
)
```
Creates a new Firebase session cookie from the given ID token and options.

The returned JWT can be set as a server-side session cookie with a custom cookie policy.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `FirebaseAuthException` | If an error occurs while creating the cookie. | |
| Parameters | |---|---| | `idToken` | The Firebase ID token to exchange for a session cookie. | | `options` | Additional options required to create the cookie. | |
| **Returns** | A task that completes with the Firebase session cookie. |

### CreateSessionCookieAsync

```
async Task< string > CreateSessionCookieAsync(
  string idToken,
  SessionCookieOptions options,
  CancellationToken cancellationToken
)
```
Creates a new Firebase session cookie from the given ID token and options.

The returned JWT can be set as a server-side session cookie with a custom cookie policy.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `FirebaseAuthException` | If an error occurs while creating the cookie. | |
| Parameters | |---|---| | `idToken` | The Firebase ID token to exchange for a session cookie. | | `options` | Additional options required to create the cookie. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| **Returns** | A task that completes with the Firebase session cookie. |

### VerifySessionCookieAsync

```
async Task< FirebaseToken > VerifySessionCookieAsync(
  string sessionCookie
)
```
Parses and verifies a Firebase session cookie.

See [Manage Session Cookies](https://firebase.google.com/docs/auth/admin/manage-cookies) for code samples and detailed documentation.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `ArgumentException` | If the session cookie is null or empty. | | `FirebaseAuthException` | If the session cookie is invalid. | |
| Parameters | |---|---| | `sessionCookie` | A Firebase session cookie string to verify and parse. | |
| **Returns** | A task that completes with a [FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token) representing the verified and decoded session cookie. |

### VerifySessionCookieAsync

```
async Task< FirebaseToken > VerifySessionCookieAsync(
  string sessionCookie,
  CancellationToken cancellationToken
)
```
Parses and verifies a Firebase session cookie.

See [Manage Session Cookies](https://firebase.google.com/docs/auth/admin/manage-cookies) for code samples and detailed documentation.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `ArgumentException` | If the session cookie is null or empty. | | `FirebaseAuthException` | If the session cookie is invalid. | |
| Parameters | |---|---| | `sessionCookie` | A Firebase session cookie string to verify and parse. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| **Returns** | A task that completes with a [FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token) representing the verified and decoded session cookie. |

### VerifySessionCookieAsync

```
async Task< FirebaseToken > VerifySessionCookieAsync(
  string sessionCookie,
  bool checkRevoked
)
```
Parses and verifies a Firebase session cookie.

See [Manage Session Cookies](https://firebase.google.com/docs/auth/admin/manage-cookies) for code samples and detailed documentation.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `ArgumentException` | If the session cookie is null or empty. | | `FirebaseAuthException` | If the session cookie is invalid. | |
| Parameters | |---|---| | `sessionCookie` | A Firebase session cookie string to verify and parse. | | `checkRevoked` | A boolean indicating whether to check if the tokens were revoked. | |
| **Returns** | A task that completes with a [FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token) representing the verified and decoded session cookie. |

### VerifySessionCookieAsync

```
async Task< FirebaseToken > VerifySessionCookieAsync(
  string sessionCookie,
  bool checkRevoked,
  CancellationToken cancellationToken
)
```
Parses and verifies a Firebase session cookie.

See [Manage Session Cookies](https://firebase.google.com/docs/auth/admin/manage-cookies) for code samples and detailed documentation.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `ArgumentException` | If the session cookie is null or empty. | | `FirebaseAuthException` | If the session cookie is invalid. | |
| Parameters | |---|---| | `sessionCookie` | A Firebase session cookie string to verify and parse. | | `checkRevoked` | A boolean indicating whether to check if the tokens were revoked. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| **Returns** | A task that completes with a [FirebaseToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token) representing the verified and decoded session cookie. |