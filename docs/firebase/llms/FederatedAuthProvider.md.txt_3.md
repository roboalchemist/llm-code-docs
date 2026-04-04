# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FederatedAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRFederatedAuthProvider)
    public protocol FederatedAuthProvider : NSObjectProtocol

Utility type for constructing federated auth provider credentials.
- `


  ### [credential(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider#/c:@M@FirebaseAuth@objc(pl)FIRFederatedAuthProvider(im)getCredentialWithUIDelegate:completion:)


  ` Used to obtain an auth credential via a mobile web flow.
  This method is available on iOS only.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 8, *)
      @objc(getCredentialWithUIDelegate:completion:)
      func credential(with uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html

  #### Parameters

  |---|---|
  | ` uiDelegate ` | An optional UI delegate used to present the mobile web flow. |
  | ` completionHandler ` | Optionally; a block which is invoked asynchronously on the main thread when the mobile web flow is completed. |