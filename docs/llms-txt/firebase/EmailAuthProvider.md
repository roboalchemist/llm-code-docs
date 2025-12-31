# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/EmailAuthProvider.md.txt

# FirebaseAuth Framework Reference

# EmailAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIREmailAuthProvider)
    open class EmailAuthProvider : NSObject

A concrete implementation of `AuthProvider` for Email \& Password Sign In.
- `
  ``
  ``
  `

  ### [id](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/EmailAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIREmailAuthProvider(cpy)id)

  `
  `  
  A string constant identifying the email \& password identity provider.  

  #### Declaration

  Swift  

      @objc
      public static let id: String

- `
  ``
  ``
  `

  ### [credential(withEmail:password:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/EmailAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIREmailAuthProvider(cm)credentialWithEmail:password:)

  `
  `  
  Creates an [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) for an email \& password sign in  

  #### Declaration

  Swift  

      @objc
      open class func credential(withEmail email: String, password: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html

  #### Parameters

  |------------------|---------------------------|
  | ` `*email*` `    | The user's email address. |
  | ` `*password*` ` | The user's password.      |

  #### Return Value

  An [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) containing the email \& password credential.
- `
  ``
  ``
  `

  ### [credential(withEmail:link:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/EmailAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIREmailAuthProvider(cm)credentialWithEmail:link:)

  `
  `  
  Creates an [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) for an email \& link sign in.  

  #### Declaration

  Swift  

      @objc
      open class func credential(withEmail email: String, link: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html

  #### Parameters

  |---------------|---------------------------|
  | ` `*email*` ` | The user's email address. |
  | ` `*link*` `  | The email sign-in link.   |

  #### Return Value

  An [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) containing the email \& link credential.