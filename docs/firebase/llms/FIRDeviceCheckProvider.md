# Source: https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRDeviceCheckProvider.md.txt

# FirebaseAppCheck Framework Reference

# FIRDeviceCheckProvider


    @interface FIRDeviceCheckProvider : NSObject <https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProvider.html>

Firebase App Check provider that verifies app integrity using the
[DeviceCheck](https://developer.apple.com/documentation/devicecheck) API.
This class is available on all platforms for select OS versions. See
<https://firebase.google.com/docs/ios/learn-more> for more details.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRDeviceCheckProvider#/c:objc(cs)FIRDeviceCheckProvider(im)init)

  `
  `  
  Unavailable  
  Undocumented  

  #### Declaration

  Objective-C  

      - (instancetype)init NS_UNAVAILABLE;

- `
  ``
  ``
  `

  ### [-initWithApp:](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRDeviceCheckProvider#/c:objc(cs)FIRDeviceCheckProvider(im)initWithApp:)

  `
  `  
  The default initializer.  

  #### Declaration

  Objective-C  

      - (nullable instancetype)initWithApp:(nonnull FIRApp *)app;

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

  ### [-getTokenWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRDeviceCheckProvider#/c:objc(cs)FIRDeviceCheckProvider(im)getTokenWithCompletion:)

  `
  `  
  Returns a new Firebase App Check token.  

  #### Declaration

  Objective-C  

      - (void)getTokenWithCompletion:(nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken.html *_Nullable,
                                                       NSError *_Nullable))handler;

  #### Parameters

  |-----------------|----------------------------------------------------------------------------------------|
  | ` `*handler*` ` | The completion handler. Make sure to call the handler with either a token or an error. |

- `
  ``
  ``
  `

  ### [-getLimitedUseTokenWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRDeviceCheckProvider#/c:objc(cs)FIRDeviceCheckProvider(im)getLimitedUseTokenWithCompletion:)

  `
  `  
  Returns a new Firebase App Check token.
  When implementing this method for your custom provider, the token returned should be suitable
  for consumption in a limited-use scenario. If you do not implement this method, the
  getTokenWithCompletion will be invoked instead whenever a limited-use token is requested.  

  #### Declaration

  Objective-C  

      - (void)getLimitedUseTokenWithCompletion:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken.html *_Nullable, NSError *_Nullable))handler;

  #### Parameters

  |-----------------|----------------------------------------------------------------------------------------|
  | ` `*handler*` ` | The completion handler. Make sure to call the handler with either a token or an error. |