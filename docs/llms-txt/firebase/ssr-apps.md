# Source: https://firebase.google.com/docs/web/ssr-apps.md.txt

If you have worked with the Firebase JS SDK or other Firebase client SDKs, you are probably familiar with the`FirebaseApp`interface and how to use it to configure app instances. To facilitate similar operations on the server side, Firebase provides`FirebaseServerApp`.

`FirebaseServerApp`is a variant of`FirebaseApp`for use in server-side rendering (SSR) environments. It includes tools to continue Firebase sessions that span the client side rendering (CSR) / server-side rendering divide. These tools and strategies can help enhance dynamic web apps built with Firebase and deployed in Google environments like[Firebase App Hosting](https://firebase.google.com/docs/app-hosting).

Use`FirebaseServerApp`to:

- Execute server-side code within the*user*context, in contrast to the Firebase Admin SDK which has full administration rights.
- Enable the use of App Check in SSR environments.
- Continue a Firebase Auth session that was created in the client.

## The FirebaseServerApp lifecycle

Server-side rendering (SSR) frameworks and other non-browser runtimes such as cloud workers optimize for initialization time by reusing resources across multiple executions.`FirebaseServerApp`is designed to accommodate these environments by using a reference count mechanism. If an app invokes`initializeServerApp`with the same parameters as a previous`initializeServerApp`, it receives the same`FirebaseServerApp`instance that was already initialized. This cuts down on unnecessary initialization overhead and memory allocations. When`deleteApp`is invoked on a`FirebaseServerApp`instance, it reduces the reference count, and the instance is freed after the reference count reaches zero.

### Cleaning up`FirebaseServerApp`instances

It can be tricky to know when to call`deleteApp`on a`FirebaseServerApp`instance, especially if you are running many asynchronous operations in parallel. The`releaseOnDeref`field of the`FirebaseServerAppSettings`helps simplify this. If you assign`releaseOnDeref`a reference to an object with the lifespan of the request's scope (for example, the headers object of the SSR request), the`FirebaseServerApp`will reduce its reference count when the framework reclaims the header object. This automatically cleans up your`FirebaseServerApp`instance.
| **Note:** The value`FirebaseServerApp.releaseOnDeref`is not used when`initializeServerApp`checks for an existing`FirebaseServerApp`instance with an identical configuration.

Here's an example usage of`releaseOnDeref`:  

    /// Next.js
    import { headers } from 'next/headers'
    import { FirebaseServerAppSettings, initializeServerApp} from "@firebase/app";

    export default async function Page() {
      const headersObj = await headers();
      appSettings.releaseOnDeref = headersObj;
      let appSettings: FirebaseServerAppSettings = {};
      const serverApp = initializeServerApp(firebaseConfig, appSettings);
      ...
    }

| **Note:** Avoid mixing`deleteApp()`calls with instances that were created with`releaseOnDeref`; otherwise apps might be destroyed earlier than intended.

## Resume authenticated sessions created on the client

When an instance of`FirebaseServerApp`is initialized with an Auth ID token, it enables bridging of authenticated user sessions between the client-side rendering (CSR) and server-side rendering (SSR) environments. Instances of the Firebase Auth SDK initialized with a`FirebaseServerApp`object containing an Auth ID token will attempt to sign in the user on initialization without the need for the application to invoke any sign-in methods.

Providing an Auth ID token allows apps to use any of Auth's sign-in methods on the client, ensuring that the session continues on the server-side, even for those sign-in methods that require user interaction. Additionally, it enables the offloading of intensive operations to the server such as authenticated Firestore queries, which should improve your app's rendering performance.  

    /// Next.js
    import { initializeServerApp } from "firebase/app";
    import { getAuth } from "firebase/auth";

    // Replace the following with your app's
    // Firebase project configuration
    const firebaseConfig = {
      // ...
    };

    const firebaseServerAppSettings = {
      authIdToken: token  // See "Pass client tokens to the server side
                          // rendering phase" for an example on how transmit
                          // the token from the client and the server.
    }

    const serverApp =
      initializeServerApp(firebaseConfig,
                          firebaseServerAppSettings);
    const serverAuth = getAuth(serverApp);

    // FirebaseServerApp and Auth will now attempt
    // to sign in the current user based on provided
    // authIdToken.

| **Note:** Auth instances created with`FirebaseServerApp`don't support operations that log out the current user, sign in a new user, or otherwise replace the current user. Mutations to the Auth user state should be driven by the browser session.

## Use App Check in SSR environments

App Check enforcement relies on an App Check SDK instance that Firebase SDKs use to internally call`getToken`. The resulting token is then included in requests to all Firebase services, allowing the backend to validate the app.

However, because the App Check SDK needs a browser to access specific heuristics for app validation, it can't be initialized in server environments.

`FirebaseServerApp`provides an alternative. If a client-generated App Check token is provided during`FirebaseServerApp`initialization, it will be used by the Firebase product SDKs when invoking Firebase services, eliminating the need for an App Check SDK instance.  

    /// Next.js
    import { initializeServerApp } from "firebase/app";

    // Replace the following with your app's
    // Firebase project configuration
    const firebaseConfig = {
      // ...
    };

    const firebaseServerAppSettings = {
      appCheckToken: token // See "Pass client tokens to the server side
                           // rendering phase" for an example on how transmit
                           // the token from the client and the server.
    }

    const serverApp =
      initializeServerApp(firebaseConfig,
                          firebaseServerAppSettings);

    // The App Check token will now be appended to all Firebase service requests.

| **Note:** If the token fails local verification due to expiration or parsing errors, then a console error is logged at the time of initialization of the`FirebaseServerApp`instance.

## Pass client tokens to the server-side rendering phase

To transmit authenticated Auth ID tokens (and App Check tokens) from the client to the server-side rendering (SSR) phase, use a service worker. This approach involves intercepting fetch requests that trigger SSR and appending the tokens to the request headers.

Refer to[Session management with service workers](https://firebase.google.com/docs/auth/web/service-worker-sessions)for a reference implementation of a Firebase Auth service worker. Also see[Server side changes](https://firebase.google.com/docs/auth/web/service-worker-sessions#server_side_changes)for code that demonstrates how to parse these tokens from the headers for use in`FirebaseServerApp`initialization.
| **Tip:** Refreshing the tokens within the service worker before appending them to the request headers is a best practice that ensures the SSR phase receives up-to-date credentials.