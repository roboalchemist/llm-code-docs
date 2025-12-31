# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPMultiFactorGenerator.md.txt

# FirebaseAuth Framework Reference

# FIRTOTPMultiFactorGenerator


    @interface FIRTOTPMultiFactorGenerator : NSObject

The data structure used to help initialize an assertion for a second factor entity to the
Firebase Auth/CICP server. Depending on the type of second factor, this will help generate
the assertion.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [+generateSecretWithMultiFactorSession:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPMultiFactorGenerator#/c:objc(cs)FIRTOTPMultiFactorGenerator(cm)generateSecretWithMultiFactorSession:completion:)

  `
  `  
  Creates a TOTP secret as part of enrolling a TOTP second factor. Used for generating a
  QR code URL or inputting into a TOTP app. This method uses the auth instance corresponding to the
  user in the multiFactorSession.  

  #### Declaration

  Objective-C  

      + (void)generateSecretWithMultiFactorSession:
                  (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRMultiFactorSession *)session
                                        completion:(nonnull void (^)(
                                                       https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPSecret.html *_Nullable,
                                                       NSError *_Nullable))completion;

  #### Parameters

  |--------------------|----------------------------------|
  | ` `*session*` `    | The multiFactorSession instance. |
  | ` `*completion*` ` | Completion block                 |

- `
  ``
  ``
  `

  ### [+assertionForEnrollmentWithSecret:oneTimePassword:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPMultiFactorGenerator#/c:objc(cs)FIRTOTPMultiFactorGenerator(cm)assertionForEnrollmentWithSecret:oneTimePassword:)

  `
  `  
  Initializes the MFA assertion to confirm ownership of the TOTP second factor. This assertion
  is used to complete enrollment of TOTP as a second factor.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRTOTPMultiFactorAssertion *)
          assertionForEnrollmentWithSecret:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPSecret.html *)secret
                           oneTimePassword:(nonnull NSString *)oneTimePassword;

  #### Parameters

  |-------------------------|---------------------------|
  | ` `*secret*` `          | The TOTP secret.          |
  | ` `*oneTimePassword*` ` | one time password string. |

- `
  ``
  ``
  `

  ### [+assertionForSignInWithEnrollmentID:oneTimePassword:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPMultiFactorGenerator#/c:objc(cs)FIRTOTPMultiFactorGenerator(cm)assertionForSignInWithEnrollmentID:oneTimePassword:)

  `
  `  
  Initializes the MFA assertion to confirm ownership of the TOTP second factor. This
  assertion is used to complete signIn with TOTP as a second factor.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRTOTPMultiFactorAssertion *)
          assertionForSignInWithEnrollmentID:(nonnull NSString *)enrollmentID
                             oneTimePassword:(nonnull NSString *)oneTimePassword;

  #### Parameters

  |-------------------------|---------------------------------------------------------|
  | ` `*enrollmentID*` `    | The ID that identifies the enrolled TOTP second factor. |
  | ` `*oneTimePassword*` ` | one time password string.                               |