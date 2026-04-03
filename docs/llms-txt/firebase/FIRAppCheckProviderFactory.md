# Source: https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProviderFactory.md.txt

# FirebaseAppCheck Framework Reference

# FIRAppCheckProviderFactory

    @protocol FIRAppCheckProviderFactory <NSObject>

This protocol defines the interface for classes that can create Firebase App Check providers.
- `
  ``
  ``
  `

  ### [-createProviderWithApp:](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProviderFactory#/c:objc(pl)FIRAppCheckProviderFactory(im)createProviderWithApp:)

  `
  `  
  Creates a new instance of a Firebase App Check provider.  

  #### Declaration

  Objective-C  

      - (nullable id<https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProvider.html>)createProviderWithApp:(nonnull FIRApp *)app;

  #### Parameters

  |-------------|----------------------------------------------------------|
  | ` `*app*` ` | An instance of `FirebaseApp` to create the provider for. |

  #### Return Value

  A new instance implementing `AppCheckProvider` protocol.