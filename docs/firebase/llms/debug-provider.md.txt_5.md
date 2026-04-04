# Source: https://firebase.google.com/docs/app-check/unity/debug-provider.md.txt

After you have registered your app for App Check, your app normally won't run
on desktop platforms, in an emulator, or from a continuous integration (CI)
environment, since those environments don't qualify as valid devices. If you
want to run your app in such an environment during development and testing, you
can create a debug build of your app that uses the App Check debug provider
instead of a real attestation provider.

> [!WARNING]
> **Warning:** The debug provider allows access to your Firebase resources from unverified devices. Don't use the debug provider in production builds of your app, and don't share your debug builds with untrusted parties.

## Configuration via code

To use the debug provider while running your app
(during development, for example), do the following:

1. In the [**App Check**](https://console.firebase.google.com/project/_/appcheck) section
   of the Firebase console, choose **Manage debug tokens** from your app's
   overflow menu. Then, create a new debug token. You'll need the token in the
   next step.

   Because this token allows access to your Firebase resources without
   a valid device, it is crucial that you keep it private. Don't commit it to a
   public repository, and if a registered token is ever compromised, revoke it
   immediately in the Firebase console.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)
2. In your initialization code, do the following:

       using Firebase.AppCheck;

       void InitializeFirebase() {
         // Configure the Debug Provider factory with your debug token.
         DebugAppCheckProviderFactory.Instance.SetDebugToken("YOUR DEBUG TOKEN");

         // Set App Check to use the debug provider factory
         FirebaseAppCheck.SetAppCheckProviderFactory(
           DebugAppCheckProviderFactory.Instance);

         // Proceed to initialize Firebase as normal
       }

## Other configuration options

Other configuration options are available based on platform, for example using
the platforms environment variables. For more
information, refer to the [iOS+](https://firebase.google.com/docs/app-check/ios/debug-provider) or
[Android](https://firebase.google.com/docs/app-check/android/debug-provider) debug provider documentation.

Because this token allows access to your Firebase resources without a
valid device, it is crucial that you keep it private. Don't commit it to a
public repository, and if a registered token is ever compromised, revoke it
immediately in the Firebase console.