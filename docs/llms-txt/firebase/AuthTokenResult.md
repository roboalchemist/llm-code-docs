# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult.md.txt

# FirebaseAuth Framework Reference

# AuthTokenResult

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRAuthTokenResult)
    open class AuthTokenResult : NSObject

    extension AuthTokenResult: NSSecureCoding

A data class containing the ID token JWT string and other properties associated with the
token including the decoded payload claims.
- `
  ``
  ``
  `

  ### [token](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(py)token)

  `
  `  
  Stores the JWT string of the ID token.  

  #### Declaration

  Swift  

      @objc
      open var token: String

- `
  ``
  ``
  `

  ### [expirationDate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(py)expirationDate)

  `
  `  
  Stores the ID token's expiration date.  

  #### Declaration

  Swift  

      @objc
      open var expirationDate: Date

- `
  ``
  ``
  `

  ### [authDate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(py)authDate)

  `
  `  
  Stores the ID token's authentication date.

  This is the date the user was signed in and NOT the date the token was refreshed.  

  #### Declaration

  Swift  

      @objc
      open var authDate: Date

- `
  ``
  ``
  `

  ### [issuedAtDate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(py)issuedAtDate)

  `
  `  
  Stores the date that the ID token was issued.

  This is the date last refreshed and NOT the last authentication date.  

  #### Declaration

  Swift  

      @objc
      open var issuedAtDate: Date

- `
  ``
  ``
  `

  ### [signInProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(py)signInProvider)

  `
  `  
  Stores sign-in provider through which the token was obtained.  

  #### Declaration

  Swift  

      @objc
      open var signInProvider: String

- `
  ``
  ``
  `

  ### [signInSecondFactor](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(py)signInSecondFactor)

  `
  `  
  Stores sign-in second factor through which the token was obtained.  

  #### Declaration

  Swift  

      @objc
      open var signInSecondFactor: String

- `
  ``
  ``
  `

  ### [claims](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(py)claims)

  `
  `  
  Stores the entire payload of claims found on the ID token.

  This includes the standard
  reserved claims as well as custom claims set by the developer via the Admin SDK.  

  #### Declaration

  Swift  

      @objc
      open var claims: [String : Any]

[## Secure Coding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/Secure-Coding)

- `
  ``
  ``
  `

  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(cpy)supportsSecureCoding)

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

  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(im)encodeWithCoder:)

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

  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthTokenResult(im)initWithCoder:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public required convenience init?(coder: NSCoder)