# Source: https://firebase.google.com/docs/auth/ios/microsoft-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like
Microsoft Azure Active Directory by integrating web-based generic OAuth Login
into your app using the Firebase SDK to carry out the end to end sign-in flow.

## Before you begin

To sign in users using Microsoft accounts (Azure Active Directory and personal
Microsoft accounts), you must first enable Microsoft as a sign-in provider for
your Firebase project:

1. [Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup).
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
3. On the **Sign in method** tab, enable the **Microsoft** provider.
4. Add the **Client ID** and **Client Secret** from that provider's developer console to the provider configuration:
   1. To register a Microsoft OAuth client, follow the instructions in [Quickstart: Register an app with the Azure Active Directory v2.0 endpoint](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-register-an-app). Note that this endpoint supports sign-in using Microsoft personal accounts as well as Azure Active Directory accounts. [Learn more](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview) about Azure Active Directory v2.0.
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
2. Create an instance of an **OAuthProvider** using the provider ID
   **microsoft.com**.

   #### Swift

   ```swift
       var provider = OAuthProvider(providerID: "microsoft.com")
       
   ```

   #### Objective-C

   ```objective-c
       FIROAuthProvider *provider = [FIROAuthProvider providerWithProviderID:@"microsoft.com"];
       
   ```
3. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

   #### Swift

   ```swift
       provider.customParameters = [
         "prompt": "consent",
         "login_hint": "user@firstadd.onmicrosoft.com"
       ]
       
   ```

   #### Objective-C

   ```objective-c
       [provider setCustomParameters:@{@"prompt": @"consent", @"login_hint": @"user@firstadd.onmicrosoft.com"}];
       
   ```

   For the parameters Microsoft supports, see the
   [Microsoft OAuth documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code).
   Note that you can't pass Firebase-required parameters with
   `setCustomParameters`. These parameters are **client_id** ,
   **response_type** , **redirect_uri** , **state** , **scope** and
   **response_mode**.

   To allow only users from a particular Azure AD tenant to sign
   into the application, either the friendly domain name of the Azure AD tenant
   or the tenant's GUID identifier can be used. This can be done by specifying
   the "tenant" field in the custom parameters object.

   #### Swift

   ```swift
       provider.customParameters = [
         // Optional "tenant" parameter in case you are using an Azure AD
         // tenant. eg. '8eaef023-2b34-4da1-9baa-8bc8c9d6a490' or
         // 'contoso.onmicrosoft.com' or "common" for tenant-independent
         // tokens. The default value is "common".
         "tenant": "TENANT_ID"
       ]
       
   ```

   #### Objective-C

   ```objective-c
       // Optional "tenant" parameter in case you are using an Azure AD tenant.
       // eg. '8eaef023-2b34-4da1-9baa-8bc8c9d6a490' or
       // 'contoso.onmicrosoft.com' or "common" for tenant-independent tokens.
       // The default value is "common".
       provider.customParameters = @{@"tenant": @"TENANT_ID"};
       
   ```
4. **Optional**: Specify additional OAuth 2.0 scopes beyond basic profile that
   you want to request from the authentication provider.

   #### Swift

   ```swift
       provider.scopes = ["mail.read", "calendars.read"]
       
   ```

   #### Objective-C

   ```objective-c
       [provider setScopes:@[@"mail.read", @"calendars.read"]];
       
   ```

   To learn more, refer to the
   [Microsoft permissions and consent documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent).
5. **Optional** : If you want to customize the way your app presents the
   `SFSafariViewController` or `UIWebView` when
   displaying the reCAPTCHA to the user, create a custom class that conforms
   to the `AuthUIDelegate` protocol, and pass it to
   `credentialWithUIDelegate`.

6. Authenticate with Firebase using the OAuth provider object.

   #### Swift

   ```swift
       // Replace nil with the custom class that conforms to AuthUIDelegate
       // you created in last step to use a customized web view.
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
             // OAuth access token can also be retrieved:
             // ((FIROAuthCredential *)authResult.credential).accessToken
             // OAuth ID token can also be retrieved:
             // ((FIROAuthCredential *)authResult.credential).idToken
           }];
         }
       }];
       
   ```

   Using the OAuth access token, you can call the
   [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?toc=./toc.json&view=graph-rest-1.0).

   For example, to get basic profile information, you can call the REST API,
   passing the access token in the `Authorization` header:

   ```
   https://graph.microsoft.com/v1.0/me
   ```

   Unlike other providers supported by Firebase Auth, Microsoft does not
   provide a photo URL and instead, the binary data for a profile photo has to
   be requested via
   [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/api/profilephoto-get?view=graph-rest-1.0).

   In addition to the OAuth access token, the user's OAuth
   [ID token](https://docs.microsoft.com/en-us/azure/active-directory/develop/id-tokens)
   can also be retrieved from the `OAuthCredential` object. The
   `sub` claim in the ID token is app-specific and will not match the federated
   user identifier used by Firebase Auth and accessible via
   `user.providerData[0].uid`. The `oid` claim field should be used instead.
   When using a Azure AD tenant to sign-in, the `oid` claim will be an exact
   match.
   However for the non-tenant case, the `oid` field is padded. For a federated
   ID `4b2eabcdefghijkl`, the `oid` will have have a form
   `00000000-0000-0000-4b2e-abcdefghijkl`.
7. While the above examples focus on sign-in flows, you also have the
   ability to link a Microsoft provider to an existing user using
   `linkWithCredential`. For example, you can link multiple
   providers to the same user allowing them to sign in with either.

   #### Swift

   ```swift
       Auth().currentUser.link(withCredential: credential) { authResult, error in
         if error != nil {
           // Handle error.
         }
         // Microsoft credential is linked to the current user.
         // IdP data available in authResult.additionalUserInfo.profile.
         // OAuth access token can also be retrieved:
         // (authResult.credential as? OAuthCredential)?.accessToken
         // OAuth ID token can also be retrieved:
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
         // Microsoft credential is linked to the current user.
         // IdP data available in authResult.additionalUserInfo.profile.
         // OAuth access token can also be retrieved:
         // ((FIROAuthCredential *)authResult.credential).accessToken
         // OAuth ID token can also be retrieved:
         // ((FIROAuthCredential *)authResult.credential).idToken
       }];
       
   ```
8. The same pattern can be used with
   `reauthenticateWithCredential` which can be used to
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
         // Additional OAuth access token can also be retrieved:
         // (authResult.credential as? OAuthCredential)?.accessToken
         // OAuth ID token can also be retrieved:
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
         // Additional OAuth access token can also be retrieved:
         // ((FIROAuthCredential *)authResult.credential).accessToken
         // OAuth ID token can also be retrieved:
         // ((FIROAuthCredential *)authResult.credential).idToken
       }];
       
   ```

## Handling account-exists-with-different-credential Errors

If you enabled the **One account per email address** setting in the [Firebase console](https://console.firebase.google.com/),
when a user tries to sign in a to a provider (such as Microsoft) with an email that already
exists for another Firebase user's provider (such as Google), the error
`FIRAuthErrorCodeAccountExistsWithDifferentCredential` is thrown along with a temporary
`FIRAuthCredential` object (Microsoft credential). To complete the sign in to the
intended provider, the user has to sign first to the existing provider (Google) and then link to the
former `FIRAuthCredential` (Microsoft credential). This would look as illustrated below:

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