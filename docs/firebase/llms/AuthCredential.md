# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.md.txt

# FirebaseAuth Framework Reference

# AuthCredential

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRAuthCredential)
    open class AuthCredential : NSObject, @unchecked Sendable

Public representation of a credential.
- `
  ``
  ``
  `

  ### [provider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential#/c:@M@FirebaseAuth@objc(cs)FIRAuthCredential(py)provider)

  `
  `  
  The name of the identity provider for the credential.  

  #### Declaration

  Swift  

      @objc
      public let provider: String