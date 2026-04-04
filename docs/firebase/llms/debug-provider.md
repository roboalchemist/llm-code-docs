# Source: https://firebase.google.com/docs/app-check/cpp/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/android/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/web/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/unity/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/ios/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/flutter/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/cpp/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/android/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/web/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/unity/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/ios/debug-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/flutter/debug-provider.md.txt

After you have registered your app for App Check, your app normally won't run in an emulator or from a continuous integration (CI) environment, since those environments don't qualify as valid devices. If you want to run your app in such an environment during development and testing, you can create a debug build of your app that uses the App Check debug provider instead of a real attestation provider.
| **Warning:** The debug provider allows access to your Firebase resources from unverified devices. Don't use the debug provider in production builds of your app, and don't share your debug builds with untrusted parties.

## Apple platforms

To use the debug provider while running your app in a simulator interactively (during development, for example), do the following:

1. Activate App Check with the debug provider right after you have initialized your Firebase app:

       import 'package:flutter/material.dart';
       import 'package:firebase_core/firebase_core.dart';

       // Import the firebase_app_check plugin
       import 'package:firebase_app_check/firebase_app_check.dart';

       Future<void> main() async {
         WidgetsFlutterBinding.ensureInitialized();
         await Firebase.initializeApp();
         await FirebaseAppCheck.instance.activate(
           // Set appleProvider to `AppleProvider.debug`
           appleProvider: AppleProvider.debug,
         );
         runApp(App());
       }

2. Enable debug logging in your Xcode project (v11.0 or newer):

   1. Open**Product \> Scheme \> Edit scheme**.
   2. Select**Run** from the left menu, then select the**Arguments**tab.
   3. In the**Arguments Passed on Launch** section, add`-FIRDebugEnabled`.
3. Open`ios/Runner.xcworkspace`with Xcode and run your app in the Simulator. Your app will print a local debug token to the debug output when Firebase tries to send a request to the backend. For example:

   ```
   Firebase App Check Debug Token:
   123a4567-b89c-12d3-e456-789012345678
   ```
4. In the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole, choose**Manage debug tokens**from your app's overflow menu. Then, register the debug token you logged in the previous step.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)

After you register the token, Firebase backend services will accept it as valid.

Because this token allows access to your Firebase resources without a valid device, it is crucial that you keep it private. Don't commit it to a public repository, and if a registered token is ever compromised, revoke it immediately in the Firebase console.

## Android

To use the debug provider while running your Flutter app in an Android environment, implement the following code in your Flutter application:  

    import 'package:flutter/material.dart';
    import 'package:firebase_core/firebase_core.dart';

    // Import the firebase_app_check plugin
    import 'package:firebase_app_check/firebase_app_check.dart';

    Future<void> main() async {
      WidgetsFlutterBinding.ensureInitialized();
      await Firebase.initializeApp();
      await FirebaseAppCheck.instance.activate(
        webRecaptchaSiteKey: 'recaptcha-v3-site-key',
        // Set androidProvider to `AndroidProvider.debug`
        androidProvider: AndroidProvider.debug,
      );
      runApp(App());
    }

Your app will print a local debug token to the debug output when Firebase tries to send a request to the backend. For example:  

```
D DebugAppCheckProvider: Enter this debug secret into the allow list in
the Firebase Console for your project: 123a4567-b89c-12d3-e456-789012345678
```

1. In the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole, choose**Manage debug tokens**from your app's overflow menu. Then, register the debug token you logged in the previous step.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)

After you register the token, Firebase backend services will accept it as valid.

## Web

To use the debug provider while running your app from`localhost`(during development, for example), do the following:
| **Warning:** *Do not* try to enable`localhost`debugging by adding`localhost`to reCAPTCHA's allowed domains. Doing so would allow anyone to run your app from their local machines!

1. In the file`web/index.html`, enable debug mode by setting`self.FIREBASE_APPCHECK_DEBUG_TOKEN`to`true`:

       <body>
         <script>
           self.FIREBASE_APPCHECK_DEBUG_TOKEN = true;
         </script>

         ...

       </body>

2. Run your web app locally and open the browser's developer tool. In the debug console, you'll see a debug token:

   ```
   AppCheck debug token: "123a4567-b89c-12d3-e456-789012345678". You will
   need to safelist it in the Firebase console for it to work.
   ```

   This token is stored locally in your browser and will be used whenever you use your app in the same browser on the same machine. If you want to use the token in another browser or on another machine, set`self.FIREBASE_APPCHECK_DEBUG_TOKEN`to the token string instead of`true`.
3. In the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole, choose**Manage debug tokens**from your app's overflow menu. Then, register the debug token you logged in the previous step.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)

After you register the token, Firebase backend services will accept it as valid.

Because this token allows access to your Firebase resources without a valid device, it is crucial that you keep it private. Don't commit it to a public repository, and if a registered token is ever compromised, revoke it immediately in the Firebase console.