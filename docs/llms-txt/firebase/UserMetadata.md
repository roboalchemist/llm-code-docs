# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata.md.txt

# FirebaseAuth Framework Reference

# UserMetadata

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRUserMetadata)
    open class UserMetadata : NSObject

    extension UserMetadata: NSSecureCoding

A data class representing the metadata corresponding to a Firebase user.
- `
  ``
  ``
  `

  ### [lastSignInDate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata#/c:@M@FirebaseAuth@objc(cs)FIRUserMetadata(py)lastSignInDate)

  `
  `  
  Stores the last sign in date for the corresponding Firebase user.  

  #### Declaration

  Swift  

      @objc
      public let lastSignInDate: Date?

- `
  ``
  ``
  `

  ### [creationDate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata#/c:@M@FirebaseAuth@objc(cs)FIRUserMetadata(py)creationDate)

  `
  `  
  Stores the creation date for the corresponding Firebase user.  

  #### Declaration

  Swift  

      @objc
      public let creationDate: Date?

[## Secure Coding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata#/Secure-Coding)

- `
  ``
  ``
  `

  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata#/c:@M@FirebaseAuth@objc(cs)FIRUserMetadata(cpy)supportsSecureCoding)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static let supportsSecureCoding: Bool

- `
  ``
  ``
  `

  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata#/c:@M@FirebaseAuth@objc(cs)FIRUserMetadata(im)encodeWithCoder:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public func encode(with coder: NSCoder)

- `
  ``
  ``
  `

  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata#/c:@M@FirebaseAuth@objc(cs)FIRUserMetadata(im)initWithCoder:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public required convenience init?(coder: NSCoder)