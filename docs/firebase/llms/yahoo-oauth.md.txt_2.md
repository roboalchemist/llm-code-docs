# Source: https://firebase.google.com/docs/auth/cpp/yahoo-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like
Yahoo by integrating web-based generic OAuth Login into your app using the
Firebase SDK to carry out the end to end sign-in flow. Since this flow requires
the use of the phone-based Firebase SDKs, it is only supported on Android and
Apple platforms.

## Before you begin

1. [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup#note_select_platform).
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
3. On the **Sign in method** tab, enable the **Yahoo** provider.
4. Add the **Client ID** and **Client Secret** from that provider's developer console to the provider configuration:
   1. To register a Yahoo OAuth client, follow the Yahoo developer
      documentation on [registering a web application with Yahoo](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).

      Be sure to select the two OpenID Connect API permissions:
      `profile` and `email`.
   2. When registering apps with these providers, be sure to register the `*.firebaseapp.com` domain for your project as the redirect domain for your app.
5. Click **Save**.

## Access the `firebase::auth::Auth` class

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

## Handle the sign-in flow with the Firebase SDK

To handle the sign-in flow with the Firebase SDK, follow these steps:

1. Construct an instance of a `FederatedOAuthProviderData` configured with
   the provider ID appropriate for Yahoo.

       firebase::auth::FederatedOAuthProviderData
           provider_data(firebase::auth::YahooAuthProvider::kProviderId);

2. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

       // Prompt user to re-authenticate to Yahoo.
       provider_data.custom_parameters["prompt"] = "login";

       // Localize to French.
       provider_data.custom_parameters["language"] = "fr";

   For the parameters Yahoo supports, see the
   [Yahoo OAuth documentation](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).
   Note that you can't pass Firebase-required parameters with
   `custom_parameters()`. These parameters are **client_id** ,
   **redirect_uri** , **response_type** , **scope** and **state**.
3. **Optional** : Specify additional OAuth 2.0 scopes beyond `profile` and
   `email` that you want to request from the authentication provider. If your
   application requires access to private user data from Yahoo APIs, you'll
   need to request permissions to Yahoo APIs under **API Permissions** in the
   Yahoo developer console. Requested OAuth scopes must be exact matches to the
   preconfigured ones in the app's API permissions. For example if, read/write
   access is requested to user contacts and preconfigured in the app's API
   permissions, `sdct-w` has to be passed instead of the readonly OAuth scope
   `sdct-r`. Otherwise,the flow will fail and an error would be shown to the
   end user.

       // Request access to Yahoo Mail API.
       provider_data.scopes.push_back("mail-r");
       // This must be preconfigured in the app's API permissions.
       provider_data.scopes.push_back("sdct-w");

   To learn more, refer to the
   [Yahoo scopes documentation](https://developer.yahoo.com/oauth2/guide/yahoo_scopes/).
4. Once your provider data has been configured, use it to create a
   FederatedOAuthProvider.

       // Construct a FederatedOAuthProvider for use in Auth methods.
       firebase::auth::FederatedOAuthProvider provider(provider_data);

5. Authenticate with Firebase using the Auth provider object. Note that unlike
   other FirebaseAuth operations, this will take control of your UI by popping
   up a web view in which the user can enter their credentials.

   To start the sign in flow, call `SignInWithProvider`:

       firebase::Future<firebase::auth::AuthResult> result =
         auth->SignInWithProvider(provider_data);

   Your application may then wait or [register a callback on the Future](https://firebase.google.com/docs/auth/cpp/yahoo-oauth#register_callback_on_future).
6. While the above examples focus on sign-in flows, you also have the
   ability to link a Yahoo provider to an existing user using
   `LinkWithProvider`. For example, you can link multiple
   providers to the same user allowing them to sign in with either.

       firebase::Future<firebase::auth::AuthResult> result = user.LinkWithProvider(provider_data);

7. The same pattern can be used with `ReauthenticateWithProvider` which can be
   used to retrieve fresh credentials for sensitive operations that require
   recent login.

       firebase::Future<firebase::auth::AuthResult> result =
         user.ReauthenticateWithProvider(provider_data);

   Your application may then wait or [register a callback on
   the Future](https://firebase.google.com/docs/auth/cpp/yahoo-oauth#register_callback_on_future).

## Advanced: Handle the sign-in flow manually

Unlike other OAuth providers supported by Firebase such as Google, Facebook,
and Twitter, where sign-in can directly be achieved with OAuth access token
based credentials, Firebase Auth does not support the same capability for
providers such as Yahoo due to the inability of the Firebase
Auth server to verify the audience of Yahoo OAuth access tokens.
This is a critical security requirement and could expose applications and
websites to replay attacks where a Yahoo OAuth access token obtained for
one project (attacker) can be used to sign in to another project (victim).
Instead, Firebase Auth offers the ability to handle the entire OAuth flow and
the authorization code exchange using the OAuth client ID and secret
configured in the Firebase Console. As the authorization code can only be used
in conjunction with a specific client ID/secret, an authorization code
obtained for one project cannot be used with another.

If these providers are required to be used in unsupported environments, a
third party OAuth library and
[Firebase custom authentication](https://firebase.google.com/docs/auth/admin/create-custom-tokens)
would need to be used. The former is needed to authenticate with the provider
and the latter to exchange the provider's credential for a custom token.

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