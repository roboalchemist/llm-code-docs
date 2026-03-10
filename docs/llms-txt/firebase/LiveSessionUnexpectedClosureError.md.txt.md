# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionUnexpectedClosureError.md.txt

# FirebaseAILogic Framework Reference

# LiveSessionUnexpectedClosureError

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveSessionUnexpectedClosureError : Error, Sendable, CustomNSError

The live session was closed, but not for a reason the SDK expected.

Check the `NSUnderlyingErrorKey` entry in `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionUnexpectedClosureError.html#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp`
for the error that caused this.
- `


  ### [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionUnexpectedClosureError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp)


  `

  #### Declaration

  Swift

      public var errorUserInfo: [String : Any] { get }