# Source: https://firebase.google.com/docs/auth/ios/password-auth.md.txt

You can use Firebase Authentication to let your users authenticate with
Firebase using their email addresses and passwords, and to manage your app's
password-based accounts.

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

Next, perform some configuration steps:

1. If you haven't yet connected your app to your Firebase project, do so from the [Firebase console](https://console.firebase.google.com/).
2. Enable Email/Password sign-in:
   1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
   2. On the **Sign in method** tab, enable the **Email/password** sign-in method and click **Save**.

## Create a password-based account

To create a new user account with a password, complete the following steps in
your app's sign-in activity:

1. Import the `FirebaseCore` module in your `UIApplicationDelegate`, as well as any other [Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods) your app delegate uses. For example, to use Cloud Firestore and Authentication:

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
2. Configure a [`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp) shared instance in your app delegate's `application(_:didFinishLaunchingWithOptions:)` method:

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
3. If you're using SwiftUI, you must create an application delegate and attach it to your `App` struct via `UIApplicationDelegateAdaptor` or `NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the [SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

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
4. When a new user signs up using your app's sign-up form, complete any new account validation steps that your app requires, such as verifying that the new account's password was correctly typed and meets your complexity requirements.
5. Create a new account by passing the new user's email address and password to `createUser`.

   #### Swift

   ```swift
   Auth.auth().createUser(withEmail: email, password: password) { authResult, error in
     // ...
   }
   ```

   #### Objective-C

   ```objective-c
   [[FIRAuth auth] createUserWithEmail:email
                              password:password
                            completion:^(FIRAuthDataResult * _Nullable authResult,
                                         NSError * _Nullable error) {
     // ...
   }];
   ```
   If the new account was successfully created, the user is signed in, and you can get the user's account data from the result object that's passed to the callback method.

To protect your project from abuse, Firebase limits the number of new email/password and anonymous sign-ups that your application can have from the same IP address in a short period of time. You can request and schedule temporary changes to this quota from the [Firebase console](https://console.firebase.google.com/project/_/authentication/providers).

## Sign in a user with an email address and password

The steps for signing in a user with a password are similar to the steps for
creating a new account. In your app's sign-in activity, do the following:

1. Import the `FirebaseCore` module in your `UIApplicationDelegate`, as well as any other [Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods) your app delegate uses. For example, to use Cloud Firestore and Authentication:

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
2. Configure a [`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp) shared instance in your app delegate's `application(_:didFinishLaunchingWithOptions:)` method:

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
3. If you're using SwiftUI, you must create an application delegate and attach it to your `App` struct via `UIApplicationDelegateAdaptor` or `NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the [SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

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
4. When a user signs in to your app, pass the user's email address and password to `signIn`.

   #### Swift

   ```swift
   Auth.auth().signIn(withEmail: email, password: password) { [weak self] authResult, error in
     guard let strongSelf = self else { return }
     // ...
   }
   ```

   #### Objective-C

   ```objective-c
   [[FIRAuth auth] signInWithEmail:self->_emailField.text
                          password:self->_passwordField.text
                        completion:^(FIRAuthDataResult * _Nullable authResult,
                                     NSError * _Nullable error) {
     // ...
   }];
   ```
   If the user successfully signs in, you can get the user's account data from the result object that's passed to the callback method.

## Recommended: Set a password policy

[Video](https://www.youtube.com/watch?v=smB-4UogJpQ)

You can improve account security by enforcing password complexity requirements.

To configure a password policy for your project, open the **Password policy**
tab on the Authentication Settings page of the Firebase console:

[Authentication Settings](https://console.firebase.google.com/project/_/authentication/settings)

Firebase Authentication password policies support the following password requirements:

- Lowercase character required

- Uppercase character required

- Numeric character required

- Non-alphanumeric character required

  The following characters satisfy the non-alphanumeric character requirement:
  `^ $ * . [ ] { } ( ) ? " ! @ # % & / \ , > < ' : ; | _ ~`
- Minimum password length (ranges from 6 to 30 characters; defaults to 6)

- Maximum password length (maximum length of 4096 characters)

You can enable password policy enforcement in two modes:

- **Require**: Attempts to sign up fail until the user updates to a password
  that complies with your policy.

- **Notify**: Users are allowed to sign up with a non-compliant password. When
  using this mode, you should check if the user's password complies with the
  policy on the client side and prompt the user in some way to update their
  password if it does not comply.

New users are always required to choose a password that complies with your
policy.

If you have active users, we recommend not enabling force upgrade on sign in
unless you intend to block access to users whose passwords don't comply with
your policy. Instead, use notify mode, which allows users to sign in with their
current passwords, and inform them of the requirements their password lacks.

## Recommended: Enable email enumeration protection

Some Firebase Authentication methods that take email addresses as parameters throw
specific errors if the email address is unregistered when it must be registered
(for example, when signing in with an email address and password), or registered
when it must be unused (for example, when changing a user's email address).
While this can be helpful for suggesting specific remedies to users, it can also
be abused by malicious actors to discover the email addresses registered by your
users.

To mitigate this risk, we recommend you [enable email enumeration protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
for your project using the Google Cloud `gcloud` tool. Note that enabling this
feature changes Firebase Authentication's error reporting behavior: be sure your app
doesn't rely on the more specific errors.

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