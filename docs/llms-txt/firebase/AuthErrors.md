# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthErrors.md.txt

# FirebaseAuth Framework Reference

# AuthErrors

    @objc(FIRAuthErrors)
    open class AuthErrors : NSObject

Error Codes common to all API Methods:
- `
  ``
  ``
  `

  ### [domain](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthErrors#/c:@M@FirebaseAuth@objc(cs)FIRAuthErrors(cpy)domain)

  `
  `  
  The Firebase Auth error domain.  

  #### Declaration

  Swift  

      @objc
      public static let domain: String

- `
  ``
  ``
  `

  ### [userInfoNameKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthErrors#/c:@M@FirebaseAuth@objc(cs)FIRAuthErrors(cpy)userInfoNameKey)

  `
  `  
  The name of the key for the error short string of an error code.  

  #### Declaration

  Swift  

      @objc
      public static let userInfoNameKey: String

- `
  ``
  ``
  `

  ### [userInfoEmailKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthErrors#/c:@M@FirebaseAuth@objc(cs)FIRAuthErrors(cpy)userInfoEmailKey)

  `
  `  
  Error codes for Email operations

  Errors with one of the following three codes:
  - `accountExistsWithDifferentCredential`
  - `credentialAlreadyInUse`
  - emailAlreadyInUse\`

  may contain an `NSError.userInfo` dictionary object which contains this key. The value
  associated with this key is an NSString of the email address of the account that already
  exists.  

  #### Declaration

  Swift  

      @objc
      public static let userInfoEmailKey: String

- `
  ``
  ``
  `

  ### [userInfoUpdatedCredentialKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthErrors#/c:@M@FirebaseAuth@objc(cs)FIRAuthErrors(cpy)userInfoUpdatedCredentialKey)

  `
  `  
  The key used to read the updated Auth credential from the userInfo dictionary of the
  NSError object returned. This is the updated auth credential the developer should use for
  recovery if applicable.  

  #### Declaration

  Swift  

      @objc
      public static let userInfoUpdatedCredentialKey: String

- `
  ``
  ``
  `

  ### [userInfoMultiFactorResolverKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthErrors#/c:@M@FirebaseAuth@objc(cs)FIRAuthErrors(cpy)FIRAuthErrorUserInfoMultiFactorResolverKey)

  `
  `  
  The key used to read the MFA resolver from the userInfo dictionary of the NSError object
  returned when 2FA is required for sign-incompletion.  

  #### Declaration

  Swift  

      @objc(FIRAuthErrorUserInfoMultiFactorResolverKey)
      public static let userInfoMultiFactorResolverKey: String