# Source: https://firebase.google.com/docs/app-check/cpp/custom-provider.md.txt

<br />

This page shows you how to enable App Check in a C++ app, using [your
custom App Check provider](https://firebase.google.com/docs/app-check/custom-provider). When you enable
App Check, you help ensure that only your app can access your project's
Firebase resources.

If you want to use App Check with the default providers, see
[Enable App Check with default providers with C++](https://firebase.google.com/docs/app-check/cpp/default-providers).

## Before you begin

- [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup) if you haven't
  already done so.

- [Implement your custom App Check provider's server-side logic](https://firebase.google.com/docs/app-check/custom-provider).

## 1. Add the App Check library to your app

Include the App Check library in your set of dependencies, following
[the setup instructions](https://firebase.google.com/docs/cpp/setup#add-sdks) for App Check.

## 2. Implement the App Check interfaces

First, you need to create classes that implement the `AppCheckProvider` and
`AppCheckProviderFactory` interfaces.

Your `AppCheckProvider` class must have a `GetToken()` method, which collects
whatever information your custom App Check provider requires as proof of
authenticity, and sends it to your token acquisition service in exchange for an
App Check token. The App Check SDK handles token caching, so always get
a new token in your implementation of `GetToken()`.

    class YourCustomAppCheckProvider : public AppCheckProvider {
      void GetToken(std::function<void(AppCheckToken, int, const std::string&)>
          completion_callback) {
        // Logic to exchange proof of authenticity for an App Check token and
        //   expiration time.
        // ...

        // Create AppCheckToken object.
        AppCheckToken appCheckToken;
        appCheckToken.token = token;
        appCheckToken.expire_time_millis = expireTime;

        completion_callback(appCheckToken, 0, "");

        // Or, if needing to return an error
        //completion_callback({}, error_code, "Error description");
      }
    };

Also, implement a `AppCheckProviderFactory` class that creates instances of your
`AppCheckProvider` implementation:

    class YourCustomAppCheckProviderFactory : public AppCheckProviderFactory {
      AppCheckProvider* CreateProvider(App* app) {
        // Create and return an AppCheckProvider object.
        return new YourCustomAppCheckProvider(app);
      }
    }

## 3. Initialize App Check

Add the following initialization code to your app so that it runs before you use
any other Firebase SDKs:

    firebase::app_check::AppCheck::SetAppCheckProviderFactory(
        YourCustomAppCheckProviderFactory::GetInstance());

## Next steps

Once the App Check library is installed in your app, start distributing the
updated app to your users.

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
such as an emulator during development, or from a continuous integration (CI)
environment, you can create a debug build of your app that uses the
App Check debug provider instead of a real attestation provider.

See [Use App Check with the debug provider with C++](https://firebase.google.com/docs/app-check/cpp/debug-provider).