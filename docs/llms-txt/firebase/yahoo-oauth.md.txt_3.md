# Source: https://firebase.google.com/docs/auth/ios/yahoo-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like
Yahoo by integrating generic OAuth Login into your app using the Firebase SDK to
carry out the end to end sign-in flow.

## Before you begin

To sign in users using Yahoo accounts, you must first enable Yahoo as a sign-in
provider for your Firebase project:

1. [Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup).
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
3. On the **Sign in method** tab, enable the **Yahoo** provider.
4. Add the **Client ID** and **Client Secret** from that provider's developer console to the provider configuration:
   1. To register a Yahoo OAuth client, follow the Yahoo developer
      documentation on [registering a web application with Yahoo](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).

      Be sure to select the two OpenID Connect API permissions:
      `profile` and `email`.
   2. When registering apps with these providers, be sure to register the `*.firebaseapp.com` domain for your project as the redirect domain for your app.
5. Click **Save**.

## Handle the sign-in flow with the Firebase SDK

To handle the sign-in flow with the Firebase Apple platforms SDK, follow these steps:

1. Add custom URL schemes to your Xcode project:

   1. Open your project configuration: double-click the project name in the left tree view. Select your app from the **TARGETS** section, then select the **Info** tab, and expand the **URL Types** section.
   2. Click the **+** button, and add your Encoded App ID as a URL scheme. You can find your Encoded App ID on the [General
      Settings](https://console.firebase.google.com/project/_/settings/general/) page of the Firebase console, in the section for your iOS app. Leave the other fields blank.

      When completed, your config should look something similar to the
      following (but with your application-specific values):
      ![Screenshot of Xcode's custom URL scheme setup interface](https://firebase.google.com/static/docs/auth/images/app-id-url-scheme.png)

   <br />

2. Create an instance of an **OAuthProvider** using the provider ID
   **yahoo.com**.

   #### Swift

   ```swift
   var provider = OAuthProvider(providerID: "yahoo.com")
       
   ```

   #### Objective-C

   ```objective-c
   FIROAuthProvider *provider = [FIROAuthProvider providerWithProviderID:@"yahoo.com"];
       
   ```
3. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

   #### Swift

   ```swift
   provider.customParameters = [
   "prompt": "login",
   "language": "fr"
   ]
       
   ```

   #### Objective-C

   ```objective-c
   [provider setCustomParameters:@{@"prompt": @"login", @"language": @"fr"}];
       
   ```

   For the parameters Yahoo supports, see the
   [Yahoo OAuth documentation](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).
   Note that you can't pass Firebase-required parameters with
   `setCustomParameters`. These parameters are **client_id** ,
   **redirect_uri** , **response_type** , **scope** and **state**.
4. **Optional** : Specify additional OAuth 2.0 scopes beyond `profile` and
   `email` that you want to request from the authentication provider. If your
   application requires access to private user data from Yahoo APIs, you'll
   need to request permissions to Yahoo APIs under **API Permissions** in the
   Yahoo developer console. Requested OAuth scopes must be exact matches to the
   preconfigured ones in the app's API permissions. For example if, read/write
   access is requested to user contacts and preconfigured in the app's API
   permissions, `sdct-w` has to be passed instead of the readonly OAuth scope
   `sdct-r`. Otherwise, the flow will fail and an error would be shown to the
   end user.

   #### Swift

   ```swift
   // Request access to Yahoo Mail API.
   // Request read/write access to user contacts.
   // This must be preconfigured in the app's API permissions.
   provider.scopes = ["mail-r", "sdct-w"]
       
   ```

   #### Objective-C

   ```objective-c
   // Request access to Yahoo Mail API.
   // Request read/write access to user contacts.
   // This must be preconfigured in the app's API permissions.
   [provider setScopes:@[@"mail-r", @"sdct-w"]];
       
   ```

   To learn more, refer to the
   [Yahoo scopes documentation](https://developer.yahoo.com/oauth2/guide/yahoo_scopes/).
5. **Optional** : If you want to customize the way your app presents the
   `SFSafariViewController` or `UIWebView` when
   displaying the reCAPTCHA to the user, create a custom class that conforms
   to the `AuthUIDelegate` protocol, and pass it to
   `credentialWithUIDelegate`.

6. Authenticate with Firebase using the OAuth provider object.

   #### Swift

   ```swift
   provider.getCredentialWith(nil) { credential, error in
   if error != nil {
   // Handle error.
   }
   if credential != nil {
   Auth().signIn(with: credential) { authResult, error in
     if error != nil {
       // Handle error.
     }
     // User is signed in.
     // IdP data available in authResult.additionalUserInfo.profile.
     // Yahoo OAuth access token can also be retrieved by:
     // (authResult.credential as? OAuthCredential)?.accessToken
     // Yahoo OAuth ID token can be retrieved by calling:
     // (authResult.credential as? OAuthCredential)?.idToken
   }
   }
   }
       
   ```

   #### Objective-C

   ```objective-c
   [provider getCredentialWithUIDelegate:nil
                          completion:^(FIRAuthCredential *_Nullable credential, NSError *_Nullable error) {
   if (error) {
   // Handle error.
   }
   if (credential) {
   [[FIRAuth auth] signInWithCredential:credential
                             completion:^(FIRAuthDataResult *_Nullable authResult, NSError *_Nullable error) {
     if (error) {
       // Handle error.
     }
     // User is signed in.
     // IdP data available in authResult.additionalUserInfo.profile.
     // Yahoo OAuth access token can also be retrieved by:
     // ((FIROAuthCredential *)authResult.credential).accessToken
     // Yahoo OAuth ID token can be retrieved by calling:
     // ((FIROAuthCredential *)authResult.credential).idToken
   }];
   }
   }];
       
   ```

   Using the OAuth access token, you can call the
   [Yahoo API](https://developer.yahoo.com/oauth2/guide/apirequests/).

   For example, to get basic profile information, you can call the REST API,
   passing the access token in the `Authorization` header:

   ```
   https://social.yahooapis.com/v1/user/YAHOO_USER_UID/profile?format=json
   ```

   Where `YAHOO_USER_UID` is the Yahoo user's ID which can be retrieved from
   the `Auth.auth.currentUser.providerData[0].uid` field or from
   `authResult.additionalUserInfo.profile`.
7. While the above examples focus on sign-in flows, you also have the
   ability to link a Yahoo provider to an existing user using
   `linkWithPopup`. For example, you can link multiple
   providers to the same user allowing them to sign in with either.

   #### Swift

   ```swift
   Auth().currentUser.link(withCredential: credential) { authResult, error in
   if error != nil {
   // Handle error.
   }
   // Yahoo credential is linked to the current user.
   // IdP data available in authResult.additionalUserInfo.profile.
   // Yahoo OAuth access token can also be retrieved by:
   // (authResult.credential as? OAuthCredential)?.accessToken
   // Yahoo OAuth ID token can be retrieved by calling:
   // (authResult.credential as? OAuthCredential)?.idToken
   }
       
   ```

   #### Objective-C

   ```objective-c
   [[FIRAuth auth].currentUser
   linkWithCredential:credential
           completion:^(FIRAuthDataResult * _Nullable authResult, NSError * _Nullable error) {
   if (error) {
   // Handle error.
   }
   // Yahoo credential is linked to the current user.
   // IdP data available in authResult.additionalUserInfo.profile.
   // Yahoo OAuth access token is can also be retrieved by:
   // ((FIROAuthCredential *)authResult.credential).accessToken
   // Yahoo OAuth ID token can be retrieved by calling:
   // ((FIROAuthCredential *)authResult.credential).idToken
   }];
       
   ```
8. The same pattern can be used with
   `reauthenticateWithPopup`/`reauthenticateWithRedirect` which can be used to
   retrieve fresh credentials for sensitive operations that require recent
   login.

   #### Swift

   ```swift
   Auth().currentUser.reauthenticateWithCredential(withCredential: credential) { authResult, error in
   if error != nil {
   // Handle error.
   }
   // User is re-authenticated with fresh tokens minted and
   // should be able to perform sensitive operations like account
   // deletion and email or password update.
   // IdP data available in result.additionalUserInfo.profile.
   // Additional OAuth access token is can also be retrieved by:
   // (authResult.credential as? OAuthCredential)?.accessToken
   // Yahoo OAuth ID token can be retrieved by calling:
   // (authResult.credential as? OAuthCredential)?.idToken
   }
       
   ```

   #### Objective-C

   ```objective-c
   [[FIRAuth auth].currentUser
   reauthenticateWithCredential:credential
                     completion:^(FIRAuthDataResult * _Nullable authResult, NSError * _Nullable error) {
   if (error) {
   // Handle error.
   }
   // User is re-authenticated with fresh tokens minted and
   // should be able to perform sensitive operations like account
   // deletion and email or password update.
   // IdP data available in result.additionalUserInfo.profile.
   // Additional OAuth access token is can also be retrieved by:
   // ((FIROAuthCredential *)authResult.credential).accessToken
   // Yahoo OAuth ID token can be retrieved by calling:
   // ((FIROAuthCredential *)authResult.credential).idToken
   }];
       
   ```

## Handling account-exists-with-different-credential Errors

If you enabled the **One account per email address** setting in the [Firebase console](https://console.firebase.google.com/),
when a user tries to sign in a to a provider (such as Yahoo) with an email that already
exists for another Firebase user's provider (such as Google), the error
`FIRAuthErrorCodeAccountExistsWithDifferentCredential` is thrown along with a temporary
`FIRAuthCredential` object (Yahoo credential). To complete the sign in to the
intended provider, the user has to sign first to the existing provider (Google) and then link to the
former `FIRAuthCredential` (Yahoo credential). This would look as illustrated below:

#### Swift

```swift
  // Sign-in with an OAuth credential.
  provider.getCredentialWith(nil) { credential, error in
    // An account with the same email already exists.
    if (error as NSError?)?.code == AuthErrorCode.accountExistsWithDifferentCredential.rawValue {
      // Get pending credential and email of existing account.
      let existingAcctEmail = (error! as NSError).userInfo[AuthErrorUserInfoEmailKey] as! String
      let pendingCred = (error! as NSError).userInfo[AuthErrorUserInfoUpdatedCredentialKey] as! AuthCredential
      // Lookup existing account identifier by the email.
      Auth.auth().fetchProviders(forEmail:existingAcctEmail) { providers, error in
        // Existing email/password account.
        if (providers?.contains(EmailAuthProviderID))! {
          // Existing password account for email. Ask user to provide the password of the
          // existing account.
          // Sign in with existing account.
          Auth.auth().signIn(withEmail:existingAcctEmail, password:password) { user, error in
            // Successfully signed in.
            if user != nil {
              // Link pending credential to account.
              Auth.auth().currentUser?.linkAndRetrieveData(with: pendingCred) { result, error in
                // ...
              }
            }
          }
        }
      }
      return
    }

    // Other errors.
    if error != nil {
      // handle the error.
      return
    }

    // Sign in with the credential.
    if credential != nil {
      Auth.auth().signInAndRetrieveData(with: credential!) { result, error in
        if error != nil {
          // handle the error.
          return
        }
      }
    }
  }

  
```

#### Objective-C

```objective-c
  // Sign-in with an OAuth credential.
  [provider getCredentialWithUIDelegate:nil
                             completion:^(FIRAuthCredential *_Nullable credential, NSError *_Nullable error) {
    // An account with the same email already exists.
    if (error.code == FIRAuthErrorCodeAccountExistsWithDifferentCredential) {
      // Get pending credential and email of existing account.
      NSString *existingAcctEmail = error.userInfo[FIRAuthErrorUserInfoEmailKey];
      FIRAuthCredential *pendingCred = error.userInfo[FIRAuthErrorUserInfoUpdatedCredentialKey];
      // Lookup existing account identifier by the email.
      [[FIRAuth auth] fetchProvidersForEmail:existingAcctEmail
                                 completion:^(NSArray<NSString *> *_Nullable providers,
                                              NSError *_Nullable error) {
        // Existing email/password account.
        if ( [providers containsObject:FIREmailAuthProviderID] ) {
          // Existing password account for email. Ask user to provide the password of the
          // existing account.

          // Sign in with existing account.
          [[FIRAuth auth] signInWithEmail:existingAcctEmail
                                 password:password
                               completion:^(FIRUser *user, NSError *error) {
            // Successfully signed in.
            if (user) {
              // Link pending credential to account.
              [[FIRAuth auth].currentUser linkWithCredential:pendingCred
                                                  completion:^(FIRUser *_Nullable user,
                                                               NSError *_Nullable error) {
                // ...
              }];
            }
          }];
        }
      }];
      return;
    }

    // Other errors.
    if (error) {
      // handle the error.
      return;
    }

    // Sign in with the credential.
    if (credential) {
      [[FIRAuth auth] signInAndRetrieveDataWithCredential:credential
          completion:^(FIRAuthDataResult *_Nullable authResult,
                       NSError *_Nullable error) {
        if (error) {
          // handle the error.
          return;
        }
      }];
    }
  }];
  
```

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
  [`User`](https://firebase.google.com/docs/reference/ios/firebaseauth/interface_f_i_r_user) object. See [Manage Users](https://firebase.google.com/docs/auth/ios/manage-users).

- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/ios/account-linking)

To sign out a user, call [`signOut:`](https://firebase.google.com/docs/reference/ios/firebaseauth/interface_f_i_r_auth#ab0d5111f05c3f1906243852cc8ef41b1).

#### Swift

```swift
let firebaseAuth = Auth.auth()
do {
  try firebaseAuth.signOut()
} catch let signOutError as NSError {
  print("Error signing out: %@", signOutError)
}
```

#### Objective-C

```objective-c
NSError *signOutError;
BOOL status = [[FIRAuth auth] signOut:&signOutError];
if (!status) {
  NSLog(@"Error signing out: %@", signOutError);
  return;
}
```

You may also want to add error handling code for the full range of authentication
errors. See [Handle Errors](https://firebase.google.com/docs/auth/ios/errors).