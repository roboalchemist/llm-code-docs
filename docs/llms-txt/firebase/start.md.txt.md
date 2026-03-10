# Source: https://firebase.google.com/docs/auth/ios/start.md.txt

You can use Firebase Authentication to allow users to sign in to your app using one or
more sign-in methods, including email address and password sign-in, and
federated identity providers such as Google Sign-in and Facebook Login. This
tutorial gets you started with Firebase Authentication by showing you how to add
email address and password sign-in to your app.

## Connect your app to Firebase

[Video](https://www.youtube.com/watch?v=q-9lx7aSWcc)

1. [Install the Firebase SDK](https://firebase.google.com/docs/ios/setup).
2. In the [Firebase console](https://console.firebase.google.com/), add your app to your Firebase project.

## Add Firebase Authentication to your app

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

**Important:** For Mac apps, enable the Keychain Sharing capability so the SDK has permission to store user entries in the keychain. For more information, see the [FAQ guide](https://firebase.google.com/docs/ios/troubleshooting-faq#macos-keychain-sharing).

## (Optional) Prototype and test with Firebase Local Emulator Suite

Before talking about how your app authenticates users, let's introduce a set of
tools you can use to prototype and test Authentication functionality:
Firebase Local Emulator Suite. If you're deciding among authentication techniques
and providers, trying out different data models with public and private data
using Authentication and Firebase Security Rules, or prototyping sign-in UI designs, being able to
work locally without deploying live services can be a great idea.

An Authentication emulator is part of the Local Emulator Suite, which
enables your app to interact with emulated database content and config, as
well as optionally your emulated project resources (functions, other databases,
and security rules).

Using the Authentication emulator involves just a few steps:

1. Adding a line of code to your app's test config to connect to the emulator.
2. From the root of your local project directory, running `firebase emulators:start`.
3. Using the Local Emulator Suite UI for interactive prototyping, or the Authentication emulator REST API for non-interactive testing.

A detailed guide is available at [Connect your app to the Authentication emulator](https://firebase.google.com/docs/emulator-suite/connect_auth).
For more information, see the [Local Emulator Suite introduction](https://firebase.google.com/docs/emulator-suite).

Now let's continue with how to authenticate users.

## Initialize the Firebase SDK

In your app delegate, first import the Firebase SDK:

### Swift

    import FirebaseCorehttps://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExampleSwift/AppDelegate.swift#L20-L20

### Objective-C

    @import FirebaseCore;https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExample/AppDelegate.m#L21-L21

Then, in the `application:didFinishLaunchingWithOptions:` method, initialize the
`FirebaseApp` object:

### Swift

    // Use Firebase library to configure APIs
    FirebaseApp.configure()https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExampleSwift/AppDelegate.swift#L40-L41

### Objective-C

    // Use Firebase library to configure APIs
    [FIRApp configure];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExample/AppDelegate.m#L34-L35

## Listen for authentication state

For each of your app's views that need information about the signed-in user,
attach a listener to the `FIRAuth` object. This listener gets called whenever
the user's sign-in state changes.

Attach the listener in the view controller's `viewWillAppear` method:

### Swift

    handle = Auth.auth().addStateDidChangeListener { auth, user in
      // ...
    }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExampleSwift/MainViewController.swift#L505-L510

### Objective-C

    self.handle = [[FIRAuth auth]
        addAuthStateDidChangeListener:^(FIRAuth *_Nonnull auth, FIRUser *_Nullable user) {
          // ...
        }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExample/MainViewController.m#L575-L581

And detach the listener in the view controller's `viewWillDisappear` method:

### Swift

    Auth.auth().removeStateDidChangeListener(handle!)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExampleSwift/MainViewController.swift#L523-L523

### Objective-C

    [[FIRAuth auth] removeAuthStateDidChangeListener:_handle];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExample/MainViewController.m#L604-L604

## Sign up new users

Create a form that allows new users to register with your app using their email
address and a password. When a user completes the form, validate the email
address and password provided by the user, then pass them to the `createUser`
method:

### Swift

    Auth.auth().createUser(withEmail: email, password: password) { authResult, error in
      // ...
    }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExampleSwift/EmailViewController.swift#L173-L184

### Objective-C

    [[FIRAuth auth] createUserWithEmail:email
                               password:password
                             completion:^(FIRAuthDataResult * _Nullable authResult,
                                          NSError * _Nullable error) {
      // ...
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExample/EmailViewController.m#L170-L184

## Sign in existing users

Create a form that allows existing users to sign in using their email address
and password. When a user completes the form, call the `signIn` method:

### Swift

    Auth.auth().signIn(withEmail: email, password: password) { [weak self] authResult, error in
      guard let strongSelf = self else { return }
      // ...
    }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExampleSwift/EmailViewController.swift#L37-L99

### Objective-C

    [[FIRAuth auth] signInWithEmail:self->_emailField.text
                           password:self->_passwordField.text
                         completion:^(FIRAuthDataResult * _Nullable authResult,
                                      NSError * _Nullable error) {
      // ...
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExample/EmailViewController.m#L36-L89

## Get user information

After a user signs in successfully, you can get information about the user. For
example, in your [authentication state listener](https://firebase.google.com/docs/auth/ios/start#listen_for_authentication_state):

### Swift

    if let user = user {
      // The user's ID, unique to the Firebase project.
      // Do NOT use this value to authenticate with your backend server,
      // if you have one. Use getTokenWithCompletion:completion: instead.
      let uid = user.uid
      let email = user.email
      let photoURL = user.photoURL
      var multiFactorString = "MultiFactor: "
      for info in user.multiFactor.enrolledFactors {
        multiFactorString += info.displayName ?? "[DispayName]"
        multiFactorString += " "
      }
      // ...
    }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExampleSwift/MainViewController.swift#L590-L636

### Objective-C

    if (user) {
      // The user's ID, unique to the Firebase project.
      // Do NOT use this value to authenticate with your backend server,
      // if you have one. Use getTokenWithCompletion:completion: instead.
      NSString *email = user.email;
      NSString *uid = user.uid;
      NSMutableString *multiFactorString = [NSMutableString stringWithFormat:@"MultiFactor: "];
      for (FIRMultiFactorInfo *info in user.multiFactor.enrolledFactors) {
        [multiFactorString appendString:info.displayName];
        [multiFactorString appendString:@" "];
      }
      NSURL *photoURL = user.photoURL;
      // ...
    }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyAuthQuickstart/AuthenticationExample/MainViewController.m#L647-L688

## Next steps

Learn how to add support for other identity providers and anonymous guest
accounts:

- [Google Sign-in](https://firebase.google.com/docs/auth/ios/google-signin)
- [Facebook Login](https://firebase.google.com/docs/auth/ios/facebook-login)
- [Twitter Login](https://firebase.google.com/docs/auth/ios/twitter-login)
- [GitHub Login](https://firebase.google.com/docs/auth/ios/github-auth)
- [Anonymous sign-in](https://firebase.google.com/docs/auth/ios/anonymous-auth)