# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols.md.txt

# FirebaseAuth Framework Reference

# Protocols

The following protocols are available globally.
- `


  ### [FederatedAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider)


  ` Utility type for constructing federated auth provider credentials.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRFederatedAuthProvider)
      public protocol FederatedAuthProvider : NSObjectProtocol

- `


  ### [UserInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo)


  ` Represents user data returned from an identity provider.

  #### Declaration

  Swift

      @objc(FIRUserInfo)
      public protocol UserInfo : NSObjectProtocol

- `


  ### [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate)


  ` A protocol to handle user interface interactions for Firebase Auth.

  This protocol is available on iOS, macOS Catalyst, and tvOS only.

  #### Declaration

  Swift

      @objc(FIRAuthUIDelegate)
      public protocol AuthUIDelegate : NSObjectProtocol