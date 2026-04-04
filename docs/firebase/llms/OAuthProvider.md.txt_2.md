# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider.md.txt

# FirebaseAuth Framework Reference

# OAuthProvider

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIROAuthProvider)
    open class OAuthProvider : NSObject, https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider.html

Utility class for constructing OAuth Sign In credentials.
- `


  ### [id](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIROAuthProvider(cpy)id)


  ` Undocumented

  #### Declaration

  Swift

      @objc
      public static let id: String

- `


  ### [scopes](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIROAuthProvider(py)scopes)


  ` Array used to configure the OAuth scopes.

  #### Declaration

  Swift

      @objc
      open var scopes: [String]?

- `


  ### [customParameters](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIROAuthProvider(py)customParameters)


  ` Dictionary used to configure the OAuth custom parameters.

  #### Declaration

  Swift

      @objc
      open var customParameters: [String : String]?

- `


  ### [providerID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIROAuthProvider(py)providerID)


  ` The provider ID indicating the specific OAuth provider this OAuthProvider instance represents.

  #### Declaration

  Swift

      @objc
      public let providerID: String

- `


  ### [provider(providerID:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/s:12FirebaseAuth13OAuthProviderC8provider0E2IDAcA0bdF0V_tFZ)


  ` An instance of OAuthProvider corresponding to the given provider ID.

  #### Declaration

  Swift

      public class func provider(providerID: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Structs/AuthProviderID.html) -> OAuthProvider

  #### Parameters

  |---|---|
  | ` providerID ` | The provider ID of the IDP for which this auth provider instance will be configured. |

  #### Return Value

  An instance of OAuthProvider corresponding to the specified provider ID.
- `


  ### [provider(providerID:auth:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/s:12FirebaseAuth13OAuthProviderC8provider0E2ID4authAcA0bdF0V_AA0B0CtFZ)


  ` An instance of OAuthProvider corresponding to the given provider ID and auth instance.

  #### Declaration

  Swift

      public class func provider(providerID: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Structs/AuthProviderID.html, auth: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html) -> OAuthProvider

  #### Parameters

  |---|---|
  | ` providerID ` | The provider ID of the IDP for which this auth provider instance will be configured. |
  | ` auth ` | The auth instance to be associated with the OAuthProvider instance. |

  #### Return Value

  An instance of OAuthProvider corresponding to the specified provider ID.
- `


  ### [init(providerID:auth:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/s:12FirebaseAuth13OAuthProviderC10providerID4authACSS_AA0B0Ctcfc)


  ` Initializes an `OAuthProvider`.

  #### Declaration

  Swift

      public init(providerID: String, auth: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html = https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html.auth())

  #### Parameters

  |---|---|
  | ` providerID ` | The provider ID of the IDP for which this auth provider instance will be configured. |
  | ` auth ` | The auth instance to be associated with the OAuthProvider instance. |

- `


  ### [init(providerID:auth:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/s:12FirebaseAuth13OAuthProviderC10providerID4authAcA0bdF0V_AA0B0Ctcfc)


  ` Initializes an `OAuthProvider`.

  #### Declaration

  Swift

      public convenience init(providerID: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Structs/AuthProviderID.html, auth: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html = https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html.auth())

  #### Parameters

  |---|---|
  | ` providerID ` | The provider ID of the IDP for which this auth provider instance will be configured. |
  | ` auth ` | The auth instance to be associated with the OAuthProvider instance. |

- `


  ### [credential(providerID:idToken:accessToken:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/s:12FirebaseAuth13OAuthProviderC10credential10providerID7idToken06accessI0AA0C10CredentialCAA0bdG0V_S2SSgtFZ)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` for the OAuth 2 provider identified by provider ID, ID
  token, and access token.

  #### Declaration

  Swift

      public static func credential(providerID: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Structs/AuthProviderID.html,
                                    idToken: String,
                                    accessToken: String? = nil) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential.html

  #### Parameters

  |---|---|
  | ` providerID ` | The provider ID associated with the Auth credential being created. |
  | ` idToken ` | The IDToken associated with the Auth credential being created. |
  | ` accessToken ` | The access token associated with the Auth credential be created, if available. |

  #### Return Value

  An AuthCredential for the specified provider ID, ID token and access token.
- `


  ### [credential(providerID:accessToken:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/s:12FirebaseAuth13OAuthProviderC10credential10providerID11accessTokenAA0C10CredentialCAA0bdG0V_SStFZ)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` for the OAuth 2 provider identified by provider ID using
  an ID token.

  #### Declaration

  Swift

      public static func credential(providerID: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Structs/AuthProviderID.html,
                                    accessToken: String) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential.html

  #### Parameters

  |---|---|
  | ` providerID ` | The provider ID associated with the Auth credential being created. |
  | ` accessToken ` | The access token associated with the Auth credential be created |

  #### Return Value

  An AuthCredential.
- `


  ### [credential(providerID:idToken:rawNonce:accessToken:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/s:12FirebaseAuth13OAuthProviderC10credential10providerID7idToken8rawNonce06accessI0AA0C10CredentialCAA0bdG0V_S3SSgtFZ)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` for that OAuth 2 provider identified by provider ID, ID
  token, raw nonce, and access token.

  #### Declaration

  Swift

      public static func credential(providerID: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Structs/AuthProviderID.html, idToken: String,
                                    rawNonce: String,
                                    accessToken: String? = nil) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential.html

  #### Parameters

  |---|---|
  | ` providerID ` | The provider ID associated with the Auth credential being created. |
  | ` idToken ` | The IDToken associated with the Auth credential being created. |
  | ` rawNonce ` | The raw nonce associated with the Auth credential being created. |
  | ` accessToken ` | The access token associated with the Auth credential be created, if available. |

  #### Return Value

  An AuthCredential for the specified provider ID, ID token and access token.
- `


  ### [getCredentialWith(_:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/s:12FirebaseAuth13OAuthProviderC17getCredentialWith_10completionyAA0B10UIDelegate_pSg_yAA0bF0CSg_s5Error_pSgtcSgtF)


  ` Used to obtain an auth credential via a mobile web flow.

  This method is available on iOS only.

  #### Declaration

  Swift

      open func getCredentialWith(_ uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?,
                                  completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html?, Error?) -> Void)? = nil)

  #### Parameters

  |---|---|
  | ` uiDelegate ` | An optional UI delegate used to present the mobile web flow. |
  | ` completion ` | Optionally; a block which is invoked asynchronously on the main thread when the mobile web flow is completed. |

- `


  ### [credential(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIROAuthProvider(im)getCredentialWithUIDelegate:completion:)


  ` Used to obtain an auth credential via a mobile web flow.
  This method is available on iOS only.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 8, *)
      @objc(getCredentialWithUIDelegate:completion:)
      @MainActor
      open func credential(with uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html

  #### Parameters

  |---|---|
  | ` uiDelegate ` | An optional UI delegate used to present the mobile web flow. |
  | ` completionHandler ` | Optionally; a block which is invoked asynchronously on the main thread when the mobile web flow is completed. |

- `


  ### [appleCredential(withIDToken:rawNonce:fullName:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider#/c:@M@FirebaseAuth@objc(cs)FIROAuthProvider(cm)appleCredentialWithIDToken:rawNonce:fullName:)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html` for the Sign in with Apple OAuth 2 provider identified by ID
  token, raw nonce, and full name.This method is specific to the Sign in with Apple OAuth 2
  provider as this provider requires the full name to be passed explicitly.

  #### Declaration

  Swift

      @objc(appleCredentialWithIDToken:rawNonce:fullName:)
      public static func appleCredential(withIDToken idToken: String,
                                         rawNonce: String?,
                                         fullName: PersonNameComponents?) -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential.html

  #### Parameters

  |---|---|
  | ` idToken ` | The IDToken associated with the Sign in with Apple Auth credential being created. |
  | ` rawNonce ` | The raw nonce associated with the Sign in with Apple Auth credential being created. |
  | ` fullName ` | The full name associated with the Sign in with Apple Auth credential being created. |

  #### Return Value

  An AuthCredential.