# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth.md.txt

# Firebase.Auth.FirebaseAuth Class Reference

# Firebase.Auth.FirebaseAuth

[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) authentication object.

## Summary

[Firebase.Auth.FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) is the gateway to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) authentication API. With it, you can reference [Firebase.Auth.FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) objects to manage user accounts and credentials.

Each [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) has up to one [Firebase.Auth.FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) class. You acquire the [Firebase.Auth.FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) class through the static function [Firebase.Auth.FirebaseAuth.GetAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1afcf28ace32a24ce2b1a360d39364dcbc).

For example:

```c#
// Get the Auth class for your App.
Firebase.Auth.FirebaseAuth auth = Firebase.Auth.FirebaseAuth.GetAuth(app);

// Request anonymous sign-in and wait until asynchronous call completes.
auth.SignInAnonymouslyAsync().ContinueWith((authTask) => {
// Print sign in results.
  if (authTask.IsCanceled) {
    DebugLog("Sign-in canceled.");
  } else if (authTask.IsFaulted) {
    DebugLog("Sign-in encountered an error.");
    DebugLog(authTask.Exception.ToString());
  } else if (authTask.IsCompleted) {
    Firebase.Auth.User user = authTask.Result;
    DebugLog(String.Format("Signed in as {0} user.",
        user.Anonymous ? "an anonymous" : "a non-anonymous"));
    DebugLog("Signing out.");
    auth.SignOut();
});
```

<br />

### Inheritance

Inherits from: SystemIDisposable

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1affef0fac66b90f1e06b4c1eb08dcb8c2` | `https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app` Get the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) associated with this object. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a9e2b7cd169e0c1ab8d764ac9e028de3d` | `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user` Synchronously gets the cached current user, or null if there is none. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a7a29c5b4356dde3a3610d761440c9936` | `static https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth` Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) associated with FirebaseApp.DefaultApp. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a9702ee15ade6886eb9cbfd6537ab5966` | `System.EventHandler` Event raised on ID token changes. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1ac691cb9d03d6e36f1b435b6517fcb02b` | `System.String` The user-facing language code for auth operations that can be internationalized, such as FirebaseUser.sendEmailVerification(). |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a849f6a1fbcc42d7f470bdf33a98654fd` | `System.EventHandler` Event raised on changes in the authentication state. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1aec51af9fd5200d8e1c98f850e7fd964a(string email, string password)` | `async System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result >` Creates, and on success, logs in a user with the given email address and password. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1aadfcf3a12c4c927d10cd80f21991ae3e()` | `void` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a2c05d831e86f6c0a1932edaf1f1d5693(bool disposing)` | `void` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a2a9b55828bc18bd68a114b3acafea342(string email)` | `System.Threading.Tasks.Task< System.Collections.Generic.IEnumerable< string > >` Asynchronously requests the IDPs (identity providers) that can be used for the given email address. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a95342b10a704eeb8cc75297c7966798d(string email)` | `System.Threading.Tasks.Task` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a14887e52bbe4c7611b3658bf380d8fa0(https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential credential)` | `async System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result >` Asynchronously logs into [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) with the given credentials. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a1dea25b66866b4cd9205ad6f0f5eb8d4()` | `async System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result >` Asynchronously creates and becomes an anonymous user. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a836d7febdaa2f3c789345da1c74f5e15(https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential credential)` | `async System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user >` Asynchronously logs into [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) with the given `https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth` token. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1ab07cc925a609c5fe266218b31c523f75(string token)` | `async System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result >` Asynchronously logs into [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) with the given [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) token. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1aec9d3f4a0567fce8244675e4def1218c(string email, string password)` | `async System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result >` Signs in using provided email address and password. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a3626246ac8e77bc3dbd4fd9abb198f8c(https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-auth-provider#class_firebase_1_1_auth_1_1_federated_auth_provider provider)` | `async System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result >` Sign-in a user authenticated via a federated auth provider. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1ab53ba445fd7770ee2e9af595258b0231()` | `void` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1a87307a257ea553ed65c30b45e743dc2e()` | `void` |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth_1afcf28ace32a24ce2b1a360d39364dcbc(https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app app)` | `https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth` Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) object for an App. |

## Properties

### App

```c#
FirebaseApp App
```
Get the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) associated with this object.

<br />

| Details ||
|---|---|
| **Returns** | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) associated with this object. |

### CurrentUser

```c#
FirebaseUser CurrentUser
```
Synchronously gets the cached current user, or null if there is none.


> [!NOTE]
> **Note:** Accessing this property may block and wait until the [FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) instance finishes loading the saved user's state. This should only happen for a short period of time after the [FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) instance is created.

<br />

### DefaultInstance

```c#
static FirebaseAuth DefaultInstance
```
Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) associated with FirebaseApp.DefaultApp.

[FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) will be created if required.

<br />

| Details ||
|---|---|
| Exceptions | |---|---| | `InitializationException` | Thrown with the invalid InitResult if initialization failed. | |

### IdTokenChanged

```c#
System.EventHandler IdTokenChanged
```
Event raised on ID token changes.

Authentication ID token changes are:

- Right after the listener has been registered
- When a user signs in
- When the current user signs out
- When the current user changes
- When there is a change in the current user's token

<br />

### LanguageCode

```c#
System.String LanguageCode
```
The user-facing language code for auth operations that can be internationalized, such as FirebaseUser.sendEmailVerification().

This language code should follow the conventions defined by the IETF in BCP 47.

### StateChanged

```c#
System.EventHandler StateChanged
```
Event raised on changes in the authentication state.

Authentication state changes are:

- Right after the listener has been registered
- When a user signs in
- When the current user signs out
- When the current user changes

<br />

It is a recommended practice to always listen to sign-out events, as you may want to prompt the user to sign in again and maybe restrict the information or actions they have access to.

## Public functions

### CreateUserWithEmailAndPasswordAsync

```c#
async System.Threading.Tasks.Task< AuthResult > CreateUserWithEmailAndPasswordAsync(
  string email,
  string password
)
```
Creates, and on success, logs in a user with the given email address and password.

An error is returned when account creation is unsuccessful (due to another existing account, invalid password, etc.).

### Dispose

```c#
void Dispose()
```

### Dispose

```c#
void Dispose(
  bool disposing
)
```

### FetchProvidersForEmailAsync

```c#
System.Threading.Tasks.Task< System.Collections.Generic.IEnumerable< string > > FetchProvidersForEmailAsync(
  string email
)
```
Asynchronously requests the IDPs (identity providers) that can be used for the given email address.

Useful for an "identifier-first" login flow.


```c#
// Print out all available providers for a given email.
void DisplayIdentityProviders(Firebase.Auth.FirebaseAuth auth,
                              String email) {
  auth.FetchProvidersForEmailAsync().ContinueWith((authTask) => {
    if (authTask.IsCanceled) {
      DebugLog("Provider fetch canceled.");
    } else if (authTask.IsFaulted) {
      DebugLog("Provider fetch encountered an error.");
      DebugLog(authTask.Exception.ToString());
    } else if (authTask.IsCompleted) {
      DebugLog("Email Providers:");
      foreach (string provider in authTask.result) {
        DebugLog(provider);
      }
    }
  });
}
```

<br />

### SendPasswordResetEmailAsync

```c#
System.Threading.Tasks.Task SendPasswordResetEmailAsync(
  string email
)
```

### SignInAndRetrieveDataWithCredentialAsync

```c#
async System.Threading.Tasks.Task< AuthResult > SignInAndRetrieveDataWithCredentialAsync(
  Credential credential
)
```
Asynchronously logs into [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) with the given credentials.

For example, the credential could wrap a Facebook login access token, a Twitter token/token-secret pair).

[AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result) contains both a reference to the [FirebaseUser](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user) (which can be null if the sign in failed), and [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info), which holds details specific to the Identity Provider used to sign in.

An error is returned if the token is invalid, expired, or otherwise not accepted by the server.

### SignInAnonymouslyAsync

```c#
async System.Threading.Tasks.Task< AuthResult > SignInAnonymouslyAsync()
```
Asynchronously creates and becomes an anonymous user.

If there is already an anonymous user signed in, that user will be returned instead. If there is any other existing user, that user will be signed out.

```c#
bool SignIn(Firebase.Auth.FirebaseAuth auth) {
  auth.SignInAnonymouslyAsync().ContinueWith((authTask) => {
    if (authTask.IsCanceled) {
      DebugLog("Anonymous sign in canceled.");
    } else if (authTask.IsFaulted) {
      DebugLog("Anonymous sign in encountered an error.");
      DebugLog(authTask.Exception.ToString());
    } else if (authTask.IsCompleted) {
      DebugLog("Anonymous sign in successful!");
    }
  });
}
```

<br />

### SignInWithCredentialAsync

```c#
async System.Threading.Tasks.Task< FirebaseUser > SignInWithCredentialAsync(
  Credential credential
)
```
Asynchronously logs into [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) with the given `https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth` token.

An error is returned, if the token is invalid, expired or otherwise not accepted by the server.

### SignInWithCustomTokenAsync

```c#
async System.Threading.Tasks.Task< AuthResult > SignInWithCustomTokenAsync(
  string token
)
```
Asynchronously logs into [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) with the given [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) token.

An error is returned, if the token is invalid, expired or otherwise not accepted by the server.

### SignInWithEmailAndPasswordAsync

```c#
async System.Threading.Tasks.Task< AuthResult > SignInWithEmailAndPasswordAsync(
  string email,
  string password
)
```
Signs in using provided email address and password.

An error is returned if the password is wrong or otherwise not accepted by the server.

### SignInWithProviderAsync

```c#
async System.Threading.Tasks.Task< AuthResult > SignInWithProviderAsync(
  FederatedAuthProvider provider
)
```
Sign-in a user authenticated via a federated auth provider.


> [!NOTE]
> **Note:** : This operation is supported only on iOS, tvOS and Android platforms. On other platforms this method will return a Future with a preset error code: kAuthErrorUnimplemented.

<br />

### SignOut

```c#
void SignOut()
```

### UseAppLanguage

```c#
void UseAppLanguage()
```

## Public static functions

### GetAuth

```c#
FirebaseAuth GetAuth(
  FirebaseApp app
)
```
Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) object for an App.

Creates the [FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) if required.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | The [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) to use for the [FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth) object. | |
| Exceptions | |---|---| | `InitializationException` | Thrown with the invalid InitResult if initialization failed. | |