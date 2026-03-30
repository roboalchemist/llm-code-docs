# Source: https://firebase.google.com/docs/auth/ios/google-signin.md.txt

[Video](https://www.youtube.com/watch?v=IzyOdKm0bWE)

You can let your users authenticate with Firebase using their Google Accounts by
integrating Google Sign-In into your app.

## Before you begin

Use Swift Package Manager to install and manage Firebase dependencies.

> [!NOTE]
> Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods) to learn about the different ways you can add Firebase SDKs to your Apple project.

1. In Xcode, with your app project open, navigate to **File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk.git
```

> [!NOTE]
> **Note:** New projects should use the default (latest) SDK version, but you can choose an older version if needed.

3. Choose the Firebase Authentication library.
4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

## Add the Google Sign-In SDK to your project

1. In Xcode, with your app project open, navigate to **File \> Add Packages**.

2. When prompted, add the Google Sign-In SDK repository:

       https://github.com/google/GoogleSignIn-iOS

3. When finished, Xcode will automatically begin resolving and downloading your
   dependencies in the background.

## Enable Google Sign-In for your Firebase project

To allow users to sign in using Google Sign-In, you must first enable the
Google Sign-In provider for your Firebase project:

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section.
2. On the **Sign in method** tab, enable the **Google** provider.
3. Click **Save**.

4. Download a new copy of your project's `GoogleService-Info.plist` file and
   copy it to your Xcode project. Overwrite any existing versions with the new
   one. (See [Add Firebase to your iOS
   project](https://firebase.google.com/docs/ios/setup#add-config-file).)

## Import the required header files

First, you must import the Firebase SDK and Google Sign-In SDK header files into
your app.

#### Swift

```swift
import FirebaseAuth
import GoogleSignIn
```

#### Objective-C

```objective-c
@import FirebaseCore;
@import GoogleSignIn;
```

## Implement Google Sign-In

Implement Google Sign-In by following these steps. See the [Google Sign-In
developer documentation](https://developers.google.com/identity/sign-in/ios) for details on using Google
Sign-In with iOS.

1. Add custom URL schemes to your Xcode project:
   1. Open your project configuration: click the project name in the left tree view. Select your app from the **TARGETS** section, then select the **Info** tab, and expand the **URL Types** section.
   2. Click the **+** button, and add a URL scheme for your reversed client ID. To find this value, open the `` `GoogleService-Info.plist` `` configuration file, and look for the `REVERSED_CLIENT_ID` key. Copy the value of that key, and paste it into the **URL Schemes** box on the configuration page. Leave the other fields untouched.

      When completed, your config should look something similar to the
      following (but with your application-specific values):
      ![](https://firebase.google.com/static/docs/auth/images/xcode_infotab_url_type_values.png)
2. In your app delegate's `application:didFinishLaunchingWithOptions:` method, configure the `FirebaseApp` object.

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
3. Implement the `application:openURL:options:` method of your app delegate. The method should call the `handleURL` method of the `GIDSignIn` instance, which will properly handle the URL that your application receives at the end of the authentication process.

   #### Swift

   ```swift
   func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
     // ...
   }
     return GIDSignIn.sharedInstance.handle(url)
   }
   ```

   #### Objective-C

   ```objective-c
   - (BOOL)application:(nonnull UIApplication *)application
               openURL:(nonnull NSURL *)url
               options:(nonnull NSDictionary<NSString *, id> *)options {
     return [[GIDSignIn sharedInstance] handleURL:url];
   }
   ```
4. Pass the presenting view controller and client ID for your app to the `signIn` method of the Google Sign-In provider and create a Firebase Authentication credential from the resulting Google auth token:

   #### Swift

   ```swift
   guard let clientID = FirebaseApp.app()?.options.clientID else { return }

   // Create Google Sign In configuration object.
   let config = GIDConfiguration(clientID: clientID)
   GIDSignIn.sharedInstance.configuration = config

   // Start the sign in flow!
   GIDSignIn.sharedInstance.signIn(withPresenting: viewController) { result, error in
     guard error == nil else {
       // ...
       return
     }

     guard let user = result?.user,
           let idToken = user.idToken?.tokenString
     else {
       // ...
       return
     }

     let credential = GoogleAuthProvider.credential(withIDToken: idToken,
                                                    accessToken: user.accessToken.tokenString)
     self.signIn(with: credential)
   }
   ```

   #### Objective-C

   ```objective-c
   GIDConfiguration *config = [[GIDConfiguration alloc] initWithClientID:[FIRApp defaultApp].options.clientID];
   [GIDSignIn.sharedInstance setConfiguration:config];

   __weak __auto_type weakSelf = self;
   [GIDSignIn.sharedInstance signInWithPresentingViewController:self
         completion:^(GIDSignInResult * _Nullable result, NSError * _Nullable error) {
     __auto_type strongSelf = weakSelf;
     if (strongSelf == nil) { return; }

     if (error == nil) {
       FIRAuthCredential *credential =
       [FIRGoogleAuthProvider credentialWithIDToken:result.user.idToken.tokenString
                                        accessToken:result.user.accessToken.tokenString];
       // ...
     } else {
       // ...
     }
   }];
   ```
5. Add a `GIDSignInButton` to your storyboard, XIB file, or instantiate it programmatically. To add the button to your storyboard or XIB file, add a View and set its custom class to `GIDSignInButton`.

   > [!NOTE]
   > When you add a `GIDSignInButton` view to your storyboard, the sign-in button doesn't render in the interface builder. Run the app to see the sign-in button.

6. **Optional** : If you want to customize the button, do the following:

   #### Swift

   1. In your view controller, declare the sign-in button as a property.

      ```swift
      @IBOutlet weak var signInButton: GIDSignInButton!
      ```
   2. Connect the button to the `signInButton` property you just declared.
   3. Customize the button by setting the properties of the [GIDSignInButton](https://developers.google.com/identity/sign-in/ios/api/interface_g_i_d_sign_in_button#property-summary) object.

   #### Objective-C

   1. In your view controller's header file, declare the sign-in button as a property.

      ```objective-c
      @property(weak, nonatomic) IBOutlet GIDSignInButton *signInButton;
      ```
   2. Connect the button to the `signInButton` property you just declared.
   3. Customize the button by setting the properties of the [GIDSignInButton](https://developers.google.com/identity/sign-in/ios/api/interface_g_i_d_sign_in_button#property-summary) object.

## Authenticate with Firebase

Finally, complete the Firebase login process with the auth credential created
in the previous step.

#### Swift

```swift
Auth.auth().signIn(with: credential) { result, error in
  guard error == nil else {
    // ...
    return
  }

  // At this point, our user is signed in
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