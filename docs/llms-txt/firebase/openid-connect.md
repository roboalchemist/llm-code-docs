# Source: https://firebase.google.com/docs/auth/web/openid-connect.md.txt

# Source: https://firebase.google.com/docs/auth/android/openid-connect.md.txt

# Source: https://firebase.google.com/docs/auth/ios/openid-connect.md.txt

If you've upgraded toFirebase Authenticationwith Identity Platform, you can authenticate your users with Firebase using the OpenID Connect (OIDC) compliant provider of your choice. This makes it possible to use identity providers not natively supported by Firebase.

## Before you begin

To sign in users using an OIDC provider, you must first collect some information from the provider:

- **Client ID** : A string unique to the provider that identifies your app. Your provider might assign you a different client ID for each platform you support. This is one of the values of the`aud`claim in ID tokens issued by your provider.

- **Client secret** : A secret string that the provider uses to confirm ownership of a client ID. For every client ID, you will need a matching client secret. (This value is required only if you're using the*auth code flow*, which is strongly recommended.)

- **Issuer** : A string that identifies your provider. This value must be a URL that, when appended with`/.well-known/openid-configuration`, is the location of the provider's OIDC discovery document. For example, if the issuer is`https://auth.example.com`, the discovery document must be available at`https://auth.example.com/.well-known/openid-configuration`.

After you have the above information, enable OpenID Connect as a sign-in provider for your Firebase project:

1. [Add Firebase to your iOS project](https://firebase.google.com/docs/ios/setup).

2. If you haven't upgraded toFirebase Authenticationwith Identity Platform, do so. OpenID Connect authentication is only available in upgraded projects.

3. On the[**Sign-in providers**](https://console.firebase.google.com/project/_/authentication/providers)page of theFirebaseconsole, click**Add new provider** , and then click**OpenID Connect**.

4. Select whether you will be using the*authorization code flow* or the*implicit grant flow*.

   **You should use always the code flow if your provider supports it**. The implicit flow is less secure and using it is strongly discouraged.
5. Give a name to this provider. Note the provider ID that's generated: something like`oidc.example-provider`. You'll need this ID when you add sign-in code to your app.

6. Specify your client ID and client secret, and your provider's issuer string. These values must exactly match the values your provider assigned to you.

7. Save your changes.

## Handle the sign-in flow with the Firebase SDK

The easiest way to authenticate your users with Firebase using your OIDC provider is to handle the entire sign-in flow with the Firebase SDK.

To handle the sign-in flow with the Firebase Apple platforms SDK, follow these steps:

1. Add custom URL schemes to your Xcode project:

   1. Open your project configuration: double-click the project name in the left tree view. Select your app from the**TARGETS** section, then select the**Info** tab, and expand the**URL Types**section.
   2. Click the**+** button, and add your Encoded App ID as a URL scheme. You can find your Encoded App ID on the[General Settings](https://console.firebase.google.com/project/_/settings/general/)page of the Firebase console, in the section for your iOS app. Leave the other fields blank.

      When completed, your config should look something similar to the following (but with your application-specific values):
      ![Screenshot of Xcode's custom URL scheme setup interface](https://firebase.google.com/static/docs/auth/images/app-id-url-scheme.png)
2. Create an instance of an`OAuthProvider`using the provider ID you got in the Firebase console.

   ### Swift

       var provider = OAuthProvider(providerID: "oidc.example-provider")

   ### Objective-C

       FIROAuthProvider *provider = [FIROAuthProvider providerWithProviderID:@"oidc.example-provider"];

3. **Optional**: Specify additional custom OAuth parameters that you want to send with the OAuth request.

   ### Swift

       provider.customParameters = [
         "login_hint": "user@example.com"
       ]

   ### Objective-C

       [provider setCustomParameters:@{@"login_hint": @"user@example.com"}];

   Check with your provider for the parameters it supports. Note that you can't pass Firebase-required parameters with`setCustomParameters`. These parameters are`client_id`,`response_type`,`redirect_uri`,`state`,`scope`and`response_mode`.
4. **Optional**: Specify additional OAuth 2.0 scopes beyond basic profile that you want to request from the authentication provider.

   ### Swift

       provider.scopes = ["mail.read", "calendars.read"]

   ### Objective-C

       [provider setScopes:@[@"mail.read", @"calendars.read"]];

   Check with your provider for the scopes it supports.
5. **Optional** : If you want to customize the way your app presents the`SFSafariViewController`or`UIWebView`when displaying the reCAPTCHA to the user, create a custom class that conforms to the`AuthUIDelegate`protocol.

6. Authenticate with Firebase using the OAuth provider object.

   ### Swift

       // If you created a custom class that conforms to AuthUIDelegate,
       // pass it instead of nil:
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
             // OAuth access token can also be retrieved:
             // (authResult.credential as? OAuthCredential)?.accessToken
             // OAuth ID token can also be retrieved:
             // (authResult.credential as? OAuthCredential)?.idToken
           }
         }
       }

   ### Objective-C

       // If you created a custom class that conforms to AuthUIDelegate,
       // pass it instead of nil:
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
             // OAuth access token can also be retrieved:
             // ((FIROAuthCredential *)authResult.credential).accessToken
             // OAuth ID token can also be retrieved:
             // ((FIROAuthCredential *)authResult.credential).idToken
           }];
         }
       }];

7. While the above examples focus on sign-in flows, you also have the ability to link an OIDC provider to an existing user using`linkWithCredential`. For example, you can link multiple providers to the same user allowing them to sign in with either.

   ### Swift

       Auth().currentUser.link(withCredential: credential) { authResult, error in
         if error != nil {
           // Handle error.
         }
         // OIDC credential is linked to the current user.
         // IdP data available in authResult.additionalUserInfo.profile.
         // OAuth access token can also be retrieved:
         // (authResult.credential as? OAuthCredential)?.accessToken
         // OAuth ID token can also be retrieved:
         // (authResult.credential as? OAuthCredential)?.idToken
       }

   ### Objective-C

       [[FIRAuth auth].currentUser
           linkWithCredential:credential
                   completion:^(FIRAuthDataResult * _Nullable authResult, NSError * _Nullable error) {
         if (error) {
           // Handle error.
         }
         // OIDC credential is linked to the current user.
         // IdP data available in authResult.additionalUserInfo.profile.
         // OAuth access token can also be retrieved:
         // ((FIROAuthCredential *)authResult.credential).accessToken
         // OAuth ID token can also be retrieved:
         // ((FIROAuthCredential *)authResult.credential).idToken
       }];

8. The same pattern can be used with`reauthenticateWithCredential`which can be used to retrieve fresh credentials for sensitive operations that require recent login.

   ### Swift

       Auth().currentUser.reauthenticateWithCredential(withCredential: credential) { authResult, error in
         if error != nil {
           // Handle error.
         }
         // User is re-authenticated with fresh tokens minted and
         // should be able to perform sensitive operations like account
         // deletion and email or password update.
         // IdP data available in result.additionalUserInfo.profile.
         // Additional OAuth access token can also be retrieved:
         // (authResult.credential as? OAuthCredential)?.accessToken
         // OAuth ID token can also be retrieved:
         // (authResult.credential as? OAuthCredential)?.idToken
       }

   ### Objective-C

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
         // Additional OAuth access token can also be retrieved:
         // ((FIROAuthCredential *)authResult.credential).accessToken
         // OAuth ID token can also be retrieved:
         // ((FIROAuthCredential *)authResult.credential).idToken
       }];

## Handle the sign-in flow manually

If you've already implemented the OpenID Connect sign-in flow in your app, you can use the ID token directly to authenticate with Firebase:  

### Swift

    let credential = OAuthProvider.credential(
        withProviderID: "oidc.example-provider",  // As registered in Firebase console.
        idToken: idToken,  // ID token from OpenID Connect flow.
        rawNonce: nil
    )
    Auth.auth().signIn(with: credential) { authResult, error in
        if error {
            // Handle error.
            return
        }
        // User is signed in.
        // IdP data available in authResult?.additionalUserInfo?.profile
    }

### Objective-C

    FIROAuthCredential *credential =
        [FIROAuthProvider credentialWithProviderID:@"oidc.example-provider"  // As registered in Firebase console.
                                           IDToken:idToken  // ID token from OpenID Connect flow.
                                          rawNonce:nil];
    [[FIRAuth auth] signInWithCredential:credential
                              completion:^(FIRAuthDataResult * _Nullable authResult,
                                          NSError * _Nullable error) {
        if (error != nil) {
            // Handle error.
            return;
        }
        // User is signed in.
        // IdP data available in authResult.additionalUserInfo.profile
    }];

## Next steps

After a user signs in for the first time, a new user account is created and linked to the credentials---that is, the user name and password, phone number, or auth provider information---the user signed in with. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the[`User`](https://firebase.google.com/docs/reference/ios/firebaseauth/interface_f_i_r_user)object. See[Manage Users](https://firebase.google.com/docs/auth/ios/manage-users).

- In yourFirebase Realtime DatabaseandCloud Storage[Security Rules](https://firebase.google.com/docs/database/security/user-security), you can get the signed-in user's unique user ID from the`auth`variable, and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication providers by[linking auth provider credentials to an existing user account.](https://firebase.google.com/docs/auth/ios/account-linking)

To sign out a user, call[`signOut:`](https://firebase.google.com/docs/reference/ios/firebaseauth/interface_f_i_r_auth#ab0d5111f05c3f1906243852cc8ef41b1).  

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

You may also want to add error handling code for the full range of authentication errors. See[Handle Errors](https://firebase.google.com/docs/auth/ios/errors).