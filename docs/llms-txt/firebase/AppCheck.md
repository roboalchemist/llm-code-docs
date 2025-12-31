# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck.md.txt

# FirebaseAppCheck Framework Reference

# AppCheck

    class AppCheck : NSObject

A class used to manage app check tokens for a given Firebase app.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck#/c:objc(cs)FIRAppCheck(im)init)

  `
  `  
  Unavailable  
  Undocumented
- `
  ``
  ``
  `

  ### [appCheck()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck#/c:objc(cs)FIRAppCheck(cm)appCheck)

  `
  `  
  Returns a default instance of `AppCheck`.  

  #### Declaration

  Swift  

      class func appCheck() -> Self

  #### Return Value

  An instance of `AppCheck` for `FirebaseApp.defaultApp()`.
  @throw Throws an exception if the default app is not configured yet or required `FirebaseApp`
  options are missing.
- `
  ``
  ``
  `

  ### [appCheck(app:)](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck#/c:objc(cs)FIRAppCheck(cm)appCheckWithApp:)

  `
  `  
  Returns an instance of `AppCheck` for an application.  

  #### Declaration

  Swift  

      class func appCheck(app firebaseApp: FIRApp) -> Self?

  #### Parameters

  |---------------------|------------------------------------------------|
  | ` `*firebaseApp*` ` | A configured `FirebaseApp` instance if exists. |

  #### Return Value

  An instance of `AppCheck` corresponding to the passed application.
  @throw Throws an exception if required `FirebaseApp` options are missing.
- `
  ``
  ``
  `

  ### [setAppCheckProviderFactory(_:)](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck#/c:objc(cs)FIRAppCheck(cm)setAppCheckProviderFactory:)

  `
  `  
  Sets the [AppCheckProviderFactory](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory.html) to use to generate
  [AppCheckDebugProvider](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckDebugProvider.html) objects.

  An instance of [DeviceCheckProviderFactory](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes.html#/c:objc(cs)FIRDeviceCheckProviderFactory) is used by default, but you can
  also use a custom [AppCheckProviderFactory](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory.html) implementation or an
  instance of [AppCheckDebugProviderFactory](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes.html#/c:objc(cs)FIRAppCheckDebugProviderFactory) to test your app on a simulator
  on a local machine or a build server.

  NOTE: Make sure to call this method before `FirebaseApp.configure()`. If
  this method is called after configuring Firebase, the changes will not take
  effect.  

  #### Declaration

  Swift  

      class func setAppCheckProviderFactory(_ factory: (any FIRAppCheckProviderFactory)?)

- `
  ``
  ``
  `

  ### [isTokenAutoRefreshEnabled](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck#/c:objc(cs)FIRAppCheck(py)isTokenAutoRefreshEnabled)

  `
  `  
  If this flag is disabled then Firebase app check will not periodically auto-refresh the app
  check token. The default value of the flag is equal to
  `FirebaseApp.dataCollectionDefaultEnabled`. To disable the flag by default set
  `FirebaseAppCheckTokenAutoRefreshEnabled` flag in the app Info.plist to `NO`. Once the flag is
  set explicitly, the value will be persisted and used as a default value on next app launches.  

  #### Declaration

  Swift  

      var isTokenAutoRefreshEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [token(forcingRefresh:)](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck#/c:objc(cs)FIRAppCheck(im)tokenForcingRefresh:completion:)

  `
  `  
  Requests Firebase app check token. This method should *only* be used if you need to authorize
  requests to a non-Firebase backend. Requests to Firebase backend are authorized automatically if
  configured.

  If your non-Firebase backend exposes sensitive or expensive endpoints that have low traffic
  volume, consider protecting it with [Replay
  Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection).
  In this case, use the `limitedUseToken(completion:)` instead to obtain a limited-use token.  

  #### Declaration

  Swift  

      func token(forcingRefresh: Bool) async throws -> FIRAppCheckToken

  #### Parameters

  |------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*forcingRefresh*` ` | If `YES`, a new Firebase app check token is requested and the token cache is ignored. If `NO`, the cached token is used if it exists and has not expired yet. In most cases, `NO` should be used. `YES` should only be used if the server explicitly returns an error, indicating a revoked token. |
  | ` `*handler*` `        | The completion handler. Includes the app check token if the request succeeds, or an error if the request fails.                                                                                                                                                                                    |

- `
  ``
  ``
  `

  ### [limitedUseToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheck#/c:objc(cs)FIRAppCheck(im)limitedUseTokenWithCompletion:)

  `
  `  
  Requests a limited-use Firebase App Check token. This method should be used only if you need to
  authorize requests to a non-Firebase backend.

  Returns limited-use tokens that are intended for use with your non-Firebase backend endpoints
  that are protected with [Replay
  Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection).
  This method does not affect the token generation behavior of the
  `tokenForcingRefresh()` method.  

  #### Declaration

  Swift  

      func limitedUseToken() async throws -> FIRAppCheckToken