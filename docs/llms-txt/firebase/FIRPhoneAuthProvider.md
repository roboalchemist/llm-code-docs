# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIRPhoneAuthProvider


    @interface FIRPhoneAuthProvider : NSObject

A concrete implementation of `AuthProvider` for phone auth providers.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [+provider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider#/c:objc(cs)FIRPhoneAuthProvider(cm)provider)

  `
  `  
  Returns an instance of `PhoneAuthProvider` for the default `Auth` object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)provider;

- `
  ``
  ``
  `

  ### [+providerWithAuth:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider#/c:objc(cs)FIRPhoneAuthProvider(cm)providerWithAuth:)

  `
  `  
  Returns an instance of `PhoneAuthProvider` for the provided `Auth` object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)providerWithAuth:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth.html *)auth;

  #### Parameters

  |--------------|---------------------------------------------------------------------|
  | ` `*auth*` ` | The auth object to associate with the phone auth provider instance. |

- `
  ``
  ``
  `

  ### [-verifyPhoneNumber:UIDelegate:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider#/c:objc(cs)FIRPhoneAuthProvider(im)verifyPhoneNumber:UIDelegate:completion:)

  `
  `  
  Starts the phone number authentication flow by sending a verification code to the
  specified phone number.  

  #### Declaration

  Objective-C  

      - (void)verifyPhoneNumber:(nonnull NSString *)phoneNumber
                     UIDelegate:(nullable id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate.html>)UIDelegate
                     completion:(nullable void (^)(NSString *_Nullable,
                                                   NSError *_Nullable))completion;

  #### Parameters

  |---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*phoneNumber*` ` | The phone number to be verified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | ` `*UIDelegate*` `  | An object used to present the SFSafariViewController. The object is retained by this method until the completion block is executed.                                                                                                                                                                                                                                                                                                                                                                                          |
  | ` `*completion*` `  | The callback to be invoked when the verification flow is finished. Possible error codes: - `AuthErrorCodeCaptchaCheckFailed` - Indicates that the reCAPTCHA token obtained by the Firebase Auth is invalid or has expired. - `AuthErrorCodeQuotaExceeded` - Indicates that the phone verification quota for this project has been exceeded. - `AuthErrorCodeInvalidPhoneNumber` - Indicates that the phone number provided is invalid. - `AuthErrorCodeMissingPhoneNumber` - Indicates that a phone number was not provided. |

- `
  ``
  ``
  `

  ### [-verifyPhoneNumber:UIDelegate:multiFactorSession:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider#/c:objc(cs)FIRPhoneAuthProvider(im)verifyPhoneNumber:UIDelegate:multiFactorSession:completion:)

  `
  `  
  Verify ownership of the second factor phone number by the current user.  

  #### Declaration

  Objective-C  

      - (void)verifyPhoneNumber:(nonnull NSString *)phoneNumber
                     UIDelegate:(nullable id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate.html>)UIDelegate
             multiFactorSession:(nullable https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRMultiFactorSession *)session
                     completion:(nullable void (^)(NSString *_Nullable,
                                                   NSError *_Nullable))completion;

  #### Parameters

  |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*phoneNumber*` ` | The phone number to be verified.                                                                                                                                                     |
  | ` `*UIDelegate*` `  | An object used to present the SFSafariViewController. The object is retained by this method until the completion block is executed.                                                  |
  | ` `*session*` `     | A session to identify the MFA flow. For enrollment, this identifies the user trying to enroll. For sign-in, this identifies that the user already passed the first factor challenge. |
  | ` `*completion*` `  | The callback to be invoked when the verification flow is finished.                                                                                                                   |

- `
  ``
  ``
  `

  ### [-verifyPhoneNumberWithMultiFactorInfo:UIDelegate:multiFactorSession:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider#/c:objc(cs)FIRPhoneAuthProvider(im)verifyPhoneNumberWithMultiFactorInfo:UIDelegate:multiFactorSession:completion:)

  `
  `  
  Verify ownership of the second factor phone number by the current user.  

  #### Declaration

  Objective-C  

      - (void)verifyPhoneNumberWithMultiFactorInfo:
                  (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneMultiFactorInfo.html *)phoneMultiFactorInfo
                                        UIDelegate:
                                            (nullable id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate.html>)UIDelegate
                                multiFactorSession:
                                    (nullable https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRMultiFactorSession *)session
                                        completion:(nullable void (^)(
                                                       NSString *_Nullable,
                                                       NSError *_Nullable))completion;

  #### Parameters

  |------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*phoneMultiFactorInfo*` ` | The phone multi factor whose number need to be verified.                                                                                                                             |
  | ` `*UIDelegate*` `           | An object used to present the SFSafariViewController. The object is retained by this method until the completion block is executed.                                                  |
  | ` `*session*` `              | A session to identify the MFA flow. For enrollment, this identifies the user trying to enroll. For sign-in, this identifies that the user already passed the first factor challenge. |
  | ` `*completion*` `           | The callback to be invoked when the verification flow is finished.                                                                                                                   |

- `
  ``
  ``
  `

  ### [-credentialWithVerificationID:verificationCode:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider#/c:objc(cs)FIRPhoneAuthProvider(im)credentialWithVerificationID:verificationCode:)

  `
  `  
  Creates an `AuthCredential` for the phone number provider identified by the
  verification ID and verification code.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthCredential.html *)
          credentialWithVerificationID:(nonnull NSString *)verificationID
                      verificationCode:(nonnull NSString *)verificationCode;

  #### Parameters

  |--------------------------|--------------------------------------------------------------------------|
  | ` `*verificationID*` `   | The verification ID obtained from invoking verifyPhoneNumber:completion: |
  | ` `*verificationCode*` ` | The verification code obtained from the user.                            |

  #### Return Value

  The corresponding phone auth credential for the verification ID and verification code
  provided.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider#/c:objc(cs)FIRPhoneAuthProvider(im)init)

  `
  `  
  Please use the `provider()` or `provider(auth:)` methods to obtain an instance of
  `PhoneAuthProvider`.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;