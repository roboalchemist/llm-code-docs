# Source: https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Classes/FIRInstallationsAuthTokenResult.md.txt

# FirebaseInstallations Framework Reference

# FIRInstallationsAuthTokenResult


    @interface FIRInstallationsAuthTokenResult : NSObject

The class represents a result of the installation auth token request.
- `
  ``
  ``
  `

  ### [authToken](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Classes/FIRInstallationsAuthTokenResult#/c:objc(cs)FIRInstallationsAuthTokenResult(py)authToken)

  `
  `  
  The installation auth token string.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull authToken;

- `
  ``
  ``
  `

  ### [expirationDate](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Classes/FIRInstallationsAuthTokenResult#/c:objc(cs)FIRInstallationsAuthTokenResult(py)expirationDate)

  `
  `  
  The installation auth token expiration date.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSDate *_Nonnull expirationDate;