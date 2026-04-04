# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse.md.txt

# FirebaseFunctions Framework Reference

# StreamResponse

    @available(macOS 12.0, iOS 15.0, watchOS 8.0, tvOS 15.0, *)
    public enum StreamResponse<Message: Decodable & Sendable, Result: Decodable & Sendable>: Decodable,
      Sendable,
      StreamResponseProtocol

A convenience type used to receive both the streaming callable function's yielded messages and
its return value.

This can be used as the generic `Response` parameter to `https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable.html` to receive both the
yielded messages and final return value of the streaming callable function.
- `


  ### [message(_:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse#/s:17FirebaseFunctions14StreamResponseO7messageyACyxq_GxcAEmSeRzs8SendableRzSeR_sAFR_r0_lF)


  ` The message yielded by the callable function.

  #### Declaration

  Swift

      case message(Message)

- `


  ### [result(_:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse#/s:17FirebaseFunctions14StreamResponseO6resultyACyxq_Gq_cAEmSeRzs8SendableRzSeR_sAFR_r0_lF)


  ` The final result returned by the callable function.

  #### Declaration

  Swift

      case result(Result)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws