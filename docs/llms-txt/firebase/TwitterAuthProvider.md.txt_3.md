# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TwitterAuthProvider.md.txt

# FirebaseAuth Framework Reference

# TwitterAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRTwitterAuthProvider)
    open class TwitterAuthProvider : NSObject

Utility class for constructing Twitter Sign In credentials.
- `


  ### [id](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TwitterAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRTwitterAuthProvider(cpy)id)


  ` A string constant identifying the Twitter identity provider.

  #### Declaration

  Swift

      @objc
      public static let id: String

- `


  ### [credential(withToken:secret:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TwitterAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRTwitterAuthProvider(cm)credentialWithToken:secret:)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` for a Twitter sign in.

  #### Declaration

  Swift

      @objc
      open class func credential(withToken token: String, secret: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html

  #### Parameters

  |---|---|
  | ` token ` | The Twitter OAuth token. |
  | ` secret ` | The Twitter OAuth secret. |

  #### Return Value

  An AuthCredential containing the Twitter credentials.