# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorResolver.md.txt

# FirebaseAuth Framework Reference

# MultiFactorResolver

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRMultiFactorResolver)
    open class MultiFactorResolver : NSObject

The subclass of base class `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html`, used to assert ownership of a phone
second factor.

This class is available on iOS and macOS.
- `


  ### [session](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorResolver#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorResolver(py)session)


  ` The opaque session identifier for the current sign-in flow.

  #### Declaration

  Swift

      @objc
      public let session: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession

- `


  ### [hints](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorResolver#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorResolver(py)hints)


  ` The list of hints for the second factors needed to complete the sign-in for the current
  session.

  #### Declaration

  Swift

      @objc
      public let hints: [https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo.html]

- `


  ### [auth](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorResolver#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorResolver(py)auth)


  ` The Auth reference for the current `MultiResolver`.

  #### Declaration

  Swift

      @objc
      public let auth: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html

- `


  ### [resolveSignIn(with:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorResolver#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorResolver(im)resolveSignInWithAssertion:completion:)


  ` A helper function to help users complete sign in with a second factor using a

  #### Declaration

  Swift

      @objc(resolveSignInWithAssertion:completion:)
      open func resolveSignIn(with assertion: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html,
                              completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |---|---|
  | ` assertion ` | The assertion confirming the user successfully completed the second factor challenge. |
  | ` completion ` | The block invoked when the request is complete, or fails. |

- `


  ### [resolveSignIn(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorResolver#/s:12FirebaseAuth19MultiFactorResolverC13resolveSignIn4withAA0B10DataResultCAA0cD9AssertionC_tYaKF)


  ` A helper function to help users complete sign in with a second factor using a

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func resolveSignIn(with assertion: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |---|---|
  | ` assertion ` | The assertion confirming the user successfully completed the second factor challenge. |