# Source: https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProvider.md.txt

# FirebaseAppCheck Framework Reference

# FIRAppCheckProvider

    @protocol FIRAppCheckProvider <NSObject>

Defines the methods required to be implemented by a specific Firebase App Check
provider.
- `
  ``
  ``
  `

  ### [-getTokenWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProvider#/c:objc(pl)FIRAppCheckProvider(im)getTokenWithCompletion:)

  `
  `  
  Returns a new Firebase App Check token.  

  #### Declaration

  Objective-C  

      - (void)getTokenWithCompletion:(nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken.html *_Nullable,
                                                       NSError *_Nullable))handler;

  #### Parameters

  |-----------------|----------------------------------------------------------------------------------------|
  | ` `*handler*` ` | The completion handler. Make sure to call the handler with either a token or an error. |

- `
  ``
  ``
  `

  ### [-getLimitedUseTokenWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Protocols/FIRAppCheckProvider#/c:objc(pl)FIRAppCheckProvider(im)getLimitedUseTokenWithCompletion:)

  `
  `  
  Returns a new Firebase App Check token.
  When implementing this method for your custom provider, the token returned should be suitable
  for consumption in a limited-use scenario. If you do not implement this method, the
  getTokenWithCompletion will be invoked instead whenever a limited-use token is requested.  

  #### Declaration

  Objective-C  

      - (void)getLimitedUseTokenWithCompletion:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken.html *_Nullable, NSError *_Nullable))handler;

  #### Parameters

  |-----------------|----------------------------------------------------------------------------------------|
  | ` `*handler*` ` | The completion handler. Make sure to call the handler with either a token or an error. |