# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPMultiFactorGenerator.md.txt

# FirebaseAuth Framework Reference

# TOTPMultiFactorGenerator

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRTOTPMultiFactorGenerator)
    open class TOTPMultiFactorGenerator : NSObject

The data structure used to help initialize an assertion for a second factor entity to the
Firebase Auth/CICP server. Depending on the type of second factor, this will help generate
the assertion.

This class is available on iOS and macOS.
- `
  ``
  ``
  `

  ### [generateSecret(with:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPMultiFactorGenerator#/c:@M@FirebaseAuth@objc(cs)FIRTOTPMultiFactorGenerator(cm)generateSecretWithMultiFactorSession:completion:)

  `
  `  
  Creates a TOTP secret as part of enrolling a TOTP second factor. Used for generating a
  QR code URL or inputting into a TOTP app. This method uses the auth instance corresponding
  to the user in the multiFactorSession.  

  #### Declaration

  Swift  

      @objc(generateSecretWithMultiFactorSession:completion:)
      open class func generateSecret(with session: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession,
                                     completion: @escaping (https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPSecret.html?, Error?) -> Void)

  #### Parameters

  |--------------------|----------------------------------|
  | ` `*session*` `    | The multiFactorSession instance. |
  | ` `*completion*` ` | Completion block                 |

- `
  ``
  ``
  `

  ### [generateSecret(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPMultiFactorGenerator#/s:12FirebaseAuth24TOTPMultiFactorGeneratorC14generateSecret4withAA10TOTPSecretCAA05MultiD7SessionC_tYaKFZ)

  `
  `  
  Creates a TOTP secret as part of enrolling a TOTP second factor.

  Used for generating a QR code URL or inputting into a TOTP app. This
  method uses the auth instance correspondingto the user in the multiFactorSession.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open class func generateSecret(with session: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPSecret.html

  #### Parameters

  |-----------------|----------------------------------|
  | ` `*session*` ` | The multiFactorSession instance. |

  #### Return Value

  The TOTP secret.
- `
  ``
  ``
  `

  ### [assertionForEnrollment(with:oneTimePassword:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPMultiFactorGenerator#/c:@M@FirebaseAuth@objc(cs)FIRTOTPMultiFactorGenerator(cm)assertionForEnrollmentWithSecret:oneTimePassword:)

  `
  `  
  Initializes the MFA assertion to confirm ownership of the TOTP second factor.

  This assertion is used to complete enrollment of TOTP as a second factor.  

  #### Declaration

  Swift  

      @objc(assertionForEnrollmentWithSecret:oneTimePassword:)
      open class func assertionForEnrollment(with secret: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPSecret.html,
                                             oneTimePassword: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRTOTPMultiFactorAssertion

  #### Parameters

  |-------------------------|---------------------------|
  | ` `*secret*` `          | The TOTP secret.          |
  | ` `*oneTimePassword*` ` | One time password string. |

  #### Return Value

  The MFA assertion.
- `
  ``
  ``
  `

  ### [assertionForSignIn(withEnrollmentID:oneTimePassword:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPMultiFactorGenerator#/c:@M@FirebaseAuth@objc(cs)FIRTOTPMultiFactorGenerator(cm)assertionForSignInWithEnrollmentID:oneTimePassword:)

  `
  `  
  Initializes the MFA assertion to confirm ownership of the TOTP second factor.

  This assertion is used to complete signIn with TOTP as a second factor.  

  #### Declaration

  Swift  

      @objc(assertionForSignInWithEnrollmentID:oneTimePassword:)
      open class func assertionForSignIn(withEnrollmentID enrollmentID: String,
                                         oneTimePassword: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRTOTPMultiFactorAssertion

  #### Parameters

  |-------------------------|---------------------------------------------------------|
  | ` `*enrollmentID*` `    | The ID that identifies the enrolled TOTP second factor. |
  | ` `*oneTimePassword*` ` | one time password string.                               |

  #### Return Value

  The MFA assertion.