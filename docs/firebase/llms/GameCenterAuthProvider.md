# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GameCenterAuthProvider.md.txt

# FirebaseAuth Framework Reference

# GameCenterAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRGameCenterAuthProvider)
    open class GameCenterAuthProvider : NSObject

A concrete implementation of `AuthProvider` for Game Center Sign In. Not available on watchOS.
- `
  ``
  ``
  `

  ### [id](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GameCenterAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRGameCenterAuthProvider(cpy)id)

  `
  `  
  A string constant identifying the Game Center identity provider.  

  #### Declaration

  Swift  

      @objc
      public static let id: String

- `
  ``
  ``
  `

  ### [getCredential(completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GameCenterAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRGameCenterAuthProvider(cm)getCredentialWithCompletion:)

  `
  `  
  Creates an [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) for a Game Center sign in.  

  #### Declaration

  Swift  

      @objc
      open class func getCredential(completion: @escaping (https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html?, Error?) -> Void)

- `
  ``
  ``
  `

  ### [getCredential()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GameCenterAuthProvider#/s:12FirebaseAuth010GameCenterB8ProviderC13getCredentialAA0bG0CyYaKFZ)

  `
  `  
  Creates an [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) for a Game Center sign in.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 8, *)
      open class func getCredential() async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html