# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo.md.txt

# FirebaseAuth Framework Reference

# PhoneMultiFactorInfo

    @objc(FIRPhoneMultiFactorInfo)
    open class PhoneMultiFactorInfo: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo.html,
      @unchecked Sendable

Extends the MultiFactorInfo class for phone number second factors.

The identifier of this second factor is "phone".

This class is available on iOS and macOS.
- `


  ### [PhoneMultiFactorID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorInfo(cpy)FIRPhoneMultiFactorID)


  ` The string identifier for using phone as a second factor.

  #### Declaration

  Swift

      @objc(FIRPhoneMultiFactorID)
      public static let PhoneMultiFactorID: String

- `


  ### [TOTPMultiFactorID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorInfo(cpy)FIRTOTPMultiFactorID)


  ` The string identifier for using TOTP as a second factor.

  #### Declaration

  Swift

      @objc(FIRTOTPMultiFactorID)
      public static let TOTPMultiFactorID: String

- `


  ### [phoneNumber](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorInfo(py)phoneNumber)


  ` This is the phone number associated with the current second factor.

  #### Declaration

  Swift

      @objc
      open var phoneNumber: String

[## NSSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo#/NSSecureCoding)

- `


  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorInfo(cpy)supportsSecureCoding)


  ` Undocumented

  #### Declaration

  Swift

      override public class var supportsSecureCoding: Bool { get }

- `


  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorInfo(im)initWithCoder:)


  ` Undocumented

  #### Declaration

  Swift

      public required init?(coder: NSCoder)

- `


  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorInfo(im)encodeWithCoder:)


  ` Undocumented

  #### Declaration

  Swift

      override public func encode(with coder: NSCoder)