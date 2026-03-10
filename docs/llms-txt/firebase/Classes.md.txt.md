# Source: https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes.md.txt

# FirebaseAppCheck Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRAppAttestProvider](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppAttestProvider)


  ` Firebase App Check provider that verifies app integrity using the
  [DeviceCheck](https://developer.apple.com/documentation/devicecheck/dcappattestservice) API.
  This class is available on all platforms for select OS versions. See
  <https://firebase.google.com/docs/ios/learn-more> for more details.

  #### Declaration

  Objective-C


      @interface FIRAppAttestProvider : NSObject <https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProvider>

- `


  ### [FIRAppCheck](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheck)


  ` A class used to manage app check tokens for a given Firebase app.

  #### Declaration

  Objective-C


      @interface FIRAppCheck : NSObject

- `


  ### [FIRAppCheckDebugProvider](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckDebugProvider)


  ` A Firebase App Check provider that can exchange a debug token registered
  in the Firebase console for a Firebase App Check token. The debug provider
  is designed to enable testing applications on a simulator or test
  environment.

  NOTE: Do not use the debug provider in applications used by real users.

  WARNING: Keep the Firebase App Check debug token secret. If you
  accidentally share one (e.g. commit to a public source repo), remove it in
  the Firebase console ASAP.

  To use `AppCheckDebugProvider` on a local simulator:
  1. Configure `AppCheckDebugProviderFactory` before `FirebaseApp.configure()`: `AppCheck.setAppCheckProviderFactory(AppCheckDebugProviderFactory())` 2. Enable debug logging by adding the `-FIRDebugEnabled` launch argument to the app target. 3. Launch the app. A local debug token will be logged when Firebase is configured. For example: "\[Firebase/AppCheck\]\[I-FAA001001\] Firebase App Check Debug Token: '3BA09C8C-8A0D-4030-ACD5-B96D99DB73F9'". 4. Register the debug token in the Firebase console.

  Once the debug token is registered the debug provider will be able to provide a valid Firebase
  App Check token.

  To use `AppCheckDebugProvider` on a simulator on a build server:
  1. Create a new Firebase App Check debug token in the Firebase console
  2. Add the debug token to the secure storage of your build environment. E.g. see [Encrypted
     secrets](https://docs.github.com/en/actions/reference/encrypted-secrets) for GitHub Actions, etc.
  3. Configure `AppCheckDebugProviderFactory` before `FirebaseApp.configure()` `AppCheck.setAppCheckProviderFactory(AppCheckDebugProviderFactory())`
  4. Add an environment variable to the scheme with a name `FIRAAppCheckDebugToken` and value like `$(MY_APP_CHECK_DEBUG_TOKEN)`.
  5. Configure the build script to pass the debug token as the environment variable, e.g.: `xcodebuild test -scheme InstallationsExample -workspace InstallationsExample.xcworkspace \
     MY_APP_CHECK_DEBUG_TOKEN=$(MY_SECRET_ON_CI)`

  #### Declaration

  Objective-C


      @interface FIRAppCheckDebugProvider : NSObject <https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProvider>

- `


  ### [FIRAppCheckDebugProviderFactory](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes#/c:objc(cs)FIRAppCheckDebugProviderFactory)


  ` An implementation of `AppCheckProviderFactory` that creates a new instance of
  `AppCheckDebugProvider` when requested.

  #### Declaration

  Objective-C


      @interface FIRAppCheckDebugProviderFactory
          : NSObject <https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProviderFactory>

- `


  ### [FIRAppCheckToken](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken)


  ` An object representing a Firebase App Check token.

  #### Declaration

  Objective-C


      @interface FIRAppCheckToken : NSObject

- `


  ### [FIRDeviceCheckProvider](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRDeviceCheckProvider)


  ` Firebase App Check provider that verifies app integrity using the
  [DeviceCheck](https://developer.apple.com/documentation/devicecheck) API.
  This class is available on all platforms for select OS versions. See
  <https://firebase.google.com/docs/ios/learn-more> for more details.

  #### Declaration

  Objective-C


      @interface FIRDeviceCheckProvider : NSObject <https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProvider>

- `


  ### [FIRDeviceCheckProviderFactory](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes#/c:objc(cs)FIRDeviceCheckProviderFactory)


  ` An implementation of `AppCheckProviderFactory` that creates a new instance of
  `DeviceCheckProvider` for the specified `FirebaseApp` on request. Currently
  `DeviceCheckProviderFactory` is the default that will be used by Firebase App Check if no other
  provider is specified. See `AppCheck` class for more details.
  This class is available on all platforms for select OS versions. See
  <https://firebase.google.com/docs/ios/learn-more> for more details.

  #### Declaration

  Objective-C


      @interface FIRDeviceCheckProviderFactory : NSObject <https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProviderFactory>