# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor.md.txt

# FirebaseAuth Framework Reference

# MultiFactor

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRMultiFactor)
    open class MultiFactor : NSObject

    extension MultiFactor: NSSecureCoding

The interface defining the multi factor related properties and operations pertaining to a
user.

This class is available on iOS and macOS.
- `


  ### [enrolledFactors](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactor(py)enrolledFactors)


  ` Undocumented

  #### Declaration

  Swift

      @objc
      open var enrolledFactors: [https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo.html]

- `


  ### [getSessionWithCompletion(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactor(im)getSessionWithCompletion:)


  ` Get a session for a second factor enrollment operation.

  This is used to identify the current user trying to enroll a second factor.

  #### Declaration

  Swift

      @objc(getSessionWithCompletion:)
      open func getSessionWithCompletion(_ completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession?, Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` completion ` | A block with the session identifier for a second factor enrollment operation. |

- `


  ### [session()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/s:12FirebaseAuth11MultiFactorC7sessionAA0cD7SessionCyYaKF)


  ` Get a session for a second factor enrollment operation.

  This is used to identify the current user trying to enroll a second factor.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func session() async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession

- `


  ### [enroll(with:displayName:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactor(im)enrollWithAssertion:displayName:completion:)


  ` Enrolls a second factor as identified by the `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html` parameter for the
  current user.

  #### Declaration

  Swift

      @objc(enrollWithAssertion:displayName:completion:)
      open func enroll(with assertion: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html,
                       displayName: String?,
                       completion: ((Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` assertion ` | The `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html`. |
  | ` displayName ` | An optional display name associated with the multi factor to enroll. |
  | ` completion ` | The block invoked when the request is complete, or fails. |

- `


  ### [enroll(with:displayName:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/s:12FirebaseAuth11MultiFactorC6enroll4with11displayNameyAA0cD9AssertionC_SSSgtYaKF)


  ` Enrolls a second factor as identified by the `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html` parameter for the
  current user.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func enroll(with assertion: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html, displayName: String?) async throws

  #### Parameters

  |---|---|
  | ` assertion ` | The `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.html`. |
  | ` displayName ` | An optional display name associated with the multi factor to enroll. |

- `


  ### [unenroll(with:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactor(im)unenrollWithInfo:completion:)


  ` Unenroll the given multi factor.

  #### Declaration

  Swift

      @objc(unenrollWithInfo:completion:)
      open func unenroll(with factorInfo: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo.html,
                         completion: ((Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` factorInfo ` | The second factor instance to unenroll. |
  | ` completion ` | The block invoked when the request to send the verification email is complete, or fails. |

- `


  ### [unenroll(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/s:12FirebaseAuth11MultiFactorC8unenroll4withyAA0cD4InfoC_tYaKF)


  ` Unenroll the given multi factor.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func unenroll(with factorInfo: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo.html) async throws

- `


  ### [unenroll(withFactorUID:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactor(im)unenrollWithFactorUID:completion:)


  ` Unenroll the given multi factor.

  #### Declaration

  Swift

      @objc(unenrollWithFactorUID:completion:)
      open func unenroll(withFactorUID factorUID: String,
                         completion: ((Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` factorUID ` | The unique identifier corresponding to the second factor being unenrolled. |
  | ` completion ` | The block invoked when the request to send the verification email is complete, or fails. |

- `


  ### [unenroll(withFactorUID:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/s:12FirebaseAuth11MultiFactorC8unenroll04withD3UIDySS_tYaKF)


  ` Unenroll the given multi factor.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func unenroll(withFactorUID factorUID: String) async throws

[## NSSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/NSSecureCoding)

- `


  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactor(cpy)supportsSecureCoding)


  ` Undocumented

  #### Declaration

  Swift

      public static let supportsSecureCoding: Bool

- `


  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactor(im)encodeWithCoder:)


  ` Undocumented

  #### Declaration

  Swift

      public func encode(with coder: NSCoder)

- `


  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactor(im)initWithCoder:)


  ` Undocumented

  #### Declaration

  Swift

      public required init?(coder: NSCoder)