# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo.md.txt

# FirebaseAuth Framework Reference

# MultiFactorInfo

    @objc(FIRMultiFactorInfo)
    open class MultiFactorInfo : NSObject, @unchecked Sendable

    extension MultiFactorInfo: NSSecureCoding

Safe public structure used to represent a second factor entity from a client perspective.

This class is available on iOS and macOS.
- `


  ### [uid](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorInfo(py)UID)


  ` The multi-factor enrollment ID.

  #### Declaration

  Swift

      @objc(UID)
      public let uid: String

- `


  ### [displayName](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorInfo(py)displayName)


  ` The user friendly name of the current second factor.

  #### Declaration

  Swift

      @objc
      public let displayName: String?

- `


  ### [enrollmentDate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorInfo(py)enrollmentDate)


  ` The second factor enrollment date.

  #### Declaration

  Swift

      @objc
      public let enrollmentDate: Date

- `


  ### [factorID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorInfo(py)factorID)


  ` The identifier of the second factor.

  #### Declaration

  Swift

      @objc
      public let factorID: String

[## NSSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo#/NSSecureCoding)

- `


  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorInfo(cpy)supportsSecureCoding)


  ` Undocumented

  #### Declaration

  Swift

      public class var supportsSecureCoding: Bool { get }

- `


  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorInfo(im)encodeWithCoder:)


  ` Undocumented

  #### Declaration

  Swift

      public func encode(with coder: NSCoder)

- `


  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorInfo(im)initWithCoder:)


  ` Undocumented

  #### Declaration

  Swift

      public required init?(coder: NSCoder)