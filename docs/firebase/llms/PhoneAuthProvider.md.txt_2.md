# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider.md.txt

# FirebaseAuth Framework Reference

# PhoneAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRPhoneAuthProvider)
    open class PhoneAuthProvider : NSObject, @unchecked Sendable

A concrete implementation of `AuthProvider` for phone auth providers.

This class is available on iOS only.
- `


  ### [id](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRPhoneAuthProvider(cpy)id)


  ` A string constant identifying the phone identity provider.

  #### Declaration

  Swift

      @objc
      public static let id: String

- `


  ### [provider()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRPhoneAuthProvider(cm)provider)


  ` Returns an instance of `PhoneAuthProvider` for the default `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html` object.

  #### Declaration

  Swift

      @objc(provider)
      open class func provider() -> PhoneAuthProvider

- `


  ### [provider(auth:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRPhoneAuthProvider(cm)providerWithAuth:)


  ` Returns an instance of `PhoneAuthProvider` for the provided `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html` object.

  #### Declaration

  Swift

      @objc(providerWithAuth:)
      open class func provider(auth: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html) -> PhoneAuthProvider

  #### Parameters

  |---|---|
  | ` auth ` | The auth object to associate with the phone auth provider instance. |

- `


  ### [verifyPhoneNumber(_:uiDelegate:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRPhoneAuthProvider(im)verifyPhoneNumber:UIDelegate:completion:)


  ` Starts the phone number authentication flow by sending a verification code to the
  specified phone number.

  Possible error codes:
  - `AuthErrorCodeCaptchaCheckFailed` - Indicates that the reCAPTCHA token obtained by the Firebase Auth is invalid or has expired.
  - `AuthErrorCodeQuotaExceeded` - Indicates that the phone verification quota for this project has been exceeded.
  - `AuthErrorCodeInvalidPhoneNumber` - Indicates that the phone number provided is invalid.
  - `AuthErrorCodeMissingPhoneNumber` - Indicates that a phone number was not provided.

  #### Declaration

  Swift

      @objc(verifyPhoneNumber:UIDelegate:completion:)
      open func verifyPhoneNumber(_ phoneNumber: String,
                                  uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html? = nil,
                                  completion: (@MainActor (String?, Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` phoneNumber ` | The phone number to be verified. |
  | ` uiDelegate ` | An object used to present the SFSafariViewController. The object is retained by this method until the completion block is executed. |
  | ` completion ` | The callback to be invoked when the verification flow is finished. |

- `


  ### [verifyPhoneNumber(_:uiDelegate:multiFactorSession:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRPhoneAuthProvider(im)verifyPhoneNumber:UIDelegate:multiFactorSession:completion:)


  ` Verify ownership of the second factor phone number by the current user.

  #### Declaration

  Swift

      @objc(verifyPhoneNumber:UIDelegate:multiFactorSession:completion:)
      open func verifyPhoneNumber(_ phoneNumber: String,
                                  uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html? = nil,
                                  multiFactorSession: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession? = nil,
                                  completion: (@MainActor (String?, Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` phoneNumber ` | The phone number to be verified. |
  | ` uiDelegate ` | An object used to present the SFSafariViewController. The object is retained by this method until the completion block is executed. |
  | ` multiFactorSession ` | A session to identify the MFA flow. For enrollment, this identifies the user trying to enroll. For sign-in, this identifies that the user already passed the first factor challenge. |
  | ` completion ` | The callback to be invoked when the verification flow is finished. |

- `


  ### [verifyPhoneNumber(_:uiDelegate:multiFactorSession:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/s:12FirebaseAuth05PhoneB8ProviderC06verifyC6Number_10uiDelegate18multiFactorSessionS2S_AA0B10UIDelegate_pSgAA05MultijK0CSgtYaKF)


  ` Verify ownership of the second factor phone number by the current user.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 8, *)
      open func verifyPhoneNumber(_ phoneNumber: String,
                                  uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html? = nil,
                                  multiFactorSession: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession? = nil) async throws
        -> String

  #### Parameters

  |---|---|
  | ` phoneNumber ` | The phone number to be verified. |
  | ` uiDelegate ` | An object used to present the SFSafariViewController. The object is retained by this method until the completion block is executed. |
  | ` multiFactorSession ` | A session to identify the MFA flow. For enrollment, this identifies the user trying to enroll. For sign-in, this identifies that the user already passed the first factor challenge. |

  #### Return Value

  The verification ID
- `


  ### [verifyPhoneNumber(with:uiDelegate:multiFactorSession:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRPhoneAuthProvider(im)verifyPhoneNumberWithMultiFactorInfo:UIDelegate:multiFactorSession:completion:)


  ` Verify ownership of the second factor phone number by the current user.

  #### Declaration

  Swift

      @objc(verifyPhoneNumberWithMultiFactorInfo:UIDelegate:multiFactorSession:completion:)
      open func verifyPhoneNumber(with multiFactorInfo: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo.html,
                                  uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html? = nil,
                                  multiFactorSession: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession?,
                                  completion: ((String?, Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` multiFactorInfo ` | The phone multi factor whose number need to be verified. |
  | ` uiDelegate ` | An object used to present the SFSafariViewController. The object is retained by this method until the completion block is executed. |
  | ` multiFactorSession ` | A session to identify the MFA flow. For enrollment, this identifies the user trying to enroll. For sign-in, this identifies that the user already passed the first factor challenge. |
  | ` completion ` | The callback to be invoked when the verification flow is finished. |

- `


  ### [verifyPhoneNumber(with:uiDelegate:multiFactorSession:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/s:12FirebaseAuth05PhoneB8ProviderC06verifyC6Number4with10uiDelegate18multiFactorSessionSSAA0c5MultiK4InfoC_AA0B10UIDelegate_pSgAA0mkL0CSgtYaKF)


  ` Verify ownership of the second factor phone number by the current user.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 8, *)
      open func verifyPhoneNumber(with multiFactorInfo: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo.html,
                                  uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html? = nil,
                                  multiFactorSession: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.html#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession?) async throws -> String

  #### Parameters

  |---|---|
  | ` multiFactorInfo ` | The phone multi factor whose number need to be verified. |
  | ` uiDelegate ` | An object used to present the SFSafariViewController. The object is retained by this method until the completion block is executed. |
  | ` multiFactorSession ` | A session to identify the MFA flow. For enrollment, this identifies the user trying to enroll. For sign-in, this identifies that the user already passed the first factor challenge. |

  #### Return Value

  The verification ID.
- `


  ### [credential(withVerificationID:verificationCode:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIRPhoneAuthProvider(im)credentialWithVerificationID:verificationCode:)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` for the phone number provider identified by the
  verification ID and verification code.

  #### Declaration

  Swift

      @objc(credentialWithVerificationID:verificationCode:)
      open func credential(withVerificationID verificationID: String,
                           verificationCode: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthCredential.html

  #### Parameters

  |---|---|
  | ` verificationID ` | The verification ID obtained from invoking verifyPhoneNumber:completion: |
  | ` verificationCode ` | The verification code obtained from the user. |

  #### Return Value

  The corresponding phone auth credential for the verification ID and verification
  code provided.