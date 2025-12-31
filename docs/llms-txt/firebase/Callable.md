# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.md.txt

# FirebaseFunctions Framework Reference

# Callable

    public struct Callable<Request, Response> : Sendable where Request : Encodable, Response : Decodable

A `Callable` is a reference to a particular Callable HTTPS trigger in Cloud Functions.  
Note
If the Callable HTTPS trigger accepts no parameters, `Never` can be used for iOS 17.0+. Otherwise, a simple encodable placeholder type (e.g., `struct EmptyRequest: Encodable {}`) can be used.
- `
  ``
  ``
  `

  ### [timeoutInterval](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable#/s:17FirebaseFunctions8CallableV15timeoutIntervalSdvp)

  `
  `  
  The timeout to use when calling the function. Defaults to 70 seconds.  

  #### Declaration

  Swift  

      public var timeoutInterval: TimeInterval { get set }

- `
  ``
  ``
  `

  ### [call(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable#/s:17FirebaseFunctions8CallableV4call_10completionyx_ys6ResultOyq_s5Error_pGScMYcctF)

  `
  `  
  Executes this Callable HTTPS trigger asynchronously.

  The data passed into the trigger must be of the generic `Request` type:

  The request to the Cloud Functions backend made by this method automatically includes a
  FCM token to identify the app instance. If a user is logged in with Firebase
  Auth, an auth ID token for the user is also automatically included.

  Firebase Cloud Messaging sends data to the Firebase backend periodically to collect
  information
  regarding the app instance. To stop this, see `Messaging.deleteData()`. It
  resumes with a new FCM Token the next time you call this method.  

  #### Declaration

  Swift  

      public func call(_ data: Request,
                       completion: @escaping @MainActor (Result<Response, Error>)
                         -> Void)

  #### Parameters

  |--------------------|---------------------------------------------------------|
  | ` `*data*` `       | Parameters to pass to the trigger.                      |
  | ` `*completion*` ` | The block to call when the HTTPS request has completed. |

- `
  ``
  ``
  `

  ### [callAsFunction(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable#/s:17FirebaseFunctions8CallableV14callAsFunction_10completionyx_ys6ResultOyq_s5Error_pGScMYcctF)

  `
  `  
  Creates a directly callable function.

  This allows users to call a HTTPS Callable Function like a normal Swift function:  

          let greeter = functions.httpsCallable("greeter",
                                                requestType: GreetingRequest.self,
                                                responseType: GreetingResponse.self)
          greeter(data) { result in
            print(result.greeting)
          }

  You can also call a HTTPS Callable function using the following syntax:  

          let greeter: Callable<GreetingRequest, GreetingResponse> =
      functions.httpsCallable("greeter")
          greeter(data) { result in
            print(result.greeting)
          }

  #### Declaration

  Swift  

      public func callAsFunction(_ data: Request,
                                 completion: @escaping @MainActor (Result<Response, Error>)
                                   -> Void)

  #### Parameters

  |--------------------|---------------------------------------------------------|
  | ` `*data*` `       | Parameters to pass to the trigger.                      |
  | ` `*completion*` ` | The block to call when the HTTPS request has completed. |

- `
  ``
  ``
  `

  ### [call(_:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable#/s:17FirebaseFunctions8CallableV4callyq_xYaKF)

  `
  `  
  Executes this Callable HTTPS trigger asynchronously.

  The data passed into the trigger must be of the generic `Request` type:

  The request to the Cloud Functions backend made by this method automatically includes a
  FCM token to identify the app instance. If a user is logged in with Firebase
  Auth, an auth ID token for the user is also automatically included.

  Firebase Cloud Messaging sends data to the Firebase backend periodically to collect
  information
  regarding the app instance. To stop this, see `Messaging.deleteData()`. It
  resumes with a new FCM Token the next time you call this method.  
  Throws

  An error if any value throws an error during encoding or decoding.  
  Throws

  An error if the callable fails to complete  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      public func call(_ data: Request) async throws -> Response

  #### Parameters

  |--------------|-------------------------------------------------------------|
  | ` `*data*` ` | The `Request` representing the data to pass to the trigger. |

  #### Return Value

  The decoded `Response` value
- `
  ``
  ``
  `

  ### [callAsFunction(_:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable#/s:17FirebaseFunctions8CallableV14callAsFunctionyq_xYaKF)

  `
  `  
  Creates a directly callable function.

  This allows users to call a HTTPS Callable Function like a normal Swift function:  

          let greeter = functions.httpsCallable("greeter",
                                                requestType: GreetingRequest.self,
                                                responseType: GreetingResponse.self)
          let result = try await greeter(data)
          print(result.greeting)

  You can also call a HTTPS Callable function using the following syntax:  

          let greeter: Callable<GreetingRequest, GreetingResponse> =
      functions.httpsCallable("greeter")
          let result = try await greeter(data)
          print(result.greeting)

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      public func callAsFunction(_ data: Request) async throws -> Response

  #### Parameters

  |--------------|------------------------------------|
  | ` `*data*` ` | Parameters to pass to the trigger. |

  #### Return Value

The decoded `Response` value  
[## Available where \`Request\`: \`Sendable\`, \`Response\`: \`Sendable\`](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable#/Available-where-%60Request%60%3A-%60Sendable%60%2C-%60Response%60%3A-%60Sendable%60)

- `
  ``
  ``
  `

  ### [stream(_:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable#/s:17FirebaseFunctions8CallableVAAs8SendableRzsADR_rlE6streamyScsyq_s5Error_pGxSgKF)

  `
  `  
  Creates a stream that yields responses from the streaming callable function.

  The request to the Cloud Functions backend made by this method automatically includes a FCM
  token to identify the app instance. If a user is logged in with Firebase Auth, an auth ID
  token for the user is included. If App Check is integrated, an app check token is included.

  Firebase Cloud Messaging sends data to the Firebase backend periodically to collect
  information regarding the app instance. To stop this, see `Messaging.deleteData()`. It
  resumes with a new FCM Token the next time you call this method.  
  Important
  The final result returned by the callable function is only accessible when using [StreamResponse](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse.html) as the `Response` generic type.

  Example of using `stream` *without* [StreamResponse](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse.html):  

      let callable: Callable<MyRequest, MyResponse> = // ...
      let request: MyRequest = // ...
      let stream = try callable.stream(request)
      for try await response in stream {
        // Process each `MyResponse` message
        print(response)
      }

  Example of using `stream` *with* [StreamResponse](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse.html):  

      let callable: Callable<MyRequest, StreamResponse<MyMessage, MyResult>> = // ...
      let request: MyRequest = // ...
      let stream = try callable.stream(request)
      for try await response in stream {
        switch response {
        case .message(let message):
          // Process each `MyMessage`
          print(message)
        case .result(let result):
          // Process the final `MyResult`
          print(result)
        }
      }

  Throws
  A `FunctionsError` if the parameter `data` cannot be encoded.  

  #### Declaration

  Swift  

      func stream(_ data: Request? = nil) throws -> AsyncThrowingStream<Response, Error>

  #### Parameters

  |--------------|------------------------------------------------------|
  | ` `*data*` ` | The `Request` data to pass to the callable function. |

  #### Return Value

  A stream wrapping responses yielded by the streaming callable function or
  a `FunctionsError` if an error occurred.