# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential.md.txt

# FirebaseAuth Framework Reference

# OAuthCredential

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIROAuthCredential)
    open class OAuthCredential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html, NSSecureCoding,
      @unchecked Sendable

Internal implementation of [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) for generic credentials.
- `
  ``
  ``
  `

  ### [idToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential#/c:@M@FirebaseAuth@objc(cs)FIROAuthCredential(py)IDToken)

  `
  `  
  The ID Token associated with this credential.  

  #### Declaration

  Swift  

      @objc(IDToken)
      public let idToken: String?

- `
  ``
  ``
  `

  ### [accessToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential#/c:@M@FirebaseAuth@objc(cs)FIROAuthCredential(py)accessToken)

  `
  `  
  The access token associated with this credential.  

  #### Declaration

  Swift  

      @objc
      public let accessToken: String?

- `
  ``
  ``
  `

  ### [secret](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential#/c:@M@FirebaseAuth@objc(cs)FIROAuthCredential(py)secret)

  `
  `  
  The secret associated with this credential. This will be nil for OAuth 2.0 providers.

  OAuthCredential already exposes a `provider` getter. This will help the developer
  determine whether an access token / secret pair is needed.  

  #### Declaration

  Swift  

      @objc
      public let secret: String?

[## Secure Coding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential#/Secure-Coding)

- `
  ``
  ``
  `

  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential#/c:@M@FirebaseAuth@objc(cs)FIROAuthCredential(cpy)supportsSecureCoding)

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

  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential#/c:@M@FirebaseAuth@objc(cs)FIROAuthCredential(im)encodeWithCoder:)

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

  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential#/c:@M@FirebaseAuth@objc(cs)FIROAuthCredential(im)initWithCoder:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public required init?(coder: NSCoder)