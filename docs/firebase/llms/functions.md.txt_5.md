# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions.md.txt

# FirebaseFunctions Framework Reference

# Functions

    @objc(FIRFunctions)
    open class Functions : NSObject, @unchecked Sendable

`Functions` is the client for Cloud Functions for a Firebase project.
[## Public APIs](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/Public-APIs)

- `


  ### [emulatorOrigin](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/s:17FirebaseFunctions0B0C14emulatorOriginSSSgvp)


  ` The current emulator origin, or `nil` if it is not set.

  #### Declaration

  Swift

      open var emulatorOrigin: String? { get }

- `


  ### [functions()](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functions)


  ` Creates a Cloud Functions client using the default or returns a pre-existing instance if it
  already exists.

  #### Declaration

  Swift

      @objc(functions)
      open class func functions() -> Functions

  #### Return Value

  A shared Functions instance initialized with the default `FirebaseApp`.
- `


  ### [functions(app:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForApp:)


  ` Creates a Cloud Functions client with the given app, or returns a pre-existing
  instance if one already exists.

  #### Declaration

  Swift

      @objc(functionsForApp:)
      open class func functions(app: FirebaseApp) -> Functions

  #### Parameters

  |---|---|
  | ` app ` | The app for the Firebase project. |

  #### Return Value

  A shared Functions instance initialized with the specified `FirebaseApp`.
- `


  ### [functions(region:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForRegion:)


  ` Creates a Cloud Functions client with the default app and given region.

  #### Declaration

  Swift

      @objc(functionsForRegion:)
      open class func functions(region: String) -> Functions

  #### Parameters

  |---|---|
  | ` region ` | The region for the HTTP trigger, such as `us-central1`. |

  #### Return Value

  A shared Functions instance initialized with the default `FirebaseApp` and a
  custom region.
- `


  ### [functions(customDomain:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForCustomDomain:)


  ` Creates a Cloud Functions client with the given custom domain or returns a pre-existing
  instance if one already exists.

  #### Declaration

  Swift

      @objc(functionsForCustomDomain:)
      open class func functions(customDomain: String) -> Functions

  #### Parameters

  |---|---|
  | ` customDomain ` | A custom domain for the HTTP trigger, such as "<https://mydomain.com>". |

  #### Return Value

  A shared Functions instance initialized with the default `FirebaseApp` and a
  custom HTTP trigger domain.
- `


  ### [functions(app:region:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForApp:region:)


  ` Creates a Cloud Functions client with the given app and region, or returns a pre-existing
  instance if one already exists.

  #### Declaration

  Swift

      @objc(functionsForApp:region:)
      open class func functions(app: FirebaseApp,
                                region: String) -> Functions

  #### Parameters

  |---|---|
  | ` app ` | The app for the Firebase project. |
  | ` region ` | The region for the HTTP trigger, such as `us-central1`. |

  #### Return Value

  An instance of `Functions` with a custom app and region.
- `


  ### [functions(app:customDomain:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForApp:customDomain:)


  ` Creates a Cloud Functions client with the given app and custom domain, or returns a
  pre-existing
  instance if one already exists.

  #### Declaration

  Swift

      @objc(functionsForApp:customDomain:)
      open class func functions(app: FirebaseApp,
                                customDomain: String)
        -> Functions

  #### Parameters

  |---|---|
  | ` app ` | The app for the Firebase project. |
  | ` customDomain ` | A custom domain for the HTTP trigger, such as `https://mydomain.com`. |

  #### Return Value

  An instance of `Functions` with a custom app and HTTP trigger domain.
- `


  ### [httpsCallable(_:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)HTTPSCallableWithName:)


  ` Creates a reference to the Callable HTTPS trigger with the given name.

  #### Declaration

  Swift

      @objc(HTTPSCallableWithName:)
      open func httpsCallable(_ name: String) -> https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable.html

  #### Parameters

  |---|---|
  | ` name ` | The name of the Callable HTTPS trigger. |

  #### Return Value

  A reference to a Callable HTTPS trigger.
- `


  ### [httpsCallable(_:options:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)HTTPSCallableWithName:options:)


  ` Creates a reference to the Callable HTTPS trigger with the given name and configuration
  options.

  #### Declaration

  Swift

      @objc(HTTPSCallableWithName:options:)
      public func httpsCallable(_ name: String,
                                options: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableOptions.html)
        -> https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable.html

  #### Parameters

  |---|---|
  | ` name ` | The name of the Callable HTTPS trigger. |
  | ` options ` | The options with which to customize the Callable HTTPS trigger. |

  #### Return Value

  A reference to a Callable HTTPS trigger.
- `


  ### [httpsCallable(_:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)HTTPSCallableWithURL:)


  ` Creates a reference to the Callable HTTPS trigger with the given name.

  #### Declaration

  Swift

      @objc(HTTPSCallableWithURL:)
      open func httpsCallable(_ url: URL) -> https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable.html

  #### Parameters

  |---|---|
  | ` url ` | The URL of the Callable HTTPS trigger. |

  #### Return Value

  A reference to a Callable HTTPS trigger.
- `


  ### [httpsCallable(_:options:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)HTTPSCallableWithURL:options:)


  ` Creates a reference to the Callable HTTPS trigger with the given name and configuration
  options.

  #### Declaration

  Swift

      @objc(HTTPSCallableWithURL:options:)
      public func httpsCallable(_ url: URL,
                                options: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableOptions.html)
        -> https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable.html

  #### Parameters

  |---|---|
  | ` url ` | The URL of the Callable HTTPS trigger. |
  | ` options ` | The options with which to customize the Callable HTTPS trigger. |

  #### Return Value

  A reference to a Callable HTTPS trigger.
- `


  ### [httpsCallable(_:requestAs:responseAs:encoder:decoder:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/s:17FirebaseFunctions0B0C13httpsCallable_9requestAs08responseF07encoder7decoderAA0D0Vyxq_GSS_xmq_m0A11SharedSwift0A11DataEncoderCAL0aL7DecoderCtSERzSeR_r0_lF)


  ` Creates a reference to the Callable HTTPS trigger with the given name, the type of an
  `Encodable`
  request and the type of a `Decodable` response.

  #### Declaration

  Swift

      open func httpsCallable<Request: Encodable,
        Response: Decodable>(_ name: String,
                             requestAs: Request.Type = Request.self,
                             responseAs: Response.Type = Response.self,
                             encoder: FirebaseDataEncoder = FirebaseDataEncoder(
                             ),
                             decoder: FirebaseDataDecoder = FirebaseDataDecoder(
                             ))
        -> https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html<Request, Response>

  #### Parameters

  |---|---|
  | ` name ` | The name of the Callable HTTPS trigger |
  | ` requestAs ` | The type of the `Encodable` entity to use for requests to this `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` |
  | ` responseAs ` | The type of the `Decodable` entity to use for responses from this `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` |
  | ` encoder ` | The encoder instance to use to perform encoding. |
  | ` decoder ` | The decoder instance to use to perform decoding. |

  #### Return Value

  A reference to an HTTPS-callable Cloud Function that can be used to make Cloud
  Functions invocations.
- `


  ### [httpsCallable(_:options:requestAs:responseAs:encoder:decoder:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/s:17FirebaseFunctions0B0C13httpsCallable_7options9requestAs08responseG07encoder7decoderAA0D0Vyxq_GSS_AA20HTTPSCallableOptionsCxmq_m0A11SharedSwift0A11DataEncoderCAO0aO7DecoderCtSERzSeR_r0_lF)


  ` Creates a reference to the Callable HTTPS trigger with the given name, the type of an
  `Encodable`
  request and the type of a `Decodable` response.

  #### Declaration

  Swift

      open func httpsCallable<Request: Encodable,
        Response: Decodable>(_ name: String,
                             options: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableOptions.html,
                             requestAs: Request.Type = Request.self,
                             responseAs: Response.Type = Response.self,
                             encoder: FirebaseDataEncoder = FirebaseDataEncoder(
                             ),
                             decoder: FirebaseDataDecoder = FirebaseDataDecoder(
                             ))
        -> https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html<Request, Response>

  #### Parameters

  |---|---|
  | ` name ` | The name of the Callable HTTPS trigger |
  | ` options ` | The options with which to customize the Callable HTTPS trigger. |
  | ` requestAs ` | The type of the `Encodable` entity to use for requests to this `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` |
  | ` responseAs ` | The type of the `Decodable` entity to use for responses from this `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` |
  | ` encoder ` | The encoder instance to use to perform encoding. |
  | ` decoder ` | The decoder instance to use to perform decoding. |

  #### Return Value

  A reference to an HTTPS-callable Cloud Function that can be used to make Cloud
  Functions invocations.
- `


  ### [httpsCallable(_:requestAs:responseAs:encoder:decoder:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/s:17FirebaseFunctions0B0C13httpsCallable_9requestAs08responseF07encoder7decoderAA0D0Vyxq_G10Foundation3URLV_xmq_m0A11SharedSwift0A11DataEncoderCAO0aN7DecoderCtSERzSeR_r0_lF)


  ` Creates a reference to the Callable HTTPS trigger with the given name, the type of an
  `Encodable`
  request and the type of a `Decodable` response.

  #### Declaration

  Swift

      open func httpsCallable<Request: Encodable,
        Response: Decodable>(_ url: URL,
                             requestAs: Request.Type = Request.self,
                             responseAs: Response.Type = Response.self,
                             encoder: FirebaseDataEncoder = FirebaseDataEncoder(
                             ),
                             decoder: FirebaseDataDecoder = FirebaseDataDecoder(
                             ))
        -> https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html<Request, Response>

  #### Parameters

  |---|---|
  | ` url ` | The url of the Callable HTTPS trigger |
  | ` requestAs ` | The type of the `Encodable` entity to use for requests to this `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` |
  | ` responseAs ` | The type of the `Decodable` entity to use for responses from this `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` |
  | ` encoder ` | The encoder instance to use to perform encoding. |
  | ` decoder ` | The decoder instance to use to perform decoding. |

  #### Return Value

  A reference to an HTTPS-callable Cloud Function that can be used to make Cloud
  Functions invocations.
- `


  ### [httpsCallable(_:options:requestAs:responseAs:encoder:decoder:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/s:17FirebaseFunctions0B0C13httpsCallable_7options9requestAs08responseG07encoder7decoderAA0D0Vyxq_G10Foundation3URLV_AA20HTTPSCallableOptionsCxmq_m0A11SharedSwift0A11DataEncoderCAR0aQ7DecoderCtSERzSeR_r0_lF)


  ` Creates a reference to the Callable HTTPS trigger with the given name, the type of an
  `Encodable`
  request and the type of a `Decodable` response.

  #### Declaration

  Swift

      open func httpsCallable<Request: Encodable,
        Response: Decodable>(_ url: URL,
                             options: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableOptions.html,
                             requestAs: Request.Type = Request.self,
                             responseAs: Response.Type = Response.self,
                             encoder: FirebaseDataEncoder = FirebaseDataEncoder(
                             ),
                             decoder: FirebaseDataDecoder = FirebaseDataDecoder(
                             ))
        -> https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html<Request, Response>

  #### Parameters

  |---|---|
  | ` url ` | The url of the Callable HTTPS trigger |
  | ` options ` | The options with which to customize the Callable HTTPS trigger. |
  | ` requestAs ` | The type of the `Encodable` entity to use for requests to this `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` |
  | ` responseAs ` | The type of the `Decodable` entity to use for responses from this `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` |
  | ` encoder ` | The encoder instance to use to perform encoding. |
  | ` decoder ` | The decoder instance to use to perform decoding. |

  #### Return Value

  A reference to an HTTPS-callable Cloud Function that can be used to make Cloud
  Functions invocations.
- `


  ### [useEmulator(withHost:port:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/Functions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)useEmulatorWithHost:port:)


  ` Changes this instance to point to a Cloud Functions emulator running locally.
  See <https://firebase.google.com/docs/functions/local-emulator>

  #### Declaration

  Swift

      @objc
      open func useEmulator(withHost host: String, port: Int)

  #### Parameters

  |---|---|
  | ` host ` | The host of the local emulator, such as "localhost". |
  | ` port ` | The port of the local emulator, for example 5005. |