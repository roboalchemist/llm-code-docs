# Source: https://firebase.google.com/docs/auth/web/custom-dependencies.md.txt

The modular design of the Firebase JS SDK gives you much greater control over how your app is built. This flexibility allows you to tailor your dependencies for your platform and optimize your bundle size by stripping away features that you don't need.

There are two ways to initialize the Auth library: the`getAuth()`function and the`initializeAuth()`function. The first,`getAuth()`, provides everything your app needs in order to take advantage of all the features the Auth library has to offer. The downside is that it pulls in a lot of code that is potentially unused by your app. It also may pull in code that is simply unsupported on the platform you're targeting, leading to errors. To avoid these problems, you can use`initializeAuth()`, which takes a map of dependencies. The`getAuth()`function simply calls`initializeAuth()`with all of the dependencies specified. To illustrate, here is the equivalent to`getAuth()`on browser environments:  

    import {initializeAuth, browserLocalPersistence, browserPopupRedirectResolver, browserSessionPersistence, indexedDBLocalPersistence} from "firebase/auth";
    import {initializeApp} from "firebase/app";

    const app = initializeApp({/** Your app config */});
    const auth = initializeAuth(app, {
      persistence: [indexedDBLocalPersistence, browserLocalPersistence, browserSessionPersistence],
      popupRedirectResolver: browserPopupRedirectResolver,
    });

## Tailoring your dependencies

Not all apps use the`signInWithPopup`or`signInWithRedirect`family of functions. Many apps won't need the flexibility that`indexedDB`provides, or won't need the ability to support both`indexedDB`and`localStorage`should one not be available. In these cases, the default`getAuth()`includes a lot of unused code that increases bundle sizes for no reason. Instead, these apps can tailor their dependencies. For example, if your app only uses email link authentication and localStorage is sufficient (because you're not using web or service worker scripts), you can strip a lot of code bloat by initializing Auth like this:  

    import {initializeAuth, browserLocalPersistence} from "firebase/auth";
    import {initializeApp} from "firebase/app";

    const app = initializeApp({/** Your app config */});
    const auth = initializeAuth(app, {
      persistence: browserLocalPersistence,
      // No popupRedirectResolver defined
    });

With this code, you've removed three large dependencies that your app does not need, significantly cutting down the amount of bandwidth your users use whenever they visit your site.

## Platform-specific considerations

In many cases, you need to manually define the Auth dependencies in order to avoid errors on initialization. The`getAuth()`function assumes a specific platform. For the default entry point, that is a browser environment and for the Cordova entry point, that's a Cordova environment. But sometimes the needs of your particular application clash with these assumptions. For web and service worker scripts, for example, the default`getAuth()`implementation pulls in code that reads from the`window`object, which will cause errors. In those cases, it is necessary to tailor your dependencies. The following code is appropriate to initialize the Auth library in a service worker context:  

    import {initializeAuth, indexedDBLocalPersistence} from "firebase/auth";
    import {initializeApp} from "firebase/app";

    const app = initializeApp({/** Your app config */});
    const auth = initializeAuth(app, {
      persistence: indexedDBLocalPersistence,
      // No popupRedirectResolver defined
    });

This code instructs Auth to initialize with`indexedDB`persistence (which is available in worker contexts) and omits the`popupRedirectResolver`dependency, which assumes a DOM context is available.

There are other reasons you might manually define dependencies on certain platforms. By defining the`popupRedirectResolver`field in Auth initialization, in some cases the library will perform additional work on initialization. On mobile browsers, the library will automatically open an iframe to your Auth domain preemptively. This is done to make the experience seamless for most users, but it can impact performance by loading additional code right when the app starts. This behavior can be avoided by utilizing`initializeAuth()`and manually passing the`browserPopupRedirectResolver`dependency to the functions that need it:  

    import {initializeAuth, browserLocalPersistence, browserPopupRedirectResolver, indexedDBLocalPersistence, signInWithRedirect, GoogleAuthProvider} from "firebase/auth";
    import {initializeApp} from "firebase/app";

    const app = initializeApp({/** Your app config */});
    const auth = initializeAuth(app, {
      persistence: [indexedDBLocalPersistence, browserLocalPersistence],
    });

    // Later
    signInWithRedirect(auth, new GoogleAuthProvider(), browserPopupRedirectResolver);

If we had provided`browserPopupRedirectResolver`in the dependencies to`initializeAuth()`, the third parameter in the call to`signInWithRedirect()`would not have been needed. But by moving that dependency to the call to`signInWithRedirect()`directly, the initial performance hit during initialization is removed. There are tradeoffs that come with moving the dependency, but the important part is that you are able to make decisions about those tradeoffs by manually initializing the library.

## When to use custom initialization

To recap, custom initialization gives you far greater control over your app's usage of the Auth SDK. The standard`getAuth()`function is good for getting started and serves most use cases. For most apps,`getAuth()`may be all you need. But there are many reasons why you may want (or need) to switch to manual dependency management:

- For apps where bundle size and load times are extremely important, custom Auth initialization can potentially cut down on many kilobytes of data. It can also cut down on*initial*load times by moving dependencies to time of use instead of time of initialization.
- For code that runs in non-DOM contexts (like web and service workers),`initializeAuth()`must be used to avoid errors.