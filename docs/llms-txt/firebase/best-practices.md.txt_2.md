# Source: https://firebase.google.com/docs/web/best-practices.md.txt

# Firebase JavaScript SDK best practices

This page offers tips and troubleshooting for JavaScript issues that you might
encounter when using the Firebase JavaScript SDK.

Have other challenges or don't see your issue? Make sure to check
out the [main Firebase FAQ](https://firebase.google.com/support/faq) for more pan-Firebase or
product-specific FAQ.

You can also check the [Firebase JavaScript SDK GitHub
repo](https://github.com/firebase/firebase-js-sdk) for an up-to-date list of
reported issues and troubleshooting, and file your own issues there.

## Admin SDK for Node.js constructs are not compatible with the Firebase JavaScript SDK

The Firebase Admin SDK for Node.js and the Firebase JavaScript SDK are distinct
implementations that do not share interface, class, or function definitions.
Instances of Admin SDK objects are incompatible with Firebase JavaScript SDK
functions.

For example, an instance of the Admin SDK's `FirebaseApp` passed to the
Firebase JavaScript SDK `getDatabase` function produces the following error:

    TypeError: Cannot read properties of undefined (reading 'getProvider')
     at _getProvider
     at getDatabase

This is true for the entire Firebase JavaScript SDK API surface, not just Realtime Database.
It's also true for usage in the opposite direction. Attempting to use the
Cloud Firestore JS SDK's `Timestamp` type with the Firebase Admin SDK for Node.js
produces similar errors.

## Avoid using conflicting versions of the Firebase JavaScript SDK

Multiple conflicting versions of the Firebase JavaScript SDK configured as dependencies
in a project will cause runtime errors when SDK instances are passed between SDK
packages. For example, using the Data Connect library with a
mismatched version of `FirebaseApp` causes the following error:

    Error: Component data-connect has not been registered yet

This issue is commonly caused by a dependency update of one but not all of the
Firebase SDK packages. This situation often occurs when an automated dependency
update tool changes a subset of the Firebase SDK dependencies within the
project's `yarn.lock` or `package-lock.json` file. Since many Firebase JavaScript SDKs
interoperate with each other, the use of various versions of the SDKs causes
runtime incompatibilities,

To fix this issue, delete the `node_modules`/ directory and the `yarn.lock` (for
`yarn`) or `package-lock.json` (for `npm`) in your project and reinstall your
dependencies.

If errors remain, further debug the issue with the [npm ls
command](https://docs.npmjs.com/commands/npm-ls). This will log the dependencies
of your project so you can identify conflicting versions of the `firebase`
module.

For example, the following log shows `package-using-older-firebase` importing a
conflicting version of the Firebase JavaScript SDK:

    $ npm ls firebase --all
    your-app@0.0.0
    ├── firebase@11.2.0
    ├─┬ @angular/fire@19.0.0
    │ ├── firebase@11.2.0 deduped
    │ └─┬ rxfire@6.1.0
    │   └── firebase@10.14.1 deduped
    └─┬ package-using-older-firebase@0.1.0
      └─── firebase@10.14.1

Errors may also occur due to mixing CJS and ESM's `require` and `import`
statements in your app. This creates multiple instances of the Firebase JavaScript SDK,
each distinct from the other, which breaks Firebase JavaScript SDK interoperability.
Increase the verbosity of your bundler of choice to debug this scenario. For
example, you can use the [esbuild analyze
flag](https://esbuild.github.io/api/#analyze) for this purpose.

## Make sure that service workers are bundled

Service workers are often built from a separate pipeline from the rest of a web
app, and are not included in the default configuration of bundlers such as
Webpack.

If you use the modular version of the Firebase JavaScript SDK within your service
worker, then make sure you configure your app bundler to include the service
worker source file. The following example uses `npx` to bundle the
`firebase-sw.js` service worker in the project's `src` directory:

    npx esbuild ./src/firebase-sw.js --bundle --minify --main-fields=webworker,browser,module,main,default --outfile=public/firebase-sw.js

The activation of a service worker that is not bundled will fail if it sources
import ES modules that don't support service workers or files that don't exist
in the service worker's scope. Sometimes these failures are silent and hard to
debug.

See [Using module bundlers with Firebase](https://firebase.google.com/docs/web/module-bundling) for more
information about bundling the modular version of the Firebase JavaScript SDK into your
app.

Alternatively, you can eliminate the need for bundling by importing the `compat`
Firebase JavaScript SDK bundles from the CDN:

    // Give the service worker access to Firebase Messaging.
    // Replace 10.13.2 with the version of the Firebase JS SDK you're using
    // in your app.
    importScripts('https://www.gstatic.com/firebasejs/10.13.2/firebase-app-compat.js');
    importScripts('https://www.gstatic.com/firebasejs/10.13.2/firebase-messaging-compat.js');

    // Initialize the Firebase app in the service worker by passing in
    // your app's Firebase config object.
    // https://firebase.google.com/docs/web/setup#config-object
    firebase.initializeApp({
      ...
    });

    // Retrieve an instance of Firebase Messaging so that it can handle
    // background messages.
    const messaging = firebase.messaging();

## Use `FirebaseServerApp` when working with Server Side Rendering

The Firebase JavaScript SDK was originally intended to run in browser environments. The
introduction of Server-Side Rendering (SSR) frameworks pushes SDK usage into new
runtime environments. These runtimes provide a subset of tools and APIs that web
browsers provide.

For example, some Firebase SDKs require data caching with IndexedDB, a
browser-only API. Firebase Auth may require user interaction in certain sign-in
flows that is impossible in headless server environments. App Check relies
on browser heuristics to validate the user before creating App Check tokens.

When working with the SDK in these new environments, use
[`FirebaseServerApp`](https://firebase.google.com/docs/reference/js/app.firebaseserverapp), a new variant
of `FirebaseApp` that provides the means to preload the SSR Firebase instance
with data that was collected from the client side.

`FirebaseServerApp` supports two parameters:

- **Auth ID Token**: if provided, Firebase Auth automatically signs in a previously authenticated user, potentially spanning a session across the CSR / SSR divide.
- **App Check Token** : If provided, the token is used by the other Firebase SDKs without the need to initialize an instance of an App Check client (which isn't supported outside browser environments). This unblocks SSR support for products that have App Check enabled, such as Cloud Functions, Data Connect, Cloud Firestore, Realtime Database, and Vertex AI.

See [Streamline SSR app development with
FirebaseServerApp](https://firebase.blog/posts/2024/05/firebase-serverapp-ssr/)
for example usage of `FirebaseServerApp` in Next.js.