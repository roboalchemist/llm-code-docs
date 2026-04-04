# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPSecret.md.txt

# FirebaseAuth Framework Reference

# FIRTOTPSecret


    @interface FIRTOTPSecret : NSObject

- `
  ``
  ``
  `

  ### [-sharedSecretKey](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPSecret#/c:objc(cs)FIRTOTPSecret(im)sharedSecretKey)

  `
  `  
  Returns the shared secret key/seed used to generate time-based one-time passwords.  

  #### Declaration

  Objective-C  

      - (nonnull NSString *)sharedSecretKey;

- `
  ``
  ``
  `

  ### [-generateQRCodeURLWithAccountName:issuer:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPSecret#/c:objc(cs)FIRTOTPSecret(im)generateQRCodeURLWithAccountName:issuer:)

  `
  `  
  Returns a QRCode URL as described in
  <https://github.com/google/google-authenticator/wiki/Key-Uri-Format>
  This can be displayed to the user as a QRCode to be scanned into a TOTP app like Google
  Authenticator.  

  #### Declaration

  Objective-C  

      - (nonnull NSString *)
          generateQRCodeURLWithAccountName:(nonnull NSString *)accountName
                                    issuer:(nonnull NSString *)issuer;

  #### Parameters

  |---------------------|-----------------------------------------------------------------------|
  | ` `*accountName*` ` | the name of the account/app.                                          |
  | ` `*issuer*` `      | issuer of the TOTP(likely the app name). Returns A QRCode URL string. |

- `
  ``
  ``
  `

  ### [-openInOTPAppWithQRCodeURL:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPSecret#/c:objc(cs)FIRTOTPSecret(im)openInOTPAppWithQRCodeURL:)

  `
  `  
  Opens the specified QR Code URL in a password manager like iCloud Keychain.  
  See
  See more details here: <https://developer.apple.com/documentation/authenticationservices/securing_logins_with_icloud_keychain_verification_codes>  

  #### Declaration

  Objective-C  

      - (void)openInOTPAppWithQRCodeURL:(nonnull NSString *)QRCodeURL;