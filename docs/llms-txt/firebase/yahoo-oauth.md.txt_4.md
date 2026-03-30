# Source: https://firebase.google.com/docs/auth/unity/yahoo-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like
Yahoo by integrating web-based generic OAuth Login into your app using the
Firebase SDK to carry out the end to end sign-in flow. Since this flow requires
the use of the phone-based Firebase SDKs, it is only supported on Android and
Apple platforms.

## Before you begin

Before you can use
[Firebase Authentication](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth),
you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already
    registered and configured for Firebase.

  - If you don't have a Unity project, you can download a
    [sample app](https://github.com/google/mechahamster).

- Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseAuth.unitypackage`) to
  your Unity project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open Unity project
(for example, you download Firebase config files from the console, then move
them into your Unity project).

## Access the `Firebase.Auth.FirebaseAuth` class

The `FirebaseAuth` class is the gateway for all API calls. It is accessible through [FirebaseAuth.DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#defaultinstance).

```c#
Firebase.Auth.FirebaseAuth auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
```

## Handle the sign-in flow with the Firebase SDK

To handle the sign-in flow with the Firebase SDK, follow these steps:

1. Construct an instance of a `FederatedOAuthProviderData` configured with
   the provider ID appropriate for Yahoo.

       Firebase.Auth.FederatedOAuthProviderData providerData =
         new Firebase.Auth.FederatedOAuthProviderData();
       providerData.ProviderId = Firebase.Auth.YahooAuthProvider.ProviderId;

2. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

       providerData.CustomParameters = new Dictionary<string,string>;

       // Prompt user to re-authenticate to Yahoo.
       providerData.CustomParameters.Add("prompt", "login");

       // Localize to French.
       providerData.CustomParameters.Add("language", "fr");

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

       providerData.Scopes = new List<string>();

       // Request access to Yahoo Mail API.
       providerData.Scopes.Add("mail-r");
       // This must be preconfigured in the app's API permissions.
       providerData.Scopes.Add("sdct-w");

   To learn more, refer to the
   [Yahoo scopes documentation](https://developer.yahoo.com/oauth2/guide/yahoo_scopes/).
4. Once your provider data has been configured, use it to create a
   FederatedOAuthProvider.

       // Construct a FederatedOAuthProvider for use in Auth methods.
       Firebase.Auth.FederatedOAuthProvider provider =
           new Firebase.Auth.FederatedOAuthProvider();
       provider.SetProviderData(providerData);

5. Authenticate with Firebase using the Auth provider object. Note that unlike
   other FirebaseAuth operations, this will take control of your UI by popping
   up a web view in which the user can enter their credentials.

   To start the sign in flow, call `SignInAndRetrieveDataWithCredentialAsync`:

\<\<../_includes/_sign_in_with_provider_unity.md\>\>\>

1. While the above examples focus on sign-in flows, you also have the
   ability to link a Yahoo provider to an existing user using
   `LinkWithProviderAsync`. For example, you can link multiple
   providers to the same user allowing them to sign in with either.

       user.LinkWithProviderAsync(provider).ContinueOnMainThread(task => {
           if (task.IsCanceled) {
               Debug.LogError("LinkWithProviderAsync was canceled.");
               return;
           }
           if (task.IsFaulted) {
               Debug.LogError("LinkWithProviderAsync encountered an error: "
                 + task.Exception);
               return;
           }

           Firebase.Auth.AuthResult authResult = task.Result;
           Firebase.Auth.FirebaseUser user = authResult.User;
           Debug.LogFormat("User linked successfully: {0} ({1})",
               user.DisplayName, user.UserId);
       });

2. The same pattern can be used with `ReauthenticateWithProviderAsync` which
   can be used to retrieve fresh credentials for sensitive operations that
   require recent login.

       user.ReauthenticateWithProviderAsync(provider).ContinueOnMainThread(task => {
           if (task.IsCanceled) {
               Debug.LogError("ReauthenticateWithProviderAsync was canceled.");
               return;
           }
           if (task.IsFaulted) {
               Debug.LogError(
               "ReauthenticateWithProviderAsync encountered an error: " +
                   task.Exception);
               return;
           }

           Firebase.Auth.AuthResult authResult = task.Result;
           Firebase.Auth.FirebaseUser user = authResult.User;
           Debug.LogFormat("User reauthenticated successfully: {0} ({1})",
               user.DisplayName, user.UserId);
       });

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
  [`Firebase.Auth.FirebaseUser`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user) object:

  ```c#
  Firebase.Auth.FirebaseUser user = auth.CurrentUser;
  if (user != null) {
    string name = user.DisplayName;
    string email = user.Email;
    System.Uri photo_url = user.PhotoUrl;
    // The user's Id, unique to the Firebase project.
    // Do NOT use this value to authenticate with your backend server, if you
    // have one; use User.TokenAsync() instead.
    string uid = user.UserId;
  }
  ```
- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/unity/account-linking)

To sign out a user, call [`SignOut()`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#signout):

```c#
auth.SignOut();
```