# Source: https://firebase.google.com/docs/auth/ios/email-link-auth.md.txt

> [!NOTE]
> **Note**: The legacy implementation of email link authentication and actions in SDK versions
> lower than Android SDK v23.2.0 and iOS SDK 11.8.0 uses Firebase Dynamic Links, which will be
> shut down on August 25, 2025.
>
>
> This guide has been updated to refer to the new solution in later SDK versions.
>
> For specific information and migration guidance, visit the
> [Dynamic Links
> Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq#impacts-on-email-link-authentication).

You can use Firebase Authentication to sign in a user by sending them an email
containing a link, which they can click to sign in. In the process, the user's
email address is also verified.

There are numerous benefits to signing in by email:

- Low friction sign-up and sign-in.
- Lower risk of password reuse across applications, which can undermine security of even well-selected passwords.
- The ability to authenticate a user while also verifying that the user is the legitimate owner of an email address.
- A user only needs an accessible email account to sign in. No ownership of a phone number or social media account is required.
- A user can sign in securely without the need to provide (or remember) a password, which can be cumbersome on a mobile device.
- An existing user who previously signed in with an email identifier (password or federated) can be upgraded to sign in with just the email. For example, a user who has forgotten their password can still sign in without needing to reset their password.

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

## Enable Email Link sign-in for your Firebase project

To sign in users by email link, you must first enable the Email provider and
Email link sign-in method for your Firebase project:

1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
2. On the **Sign in method** tab, enable the **Email/Password** provider. Note that email/password sign-in must be enabled to use email link sign-in.
3. In the same section, enable **Email link (passwordless sign-in)** sign-in method.
4. Click **Save**.

## Send an authentication link to the user's email address

To initiate the authentication flow, present the user with an interface that
prompts the user to provide their email address and then call
`sendSignInLink` to request that Firebase
send the authentication link to the user's email.

1. Construct the `ActionCodeSettings` object, which provides Firebase with
   instructions on how to construct the email link. Set the following fields:

   - `url`: The deep link to embed and any additional state to be passed along. The link's domain has to be whitelisted in the Firebase Console list of authorized domains, which can be found by going to the Sign-in method tab (Authentication -\> Sign-in method).

   > [!IMPORTANT]
   > **Important:** In projects created after April 28, 2025, Firebase Authentication no longer includes `localhost` as an authorized domain by default. Google strongly discourages the use of `localhost` in production projects. If you choose to authorize `localhost`, you can manually add it in the **Settings** page, in **Authorized Domains** , by clicking **Add Domain**.

   - `iOSBundleID` and `androidPackageName`: Helps Firebase Authentication determine if it should create a web-only or mobile link which is opened on an Android or Apple device.
   - `handleCodeInApp`: Set to true. The sign-in operation has to always be completed in the app unlike other out of band email actions (password reset and email verifications). This is because, at the end of the flow, the user is expected to be signed in and their Auth state persisted within the app.
   - `linkDomain`: When custom Hosting link domains are defined for a project, specify which one to use when the link is to be opened by a specified mobile app. Otherwise the default domain is automatically selected (for example, `PROJECT_ID.firebaseapp.com`).
   - `dynamicLinkDomain`: Deprecated. Don't specify this parameter.

   #### Swift

   ```swift
   let actionCodeSettings = ActionCodeSettings()
   actionCodeSettings.url = URL(string: "https://www.example.com")
   // The sign-in operation has to always be completed in the app.
   actionCodeSettings.handleCodeInApp = true
   actionCodeSettings.setIOSBundleID(Bundle.main.bundleIdentifier!)
   actionCodeSettings.setAndroidPackageName("com.example.android",
                                            installIfNotAvailable: false, minimumVersion: "12")
   ```

   #### Objective-C

   ```objective-c
   FIRActionCodeSettings *actionCodeSettings = [[FIRActionCodeSettings alloc] init];
   [actionCodeSettings setURL:[NSURL URLWithString:@"https://www.example.com"]];
   // The sign-in operation has to always be completed in the app.
   actionCodeSettings.handleCodeInApp = YES;
   [actionCodeSettings setIOSBundleID:[[NSBundle mainBundle] bundleIdentifier]];
   [actionCodeSettings setAndroidPackageName:@"com.example.android"
                       installIfNotAvailable:NO
                              minimumVersion:@"12"];
   ```

   To learn more on `ActionCodeSettings`, refer to the
   [Passing State in Email Actions](https://firebase.google.com/docs/auth/ios/passing-state-in-email-actions#passing_statecontinue_url_in_email_actions)
   section.
2. Ask the user for their email.

3. Send the authentication link to the user's email, and save the user's email
   in case the user completes the email sign-in on the same device.

   #### Swift

   ```swift
   Auth.auth().sendSignInLink(toEmail: email,
                              actionCodeSettings: actionCodeSettings) { error in
     // ...
       if let error = error {
         self.showMessagePrompt(error.localizedDescription)
         return
       }
       // The link was successfully sent. Inform the user.
       // Save the email locally so you don't need to ask the user for it again
       // if they open the link on the same device.
       UserDefaults.standard.set(email, forKey: "Email")
       self.showMessagePrompt("Check your email for link")
       // ...
   }
   ```

   #### Objective-C

   ```objective-c
   [[FIRAuth auth] sendSignInLinkToEmail:email
                      actionCodeSettings:actionCodeSettings
                              completion:^(NSError *_Nullable error) {
     // ...
       if (error) {
         [self showMessagePrompt:error.localizedDescription];
          return;
       }
       // The link was successfully sent. Inform the user.
       // Save the email locally so you don't need to ask the user for it again
       // if they open the link on the same device.
       [NSUserDefaults.standardUserDefaults setObject:email forKey:@"Email"];
       [self showMessagePrompt:@"Check your email for link"];
       // ...
   }];
   ```

## Complete sign in with the email link

### Security concerns

To prevent a sign-in link from being used to sign in as an unintended user or on
an unintended device, Firebase Auth requires the user's email address to be
provided when completing the sign-in flow. For sign-in to succeed, this email
address must match the address to which the sign-in link was originally sent.

You can streamline this flow for users who open the sign-in link on the same
device they request the link, by storing their email address locally when you
send the sign-in email. Then, use this address to complete the flow.

After sign-in completion, any previous unverified mechanism of sign-in will be
removed from the user and any existing sessions will be invalidated.
For example, if someone previously created an unverified account with the same
email and password, the user's password will be removed to prevent the
impersonator who claimed ownership and created that unverified account from
signing in again with the same account.

### Completing sign-in in an Apple mobile app

Firebase Authentication uses Firebase Hosting to send the email link to a
mobile device. For sign-in completion with a mobile application, the application
has to be configured to detect the incoming application link, parse the
underlying deep link and then complete the sign-in. Check out the
[on universal links and associated domains on iOS](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content/)
for more details on how to accomplish this.

#### Configure Firebase Hosting

Firebase Authentication uses [Firebase Hosting](https://firebase.google.com/docs/hosting) domains when
creating and sending a link that is meant to be opened in a mobile application.
A default Firebase Hosting domain has already been configured for you.

1. Configure Firebase Hosting domains:

   In the Firebase console, open the
   [Hosting](https://console.firebase.google.com/project/_/hosting/sites) section.
   - If you want to use the default domain for the email link that opens in
     mobile applications, go to your default site and take note of your default
     Hosting domain. A default Hosting domain typically
     looks like this:
     `PROJECT_ID.firebaseapp.com`.

     You'll need this value when you configure your app to intercept the
     incoming link.
   - If you want to use a custom domain for the email link, you can
     [register one with Firebase Hosting](https://firebase.google.com/docs/hosting/custom-domain)
     and use that for the link's domain.

2. Configuring Apple applications:

   You will need to configure the chosen domain as an **Associated Domain** for
   app links. To set up the entitlement in your app, open the target's
   **Signing \& Capabilities** tab in Xcode and add Firebase Hosting domains
   from the previous step to the Associated Domains capability. If using the
   default Firebase Hosting domain, this will be
   `applinks:PROJECT_ID.firebaseapp.com`.

   See [Supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains)
   on Apple's documentation site for more information.

#### Verify link and sign in

After you receive the link as described above, verify that it is meant for email
link authentication and complete the sign in.

#### Swift

```swift
if Auth.auth().isSignIn(withEmailLink: link) {
        Auth.auth().signIn(withEmail: email, link: self.link) { user, error in
          // ...
        }
}
```

#### Objective-C

```objective-c
if ([[FIRAuth auth] isSignInWithEmailLink:link]) {
    [[FIRAuth auth] signInWithEmail:email
                               link:link
                         completion:^(FIRAuthDataResult * _Nullable authResult, NSError * _Nullable error) {
      // ...
    }];
}
```

To learn about how to handle sign-in with email link in an Android
application, refer to the [Android guide](https://firebase.google.com/docs/auth/android/email-link-auth).

To learn about how to handle sign-in with email link in a web
application, refer to the [Web guide](https://firebase.google.com/docs/auth/web/email-link-auth).

### Linking/re-authentication with email link

You can also link this method of authentication to an existing user. For example
a user previously authenticated with another provider, such as a phone number,
can add this method of sign-in to their existing account.

The difference would be in the second half of the operation:

#### Swift

```swift
  let credential = EmailAuthCredential.credential(withEmail:email
                                                       link:link)
  Auth.auth().currentUser?.link(with: credential) { authData, error in
    if (error) {
      // And error occurred during linking.
      return
    }
    // The provider was successfully linked.
    // The phone user can now sign in with their phone number or email.
  }
```

#### Objective-C

```objective-c
  FIRAuthCredential *credential =
      [FIREmailAuthProvider credentialWithEmail:email link:link];
  [FIRAuth auth].currentUser
      linkWithCredential:credential
              completion:^(FIRAuthDataResult *_Nullable result,
                           NSError *_Nullable error) {
    if (error) {
      // And error occurred during linking.
      return;
    }
    // The provider was successfully linked.
    // The phone user can now sign in with their phone number or email.
  }];
```

This can also be used to re-authenticate an email link user before running a
sensitive operation.

#### Swift

```swift
  let credential = EmailAuthProvider.credential(withEmail:email
                                                       link:link)
  Auth.auth().currentUser?.reauthenticate(with: credential) { authData, error in
    if (error) {
      // And error occurred during re-authentication.
      return
    }
    // The user was successfully re-authenticated.
  }
```

#### Objective-C

```objective-c
  FIRAuthCredential *credential =
      [FIREmailAuthCredential credentialWithEmail:email link:link];
  [FIRAuth auth].currentUser
      reauthenticateWithCredential:credential
                        completion:^(FIRAuthDataResult *_Nullable result,
                                     NSError *_Nullable error) {
    if (error) {
      // And error occurred during re-authentication
      return;
    }
    // The user was successfully re-authenticated.
  }];
```

However, as the flow could end up on a different device where the original user
was not logged in, this flow might not be completed. In that case, an error can
be shown to the user to force them to open the link on the same device. Some
state can be passed in the link to provide information on the type of operation
and the user uid.

## Deprecated: Firebase Dynamic Links based verification

Prior to the Firebase Authentication iOS SDK v11.8.0, the email link sign in feature
relied on Firebase Dynamic Links to open sign in links in the correct
app. These verification links are deprecated, as Firebase Dynamic Links will
[shut down on August 25, 2025](https://firebase.google.com/support/dynamic-links-faq).

If your app uses the old style links, you should
[migrate your app](https://firebase.google.com/docs/auth/ios/email-link-migration)
to the new Firebase Hosting based system.

## Deprecated: Differentiating email-password from email link

If you created your project on or after September 15, 2023, email enumeration
protection is enabled by default. This feature improves the security of your
project's user accounts, but it disables the `fetchSignInMethodsForEmail()`
method, which we formerly recommended to implement identifier-first flows.

Although you can disable email enumeration protection for your project, we
recommend against doing so.

To learn more, see [Enable or disable email enumeration protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection).

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