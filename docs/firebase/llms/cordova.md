# Source: https://firebase.google.com/docs/auth/web/cordova.md.txt

| **Warning** : The following threeFirebase Authenticationfeatures are impacted by the shutdown ofFirebase Dynamic Linkson August 25, 2025: email link authentication for mobile apps, OAuth flows for Android apps using older versions of theAuthenticationSDK, and Cordova OAuth support for web apps. In order to use these features after the shutdown ofDynamic Links, migrate to use a newer SDK version and complete some additional steps.
|
| For specific information and migration guidance, visit the[Dynamic LinksDeprecation FAQ](https://firebase.google.com/support/dynamic-links-faq#impacts-on-email-link-authentication).

With the Firebase JS SDK, you can let your Firebase users authenticate using any supported OAuth provider in a Cordova environment. You can integrate any supported OAuth provider by carrying out the OAuth flow manually and passing the resulting OAuth credential to Firebase.

Instructions on how to handle the sign-in flow manually for each provider:

- [Google](https://firebase.google.com/docs/auth/web/google-signin#expandable-2)
- [Facebook](https://firebase.google.com/docs/auth/web/facebook-login#expandable-2)
- [Twitter](https://firebase.google.com/docs/auth/web/twitter-login#handle_the_sign-in_flow_manually)
- [GitHub](https://firebase.google.com/docs/auth/web/github-auth#handle_the_sign-in_flow_manually)
- [Microsoft](https://firebase.google.com/docs/auth/web/microsoft-oauth#expandable-2)
- [Yahoo](https://firebase.google.com/docs/auth/web/yahoo-oauth#expandable-2)
- Apple
  1. Follow[Configuring your webpage for Sign in with Apple](https://developer.apple.com/documentation/signinwithapplejs/configuring_your_webpage_for_sign_in_with_apple)to sign in the user with their Apple Account and get the user's Apple ID token.
  2. After you get the user's Apple ID token, use it to build a[Credential object](https://firebase.google.com/docs/auth/web/apple#advanced_authenticate_with_firebase_in_nodejs)and then sign in the user with the credential.