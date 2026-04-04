# Source: https://firebase.google.com/docs/auth/cpp/microsoft-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like
Microsoft Azure Active Directory by integrating web-based generic OAuth Login
into your app using the Firebase SDK to carry out the end to end sign-in flow.
Since this flow requires the use of the phone-based Firebase SDKs, it is only
supported on Android and Apple platforms.

## Before you begin

1. [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup#note_select_platform).
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
3. On the **Sign in method** tab, enable the **Microsoft** provider.
4. Add the **Client ID** and **Client Secret** from that provider's developer console to the provider configuration:
   1. To register a Microsoft OAuth client, follow the instructions in [Quickstart: Register an app with the Azure Active Directory v2.0 endpoint](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-register-an-app). Note that this endpoint supports sign-in using Microsoft personal accounts as well as Azure Active Directory accounts. [Learn more](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview) about Azure Active Directory v2.0.
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
   the provider id appropriate for Microsoft.

       firebase::auth::FederatedOAuthProviderData
           provider_data(firebase::auth::MicrosoftAuthProvider::kProviderId);

2. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

       // Prompt user to re-authenticate to Microsoft.
       provider_data.custom_parameters["prompt"] = "login";

       // Target specific email with login hint.
       provider_data.custom_parameters["login_hint"] =
           "user@firstadd.onmicrosoft.com";

   For the parameters Microsoft supports, see the
   [Microsoft OAuth documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code).
   Note that you can't pass Firebase-required parameters with
   `setCustomParameters()`. These parameters are **client_id** ,
   **response_type** , **redirect_uri** , **state** , **scope** and
   **response_mode**.

   To allow only users from a particular Azure AD tenant to sign
   into the application, either the friendly domain name of the Azure AD tenant
   or the tenant's GUID identifier can be used. This can be done by specifying
   the "tenant" field in the custom parameters object.

       // Optional "tenant" parameter in case you are using an Azure AD tenant.
       // eg. '8eaef023-2b34-4da1-9baa-8bc8c9d6a490' or 'contoso.onmicrosoft.com'
       // or "common" for tenant-independent tokens.
       // The default value is "common".
       provider_data.custom_parameters["tenant"] ="TENANT_ID";

3. **Optional**: Specify additional OAuth 2.0 scopes beyond basic profile that
   you want to request from the authentication provider.

       provider_data.scopes.push_back("mail.read");
       provider_data.scopes.push_back("calendars.read");

   To learn more, refer to the
   [Microsoft permissions and consent documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent).
4. Once your provider data has been configured, use it to create a
   `FederatedOAuthProvider`.

       // Construct a FederatedOAuthProvider for use in Auth methods.
       firebase::auth::FederatedOAuthProvider provider(provider_data);

5. Authenticate with Firebase using the Auth provider object. Note that unlike
   other FirebaseAuth operations, this will take control of your UI by popping
   up a web view in which the user can enter their credentials.

   To start the sign in flow, call `SignInWithProvider`:

       firebase::Future<firebase::auth::AuthResult> result =
         auth->SignInWithProvider(provider_data);

   Your application may then wait or [register a callback on the Future](https://firebase.google.com/docs/auth/cpp/microsoft-oauth#register_callback_on_future).

   Using the OAuth access token, you can call the
   [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?toc=./toc.json&view=graph-rest-1.0).

   Unlike other providers supported by Firebase Auth, Microsoft does not
   provide a photo URL and instead, the binary data for a profile photo has to
   be requested via
   [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/api/profilephoto-get?view=graph-rest-1.0).
6. While the above examples focus on sign-in flows, you also have the
   ability to link a Microsoft Azure Active Directory provider to an existing
   user using `LinkWithProvider`. For example, you can link multiple
   providers to the same user allowing them to sign in with either.

       firebase::Future<firebase::auth::AuthResult> result = user.LinkWithProvider(provider_data);

7. The same pattern can be used with `ReauthenticateWithProvider` which can be
   used to retrieve fresh credentials for sensitive operations that require
   recent login.

       firebase::Future<firebase::auth::AuthResult> result =
         user.ReauthenticateWithProvider(provider_data);

   Your application may then wait or [register a callback on
   the Future](https://firebase.google.com/docs/auth/cpp/microsoft-oauth#register_callback_on_future).

## Advanced: Handle the sign-in flow manually

Unlike other OAuth providers supported by Firebase such as Google, Facebook,
and Twitter, where sign-in can directly be achieved with OAuth access token
based credentials, Firebase Auth does not support the same capability for
providers such as Microsoft due to the inability of the Firebase
Auth server to verify the audience of Microsoft OAuth access tokens.
This is a critical security requirement and could expose applications and
websites to replay attacks where a Microsoft OAuth access token obtained for
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