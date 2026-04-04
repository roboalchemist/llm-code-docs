# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth.md.txt

# firebase::auth::Auth Class Reference

# firebase::auth::Auth


`#include <auth.h>`

Firebase authentication object.

## Summary

[firebase::auth::Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) is the gateway to the Firebase authentication API. With it, you can reference [firebase::auth::User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) objects to manage user accounts and credentials.

Each [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) has up to one [firebase::auth::Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) class. You acquire the [firebase::auth::Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) class through the static function [firebase::auth::Auth::GetAuth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a976bf63368d33aae7857f66dd3babf67).

For example:

```c++
// Get the Auth class for your App.
firebase::auth::Auth* auth = firebase::auth::Auth::GetAuth(app);

// Request anonymous sign-in and wait until asynchronous call completes.
firebase::Future<firebase::auth::AuthResult> sign_in_future =
    auth->SignInAnonymously();
while(sign_in_future.status() == firebase::kFutureStatusPending) {
    // when polling, like this, make sure you service your platform's
    // message loop
    // see https://github.com/firebase/quickstart-cpp for a sample
    ProcessEvents(300);
    std::cout << "Signing in...\n";
}

const firebase::auth::AuthError error =
    static_cast<firebase::auth::AuthError>(sign_in_future.error());
if (error != firebase::auth::kAuthErrorNone) {
    std::cout << "Sign in failed with error '"
        << sign_in_future.error_message() << "'\n";
} else {
    firebase::auth::User user = sign_in_future.result()->user;
    // is_anonymous from Anonymous
    std::cout << "Signed in as "
        << (user.is_anonymous() ? "an anonymous" : "a non-anonymous")
        << " user\n";
}
```

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1af3758e9f3edbcba4c51a0404e9eddfdb()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1add18126b0c434561cb48c82354ce5b87(https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth-state-listener#classfirebase_1_1auth_1_1_auth_state_listener *listener)` | `void` Registers a listener to changes in the authentication state. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1adbc02357322542222894dfc7b84e4b4f(https://firebase.google.com/docs/reference/cpp/class/firebase/auth/id-token-listener#classfirebase_1_1auth_1_1_id_token_listener *listener)` | `void` Registers a listener to changes in the ID token state. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a5b1cad2175bb17aaf4c9838cb56af4d8(const char *email, const char *password)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Creates, and on success, logs in a user with the given email address and password. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1adef44d3093f493055886b1126ecb365e() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Get results of the most recent call to CreateUserWithEmailAndPassword. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a7d5e2204e48a52a6b784a0e924fdcdbf(const char *email)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth/fetch-providers-result#structfirebase_1_1auth_1_1_auth_1_1_fetch_providers_result >` Asynchronously requests the IDPs (identity providers) that can be used for the given email address. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1aa25144a43db917188b22253b0b95d1d9() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth/fetch-providers-result#structfirebase_1_1auth_1_1_auth_1_1_fetch_providers_result >` Get results of the most recent call to FetchProvidersForEmail. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a12df4e097c2af0901118401340562ef2(https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth-state-listener#classfirebase_1_1auth_1_1_auth_state_listener *listener)` | `void` Unregisters a listener of authentication changes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1aee7d9bdcab446be77f1f2c028cc6d663(https://firebase.google.com/docs/reference/cpp/class/firebase/auth/id-token-listener#classfirebase_1_1auth_1_1_id_token_listener *listener)` | `void` Unregisters a listener of ID token changes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a3be7e6883714965eab50a73feab4a63d(const char *email)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Initiates a password reset for the given email address. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a1571493550b41022fad6338f21ceab7a() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Get results of the most recent call to SendPasswordResetEmail. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a0e830c3a1efa725996220604710fe5dc(const https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential & credential)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Asynchronously logs into Firebase with the given credentials. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a20b254d417641c2ed77c18bf3b2a54e1() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Get results of the most recent call to SignInAndRetrieveDataWithCredential. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1abb653e75f247a92a64d76b76bac175e4()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Asynchronously creates and becomes an anonymous user. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a6ffafdb61185595ac8d554cbe8a19e75() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Get results of the most recent call to SignInAnonymously. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a16d92dd01886a3327afe08f65e0fa2b8(const https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential & credential)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user >` Convenience method for SignInAndRetrieveDataWithCredential that doesn't return additional identity provider data. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1aea2341ffffb227e7fb9d8fa9f75b5ce2(const char *custom_token)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Asynchronously logs into Firebase with the given [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) token. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a74436a197e81e0737375192653125123() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Get results of the most recent call to SignInWithCustomToken. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a5c4056cea946051aa3e14fdbf8fed7e7(const char *email, const char *password)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Signs in using provided email address and password. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a1b7a7deb17be4099289bad2cc633c019() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Get results of the most recent call to SignInWithEmailAndPassword. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a91a15f187adad095df0eb5be3835583a(https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider#classfirebase_1_1auth_1_1_federated_auth_provider *provider)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result >` Sign-in a user authenticated via a federated auth provider. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1adfd6981dea2ba8a193af82af02907aad()` | `void` Removes any existing authentication credentials from this client. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a037aa6dd1511624594eccf39ca599f6d()` | `void` Sets the user-facing language code to be the default app language. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a67ba0cab97d1b41e14c1d8bd302902b8(std::string host, uint32_t port)` | `void` Modify this [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) instance to communicate with the Firebase Authentication emulator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a837e1ae0664a1637493ab73b8cc94b7a()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app &` Gets the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this auth object is connected to. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a0684f7f576d13105298c1282d05fd0b9()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user` Synchronously gets the cached current user, or returns an object where is_valid() == false if there is none. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a3ddcd814ed2511eb7fc886613cfcb261() const ` | `std::string` The current user language code. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a7fff6c573b749adcab26af1d3a398224(const char *language_code)` | `void` Sets the user-facing language code for auth operations that can be internationalized, such as FirebaseUser.sendEmailVerification(). |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a976bf63368d33aae7857f66dd3babf67(https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth *` Returns the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) object for an [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |

| ### Structs ||
|---|---|
| [firebase::auth::Auth::FetchProvidersResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth/fetch-providers-result) | Results of calls FetchProvidersForEmail. |

## Public functions

### AddAuthStateListener

```c++
void AddAuthStateListener(
  AuthStateListener *listener
)
```
Registers a listener to changes in the authentication state.

There can be more than one listener registered at the same time. The listeners are called asynchronously, possibly on a different thread.

Authentication state changes are:

- Right after the listener has been registered
- When a user signs in
- When the current user signs out
- When the current user changes

<br />

It is a recommended practice to always listen to sign-out events, as you may want to prompt the user to sign in again and maybe restrict the information or actions they have access to.

Use RemoveAuthStateListener to unregister a listener.


> [!NOTE]
> **Note:** The caller owns `listener` and is responsible for destroying it. When `listener` is destroyed, or when [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) is destroyed, RemoveAuthStateListener is called automatically.

<br />

### AddIdTokenListener

```c++
void AddIdTokenListener(
  IdTokenListener *listener
)
```
Registers a listener to changes in the ID token state.

There can be more than one listener registered at the same time. The listeners are called asynchronously, possibly on a different thread.

Authentication state changes are:

- Right after the listener has been registered
- When a user signs in
- When the current user signs out
- When the current user changes
- When there is a change in the current user's token

<br />

Use RemoveIdTokenListener to unregister a listener.


> [!NOTE]
> **Note:** The caller owns `listener` and is responsible for destroying it. When `listener` is destroyed, or when [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) is destroyed, RemoveIdTokenListener is called automatically.

<br />

### CreateUserWithEmailAndPassword

```c++
Future< AuthResult > CreateUserWithEmailAndPassword(
  const char *email,
  const char *password
)
```
Creates, and on success, logs in a user with the given email address and password.

An error is returned when account creation is unsuccessful (due to another existing account, invalid password, etc.).

### CreateUserWithEmailAndPasswordLastResult

```c++
Future< AuthResult > CreateUserWithEmailAndPasswordLastResult() const 
```
Get results of the most recent call to CreateUserWithEmailAndPassword.

### FetchProvidersForEmail

```c++
Future< FetchProvidersResult > FetchProvidersForEmail(
  const char *email
)
```
Asynchronously requests the IDPs (identity providers) that can be used for the given email address.

Useful for an "identifier-first" login flow.

The following sample code illustrates a possible login screen that allows the user to pick an identity provider.

```c++
// This function is called every frame to display the login screen.
// Returns the identity provider name, or "" if none selected.
const char* DisplayIdentityProviders(firebase::auth::Auth& auth,
                                     const char* email) {
  // Get results of most recent call to FetchProvidersForEmail().
  firebase::Future<firebase::auth::Auth::FetchProvidersResult> future =
      auth.FetchProvidersForEmailLastResult();
  const firebase::auth::Auth::FetchProvidersResult* result =
      future.result();

  // Header.
  ShowTextBox("Sign in %s", email);

  // Fetch providers from the server if we need to.
  const bool refetch =
      future.status() == firebase::kFutureStatusInvalid ||
      (result != nullptr && strcmp(email, result->email.c_str()) != 0);
  if (refetch) {
    auth.FetchProvidersForEmail(email);
  }

  // Show a waiting icon if we're waiting for the asynchronous call to
  // complete.
  if (future.status() != firebase::kFutureStatusComplete) {
    ShowImage("waiting icon");
    return "";
  }

  // Show error code if the call failed.
  if (future.error() != firebase::auth::kAuthErrorNone) {
    ShowTextBox("Error fetching providers: %s", future.error_message());
  }

  // Show a button for each provider available to this email.
  // Return the provider for the button that's pressed.
  for (size_t i = 0; i < result->providers.size(); ++i) {
    const bool selected = ShowTextButton(result->providers[i].c_str());
    if (selected) return result->providers[i].c_str();
  }
  return "";
}
```

<br />

### FetchProvidersForEmailLastResult

```c++
Future< FetchProvidersResult > FetchProvidersForEmailLastResult() const 
```
Get results of the most recent call to FetchProvidersForEmail.

### RemoveAuthStateListener

```c++
void RemoveAuthStateListener(
  AuthStateListener *listener
)
```
Unregisters a listener of authentication changes.

Listener must previously been added with AddAuthStateListener.

Note that listeners unregister themselves automatically when they are destroyed, and the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) class unregisters its listeners when the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) class itself is destroyed, so this function does not normally need to be called explicitly.

### RemoveIdTokenListener

```c++
void RemoveIdTokenListener(
  IdTokenListener *listener
)
```
Unregisters a listener of ID token changes.

Listener must previously been added with AddIdTokenListener.

Note that listeners unregister themselves automatically when they are destroyed, and the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) class unregisters its listeners when the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) class itself is destroyed, so this function does not normally need to be called explicitly.

### SendPasswordResetEmail

```c++
Future< void > SendPasswordResetEmail(
  const char *email
)
```
Initiates a password reset for the given email address.

If the email address is not registered, then the returned task has a status of IsFaulted.

The following sample code illustrating a possible password reset flow. Like in the Anonymous Sign-In example above, the ResetPasswordScreen() function is called once per frame (say 30 times per second).

No state is persisted by the caller in this example. The state of the most recent calls are instead accessed through calls to functions like auth.SendPasswordResetEmailLastResult().

```c++
const char* ImageNameForStatus(const firebase::FutureBase& future) {
  assert(future.status() != firebase::kFutureStatusInvalid);
  return future.status() == firebase::kFutureStatusPending
             ? "waiting icon"
             : future.error() == firebase::auth::kAuthErrorNone
                  ? "checkmark icon"
                  : "x mark icon";
}

// This function is called once per frame.
void ResetPasswordScreen(firebase::auth::Auth& auth) {
  // Gather email address.
  // ShowInputBox() returns a value when `enter` is pressed.
  const std::string email = ShowInputBox("Enter e-mail");
  if (email != "") {
    auth.SendPasswordResetEmail(email.c_str());
  }

  // Show checkmark, X-mark, or waiting icon beside the
  // email input box, to indicate if email has been sent.
  firebase::Future send_future =
      auth.SendPasswordResetEmailLastResult();
  ShowImage(ImageNameForStatus(send_future));

  // Display error message if the e-mail could not be sent.
  if (send_future.status() == firebase::kFutureStatusComplete &&
      send_future.error() != firebase::auth::kAuthErrorNone) {
    ShowTextBox(send_future.error_message());
  }
}
```

<br />

### SendPasswordResetEmailLastResult

```c++
Future< void > SendPasswordResetEmailLastResult() const 
```
Get results of the most recent call to SendPasswordResetEmail.

### SignInAndRetrieveDataWithCredential

```c++
Future< AuthResult > SignInAndRetrieveDataWithCredential(
  const Credential & credential
)
```
Asynchronously logs into Firebase with the given credentials.

For example, the credential could wrap a Facebook login access token or a Twitter token/token-secret pair.

The [AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result) contains both a reference to the [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) (which is_valid() will return false if the sign in failed), and [AdditionalUserInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info), which holds details specific to the Identity Provider used to sign in.

An error is returned if the token is invalid, expired, or otherwise not accepted by the server.

### SignInAndRetrieveDataWithCredentialLastResult

```c++
Future< AuthResult > SignInAndRetrieveDataWithCredentialLastResult() const 
```
Get results of the most recent call to SignInAndRetrieveDataWithCredential.

### SignInAnonymously

```c++
Future< AuthResult > SignInAnonymously()
```
Asynchronously creates and becomes an anonymous user.

If there is already an anonymous user signed in, that user will be returned instead. If there is any other existing user, that user will be signed out.

The following sample code illustrates the sign-in flow that might be used by a game or some other program with a regular (for example, 30Hz) update loop.

The sample calls SignIn() every frame. We don't maintain our own Futures but instead call [SignInAnonymouslyLastResult()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a6ffafdb61185595ac8d554cbe8a19e75) to get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) of our most recent call.


```c++
// Try to ensure that we get logged in.
// This function is called every frame.
bool SignIn(firebase::auth::Auth& auth) {
  // Grab the result of the latest sign-in attempt.
  firebase::Future<firebase::auth::AuthResult> future =
      auth.SignInAnonymouslyLastResult();

  // If we're in a state where we can try to sign in, do so.
  if (future.status() == firebase::kFutureStatusInvalid ||
      (future.status() == firebase::kFutureStatusComplete &&
       future.error() != firebase::auth::kAuthErrorNone)) {
    auth.SignInAnonymously();
  }

  // We're signed in if the most recent result was successful.
  return future.status() == firebase::kFutureStatusComplete &&
         future.error() == firebase::auth::kAuthErrorNone;
}
```

<br />

### SignInAnonymouslyLastResult

```c++
Future< AuthResult > SignInAnonymouslyLastResult() const 
```
Get results of the most recent call to SignInAnonymously.

### SignInWithCredential

```c++
Future< User > SignInWithCredential(
  const Credential & credential
)
```
Convenience method for SignInAndRetrieveDataWithCredential that doesn't return additional identity provider data.

### SignInWithCustomToken

```c++
Future< AuthResult > SignInWithCustomToken(
  const char *custom_token
)
```
Asynchronously logs into Firebase with the given [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) token.

An error is returned if the token is invalid, expired or otherwise not accepted by the server.

### SignInWithCustomTokenLastResult

```c++
Future< AuthResult > SignInWithCustomTokenLastResult() const 
```
Get results of the most recent call to SignInWithCustomToken.

### SignInWithEmailAndPassword

```c++
Future< AuthResult > SignInWithEmailAndPassword(
  const char *email,
  const char *password
)
```
Signs in using provided email address and password.

An error is returned if the password is wrong or otherwise not accepted by the server.

### SignInWithEmailAndPasswordLastResult

```c++
Future< AuthResult > SignInWithEmailAndPasswordLastResult() const 
```
Get results of the most recent call to SignInWithEmailAndPassword.

### SignInWithProvider

```c++
Future< AuthResult > SignInWithProvider(
  FederatedAuthProvider *provider
)
```
Sign-in a user authenticated via a federated auth provider.


> [!NOTE]
> **Note:** : This operation is supported only on iOS, tvOS and Android platforms. On other platforms this method will return a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) with a preset error code: kAuthErrorUnimplemented.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `provider` | Contains information on the provider to authenticate with. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) with the result of the sign-in request. |

### SignOut

```c++
void SignOut()
```
Removes any existing authentication credentials from this client.

This function always succeeds.

### UseAppLanguage

```c++
void UseAppLanguage()
```
Sets the user-facing language code to be the default app language.

This uses a language associated with the device's locale data. On desktop this will set the language code to the Firebase service's default. You may subsequently customize the language code again by invoking [set_language_code()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a7fff6c573b749adcab26af1d3a398224).

### UseEmulator

```c++
void UseEmulator(
  std::string host,
  uint32_t port
)
```
Modify this [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) instance to communicate with the Firebase Authentication emulator.

### app

```c++
App & app()
```
Gets the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this auth object is connected to.

### current_user

```c++
User current_user()
```
Synchronously gets the cached current user, or returns an object where is_valid() == false if there is none.


> [!NOTE]
> **Note:** This function may block and wait until the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) instance finishes loading the saved user's state. This should only happen for a short time after the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) instance is created.

<br />

### language_code

```c++
std::string language_code() const 
```
The current user language code.

This can be set to the app's current language by calling set_language_code. The string must be a language code that follows BCP 47. This will return an empty string if the app default language code is being used.

### set_language_code

```c++
void set_language_code(
  const char *language_code
)
```
Sets the user-facing language code for auth operations that can be internationalized, such as FirebaseUser.sendEmailVerification().

This language code should follow the conventions defined by the IETF in BCP 47.

### \~Auth

```c++
 ~Auth()
```

## Public static functions

### GetAuth

```c++
Auth * GetAuth(
  App *app,
  InitResult *init_result_out
)
```
Returns the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) object for an [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).

Creates the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) if required.

To get the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) object for the default app, use, GetAuth(GetDefaultFirebaseApp());

If the library [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) fails to initialize, init_result_out will be written with the result status (if a pointer is given).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | The [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to use for the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) object. | | `init_result_out` | Optional: If provided, write the init result here. Will be set to kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if Google Play services is not available on the current device. | |