# Source: https://firebase.google.com/docs/auth/unity/apple.md.txt

You can let your users authenticate with Firebase using their Apple ID by
using the Firebase SDK to carry out the end-to-end OAuth 2.0 sign-in flow.
**Important**: To sign in with an Apple account, users must:

- Have an Apple ID with two-factor authentication (2FA) enabled.
- Be signed in to iCloud on an Apple device.

See [How
to use Sign in with Apple](https://support.apple.com/en-us/HT210318). You will also need to meet these requirements
to test your integration with Sign In with Apple.

## Before you begin

[Video](https://www.youtube.com/watch?v=HyiNbqLOCQ8)

To sign in users using Apple, first configure Sign In with Apple
on Apple's developer site, then enable Apple as a sign-in provider for your
Firebase project.

### Join the Apple Developer Program

Sign In with Apple can only be configured by members of the [Apple Developer
Program](https://developer.apple.com/programs/).

### Configure Sign In with Apple

Apple Sign In must be enabled and properly configured in your Firebase project. The Apple Developer configuration varies across Android and Apple platforms. Please follow the "Configure Sign In With Apple" section of the [iOS+](https://firebase.google.com/docs/auth/ios/apple#configure-sign-in-with-apple) and/or [Android](https://firebase.google.com/docs/auth/android/apple#configure-sign-in-with-apple) guides before proceeding.

### Enable Apple as a sign-in provider

1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section. On the **Sign in method** tab, enable the **Apple** provider.
2. Configure the Apple Sign In provider settings:
   1. If you're deploying your app only on Apple platforms, you can leave the Service ID, Apple Team ID, private key and key ID fields empty.
   2. For support on Android devices:
      1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup). Be sure to register your app's SHA-1 signature when you set up your app in the Firebase console.
      2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section. On the **Sign in method** tab, enable the **Apple** provider. Specify the Service ID you created in the previous section. Also, in the OAuth code flow configuration section, specify your Apple Team ID and the private key and key ID you created in the previous section.

<br />

## Comply with Apple anonymized data requirements

Sign In with Apple gives users the option of anonymizing their data,
including their email address, when signing in. Users who choose this option
have email addresses with the domain `privaterelay.appleid.com`. When
you use Sign In with Apple in your app, you must comply with any applicable
developer policies or terms from Apple regarding these anonymized Apple
IDs.

This includes obtaining any required user consent before you
associate any directly identifying personal information with an anonymized Apple
ID. When using Firebase Authentication, this may include the following
actions:

- Link an email address to an anonymized Apple ID or vice versa.
- Link a phone number to an anonymized Apple ID or vice versa
- Link a non-anonymous social credential (Facebook, Google, etc) to an anonymized Apple ID or vice versa.

The above list is not exhaustive. Refer to the Apple Developer Program
License Agreement in the Membership section of your developer account to make
sure your app meets Apple's requirements.

## Access the `Firebase.Auth.FirebaseAuth` class

The `FirebaseAuth` class is the gateway for all API calls. It is accessible through [FirebaseAuth.DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#defaultinstance).

```c#
Firebase.Auth.FirebaseAuth auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
```

## Handle the sign-in flow with the Firebase SDK

The process to Sign-in With Apple varies across Apple and Android platforms.

### On Apple platforms

1. Install a third party plugin to handle Apple sign in nonce and token
   generation, such as the [Unity's Sign In With Apple Asset Storage
   Package](https://blogs.unity3d.com/2019/09/19/support-for-apple-sign-in/).
   You may need to alter the code to plumb the generated random nonce string in
   its raw string state for use in Firebase operations (that is, store a copy of
   it before the SHA256 digest form of the nonce is created).

2. Use the resulting token string and raw nonce to construct a Firebase
   Credential and sign into Firebase.

   ```c#
   Firebase.Auth.Credential credential =
       Firebase.Auth.OAuthProvider.GetCredential("apple.com", appleIdToken, rawNonce, null);
   auth.SignInAndRetrieveDataWithCredentialAsync(credential).ContinueWith(task => {
     if (task.IsCanceled) {
       Debug.LogError("SignInAndRetrieveDataWithCredentialAsync was canceled.");
       return;
     }
     if (task.IsFaulted) {
       Debug.LogError("SignInAndRetrieveDataWithCredentialAsync encountered an error: " + task.Exception);
       return;
     }

     Firebase.Auth.AuthResult result = task.Result;
     Debug.LogFormat("User signed in successfully: {0} ({1})",
         result.User.DisplayName, result.User.UserId);
   });
   ```

   <br />

3. The same pattern can be used with `ReauthenticateAsync` which can be
   used to retrieve fresh credentials for sensitive operations that require
   recent login. For more information see
   [Manage Users](https://firebase.google.com/docs/auth/cpp/manage-users).

4. When linking with Apple Sign In on Apple platforms you may encounter an error that an
   existing Firebase account has already been linked to the Apple account. When
   this occurs a `Firebase.Auth.FirebaseAccountLinkException` will be thrown
   instead of the standard `Firebase.FirebaseException`. In this case the
   exception includes a `UserInfo.UpdatedCredential` property
   that, if valid, may be used to sign-in the Apple-linked user via
   `FirebaseAuth.SignInAndRetrieveDataWithCredentialAsync`.
   The updated credential circumvents the need to generate new Apple Sign-In token
   with nonce for the sign-in operation.

   ```c#
   auth.CurrentUser.LinkWithCredentialAsync(
     Firebase.Auth.OAuthProvider.GetCredential("apple.com", idToken, rawNonce, null))
       .ContinueWithOnMainThread( task => {
         if (task.IsCompletedSuccessfully) {
           // Link Success
         } else {
           if (task.Exception != null) {
             foreach (Exception exception in task.Exception.Flatten().InnerExceptions) {
               Firebase.Auth.FirebaseAccountLinkException firebaseEx =
                 exception as Firebase.Auth.FirebaseAccountLinkException;
               if (firebaseEx != null && firebaseEx.UserInfo.UpdatedCredential.IsValid()) {
                 // Attempt to sign in with the updated credential.
                 auth.SignInAndRetrieveDataWithCredentialAsync(firebaseEx.UserInfo.UpdatedCredential).
                   ContinueWithOnMainThread( authResultTask => {
                     // Handle Auth result.
                   });
               } else {
                 Debug.Log("Link with Apple failed:" + firebaseEx );
               }
             } // end for loop
           }
         }
       });
   ```

   <br />

### On Android

On Android, authenticate your users with Firebase by integrating web-based
generic OAuth Login into your app using the Firebase SDK to carry out the end to
end sign-in flow.

To handle the sign-in flow with the Firebase SDK, follow these steps:

1. Construct an instance of a `FederatedOAuthProviderData` configured with
   the provider ID appropriate for Apple.

       Firebase.Auth.FederatedOAuthProviderData providerData =
         new Firebase.Auth.FederatedOAuthProviderData();

       providerData.ProviderId = "apple.com";

2. **Optional:** Specify additional OAuth 2.0 scopes beyond the default that you
   want to request from the authentication provider.

       providerData.Scopes = new List<string>();
       providerData.Scopes.Add("email");
       providerData.Scopes.Add("name");

3. **Optional:** If you want to display Apple's sign-in screen in a language
   other than English, set the `locale` parameter. See the
   [Sign In with Apple docs](https://developer.apple.com/documentation/signinwithapplejs/incorporating_sign_in_with_apple_into_other_platforms#3332112)
   for the supported locales.

       providerData.CustomParameters = new Dictionary<string,string>;

       // Localize to French.
       providerData.CustomParameters.Add("language", "fr");

4. Once your provider data has been configured, use it to create a
   FederatedOAuthProvider.

       // Construct a FederatedOAuthProvider for use in Auth methods.
       Firebase.Auth.FederatedOAuthProvider provider =
         new Firebase.Auth.FederatedOAuthProvider();
       provider.SetProviderData(providerData);

5. Authenticate with Firebase using the Auth provider object. Note that unlike
   other FirebaseAuth operations, this will take control of your UI by popping
   up a web view in which the user can enter their credentials.

   To start the sign in flow, call `signInWithProvider`:

       auth.SignInWithProviderAsync(provider).ContinueOnMainThread(task => {
           if (task.IsCanceled) {
               Debug.LogError("SignInWithProviderAsync was canceled.");
               return;
           }
           if (task.IsFaulted) {
               Debug.LogError("SignInWithProviderAsync encountered an error: " +
                 task.Exception);
               return;
           }

           Firebase.Auth.AuthResult authResult = task.Result;
           Firebase.Auth.FirebaseUser user = authResult.User;
           Debug.LogFormat("User signed in successfully: {0} ({1})",
               user.DisplayName, user.UserId);
       });

6. The same pattern can be used with `ReauthenticateWithProvider` which can be
   used to retrieve fresh credentials for sensitive operations that require
   recent login.

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

7. And, you can use `LinkWithCredentialAsync()` to link different identity providers
   to existing accounts.

   Note that Apple requires you to get explicit consent from users before you
   link their Apple accounts to other data.

   For example, to link a Facebook account to the current Firebase account, use
   the access token you got from signing the user in to Facebook:

       // Initialize a Facebook credential with a Facebook access token.

       Firebase.Auth.Credential credential =
           Firebase.Auth.FacebookAuthProvider.GetCredential(facebook_token);

       // Assuming the current user is an Apple user linking a Facebook provider.
       user.LinkWithCredentialAsync(credential)
           .ContinueWithOnMainThread( task => {
             if (task.IsCanceled) {
                 Debug.LogError("LinkWithCredentialAsync was canceled.");
                 return;
             }
             if (task.IsFaulted) {
               Debug.LogError("LinkWithCredentialAsync encountered an error: "
                              + task.Exception);
                 return;
             }

             Firebase.Auth.AuthResult result = task.Result;
             Firebase.Auth.FirebaseUser user = result.User;
             Debug.LogFormat("User linked successfully: {0} ({1})",
                 user.DisplayName, user.UserId);
           });

### Sign in with Apple Notes

Unlike other providers supported by Firebase Auth, Apple does not provide a
photo URL.

Also, when the user chooses not to share their email with the app, Apple
provisions a unique email address for that user (of the form
`xyz@privaterelay.appleid.com`), which it shares with your app. If you
configured the private email relay service, Apple forwards emails sent to
the anonymized address to the user's real email address.

Apple only shares user information such as the display name with apps the
first time a user signs in. Usually, Firebase stores the display name the
first time a user signs in with Apple, which you can get with
`auth.CurrentUser.DisplayName`.
However, if you previously used Apple to sign a user in to the app without
using Firebase, Apple will not provide Firebase with the user's display name.

## Next steps

After a user signs in for the first time, a new user account is created and linked to the credentials---that is, the user name and password, phone number, or auth provider information---the user signed in with. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project, regardless of how the user signs in.

<br />

In your apps, you can get the user's basic profile information from the Firebase.Auth.FirebaseUser object. See [Manage Users](https://firebase.google.com/docs/auth/cpp/manage-users).

In your Firebase Realtime Database and Cloud Storage Security Rules, you can get the signed-in user's unique user ID from the auth variable, and use it to control what data a user can access.