# Source: https://firebase.google.com/docs/auth/web/firebaseui.md.txt

[FirebaseUI](https://github.com/firebase/firebaseui-web) is a library built on
top of the Firebase Authentication SDK that provides drop-in UI flows for use in
your app. FirebaseUI provides the following benefits:

- **Multiple Providers** - sign-in flows for email/password, email link, phone authentication, Google, Facebook, Twitter and GitHub sign-in.
- **Account Linking** - flows to safely link user accounts across identity providers.
- **Customization** - override CSS styles of FirebaseUI to match your app requirements. Also, because FirebaseUI is open source, you can fork the project and customize it exactly to your needs.
- **One-tap sign-up and automatic sign-in** - automatic integration with [One-tap sign-up](https://developers.google.com/identity/one-tap/web/) for fast cross-device sign-in.
- **Localized UI** - internationalization for over 40 [languages](https://github.com/firebase/firebaseui-web/blob/master/LANGUAGES.md).
- **Upgrading anonymous users** - ability to upgrade anonymous users through sign-in/sign-up. For more information, visit the [Upgrading anonymous users
  section](https://github.com/firebase/firebaseui-web/blob/master/README.md#upgrading-anonymous-users).

> [!WARNING]
> **Warning:** FirebaseUI is **not** compatible with the [modular API](https://firebase.google.com/docs/web/learn-more#modular-version). The [namespaced API](https://firebase.google.com/docs/web/modular-upgrade#about_the_namespaced_compat_libraries) (specifically, the app-compat and auth-compat packages) permits the usage of FirebaseUI alongside the JavaScript SDK, but without the app size reduction and other benefits of the modular API.

## Before you begin

1. [Add Firebase Authentication to your web application](https://firebase.google.com/docs/web/setup),
   making sure that you're using the v9 or later namespaced API
   (*not* the modular API; see sidebar above).

2. Include FirebaseUI via one of the following options:

   1. CDN

      Include the following script and CSS file in the \<head\> tag of
      your page, below the initialization snippet from the Firebase Console:

          <script src="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.js"></script>
          <link type="text/css" rel="stylesheet" href="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.css" />

   2. npm Module

      Install FirebaseUI and its dependencies via npm using the following
      command:

          $ npm install firebaseui --save

      `require` the following modules within your source files:

      ```
      var firebase = require('firebase');
      var firebaseui = require('firebaseui');
      ```
   3. Bower Component

      Install FirebaseUI and its dependencies via Bower using the following
      command:

      ```
      $ bower install firebaseui --save
      ```

      Include the required files in your HTML, if your HTTP Server serves the
      files within `bower_components/`:

          <script src="bower_components/firebaseui/dist/firebaseui.js"></script>
          <link type="text/css" rel="stylesheet" href="bower_components/firebaseui/dist/firebaseui.css" />

## Initialize FirebaseUI

After importing the SDK, initialize the Auth UI.

    // Initialize the FirebaseUI Widget using Firebase.
    var ui = new firebaseui.auth.AuthUI(firebase.auth());

## Set up sign-in methods

Before you can use Firebase to sign in users, you must enable and configure the
sign-in methods you want to support.

### Email address and password

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section and enable
   email and password authentication.

2. Add the email provider ID to the list of FirebaseUI `signInOptions`.

   ```
   ui.start('#firebaseui-auth-container', {
     signInOptions: [
       firebase.auth.EmailAuthProvider.PROVIDER_ID
     ],
     // Other config options...
   });
   ```
3. **Optional** : The `EmailAuthProvider` can be configured to require the user
   to enter a display name (defaults to `true`).

   ```
   ui.start('#firebaseui-auth-container', {
     signInOptions: [
       {
         provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
         requireDisplayName: false
       }
     ]
   });
   ```

### Email link authentication

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section. On the
   **Sign in method** tab, enable the **Email/Password** provider. Note
   that email/password sign-in must be enabled to use email link sign-in.

2. In the same section, enable **Email link (passwordless sign-in)** sign-in
   method and click **Save**.

3. Add the email provider ID to the list of FirebaseUI `signInOptions` along
   with the email link `signInMethod`.

   ```
   ui.start('#firebaseui-auth-container', {
     signInOptions: [
       {
         provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
         signInMethod: firebase.auth.EmailAuthProvider.EMAIL_LINK_SIGN_IN_METHOD
       }
     ],
     // Other config options...
   });
   ```
4. When rendering the sign-in UI conditionally (relevant for single page apps),
   use `ui.isPendingRedirect()` to detect if the URL corresponds to a sign-in
   with email link and the UI needs to be rendered to complete sign-in.

   ```
   // Is there an email link sign-in?
   if (ui.isPendingRedirect()) {
     ui.start('#firebaseui-auth-container', uiConfig);
   }
   // This can also be done via:
   if (firebase.auth().isSignInWithEmailLink(window.location.href)) {
     ui.start('#firebaseui-auth-container', uiConfig);
   }
   ```
5. **Optional** : The `EmailAuthProvider` for email link sign-in can be
   configured to allow or block the user from completing cross device sign-in.

   An optional `emailLinkSignIn` callback can be defined to return the
   [`firebase.auth.ActionCodeSettings`](https://firebase.google.com/docs/auth/web/email-link-auth#send_an_authentication_link_to_the_users_email_address)
   configuration to use when sending the link. This provides the ability to
   specify how the link can be handled, custom dynamic link, additional state
   in the deep link, etc. When not provided, the current URL is used and a web
   only flow is triggered.

   Email link sign-in in FirebaseUI-web is compatible with
   [FirebaseUI-Android](https://github.com/firebase/FirebaseUI-Android/tree/master/auth#configuring-email-link-sign-in)
   and
   [FirebaseUI-iOS](https://github.com/firebase/FirebaseUI-iOS/tree/master/Auth#configuring-email-link-sign-in)
   where one user starting the flow from FirebaseUI-Android can open the link
   and complete sign-in with FirebaseUI-web. The same is true for the opposite
   flow.

   ```
   ui.start('#firebaseui-auth-container', {
     signInOptions: [
       {
         provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
         signInMethod: firebase.auth.EmailAuthProvider.EMAIL_LINK_SIGN_IN_METHOD,
         // Allow the user the ability to complete sign-in cross device,
         // including the mobile apps specified in the ActionCodeSettings
         // object below.
         forceSameDevice: false,
         // Used to define the optional firebase.auth.ActionCodeSettings if
         // additional state needs to be passed along request and whether to open
         // the link in a mobile app if it is installed.
         emailLinkSignIn: function() {
           return {
             // Additional state showPromo=1234 can be retrieved from URL on
             // sign-in completion in signInSuccess callback by checking
             // window.location.href.
             url: 'https://www.example.com/completeSignIn?showPromo=1234',
             // Custom FDL domain.
             dynamicLinkDomain: 'example.page.link',
             // Always true for email link sign-in.
             handleCodeInApp: true,
             // Whether to handle link in iOS app if installed.
             iOS: {
               bundleId: 'com.example.ios'
             },
             // Whether to handle link in Android app if opened in an Android
             // device.
             android: {
               packageName: 'com.example.android',
               installApp: true,
               minimumVersion: '12'
             }
           };
         }
       }
     ]
   });
   ```

### OAuth providers (Google, Facebook, Twitter and GitHub)

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section and enable
   the specified OAuth provider sign-in. Make sure the corresponding OAuth
   client ID and secret are also specified.

2. Also in the **Authentication** section, make sure the domain where your
   sign-in page will be rendered is also added to the authorized domains list.

3. Add the OAuth provider ID to the list of FirebaseUI `signInOptions`.

   ```
   ui.start('#firebaseui-auth-container', {
     signInOptions: [
       // List of OAuth providers supported.
       firebase.auth.GoogleAuthProvider.PROVIDER_ID,
       firebase.auth.FacebookAuthProvider.PROVIDER_ID,
       firebase.auth.TwitterAuthProvider.PROVIDER_ID,
       firebase.auth.GithubAuthProvider.PROVIDER_ID
     ],
     // Other config options...
   });
   ```
4. **Optional**: To specify custom scopes, or custom OAuth parameters per
   provider, you can pass an object instead of just the provider value:

   ```
   ui.start('#firebaseui-auth-container', {
     signInOptions: [
       {
         provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
         scopes: [
           'https://www.googleapis.com/auth/contacts.readonly'
         ],
         customParameters: {
           // Forces account selection even when one account
           // is available.
           prompt: 'select_account'
         }
       },
       {
         provider: firebase.auth.FacebookAuthProvider.PROVIDER_ID,
         scopes: [
           'public_profile',
           'email',
           'user_likes',
           'user_friends'
         ],
         customParameters: {
           // Forces password re-entry.
           auth_type: 'reauthenticate'
         }
       },
       firebase.auth.TwitterAuthProvider.PROVIDER_ID, // Twitter does not support scopes.
       firebase.auth.EmailAuthProvider.PROVIDER_ID // Other providers don't need to be given as object.
     ]
   });
   ```

### Phone number

1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section and enable
   phone number sign-in.

2. Make sure the domain where your sign-in page will be rendered is also
   added to the authorized domain list.

3. Add the phone number provider ID to the list of FirebaseUI `signInOptions`.

   ```
   ui.start('#firebaseui-auth-container', {
     signInOptions: [
       firebase.auth.PhoneAuthProvider.PROVIDER_ID
     ],
     // Other config options...
   });
   ```
4. **Optional** : The PhoneAuthProvider can be configured with custom reCAPTCHA
   parameters whether reCAPTCHA is visible or invisible (defaults to normal).
   Refer to the
   [reCAPTCHA API docs](https://developers.google.com/recaptcha/docs/display)
   for more details.

   The default country to select in the phone number input can also be set.
   Refer to the
   [list of supported country codes](https://github.com/firebase/firebaseui-web/blob/master/javascript/data/README.md)
   for the full list of codes.
   If unspecified, the phone number input will default to the United States
   (+1).

   The following options are currently supported.

   ```
   ui.start('#firebaseui-auth-container', {
     signInOptions: [
       {
         provider: firebase.auth.PhoneAuthProvider.PROVIDER_ID,
         recaptchaParameters: {
           type: 'image', // 'audio'
           size: 'normal', // 'invisible' or 'compact'
           badge: 'bottomleft' //' bottomright' or 'inline' applies to invisible.
         },
         defaultCountry: 'GB', // Set default country to the United Kingdom (+44).
         // For prefilling the national number, set defaultNationNumber.
         // This will only be observed if only phone Auth provider is used since
         // for multiple providers, the NASCAR screen will always render first
         // with a 'sign in with phone number' button.
         defaultNationalNumber: '1234567890',
         // You can also pass the full phone number string instead of the
         // 'defaultCountry' and 'defaultNationalNumber'. However, in this case,
         // the first country ID that matches the country code will be used to
         // populate the country selector. So for countries that share the same
         // country code, the selected country may not be the expected one.
         // In that case, pass the 'defaultCountry' instead to ensure the exact
         // country is selected. The 'defaultCountry' and 'defaultNationaNumber'
         // will always have higher priority than 'loginHint' which will be ignored
         // in their favor. In this case, the default country will be 'GB' even
         // though 'loginHint' specified the country code as '+1'.
         loginHint: '+11234567890'
       }
     ]
   });
   ```

## Sign in

To kick off the FirebaseUI sign in flow, initialize the FirebaseUI instance by
passing the underlying `Auth` instance.

    // Initialize the FirebaseUI Widget using Firebase.
    var ui = new firebaseui.auth.AuthUI(firebase.auth());

Define the HTML element where the FirebaseUI sign-in widget will be rendered.

    <!-- The surrounding HTML is left untouched by FirebaseUI.
         Your app may use that space for branding, controls and other customizations.-->
    <h1>Welcome to My Awesome App</h1>
    <div id="firebaseui-auth-container"></div>
    <div id="loader">Loading...</div>

Specify the FirebaseUI configuration (providers supported and UI customizations
as well as success callbacks, etc).

    var uiConfig = {
      callbacks: {
        signInSuccessWithAuthResult: function(authResult, redirectUrl) {
          // User successfully signed in.
          // Return type determines whether we continue the redirect automatically
          // or whether we leave that to developer to handle.
          return true;
        },
        uiShown: function() {
          // The widget is rendered.
          // Hide the loader.
          document.getElementById('loader').style.display = 'none';
        }
      },
      // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
      signInFlow: 'popup',
      signInSuccessUrl: '<url-to-redirect-to-on-success>',
      signInOptions: [
        // Leave the lines as is for the providers you want to offer your users.
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        firebase.auth.FacebookAuthProvider.PROVIDER_ID,
        firebase.auth.TwitterAuthProvider.PROVIDER_ID,
        firebase.auth.GithubAuthProvider.PROVIDER_ID,
        firebase.auth.EmailAuthProvider.PROVIDER_ID,
        firebase.auth.PhoneAuthProvider.PROVIDER_ID
      ],
      // Terms of service url.
      tosUrl: '<your-tos-url>',
      // Privacy policy url.
      privacyPolicyUrl: '<your-privacy-policy-url>'
    };

Finally, render the FirebaseUI Auth interface:

    // The start method will wait until the DOM is loaded.
    ui.start('#firebaseui-auth-container', uiConfig);

## Upgrading anonymous users

### Enabling anonymous user upgrade

When an anonymous user signs in or signs up with a permanent account, you want
to be sure the user can continue with what they were doing before signing up.
To do so, simply set `autoUpgradeAnonymousUsers` to `true` when you configure
the sign-in UI (this option is disabled by default).

### Handling anonymous user upgrade merge conflicts

There are cases when a user, initially signed in anonymously, tries to upgrade
to an existing Firebase user. Since an existing user cannot be linked to another
existing user, FirebaseUI will trigger the `signInFailure` callback with an
error code `firebaseui/anonymous-upgrade-merge-conflict` when the above occurs.
The error object will also contain the permanent credential. Sign-in with the
permanent credential should be triggered in the callback to complete sign-in.
Before sign-in can be completed via
`auth.signInWithCredential(error.credential)`, you must save the anonymous
user's data and delete the anonymous user. Then, after sign-in completion, copy
the data back to the non-anonymous user. An example below illustrates how this
flow would work.

    // Temp variable to hold the anonymous user data if needed.
    var data = null;
    // Hold a reference to the anonymous current user.
    var anonymousUser = firebase.auth().currentUser;
    ui.start('#firebaseui-auth-container', {
      // Whether to upgrade anonymous users should be explicitly provided.
      // The user must already be signed in anonymously before FirebaseUI is
      // rendered.
      autoUpgradeAnonymousUsers: true,
      signInSuccessUrl: '<url-to-redirect-to-on-success>',
      signInOptions: [
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        firebase.auth.FacebookAuthProvider.PROVIDER_ID,
        firebase.auth.EmailAuthProvider.PROVIDER_ID,
        firebase.auth.PhoneAuthProvider.PROVIDER_ID
      ],
      callbacks: {
        // signInFailure callback must be provided to handle merge conflicts which
        // occur when an existing credential is linked to an anonymous user.
        signInFailure: function(error) {
          // For merge conflicts, the error.code will be
          // 'firebaseui/anonymous-upgrade-merge-conflict'.
          if (error.code != 'firebaseui/anonymous-upgrade-merge-conflict') {
            return Promise.resolve();
          }
          // The credential the user tried to sign in with.
          var cred = error.credential;
          // Copy data from anonymous user to permanent user and delete anonymous
          // user.
          // ...
          // Finish sign-in after data is copied.
          return firebase.auth().signInWithCredential(cred);
        }
      }
    });

## Next Steps

- For more information on using and customizing FirebaseUI, visit the [README](https://github.com/firebase/firebaseui-web/blob/master/README.md).
- If you find an issue in FirebaseUI and would like to report it, use the [GitHub issue tracker](https://github.com/firebase/firebaseui-web/issues).