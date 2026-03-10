# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums.md.txt

# FirebaseFunctions Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [StreamResponse](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse)


  ` A convenience type used to receive both the streaming callable function's yielded messages and
  its return value.

  This can be used as the generic `Response` parameter to `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable` to receive both the
  yielded messages and final return value of the streaming callable function.

  #### Declaration

  Swift

      @available(macOS 12.0, iOS 15.0, watchOS 8.0, tvOS 15.0, *)
      public enum StreamResponse<Message: Decodable & Sendable, Result: Decodable & Sendable>: Decodable,
        Sendable,
        StreamResponseProtocol

- `


  ### [FunctionsErrorCode](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode)


  ` The set of error status codes that can be returned from a Callable HTTPS trigger. These are the
  canonical error codes for Google APIs, as documented here:
  <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto#L26>

  #### Declaration

  Swift

      @objc(FIRFunctionsErrorCode)
      public enum FunctionsErrorCode : Int, Sendable