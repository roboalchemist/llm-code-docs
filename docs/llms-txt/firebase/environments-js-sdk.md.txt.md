# Source: https://firebase.google.com/docs/web/environments-js-sdk.md.txt

# Supported environments for the Firebase JavaScript SDK

## Supported environments

The Firebase JavaScript SDK is officially supported in the following environments.

> [!IMPORTANT]
> **Important:** You still need to [include polyfills](https://firebase.google.com/docs/web/environments-js-sdk#polyfills) for environments that don't support the features required by Firebase.

### Browsers

| Firebase product | Edge | Firefox | Chrome | iOS Safari | Safari |
|---|---|---|---|---|---|
| **Firebase AI Logic** ^1^ | Yes | Yes | Yes | Yes | Yes |
| **Analytics** | Yes | Yes | Yes | Yes | Yes |
| **App Check** | Yes | Yes | Yes | Yes | Yes |
| **Authentication** | Yes | Yes | Yes | Yes | Yes |
| **Cloud Firestore** | Yes (except persistence) | Yes | Yes | Yes (except persistence if iOS \< 10) | Yes |
| **Cloud Functions** | Yes | Yes | Yes | Yes | Yes |
| **Firebase installations** | Yes | Yes | Yes | Yes | Yes |
| **Cloud Messaging** | Yes (Edge 17+, except mobile) | Yes | Yes | Yes | Yes |
| **Cloud Storage** | Yes | Yes | Yes | Yes | Yes |
| **Data Connect** | Yes | Yes | Yes | Yes | Yes |
| **Performance Monitoring** | Yes | Yes | Yes | Yes | Yes |
| **Realtime Database** | Yes | Yes | Yes | Yes | Yes |
| **Remote Config** | Yes | Yes | Yes | Yes | Yes |

^**1** *Firebase AI Logic was formerly called
"Vertex AI in Firebase".*^

### Other environments

| Firebase product | React Native | Node.js (18+) | Chrome Extensions | Cordova |
|---|---|---|---|---|
| **Firebase AI Logic** ^1^ | Yes | Yes | Yes | Yes |
| **App Check** | Yes (using a [custom provider](https://firebase.google.com/docs/app-check/android/custom-provider) to do native device attestation) | Yes (using a [custom provider](https://firebase.google.com/docs/app-check/custom-provider)) | No | No |
| **Analytics** | No | No | No | No |
| **Authentication** | Yes (see [Note](https://firebase.google.com/docs/web/environments-js-sdk#auth-note)) | Yes (see [Note](https://firebase.google.com/docs/web/environments-js-sdk#auth-note)) | Yes (see [Note](https://firebase.google.com/docs/web/environments-js-sdk#auth-note)) | Yes (see [Note](https://firebase.google.com/docs/web/environments-js-sdk#auth-note)) |
| **Cloud Firestore** | Yes (except persistence) | Yes (except persistence) | Yes | Yes |
| **Cloud Functions** | Yes | Yes | Yes | Yes |
| **Data Connect** | Yes | Yes | No | No |
| **Firebase installations** | No | No | No | No |
| **Cloud Messaging** | No | No | Yes | No |
| **Cloud Storage** | Yes (except uploads) | Yes | Yes | Yes |
| **Performance Monitoring** | No | No | No | No |
| **Realtime Database** | Yes | Yes | Yes | Yes |
| **Remote Config** | No | No | Yes | Yes |

^**1** *Firebase AI Logic was formerly called
"Vertex AI in Firebase".*^

> [!NOTE]
> **Note:** All Authentication features, *except phone authentication and popup/redirect OAuth operations*, are supported.

## Polyfills

The Firebase JavaScript SDK is built on the latest standards of the web platform. Some
older browsers and JavaScript environments do not support all the features
required by Firebase. If you must support these browsers/environments, then you
need to load polyfills accordingly.

The sections below identify most of the polyfills you might need.

### Required polyfills

| **Environments** | **Polyfills** |
|---|---|
| Safari 7 \& 8 \& 9 | [ES Stable](https://firebase.google.com/docs/web/environments-js-sdk#suggested-polyfills) |
| Node \< 10 | [ES Stable](https://firebase.google.com/docs/web/environments-js-sdk#suggested-polyfills) |

### Optional polyfills

| **Environments** | **Polyfills** | **Firebase products** |
|---|---|---|
| - Safari \< 10.1 - iOS \< 10.3 | [fetch](https://firebase.google.com/docs/web/environments-js-sdk#suggested-polyfills) | - Authentication - Cloud Firestore - Cloud Functions - Performance Monitoring |
| - Node \< 18 | [fetch](https://firebase.google.com/docs/web/environments-js-sdk#suggested-polyfills) | - Authentication - Cloud Firestore - Cloud Functions - Cloud Storage |
| - React Native and Expo | [base-64](https://firebase.google.com/docs/web/environments-js-sdk#suggested-polyfills) | - Cloud Storage |

### Suggested polyfills

| **Polyfills** | **License** |
|---|---|
| [ES Stable](https://github.com/zloirock/core-js/tree/master/packages/core-js/stable) | MIT |
| [fetch](https://github.com/lquixada/cross-fetch) - \`cross-fetch\` - best for older browsers | MIT |
| [fetch](https://github.com/nodejs/undici) - \`undici\` - best for Node.js | MIT |
| [base-64](https://firebase.google.com/docs/web/environments-js-sdk#react-native-polyfill-setup) | MIT |

### Required Polyfill Setup for React Native and Expo

For React Native and Expo if you are uploading a base-64 encoded string, you need to do the following:

Install [base-64](https://github.com/mathiasbynens/base64) from npm:

<br />

```
npm install base-64
```

<br />

Import `decode` from `base-64` and attach it to the global scope as `atob` so
Cloud Storage can access it.

    import { decode } from 'base-64';

    if(typeof atob === 'undefined') {
      global.atob = decode;
    }

## Add polyfills in your application

### **Option 1** : *(Recommended)* Use bundler integrated with Babel

If you're using a bundler, integrate with [Babel](https://babeljs.io/) and
[@babel/preset-env](https://babeljs.io/docs/en/babel-preset-env) to get
polyfills.

Use Babel's interactive [setup guide](https://babeljs.io/setup.html) to learn
how to integrate Babel with your bundler.

With Babel, you don't need to worry about the exact polyfills to include.
Instead, you specify the minimal browser environments that you need to support.
Babel then adds the necessary polyfills for you. Babel ensures that your
requirements for browser support are always met, even if Firebase or your own
code starts using new ES features.

[@babel/preset-env](https://babeljs.io/docs/en/babel-preset-env) has detailed
information about the available configuration options for specifying environment
targets (option `targets`) and adding polyfills (option `useBuiltIns`).

> [!NOTE]
> **Note:** If you're using a framework, the work of configuring Babel and adding polyfills might be different or actually already handled for you. Refer to Babel's interactive [setup guide](https://babeljs.io/setup.html) for more information.

### **Option 2** : *(Not Recommended)* Add polyfills manually

You can add polyfills manually using your favorite polyfill libraries (for
example, [`core-js`](https://github.com/zloirock/core-js/tree/v3)).

    import 'core-js/stable'
    import 'cross-fetch/polyfill';

`core-js` also provides an
[all-in-one polyfill file](https://unpkg.com/core-js-bundle@3.0.1/minified.js)
that you can directly include in the HTML page.

This option can be a convenient way for managing polyfills if you don't use
Babel. However, **we don't recommend this all-in-one option for production
apps** as it will likely include unnecessary polyfills, which increases the page
weight and hence the page load time.