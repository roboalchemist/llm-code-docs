# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GitHubAuthProvider.md.txt

# FirebaseAuth Framework Reference

# GitHubAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRGitHubAuthProvider)
    open class GitHubAuthProvider : NSObject

Utility class for constructing GitHub Sign In credentials.
- `
  ``
  ``
  `

  ### [id](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GitHubAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRGitHubAuthProvider(cpy)id)

  `
  `  
  A string constant identifying the GitHub identity provider.  

  #### Declaration

  Swift  

      @objc
      public static let id: String

- `
  ``
  ``
  `

  ### [credential(withToken:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GitHubAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRGitHubAuthProvider(cm)credentialWithToken:)

  `
  `  
  Creates an [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) for a GitHub sign in.  

  #### Declaration

  Swift  

      @objc
      open class func credential(withToken token: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html

  #### Parameters

  |---------------|--------------------------------|
  | ` `*token*` ` | The GitHub OAuth access token. |

  #### Return Value

  An AuthCredential containing the GitHub credentials.