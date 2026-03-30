# Source: https://firebase.google.com/docs/app-check/web/debug-provider.md.txt

If, after you have registered your app for App Check, you want to run your
app in an environment that App Check would normally not classify as valid,
such as locally during development, or from a continuous integration (CI)
environment, you can create a debug build of your app that uses the
App Check debug provider instead of a real attestation provider.

> [!WARNING]
> **Warning:** The debug provider allows access to your Firebase resources from unverified devices. **Don't** use the debug provider in production builds of your app, and **don't** share your debug builds with untrusted parties.

## Use the debug provider on localhost

To use the debug provider while running your app from `localhost` (during
development, for example), do the following:

> [!WARNING]
> **Warning:** *Do not* try to enable `localhost` debugging by adding `localhost` to reCAPTCHA's allowed domains. Doing so would allow anyone to run your app from their local machines!

1. In your debug build, enable debug mode by setting
   `self.FIREBASE_APPCHECK_DEBUG_TOKEN` to `true` before you initialize
   App Check. For example:

   ### Web

       self.FIREBASE_APPCHECK_DEBUG_TOKEN = true;
       initializeAppCheck(app, { /* App Check options */ });

   ### Web

       self.FIREBASE_APPCHECK_DEBUG_TOKEN = true;
       firebase.appCheck().activate(/* site key or provider */);

   > [!NOTE]
   > **Note:** In Firebase Web SDK versions before v9, `self.FIREBASE_APPCHECK_DEBUG_TOKEN` is read at import time, and not at initialization/activation time. This required it to be set in `index.html` before the code bundle is loaded. To avoid this restriction, upgrade to v9.

2. Visit your web app locally and open the browser's developer tool. In the
   debug console, you'll see a debug token:

   ```
   AppCheck debug token: "123a4567-b89c-12d3-e456-789012345678". You will
   need to safelist it in the Firebase console for it to work.
   ```
3. In the [**App Check**](https://console.firebase.google.com/project/_/appcheck) section
   of the Firebase console, choose **Manage debug tokens** from your app's
   overflow menu. Then, register the debug token you logged in the previous
   step.

   ![Screenshot of the Manage Debug Tokens menu item](https://firebase.google.com/static/docs/app-check/manage-debug-tokens.png)

After you register the token, Firebase backend services will accept it as valid.

Because this token allows access to your Firebase resources without a
valid device, it is crucial that you keep it private. Don't commit it to a
public repository, and if a registered token is ever compromised, revoke it
immediately in the Firebase console.

This token is stored locally in your browser and will be used whenever you use
your app in the same browser on the same machine. If you want to use the
token in another browser or on another machine, set
`self.FIREBASE_APPCHECK_DEBUG_TOKEN` to the token string instead of `true`.

## Use the debug provider in a CI environment

To use the debug provider in a continuous integration (CI) environment, do the following:

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

4. In your debug build, enable debug mode by setting
   `self.FIREBASE_APPCHECK_DEBUG_TOKEN` to the value of the debug token
   environment variable before you import App Check. For example:

   ### Web

       self.FIREBASE_APPCHECK_DEBUG_TOKEN = process.env.APP_CHECK_DEBUG_TOKEN_FROM_CI;
       initializeAppCheck(app, { /* App Check options */ });

   ### Web

       self.FIREBASE_APPCHECK_DEBUG_TOKEN = process.env.APP_CHECK_DEBUG_TOKEN_FROM_CI;
       firebase.appCheck().activate(/* site key or provider */);

When your app runs in a CI environment, Firebase backend services will accept
the token it sends as valid.