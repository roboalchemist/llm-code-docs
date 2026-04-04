# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/RequestOptions.md.txt

# FirebaseVertexAI Framework Reference

# RequestOptions

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct RequestOptions : Sendable

    extension RequestOptions: Equatable

Configuration parameters for sending requests to the backend.
- `


  ### [init(timeout:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/RequestOptions#/s:16FirebaseVertexAI14RequestOptionsV7timeoutACSd_tcfc)


  ` Initializes a request options object.

  #### Declaration

  Swift

      public init(timeout: TimeInterval = 180.0)

  #### Parameters

  |---|---|
  | ` timeout ` | The request's timeout interval in seconds; defaults to 180 seconds. |