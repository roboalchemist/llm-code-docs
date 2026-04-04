# Source: https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken.md.txt

# FirebaseAppCheck Framework Reference

# FIRAppCheckToken


    @interface FIRAppCheckToken : NSObject

An object representing a Firebase App Check token.
- `
  ``
  ``
  `

  ### [token](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken#/c:objc(cs)FIRAppCheckToken(py)token)

  `
  `  
  A Firebase App Check token.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull token;

- `
  ``
  ``
  `

  ### [expirationDate](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken#/c:objc(cs)FIRAppCheckToken(py)expirationDate)

  `
  `  
  The App Check token's expiration date in the device's local time.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSDate *_Nonnull expirationDate;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken#/c:objc(cs)FIRAppCheckToken(im)init)

  `
  `  
  Unavailable  
  Undocumented  

  #### Declaration

  Objective-C  

      - (instancetype)init NS_UNAVAILABLE;

- `
  ``
  ``
  `

  ### [-initWithToken:expirationDate:](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Classes/FIRAppCheckToken#/c:objc(cs)FIRAppCheckToken(im)initWithToken:expirationDate:)

  `
  `  
  The default initializer.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithToken:(nonnull NSString *)token
                             expirationDate:(nonnull NSDate *)expirationDate;

  #### Parameters

  |------------------------|----------------------------------------------------------------------|
  | ` `*token*` `          | A Firebase App Check token.                                          |
  | ` `*expirationDate*` ` | A Firebase App Check token expiration date in the device local time. |