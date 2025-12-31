# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthSettings.md.txt

# FirebaseAuth Framework Reference

# AuthSettings

    @objc(FIRAuthSettings)
    open class AuthSettings : NSObject, NSCopying

Determines settings related to an auth object.
- `
  ``
  ``
  `

  ### [appVerificationDisabledForTesting](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthSettings#/c:@M@FirebaseAuth@objc(cs)FIRAuthSettings(py)appVerificationDisabledForTesting)

  `
  `  
  Flag to determine whether app verification should be disabled for testing or not.  

  #### Declaration

  Swift  

      @objc
      open var appVerificationDisabledForTesting: Bool

- `
  ``
  ``
  `

  ### [isAppVerificationDisabledForTesting](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthSettings#/c:@M@FirebaseAuth@objc(cs)FIRAuthSettings(py)isAppVerificationDisabledForTesting)

  `
  `  
  Flag to determine whether app verification should be disabled for testing or not.  

  #### Declaration

  Swift  

      @objc
      open var isAppVerificationDisabledForTesting: Bool { get set }

[## NSCopying](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthSettings#/NSCopying)

- `
  ``
  ``
  `

  ### [copy(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthSettings#/c:@M@FirebaseAuth@objc(cs)FIRAuthSettings(im)copyWithZone:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      open func copy(with zone: NSZone? = nil) -> Any