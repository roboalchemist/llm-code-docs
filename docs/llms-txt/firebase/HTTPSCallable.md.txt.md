# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable.md.txt

# FirebaseFunctions Framework Reference

# HTTPSCallable

    @objc(FIRHTTPSCallable)
    public final class HTTPSCallable : NSObject, Sendable

A `HTTPSCallable` is a reference to a particular Callable HTTPS trigger in Cloud Functions.
[## Public Properties](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable#/Public-Properties)

- `


  ### [timeoutInterval](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallable(py)timeoutInterval)


  ` The timeout to use when calling the function. Defaults to 70 seconds.

  #### Declaration

  Swift

      @objc
      public var timeoutInterval: TimeInterval { get set }

- `


  ### [call(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable#/s:17FirebaseFunctions13HTTPSCallableC4call_10completionyypSgn_yAA0C6ResultCSg_s5Error_pSgtScMYcctF)


  ` Executes this Callable HTTPS trigger asynchronously.

  The data passed into the trigger can be any of the following types:
  - `nil` or `NSNull`
  - `String`
  - `NSNumber`, or any Swift numeric type bridgeable to `NSNumber`
  - `[Any]`, where the contained objects are also one of these types.
  - `[String: Any]` where the values are also one of these types.

  The request to the Cloud Functions backend made by this method automatically includes a
  Firebase Installations ID token to identify the app instance. If a user is logged in with
  Firebase Auth, an auth ID token for the user is also automatically included.

  Firebase Cloud Messaging sends data to the Firebase backend periodically to collect
  information
  regarding the app instance. To stop this, see `Messaging.deleteData()`. It
  resumes with a new FCM Token the next time you call this method.

  #### Declaration

  Swift

      @nonobjc
      public func call(_ data: sending Any? = nil,
                       completion: @escaping @MainActor (https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableResult.html?,
                                                         Error?)
                         -> Void)

  #### Parameters

  |---|---|
  | ` data ` | Parameters to pass to the trigger. |
  | ` completion ` | The block to call when the HTTPS request has completed. |

- `


  ### [__call(completion:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallable(im)callWithCompletion:)


  ` Executes this Callable HTTPS trigger asynchronously. This API should only be used from
  Objective-C.

  The request to the Cloud Functions backend made by this method automatically includes a
  Firebase Installations ID token to identify the app instance. If a user is logged in with
  Firebase Auth, an auth ID token for the user is also automatically included.

  Firebase Cloud Messaging sends data to the Firebase backend periodically to collect
  information
  regarding the app instance. To stop this, see `Messaging.deleteData()`. It
  resumes with a new FCM Token the next time you call this method.

  #### Declaration

  Swift

      @objc(callWithCompletion:)
      public func __call(completion: @escaping @MainActor (https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableResult.html?,
                                                           Error?) -> Void)

  #### Parameters

  |---|---|
  | ` completion ` | The block to call when the HTTPS request has completed. |

- `


  ### [call(_:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable#/s:17FirebaseFunctions13HTTPSCallableC4callyAA0C6ResultCypSgYaKF)


  ` Executes this Callable HTTPS trigger asynchronously.

  The request to the Cloud Functions backend made by this method automatically includes a
  FCM token to identify the app instance. If a user is logged in with Firebase
  Auth, an auth ID token for the user is also automatically included.

  Firebase Cloud Messaging sends data to the Firebase backend periodically to collect
  information
  regarding the app instance. To stop this, see `Messaging.deleteData()`. It
  resumes with a new FCM Token the next time you call this method.
  Throws
  An error if the Cloud Functions invocation failed.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      public func call(_ data: Any? = nil) async throws -> sending sending https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableResult.html

  #### Parameters

  |---|---|
  | ` data ` | Parameters to pass to the trigger. |

  #### Return Value

  The result of the call.