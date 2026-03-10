# Source: https://firebase.google.com/docs/auth/cpp/custom-auth.md.txt

You can integrate Firebase Authentication with a custom authentication system by
modifying your authentication server to produce custom signed tokens when a user
successfully signs in. Your app receives this token and uses it to authenticate
with Firebase.

## Before you begin

1. [Add Firebase to your C++
   project](https://firebase.google.com/docs/cpp/setup#note_select_platform).
2. Get your project's server keys:
   1. Go to the [Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk) page in your project's settings.
   2. Click *Generate New Private Key* at the bottom of the *Firebase Admin SDK* section of the *Service Accounts* page.
   3. The new service account's public/private key pair is automatically saved on your computer. Copy this file to your authentication server.

## Authenticate with Firebase

The `Auth` class is the gateway for all API calls.

1. Add the Auth and App header files:

   ```c++
   #include "firebase/app.h"
   #include "firebase/auth.h"
   ```
2. In your initialization code, create a [`firebase::App`](https://firebase.google.com/docs/reference/cpp/class/firebase/app) class.

   ```c++
   #if defined(__ANDROID__)
     firebase::App* app =
         firebase::App::Create(firebase::AppOptions(), my_jni_env, my_activity);
   #else
     firebase::App* app = firebase::App::Create(firebase::AppOptions());
   #endif  // defined(__ANDROID__)
   ```
3. Acquire the `firebase::auth::Auth` class for your `firebase::App`. There is a one-to-one mapping between `App` and `Auth`.

   ```c++
   firebase::auth::Auth* auth = firebase::auth::Auth::GetAuth(app);
   ```

Call `Auth::SignInWithCustomToken` with the token from your authentication server.

1. When users sign in to your app, send their sign-in credentials (for example, their username and password) to your authentication server. Your server checks the credentials and returns a [custom token](https://firebase.google.com/docs/auth/admin/create-custom-tokens) if they are valid.
2. After you receive the custom token from your authentication server, pass it to `Auth::SignInWithCustomToken` to sign in the user:

   ```c++
   firebase::Future<firebase::auth::AuthResult> result =
       auth->SignInWithCustomToken(custom_token);
   ```
3. If your program has an update loop that runs regularly (say at 30 or 60 times per second), you can check the results once per update with `Auth::SignInWithCustomTokenLastResult`:

   ```c++
   firebase::Future<firebase::auth::AuthResult> result =
       auth->SignInWithCustomTokenLastResult();
   if (result.status() == firebase::kFutureStatusComplete) {
     if (result.error() == firebase::auth::kAuthErrorNone) {
       firebase::auth::AuthResult auth_result = *result.result();
       printf("Sign in succeeded for `%s`\n",
              auth_result.user.display_name().c_str());
     } else {
       printf("Sign in failed with error '%s'\n", result.error_message());
     }
   }
   ```
   Or, if your program is event driven, you may prefer to [register a callback on the
   Future](https://firebase.google.com/docs/auth/cpp/custom-auth#register_callback_on_future).

## Next steps

After a user signs in for the first time, a new user account is created and
linked to the credentials---that is, the user name and password, phone
number, or auth provider information---the user signed in with. This new
account is stored as part of your Firebase project, and can be used to identify
a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the
  [`firebase::auth::User`](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user) object:

  ```c++
  firebase::auth::User user = auth->current_user();
  if (user.is_valid()) {
    std::string name = user.display_name();
    std::string email = user.email();
    std::string photo_url = user.photo_url();
    // The user's ID, unique to the Firebase project.
    // Do NOT use this value to authenticate with your backend server,
    // if you have one. Use firebase::auth::User::Token() instead.
    std::string uid = user.uid();
  }
  ```
- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/cpp/account-linking)

To sign out a user, call [`SignOut()`](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#signout):

```c++
auth->SignOut();
```