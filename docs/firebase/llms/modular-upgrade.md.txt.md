# Source: https://firebase.google.com/docs/web/modular-upgrade.md.txt

# Upgrade from the namespaced API to the modular application

Apps using any namespaced Firebase web API, from the `compat` libraries
back through version 8 or earlier, should consider
migrating to the modular API using the instructions in this guide.

This guide assumes
that you are familiar with the namespaced API and that you will take advantage of a
module bundler such as [webpack](https://webpack.js.org/) or
[Rollup](https://rollupjs.org/) for upgrading and
ongoing modular app development.

Using a module bundler in your development environment is strongly
recommended. If you don't use one, you won't be able to take advantage of
the modular API's main benefits in reduced app size. You'll need
[npm](https://www.npmjs.com/) or
[yarn](https://yarnpkg.com/) to install the SDK.

The upgrade steps in this guide will be based around an imaginary web app that
uses the Authentication and Cloud Firestore SDKs. By working through the examples, you
can master the concepts and practical steps required to upgrade all supported
Firebase web SDKs.

## About the namespaced (`compat`) libraries

There are two types of libraries available for the Firebase web SDK:

- **Modular** - a new API surface designed to facilitate tree-shaking (removal of unused code) to make your web app as small and fast as possible.
- **Namespaced (`compat`)** - a familiar API surface which is fully compatible with the earlier versions of the SDK, allowing you to upgrade without changing all of your Firebase code at once. Compat libraries have little to no size or performance advantages over their namespaced counterparts.

This guide assumes that you will take advantage of the compat
libraries to facilitate your upgrade. These libraries allow you to continue
using namespaced code alongside code refactored for the modular API. This means you
can compile and debug your app more easily as you work through the upgrade
process.

> [!CAUTION]
> Keep in mind: the compat libraries are a temporary solution that will be removed completely in a future major SDK version (such as version 10 or version 11). Your ultimate goal is to remove compat code and keep only the modular-style code in your app.

For apps with a very small exposure to the Firebase web SDK---for example,
an app that makes only a simple call to the Authentication APIs---it may be
practical to refactor older namespaced code without using the compat libraries.
If you are upgrading such an app, you can follow the instructions in this guide
for "the modular API" without using the compat libraries.

## About the upgrade process

Each step of the upgrade process is scoped so that you can finish editing the
source for your app and then compile and run it without breakage. In summary,
here's what you'll do to upgrade an app:

1. Add the modular libraries and the compat libraries to your app.
2. Update import statements in your code to compat.
3. Refactor code for a single product (for example, Authentication) to the modular style.
4. Optional: at this point, remove the Authentication compat library and compat code for Authentication in order to realize the app size benefit for Authentication before continuing.
5. Refactor functions for each product (for example, Cloud Firestore, FCM, etc.) to the modular style, compiling and testing until all areas are complete.
6. Update initialization code to the modular style.
7. Remove all remaining compat statements and compat code from your app.

## Get the latest version of the SDK

To get started, get the modular libraries and compat libraries using npm:

```
npm i firebase@12.10.0

# OR

yarn add firebase@12.10.0
```

## Update imports to compat

In order to keep your code functioning after updating your dependencies,
change your import statements to use the "compat"
version of each import. For example:

**Before: version 8 or earlier**

    import firebase from 'firebase/app';
    import 'firebase/auth';
    import 'firebase/firestore';

**After: compat**

    // compat packages are API compatible with namespaced code
    import firebase from 'firebase/compat/app';
    import 'firebase/compat/auth';
    import 'firebase/compat/firestore';

## Refactor to the modular style

While the namespaced APIs are based on a dot-chained namespace and service
pattern, the modular approach means that your code will be organized
principally around **functions** . In the modular API, the `firebase/app` package and
other packages do not return a comprehensive export that contains all the
methods from the package. Instead, the packages export individual functions.

In the modular API, services are passed as the first argument, and the function then
uses the details of the service to do the rest. Let's examine how this works in
two examples that refactor calls to the Authentication and Cloud Firestore APIs.

### Example 1: refactoring an Authentication function

**Before: compat**

The compat code is identical to the namespaced code, but the imports
have changed.

    import firebase from "firebase/compat/app";
    import "firebase/compat/auth";

    const auth = firebase.auth();
    auth.onAuthStateChanged(user => { 
      // Check for user status
    });

**After: modular**

The `getAuth` function takes `firebaseApp` as its first parameter.
The `onAuthStateChanged`
function is not chained from the `auth` instance as it would be
in the namespaced API; instead, it's a free
function which takes `auth` as its first parameter.

    import { getAuth, onAuthStateChanged } from "firebase/auth";

    const auth = getAuth(firebaseApp);
    onAuthStateChanged(auth, user => {
      // Check for user status
    });

### Update handling of Auth method `getRedirectResult`

> [!CAUTION]
> **Caution:** If your app uses the Auth method `getRedirectResult`, you must make the updates described in this section. Failure to refactor your code could result in unpredictable app behavior.

The modular API introduces a breaking change in `getRedirectResult`. When no redirect operation is called, the modular API returns `null` as opposed to the namespaced API, which returned a `UserCredential` with a `null` user.

**Before: compat**

    const result = await auth.getRedirectResult()
    if (result.user === null && result.credential === null) {
      return null;
    }
    return result;

**After: modular**

    const result = await getRedirectResult(auth);
    // Provider of the access token could be Facebook, Github, etc.
    if (result === null || provider.credentialFromResult(result) === null) {
      return null;
    }
    return result;

### Example 2: refactoring a Cloud Firestore function

**Before: compat**

    import "firebase/compat/firestore"

    const db = firebase.firestore();
    db.collection("cities").where("capital", "==", true)
        .get()
        .then((querySnapshot) => {
            querySnapshot.forEach((doc) => {
                // doc.data() is never undefined for query doc snapshots
                console.log(doc.id, " => ", doc.data());
            });
        })
        .catch((error) => {
            console.log("Error getting documents: ", error);
        });

**After: modular**

The `getFirestore` function takes `firebaseApp` as its first parameter, which
was returned from `initializeApp` in an earlier example. Note how the
code to form a query is very different in the modular API; there is no chaining, and
methods such as `query` or `where` are now exposed as free functions.

    import { getFirestore, collection, query, where, getDocs } from "firebase/firestore";

    const db = getFirestore(firebaseApp);

    const q = query(collection(db, "cities"), where("capital", "==", true));

    const querySnapshot = await getDocs(q);
    querySnapshot.forEach((doc) => {
      // doc.data() is never undefined for query doc snapshots
      console.log(doc.id, " => ", doc.data());
    });

### Update references to Firestore `DocumentSnapshot.exists`

> [!CAUTION]
> **Caution:** If your app uses the `DocumentSnapshot.exists` property, you must perform the update described in this section. Failure to refactor your code could result in unpredictable app behavior.

The modular API introduces a breaking change in which the property
`firestore.DocumentSnapshot.exists` has been changed to a *method*. The
functionality is essentially the same (testing whether a document exists)
but you must refactor your code to use the newer method as shown:

**Before:compat**

    if (snapshot.exists) {
      console.log("the document exists");
    }

**After: modular**

    if (snapshot.exists()) {
      console.log("the document exists");
    }

### Example 3: combining namespaced and modular code styles

Using the compat libraries during upgrade allows you to continue using namespaced
code alongside code refactored for the modular API. This means you can keep
existing namespaced code for Cloud Firestore while you refactor Authentication
or other Firebase SDK code to
the modular style, and still successfully compile your app with both code
styles. The same is true for namespaced and modular API code *within* a product such
as Cloud Firestore; new and old code styles can coexist, as long as you are
importing the compat packages:

    import firebase from 'firebase/compat/app';
    import 'firebase/compat/firestore';
    import { getDoc } from 'firebase/firestore'

    const docRef = firebase.firestore().doc();
    getDoc(docRef);

Keep in mind that, although your app will compile, you won't get the app size
benefits of the modular code until you fully remove the compat statements and
code from your app.

## Update initialization code

Update your app's initialization code to use modular syntax. It is
important to update this code *after* you have completed refactoring all the
code in your app; this is because `firebase.initializeApp()` initializes global
state for both the compat and modular APIs, whereas the modular
`initializeApp()` function initializes only the state for modular.

**Before: compat**

    import firebase from "firebase/compat/app"

    firebase.initializeApp({ /* config */ });

**After: modular**

    import { initializeApp } from "firebase/app"

    const firebaseApp = initializeApp({ /* config */ });

## Remove compat code

To realize the size benefits of the modular API, you should eventually
convert all invocations to the modular style shown above and remove all of the
`import "firebase/compat/*` statements from your code. When you are done, there
should be no more references to the `firebase.*` global namespace or any other
code in the namespaced API style.

## Using the compat library from the window

The modular API is optimized to work with modules rather than the browser's
`window` object. Previous versions of the library allowed the loading and
management of Firebase by using the `window.firebase` namespace. This is not
recommended going forward as it does not allow for unused code elimination.
However, the compat version of the JavaScript SDK does work with the `window`
for developers who prefer not to immediately begin the modular upgrade path.

    <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-firestore-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-auth-compat.js"></script>
    <script>
       const firebaseApp = firebase.initializeApp({ /* Firebase config */ });
       const db = firebaseApp.firestore();
       const auth = firebaseApp.auth();
    </script>

The compatibility library uses modular code under the hood and
provides it with the same API as the namespaced API; this means you can
refer to the [namespaced API reference](https://firebase.google.com/docs/reference/js/v8)
and namespaced code snippets for details. This method is not
recommended for long term use, but as a start to upgrade to the fully modular
library.

## Benefits and limitations of the modular SDK

The fully modularized SDK has these advantages over earlier versions:

- The modular SDK enables a dramatically reduced app size. It adopts the modern JavaScript Module format, allowing for "tree shaking" practices in which you import only the artifacts your app needs. Depending on your app, tree-shaking with the modular SDK can result in 80% less kilobytes than a comparable app built using the namespaced API.
- The modular SDK will continue to benefit from ongoing feature development, while the namespaced API will not.