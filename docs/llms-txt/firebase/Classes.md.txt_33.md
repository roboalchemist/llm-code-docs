# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes.md.txt

# FirebaseAppCheck Framework Reference

# Classes

The following classes are available globally.
- `


  ### [AppAttestProvider](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppAttestProvider)


  ` Firebase App Check provider that verifies app integrity using the
  [DeviceCheck](https://developer.apple.com/documentation/devicecheck/dcappattestservice) API.
  This class is available on all platforms for select OS versions. See
  <https://firebase.google.com/docs/ios/learn-more> for more details.

  #### Declaration

  Swift

      class AppAttestProvider : NSObject, https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider

- `


  ### [AppCheck](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck)


  ` A class used to manage app check tokens for a given Firebase app.

  #### Declaration

  Swift

      class AppCheck : NSObject

- `


  ### [AppCheckDebugProvider](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider)


  ` A Firebase App Check provider that can exchange a debug token registered
  in the Firebase console for a Firebase App Check token. The debug provider
  is designed to enable testing applications on a simulator or test
  environment.

  NOTE: Do not use the debug provider in applications used by real users.

  WARNING: Keep the Firebase App Check debug token secret. If you
  accidentally share one (e.g. commit to a public source repo), remove it in
  the Firebase console ASAP.

  To use `AppCheckDebugProvider` on a local simulator:
  1. Configure `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes#/c:objc(cs)FIRAppCheckDebugProviderFactory` before `FirebaseApp.configure()`: `AppCheck.setAppCheckProviderFactory(AppCheckDebugProviderFactory())` 2. Enable debug logging by adding the `-FIRDebugEnabled` launch argument to the app target. 3. Launch the app. A local debug token will be logged when Firebase is configured. For example: "\[Firebase/AppCheck\]\[I-FAA001001\] Firebase App Check Debug Token: '3BA09C8C-8A0D-4030-ACD5-B96D99DB73F9'". 4. Register the debug token in the Firebase console.

  Once the debug token is registered the debug provider will be able to provide a valid Firebase
  App Check token.

  To use `AppCheckDebugProvider` on a simulator on a build server:
  1. Create a new Firebase App Check debug token in the Firebase console
  2. Add the debug token to the secure storage of your build environment. E.g. see [Encrypted
     secrets](https://docs.github.com/en/actions/reference/encrypted-secrets) for GitHub Actions, etc.
  3. Configure `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes#/c:objc(cs)FIRAppCheckDebugProviderFactory` before `FirebaseApp.configure()` `AppCheck.setAppCheckProviderFactory(AppCheckDebugProviderFactory())`
  4. Add an environment variable to the scheme with a name `FIRAAppCheckDebugToken` and value like `$(MY_APP_CHECK_DEBUG_TOKEN)`.
  5. Configure the build script to pass the debug token as the environment variable, e.g.: `xcodebuild test -scheme InstallationsExample -workspace InstallationsExample.xcworkspace \
     MY_APP_CHECK_DEBUG_TOKEN=$(MY_SECRET_ON_CI)`

  #### Declaration

  Swift

      class AppCheckDebugProvider : NSObject, https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider

- `


  ### [AppCheckDebugProviderFactory](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes#/c:objc(cs)FIRAppCheckDebugProviderFactory)


  ` An implementation of `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory` that creates a new instance of
  `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider` when requested.

  #### Declaration

  Swift

      class AppCheckDebugProviderFactory : NSObject, https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory

- `


  ### [AppCheckToken](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckToken)


  ` An object representing a Firebase App Check token.

  #### Declaration

  Swift

      class AppCheckToken : NSObject

- `


  ### [DeviceCheckProvider](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/DeviceCheckProvider)


  ` Firebase App Check provider that verifies app integrity using the
  [DeviceCheck](https://developer.apple.com/documentation/devicecheck) API.
  This class is available on all platforms for select OS versions. See
  <https://firebase.google.com/docs/ios/learn-more> for more details.

  #### Declaration

  Swift

      class DeviceCheckProvider : NSObject, https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider

- `


  ### [DeviceCheckProviderFactory](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes#/c:objc(cs)FIRDeviceCheckProviderFactory)


  ` An implementation of `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory` that creates a new instance of
  `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/DeviceCheckProvider` for the specified `FirebaseApp` on request. Currently
  `DeviceCheckProviderFactory` is the default that will be used by Firebase App Check if no other
  provider is specified. See `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck` class for more details.
  This class is available on all platforms for select OS versions. See
  <https://firebase.google.com/docs/ios/learn-more> for more details.

  #### Declaration

  Swift

      class DeviceCheckProviderFactory : NSObject, https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory