# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider.md.txt

# FirebaseAppCheck Framework Reference

# AppCheckProvider

    protocol AppCheckProvider : NSObjectProtocol

Defines the methods required to be implemented by a specific Firebase App Check
provider.
- `


  ### [getToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider#/c:objc(pl)FIRAppCheckProvider(im)getTokenWithCompletion:)


  ` Returns a new Firebase App Check token.

  #### Declaration

  Swift

      func getToken() async throws -> FIRAppCheckToken

  #### Parameters

  |---|---|
  | ` handler ` | The completion handler. Make sure to call the handler with either a token or an error. |

- `


  ### [getLimitedUseToken()](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider#/c:objc(pl)FIRAppCheckProvider(im)getLimitedUseTokenWithCompletion:)


  ` Returns a new Firebase App Check token.
  When implementing this method for your custom provider, the token returned should be suitable
  for consumption in a limited-use scenario. If you do not implement this method, the
  getTokenWithCompletion will be invoked instead whenever a limited-use token is requested.

  #### Declaration

  Swift

      optional func getLimitedUseToken() async throws -> FIRAppCheckToken

  #### Parameters

  |---|---|
  | ` handler ` | The completion handler. Make sure to call the handler with either a token or an error. |