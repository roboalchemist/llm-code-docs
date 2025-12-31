# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/DeviceCheckProvider.md.txt

# FirebaseAppCheck Framework Reference

# DeviceCheckProvider

    class DeviceCheckProvider : NSObject, https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider.html

Firebase App Check provider that verifies app integrity using the
[DeviceCheck](https://developer.apple.com/documentation/devicecheck) API.
This class is available on all platforms for select OS versions. See
<https://firebase.google.com/docs/ios/learn-more> for more details.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/DeviceCheckProvider#/c:objc(cs)FIRDeviceCheckProvider(im)init)

  `
  `  
  Unavailable  
  Undocumented
- `
  ``
  ``
  `

  ### [init(app:)](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/DeviceCheckProvider#/c:objc(cs)FIRDeviceCheckProvider(im)initWithApp:)

  `
  `  
  The default initializer.  

  #### Declaration

  Swift  

      init?(app: FIRApp)

  #### Parameters

  |-------------|---------------------------|
  | ` `*app*` ` | A `FirebaseApp` instance. |

  #### Return Value

  An instance of `DeviceCheckProvider` if the provided `FirebaseApp` instance contains all
  required parameters.
- `
  ``
  ``
  `

  ### [getToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/DeviceCheckProvider#/c:objc(cs)FIRDeviceCheckProvider(im)getTokenWithCompletion:)

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

  ### [getLimitedUseToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/DeviceCheckProvider#/c:objc(cs)FIRDeviceCheckProvider(im)getLimitedUseTokenWithCompletion:)

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