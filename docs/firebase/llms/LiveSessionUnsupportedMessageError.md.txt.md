# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionUnsupportedMessageError.md.txt

# FirebaseAILogic Framework Reference

# LiveSessionUnsupportedMessageError

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveSessionUnsupportedMessageError : Error, Sendable, CustomNSError

The model sent a message that the SDK failed to parse.

This may indicate that the SDK version needs updating, a model is too old for the current SDK
version, or that the model is just
not supported.

Check the `NSUnderlyingErrorKey` entry in `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionUnsupportedMessageError.html#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp`
for the error that caused this.
- `


  ### [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionUnsupportedMessageError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp)


  `

  #### Declaration

  Swift

      public var errorUserInfo: [String : Any] { get }