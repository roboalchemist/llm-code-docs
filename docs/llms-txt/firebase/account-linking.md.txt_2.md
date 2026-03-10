# Source: https://firebase.google.com/docs/auth/ios/account-linking.md.txt

[Video](https://www.youtube.com/watch?v=6jGNSFdHHXc) **Important** : There is a [known issue](https://github.com/firebase/firebase-js-sdk/issues/7675) that prevents `linkWithCredentials()` from working correctly in some projects. See the issue report for a workaround and the status of a fix.

You can allow users to sign in to your app using multiple authentication
providers by linking auth provider credentials to an existing user account.
Users are identifiable by the same Firebase user ID regardless of the
authentication provider they used to sign in. For example, a user who signed in
with a password can link a Google account and sign in with either method in the
future. Or, an anonymous user can link a Facebook account and then, later, sign
in with Facebook to continue using your app.

## Before you begin

Add support for two or more authentication providers (possibly including
anonymous authentication) to your app.

## Link auth provider credentials to a user account

To link auth provider credentials to an existing user account:

1. Sign in the user using any authentication provider or method.
2. Complete the sign-in flow for the new authentication provider up to, but not including, calling one of the [`FIRAuth.signInWith`](https://firebase.google.com/docs/reference/ios/firebaseauth/interface_f_i_r_auth) methods. For example, get the user's Google ID token, Facebook access token, or email and password.
3. Get a `FIRAuthCredential` for the new authentication provider:

   ##### Google Sign-In

   ###### Swift

   ```swift
   guard
     let authentication = user?.authentication,
     let idToken = authentication.idToken
   else {
     return
   }

   let credential = GoogleAuthProvider.credential(withIDToken: idToken,
                                                  accessToken: authentication.accessToken)
   ```

   ###### Objective-C

   ```objective-c
   FIRAuthCredential *credential =
   [FIRGoogleAuthProvider credentialWithIDToken:result.user.idToken.tokenString
                                    accessToken:result.user.accessToken.tokenString];
   ```

   ##### Facebook Login

   ###### Swift

   ```swift
   let credential = FacebookAuthProvider
     .credential(withAccessToken: AccessToken.current!.tokenString)
   ```

   ###### Objective-C

   ```objective-c
   FIRAuthCredential *credential = [FIRFacebookAuthProvider
       credentialWithAccessToken:[FBSDKAccessToken currentAccessToken].tokenString];
   ```

   ##### Email-password sign-in

   ###### Swift

   ```swift
   let credential = EmailAuthProvider.credential(withEmail: email, password: password)
   ```

   ###### Objective-C

   ```objective-c
   FIRAuthCredential *credential =
       [FIREmailAuthProvider credentialWithEmail:email
                                                password:password];
   ```
4. Pass the `FIRAuthCredential` object to the signed-in user's
   `linkWithCredential:completion:` method:

   ###### Swift

   ```swift
       user.link(with: credential) { authResult, error in
     // ...
   }
   }
   ```

   ###### Objective-C

   ```objective-c
       [[FIRAuth auth].currentUser linkWithCredential:credential
       completion:^(FIRAuthDataResult *result, NSError *_Nullable error) {
     // ...
   }];
   ```

   The call to `linkWithCredential:completion:` will fail if the credentials are
   already linked to another user account. In this situation, you must handle
   merging the accounts and associated data as appropriate for your app:

   #### Swift

   ```swift
   let prevUser = Auth.auth().currentUser
   Auth.auth().signIn(with: credential) { authResult, error in
       if let error = error {
         let authError = error as NSError
         if isMFAEnabled, authError.code == AuthErrorCode.secondFactorRequired.rawValue {
           // The user is a multi-factor user. Second factor challenge is required.
           let resolver = authError
             .userInfo[AuthErrorUserInfoMultiFactorResolverKey] as! MultiFactorResolver
           var displayNameString = ""
           for tmpFactorInfo in resolver.hints {
             displayNameString += tmpFactorInfo.displayName ?? ""
             displayNameString += " "
           }
           self.showTextInputPrompt(
             withMessage: "Select factor to sign in\n\(displayNameString)",
             completionBlock: { userPressedOK, displayName in
               var selectedHint: PhoneMultiFactorInfo?
               for tmpFactorInfo in resolver.hints {
                 if displayName == tmpFactorInfo.displayName {
                   selectedHint = tmpFactorInfo as? PhoneMultiFactorInfo
                 }
               }
               PhoneAuthProvider.provider()
                 .verifyPhoneNumber(with: selectedHint!, uiDelegate: nil,
                                    multiFactorSession: resolver
                                      .session) { verificationID, error in
                   if error != nil {
                     print(
                       "Multi factor start sign in failed. Error: \(error.debugDescription)"
                     )
                   } else {
                     self.showTextInputPrompt(
                       withMessage: "Verification code for \(selectedHint?.displayName ?? "")",
                       completionBlock: { userPressedOK, verificationCode in
                         let credential: PhoneAuthCredential? = PhoneAuthProvider.provider()
                           .credential(withVerificationID: verificationID!,
                                       verificationCode: verificationCode!)
                         let assertion: MultiFactorAssertion? = PhoneMultiFactorGenerator
                           .assertion(with: credential!)
                         resolver.resolveSignIn(with: assertion!) { authResult, error in
                           if error != nil {
                             print(
                               "Multi factor finanlize sign in failed. Error: \(error.debugDescription)"
                             )
                           } else {
                             self.navigationController?.popViewController(animated: true)
                           }
                         }
                       }
                     )
                   }
                 }
             }
           )
         } else {
           self.showMessagePrompt(error.localizedDescription)
           return
         }
         // ...
         return
       }
       // User is signed in
       // ...
   }
               // Merge prevUser and currentUser accounts and data
               // ...
           }
   ```

   #### Objective-C

   ```objective-c
   FIRUser *prevUser = [FIRAuth auth].currentUser;
   [[FIRAuth auth] signInWithCredential:credential
                             completion:^(FIRAuthDataResult * _Nullable authResult,
                                          NSError * _Nullable error) {
       if (isMFAEnabled && error && error.code == FIRAuthErrorCodeSecondFactorRequired) {
         FIRMultiFactorResolver *resolver = error.userInfo[FIRAuthErrorUserInfoMultiFactorResolverKey];
         NSMutableString *displayNameString = [NSMutableString string];
         for (FIRMultiFactorInfo *tmpFactorInfo in resolver.hints) {
           [displayNameString appendString:tmpFactorInfo.displayName];
           [displayNameString appendString:@" "];
         }
         [self showTextInputPromptWithMessage:[NSString stringWithFormat:@"Select factor to sign in\n%@", displayNameString]
                              completionBlock:^(BOOL userPressedOK, NSString *_Nullable displayName) {
          FIRPhoneMultiFactorInfo* selectedHint;
          for (FIRMultiFactorInfo *tmpFactorInfo in resolver.hints) {
            if ([displayName isEqualToString:tmpFactorInfo.displayName]) {
              selectedHint = (FIRPhoneMultiFactorInfo *)tmpFactorInfo;
            }
          }
          [FIRPhoneAuthProvider.provider
           verifyPhoneNumberWithMultiFactorInfo:selectedHint
           UIDelegate:nil
           multiFactorSession:resolver.session
           completion:^(NSString * _Nullable verificationID, NSError * _Nullable error) {
             if (error) {
               [self showMessagePrompt:error.localizedDescription];
             } else {
               [self showTextInputPromptWithMessage:[NSString stringWithFormat:@"Verification code for %@", selectedHint.displayName]
                                    completionBlock:^(BOOL userPressedOK, NSString *_Nullable verificationCode) {
                FIRPhoneAuthCredential *credential =
                    [[FIRPhoneAuthProvider provider] credentialWithVerificationID:verificationID
                                                                 verificationCode:verificationCode];
                FIRMultiFactorAssertion *assertion = [FIRPhoneMultiFactorGenerator assertionWithCredential:credential];
                [resolver resolveSignInWithAssertion:assertion completion:^(FIRAuthDataResult * _Nullable authResult, NSError * _Nullable error) {
                  if (error) {
                    [self showMessagePrompt:error.localizedDescription];
                  } else {
                    NSLog(@"Multi factor finanlize sign in succeeded.");
                  }
                }];
              }];
             }
           }];
        }];
       }
     else if (error) {
       // ...
       return;
     }
     // User successfully signed in. Get user data from the FIRUser object
     if (authResult == nil) { return; }
     FIRUser *user = authResult.user;
     // ...
   }];
                                       // Merge prevUser and currentUser accounts and data
                                       // ...
                                   }];
   ```

If the call to `linkWithCredential:completion:` succeeds, the user can now sign in using
any linked authentication provider and access the same Firebase data.

## Unlink an auth provider from a user account

A single Firebase user account can have multiple authentication providers linked to it (for example, email/password, Google, Facebook), which lets the user sign in to the same Firebase account through different methods.

If you unlink an authentication provider from a user's account, they can no longer sign in with that provider.
**Important:** If a user signs in again with the same provider after it has been unlinked, Firebase creates a new, separate user account instead of restoring link to the original account.

To unlink an auth provider from a user account, pass the provider ID to the
`unlink` method. You can get the provider IDs
of the auth providers linked to a user from the `providerData`
property.

#### Swift

```swift
Auth.auth().currentUser?.unlink(fromProvider: providerID!) { user, error in
  // ...
}
```

#### Objective-C

```objective-c
[[FIRAuth auth].currentUser unlinkFromProvider:providerID
                                    completion:^(FIRUser *_Nullable user, NSError *_Nullable error) {
  // ...
}];
```

## Troubleshooting

If you encounter errors when trying to link multiple accounts, see the
[documentation on
verified email addresses](https://firebase.google.com/docs/auth/users#verified_email_addresses).