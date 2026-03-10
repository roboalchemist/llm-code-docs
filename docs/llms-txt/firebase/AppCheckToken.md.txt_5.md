# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckToken.md.txt

# FirebaseAppCheck Framework Reference

# AppCheckToken

    class AppCheckToken : NSObject

An object representing a Firebase App Check token.
- `


  ### [token](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckToken#/c:objc(cs)FIRAppCheckToken(py)token)


  ` A Firebase App Check token.

  #### Declaration

  Swift

      var token: String { get }

- `


  ### [expirationDate](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckToken#/c:objc(cs)FIRAppCheckToken(py)expirationDate)


  ` The App Check token's expiration date in the device's local time.

  #### Declaration

  Swift

      var expirationDate: Date { get }

- `


  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckToken#/c:objc(cs)FIRAppCheckToken(im)init)


  ` Unavailable
  Undocumented
- `


  ### [init(token:expirationDate:)](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckToken#/c:objc(cs)FIRAppCheckToken(im)initWithToken:expirationDate:)


  ` The default initializer.

  #### Declaration

  Swift

      init(token: String, expirationDate: Date)

  #### Parameters

  |---|---|
  | ` token ` | A Firebase App Check token. |
  | ` expirationDate ` | A Firebase App Check token expiration date in the device local time. |