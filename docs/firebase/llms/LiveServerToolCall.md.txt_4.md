# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerToolCall.md.txt

# FirebaseAILogic Framework Reference

# LiveServerToolCall

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    @available(watchOS, unavailable)
    public struct LiveServerToolCall : Sendable

Request for the client to execute the provided `functionCalls`.

The client should return matching `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart.html`, where the
`https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart.html#/s:15FirebaseAILogic20FunctionResponsePartV10functionIdSSSgvp` fields correspond to individual `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html`s.
- `


  ### [functionCalls](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerToolCall#/s:15FirebaseAILogic18LiveServerToolCallV13functionCallsSayAA08FunctionF4PartVGSgvp)


  ` A list of `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html` to run and return responses for.

  #### Declaration

  Swift

      public var functionCalls: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html]? { get }