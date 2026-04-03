# Source: https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallable.md.txt

# FirebaseFunctions Framework Reference

# FIRHTTPSCallable


    @interface FIRHTTPSCallable : NSObject

A `HTTPSCallable` is a reference to a particular Callable HTTPS trigger in Cloud Functions.
- `
  ``
  ``
  `

  ### [timeoutInterval](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallable#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallable(py)timeoutInterval)

  `
  `  
  The timeout to use when calling the function. Defaults to 70 seconds.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSTimeInterval timeoutInterval;

- `
  ``
  ``
  `

  ### [-callWithObject:completion:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallable#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallable(im)callWithObject:completion:)

  `
  `  
  Executes this Callable HTTPS trigger asynchronously.
  The data passed into the trigger can be any of the following types:
  - `nil` or `NSNull`
  - `String`
  - `NSNumber`, or any Swift numeric type bridgeable to `NSNumber`
  - `[Any]`, where the contained objects are also one of these types.
  - `[String: Any]` where the values are also one of these types.

  The request to the Cloud Functions backend made by this method automatically includes a
  Firebase Installations ID token to identify the app instance. If a user is logged in with
  Firebase Auth, an auth ID token for the user is also automatically included.
  Firebase Cloud Messaging sends data to the Firebase backend periodically to collect information
  regarding the app instance. To stop this, see `Messaging.deleteData()`. It
  resumes with a new FCM Token the next time you call this method.
  \\param data Parameters to pass to the trigger.

  \\param completion The block to call when the HTTPS request has completed.  

  #### Declaration

  Objective-C  

      - (void)callWithObject:(id _Nullable)data
                  completion:(void (^_Nonnull)(https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallableResult.html *_Nullable,
                                               NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-callWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallable#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallable(im)callWithCompletion:)

  `
  `  
  Executes this Callable HTTPS trigger asynchronously. This API should only be used from Objective-C.
  The request to the Cloud Functions backend made by this method automatically includes a
  Firebase Installations ID token to identify the app instance. If a user is logged in with
  Firebase Auth, an auth ID token for the user is also automatically included.
  Firebase Cloud Messaging sends data to the Firebase backend periodically to collect information
  regarding the app instance. To stop this, see `Messaging.deleteData()`. It
  resumes with a new FCM Token the next time you call this method.
  \\param completion The block to call when the HTTPS request has completed.  

  #### Declaration

  Objective-C  

      - (void)callWithCompletion:(void (^_Nonnull)(https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallableResult.html *_Nullable,
                                                   NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallable#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallable(im)init)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init SWIFT_UNAVAILABLE;

- `
  ``
  ``
  `

  ### [+new](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallable#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallable(cm)new)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)new SWIFT_UNAVAILABLE_MSG("-init is unavailable");