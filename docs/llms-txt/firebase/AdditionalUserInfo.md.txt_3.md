# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo.md.txt

# FirebaseAuth Framework Reference

# AdditionalUserInfo

    @objc(FIRAdditionalUserInfo)
    open class AdditionalUserInfo : NSObject

    extension AdditionalUserInfo: NSSecureCoding

Undocumented
- `


  ### [providerID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/c:@M@FirebaseAuth@objc(cs)FIRAdditionalUserInfo(py)providerID)


  ` The provider identifier.

  #### Declaration

  Swift

      @objc
      public let providerID: String

- `


  ### [profile](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/c:@M@FirebaseAuth@objc(cs)FIRAdditionalUserInfo(py)profile)


  ` Dictionary containing the additional IdP specific information.

  #### Declaration

  Swift

      @objc
      public let profile: [String : Any]?

- `


  ### [username](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/c:@M@FirebaseAuth@objc(cs)FIRAdditionalUserInfo(py)username)


  ` The name of the user.

  #### Declaration

  Swift

      @objc
      public let username: String?

- `


  ### [isNewUser](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/c:@M@FirebaseAuth@objc(cs)FIRAdditionalUserInfo(py)isNewUser)


  ` Indicates whether or not the current user was signed in for the first time.

  #### Declaration

  Swift

      @objc
      public let isNewUser: Bool

- `


  ### [newUser()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/c:@M@FirebaseAuth@objc(cs)FIRAdditionalUserInfo(im)newUser)


  ` Indicates whether or not the current user was signed in for the first time.

  #### Declaration

  Swift

      @objc
      open func newUser() -> Bool

[## Secure Coding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/Secure-Coding)

- `


  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/c:@M@FirebaseAuth@objc(cs)FIRAdditionalUserInfo(cpy)supportsSecureCoding)


  ` Undocumented

  #### Declaration

  Swift

      public static let supportsSecureCoding: Bool

- `


  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/c:@M@FirebaseAuth@objc(cs)FIRAdditionalUserInfo(im)initWithCoder:)


  ` Undocumented

  #### Declaration

  Swift

      public required init?(coder aDecoder: NSCoder)

- `


  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo#/c:@M@FirebaseAuth@objc(cs)FIRAdditionalUserInfo(im)encodeWithCoder:)


  ` Undocumented

  #### Declaration

  Swift

      public func encode(with aCoder: NSCoder)