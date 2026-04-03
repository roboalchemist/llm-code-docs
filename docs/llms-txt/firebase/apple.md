# Source: https://firebase.google.com/docs/auth/web/apple.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/apple.md.txt

# Source: https://firebase.google.com/docs/auth/android/apple.md.txt

# Source: https://firebase.google.com/docs/auth/unity/apple.md.txt

# Source: https://firebase.google.com/docs/auth/ios/apple.md.txt

# Source: https://firebase.google.com/docs/auth/unity/apple.md.txt

# Source: https://firebase.google.com/docs/auth/ios/apple.md.txt

You can let your users authenticate with Firebase using their Apple ID by using the Firebase SDK to carry out the end-to-end OAuth 2.0 sign-in flow.
| **Important**: To sign in with an Apple account, users must:
|
| - Have an Apple ID with two-factor authentication (2FA) enabled.
| - Be signed in to iCloud on an Apple device.
|
| See[How to use Sign in with Apple](https://support.apple.com/en-us/HT210318). You will also need to meet these requirements to test your integration with Sign In with Apple.

## Before you begin

To sign in users using Apple, first configure Sign In with Apple on Apple's developer site, then enable Apple as a sign-in provider for your Firebase project.

### Join the Apple Developer Program

Sign In with Apple can only be configured by members of the[Apple Developer Program](https://developer.apple.com/programs/).

### Configure Sign In with Apple

1. Enable Sign In with Apple for your app on the[Certificates, Identifiers \& Profiles](https://developer.apple.com/account/resources)page of Apple's developer site.
2. Associate your website with your app as described in the first section of[Configure Sign In with Apple for the web](https://developer.apple.com/help/account/configure-app-capabilities/configure-sign-in-with-apple-for-the-web). When prompted, register the following URL as a Return URL:  

   ```
   https://YOUR_FIREBASE_PROJECT_ID.firebaseapp.com/__/auth/handler
   ```
   You can get your Firebase project ID on the[Firebaseconsole settings page](https://console.firebase.google.com/project/_/settings/general/). When you're done, take note of your new Service ID, which you'll need in the next section.
3. [Create a Sign In with Apple private key](https://developer.apple.com/help/account/configure-app-capabilities/create-a-sign-in-with-apple-private-key/). You'll need your new private key and key ID in the next section.
4. If you use any ofFirebase Authentication's features that send emails to users, including email link sign-in, email address verification, account change revocation, and others,[configure the Apple private email relay service](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service/)and register`noreply@`<var translate="no">YOUR_FIREBASE_PROJECT_ID</var>`.firebaseapp.com`(or your customized email template domain) so Apple can relay emails sent byFirebase Authenticationto anonymized Apple email addresses.

### Enable Apple as a sign-in provider

1. [Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup). Be sure to register your app's bundle ID when you set up your app in theFirebaseconsole.
2. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth** section. On the**Sign in method** tab, enable the**Apple** provider. Specify the Service ID you created in the previous section. Also, in the**OAuth code flow configuration section**, specify your Apple Team ID and the private key and key ID you created in the previous section.

## Comply with Apple anonymized data requirements

Sign In with Apple gives users the option of anonymizing their data, including their email address, when signing in. Users who choose this option have email addresses with the domain`privaterelay.appleid.com`. When you use Sign In with Apple in your app, you must comply with any applicable developer policies or terms from Apple regarding these anonymized Apple IDs.

This includes obtaining any required user consent before you associate any directly identifying personal information with an anonymized Apple ID. When using Firebase Authentication, this may include the following actions:

- Link an email address to an anonymized Apple ID or vice versa.
- Link a phone number to an anonymized Apple ID or vice versa
- Link a non-anonymous social credential (Facebook, Google, etc) to an anonymized Apple ID or vice versa.

The above list is not exhaustive. Refer to the Apple Developer Program License Agreement in the Membership section of your developer account to make sure your app meets Apple's requirements.

## Sign in with Apple and authenticate with Firebase

To authenticate with an Apple account, first sign the user in to their Apple account using Apple's[`AuthenticationServices`framework](https://developer.apple.com/documentation/authenticationservices), and then use the ID token from Apple's response to create a Firebase`AuthCredential`object:

1. For every sign-in request, generate a random string---a "nonce"---which you will use to make sure the ID token you get was granted specifically in response to your app's authentication request. This step is important to prevent replay attacks.

   You can generate a cryptographically secure nonce with`SecRandomCopyBytes(_:_:_)`, as in the following example:  

   #### Swift

   ```swift
   private func randomNonceString(length: Int = 32) -> String {
     precondition(length > 0)
     var randomBytes = [UInt8](repeating: 0, count: length)
     let errorCode = SecRandomCopyBytes(kSecRandomDefault, randomBytes.count, &randomBytes)
     if errorCode != errSecSuccess {
       fatalError(
         "Unable to generate nonce. SecRandomCopyBytes failed with OSStatus \(errorCode)"
       )
     }

     let charset: [Character] =
       Array("0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz-._")

     let nonce = randomBytes.map { byte in
       // Pick a random character from the set, wrapping around if needed.
       charset[Int(byte) % charset.count]
     }

     return String(nonce)
   }

       
   ```

   #### Objective-C

   ```objective-c
   // Adapted from https://auth0.com/docs/api-auth/tutorials/nonce#generate-a-cryptographically-random-nonce
   - (NSString *)randomNonce:(NSInteger)length {
     NSAssert(length > 0, @"Expected nonce to have positive length");
     NSString *characterSet = @"0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz-._";
     NSMutableString *result = [NSMutableString string];
     NSInteger remainingLength = length;

     while (remainingLength > 0) {
       NSMutableArray *randoms = [NSMutableArray arrayWithCapacity:16];
       for (NSInteger i = 0; i < 16; i++) {
         uint8_t random = 0;
         int errorCode = SecRandomCopyBytes(kSecRandomDefault, 1, &random);
         NSAssert(errorCode == errSecSuccess, @"Unable to generate nonce: OSStatus %i", errorCode);

         [randoms addObject:@(random)];
       }

       for (NSNumber *random in randoms) {
         if (remainingLength == 0) {
           break;
         }

         if (random.unsignedIntValue < characterSet.length) {
           unichar character = [characterSet characterAtIndex:random.unsignedIntValue];
           [result appendFormat:@"%C", character];
           remainingLength--;
         }
       }
     }

     return [result copy];
   }
       
   ```

   You will send the SHA256 hash of the nonce with your sign-in request, which Apple will pass unchanged in the response. Firebase validates the response by hashing the original nonce and comparing it to the value passed by Apple.  

   #### Swift

   ```swift
   @available(iOS 13, *)
   private func sha256(_ input: String) -> String {
     let inputData = Data(input.utf8)
     let hashedData = SHA256.hash(data: inputData)
     let hashString = hashedData.compactMap {
       String(format: "%02x", $0)
     }.joined()

     return hashString
   }

       
   ```

   #### Objective-C

   ```objective-c
   - (NSString *)stringBySha256HashingString:(NSString *)input {
     const char *string = [input UTF8String];
     unsigned char result[CC_SHA256_DIGEST_LENGTH];
     CC_SHA256(string, (CC_LONG)strlen(string), result);

     NSMutableString *hashed = [NSMutableString stringWithCapacity:CC_SHA256_DIGEST_LENGTH * 2];
     for (NSInteger i = 0; i < CC_SHA256_DIGEST_LENGTH; i++) {
       [hashed appendFormat:@"%02x", result[i]];
     }
     return hashed;
   }
       
   ```
2. Start Apple's sign-in flow, including in your request the SHA256 hash of the nonce and the delegate class that will handle Apple's response (see the next step):

   ### Swift

       import CryptoKit

       // Unhashed nonce.
       fileprivate var currentNonce: String?

       @available(iOS 13, *)
       func startSignInWithAppleFlow() {
         let nonce = randomNonceString()
         currentNonce = nonce
         let appleIDProvider = ASAuthorizationAppleIDProvider()
         let request = appleIDProvider.createRequest()
         request.requestedScopes = [.fullName, .email]
         request.nonce = sha256(nonce)

         let authorizationController = ASAuthorizationController(authorizationRequests: [request])
         authorizationController.delegate = self
         authorizationController.presentationContextProvider = self
         authorizationController.performRequests()
       }

   ### Objective-C

       @import CommonCrypto;

       - (void)startSignInWithAppleFlow {
         NSString *nonce = [self randomNonce:32];
         self.currentNonce = nonce;
         ASAuthorizationAppleIDProvider *appleIDProvider = [[ASAuthorizationAppleIDProvider alloc] init];
         ASAuthorizationAppleIDRequest *request = [appleIDProvider createRequest];
         request.requestedScopes = @[ASAuthorizationScopeFullName, ASAuthorizationScopeEmail];
         request.nonce = [self stringBySha256HashingString:nonce];

         ASAuthorizationController *authorizationController =
             [[ASAuthorizationController alloc] initWithAuthorizationRequests:@[request]];
         authorizationController.delegate = self;
         authorizationController.presentationContextProvider = self;
         [authorizationController performRequests];
       }

3. Handle Apple's response in your implementation of`ASAuthorizationControllerDelegate`. If sign-in was successful, use the ID token from Apple's response with the unhashed nonce to authenticate with Firebase:

   ### Swift

       @available(iOS 13.0, *)
       extension MainViewController: ASAuthorizationControllerDelegate {

         func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization authorization: ASAuthorization) {
           if let appleIDCredential = authorization.credential as? ASAuthorizationAppleIDCredential {
             guard let nonce = currentNonce else {
               fatalError("Invalid state: A login callback was received, but no login request was sent.")
             }
             guard let appleIDToken = appleIDCredential.identityToken else {
               print("Unable to fetch identity token")
               return
             }
             guard let idTokenString = String(data: appleIDToken, encoding: .utf8) else {
               print("Unable to serialize token string from data: \(appleIDToken.debugDescription)")
               return
             }
             // Initialize a Firebase credential, including the user's full name.
             let credential = OAuthProvider.appleCredential(withIDToken: idTokenString,
                                                               rawNonce: nonce,
                                                               fullName: appleIDCredential.fullName)
             // Sign in with Firebase.
             Auth.auth().signIn(with: credential) { (authResult, error) in
               if error {
                 // Error. If error.code == .MissingOrInvalidNonce, make sure
                 // you're sending the SHA256-hashed nonce as a hex string with
                 // your request to Apple.
                 print(error.localizedDescription)
                 return
               }
               // User is signed in to Firebase with Apple.
               // ...
             }
           }
         }

         func authorizationController(controller: ASAuthorizationController, didCompleteWithError error: Error) {
           // Handle error.
           print("Sign in with Apple errored: \(error)")
         }

       }

   ### Objective-C

       - (void)authorizationController:(ASAuthorizationController *)controller
          didCompleteWithAuthorization:(ASAuthorization *)authorization API_AVAILABLE(ios(13.0)) {
         if ([authorization.credential isKindOfClass:[ASAuthorizationAppleIDCredential class]]) {
           ASAuthorizationAppleIDCredential *appleIDCredential = authorization.credential;
           NSString *rawNonce = self.currentNonce;
           NSAssert(rawNonce != nil, @"Invalid state: A login callback was received, but no login request was sent.");

           if (appleIDCredential.identityToken == nil) {
             NSLog(@"Unable to fetch identity token.");
             return;
           }

           NSString *idToken = [[NSString alloc] initWithData:appleIDCredential.identityToken
                                                     encoding:NSUTF8StringEncoding];
           if (idToken == nil) {
             NSLog(@"Unable to serialize id token from data: %@", appleIDCredential.identityToken);
           }

           // Initialize a Firebase credential, including the user's full name.
           FIROAuthCredential *credential = [FIROAuthProvider appleCredentialWithIDToken:IDToken
                                                                                rawNonce:self.appleRawNonce
                                                                                fullName:appleIDCredential.fullName];

           // Sign in with Firebase.
           [[FIRAuth auth] signInWithCredential:credential
                                     completion:^(FIRAuthDataResult * _Nullable authResult,
                                                  NSError * _Nullable error) {
             if (error != nil) {
               // Error. If error.code == FIRAuthErrorCodeMissingOrInvalidNonce,
               // make sure you're sending the SHA256-hashed nonce as a hex string
               // with your request to Apple.
               return;
             }
             // Sign-in succeeded!
           }];
         }
       }

       - (void)authorizationController:(ASAuthorizationController *)controller
                  didCompleteWithError:(NSError *)error API_AVAILABLE(ios(13.0)) {
         NSLog(@"Sign in with Apple errored: %@", error);
       }

Unlike other providers supported by Firebase Auth, Apple does not provide a photo URL.

Also, when the user chooses not to share their email with the app, Apple provisions a unique email address for that user (of the form`xyz@privaterelay.appleid.com`), which it shares with your app. If you configured the private email relay service, Apple forwards emails sent to the anonymized address to the user's real email address.
| **Important:** Apple only shares user information such as the display name with apps the first time a user signs in. Use`OAuthProvider.appleCredential(withIDToken:rawNonce:fullName:)`to make sure Firebase stores the display name the first time a user signs in with Apple. You can later retrieve the user's full name with`Auth.auth().currentUser.displayName`. However, if you previously used Apple to sign a user in to the app without using Firebase, Apple will not provide Firebase with the user's display name.

### Reauthentication and account linking

The same pattern can be used with`reauthenticateWithCredential()`, which you can use to retrieve a fresh credential for sensitive operations that require recent sign-in:  

### Swift

    // Initialize a fresh Apple credential with Firebase.
    let credential = OAuthProvider.credential(
      withProviderID: "apple.com",
      IDToken: appleIdToken,
      rawNonce: rawNonce
    )
    // Reauthenticate current Apple user with fresh Apple credential.
    Auth.auth().currentUser.reauthenticate(with: credential) { (authResult, error) in
      guard error != nil else { return }
      // Apple user successfully re-authenticated.
      // ...
    }

### Objective-C

    FIRAuthCredential *credential = [FIROAuthProvider credentialWithProviderID:@"apple.com",
                                                                       IDToken:appleIdToken,
                                                                      rawNonce:rawNonce];
    [[FIRAuth auth].currentUser
        reauthenticateWithCredential:credential
                          completion:^(FIRAuthDataResult * _Nullable authResult,
                                       NSError * _Nullable error) {
      if (error) {
        // Handle error.
      }
      // Apple user successfully re-authenticated.
      // ...
    }];

And, you can use`linkWithCredential()`to link different identity providers to existing accounts.

Note that Apple requires you to get explicit consent from users before you link their Apple accounts to other data.

Sign in with Apple will not allow you to reuse an auth credential to link to an existing account. If you want to link a Sign in with Apple credential to another account, you must first attempt to link the accounts using the old Sign in with Apple credential and then examine the error returned to find a new credential. The new credential will be located in the error's`userInfo`dictionary and can be accessed via the`AuthErrorUserInfoUpdatedCredentialKey`key.

For example, to link a Facebook account to the current Firebase account, use the access token you got from signing the user in to Facebook:  

### Swift

    // Initialize a Facebook credential with Firebase.
    let credential = FacebookAuthProvider.credential(
      withAccessToken: AccessToken.current!.tokenString
    )
    // Assuming the current user is an Apple user linking a Facebook provider.
    Auth.auth().currentUser.link(with: credential) { (authResult, error) in
      // Facebook credential is linked to the current Apple user.
      // The user can now sign in with Facebook or Apple to the same Firebase
      // account.
      // ...
    }

### Objective-C

    // Initialize a Facebook credential with Firebase.
    FacebookAuthCredential *credential = [FIRFacebookAuthProvider credentialWithAccessToken:accessToken];
    // Assuming the current user is an Apple user linking a Facebook provider.
    [FIRAuth.auth linkWithCredential:credential completion:^(FIRAuthDataResult * _Nullable authResult, NSError * _Nullable error) {
      // Facebook credential is linked to the current Apple user.
      // The user can now sign in with Facebook or Apple to the same Firebase
      // account.
      // ...
    }];

## Token revocation

Apple requires that apps that support account creation must let users initiate deletion of their account within the app, as described in the[App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#5.1.1v)

To meet this requirement, implement the following steps:

1. Make sure you filled out the*Services ID* and*OAuth code flow configuration* section of the Sign in with Apple provider configuration, as outlined in the[Configure Sign in with Apple](https://firebase.google.com/docs/auth/ios/apple#configure_sign_in_with_apple)section.

2. Since Firebase does not store user tokens when users are created with Sign in with Apple, you must ask the user to sign in again before revoking their token and deleting the account.

   ### Swift

   ```swift
   private var currentNonce: String?

   private func deleteCurrentUser() {
     do {
       let nonce = try CryptoUtils.randomNonceString()
       currentNonce = nonce
       let appleIDProvider = ASAuthorizationAppleIDProvider()
       let request = appleIDProvider.createRequest()
       request.requestedScopes = [.fullName, .email]
       request.nonce = CryptoUtils.sha256(nonce)

       let authorizationController = ASAuthorizationController(authorizationRequests: [request])
       authorizationController.delegate = self
       authorizationController.presentationContextProvider = self
       authorizationController.performRequests()
     } catch {
       // In the unlikely case that nonce generation fails, show error view.
       displayError(error)
     }
   }
   ```
3. Obtain the authorization code from the`ASAuthorizationAppleIDCredential`, and use it to call`Auth.auth().revokeToken(withAuthorizationCode:)`to revoke the user's tokens.

   ### Swift

   ```swift
   private var user: User?

   func authorizationController(controller: ASAuthorizationController,
                                didCompleteWithAuthorization authorization: ASAuthorization) {
     guard let appleIDCredential = authorization.credential as? ASAuthorizationAppleIDCredential
     else {
       print("Unable to retrieve AppleIDCredential")
       return
     }

     guard let _ = currentNonce else {
       fatalError("Invalid state: A login callback was received, but no login request was sent.")
     }

     guard let appleAuthCode = appleIDCredential.authorizationCode else {
       print("Unable to fetch authorization code")
       return
     }

     guard let authCodeString = String(data: appleAuthCode, encoding: .utf8) else {
       print("Unable to serialize auth code string from data: \(appleAuthCode.debugDescription)")
       return
     }

     Task {
       do {
         try await Auth.auth().revokeToken(withAuthorizationCode: authCodeString)
         try await user?.delete()
         self.updateUI()
       } catch {
         self.displayError(error)
       }
     }
   }
   ```
4. Finally,[delete the user account](https://firebase.google.com/docs/auth/ios/manage-users#delete_a_user)(and all associated data)

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