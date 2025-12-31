# Source: https://firebase.google.com/docs/auth/web/facebook-login.md.txt

# Source: https://firebase.google.com/docs/auth/unity/facebook-login.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/facebook-login.md.txt

# Source: https://firebase.google.com/docs/auth/android/facebook-login.md.txt

# Source: https://firebase.google.com/docs/auth/ios/facebook-login.md.txt

You can let your users authenticate with Firebase using their Facebook accounts by integrating Facebook Login or Facebook Limited Login into your app.

## Before you begin

Use Swift Package Manager to install and manage Firebase dependencies.
| Visit[our installation guide](https://firebase.google.com/docs/ios/installation-methods)to learn about the different ways you can add Firebase SDKs to your Apple project, including importing frameworks directly and using CocoaPods.

1. In Xcode, with your app project open, navigate to**File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:  

```text
  https://github.com/firebase/firebase-ios-sdk.git
```
| **Note:**New projects should use the default (latest) SDK version, but you can choose an older version if needed.
3. Choose theFirebase Authenticationlibrary.
4. Add the`-ObjC`flag to the*Other Linker Flags*section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

Next, perform some configuration steps:

1. On the[Facebook for Developers](https://developers.facebook.com/)site, get the**App ID** and an**App Secret**for your app.
2. Enable Facebook Login:
   1. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Authentication**section.
   2. On the**Sign in method** tab, enable the**Facebook** sign-in method and specify the**App ID** and**App Secret**you got from Facebook.
   3. Then, make sure your**OAuth redirect URI** (e.g.`my-app-12345.firebaseapp.com/__/auth/handler`) is listed as one of your**OAuth redirect URIs** in your Facebook app's settings page on the[Facebook for Developers](https://developers.facebook.com/)site in the**Product Settings \> Facebook Login**config.

## Implement Facebook Login

To use "classic" Facebook Login, complete the following steps. Alternatively, you can use Facebook Limited Login, as shown in the next section.

1. Integrate Facebook Login into your app by following the[developer's documentation](https://developers.facebook.com/docs/facebook-login/ios). When you initialize the`FBSDKLoginButton`object, set a delegate to receive login and logout events. For example:  

   #### Swift

   ```swift
   let loginButton = FBSDKLoginButton()
   loginButton.delegate = self
   ```

   #### Objective-C

   ```objective-c
   FBSDKLoginButton *loginButton = [[FBSDKLoginButton alloc] init];
   loginButton.delegate = self;
   ```
   In your delegate, implement`didCompleteWithResult:error:`.  

   #### Swift

   ```swift
   func loginButton(_ loginButton: FBSDKLoginButton!, didCompleteWith result: FBSDKLoginManagerLoginResult!, error: Error!) {
     if let error = error {
       print(error.localizedDescription)
       return
     }
     // ...
   }
   ```

   #### Objective-C

   ```objective-c
   - (void)loginButton:(FBSDKLoginButton *)loginButton
       didCompleteWithResult:(FBSDKLoginManagerLoginResult *)result
                       error:(NSError *)error {
     if (error == nil) {
       // ...
     } else {
       NSLog(error.localizedDescription);
     }
   }
   ```
2. Import the`FirebaseCore`module in your`UIApplicationDelegate`, as well as any other[Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods)your app delegate uses. For example, to useCloud FirestoreandAuthentication:  

   #### SwiftUI

   ```swift
   import SwiftUI
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Swift

   ```swift
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Objective-C

   ```objective-c
   @import FirebaseCore;
   @import FirebaseFirestore;
   @import FirebaseAuth;
   // ...
         
   ```
3. Configure a[`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)shared instance in your app delegate's`application(_:didFinishLaunchingWithOptions:)`method:  

   #### SwiftUI

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Swift

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Objective-C

   ```objective-c
   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```
4. If you're using SwiftUI, you must create an application delegate and attach it to your`App`struct via`UIApplicationDelegateAdaptor`or`NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the[SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).  

   #### SwiftUI

   ```swift
   @main
   struct YourApp: App {
     // register app delegate for Firebase setup
     @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

     var body: some Scene {
       WindowGroup {
         NavigationView {
           ContentView()
         }
       }
     }
   }
         
   ```
5. After a user successfully signs in, in your implementation of`didCompleteWithResult:error:`, get an access token for the signed-in user and exchange it for a Firebase credential:  

   #### Swift

   ```swift
   let credential = FacebookAuthProvider
     .credential(withAccessToken: AccessToken.current!.tokenString)
   ```

   #### Objective-C

   ```objective-c
   FIRAuthCredential *credential = [FIRFacebookAuthProvider
       credentialWithAccessToken:[FBSDKAccessToken currentAccessToken].tokenString];
   ```

## Implement Facebook Limited Login

To use Facebook Limited Login instead of "classic" Facebook Login, complete the following steps.

1. Integrate Facebook Limited Login into your app by following the[developer's documentation](https://developers.facebook.com/docs/facebook-login/limited-login/ios).
2. For every sign-in request, generate a unique random string---a "nonce"---which you will use to make sure the ID token you get was granted specifically in response to your app's authentication request. This step is important to prevent replay attacks. You can generate a cryptographically secure nonce with`SecRandomCopyBytes(_:_:_)`, as in the following example:  

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
   You will send the SHA-256 hash of the nonce with your sign-in request, which Facebook will pass unchanged in the response. Firebase validates the response by hashing the original nonce and comparing it to the value passed by Facebook.  

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
3. When you set up the`FBSDKLoginButton`, set a delegate to receive login and logout events, set the tracking mode to`FBSDKLoginTrackingLimited`, and attach a nonce. For example:  

   #### Swift

   ```swift
   func setupLoginButton() {
       let nonce = randomNonceString()
       currentNonce = nonce
       loginButton.delegate = self
       loginButton.loginTracking = .limited
       loginButton.nonce = sha256(nonce)
   }
           
   ```

   #### Objective-C

   ```objective-c
   - (void)setupLoginButton {
     NSString *nonce = [self randomNonce:32];
     self.currentNonce = nonce;
     self.loginButton.delegate = self;
     self.loginButton.loginTracking = FBSDKLoginTrackingLimited
     self.loginButton.nonce = [self stringBySha256HashingString:nonce];
   }
           
   ```
   In your delegate, implement`didCompleteWithResult:error:`.  

   #### Swift

   ```swift
   func loginButton(_ loginButton: FBSDKLoginButton!, didCompleteWith result: FBSDKLoginManagerLoginResult!, error: Error!) {
     if let error = error {
       print(error.localizedDescription)
       return
     }
     // ...
   }
           
   ```

   #### Objective-C

   ```objective-c
   - (void)loginButton:(FBSDKLoginButton *)loginButton
       didCompleteWithResult:(FBSDKLoginManagerLoginResult *)result
                       error:(NSError *)error {
     if (error == nil) {
       // ...
     } else {
       NSLog(error.localizedDescription);
     }
   }
           
   ```
4. Import the`FirebaseCore`module in your`UIApplicationDelegate`, as well as any other[Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods)your app delegate uses. For example, to useCloud FirestoreandAuthentication:  

   #### SwiftUI

   ```swift
   import SwiftUI
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Swift

   ```swift
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Objective-C

   ```objective-c
   @import FirebaseCore;
   @import FirebaseFirestore;
   @import FirebaseAuth;
   // ...
         
   ```
5. Configure a[`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)shared instance in your app delegate's`application(_:didFinishLaunchingWithOptions:)`method:  

   #### SwiftUI

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Swift

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Objective-C

   ```objective-c
   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```
6. If you're using SwiftUI, you must create an application delegate and attach it to your`App`struct via`UIApplicationDelegateAdaptor`or`NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the[SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).  

   #### SwiftUI

   ```swift
   @main
   struct YourApp: App {
     // register app delegate for Firebase setup
     @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

     var body: some Scene {
       WindowGroup {
         NavigationView {
           ContentView()
         }
       }
     }
   }
         
   ```
7. After a user successfully signs in, in your implementation of`didCompleteWithResult:error:`, use the ID token from Facebook's response with the unhashed nonce to get a Firebase credential:  

   #### Swift

   ```swift
   // Initialize a Firebase credential.
   let idTokenString = AuthenticationToken.current?.tokenString
   let nonce = currentNonce
   let credential = OAuthProvider.credential(withProviderID: "facebook.com",
                                             idToken: idTokenString!,
                                             rawNonce: nonce)
           
   ```

   #### Objective-C

   ```objective-c
   // Initialize a Firebase credential.
   NSString *idTokenString = FBSDKAuthenticationToken.currentAuthenticationToken.tokenString;
   NSString *rawNonce = self.currentNonce;
   FIROAuthCredential *credential = [FIROAuthProvider credentialWithProviderID:@"facebook.com"
                                                                       IDToken:idTokenString
                                                                      rawNonce:rawNonce];
           
   ```

## Authenticate with Firebase

Finally, authenticate with Firebase using the Firebase credential:  

#### Swift

```swift
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
    
```

#### Objective-C

```objective-c
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
    
```

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