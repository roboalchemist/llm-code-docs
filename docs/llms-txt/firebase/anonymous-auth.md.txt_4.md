# Source: https://firebase.google.com/docs/auth/cpp/anonymous-auth.md.txt

You can use Firebase Authentication to create and use temporary anonymous accounts
to authenticate with Firebase. These temporary anonymous accounts can be used to
allow users who haven't yet signed up to your app to work with data protected
by security rules. If an anonymous user decides to sign up to your app, you can
[link their sign-in credentials to the anonymous
account](https://firebase.google.com/docs/auth/cpp/account-linking) so that they can continue to work with their protected data in
future sessions.

## Before you begin

1. [Add Firebase to your C++
   project](https://firebase.google.com/docs/cpp/setup#note_select_platform).
2. If you haven't yet connected your app to your Firebase project, do so from the [Firebase console](https://console.firebase.google.com/).
3. Enable anonymous auth:
   1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
   2. On the **Sign-in Methods** page, enable the **Anonymous** sign-in method.
   3. **Optional** : If you've upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can enable automatic clean-up. When you enable this setting, anonymous accounts older than 30 days will be automatically deleted. In projects with automatic clean-up enabled, anonymous authentication will no longer count toward usage limits or billing quotas. See [Automatic clean-up](https://firebase.google.com/docs/auth/cpp/anonymous-auth#auto-cleanup).

## Authenticate with Firebase anonymously

When a signed-out user uses an app feature that requires authentication with
Firebase, sign in the user anonymously by completing the following steps:
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

- Call `Auth::SignInAnonymously`.

  ```c++
  firebase::Future<firebase::auth::AuthResult> result =
      auth->SignInAnonymously();
  ```
- If your program has an update loop that runs regularly (say at 30 or 60 times per second), you can check the results once per update with `Auth::SignInAnonymouslyLastResult`:

  ```c++
  firebase::Future<firebase::auth::AuthResult> result =
      auth->SignInAnonymouslyLastResult();
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
  Future](https://firebase.google.com/docs/auth/cpp/anonymous-auth#register_callback_on_future).
To protect your project from abuse, Firebase limits the number of new email/password and anonymous sign-ups that your application can have from the same IP address in a short period of time. You can request and schedule temporary changes to this quota from the [Firebase console](https://console.firebase.google.com/project/_/authentication/providers).

## Convert an anonymous account to a permanent account

- When an anonymous user signs up to your app, you might want to allow them to continue their work with their new account---for example, you might want to make the items the user added to their shopping cart before they signed up available in their new account's shopping cart. To do so, complete the following steps:
  1. When the user signs up, complete the sign-in flow for the user's authentication provider up to, but not including, calling one of the `Auth::SignInWith` methods. For example, get the user's Google ID token, Facebook access token, or email address and password.
  2. Get an `auth::Credential` for the new authentication provider:

     **Google Sign-In**

     ```c++
     firebase::auth::Credential credential =
         firebase::auth::GoogleAuthProvider::GetCredential(google_id_token,
                                                           nullptr);
     ```
     **Facebook Login**

     ```c++
     firebase::auth::Credential credential =
         firebase::auth::FacebookAuthProvider::GetCredential(access_token);
     ```
     **Email-password sign-in**

     ```c++
     firebase::auth::Credential credential =
         firebase::auth::EmailAuthProvider::GetCredential(email, password);
     ```
  3. Pass the `auth::Credential` object to the sign-in user's
     `LinkWithCredential` method:

     ```c++
     // Link the new credential to the currently active user.
     firebase::auth::User current_user = auth->current_user();
     firebase::Future<firebase::auth::AuthResult> result =
         current_user.LinkWithCredential(credential);
     ```
- If the call to `LinkWithCredential` succeeds, the user's new account can access the anonymous account's Firebase data.

> [!NOTE]
> This technique can also be used to [link any two accounts](https://firebase.google.com/docs/auth/cpp/account-linking).

## Automatic clean-up

- If you've upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can enable automatic clean-up in the Firebase console. When you enable this feature you allow Firebase to automatically delete anonymous accounts older than 30 days. In projects with automatic clean-up enabled, anonymous authentication will not count toward usage limits or billing quotas.
  - Any anonymous accounts created after enabling automatic clean-up might be automatically deleted any time after 30 days post-creation.
  - Existing anonymous accounts will be eligible for automatic deletion 30 days after enabling automatic clean-up.
  - If you turn automatic clean-up off, any anonymous accounts scheduled to be deleted will remain scheduled to be deleted.
  - If you "upgrade" an anonymous account by linking it to any sign-in method, the account will not get automatically deleted.
- If you want to see how many users will be affected before you enable this feature, and you've upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can filter by `is_anon` in [Cloud
  Logging](https://cloud.google.com/logging/docs).

## Next steps

- Now that users can authenticate with Firebase, you can control their access to data in your Firebase database using [Firebase rules](https://firebase.google.com/docs/database/security#section-authorization).