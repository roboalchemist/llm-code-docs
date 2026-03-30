# Source: https://firebase.google.com/docs/app-hosting/firebase-sdks.md.txt

Firebase App Hosting is a natural fit for dynamic web apps built with the
Firebase JavaScript SDK and Firebase Admin SDK for Node.js. In a full-featured
web app, Firebase SDKs like Authentication, Cloud Firestore, and App Check
have important roles to play. This guide describes some key strategies to help
optimize Firebase SDKs and get started building Firebase into
your web app on Firebase App Hosting.

## Automatically initialize Firebase Admin SDK and web SDKs

Google environments such as Firebase App Hosting provide simplified app
initialization through a no-argument constructor call at build time and runtime.
This is a feature both of the [Firebase Admin SDK for
Node.js](https://firebase.google.com/docs/admin/setup) -- a server-side SDK that
unlocks a large area of Firebase functionality and can be very useful
in your web app -- and the [Firebase JavaScript SDK](https://firebase.google.com/docs/web/learn-more).

With `initializeApp()`, you can let Firebase App Hosting automatically
populate web app configuration for you while still keeping the option of
fine-grained control over specific values if you want to override default
values.

### Initialize with no arguments

To initialize either the Firebase Admin SDK or the Firebase JavaScript SDK with default
configuration values, use `initializeApp()` without supplying any arguments.

#### Admin SDK

    import { initializeApp } from 'firebase-admin/app';
    const app = initializeApp();

For the Admin SDK, this initialization strategy works in App Hosting
as well as other Google server environments including Cloud Run,
App Engine, and Cloud Run functions.

#### JavaScript SDK

    import { initializeApp } from 'firebase/app';
    const app = initializeApp();

For the JavaScript SDK, this initialization strategy works in App Hosting.

> [!NOTE]
> **Note:** No-argument initialization of the JavaScript SDK depends on [`postinstall` scripts](https://docs.npmjs.com/cli/v11/using-npm/scripts) which are disabled in Pnpm by default; opt-in with the [`pnpm.onlybuiltdependencies` option](https://pnpm.io/9.x/package_json#pnpmonlybuiltdependencies) in `your package.json`.

### Override autopopulated values

You can override the default configuration that is automatically injected. Note
that these options differ between the Admin SDK and JavaScript SDK.

#### Admin SDK override

To optionally specify custom initialization options for services such as
Realtime Database, Cloud Storage, or Cloud Functions, use the `FIREBASE_CONFIG`
environment variable. If the content of the `FIREBASE_CONFIG` variable begins
with a `{` character it will be parsed as a JSON object. Otherwise the SDK
assumes that the string is the path of a JSON file containing the options.

    # apphosting.yaml

    env:
      - variable: FIREBASE_CONFIG
        value: '{"credential: applicationDefault()","databaseURL":"https://project-id-default-rtdb.firebaseio.com"}'

#### JavaScript SDK override

To override the default `FIREBASE_WEBAPP_CONFIG` values that App Hosting
injects for JavaScript SDK initialization, you can specify values in
`apphosting.yaml`:

    # apphosting.yaml

    env:
      - variable: FIREBASE_WEBAPP_CONFIG
        value: '{"apiKey":"myApiKey","appId":"app:123","authDomain":"project-id.firebaseapp.com","databaseURL":"https://project-id-default-rtdb.firebaseio.com","messagingSenderId":"0123456789","projectId":"project-id","storageBucket":"project-id.firebasestorage.app"}'

### Using automatic initialization in other environments

Automatic initialization is set up with an [npm `postinstall`
script](https://docs.npmjs.com/cli/v11/using-npm/scripts#npm-install) when you
install the Firebase JavaScript SDK. The `postinstall` script looks for the
environment variable `FIREBASE_WEBAPP_CONFIG`, which is set automatically
in the App Hosting Cloud Build environment.

> [!NOTE]
> **Note:** `postinstall` scripts are disabled in Pnpm by default; opt-in with the [`pnpm.onlybuiltdependencies` option](https://pnpm.io/9.x/package_json#pnpmonlybuiltdependencies) in `your package.json`.

If you're installing the JS SDK outside of Cloud Build, you'll need to set this
environment variable yourself when you install the Firebase JavaScript SDK.

To set up the environment manually at installation:

1. Copy your [Firebase web app config object](https://firebase.google.com/docs/web/learn-more#config-object)
   from the Firebase console.

2. From a terminal, set the `FIREBASE_WEBAPP_CONFIG` environment variable
   before running the `npm install` command.

    FIREBASE_WEBAPP_CONFIG="{...}" npm install firebase

Any time you change your Firebase
project or web app, re-run this command. Intermediate caches
(like `.next/cache`) may also need to be cleared.

## Use `FirebaseServerApp` for SSR

If you have worked with the Firebase JS SDK or other Firebase client SDKs in the
development of your web app, you are probably familiar with the `FirebaseApp`
interface and how to use it to configure app instances. To facilitate similar
operations on the server side, Firebase provides `FirebaseServerApp`.

`FirebaseServerApp` is a variant of `FirebaseApp` for use in server side
rendering (SSR) environments. It includes tools to continue Firebase sessions
that span the client side rendering (CSR) / server side rendering divide.

Use `FirebaseServerApp` to:

- Execute server-side code within the *user* context, in contrast to the Firebase Admin SDK which has full administration rights.
- Enable the use of App Check in SSR environments.
- Continue a Firebase Auth session that was created in the client.

For full detail on using `FirebaseServerApp` for these purposes, see [Use
Firebase in dynamic web apps with SSR](https://firebase.google.com/docs/web/ssr-apps).

## Enable App Check in your web app

You can use App Check to fortify the security of your dynamic web app on
App Hosting. By implementing some of the specific server side strategies
described in [Use Firebase in dynamic web apps with
SSR](https://firebase.google.com/docs/web/ssr-apps#use-app-check), you can protect your App Hosting
backends from abuse.