# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/FacebookAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FacebookAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRFacebookAuthProvider)
    open class FacebookAuthProvider : NSObject

Utility class for constructing Facebook Sign In credentials.
- `


  ### [id](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/FacebookAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRFacebookAuthProvider(cpy)id)


  ` A string constant identifying the Facebook identity provider.

  #### Declaration

  Swift

      @objc
      public static let id: String

- `


  ### [credential(withAccessToken:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/FacebookAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRFacebookAuthProvider(cm)credentialWithAccessToken:)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` for a Facebook sign in.

  #### Declaration

  Swift

      @objc
      open class func credential(withAccessToken accessToken: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html

  #### Parameters

  |---|---|
  | ` accessToken ` | The Access Token from Facebook. |

  #### Return Value

  An `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` containing the Facebook credentials.