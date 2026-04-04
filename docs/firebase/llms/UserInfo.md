# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo.md.txt

# FirebaseAuth Framework Reference

# UserInfo

    @objc(FIRUserInfo)
    public protocol UserInfo : NSObjectProtocol

Represents user data returned from an identity provider.
- `
  ``
  ``
  `

  ### [providerID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo#/c:@M@FirebaseAuth@objc(pl)FIRUserInfo(py)providerID)

  `
  `  
  The provider identifier.  

  #### Declaration

  Swift  

      var providerID: String { get }

- `
  ``
  ``
  `

  ### [uid](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo#/c:@M@FirebaseAuth@objc(pl)FIRUserInfo(py)uid)

  `
  `  
  The provider's user ID for the user.  

  #### Declaration

  Swift  

      var uid: String { get }

- `
  ``
  ``
  `

  ### [displayName](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo#/c:@M@FirebaseAuth@objc(pl)FIRUserInfo(py)displayName)

  `
  `  
  The name of the user.  

  #### Declaration

  Swift  

      var displayName: String? { get }

- `
  ``
  ``
  `

  ### [photoURL](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo#/c:@M@FirebaseAuth@objc(pl)FIRUserInfo(py)photoURL)

  `
  `  
  The URL of the user's profile photo.  

  #### Declaration

  Swift  

      var photoURL: URL? { get }

- `
  ``
  ``
  `

  ### [email](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo#/c:@M@FirebaseAuth@objc(pl)FIRUserInfo(py)email)

  `
  `  
  The user's email address.  

  #### Declaration

  Swift  

      var email: String? { get }

- `
  ``
  ``
  `

  ### [phoneNumber](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo#/c:@M@FirebaseAuth@objc(pl)FIRUserInfo(py)phoneNumber)

  `
  `  
  A phone number associated with the user.

  This property is only available for users authenticated via phone number auth.  

  #### Declaration

  Swift  

      var phoneNumber: String? { get }