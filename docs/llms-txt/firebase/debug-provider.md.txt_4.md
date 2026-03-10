# Source: https://firebase.google.com/docs/app-check/ios/debug-provider.md.txt

If, after you have registered your app for App Check, you want to run your
app in an environment that App Check would normally not classify as valid,
such as a simulator or device during development, or from a continuous
integration (CI) environment, you can create a debug build of your app that uses
the App Check debug provider instead of a real attestation provider.

> [!WARNING]
> **Warning:** The debug provider allows access to your Firebase resources from unverified devices. **Don't** use the debug provider in production builds of your app, and be careful not to leak your debug token.

## Use the debug provider in development

To use the debug provider while running your app interactively
(during development, for example), do the following:

1. In your debug build, before using any Firebase backend services, create and
   set the App Check debug provider factory:

   ### Swift

   ```swift
   let providerFactory = AppCheckDebugProviderFactory()
   AppCheck.setAppCheckProviderFactory(providerFactory)

   FirebaseApp.configure()
   ```

   ### Objective-C

   ```objective-c
   FIRAppCheckDebugProviderFactory *providerFactory =
         [[FIRAppCheckDebugProviderFactory alloc] init];
   [FIRAppCheck setAppCheckProviderFactory:providerFactory];

   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```
2. Enable debug logging in your Xcode project (v11.0 or newer):

   1. Open **Product \> Scheme \> Edit scheme**.
   2. Select **Run** from the left menu, then select the **Arguments** tab.
   3. In the **Arguments Passed on Launch** section, add `-FIRDebugEnabled`.
3. Launch the app. A local debug token will be logged when the SDK tries to
   send a request to the backend. For example:

   ```
   [Firebase/AppCheck][I-FAA001001] Firebase App Check Debug Token:
   123a4567-b89c-12d3-e456-789012345678
   ```
4. In the [**App Check**](https://console.firebase.google.com/project/_/appcheck) section
   of the Firebase console, choose **Manage debug tokens** from your app's
   overflow menu. Then, register the debug token you logged in the previous
   step.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)

After you register the token, Firebase backend services will accept it as valid.

Because this token allows access to your Firebase resources without a
valid device, it is crucial that you keep it private. Don't commit it to a
public repository, and if a registered token is ever compromised, revoke it
immediately in the Firebase console.

## Use the debug provider in a CI environment

To use the debug provider in a continuous integration (CI) environment, do the
following:

1. In the [**App Check**](https://console.firebase.google.com/project/_/appcheck) section
   of the Firebase console, choose **Manage debug tokens** from your app's
   overflow menu. Then, create a new debug token. You'll need the token in the
   next step.

   Because this token allows access to your Firebase resources without
   a valid device, it is crucial that you keep it private. Don't commit it to a
   public repository, and if a registered token is ever compromised, revoke it
   immediately in the Firebase console.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)
2. Add the debug token you just created to your CI system's secure key store
   (for example, GitHub Actions' [encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets)
   or Travis CI's [encrypted variables](https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml)).

3. If necessary, configure your CI system to make your debug token available
   within the CI environment as an environment variable. Name the variable
   something like `APP_CHECK_DEBUG_TOKEN_FROM_CI`.

4. In Xcode, add an environment variable to your testing scheme with the name
   `FIRAAppCheckDebugToken` and something like `$(APP_CHECK_DEBUG_TOKEN)` as
   the value.

5. Configure your CI test script to pass the debug token as an environment
   variable. For example:

   ```
   xcodebuild test -scheme YourTestScheme -workspace YourProject.xcworkspace \
   APP_CHECK_DEBUG_TOKEN=$(APP_CHECK_DEBUG_TOKEN_FROM_CI)
   ```
6. In your debug build, before using any Firebase backend services, create and
   set the App Check debug provider factory:

   ### Swift

   ```swift
   let providerFactory = AppCheckDebugProviderFactory()
   AppCheck.setAppCheckProviderFactory(providerFactory)

   FirebaseApp.configure()
   ```

   ### Objective-C

   ```objective-c
   FIRAppCheckDebugProviderFactory *providerFactory =
         [[FIRAppCheckDebugProviderFactory alloc] init];
   [FIRAppCheck setAppCheckProviderFactory:providerFactory];

   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```

When your app runs in a CI environment, Firebase backend services will accept
the token it sends as valid.