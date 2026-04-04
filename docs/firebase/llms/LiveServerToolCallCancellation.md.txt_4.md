# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerToolCallCancellation.md.txt

# FirebaseAILogic Framework Reference

# LiveServerToolCallCancellation

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveServerToolCallCancellation : Sendable

Notification for the client to cancel a previous function call from `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerToolCall.html`.

The client does not need to send `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart.html`s for the cancelled
`https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html`s.
- `


  ### [ids](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerToolCallCancellation#/s:15FirebaseAILogic30LiveServerToolCallCancellationV3idsSaySSGSgvp)


  ` A list of function ids matching the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html#/s:15FirebaseAILogic16FunctionCallPartV10functionIdSSSgvp` provided in a previous
  `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerToolCall.html`, where only the provided ids should be cancelled.

  #### Declaration

  Swift

      public var ids: [String]? { get }