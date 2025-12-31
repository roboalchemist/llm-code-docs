# Source: https://firebase.google.com/docs/emulator-suite/connect_auth.md.txt

<br />

Before using theAuthenticationemulator with you app, make sure that you[understand the overallFirebase Local Emulator Suiteworkflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore), and that you[install and configure](https://firebase.google.com/docs/emulator-suite/install_and_configure)theLocal Emulator Suiteand review its[CLI commands](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

This topic assumes you are already familiar with developingFirebase Authenticationsolutions for production. If needed, review the documentation for your[combination of platform and authentication technique](https://firebase.google.com/docs/auth/where-to-start#firebasesdk).

## What can I do with theAuthenticationemulator?

TheAuthenticationemulator provides high-fidelity local emulation ofFirebase Authenticationservices, providing much of the functionality found in[productionFirebase Authentication](https://firebase.google.com/docs/auth). Paired with the Apple platforms, Android and Web Firebase SDKs, the emulator lets you:

- Create, update and manage emulated user accounts for testing email/password, phone number/SMS, SMS multi-factor, and third-party (e.g. Google) identity provider authentication
- View and edit emulated users
- Prototype custom token authentication systems
- Check authentication-related messages in the Emulator UI Logs tab.

## Choose a Firebase project

TheFirebase Local Emulator Suiteemulates products for a single Firebase project.

To select the project to use, before you start the emulators, in the CLI run`firebase use`in your working directory. Or, you can pass the`--project`flag to each emulator command.
| **Note:** It's generally a good practice to use one project ID for all emulator invocations, so theEmulator Suite UI, different product emulators, and all running instances of a particular emulator can communicate correctly in all cases. In fact, by default, theLocal Emulator Suitewill warn on detecting multiple project IDs in use, though you can override this behavior. For guidance on setting and managing project IDs, see the[Installation and configuration guide](https://firebase.google.com/docs/emulator-suite/install_and_configure#project_id_configuration).

Local Emulator Suitesupports emulation of*real* Firebase projects and*demo*projects.

| Project type |                                                                                                                      Features                                                                                                                       |                                                                                                                       Use with emulators                                                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Real         | A real Firebase project is one you created and configured (most likely via theFirebaseconsole). Real projects have live resources, like database instances, storage buckets, functions, or any other resource you set up for that Firebase project. | When working with real Firebase projects, you can run emulators for any or all of the supported products. For any products you are not emulating, your apps and code will interact with the*live*resource (database instance, storage bucket, function, etc.). |
| Demo         | A demo Firebase project has no*real*Firebase configuration and no live resources. These projects are usually accessed via codelabs or other tutorials. Project IDs for demo projects have the`demo-`prefix.                                         | When working with demo Firebase projects, your apps and code interact with emulators*only*. If your app attempts to interact with a resource for which an emulator isn't running, that code will fail.                                                         |

We recommend you use demo projects wherever possible. Benefits include:

- Easier setup, since you can run the emulators without ever creating a Firebase project
- Stronger safety, since if your code accidentally invokes non-emulated (production) resources, there is no chance of data change, usage and billing
- Better offline support, since there is no need to access the internet to download your SDK configuration.

| **Note:** If you want to emulate cross-service interactions such as database-triggeredCloud FunctionsorRulesthat rely onAuthenticationyou must make sure that the project ID in your code (in`initializeApp()`, etc.) matches the project ID used by theFirebaseCLI.

## Instrument your app to talk to the emulator

### Android, iOS, and web SDKs

Set up your in-app configuration or test classes to interact with theAuthenticationemulator as follows.  

##### Kotlin

```kotlin
Firebase.auth.useEmulator("10.0.2.2", 9099)
```

##### Java

```java
FirebaseAuth.getInstance().useEmulator("10.0.2.2", 9099);
```

##### Swift

```swift
Auth.auth().useEmulator(withHost:"127.0.0.1", port:9099)
```

### Web

```javascript
import { getAuth, connectAuthEmulator } from "firebase/auth";

const auth = getAuth();
connectAuthEmulator(auth, "http://127.0.0.1:9099");https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/emulator-suite/auth_emulator_connect.js#L8-L11
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
const auth = firebase.auth();
auth.useEmulator("http://127.0.0.1:9099");https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/emulator-suite.js#L6-L7
```

No additional setup is needed to prototype and test interactions betweenAuthenticationandCloud FunctionsorFirebase Security RulesforCloud FirestoreorRealtime Database. When theAuthenticationemulator is configured and other emulators are running, they automatically work together.

### Admin SDKs

TheFirebaseAdmin SDKs automatically connect to theAuthenticationemulator when the`FIREBASE_AUTH_EMULATOR_HOST`environment variable is set.  

    export FIREBASE_AUTH_EMULATOR_HOST="127.0.0.1:9099"

| **Note:** For emulators to work correctly the`FIREBASE_AUTH_EMULATOR_HOST`environment variable must omit protocols such as`http://`.

Note that theCloud Functionsemulator is automatically aware of theAuthenticationemulator so you can skip this step when testing integrations betweenCloud FunctionsandAuthenticationemulators. The environment variable will be automatically set for theAdmin SDKinCloud Functions.

With the environment variable set,FirebaseAdmin SDKs will accept unsigned ID Tokens and session cookies issued by theAuthenticationemulator (via`verifyIdToken`and`createSessionCookie`methods respectively) to facilitate local development and testing. Please make sure*not*to set the environment variable in production.

If you want yourAdmin SDKcode to connect to a shared emulator running in another environment, you will need to specify the[the same project ID you set using the Firebase CLI](https://firebase.google.com/docs/emulator-suite/connect_auth#choose_a_firebase_project). You can pass a project ID to`initializeApp`directly or set the`GCLOUD_PROJECT`environment variable.  

##### Node.js Admin SDK

```javascript
admin.initializeApp({ projectId: "your-project-id" });
```

##### Environment Variable

```gdscript
export GCLOUD_PROJECT="your-project-id"
```

## ID Tokens

For security reasons, theAuthenticationemulator issues*unsigned* ID tokens, which are only accepted by other Firebase emulators, or the Firebase Admin SDK when[configured](https://firebase.google.com/docs/emulator-suite/connect_auth#admin_sdks). These tokens will be rejected by production Firebase services or Firebase Admin SDK running in production mode (e.g. the default behavior without the setup steps described above).

## Start the emulator

You can use theAuthenticationemulator interactively via theEmulator Suite UIand non-interactively through its local REST interface. The following sections cover interactive and non-interactive use cases.

To start theAuthenticationemulator, its REST interface, and theEmulator Suite UI, execute:  

    firebase emulators:start

## Emulated email, email link and anonymous authentication

For**anonymous authentication** , your app can exercise the sign-in logic for your platform ([iOS](https://firebase.google.com/docs/auth/ios/anonymous-auth),[Android](https://firebase.google.com/docs/auth/android/anonymous-auth),[web](https://firebase.google.com/docs/auth/web/anonymous-auth)).

For**email/password authentication** , you can start prototyping by adding user accounts to theAuthenticationemulator from your app usingAuthenticationSDK methods, or by using theEmulator Suite UI.

1. In theEmulator Suite UI, click the**Authentication**tab.
2. Click the**Add user**button.
3. Follow the user account creation wizard, filling in the email authentication fields.

With a test user created, your app can sign the user in and out with SDK logic for your platform ([iOS](https://firebase.google.com/docs/auth/ios/password-auth#sign_in_a_user_with_an_email_address_and_password),[Android](https://firebase.google.com/docs/auth/android/password-auth#sign_in_a_user_with_an_email_address_and_password),[web](https://firebase.google.com/docs/auth/web/password-auth#sign_in_a_user_with_an_email_address_and_password)).

For testing email verification/sign-in with email link flows, the emulator prints a URL to the terminal at which`firebase emulators:start`was executed.  

    i  To verify the email address customer@ex.com, follow this link:
    http://127.0.0.1:9099/emulator/action?mode=verifyEmail&lang=en&oobCode=XYZ123&apiKey=fake-api-key

Paste the link into your browser to simulate the verification event, and check whether verification succeeded.  

    {
      "authEmulator": {
        "success": "The email has been successfully verified.",
        "email": "customer@example.com"
      }
    }

For testing password resets, the emulator prints a similar URL, including a**newPassword**parameter (which you may change as needed), to the terminal.  

    http://127.0.0.1:9099/emulator/action?mode=resetPassword&oobCode=XYZ!23&apiKey=fake-api-key&newPassword=YOUR_NEW_PASSWORD

### Non-interactive testing

Instead of using theEmulator Suite UIor client code to manage email/password user accounts, you can write test setup scripts that call REST APIs to create and delete user accounts and fetch out-of-band email verification codes to populate the emulator email verification URL. This keeps platform and test code separate and lets you test non-interactively.

For non-interactive email and password test flows, the typical sequence is as follows.

1. Create users with theAuthentication[signUp REST endpoint](https://firebase.google.com/docs/reference/rest/auth#section-create-email-password).
2. Sign in users using the emails and passwords to perform tests.
3. If applicable to your tests, fetch available out-of-band email verification codes from the[emulator-specific REST endpoint](https://firebase.google.com/docs/reference/rest/auth#section-auth-emulator-oob).
4. Flush user records with the[emulator-specific REST endpoint](https://firebase.google.com/docs/reference/rest/auth#section-auth-emulator-clearaccounts)for clearing data.

## Emulated phone/SMS authentication

For phone authentication, the Auth emulator does not support:

- reCAPTCHA and APN flows. Once configured to interact with the emulator, client SDKs disable these verification methods in a way similar to that described for integration testing ([iOS](https://firebase.google.com/docs/auth/ios/phone-auth#integration-testing),[Android](https://firebase.google.com/docs/auth/android/phone-auth#integration-testing),[web](https://firebase.google.com/docs/auth/web/phone-auth#integration-testing)).
- Test phone numbers with codes preconfigured in theFirebaseconsole.

Otherwise, in terms of client code, the phone/SMS authentication flow is identical to that described for production ([iOS](https://firebase.google.com/docs/auth/ios/phone-auth),[Android](https://firebase.google.com/docs/auth/android/phone-auth),[web](https://firebase.google.com/docs/auth/web/phone-auth)).

Using theEmulator Suite UI:

1. In theEmulator Suite UI, click the**Authentication**tab.
2. Click the**Add user**button.
3. Follow the user account creation wizard, filling in the phone authentication fields.

However, for phone authentication flows, the emulator will NOT trigger delivery of any text messages, since contacting a carrier is out of scope and not friendly for local testing! Instead, the emulator prints out the code that would have been sent via SMS to the same terminal at which you ran`firebase emulators:start`; input this code to the app to simulate users checking their text messages.

### Non-interactive testing

For non-interactive phone authentication testing, use theAuthenticationemulator REST API to retrieve available SMS codes. Note that the code is different every time you initiate the flow.

The typical sequence is as follows.

1. Call platform`signInWithPhoneNumber`to start the verification process.
2. Retrieve the verification code using the[emulator-specific REST endpoint](https://firebase.google.com/docs/reference/rest/auth#section-auth-emulator-smsverification).
3. Call`confirmationResult.confirm(code)`as usual with the verification code.

### Multi-factor SMS

TheAuthenticationemulator supports prototyping and testing the SMS multi-factor authentication (MFA) flows available in production for[iOS](https://firebase.google.com/docs/auth/ios/multi-factor),[Android](https://firebase.google.com/docs/auth/android/multi-factor), and[web](https://firebase.google.com/docs/auth/web/multi-factor).

When you add a mock user to the emulator, you can enable MFA and configure one or more phone numbers to which second factor SMS messages will be sent. Messages are output to the same terminal at which you ran`firebase emulators:start`, and available from the REST interface.

## Emulated third-party identity provider (IDP) authentication

TheAuthenticationemulator lets you test many third-party authentication flows in your iOS, Android or web apps with no changes from production code. For examples of authentication flows, consult the documentation for various[combinations of providers and platforms you can use in your app](https://firebase.google.com/docs/auth/where-to-start#firebasesdk).

Generally speaking, you can use the Firebase SDK to authenticate in one of two ways:

- Your app lets the SDK handle the entire process end-to-end, including all interactions with third-party IDP providers to retrieve credentials.
- Your app manually retrieves credentials from a third-party provider using that party's SDK and passes those credentials on to theAuthenticationSDK.

Again, check the documentation link above and make sure you're familiar with whichever flow - Firebase SDK-managed vs. manual credential retrieval - you want to use. TheAuthenticationemulator supports testing of either approach.

### Testing Firebase SDK-driven IDP flows

If your app uses any Firebase SDK end-to-end flow, like`OAuthProvider`for sign-in with Microsoft, GitHub, or Yahoo, for interactive testing, theAuthenticationemulator serves a local version of the corresponding sign-in page to help you test authentication from web apps that call the`signinWithPopup`or`signInWithRedirect`method. This locally-served sign-in page also appears in mobile apps, rendered by your platform's webview library.

The emulator creates mock third-party user accounts and credentials as needed as the flows proceed.

### Testing IDP flows with manual credential retrieval

If you use "manual" sign-in techniques and call your platform's`signInWithCredentials`method, then, as usual, your app will request real third-party sign-in and retrieve real third-party credentials.

Note that the emulator only supports`signInWithCredential`authentication for credentials retrieved from Google Sign-In, Apple, and other providers that use ID tokens implemented as JSON Web Tokens (JWTs). Access tokens (e.g. those provided by Facebook or Twitter, which are not JWTs) are not supported. The next section discusses an alternative in these cases.

### Non-interactive testing

One approach to non-interactive testing is to automate user clicks on the sign-in page served by the emulator. For web apps, use a control interface like WebDriver. For mobile, use the UI test tooling from your platform, like Espresso or Xcode.

Alternatively, you can update your code to use`signInWithCredential`(e.g. in a code branch) and use a token authentication flow with mock ID tokens for accounts instead of real credentials.

1. Rewire or comment out the part of your code that retrieve idTokens from the IDP; this removes the need to input real usernames and passwords during your tests, and relieves your tests from API quotas and rate limits at the IDP.
2. Second, use a literal JSON string in place of the token for`signInWithCredential`. Using the web SDK as an example, you can change the code to:

    firebase.auth().signInWithCredential(firebase.auth.GoogleAuthProvider.credential(
      '{"sub": "abc123", "email": "foo@example.com", "email_verified": true}'
    ));

When used with the emulator, this code will successfully authenticate a user with email`foo@example.com`at Google. Think of the sub field as a primary key, which can be changed to any string, mocking signing in different users. You can replace`firebase.auth.GoogleAuthProvider`with, for example,`new firebase.auth.OAuthProvider('yahoo.com')`or any other provider ID you want to mock.

## Emulated custom token authentication

TheAuthenticationemulator handles authentication with custom JSON Web Tokens using calls to the`signInWithCustomToken`method on supported platforms, as described in the[productionAuthenticationdocumentation](https://firebase.google.com/docs/auth/admin/create-custom-tokens).

## How theAuthenticationemulator differs from production

The FirebaseAuthenticationemulator simulates many features of the production product. However, since any kind of authentication system relies heavily on security at multiple levels (device, 3rd party providers, Firebase, etc), it is difficult for the emulator to properly recreate all flows.

### Cloud IAM

The Firebase Emulator Suite does not attempt to replicate or respect any IAM-related behavior for running. Emulators adhere to the Firebase Security Rules provided, but in situations where IAM would normally be used, for example to set Cloud Functions invoking service account and thus permissions, the emulator is not configurable and will use the globally-available account on your developer machine, similar to running a local script directly.

### Sign-in via email link on mobile

Since on mobile platforms, email link sign-in relies on Firebase Dynamic Links, all such links will be opened on the (mobile) web platform instead.

### Third-party sign-in

For third-party sign-in flows, FirebaseAuthenticationrelies on secure credentials from third-party providers like Twitter and Github.

Real credentials from OpenID Connect providers such as Google and Apple are accepted by theAuthenticationemulator. Credentials from non-OpenID Connect providers are not supported.

### Email / SMS sign-in

In production apps, email and SMS sign-in flows involve an asynchronous operation in which the user checks a received message and enters a login code into a sign-in interface. TheAuthenticationemulator doesn't send any emails or SMS messages, but as described[above](https://firebase.google.com/docs/emulator-suite/connect_auth#emulated_email_email_link_and_anonymous_authentication), it does generate login codes and output them to the terminal to be used in testing.

The emulator does not support the ability to define test phone numbers with fixed login codes as can be done using theFirebaseconsole.

### Custom token authentication

TheAuthenticationemulator does not validate the signature or expiry of custom tokens. This allows you to use hand-crafted tokens and re-use tokens indefinitely in prototyping and testing scenarios.

### Rate limiting / anti-abuse

TheAuthenticationemulator does not replicate production rate limiting or anti-abuse features.

### Blocking functions

In production, users are written to storage once after both the`beforeCreate`and`beforeSignIn`events are triggered. However, due to technical limitations, theAuthenticationemulator writes to store twice, once after user creation and another after sign-in. This means that for new users, you can successfully call`getAuth().getUser()`in`beforeSignIn`in theAuthenticationemulator, but you would encounter an error doing so in production.

## What next?

- For a curated set of videos and detailed how-to examples, follow the[Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).

- Since triggered functions are a typical integration withAuthentication, learn more about the Cloud Functions for Firebase emulator at[Run functions locally](https://firebase.google.com/docs/functions/local-emulator).