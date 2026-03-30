# Source: https://firebase.google.com/docs/auth/ios/firebaseui.md.txt

<br />

![](https://firebase.google.com/static/docs/auth/images/firebaseui-ios.png)

[FirebaseUI](https://github.com/firebase/firebaseui-ios) is a library built
on top of the Firebase Authentication SDK that provides drop-in UI flows for use
in your app. FirebaseUI provides the following benefits:

- **Multiple providers**: sign-in flows for email/password, email link, phone authentication, Google Sign-In, Facebook Login, and Twitter Login.
- **Account management**: flows to handle account management tasks, such as account creation and password resets.
- **Anonymous account linking**: flows to automatically link anonymous accounts to identity providers.
- **Customizable**: customize the look of FirebaseUI to match your app. Also, because FirebaseUI is open source, you can fork the project and customize it exactly to your needs.

## Before you begin

> [!NOTE]
> **Note:** Firebase supports both CocoaPods and Swift Package Manager. If you choose to install Firebase using [Swift Package Manager](https://firebase.google.com/docs/ios/swift-package-manager), you can skip CocoaPods-related steps, like modifying Podfiles and running the `pod` command.

1. [Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup).

2. Add FirebaseUI to your Podfile:

       pod 'FirebaseUI'

   If you prefer, you can add only the Auth component and the providers you
   want to use:

       pod 'FirebaseUI/Auth'

       pod 'FirebaseUI/Google'
       pod 'FirebaseUI/Facebook'
       pod 'FirebaseUI/OAuth' # Used for Sign in with Apple, Twitter, etc
       pod 'FirebaseUI/Phone'

3. If you haven't yet connected your app to your Firebase project, do so from
   the [Firebase console](https://console.firebase.google.com/).

## Set up sign-in methods

Before you can use Firebase to sign in users, you must enable and configure the
sign-in methods you want to support.

### Email address and password

In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section and enable email
and password authentication.

### Email link authentication

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section. On the
   **Sign in method** tab, enable the **Email/Password** provider. Note
   that email or password sign-in must be enabled to use email link sign-in.

2. In the same section, enable **Email link (passwordless sign-in)** sign-in
   method and click **Save**.

3. You can enable email link sign in by initializing an `FUIEmailAuth`
   instance with `FIREmailLinkAuthSignInMethod`. You will also need to provide
   a valid `FIRActionCodeSettings` object with `handleCodeInApp` set to true.

### Swift

    var actionCodeSettings = ActionCodeSettings()
    actionCodeSettings.url = URL(string: "https://example.firebasestorage.app")
    actionCodeSettings.handleCodeInApp = true
    actionCodeSettings.setAndroidPackageName("com.firebase.example", installIfNotAvailable: false, minimumVersion: "12")

    let provider = FUIEmailAuth(authUI: FUIAuth.defaultAuthUI()!,
                                signInMethod: FIREmailLinkAuthSignInMethod,
                                forceSameDevice: false,
                                allowNewEmailAccounts: true,
                                actionCodeSetting: actionCodeSettings)

### Objective-C

    FIRActionCodeSettings *actionCodeSettings = [[FIRActionCodeSettings alloc] init];
    actionCodeSettings.URL = [NSURL URLWithString:@"https://example.firebasestorage.app"];
    actionCodeSettings.handleCodeInApp = YES;
    [actionCodeSettings setAndroidPackageName:@"com.firebase.example"
                        installIfNotAvailable:NO
                               minimumVersion:@"12"];

    id<FUIAuthProvider> provider = [[FUIEmailAuth alloc] initWithAuthUI:[FUIAuth defaultAuthUI]
                                                           signInMethod:FIREmailLinkAuthSignInMethod
                                                        forceSameDevice:NO
                                                  allowNewEmailAccounts:YES
                                                      actionCodeSetting:actionCodeSettings];

1. Additionally, you need to whitelist the URL you pass to the initializer.
   You can do so in the [Firebase console](https://console.firebase.google.com/), open the **Authentication**
   section. On the **Sign in method** tab, add the URL under
   **Authorized domains**.

2. Once you catch the deep link, you will need to pass it to the auth UI so it
   can be handled.

### Swift

    FUIAuth.defaultAuthUI()!.handleOpen(url, sourceApplication: sourceApplication)

### Objective-C

    [[FUIAuth defaultAuthUI] handleOpenURL:url sourceApplication:sourceApplication];

1. Email link sign-in in FirebaseUI-iOS is compatible with [FirebaseUI-Android](https://github.com/firebase/FirebaseUI-Android/tree/master/auth#configuring-email-link-sign-in) and [FirebaseUI-web](https://github.com/firebase/firebaseui-web#email-link-authentication) where one user starting the flow from FirebaseUI-Android can open the link and complete sign-in with FirebaseUI-web. The same is true for the opposite flow.

### Apple

1. Follow the **Before you begin** and **Comply with Apple anonymized data
   requirements** sections in
   the Firebase [Sign in with Apple](https://firebase.google.com/docs/auth/ios/apple) guide.

2. Add the Sign in with Apple capability to your entitlements file.

3. Initialize an OAuth provider instance configured for Sign in with Apple:

   <br />

   #### Swift

   ```swift
   provider = FUIOAuth.appleAuthProvider()
   ```

   #### Objective-C

   ```objective-c
   FUIOAuth *provider = [FUIOAuth appleAuthProvider];
   ```

   <br />

### Google

1. Set up the Google Sign-in using this [tutorial](https://firebase.google.com/docs/auth/ios/google-signin)

### Facebook

1. Set up the Facebook Login SDK by following
   [Facebook's getting started page](https://developers.facebook.com/docs/ios/getting-started).

2. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section and enable
   Facebook. To enable Facebook sign-in, you must provide your Facebook App ID
   and App Secret, which you can get in the Facebook Developers console.

3. Enable keychain sharing in your Xcode project from the **Project Settings \>
   Capabilities** screen.

4. Add `fbFACEBOOK_APP_ID` as a URL scheme in your
   Xcode project.

5. Add your Facebook App ID and display name to the `Info.plist` file:

   | Key | Value |
   |---|---|
   | FacebookAppID | `FACEBOOK_APP_ID` (for example, `1234567890`) |
   | FacebookDisplayName | The name of your app |

6. Initialize a Facebook provider instance:

   <br />

   #### Swift

   ```swift
   provider = FUIFacebookAuth(authUI: FUIAuth.defaultAuthUI())
   ```

   #### Objective-C

   ```objective-c
   FUIFacebookAuth *provider = [[FUIFacebookAuth alloc] initWithAuthUI:[FUIAuth defaultAuthUI]];
   ```

   <br />

7. If you want to use
   [Facebook Limited Login](https://developers.facebook.com/docs/facebook-login/limited-login/ios),
   set the `useLimitedLogin` property on the `FUIFacebookAuth` instance.

   <br />

   #### Swift

   ```swift
   provider.useLimitedLogin = true
   ```

   #### Objective-C

   ```objective-c
   provider.useLimitedLogin = YES;
   ```

   <br />

### Twitter

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section and enable
   Twitter. To enable Twitter sign-in, you must provide your Twitter API
   consumer key and secret, which you can get in the Twitter Application
   Management console.

2. Initialize an OAuth provider instance configured for Twitter login:

   <br />

   #### Swift

   ```swift
   provider = FUIOAuth.twitterAuthProvider()
   ```

   #### Objective-C

   ```objective-c
   FUIOAuth *provider = [FUIOAuth twitterAuthProvider];
   ```

   <br />

### Phone number

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section and enable
   phone number sign-in.

2. Firebase must be able to verify that phone number sign-in requests are
   coming from your app. One of the ways this is accomplished is through APNs
   notifications. See
   [Enable app verification](https://firebase.google.com/docs/auth/ios/phone-auth#enable-app-verification)
   for details.

   To enable APNs notifications for use with Firebase Authentication:
   1. In Xcode, [enable push notifications](http://help.apple.com/xcode/mac/current/#/dev11b059073?sub=dev73a37248c)
      for your project.

   2.
      Upload your APNs authentication key to Firebase.
      If you don't already have an APNs authentication key, make sure to create one in the
      [Apple Developer Member Center](https://developer.apple.com/membercenter/index.action).

      1.
         Inside your project in the Firebase console, select the
         gear icon, select
         **Project Settings** , and then select the
         **Cloud Messaging** tab.

      2.
         In **APNs authentication key** under **iOS app configuration** ,
         click the **Upload** button to upload your development authentication key, or
         production authentication key, or both. At least one is required.

      3.
         Browse to the location where you saved your key, select it, and click
         **Open** . Add the key ID for the key (available in the
         [Apple Developer Member Center](https://developer.apple.com/membercenter/index.action)) and click
         **Upload**.

      If you already have an APNs certificate, you can upload the certificate
      instead.
3. When APNs notifications can't be received on a device, Firebase uses
   reCAPTCHA to verify requests.

   To enable reCAPTCHA verification, do the following in Xcode:
   1. Open your project configuration: double-click the project name in the left tree view. Select your app from the **TARGETS** section, then select the **Info** tab, and expand the **URL Types** section.
   2. Click the **+** button, and add your Encoded App ID as a URL scheme. You can find your Encoded App ID on the [General
      Settings](https://console.firebase.google.com/project/_/settings/general/) page of the Firebase console, in the section for your iOS app. Leave the other fields blank.

      When completed, your config should look something similar to the
      following (but with your application-specific values):
      ![Screenshot of Xcode's custom URL scheme setup interface](https://firebase.google.com/static/docs/auth/images/app-id-url-scheme.png)
4. **Optional**: Firebase uses method swizzling to automatically obtain your
   app's APNs token, to handle the silent push notifications that Firebase
   sends to your app, and to automatically intercept the custom scheme redirect
   from the reCAPTCHA verification page during verification.

   If you prefer not to use swizzling, see [Appendix: Using phone sign-in without swizzling](https://firebase.google.com/docs/auth/ios/phone-auth#appendix-using-phone-sign-in-without-swizzling)
   in Firebase SDK authentication docs.

## Sign in

To kick off the FirebaseUI sign in flow, first initialize FirebaseUI:

### Swift

    import FirebaseAuthUI

    /* ... */

    FirebaseApp.configure()
    let authUI = FUIAuth.defaultAuthUI()
    // You need to adopt a FUIAuthDelegate protocol to receive callback
    authUI.delegate = self

### Objective-C

    @import FirebaseAuthUI;

    ...

    [FIRApp configure];
    FUIAuth *authUI = [FUIAuth defaultAuthUI];
    // You need to adopt a FUIAuthDelegate protocol to receive callback
    authUI.delegate = self;

Then, configure FirebaseUI to use the sign-in methods you want to support:

### Swift

    import FirebaseAuthUI
    import FirebaseFacebookAuthUI
    import FirebaseGoogleAuthUI
    import FirebaseOAuthUI
    import FirebasePhoneAuthUI

    let providers: [FUIAuthProvider] = [
      FUIGoogleAuth(),
      FUIFacebookAuth(),
      FUITwitterAuth(),
      FUIPhoneAuth(authUI:FUIAuth.defaultAuthUI()),
    ]
    self.authUI.providers = providers

### Objective-C

    @import FirebaseAuthUI;
    @import FirebaseFacebookAuthUI;
    @import FirebaseGoogleAuthUI;
    @import FirebaseOAuthUI;
    @import FirebasePhoneAuthUI;

    ...

    NSArray<id<FUIAuthProvider>> *providers = @[
      [[FUIGoogleAuth alloc] init],
      [[FUIFacebookAuth alloc] init],
      [[FUITwitterAuth alloc] init],
      [[FUIPhoneAuth alloc] initWithAuthUI:[FUIAuth defaultAuthUI]]
    ];
    _authUI.providers = providers;

If you enabled Google or Facebook sign-in, implement a handler for the result of
the Google and Facebook sign-up flows:

### Swift

    func application(_ app: UIApplication, open url: URL,
        options: [UIApplicationOpenURLOptionsKey : Any]) -> Bool {
      let sourceApplication = options[UIApplicationOpenURLOptionsKey.sourceApplication] as! String?
      if FUIAuth.defaultAuthUI()?.handleOpen(url, sourceApplication: sourceApplication) ?? false {
        return true
      }
      // other URL handling goes here.
      return false
    }

### Objective-C

    - (BOOL)application:(UIApplication *)app
                openURL:(NSURL *)url
                options:(NSDictionary *)options {
      NSString *sourceApplication = options[UIApplicationOpenURLOptionsSourceApplicationKey];
      return [[FUIAuth defaultAuthUI] handleOpenURL:url sourceApplication:sourceApplication];
    }

Finally, get an instance of `AuthViewController` from `FUIAuth`. You can then
either present it as the first view controller of your app or present it from
another view controller in your app.

### Swift

To get the sign-in method selector:

    let authViewController = authUI.authViewController()

If you only use phone number sign-in, you can display the phone number
sign-in view directly instead:

    let phoneProvider = FUIAuth.defaultAuthUI().providers.first as! FUIPhoneAuth
    phoneProvider.signIn(withPresenting: currentlyVisibleController, phoneNumber: nil)

### Objective-C

To get the sign-in method selector:

    UINavigationController *authViewController = [authUI authViewController];

If you only use phone number sign-in, you can display the phone number
sign-in view directly instead:

    FUIPhoneAuth *phoneProvider = [FUIAuth defaultAuthUI].providers.firstObject;
    [phoneProvider signInWithPresentingViewController:currentlyVisibleController phoneNumber:nil];

After you present the authentication view and the user signs in, the result is
returned to the FirebaseUI Auth delegate in the `didSignInWithUser:error:`
method:

### Swift

    func authUI(_ authUI: FUIAuth, didSignInWith user: FIRUser?, error: Error?) {
      // handle user and error as necessary
    }

### Objective-C

       - (void)authUI:(FUIAuth *)authUI
    didSignInWithUser:(nullable FIRUser *)user
                error:(nullable NSError *)error {
      // Implement this method to handle signed in user or error if any.
    }

## Sign Out

FirebaseUI provides convenience methods to sign out of Firebase Authentication
as well as all social identity providers:

### Swift

    authUI.signOut()

### Objective-C

    [authUI signOut];

## Customization

You can customize the sign-in screens by subclassing FirebaseUI's view
controllers and specifying them in `FUIAuth`'s delegate methods:

### Swift

    func authPickerViewController(forAuthUI authUI: FUIAuth) -> FUIAuthPickerViewController {
      return FUICustomAuthPickerViewController(nibName: "FUICustomAuthPickerViewController",
                                               bundle: Bundle.main,
                                               authUI: authUI)
    }

    func emailEntryViewController(forAuthUI authUI: FUIAuth) -> FUIEmailEntryViewController {
      return FUICustomEmailEntryViewController(nibName: "FUICustomEmailEntryViewController",
                                               bundle: Bundle.main,
                                               authUI: authUI)
    }

    func passwordRecoveryViewController(forAuthUI authUI: FUIAuth, email: String) -> FUIPasswordRecoveryViewController {
      return FUICustomPasswordRecoveryViewController(nibName: "FUICustomPasswordRecoveryViewController",
                                                     bundle: Bundle.main,
                                                     authUI: authUI,
                                                     email: email)
    }

    func passwordSignInViewController(forAuthUI authUI: FUIAuth, email: String) -> FUIPasswordSignInViewController {
      return FUICustomPasswordSignInViewController(nibName: "FUICustomPasswordSignInViewController",
                                                   bundle: Bundle.main,
                                                   authUI: authUI,
                                                   email: email)
    }

    func passwordSignUpViewController(forAuthUI authUI: FUIAuth, email: String) -> FUIPasswordSignUpViewController {
      return FUICustomPasswordSignUpViewController(nibName: "FUICustomPasswordSignUpViewController",
                                                   bundle: Bundle.main,
                                                   authUI: authUI,
                                                   email: email)
    }

    func passwordVerificationViewController(forAuthUI authUI: FUIAuth, email: String, newCredential: AuthCredential) -> FUIPasswordVerificationViewController {
      return FUICustomPasswordVerificationViewController(nibName: "FUICustomPasswordVerificationViewController",
                                                         bundle: Bundle.main,
                                                         authUI: authUI,
                                                         email: email,
                                                         newCredential: newCredential)
    }

### Objective-C

    - (FUIAuthPickerViewController *)authPickerViewControllerForAuthUI:(FUIAuth *)authUI {
      return [[FUICustomAuthPickerViewController alloc] initWithNibName:@"FUICustomAuthPickerViewController"
                                                                 bundle:[NSBundle mainBundle]
                                                                 authUI:authUI];
    }

    - (FUIEmailEntryViewController *)emailEntryViewControllerForAuthUI:(FUIAuth *)authUI {
      return [[FUICustomEmailEntryViewController alloc] initWithNibName:@"FUICustomEmailEntryViewController"
                                                                 bundle:[NSBundle mainBundle]
                                                                 authUI:authUI];

    }

    - (FUIPasswordSignInViewController *)passwordSignInViewControllerForAuthUI:(FUIAuth *)authUI
                                                                         email:(NSString *)email {
      return [[FUICustomPasswordSignInViewController alloc] initWithNibName:@"FUICustomPasswordSignInViewController"
                                                                     bundle:[NSBundle mainBundle]
                                                                     authUI:authUI
                                                                      email:email];

    }

    - (FUIPasswordSignUpViewController *)passwordSignUpViewControllerForAuthUI:(FUIAuth *)authUI
                                                                         email:(NSString *)email {
      return [[FUICustomPasswordSignUpViewController alloc] initWithNibName:@"FUICustomPasswordSignUpViewController"
                                                                     bundle:[NSBundle mainBundle]
                                                                     authUI:authUI
                                                                      email:email];

    }

    - (FUIPasswordRecoveryViewController *)passwordRecoveryViewControllerForAuthUI:(FUIAuth *)authUI
                                                                             email:(NSString *)email {
      return [[FUICustomPasswordRecoveryViewController alloc] initWithNibName:@"FUICustomPasswordRecoveryViewController"
                                                                       bundle:[NSBundle mainBundle]
                                                                       authUI:authUI
                                                                        email:email];

    }

    - (FUIPasswordVerificationViewController *)passwordVerificationViewControllerForAuthUI:(FUIAuth *)authUI
                                                                                     email:(NSString *)email
                                                                             newCredential:(FIRAuthCredential *)newCredential {
      return [[FUICustomPasswordVerificationViewController alloc] initWithNibName:@"FUICustomPasswordVerificationViewController"
                                                                           bundle:[NSBundle mainBundle]
                                                                           authUI:authUI
                                                                            email:email
                                                                    newCredential:newCredential];
    }

You can customize the URL to your app's terms of service, which is linked on the
account creation screen:

### Swift

    let kFirebaseTermsOfService = URL(string: "https://example.com/terms")!
    authUI.tosurl = kFirebaseTermsOfService

### Objective-C

    authUI.TOSURL = [NSURL URLWithString:@"https://example.com/terms"];

Finally, you can customize the messages and prompts shown to your users by
specifying a custom bundle:

### Swift

    authUI.customStringsBundle = NSBundle.mainBundle() // Or any custom bundle.

### Objective-C

    authUI.customStringsBundle = [NSBundle mainBundle]; // Or any custom bundle.

## Next Steps

- For more information on using and customizing FirebaseUI, see the [README](https://github.com/firebase/FirebaseUI-iOS/blob/main/FirebaseAuthUI/README.md) file on GitHub.
- If you find and issue in FirebaseUI and would like to report it, use the [GitHub issue tracker](https://github.com/firebase/FirebaseUI-iOS/issues).