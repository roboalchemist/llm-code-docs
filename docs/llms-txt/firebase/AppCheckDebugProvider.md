# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider.md.txt

# FirebaseAppCheck Framework Reference

# AppCheckDebugProvider

    class AppCheckDebugProvider : NSObject, https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider.html

A Firebase App Check provider that can exchange a debug token registered
in the Firebase console for a Firebase App Check token. The debug provider
is designed to enable testing applications on a simulator or test
environment.

NOTE: Do not use the debug provider in applications used by real users.

WARNING: Keep the Firebase App Check debug token secret. If you
accidentally share one (e.g. commit to a public source repo), remove it in
the Firebase console ASAP.

To use `AppCheckDebugProvider` on a local simulator:

1. Configure [AppCheckDebugProviderFactory](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes.html#/c:objc(cs)FIRAppCheckDebugProviderFactory) before `FirebaseApp.configure()`: `AppCheck.setAppCheckProviderFactory(AppCheckDebugProviderFactory())` 2. Enable debug logging by adding the `-FIRDebugEnabled` launch argument to the app target. 3. Launch the app. A local debug token will be logged when Firebase is configured. For example: "\[Firebase/AppCheck\]\[I-FAA001001\] Firebase App Check Debug Token: '3BA09C8C-8A0D-4030-ACD5-B96D99DB73F9'". 4. Register the debug token in the Firebase console.

Once the debug token is registered the debug provider will be able to provide a valid Firebase
App Check token.

To use `AppCheckDebugProvider` on a simulator on a build server:

1. Create a new Firebase App Check debug token in the Firebase console
2. Add the debug token to the secure storage of your build environment. E.g. see [Encrypted
   secrets](https://docs.github.com/en/actions/reference/encrypted-secrets) for GitHub Actions, etc.
3. Configure [AppCheckDebugProviderFactory](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes.html#/c:objc(cs)FIRAppCheckDebugProviderFactory) before `FirebaseApp.configure()` `AppCheck.setAppCheckProviderFactory(AppCheckDebugProviderFactory())`
4. Add an environment variable to the scheme with a name `FIRAAppCheckDebugToken` and value like `$(MY_APP_CHECK_DEBUG_TOKEN)`.
5. Configure the build script to pass the debug token as the environment variable, e.g.: `xcodebuild test -scheme InstallationsExample -workspace InstallationsExample.xcworkspace \
   MY_APP_CHECK_DEBUG_TOKEN=$(MY_SECRET_ON_CI)`
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider#/c:objc(cs)FIRAppCheckDebugProvider(im)init)

  `
  `  
  Unavailable  
  Undocumented
- `
  ``
  ``
  `

  ### [init(app:)](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider#/c:objc(cs)FIRAppCheckDebugProvider(im)initWithApp:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      init?(app: FIRApp)

- `
  ``
  ``
  `

  ### [localDebugToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider#/c:objc(cs)FIRAppCheckDebugProvider(im)localDebugToken)

  `
  `  
  Return the locally generated token.  

  #### Declaration

  Swift  

      func localDebugToken() -> String

- `
  ``
  ``
  `

  ### [currentDebugToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider#/c:objc(cs)FIRAppCheckDebugProvider(im)currentDebugToken)

  `
  `  
  Returns the currently used App Check debug token. The priority:
  - - `FIRAAppCheckDebugToken` env variable value
  - - A previously generated token, stored locally on the device
  - - A newly generated random token. The generated token will be stored
  - locally for future use
  - - returns: The currently used App Check debug token.  

  #### Declaration

  Swift  

      func currentDebugToken() -> String

- `
  ``
  ``
  `

  ### [getToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider#/c:objc(cs)FIRAppCheckDebugProvider(im)getTokenWithCompletion:)

  `
  `  
  Returns a new Firebase App Check token.  

  #### Declaration

  Swift  

      func getToken() async throws -> FIRAppCheckToken

  #### Parameters

  |-----------------|----------------------------------------------------------------------------------------|
  | ` `*handler*` ` | The completion handler. Make sure to call the handler with either a token or an error. |

- `
  ``
  ``
  `

  ### [getLimitedUseToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider#/c:objc(cs)FIRAppCheckDebugProvider(im)getLimitedUseTokenWithCompletion:)

  `
  `  
  Returns a new Firebase App Check token.
  When implementing this method for your custom provider, the token returned should be suitable
  for consumption in a limited-use scenario. If you do not implement this method, the
  getTokenWithCompletion will be invoked instead whenever a limited-use token is requested.  

  #### Declaration

  Swift  

      func getLimitedUseToken() async throws -> FIRAppCheckToken

  #### Parameters

  |-----------------|----------------------------------------------------------------------------------------|
  | ` `*handler*` ` | The completion handler. Make sure to call the handler with either a token or an error. |