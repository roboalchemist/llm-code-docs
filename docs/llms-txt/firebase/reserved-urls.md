# Source: https://firebase.google.com/docs/hosting/reserved-urls.md.txt

<br />

Firebase Hostingreserves URLs in your site beginning with`/__`. This reserved namespace makes it easier to use other Firebase products together withFirebase Hosting.

These reserved URLs are available both when you deploy to Firebase (`firebase deploy`) or when you run your app on a local server (`firebase serve`).

## Add scripts for reserved URLs

BecauseFirebase Hostingis served over HTTP/2 when deployed, you can boost performance by loading files from the same origin.Firebase Hostingserves version 8 of theFirebaseJavaScriptSDK from special URLs formatted like so:  

```
/__/firebase/JS_SDK_VERSION/FIREBASE_SDK_NAME.js
```

We strongly recommend loading only the[libraries](https://firebase.google.com/docs/hosting/reserved-urls#libraries_hosting-urls)that you use in your app. For example, to include onlyAuthenticationandCloud Firestore, add the following scripts to the bottom of your`<body>`tag, but before you use any Firebase services:  

    <body>
      <!-- Insert these scripts at the bottom of the HTML, but before you use any Firebase services -->
      <!-- Firebase App (the core Firebase SDK) is always required and must be listed first -->
      <script src="/__/firebase/8.10.1/firebase-app.js"></script>

      <!-- Add Firebase products that you want to use -->
      <script src="/__/firebase/8.10.1/firebase-auth.js"></script>
      <script src="/__/firebase/8.10.1/firebase-firestore.js"></script>
    </body>

### SDK auto-configuration

Automatic SDK configuration makes it easy to manage multiple environments (such as dev, staging, and production) from a single codebase. By relying on the reservedHostingURL, you can deploy the same code to multiple Firebase projects.

In addition to hosting the SDKs themselves, the reserved namespace also provides all of the configuration necessary to initialize the SDK for the Firebase project associated with theHostingsite. This Firebase configuration and SDK initialization is provided by a script that you can include directly:  

    <!-- Load the Firebase SDKs before loading this file -->
    <script src="/__/firebase/init.js"></script>

When you deploy to Firebase or test your app locally, this script automatically configures theFirebaseJavaScriptSDK for the[active Firebase project](https://firebase.google.com/docs/cli#project_aliases)and initializes the SDK.

If you prefer to control initialization yourself, the Firebase configuration values are also available in JSON form:  

    fetch('/__/firebase/init.json').then(async response => {
      firebase.initializeApp(await response.json());
    });

## Available Firebase JS SDKs (from reservedHostingURLs)

| ReservedHostingURLs are available only with version 8 and earlier. You cannot use version 9 or later withHostingURLs.

|                                              **Firebase product**                                               |                                                                   **Library reference (reserved URL)**                                                                   |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firebase core (required)                                                                                        | ```scdoc <script src="/__/firebase/8.10.1/firebase-app.js"></script> ```                                                                                                 |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=web)                                | ```scdoc <script src="/__/firebase/8.10.1/firebase-analytics.js"></script> ```                                                                                           |
| [App Check](https://firebase.google.com/docs/app-check)                                                         | ```scdoc <script src="/__/firebase/8.10.1/firebase-app-check.js"></script> ```                                                                                           |
| [Authentication](https://firebase.google.com/docs/auth/web/start)                                               | ```scdoc <script src="/__/firebase/8.10.1/firebase-auth.js"></script> ```                                                                                                |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart)                                        | ```scdoc <script src="/__/firebase/8.10.1/firebase-firestore.js"></script> ```                                                                                           |
| [Cloud Functions for FirebaseClient SDK](https://firebase.google.com/docs/functions/callable#call_the_function) | ```scdoc <script src="/__/firebase/8.10.1/firebase-functions.js"></script> ```                                                                                           |
| [Firebaseinstallations](https://firebase.google.com/docs/projects/manage-installations)                         | ```scdoc <script src="/__/firebase/8.10.1/firebase-installations.js"></script> ```                                                                                       |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/js/client)                                   | ```scdoc <script src="/__/firebase/8.10.1/firebase-messaging.js"></script> ``` For an optimal experience usingCloud Messaging, also add the Firebase SDK forAnalytics.   |
| [Cloud Storage](https://firebase.google.com/docs/storage/web/start)                                             | ```scdoc <script src="/__/firebase/8.10.1/firebase-storage.js"></script> ```                                                                                             |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-web) *(**beta**release)*         | ```scdoc <script src="/__/firebase/8.10.1/firebase-performance.js"></script> ```                                                                                         |
| [Realtime Database](https://firebase.google.com/docs/database/web/start)                                        | ```scdoc <script src="/__/firebase/8.10.1/firebase-database.js"></script> ```                                                                                            |
| [Remote Config](https://firebase.google.com/docs/remote-config/use-config-web) *(**beta**release)*              | ```scdoc <script src="/__/firebase/8.10.1/firebase-remote-config.js"></script> ``` For an optimal experience usingRemote Config, also add the Firebase SDK forAnalytics. |
| FirebaseJavaScriptSDK (entire SDK)                                                                              | ```scdoc <script src="/__/firebase/8.10.1/firebase.js"></script> ```                                                                                                     |

## Auth helpers

[Firebase Authentication](https://firebase.google.com/docs/auth/)uses the reserved namespace to provide special JavaScript and HTML to complete authentication with providers via OAuth. This allows each Firebase project to have a unique Firebase subdomain, increasing the security ofFirebase Authentication.

In addition, this allows you to use your own custom domain for the`authDomain`option of`firebase.initializeApp()`. If you[configure a custom domain](https://firebase.google.com/docs/hosting/custom-domain)forFirebase Hosting, then you can also specify that custom domain (instead of your`web.app`or`firebaseapp.com`subdomain) when initializing the Firebase SDKs. See[Best practices for using signInWithRedirect](https://firebase.google.com/docs/auth/web/redirect-best-practices#update-authdomain)for more details on using a custom domain.

## Reserved URLs and service workers

If you are building a Progressive Web App (PWA), you might create a service worker that has a "navigation fallback" and renders a specific URL by default if it doesn't match a list of precached items.
| You must disable any fallbacks for the \`/__\` namespace in order forFirebase Hostingto function properly.

If you're using the[sw-precache](https://github.com/GoogleChrome/sw-precache)library, you can add a navigation fallback whitelist setting that excludes the reserved namespace:  

    {
      navigateFallbackWhitelist: [/^(?!\/__).*/]
    }

In general, just remember that the double-underscore namespace is reserved for Firebase usage and that you should not intercept these requests in your service worker.