# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo.md.txt

# FirebaseAuth Framework Reference

# FIRUserInfo

    @protocol FIRUserInfo <NSObject>

Represents user data returned from an identity provider.
- `
  ``
  ``
  `

  ### [providerID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo#/c:objc(pl)FIRUserInfo(py)providerID)

  `
  `  
  The provider identifier.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull providerID;

- `
  ``
  ``
  `

  ### [uid](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo#/c:objc(pl)FIRUserInfo(py)uid)

  `
  `  
  The provider's user ID for the user.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull uid;

- `
  ``
  ``
  `

  ### [displayName](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo#/c:objc(pl)FIRUserInfo(py)displayName)

  `
  `  
  The name of the user.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *displayName;

- `
  ``
  ``
  `

  ### [photoURL](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo#/c:objc(pl)FIRUserInfo(py)photoURL)

  `
  `  
  The URL of the user's profile photo.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSURL *photoURL;

- `
  ``
  ``
  `

  ### [email](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo#/c:objc(pl)FIRUserInfo(py)email)

  `
  `  
  The user's email address.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *email;

- `
  ``
  ``
  `

  ### [phoneNumber](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo#/c:objc(pl)FIRUserInfo(py)phoneNumber)

  `
  `  
  A phone number associated with the user.
  This property is only available for users authenticated via phone number auth.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *phoneNumber;