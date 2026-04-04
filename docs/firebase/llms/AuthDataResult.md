# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.md.txt

# FirebaseAuth Framework Reference

# AuthDataResult

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRAuthDataResult)
    open class AuthDataResult : NSObject

    extension AuthDataResult: NSSecureCoding

Helper object that contains the result of a successful sign-in, link and reauthenticate
action.

It contains references to a [User](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html) instance and an [AdditionalUserInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo.html) instance.
- `
  ``
  ``
  `

  ### [user](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthDataResult(py)user)

  `
  `  
  The signed in user.  

  #### Declaration

  Swift  

      @objc
      public let user: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html

- `
  ``
  ``
  `

  ### [additionalUserInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthDataResult(py)additionalUserInfo)

  `
  `  
  If available, contains the additional IdP specific information about signed in user.  

  #### Declaration

  Swift  

      @objc
      public let additionalUserInfo: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo.html?

- `
  ``
  ``
  `

  ### [credential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthDataResult(py)credential)

  `
  `  
  This property will be non-nil after a successful headful-lite sign-in via
  `signIn(with:uiDelegate:completion:)`.

  May be used to obtain the accessToken and/or IDToken
  pertaining to a recently signed-in user.  

  #### Declaration

  Swift  

      @objc
      public let credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential.html?

[## Secure Coding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult#/Secure-Coding)

- `
  ``
  ``
  `

  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthDataResult(cpy)supportsSecureCoding)

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

  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthDataResult(im)encodeWithCoder:)

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

  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult#/c:@M@FirebaseAuth@objc(cs)FIRAuthDataResult(im)initWithCoder:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public required init?(coder: NSCoder)