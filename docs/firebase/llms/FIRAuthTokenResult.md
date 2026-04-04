# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult.md.txt

# FirebaseAuth Framework Reference

# FIRAuthTokenResult


    @interface FIRAuthTokenResult : NSObject

A data class containing the ID token JWT string and other properties associated with the
token including the decoded payload claims.
- `
  ``
  ``
  `

  ### [token](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult#/c:objc(cs)FIRAuthTokenResult(py)token)

  `
  `  
  Stores the JWT string of the ID token.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull token;

- `
  ``
  ``
  `

  ### [expirationDate](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult#/c:objc(cs)FIRAuthTokenResult(py)expirationDate)

  `
  `  
  Stores the ID token's expiration date.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSDate *_Nonnull expirationDate;

- `
  ``
  ``
  `

  ### [authDate](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult#/c:objc(cs)FIRAuthTokenResult(py)authDate)

  `
  `  
  Stores the ID token's authentication date.
  This is the date the user was signed in and NOT the date the token was refreshed.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSDate *_Nonnull authDate;

- `
  ``
  ``
  `

  ### [issuedAtDate](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult#/c:objc(cs)FIRAuthTokenResult(py)issuedAtDate)

  `
  `  
  Stores the date that the ID token was issued.
  This is the date last refreshed and NOT the last authentication date.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSDate *_Nonnull issuedAtDate;

- `
  ``
  ``
  `

  ### [signInProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult#/c:objc(cs)FIRAuthTokenResult(py)signInProvider)

  `
  `  
  Stores sign-in provider through which the token was obtained.
  This does not necessarily map to provider IDs.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull signInProvider;

- `
  ``
  ``
  `

  ### [signInSecondFactor](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult#/c:objc(cs)FIRAuthTokenResult(py)signInSecondFactor)

  `
  `  
  Stores sign-in second factor through which the token was obtained.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull signInSecondFactor;

- `
  ``
  ``
  `

  ### [claims](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult#/c:objc(cs)FIRAuthTokenResult(py)claims)

  `
  `  
  Stores the entire payload of claims found on the ID token. This includes the standard
  reserved claims as well as custom claims set by the developer via the Admin SDK.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSDictionary<NSString *, id> *_Nonnull claims;