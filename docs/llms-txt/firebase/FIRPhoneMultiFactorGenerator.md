# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneMultiFactorGenerator.md.txt

# FirebaseAuth Framework Reference

# FIRPhoneMultiFactorGenerator


    @interface FIRPhoneMultiFactorGenerator : NSObject

The data structure used to help initialize an assertion for a second factor entity to the
Firebase Auth/CICP server. Depending on the type of second factor, this will help generate
the assertion.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [+assertionWithCredential:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneMultiFactorGenerator#/c:objc(cs)FIRPhoneMultiFactorGenerator(cm)assertionWithCredential:)

  `
  `  
  Initializes the MFA assertion to confirm ownership of the phone second factor. Note that
  this API is used for both enrolling and signing in with a phone second factor.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRPhoneMultiFactorAssertion *)assertionWithCredential:
          (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthCredential.html *)phoneAuthCredential;

  #### Parameters

  |-----------------------------|--------------------------------------------------------|
  | ` `*phoneAuthCredential*` ` | The phone auth credential used for multi factor flows. |