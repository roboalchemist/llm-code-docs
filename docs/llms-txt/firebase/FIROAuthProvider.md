# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIROAuthProvider


    @interface FIROAuthProvider : NSObject <https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRFederatedAuthProvider.html>

A concrete implementation of `AuthProvider` for generic OAuth Providers.
- `
  ``
  ``
  `

  ### [scopes](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(py)scopes)

  `
  `  
  Array used to configure the OAuth scopes.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSArray<NSString *> *scopes;

- `
  ``
  ``
  `

  ### [customParameters](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(py)customParameters)

  `
  `  
  Dictionary used to configure the OAuth custom parameters.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSDictionary<NSString *, NSString *> *customParameters;

- `
  ``
  ``
  `

  ### [providerID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(py)providerID)

  `
  `  
  The provider ID indicating the specific OAuth provider this OAuthProvider instance
  represents.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull providerID;

- `
  ``
  ``
  `

  ### [+providerWithProviderID:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(cm)providerWithProviderID:)

  `
  `  

  #### Declaration

  Objective-C  

      + (nonnull FIROAuthProvider *)providerWithProviderID:
          (nonnull NSString *)providerID;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------|
  | ` `*providerID*` ` | The provider ID of the IDP for which this auth provider instance will be configured. |

  #### Return Value

  An instance of `OAuthProvider` corresponding to the specified provider ID.
- `
  ``
  ``
  `

  ### [+providerWithProviderID:auth:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(cm)providerWithProviderID:auth:)

  `
  `  

  #### Declaration

  Objective-C  

      + (nonnull FIROAuthProvider *)providerWithProviderID:
                                        (nonnull NSString *)providerID
                                                      auth:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth.html *)auth;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------|
  | ` `*providerID*` ` | The provider ID of the IDP for which this auth provider instance will be configured. |
  | ` `*auth*` `       | The auth instance to be associated with the `OAuthProvider` instance.                |

  #### Return Value

  An instance of `OAuthProvider` corresponding to the specified provider ID.
- `
  ``
  ``
  `

  ### [+credentialWithProviderID:IDToken:accessToken:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(cm)credentialWithProviderID:IDToken:accessToken:)

  `
  `  
  Creates an `AuthCredential` for the OAuth 2 provider identified by provider ID, ID
  token, and access token.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential.html *)
          credentialWithProviderID:(nonnull NSString *)providerID
                           IDToken:(nonnull NSString *)IDToken
                       accessToken:(nullable NSString *)accessToken;

  #### Parameters

  |---------------------|--------------------------------------------------------------------------------|
  | ` `*providerID*` `  | The provider ID associated with the Auth credential being created.             |
  | ` `*IDToken*` `     | The IDToken associated with the Auth credential being created.                 |
  | ` `*accessToken*` ` | The access token associated with the Auth credential be created, if available. |

  #### Return Value

  A `AuthCredential` for the specified provider ID, ID token and access token.
- `
  ``
  ``
  `

  ### [+credentialWithProviderID:accessToken:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(cm)credentialWithProviderID:accessToken:)

  `
  `  
  Creates an `AuthCredential` for the OAuth 2 provider identified by provider ID using
  an ID token.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential.html *)
          credentialWithProviderID:(nonnull NSString *)providerID
                       accessToken:(nonnull NSString *)accessToken;

  #### Parameters

  |---------------------|--------------------------------------------------------------------|
  | ` `*providerID*` `  | The provider ID associated with the Auth credential being created. |
  | ` `*accessToken*` ` | The access token associated with the Auth credential be created    |

  #### Return Value

  An `AuthCredential`.
- `
  ``
  ``
  `

  ### [+credentialWithProviderID:IDToken:rawNonce:accessToken:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(cm)credentialWithProviderID:IDToken:rawNonce:accessToken:)

  `
  `  
  Creates an `AuthCredential` for that OAuth 2 provider identified by provider ID, ID
  token, raw nonce, and access token.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential.html *)
          credentialWithProviderID:(nonnull NSString *)providerID
                           IDToken:(nonnull NSString *)IDToken
                          rawNonce:(nullable NSString *)rawNonce
                       accessToken:(nullable NSString *)accessToken;

  #### Parameters

  |---------------------|--------------------------------------------------------------------------------|
  | ` `*providerID*` `  | The provider ID associated with the Auth credential being created.             |
  | ` `*IDToken*` `     | The IDToken associated with the Auth credential being created.                 |
  | ` `*rawNonce*` `    | The raw nonce associated with the Auth credential being created.               |
  | ` `*accessToken*` ` | The access token associated with the Auth credential be created, if available. |

  #### Return Value

  A `AuthCredential` for the specified provider ID, ID token and access token.
- `
  ``
  ``
  `

  ### [+credentialWithProviderID:IDToken:rawNonce:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(cm)credentialWithProviderID:IDToken:rawNonce:)

  `
  `  
  Creates an `AuthCredential` for that OAuth 2 provider identified by providerID using
  an ID token and raw nonce.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential.html *)
          credentialWithProviderID:(nonnull NSString *)providerID
                           IDToken:(nonnull NSString *)IDToken
                          rawNonce:(nullable NSString *)rawNonce;

  #### Parameters

  |--------------------|--------------------------------------------------------------------|
  | ` `*providerID*` ` | The provider ID associated with the Auth credential being created. |
  | ` `*IDToken*` `    | The IDToken associated with the Auth credential being created.     |
  | ` `*rawNonce*` `   | The raw nonce associated with the Auth credential being created.   |

  #### Return Value

  A `AuthCredential`.
- `
  ``
  ``
  `

  ### [+appleCredentialWithIDToken:rawNonce:fullName:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(cm)appleCredentialWithIDToken:rawNonce:fullName:)

  `
  `  
  Creates an `AuthCredential` for the Sign in with Apple OAuth 2 provider identified by ID
  token, raw nonce, and full name. This method is specific to the Sign in with Apple OAuth 2
  provider as this provider requires the full name to be passed explicitly.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential.html *)
          appleCredentialWithIDToken:(nonnull NSString *)IDToken
                            rawNonce:(nullable NSString *)rawNonce
                            fullName:(nullable NSPersonNameComponents *)fullName;

  #### Parameters

  |------------------|-------------------------------------------------------------------------------------|
  | ` `*IDToken*` `  | The IDToken associated with the Sign in with Apple Auth credential being created.   |
  | ` `*rawNonce*` ` | The raw nonce associated with the Sign in with Apple Auth credential being created. |
  | ` `*fullName*` ` | The full name associated with the Sign in with Apple Auth credential being created. |

  #### Return Value

  An `AuthCredential`.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider#/c:objc(cs)FIROAuthProvider(im)init)

  `
  `  
  This class is not meant to be initialized.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;