# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPSecret.md.txt

# FirebaseAuth Framework Reference

# TOTPSecret

    @objc(FIRTOTPSecret)
    open class TOTPSecret : NSObject

The subclass of base class MultiFactorAssertion, used to assert ownership of a TOTP
(Time-based One Time Password) second factor.

This class is available on iOS and macOS.
- `
  ``
  ``
  `

  ### [sharedSecretKey()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPSecret#/c:@M@FirebaseAuth@objc(cs)FIRTOTPSecret(im)sharedSecretKey)

  `
  `  
  Returns the shared secret key/seed used to generate time-based one-time passwords.  

  #### Declaration

  Swift  

      @objc
      open func sharedSecretKey() -> String

- `
  ``
  ``
  `

  ### [generateQRCodeURL(withAccountName:issuer:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPSecret#/c:@M@FirebaseAuth@objc(cs)FIRTOTPSecret(im)generateQRCodeURLWithAccountName:issuer:)

  `
  `  
  Returns a QRCode URL as described in
  <https://github.com/google/google-authenticator/wiki/Key-Uri-Format>.

  This can be displayed to the user as a QRCode to be scanned into a TOTP app like Google
  Authenticator.  

  #### Declaration

  Swift  

      @objc(generateQRCodeURLWithAccountName:issuer:)
      open func generateQRCodeURL(withAccountName accountName: String,
                                  issuer: String) -> String

  #### Parameters

  |---------------------|------------------------------------------|
  | ` `*accountName*` ` | The name of the account/app.             |
  | ` `*issuer*` `      | Issuer of the TOTP(likely the app name). |

  #### Return Value

  A QRCode URL string.
- `
  ``
  ``
  `

  ### [openInOTPApp(withQRCodeURL:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPSecret#/c:@M@FirebaseAuth@objc(cs)FIRTOTPSecret(im)openInOTPAppWithQRCodeURL:)

  `
  `  
  Opens the specified QR Code URL in a password manager like iCloud Keychain.

  See more details
  [here](https://developer.apple.com/documentation/authenticationservices/securing_logins_with_icloud_keychain_verification_codes)  

  #### Declaration

  Swift  

      @MainActor
      @objc(openInOTPAppWithQRCodeURL:)
      open func openInOTPApp(withQRCodeURL qrCodeURL: String)