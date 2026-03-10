# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionSetupError.md.txt

# FirebaseAILogic Framework Reference

# LiveSessionSetupError

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveSessionSetupError : Error, Sendable, CustomNSError

The model refused our request to setup a live session.

This can occur due to the model not supporting the requested response modalities, the project
not having access to the model, the model being invalid, or some internal error.

Check the `NSUnderlyingErrorKey` entry in `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionSetupError.html#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp` for the error
that caused this.
- `


  ### [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionSetupError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp)


  `

  #### Declaration

  Swift

      public var errorUserInfo: [String : Any] { get }