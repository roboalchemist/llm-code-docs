# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory.md.txt

# FirebaseAppCheck Framework Reference

# AppCheckProviderFactory

    protocol AppCheckProviderFactory : NSObjectProtocol

This protocol defines the interface for classes that can create Firebase App Check providers.
- `


  ### [createProvider(with:)](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory#/c:objc(pl)FIRAppCheckProviderFactory(im)createProviderWithApp:)


  ` Creates a new instance of a Firebase App Check provider.

  #### Declaration

  Swift

      func createProvider(with app: FIRApp) -> (any https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider.html)?

  #### Parameters

  |---|---|
  | ` app ` | An instance of `FirebaseApp` to create the provider for. |

  #### Return Value

  A new instance implementing `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider.html` protocol.