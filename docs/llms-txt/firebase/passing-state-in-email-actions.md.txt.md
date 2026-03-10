# Source: https://firebase.google.com/docs/auth/web/passing-state-in-email-actions.md.txt

> [!WARNING]
> **Warning** : The following three Firebase Authentication features
> are impacted by the shutdown of Firebase Dynamic Links on August 25, 2025:
> email link authentication for mobile apps, OAuth flows for Android apps
> using older versions of the Authentication SDK, and Cordova OAuth support for
> web apps. In order to use these features after the shutdown of Dynamic Links,
> migrate to use a newer SDK version and complete some additional steps.
>
> For specific information and migration guidance, visit the
> [Dynamic Links
> Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq#impacts-on-email-link-authentication).

You can pass state via a continue URL when sending email actions for password
resets or verifying a user's email. This provides the user the ability to
go back to the app after the action is completed. In addition, you can specify
whether to handle the email action link directly from a mobile application when
it is installed instead of a web page.

This can be extremely useful in the following common scenarios:

- A user, not currently logged in, may be trying to access content that
  requires the user to be signed in. However, the user might have forgotten
  their password and therefore trigger the reset password flow. At the end of
  the flow, the user expects to go back to the section of the app they were
  trying to access.

- An application may only offer access to verified accounts. For
  example, a newsletter may require the user to verify their email before
  subscribing. The user would go through the email verification flow and expect
  to go back to the app to complete their subscription.

- In other cases, the user may have started the flow from their mobile device
  and expect after verification to return back to their mobile app instead of
  the browser.

Having the ability to pass state via a continue URL is a powerful feature that
Firebase Auth provides and which can significantly enhance the user experience.

## Passing state of a continue URL in email actions

In order to securely pass a continue URL, the domain for the URL will need to
be added as an Authorized domain in the [Firebase console](https://console.firebase.google.com/).
This is done in the **Authentication** section by adding this domain to the
list of **Authorized domains** under the **Sign-in method** tab if it is not already there.

> [!IMPORTANT]
> **Important:** In projects created after April 28, 2025, Firebase Authentication no longer includes `localhost` as an authorized domain by default. Google strongly discourages the use of `localhost` in production projects. If you choose to authorize `localhost`, you can manually add it in the **Settings** page, in **Authorized Domains** , by clicking **Add Domain**.

A `firebase.auth.ActionCodeSettings` instance needs to be provided when sending
a password reset email or a verification email. This interface takes the
following parameters:

| Parameter | Type | Description |
|---|---|---|
| `url` | string | Sets the link (state/continue URL) which has different meanings in different contexts: - When the link is handled in the web action widgets, this is the deep link in the `continueUrl` query parameter. - When the link is handled in the app directly, this is the `continueUrl` query parameter in the deep link of the Hosting link. |
| `iOS` | ({bundleId: string}\|undefined) | Sets the iOS bundle ID to help Firebase Authentication determine if it should create a web-only or mobile link which is opened on an Apple device |
| `android` | ({packageName: string, installApp:boolean\|undefined, minimumVersion: string\|undefined}\|undefined) | Sets the Android package name to help Firebase Authentication determine if it should create a web-only or mobile link which is opened on an Android device |
| `handleCodeInApp` | (boolean\|undefined) | Whether the email action link will be opened in a mobile app or a web link first. The default is false. When set to true, the action code link will be sent as a Universal Link or Android App Link and will be opened by the app if installed. In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed. |
| `linkDomain` | (string\|undefined) | When custom Hosting link domains are defined for a project, specify which one to use when the link is to be opened by a specified mobile app. Otherwise, the default domain is automatically selected (for example, `PROJECT_ID.firebaseapp.com`). |
| `dynamicLinkDomain` | (string\|undefined) | Deprecated. Don't specify this parameter. |

The following example illustrates how to send an email verification link that
will open in a mobile app first using the custom Hosting domain
`custom-domain.com`. The deep link will contain the continue URL payload
`https://www.example.com/?email=user@example.com`.

    const actionCodeSettings = {
      url: 'https://www.example.com/?email=' + firebase.auth().currentUser.email,
      iOS: {
        bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
      },
      handleCodeInApp: true,
      // Specify a custom Hosting link domain to use. The domain must be
      // configured in Firebase Hosting and owned by the project.
      linkDomain: "custom-domain.com"
    };
    firebase.auth().currentUser.sendEmailVerification(actionCodeSettings)
      .then(function() {
        // Verification email sent.
      })
      .catch(function(error) {
        // Error occurred. Inspect error.code.
      });

## Configuring Firebase Hosting links

Firebase Authentication uses [Firebase Hosting](https://firebase.google.com/docs/hosting) when sending a
link that is meant to be opened in a mobile application. In order to use this
feature, Hosting links need to be configured in the Firebase console.

1. Configuring Android applications:

   1. If you plan on handling these links from your Android application, your app's package name needs to be specified in the Firebase console project settings. In addition, the SHA-1 and SHA-256 of the application certificate need to be provided.
   2. You will also need to configure the intent filter for the deep link in your `AndroidManifest.xml` file.
   3. For more on this, refer to [Receiving Android Hosting links instructions](https://firebase.google.com/docs/auth/android/email-link-auth).
2. Configuring iOS applications:

   1. If you plan on handling these links from your iOS application, you'll need to configure the Hosting link domain as an Associated Domain in your application capabilities.
   2. For more on this, refer to [Receiving iOS Hosting links instructions](https://firebase.google.com/docs/auth/ios/email-link-auth).

## Handling email actions in a web application

You can specify whether you want to handle the action code link from a web
application first and then redirect to another web page or mobile application
after successful completion, provided the mobile application is available.
This is done by setting `handleCodeInApp` to `false` in the
`firebase.auth.ActionCodeSettings` object. While an iOS bundle ID
or Android package name are not required, providing them will allow the user
to redirect back to the specified app on email action code completion.

The web URL used here, is the one configured in the email action templates
section. A default one is provisioned for all projects. Refer to
[customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler) to learn more on
how to customize the email action handler.

In this case, the link within the `continueUrl` query parameter will be
a Hosting link whose payload is the `URL` specified in the `ActionCodeSettings`
object.

When handling email actions such as email verification, the action code from the
`oobCode` query parameter needs to be parsed from the deep link and then applied
via `applyActionCode` for the change to take effect, i.e. email to be verified.

## Handling email actions in a mobile application

You can specify whether you want to handle the action code link within your
mobile application first, provided it is installed. If the link is clicked from
a device that does not support the mobile application, it is opened from a web
page instead. This is done by setting `handleCodeInApp` to `true` in the
`firebase.auth.ActionCodeSettings` object. The mobile application's
Android package name or iOS bundle ID will also need to be specified.

The fallback web URL used here, when no mobile app is available, is the one
configured in the email action templates section. A default one is provisioned
for all projects. Refer to
[customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler) to learn more on
how to customize the email action handler.

In this case, the mobile app link sent to the user will be a Hosting link
whose payload is the action code URL, configured in the Console, with the query
parameters `oobCode`, `mode`, `apiKey` and `continueUrl`. The latter will be the
original `URL` specified in the `ActionCodeSettings` object. The action code can
be applied directly from a mobile application similar to how it is handled from
the web flow described in the
[customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler) section.

When handling email actions such as email verification, the action code from the
`oobCode` query parameter needs to be parsed from the deep link and then applied
via `applyActionCode` for the change to take effect, i.e. email to be verified.