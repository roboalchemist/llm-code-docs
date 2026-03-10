# Source: https://firebase.google.com/docs/web/learn-more.md.txt

# Understand Firebase for web

As you're developing a web app using Firebase, you might encounter unfamiliar
concepts, or areas where you need more information to make the right decisions
for your project. This page aims to answer those questions or point you to
resources to learn more.

If you have questions about a topic not covered on this page, visit one of our
[online communities](https://firebase.google.com/community#join-the-discussion).
We'll also update this page with new topics periodically, so
check back to see if we've added the topic you want to learn about.

## SDK versions: namespaced and modular

Firebase provides two API surfaces for web apps:

- **JavaScript - namespaced.** This is the JavaScript interface that Firebase maintained for many years and is familiar to web developers with older Firebase apps. Because the namespaced API does not benefit from ongoing new feature support, most new apps should instead adopt the modular API.
- **JavaScript - modular** . This SDK is based on a modular approach that provides reduced SDK size and greater efficiency with modern JavaScript build tools such as [webpack](https://webpack.js.org/) or [Rollup](https://rollupjs.org/).

The modular API integrates well with build tools that strip out code that isn't being
used in your app, a process known as "tree-shaking." Apps built with this SDK
benefit from greatly reduced size footprints. The namespaced API, though available as a
module, does not have a strictly modular structure and does not provide the
same degree of size reduction.

Though the majority of the modular API follows the same patterns as the namespaced API,
the organization of the code is different. Generally, the namespaced API is
oriented towards a namespace and service pattern, while the modular API is oriented
toward discrete functions. For example, the namespaced API's dot-chaining, such as
`firebaseApp.auth()`, is replaced in the modular API by a single `getAuth()` function
that takes `firebaseApp` and returns an Authentication instance.

This means that web apps created with the namespaced API require
refactoring in order to take advantage of modular app design.
See the
[upgrade guide](https://firebase.google.com/docs/web/modular-upgrade) for further details.

### JavaScript - modular API for new apps

If you're starting on a new integration with Firebase, you can opt into the
modular API when you
[add and initialize the SDK](https://firebase.google.com/docs/web/setup?sdk_version=v9#add-sdks-initialize).

As you develop your app, keep in mind that your code will be organized
principally around **functions**. In the modular API, services are passed as the first
argument, and the function then uses the details of the service to do the rest.
For example:

    import { getAuth, onAuthStateChanged } from "firebase/auth";

    const auth = getAuth(firebaseApp);
    onAuthStateChanged(auth, user => {
      // Check for user status
    });

For more examples and details, see the guides for each product area as well
as the [the modular API reference documentation](https://firebase.google.com/docs/reference/js).

## Ways to add the web SDKs to your app

Firebase provides JavaScript libraries for most Firebase products, including
Remote Config, FCM, and more. How you add Firebase SDKs to your
Web app depends on what tooling you're using with your app (like a module
bundler).

You can add any of the
[available libraries](https://firebase.google.com/docs/web/learn-more#available-libraries) to your app via one of the
supported methods:

- npm (for module bundlers)
- CDN (content delivery network)

For detailed setup instructions, see
[Add Firebase to your JavaScript App](https://firebase.google.com/docs/web/setup). The rest of this section
contains information to help you choose from the available options.

> [!NOTE]
> **Note:** We do not recommend creating a new Firebase app with namespaced API libraries, which don't provide optimization such as tree-shaking. Existing apps using the namespaced API can still find details and code snippets in the how-to guides for each product area (for instance, FCM [message handling](https://firebase.google.com/docs/cloud-messaging/js/receive) guides).

### npm

Downloading the Firebase npm package (which includes both browser and Node.js
bundles) provides you with a local copy of the Firebase SDK, which may be needed
for non-browser applications such as Node.js apps, React Native, or Electron.
The download includes Node.js and React Native bundles as an option for some
packages. The Node.js bundles are necessary for the server-side rendering (SSR)
step of SSR frameworks.

Using npm with a module bundler such as
[webpack](https://webpack.js.org/) or
[Rollup](https://rollupjs.org/) provides optimization
options to "tree-shake" unused code and apply targeted polyfills, which can
greatly reduce the size footprint of your app. Implementing these features may
add some complexity to your configuration and build chain, but various
mainstream CLI tools can help mitigate that. These tools include
[Angular](https://angular.io),
[React](https://reactjs.org),
[Vue](https://vuejs.org/),
[Next](https://nextjs.org/), and others.

In summary:

- Provides valuable app size optimization
- Robust tooling is available to manage modules
- Required for SSR with Node.js

### CDN (content delivery network)

Adding libraries that are stored on Firebase's CDN
is a simple SDK setup method that may be familiar to many developers. Using the
CDN to add the SDKs, you won't need a build tool, and your build chain may tend
to be simpler and easier to work with compared to module bundlers.
If you're not especially concerned about
the installed size of your app and don't have special requirements such
as transpiling from TypeScript, then CDN could be a good choice.

In summary:

- Familiar and simple
- Appropriate when app size is not a major concern
- Appropriate when your website does not use build tools.

## Firebase web SDK variants

Firebase's web SDK can be used in both browser and Node applications.
However, several products are not available in Node environments.
See the list of [supported environments](https://firebase.google.com/docs/web/environments-js-sdk).

Some product SDKs provide separate browser and Node variants, each of which
are provided in both ESM and CJS formats, and some product SDKs even provide
Cordova or React Native variants. The web SDK is configured to provide the
correct variant based on your tooling config or environment and should not
require manual selection in most cases. All SDK variants are designed
to help build web apps or client apps
for end-user access, such as in a Node.js desktop or IoT application. If your
goal is to set up administrative access from privileged environments (such as
servers) use the
[Firebase Admin SDK](https://firebase.google.com/docs/admin/setup) instead.

### Environment detection with bundlers and frameworks

When you install the Firebase web SDK using npm, the JavaScript and Node.js
versions are both installed. The package provides detailed environment detection
to enable the right bundles for your application.

If your code uses Node.js `require` statements, the SDK finds the Node-specific
bundle. Otherwise, your bundler's settings must be correctly figured to detect
the right entry point field in your `package.json` file (for example, `main`,
`browser`, or `module`). If you experience runtime errors with the SDK, check to
make sure your bundler is configured to prioritize the correct type of bundle
for your environment.

## Learn about the Firebase config object

To initialize Firebase in your app, you need to provide your app's Firebase
configuration. You can [obtain your Firebase config
object](https://support.google.com/firebase/answer/7015592) at any time.

- We do not recommend manually editing your config object, especially the
  following required "Firebase options": `apiKey`, `projectId`, and `appID`. If
  you initialize your app with invalid or missing values for these required
  "Firebase options", users of your app may experience serious issues.
  The exception to this is the `authDomain`, which can be updated following
  [Best practices for using signInWithRedirect](https://firebase.google.com/docs/auth/web/redirect-best-practices#update-authdomain).

- If you enabled Google Analytics in your Firebase project, your config
  object contains the field `measurementId`. Learn more about this field in the
  [Analytics getting started page](https://firebase.google.com/docs/analytics/get-started?platform=web#add-sdk).

- If you enable Google Analytics or Realtime Database *after* you create your
  Firebase Web App, make sure that the Firebase config object that you use in
  your app is updated with the associated config values (`measurementId` and
  `databaseURL`, respectively). You can [obtain your Firebase config
  object](https://support.google.com/firebase/answer/7015592) at
  any time.

> [!NOTE]
> **Note:** The Firebase config object contains unique, but non-secret identifiers for your Firebase project and app.   
> Visit [Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects) to learn more about this config object.

Here's the format of a config object with all services enabled (these values
are automatically populated):

```javascript
var firebaseConfig = {
  apiKey: "API_KEY",
  authDomain: "PROJECT_ID.firebaseapp.com",
  // The value of `databaseURL` depends on the https://firebase.google.com/docs/database/locations
  databaseURL: "https://DATABASE_NAME.firebaseio.com",
  projectId: "PROJECT_ID",
  // The value of `storageBucket` depends on when you provisioned your default bucket (https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-storage-bucket)
  storageBucket: "`PROJECT_ID.firebasestorage.app`",
  messagingSenderId: "SENDER_ID",
  appId: "APP_ID",
  // For Firebase JavaScript SDK v7.20.0 and later, `measurementId` is an optional field
  measurementId: "G-MEASUREMENT_ID",
};
```

## Available libraries

### Available Firebase JS SDKs (from the CDN)

#### Modular libraries

Learn how to use these import statements in the guide for
[alternative ways to add the JS SDK](https://firebase.google.com/docs/web/alt-setup#from-the-cdn).

| **Firebase product** | **Library reference** |
|---|---|
| Firebase core (required) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-app.js"` |
| [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started) ^1^ | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-ai.js"` |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=web) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-analytics.js"` |
| [App Check](https://firebase.google.com/docs/app-check) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-app-check.js"` |
| [Authentication](https://firebase.google.com/docs/auth/web/start) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-auth.js"` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-firestore.js"` |
| [Cloud Functions for Firebase Client SDK](https://firebase.google.com/docs/functions/callable#call_the_function) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-functions.js"` |
| [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-installations.js"` |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/js/client) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-messaging.js"` For an optimal experience using Cloud Messaging, also add the Firebase SDK for Analytics. |
| [Cloud Storage](https://firebase.google.com/docs/storage/web/start) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-storage.js"` |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-web) *(**beta** release)* | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-performance.js"` We also provide a standalone, lightweight Performance Monitoring SDK (via the CDN). Visit the [FAQ](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=web#faq-standalone-namespaced-v8-sdk) to learn more. |
| [Realtime Database](https://firebase.google.com/docs/database/web/start) | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-database.js"` |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=web) *(**beta** release)* | `import { } from "https://www.gstatic.com/firebasejs/12.10.0/firebase-remote-config.js"` For an optimal experience using Remote Config, also add the Firebase SDK for Analytics. |

^**1** *Firebase AI Logic was formerly called
"Vertex AI in Firebase" with the import
`../firebase-vertexai.js`.*^

#### Namespaced libraries

| **Firebase product** | **Library reference** |
|---|---|
| Firebase core (required) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-app-compat.js"></script> ``` |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=web) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-analytics-compat.js"></script> ``` |
| [App Check](https://firebase.google.com/docs/app-check) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-app-check-compat.js"></script> ``` |
| [Authentication](https://firebase.google.com/docs/auth/web/start) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-auth-compat.js"></script> ``` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-firestore-compat.js"></script> ``` |
| [Cloud Functions for Firebase Client SDK](https://firebase.google.com/docs/functions/callable#call_the_function) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-functions-compat.js"></script> ``` |
| [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-installations-compat.js"></script> ``` |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/js/client) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-messaging-compat.js"></script> ``` For an optimal experience using Cloud Messaging, also add the Firebase SDK for Analytics. |
| [Cloud Storage](https://firebase.google.com/docs/storage/web/start) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-storage-compat.js"></script> ``` |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-web) *(**beta** release)* | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-performance-compat.js"></script> ``` We also provide a standalone, lightweight Performance Monitoring SDK (via the CDN). Visit the [FAQ](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=web#faq-standalone-namespaced-v8-sdk) to learn more. |
| [Realtime Database](https://firebase.google.com/docs/database/web/start) | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-database-compat.js"></script> ``` |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=web) *(**beta** release)* | ``` <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-remote-config-compat.js"></script> ``` For an optimal experience using Remote Config, also add the Firebase SDK for Analytics. |

### Available Firebase JS SDKs (using bundler with modules)

#### Modular libraries

| **Firebase product** | **Library reference** |
|---|---|
| Firebase core *(required)* | `import {} from "firebase/app";` |
| [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started) ^1^ | `import {} from "firebase/ai";` |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=web) | `import {} from "firebase/analytics";` |
| [App Check](https://firebase.google.com/docs/app-check) | `import {} from "firebase/app-check";` |
| [Authentication](https://firebase.google.com/docs/auth/web/start) | `import {} from "firebase/auth";` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | `import {} from "firebase/firestore";` |
| [Cloud Functions for Firebase Client SDK](https://firebase.google.com/docs/functions/callable#call_the_function) | `import {} from "firebase/functions";` |
| [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | `import {} from "firebase/installations";` |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/js/client) | `import {} from "firebase/messaging";` For an optimal experience using Cloud Messaging, also add the Firebase SDK for Analytics. |
| [Cloud Storage](https://firebase.google.com/docs/storage/web/start) | `import {} from "firebase/storage";` |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-web) *(**beta** release)* | `import {} from "firebase/performance";` |
| [Realtime Database](https://firebase.google.com/docs/database/web/start) | `import {} from "firebase/database";` |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=web) | `import {} from "firebase/remote-config";` For an optimal experience using Remote Config, also add the Firebase SDK for Analytics. |

^**1** *Firebase AI Logic was formerly called
"Vertex AI in Firebase" with the package
`firebase/vertexai`.*^

#### Namespaced libraries

| **Firebase product** | **Library reference** |
|---|---|
| Firebase core *(required)* | `import firebase from "firebase/compat/app";` |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=web) | `import "firebase/compat/analytics";` |
| [App Check](https://firebase.google.com/docs/app-check) | `import "firebase/compat/app-check";` |
| [Authentication](https://firebase.google.com/docs/auth/web/start) | `import "firebase/compat/auth";` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | `import "firebase/compat/firestore";` |
| [Cloud Functions for Firebase Client SDK](https://firebase.google.com/docs/functions/callable#call_the_function) | `import "firebase/compat/functions";` |
| [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | `import "firebase/compat/installations";` |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/js/client) | `import "firebase/compat/messaging";` For an optimal experience using Cloud Messaging, also add the Firebase SDK for Analytics. |
| [Cloud Storage](https://firebase.google.com/docs/storage/web/start) | `import "firebase/compat/storage";` |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-web) *(**beta** release)* | `import "firebase/compat/performance";` |
| [Realtime Database](https://firebase.google.com/docs/database/web/start) | `import "firebase/compat/database";` |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=web) *(**beta** release)* | `import "firebase/compat/remote-config";` For an optimal experience using Remote Config, also add the Firebase SDK for Analytics. |

### Available Firebase JS SDKs (from reserved Hosting URLs)

> [!NOTE]
> Reserved Hosting URLs are available only with version 8 and earlier. You cannot use version 9 or later with Hosting URLs.

| **Firebase product** | **Library reference (reserved URL)** |
|---|---|
| Firebase core (required) | ``` <script src="/__/firebase/8.10.1/firebase-app.js"></script> ``` |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=web) | ``` <script src="/__/firebase/8.10.1/firebase-analytics.js"></script> ``` |
| [App Check](https://firebase.google.com/docs/app-check) | ``` <script src="/__/firebase/8.10.1/firebase-app-check.js"></script> ``` |
| [Authentication](https://firebase.google.com/docs/auth/web/start) | ``` <script src="/__/firebase/8.10.1/firebase-auth.js"></script> ``` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | ``` <script src="/__/firebase/8.10.1/firebase-firestore.js"></script> ``` |
| [Cloud Functions for Firebase Client SDK](https://firebase.google.com/docs/functions/callable#call_the_function) | ``` <script src="/__/firebase/8.10.1/firebase-functions.js"></script> ``` |
| [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | ``` <script src="/__/firebase/8.10.1/firebase-installations.js"></script> ``` |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/js/client) | ``` <script src="/__/firebase/8.10.1/firebase-messaging.js"></script> ``` For an optimal experience using Cloud Messaging, also add the Firebase SDK for Analytics. |
| [Cloud Storage](https://firebase.google.com/docs/storage/web/start) | ``` <script src="/__/firebase/8.10.1/firebase-storage.js"></script> ``` |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-web) *(**beta** release)* | ``` <script src="/__/firebase/8.10.1/firebase-performance.js"></script> ``` |
| [Realtime Database](https://firebase.google.com/docs/database/web/start) | ``` <script src="/__/firebase/8.10.1/firebase-database.js"></script> ``` |
| [Remote Config](https://firebase.google.com/docs/remote-config/use-config-web) *(**beta** release)* | ``` <script src="/__/firebase/8.10.1/firebase-remote-config.js"></script> ``` For an optimal experience using Remote Config, also add the Firebase SDK for Analytics. |
| Firebase JavaScript SDK (entire SDK) | ``` <script src="/__/firebase/8.10.1/firebase.js"></script> ``` |

## Additional setup options

### Delay loading of Firebase SDKs (from CDN)

You can delay the inclusion of the Firebase SDKs until the entire page has
loaded. If you are using modular API CDN scripts with `<script type="module">`,
this is the default behavior. If you are using namespaced CDN scripts as a
module, complete these steps to defer loading:

1. Add a `defer` flag to each `script` tag for the Firebase SDKs, then defer
   the initialization of Firebase using a second script, for example:

       <script defer src="https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js"></script>

       <script defer src="https://www.gstatic.com/firebasejs/8.10.1/firebase-auth.js"></script>
       <script defer src="https://www.gstatic.com/firebasejs/8.10.1/firebase-firestore.js"></script>

       // ...

       <script defer src="./init-firebase.js"></script>

2. Create an `init-firebase.js` file, then include the following in the file:

   ```javascript
   // TODO: Replace the following with your app's https://firebase.google.com/docs/web/learn-more#config-object
   var firebaseConfig = {
     // ...
   };

   // Initialize Firebase
   firebase.initializeApp(firebaseConfig);
   ```

### Use multiple Firebase projects in a single app

In most cases, you only have to initialize Firebase in a single, default app.
You can access Firebase from that app in two equivalent ways:

### Web

```javascript
import { initializeApp } from "firebase/app";
import { getStorage } from "firebase/storage";
import { getFirestore } from "firebase/firestore";

// Initialize Firebase with a "default" Firebase project
const defaultProject = initializeApp(firebaseConfig);

console.log(defaultProject.name);  // "[DEFAULT]"

// Option 1: Access Firebase services via the defaultProject variable
let defaultStorage = getStorage(defaultProject);
let defaultFirestore = getFirestore(defaultProject);

// Option 2: Access Firebase services using shorthand notation
defaultStorage = getStorage();
defaultFirestore = getFirestore();
```

### Web

```javascript
// Initialize Firebase with a "default" Firebase project
const defaultProject = firebase.initializeApp(firebaseConfig);

console.log(defaultProject.name);  // "[DEFAULT]"

// Option 1: Access Firebase services via the defaultProject variable
let defaultStorage = defaultProject.storage();
let defaultFirestore = defaultProject.firestore();

// Option 2: Access Firebase services using shorthand notation
defaultStorage = firebase.storage();
defaultFirestore = firebase.firestore();
```

Sometimes, though, you need to access multiple Firebase projects at the same
time. For example, you might want to read data from the database of one Firebase
project but store files in a different Firebase project. Or you might want to
authenticate one project while keeping a second project unauthenticated.

The Firebase JavaScript SDK allows you to initialize and use multiple Firebase projects
in a single app at the same time, with each project using its own Firebase
configuration information.

> [!NOTE]
> **Note:** Each Firebase project has its own Firebase configuration and authentication state.

### Web

```javascript
import { initializeApp, getApp } from "firebase/app";
import { getStorage } from "firebase/storage";
import { getFirestore } from "firebase/firestore";

// Initialize Firebase with a default Firebase project
initializeApp(firebaseConfig);

// Initialize Firebase with a second Firebase project
const otherProject = initializeApp(otherProjectFirebaseConfig, "other");

console.log(getApp().name);  // "[DEFAULT]"
console.log(otherProject.name);    // "otherProject"

// Use the shorthand notation to access the default project's Firebase services
const defaultStorage = getStorage();
const defaultFirestore = getFirestore();

// Use the otherProject variable to access the second project's Firebase services
const otherStorage = getStorage(otherProject);
const otherFirestore = getFirestore(otherProject);
```

### Web

```javascript
// Initialize Firebase with a default Firebase project
firebase.initializeApp(firebaseConfig);

// Initialize Firebase with a second Firebase project
const otherProject = firebase.initializeApp(otherProjectFirebaseConfig, "other");

console.log(firebase.app().name);  // "[DEFAULT]"
console.log(otherProject.name);    // "otherProject"

// Use the shorthand notation to access the default project's Firebase services
const defaultStorage = firebase.storage();
const defaultFirestore = firebase.firestore();

// Use the otherProject variable to access the second project's Firebase services
const otherStorage = otherProject.storage();
const otherFirestore = otherProject.firestore();
```

### Run a local web server for development

If you're building a web app, some parts of the Firebase JavaScript SDK require that
you serve your web app from a server rather than from the local filesystem. You
can use the [Firebase CLI](https://firebase.google.com/docs/cli) to run a local server.

If you already set up Firebase Hosting for your app, you might have already
completed several of the steps below.

To serve your web app, you'll use the Firebase CLI, a command-line tool.

1. Visit the Firebase CLI documentation to learn how to
   [install the CLI](https://firebase.google.com/docs/cli#install_the_firebase_cli) or
   [update to its latest version](https://firebase.google.com/docs/cli#update-cli).

2. [Initialize your Firebase project.](https://firebase.google.com/docs/cli#initialize_a_firebase_project)
   Run the following command from the root of your local app directory:

   ```
   firebase init
   ```

   <br />

   **What does this initialization command do?**

   <br />

   - Links your local app directory with Firebase

   - Generates a [`firebase.json` file](https://firebase.google.com/docs/cli#the_firebasejson_file)
     (a required file for Firebase Hosting)

   - Prompts you to specify a public root directory which contains your public
     static files (HTML, CSS, JS, etc.)

     The default name for the directory that Firebase looks for is "public". You
     can also [set the public directory](https://firebase.google.com/docs/hosting/full-config#public) later
     by directly modifying your `firebase.json` file.

   <br />

   <br />

3. [Start the local server](https://firebase.google.com/docs/cli#test-locally) for development. Run the
   following command from the root of your local app directory:

   ```
   firebase serve
   ```

## Open source resources for Firebase JavaScript SDKs

Firebase supports open source development, and we encourage community
contributions and feedback.

### Firebase JavaScript SDKs

Most Firebase JavaScript SDKs are developed as open source libraries in our public
[Firebase GitHub repository](https://github.com/firebase/firebase-js-sdk).

### Quickstart samples

Firebase maintains a collection of quickstart samples for most Firebase APIs on
Web. Find these quickstarts in our public
[Firebase GitHub quickstart repository](https://github.com/firebase/quickstart-js).
You can use these quickstarts as example code for using Firebase SDKs.