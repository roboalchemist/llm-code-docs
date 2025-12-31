# Source: https://firebase.google.com/docs/auth/web/custom-auth.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/custom-auth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/custom-auth.md.txt

# Source: https://firebase.google.com/docs/auth/android/custom-auth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/custom-auth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/custom-auth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/custom-auth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/custom-auth.md.txt

You can integrateFirebase Authenticationwith a custom authentication system by modifying your authentication server to produce custom signed tokens when a user successfully signs in. Your app receives this token and uses it to authenticate with Firebase.

## Before you begin

1. [Create a Firebase project and register your app](https://firebase.google.com/docs/ios/setup)if you haven't already.
2. Use Swift Package Manager to install and manage Firebase dependencies.

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
3. Get your project's server keys:
   1. Go to the[Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)page in your project's settings.
   2. Click*Generate New Private Key* at the bottom of the*Firebase Admin SDK* section of the*Service Accounts*page.
   3. The new service account's public/private key pair is automatically saved on your computer. Copy this file to your authentication server.

## Authenticate with Firebase

1. Import the`FirebaseCore`module in your`UIApplicationDelegate`, as well as any other[Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods)your app delegate uses. For example, to useCloud FirestoreandAuthentication:  

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
2. Configure a[`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)shared instance in your app delegate's`application(_:didFinishLaunchingWithOptions:)`method:  

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
3. If you're using SwiftUI, you must create an application delegate and attach it to your`App`struct via`UIApplicationDelegateAdaptor`or`NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the[SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).  

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
4. When users sign in to your app, send their sign-in credentials (for example, their username and password) to your authentication server. Your server checks the credentials and returns a[custom token](https://firebase.google.com/docs/auth/admin/create-custom-tokens)if they are valid.
5. After you receive the custom token from your authentication server, pass it to`signInWithCustomToken`to sign in the user:  

   #### Swift

   ```swift
   Auth.auth().signIn(withCustomToken: customToken ?? "") { user, error in
     // ...
   }
   ```

   #### Objective-C

   ```objective-c
   [[FIRAuth auth] signInWithCustomToken:customToken
                              completion:^(FIRAuthDataResult * _Nullable authResult,
                                           NSError * _Nullable error) {
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