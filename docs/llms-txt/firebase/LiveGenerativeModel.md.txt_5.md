# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel.md.txt

# FirebaseAILogic Framework Reference

# LiveGenerativeModel

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public final class LiveGenerativeModel

A multimodal model (like Gemini) capable of real-time content generation based on
various input types, supporting bidirectional streaming.

You can create a new session via `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel.html#/s:15FirebaseAILogic19LiveGenerativeModelC7connectAA0C7SessionCyYaKF`.
- `


  ### [connect()](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel#/s:15FirebaseAILogic19LiveGenerativeModelC7connectAA0C7SessionCyYaKF)


  ` Start a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.html` with the server for bidirectional streaming.

  #### Declaration

  Swift

      public func connect() async throws -> https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.html` that you can use to stream messages to and from the server.