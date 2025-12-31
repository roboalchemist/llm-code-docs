# Source: https://firebase.google.com/docs/app-check/android/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/web/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/unity/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/ios/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/cpp/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/android/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/web/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/unity/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/ios/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/custom-provider.md.txt

# Source: https://firebase.google.com/docs/app-check/cpp/custom-provider.md.txt

This page shows you how to enableApp Checkin a C++ app, using[your customApp Checkprovider](https://firebase.google.com/docs/app-check/custom-provider). When you enableApp Check, you help ensure that only your app can access your project's Firebase resources.

If you want to useApp Checkwith the default providers, see[EnableApp Checkwith default providers with C++](https://firebase.google.com/docs/app-check/cpp/default-providers).

## Before you begin

- [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup)if you haven't already done so.

- [Implement your customApp Checkprovider's server-side logic](https://firebase.google.com/docs/app-check/custom-provider).

## 1. Add theApp Checklibrary to your app

Include the App Check library in your set of dependencies, following[the setup instructions](https://firebase.google.com/docs/cpp/setup#add-sdks)for App Check.

## 2. Implement theApp Checkinterfaces

First, you need to create classes that implement the`AppCheckProvider`and`AppCheckProviderFactory`interfaces.

Your`AppCheckProvider`class must have a`GetToken()`method, which collects whatever information your customApp Checkprovider requires as proof of authenticity, and sends it to your token acquisition service in exchange for anApp Checktoken. TheApp CheckSDK handles token caching, so always get a new token in your implementation of`GetToken()`.  

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

Also, implement a`AppCheckProviderFactory`class that creates instances of your`AppCheckProvider`implementation:  

    class YourCustomAppCheckProviderFactory : public AppCheckProviderFactory {
      AppCheckProvider* CreateProvider(App* app) {
        // Create and return an AppCheckProvider object.
        return new YourCustomAppCheckProvider(app);
      }
    }

## 3. InitializeApp Check

Add the following initialization code to your app so that it runs before you use any other Firebase SDKs:  

    firebase::app_check::AppCheck::SetAppCheckProviderFactory(
        YourCustomAppCheckProviderFactory::GetInstance());

## Next steps

Once theApp Checklibrary is installed in your app, start distributing the updated app to your users.

The updated client app will begin sendingApp Checktokens along with every request it makes to Firebase, but Firebase products will not require the tokens to be valid until you enable enforcement in theApp Checksection of the Firebase console.

### Monitor metrics and enable enforcement

Before you enable enforcement, however, you should make sure that doing so won't disrupt your existing legitimate users. On the other hand, if you're seeing suspicious use of your app resources, you might want to enable enforcement sooner.

To help make this decision, you can look atApp Checkmetrics for the services you use:

- [MonitorApp Checkrequest metrics](https://firebase.google.com/docs/app-check/monitor-metrics)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [MonitorApp Checkrequest metrics forCloud Functions](https://firebase.google.com/docs/app-check/monitor-functions-metrics).

### EnableApp Checkenforcement

When you understand howApp Checkwill affect your users and you're ready to proceed, you can enableApp Checkenforcement:

- [EnableApp Checkenforcement](https://firebase.google.com/docs/app-check/enable-enforcement)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [EnableApp Checkenforcement forCloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).

### UseApp Checkin debug environments

If, after you have registered your app forApp Check, you want to run your app in an environment thatApp Checkwould normally not classify as valid, such as an emulator during development, or from a continuous integration (CI) environment, you can create a debug build of your app that uses theApp Checkdebug provider instead of a real attestation provider.

See[UseApp Checkwith the debug provider with C++](https://firebase.google.com/docs/app-check/cpp/debug-provider).