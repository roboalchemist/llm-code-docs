# Source: https://firebase.google.com/docs/app-check/web/custom-provider.md.txt

This page shows you how to enable App Check in a web app, using [your custom
App Check provider](https://firebase.google.com/docs/app-check/web/custom-provider). When you enable App Check, you
help ensure that only your app can access your project's Firebase resources.

If you want to use App Check with one of the built-in providers, see the
docs for
[App Check with reCAPTCHA Enterprise](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider).

## Before you begin

- [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup) if you haven't
  already done so.

- [Implement your custom App Check provider's server-side logic](https://firebase.google.com/docs/app-check/custom-provider).

## 1. Add the App Check library to your app

[Add Firebase to your web app](https://firebase.google.com/docs/web/setup) if you haven't already. Be sure
to import the App Check library.

## 2. Create the App Check provider object

Create an App Check provider object for your custom provider. This object
must have a `getToken()` method, which collects whatever information your custom
App Check provider requires as proof of authenticity, and sends it to your
token acquisition service in exchange for an App Check token. The
App Check SDK handles token caching, so always get a new token in your
implementation of `getToken()`.

### Web

```javascript
import { CustomProvider } from "firebase/app-check";

const appCheckCustomProvider = new CustomProvider({
  getToken: () => {
    return new Promise((resolve, _reject) => {
      // TODO: Logic to exchange proof of authenticity for an App Check token and
      // expiration time.

      // ...

      const appCheckToken = {
        token: tokenFromServer,
        expireTimeMillis: expirationFromServer * 1000
      };

      resolve(appCheckToken);
    });
  }
});
```

### Web

```javascript
const appCheckCustomProvider = {
  getToken: () => {
    return new Promise((resolve, _reject) => {
      // TODO: Logic to exchange proof of authenticity for an App Check token and
      // expiration time.

      // ...

      const appCheckToken = {
        token: tokenFromServer,
        expireTimeMillis: expirationFromServer * 1000
      };

      resolve(appCheckToken);
    });
  }
};
```

## 3. Initialize App Check

Add the following initialization code to your application, before you access any
Firebase services:

### Web

```javascript
import { initializeApp } from "firebase/app";
import { initializeAppCheck } from "firebase/app-check";

const app = initializeApp({
  // Your firebase configuration object
});

const appCheck = initializeAppCheck(app, {
  provider: appCheckCustomProvider,

  // Optional argument. If true, the SDK automatically refreshes App Check
  // tokens as needed.
  isTokenAutoRefreshEnabled: true    
});
```

### Web

```javascript
firebase.initializeApp({
  // Your firebase configuration object
});

const appCheck = firebase.appCheck();
appCheck.activate(
  appCheckCustomProvider,

  // Optional argument. If true, the SDK automatically refreshes App Check
  // tokens as needed.
  true);
```

> [!NOTE]
> **Note:** The SDK will not automatically refresh App Check tokens by default. That functionality must be explicitly enabled by providing `true` as a second argument to `activate()` or by calling `firebase.appCheck().setTokenAutoRefreshEnabled(true)`. For more, see [the App Check reference docs](https://firebase.google.com/docs/reference/js/firebase.appcheck.AppCheck).

## Next steps

Once the App Check library is installed in your app, deploy it.

The updated client app will begin sending App Check tokens along with every
request it makes to Firebase, but Firebase products will not require the tokens
to be valid until you enable enforcement in the App Check section of the
Firebase console.

### Monitor metrics and enable enforcement

Before you enable enforcement, however, you should make sure that doing so won't
disrupt your existing legitimate users. On the other hand, if you're seeing
suspicious use of your app resources, you might want to enable enforcement
sooner.

To help make this decision, you can look at App Check metrics for the
services you use:

- [Monitor App Check request metrics](https://firebase.google.com/docs/app-check/monitor-metrics) for Firebase AI Logic, Data Connect, Realtime Database, Cloud Firestore, Cloud Storage, Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [Monitor App Check request metrics for Cloud Functions](https://firebase.google.com/docs/app-check/monitor-functions-metrics).

### Enable App Check enforcement

When you understand how App Check will affect your users and you're ready to
proceed, you can enable App Check enforcement:

- [Enable App Check enforcement](https://firebase.google.com/docs/app-check/enable-enforcement) for Firebase AI Logic, Data Connect, Realtime Database, Cloud Firestore, Cloud Storage, Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [Enable App Check enforcement for Cloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).

### Use App Check in debug environments

If, after you have registered your app for App Check, you want to run your
app in an environment that App Check would normally not classify as valid,
such as locally during development, or from a continuous integration (CI)
environment, you can create a debug build of your app that uses the
App Check debug provider instead of a real attestation provider.

See [Use App Check with the debug provider in web apps](https://firebase.google.com/docs/app-check/web/debug-provider).