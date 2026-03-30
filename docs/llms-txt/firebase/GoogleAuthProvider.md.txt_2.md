# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GoogleAuthProvider.md.txt

# FirebaseAuth Framework Reference

# GoogleAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRGoogleAuthProvider)
    open class GoogleAuthProvider : NSObject

Utility class for constructing Google Sign In credentials.
- `


  ### [id](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GoogleAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRGoogleAuthProvider(cpy)id)


  ` A string constant identifying the Google identity provider.

  #### Declaration

  Swift

      @objc
      public static let id: String

- `


  ### [credential(withIDToken:accessToken:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GoogleAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRGoogleAuthProvider(cm)credentialWithIDToken:accessToken:)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` for a Google sign in.

  #### Declaration

  Swift

      @objc
      open class func credential(withIDToken idToken: String,
                                 accessToken: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html

  #### Parameters

  |---|---|
  | ` idToken ` | The ID Token from Google. |
  | ` accessToken ` | The Access Token from Google. |

  #### Return Value

  An AuthCredential containing the Google credentials.