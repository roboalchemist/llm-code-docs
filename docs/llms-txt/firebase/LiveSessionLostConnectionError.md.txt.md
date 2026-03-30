# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionLostConnectionError.md.txt

# FirebaseAILogic Framework Reference

# LiveSessionLostConnectionError

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveSessionLostConnectionError : Error, Sendable, CustomNSError

The live session was closed, because the network connection was lost.

Check the `NSUnderlyingErrorKey` entry in `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionLostConnectionError.html#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp` for
the error that caused this.
- `


  ### [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionLostConnectionError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp)


  `

  #### Declaration

  Swift

      public var errorUserInfo: [String : Any] { get }