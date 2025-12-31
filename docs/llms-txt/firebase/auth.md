# Source: https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth.md.txt

# Source: https://firebase.google.com/docs/database/rest/auth.md.txt

# Source: https://firebase.google.com/docs/reference/rest/auth.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/auth.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth.md.txt

# Source: https://firebase.google.com/docs/cli/auth.md.txt

# Source: https://firebase.google.com/docs/auth.md.txt

# Source: https://firebase.google.com/docs/reference/js/auth.md.txt

# Source: https://firebase.google.com/docs/cli/auth.md.txt

# Source: https://firebase.google.com/docs/auth.md.txt

# Source: https://firebase.google.com/docs/reference/js/auth.md.txt

Firebase Authentication

## Functions

|                                                                           Function                                                                           |                                                                                                                                                          Description                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                |
| [getAuth(app)](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1)                                                                        | Returns the Auth instance associated with the provided[FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes an Auth instance with platform-specific default dependencies.                                                                  |
| [initializeAuth(app, deps)](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b)                                                    | Initializes an[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance with fine-grained control over[Dependencies](https://firebase.google.com/docs/reference/js/auth.dependencies.md#dependencies_interface).                                                                               |
| **function(storage, ...)**                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                |
| [getReactNativePersistence(storage)](https://firebase.google.com/docs/reference/js/auth.md#getreactnativepersistence_bab4ada)                                | Returns a persistence object that wraps`AsyncStorage`imported from`react-native`or`@react-native-community/async-storage`, and can be used in the persistence dependency field in[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b).                                             |
| **function(auth, ...)**                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                |
| [applyActionCode(auth, oobCode)](https://firebase.google.com/docs/reference/js/auth.md#applyactioncode_d2ae15a)                                              | Applies a verification code sent to the user by email or other out-of-band mechanism.                                                                                                                                                                                                                                          |
| [beforeAuthStateChanged(auth, callback, onAbort)](https://firebase.google.com/docs/reference/js/auth.md#beforeauthstatechanged_22f2ab6)                      | Adds a blocking callback that runs before an auth state change sets a new user.                                                                                                                                                                                                                                                |
| [checkActionCode(auth, oobCode)](https://firebase.google.com/docs/reference/js/auth.md#checkactioncode_d2ae15a)                                              | Checks a verification code sent to the user by email or other out-of-band mechanism.                                                                                                                                                                                                                                           |
| [confirmPasswordReset(auth, oobCode, newPassword)](https://firebase.google.com/docs/reference/js/auth.md#confirmpasswordreset_749dad8)                       | Completes the password reset process, given a confirmation code and new password.                                                                                                                                                                                                                                              |
| [connectAuthEmulator(auth, url, options)](https://firebase.google.com/docs/reference/js/auth.md#connectauthemulator_657c7e5)                                 | Changes the[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance to communicate with the Firebase Auth Emulator, instead of production Firebase Auth services.                                                                                                                             |
| [createUserWithEmailAndPassword(auth, email, password)](https://firebase.google.com/docs/reference/js/auth.md#createuserwithemailandpassword_21ad33b)        | Creates a new user account associated with the specified email address and password.                                                                                                                                                                                                                                           |
| [fetchSignInMethodsForEmail(auth, email)](https://firebase.google.com/docs/reference/js/auth.md#fetchsigninmethodsforemail_efb3887)                          | Gets the list of possible sign in methods for the given email address. This method returns an empty list when[Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)is enabled, irrespective of the number of authentication methods available for the given email. |
| [getMultiFactorResolver(auth, error)](https://firebase.google.com/docs/reference/js/auth.md#getmultifactorresolver_201ba61)                                  | Provides a[MultiFactorResolver](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolver_interface)suitable for completion of a multi-factor flow.                                                                                                                                        |
| [getRedirectResult(auth, resolver)](https://firebase.google.com/docs/reference/js/auth.md#getredirectresult_c35dc1f)                                         | Returns a[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)from the redirect-based sign-in flow.                                                                                                                                                                  |
| [initializeRecaptchaConfig(auth)](https://firebase.google.com/docs/reference/js/auth.md#initializerecaptchaconfig_2a61ea7)                                   | Loads the reCAPTCHA configuration into the`Auth`instance.                                                                                                                                                                                                                                                                      |
| [isSignInWithEmailLink(auth, emailLink)](https://firebase.google.com/docs/reference/js/auth.md#issigninwithemaillink_db04f1d)                                | Checks if an incoming link is a sign-in with email link suitable for[signInWithEmailLink()](https://firebase.google.com/docs/reference/js/auth.md#signinwithemaillink_ed14c53).                                                                                                                                                |
| [onAuthStateChanged(auth, nextOrObserver, error, completed)](https://firebase.google.com/docs/reference/js/auth.md#onauthstatechanged_b0d07ab)               | Adds an observer for changes to the user's sign-in state.                                                                                                                                                                                                                                                                      |
| [onIdTokenChanged(auth, nextOrObserver, error, completed)](https://firebase.google.com/docs/reference/js/auth.md#onidtokenchanged_b0d07ab)                   | Adds an observer for changes to the signed-in user's ID token.                                                                                                                                                                                                                                                                 |
| [revokeAccessToken(auth, token)](https://firebase.google.com/docs/reference/js/auth.md#revokeaccesstoken_5556ad5)                                            | Revokes the given access token. Currently only supports Apple OAuth access tokens.                                                                                                                                                                                                                                             |
| [sendPasswordResetEmail(auth, email, actionCodeSettings)](https://firebase.google.com/docs/reference/js/auth.md#sendpasswordresetemail_95b079b)              | Sends a password reset email to the given email address. This method does not throw an error when there's no user account with the given email address and[Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)is enabled.                                        |
| [sendSignInLinkToEmail(auth, email, actionCodeSettings)](https://firebase.google.com/docs/reference/js/auth.md#sendsigninlinktoemail_95b079b)                | Sends a sign-in email link to the user with the specified email.                                                                                                                                                                                                                                                               |
| [setPersistence(auth, persistence)](https://firebase.google.com/docs/reference/js/auth.md#setpersistence_a3592ac)                                            | Changes the type of persistence on the[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance for the currently saved`Auth`session and applies this type of persistence for future sign-in requests, including sign-in with redirect requests.                                               |
| [signInAnonymously(auth)](https://firebase.google.com/docs/reference/js/auth.md#signinanonymously_2a61ea7)                                                   | Asynchronously signs in as an anonymous user.                                                                                                                                                                                                                                                                                  |
| [signInWithCredential(auth, credential)](https://firebase.google.com/docs/reference/js/auth.md#signinwithcredential_8074518)                                 | Asynchronously signs in with the given credentials.                                                                                                                                                                                                                                                                            |
| [signInWithCustomToken(auth, customToken)](https://firebase.google.com/docs/reference/js/auth.md#signinwithcustomtoken_32af683)                              | Asynchronously signs in using a custom token.                                                                                                                                                                                                                                                                                  |
| [signInWithEmailAndPassword(auth, email, password)](https://firebase.google.com/docs/reference/js/auth.md#signinwithemailandpassword_21ad33b)                | Asynchronously signs in using an email and password.                                                                                                                                                                                                                                                                           |
| [signInWithEmailLink(auth, email, emailLink)](https://firebase.google.com/docs/reference/js/auth.md#signinwithemaillink_ed14c53)                             | Asynchronously signs in using an email and sign-in email link.                                                                                                                                                                                                                                                                 |
| [signInWithPhoneNumber(auth, phoneNumber, appVerifier)](https://firebase.google.com/docs/reference/js/auth.md#signinwithphonenumber_75b2560)                 | Asynchronously signs in using a phone number.                                                                                                                                                                                                                                                                                  |
| [signInWithPopup(auth, provider, resolver)](https://firebase.google.com/docs/reference/js/auth.md#signinwithpopup_770f816)                                   | Authenticates a Firebase client using a popup-based OAuth authentication flow.                                                                                                                                                                                                                                                 |
| [signInWithRedirect(auth, provider, resolver)](https://firebase.google.com/docs/reference/js/auth.md#signinwithredirect_770f816)                             | Authenticates a Firebase client using a full-page redirect flow.                                                                                                                                                                                                                                                               |
| [signOut(auth)](https://firebase.google.com/docs/reference/js/auth.md#signout_2a61ea7)                                                                       | Signs out the current user.                                                                                                                                                                                                                                                                                                    |
| [updateCurrentUser(auth, user)](https://firebase.google.com/docs/reference/js/auth.md#updatecurrentuser_9d96fff)                                             | Asynchronously sets the provided user as[Auth.currentUser](https://firebase.google.com/docs/reference/js/auth.auth.md#authcurrentuser)on the[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                                                                         |
| [useDeviceLanguage(auth)](https://firebase.google.com/docs/reference/js/auth.md#usedevicelanguage_2a61ea7)                                                   | Sets the current language to the default device/browser preference.                                                                                                                                                                                                                                                            |
| [validatePassword(auth, password)](https://firebase.google.com/docs/reference/js/auth.md#validatepassword_4dc4ad2)                                           | Validates the password against the password policy configured for the project or tenant.                                                                                                                                                                                                                                       |
| [verifyPasswordResetCode(auth, code)](https://firebase.google.com/docs/reference/js/auth.md#verifypasswordresetcode_01e0a1a)                                 | Checks a password reset code sent to the user by email or other out-of-band mechanism.                                                                                                                                                                                                                                         |
| **function(link, ...)**                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                |
| [parseActionCodeURL(link)](https://firebase.google.com/docs/reference/js/auth.md#parseactioncodeurl_51293c3)                                                 | Parses the email action link string and returns an[ActionCodeURL](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurl_class)if the link is valid, otherwise returns null.                                                                                                                        |
| **function(user, ...)**                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                |
| [deleteUser(user)](https://firebase.google.com/docs/reference/js/auth.md#deleteuser_52b2e2e)                                                                 | Deletes and signs out the user.                                                                                                                                                                                                                                                                                                |
| [getIdToken(user, forceRefresh)](https://firebase.google.com/docs/reference/js/auth.md#getidtoken_ce7d429)                                                   | Returns a JSON Web Token (JWT) used to identify the user to a Firebase service.                                                                                                                                                                                                                                                |
| [getIdTokenResult(user, forceRefresh)](https://firebase.google.com/docs/reference/js/auth.md#getidtokenresult_ce7d429)                                       | Returns a deserialized JSON Web Token (JWT) used to identify the user to a Firebase service.                                                                                                                                                                                                                                   |
| [linkWithCredential(user, credential)](https://firebase.google.com/docs/reference/js/auth.md#linkwithcredential_60f8043)                                     | Links the user account with the given credentials.                                                                                                                                                                                                                                                                             |
| [linkWithPhoneNumber(user, phoneNumber, appVerifier)](https://firebase.google.com/docs/reference/js/auth.md#linkwithphonenumber_9ed75fe)                     | Links the user account with the given phone number.                                                                                                                                                                                                                                                                            |
| [linkWithPopup(user, provider, resolver)](https://firebase.google.com/docs/reference/js/auth.md#linkwithpopup_41c0b31)                                       | Links the authenticated provider to the user account using a pop-up based OAuth flow.                                                                                                                                                                                                                                          |
| [linkWithRedirect(user, provider, resolver)](https://firebase.google.com/docs/reference/js/auth.md#linkwithredirect_41c0b31)                                 | Links the[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class)to the user account using a full-page redirect flow.                                                                                                                                                          |
| [multiFactor(user)](https://firebase.google.com/docs/reference/js/auth.md#multifactor_52b2e2e)                                                               | The[MultiFactorUser](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruser_interface)corresponding to the user.                                                                                                                                                                                |
| [reauthenticateWithCredential(user, credential)](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithcredential_60f8043)                 | Re-authenticates a user using a fresh credential.                                                                                                                                                                                                                                                                              |
| [reauthenticateWithPhoneNumber(user, phoneNumber, appVerifier)](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithphonenumber_9ed75fe) | Re-authenticates a user using a fresh phone credential.                                                                                                                                                                                                                                                                        |
| [reauthenticateWithPopup(user, provider, resolver)](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithpopup_41c0b31)                   | Reauthenticates the current user with the specified[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class)using a pop-up based OAuth flow.                                                                                                                                    |
| [reauthenticateWithRedirect(user, provider, resolver)](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithredirect_41c0b31)             | Reauthenticates the current user with the specified[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class)using a full-page redirect flow.                                                                                                                                    |
| [reload(user)](https://firebase.google.com/docs/reference/js/auth.md#reload_52b2e2e)                                                                         | Reloads user account data, if signed in.                                                                                                                                                                                                                                                                                       |
| [sendEmailVerification(user, actionCodeSettings)](https://firebase.google.com/docs/reference/js/auth.md#sendemailverification_6a885d6)                       | Sends a verification email to a user.                                                                                                                                                                                                                                                                                          |
| [unlink(user, providerId)](https://firebase.google.com/docs/reference/js/auth.md#unlink_f289a14)                                                             | Unlinks a provider from a user account.                                                                                                                                                                                                                                                                                        |
| [updateEmail(user, newEmail)](https://firebase.google.com/docs/reference/js/auth.md#updateemail_7737d57)                                                     | Updates the user's email address.                                                                                                                                                                                                                                                                                              |
| [updatePassword(user, newPassword)](https://firebase.google.com/docs/reference/js/auth.md#updatepassword_6df673e)                                            | Updates the user's password.                                                                                                                                                                                                                                                                                                   |
| [updatePhoneNumber(user, credential)](https://firebase.google.com/docs/reference/js/auth.md#updatephonenumber_0105c49)                                       | Updates the user's phone number.                                                                                                                                                                                                                                                                                               |
| [updateProfile(user, { displayName, photoURL: photoUrl })](https://firebase.google.com/docs/reference/js/auth.md#updateprofile_017e12d)                      | Updates a user's profile data.                                                                                                                                                                                                                                                                                                 |
| [verifyBeforeUpdateEmail(user, newEmail, actionCodeSettings)](https://firebase.google.com/docs/reference/js/auth.md#verifybeforeupdateemail_09d6f11)         | Sends a verification email to a new email address.                                                                                                                                                                                                                                                                             |
| **function(userCredential, ...)**                                                                                                                            |                                                                                                                                                                                                                                                                                                                                |
| [getAdditionalUserInfo(userCredential)](https://firebase.google.com/docs/reference/js/auth.md#getadditionaluserinfo_838a6bd)                                 | Extracts provider specific[AdditionalUserInfo](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfo_interface)for the given credential.                                                                                                                                                 |

## Classes

|                                                                    Class                                                                     |                                                                                                                                                              Description                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActionCodeURL](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurl_class)                                     | A utility class to parse email action URLs such as password reset, email verification, email link sign in, etc.                                                                                                                                                                                                                        |
| [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class)                                  | Interface that represents the credentials returned by an[AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface).                                                                                                                                                                     |
| [EmailAuthCredential](https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md#emailauthcredential_class)                   | Interface that represents the credentials returned by[EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)for[ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PASSWORD                                                                    |
| [EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)                         | Provider for generating[EmailAuthCredential](https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md#emailauthcredential_class).                                                                                                                                                                                     |
| [FacebookAuthProvider](https://firebase.google.com/docs/reference/js/auth.facebookauthprovider.md#facebookauthprovider_class)                | Provider for generating an[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)for[ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).FACEBOOK.                                                                                                    |
| [GithubAuthProvider](https://firebase.google.com/docs/reference/js/auth.githubauthprovider.md#githubauthprovider_class)                      | Provider for generating an[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)for[ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).GITHUB.                                                                                                      |
| [GoogleAuthProvider](https://firebase.google.com/docs/reference/js/auth.googleauthprovider.md#googleauthprovider_class)                      | Provider for generating an[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)for[ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).GOOGLE.                                                                                                      |
| [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)                               | Represents the OAuth credentials returned by an[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class).                                                                                                                                                                               |
| [OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class)                                     | Provider for generating generic[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class).                                                                                                                                                                                         |
| [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredential_class)                   | Represents the credentials returned by[PhoneAuthProvider](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthprovider_class).                                                                                                                                                                            |
| [PhoneAuthProvider](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthprovider_class)                         | Provider for generating an[PhoneAuthCredential](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredential_class).                                                                                                                                                                                  |
| [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/js/auth.phonemultifactorgenerator.md#phonemultifactorgenerator_class) | Provider for generating a[PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.phonemultifactorassertion.md#phonemultifactorassertion_interface).                                                                                                                                                             |
| [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifier_class)                         | An[reCAPTCHA](https://www.google.com/recaptcha/)-based application verifier.                                                                                                                                                                                                                                                           |
| [SAMLAuthProvider](https://firebase.google.com/docs/reference/js/auth.samlauthprovider.md#samlauthprovider_class)                            | An[AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)for SAML.                                                                                                                                                                                                                   |
| [TotpMultiFactorGenerator](https://firebase.google.com/docs/reference/js/auth.totpmultifactorgenerator.md#totpmultifactorgenerator_class)    | Provider for generating a[TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface).                                                                                                                                                                |
| [TotpSecret](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecret_class)                                              | Provider for generating a[TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface).Stores the shared secret key and other parameters to generate time-based OTPs. Implements methods to retrieve the shared secret key and generate a QR code URL. |
| [TwitterAuthProvider](https://firebase.google.com/docs/reference/js/auth.twitterauthprovider.md#twitterauthprovider_class)                   | Provider for generating an[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class)for[ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).TWITTER.                                                                                                     |

## Interfaces

|                                                                                Interface                                                                                 |                                                                                                                                                                                                              Description                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActionCodeInfo](https://firebase.google.com/docs/reference/js/auth.actioncodeinfo.md#actioncodeinfo_interface)                                                          | A response from[checkActionCode()](https://firebase.google.com/docs/reference/js/auth.md#checkactioncode_d2ae15a).                                                                                                                                                                                                                                                                                                                     |
| [ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface)                                              | An interface that defines the required continue/state URL with optional Android and iOS bundle identifiers.                                                                                                                                                                                                                                                                                                                            |
| [AdditionalUserInfo](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfo_interface)                                              | A structure containing additional user information from a federated identity provider.                                                                                                                                                                                                                                                                                                                                                 |
| [ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface)                                           | A verifier for domain verification and abuse prevention.                                                                                                                                                                                                                                                                                                                                                                               |
| [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                                                                        | Interface representing Firebase Auth service.                                                                                                                                                                                                                                                                                                                                                                                          |
| [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface)                                                                         | Interface for an`Auth`error.                                                                                                                                                                                                                                                                                                                                                                                                           |
| [AuthErrorMap](https://firebase.google.com/docs/reference/js/auth.autherrormap.md#autherrormap_interface)                                                                | A mapping of error codes to error messages.                                                                                                                                                                                                                                                                                                                                                                                            |
| [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)                                                                | Interface that represents an auth provider, used to facilitate creating[AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class).                                                                                                                                                                                                                                                    |
| [AuthSettings](https://firebase.google.com/docs/reference/js/auth.authsettings.md#authsettings_interface)                                                                | Interface representing an[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance's settings.                                                                                                                                                                                                                                                                                                         |
| [Config](https://firebase.google.com/docs/reference/js/auth.config.md#config_interface)                                                                                  | Interface representing the`Auth`config.                                                                                                                                                                                                                                                                                                                                                                                                |
| [ConfirmationResult](https://firebase.google.com/docs/reference/js/auth.confirmationresult.md#confirmationresult_interface)                                              | A result from a phone number sign-in, link, or reauthenticate call.                                                                                                                                                                                                                                                                                                                                                                    |
| [Dependencies](https://firebase.google.com/docs/reference/js/auth.dependencies.md#dependencies_interface)                                                                | The dependencies that can be used to initialize an[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                                                                                                                                                                                                                                                                           |
| [EmulatorConfig](https://firebase.google.com/docs/reference/js/auth.emulatorconfig.md#emulatorconfig_interface)                                                          | Configuration of Firebase Authentication Emulator.                                                                                                                                                                                                                                                                                                                                                                                     |
| [IdTokenResult](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresult_interface)                                                             | Interface representing ID token result obtained from[User.getIdTokenResult()](https://firebase.google.com/docs/reference/js/auth.user.md#usergetidtokenresult).                                                                                                                                                                                                                                                                        |
| [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md#multifactorassertion_interface)                                        | The base class for asserting ownership of a second factor.                                                                                                                                                                                                                                                                                                                                                                             |
| [MultiFactorError](https://firebase.google.com/docs/reference/js/auth.multifactorerror.md#multifactorerror_interface)                                                    | The error thrown when the user needs to provide a second factor to sign in successfully.                                                                                                                                                                                                                                                                                                                                               |
| [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface)                                                       | A structure containing the information of a second factor entity.                                                                                                                                                                                                                                                                                                                                                                      |
| [MultiFactorResolver](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolver_interface)                                           | The class used to facilitate recovery from[MultiFactorError](https://firebase.google.com/docs/reference/js/auth.multifactorerror.md#multifactorerror_interface)when a user needs to provide a second factor to sign in.                                                                                                                                                                                                                |
| [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface)                                              | An interface defining the multi-factor session object used for enrolling a second factor on a user or helping sign in an enrolled user with a second factor.                                                                                                                                                                                                                                                                           |
| [MultiFactorUser](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruser_interface)                                                       | An interface that defines the multi-factor related properties and operations pertaining to a[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface).                                                                                                                                                                                                                                                         |
| [OAuthCredentialOptions](https://firebase.google.com/docs/reference/js/auth.oauthcredentialoptions.md#oauthcredentialoptions_interface)                                  | Defines the options for initializing an[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class).                                                                                                                                                                                                                                                                                 |
| [ParsedToken](https://firebase.google.com/docs/reference/js/auth.parsedtoken.md#parsedtoken_interface)                                                                   | Interface representing a parsed ID token.                                                                                                                                                                                                                                                                                                                                                                                              |
| [PasswordPolicy](https://firebase.google.com/docs/reference/js/auth.passwordpolicy.md#passwordpolicy_interface)                                                          | A structure specifying password policy requirements.                                                                                                                                                                                                                                                                                                                                                                                   |
| [PasswordValidationStatus](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatus_interface)                            | A structure indicating which password policy requirements were met or violated and what the requirements are.                                                                                                                                                                                                                                                                                                                          |
| [Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)                                                                   | An interface covering the possible persistence mechanism types.                                                                                                                                                                                                                                                                                                                                                                        |
| [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.phonemultifactorassertion.md#phonemultifactorassertion_interface)                         | The class for asserting ownership of a phone second factor. Provided by[PhoneMultiFactorGenerator.assertion()](https://firebase.google.com/docs/reference/js/auth.phonemultifactorgenerator.md#phonemultifactorgeneratorassertion).                                                                                                                                                                                                    |
| [PhoneMultiFactorEnrollInfoOptions](https://firebase.google.com/docs/reference/js/auth.phonemultifactorenrollinfooptions.md#phonemultifactorenrollinfooptions_interface) | Options used for enrolling a second factor.                                                                                                                                                                                                                                                                                                                                                                                            |
| [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.phonemultifactorinfo.md#phonemultifactorinfo_interface)                                        | The subclass of the[MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface)interface for phone number second factors. The`factorId`of this second factor is[FactorId](https://firebase.google.com/docs/reference/js/auth.md#factorid).PHONE.                                                                                                                                 |
| [PhoneMultiFactorSignInInfoOptions](https://firebase.google.com/docs/reference/js/auth.phonemultifactorsignininfooptions.md#phonemultifactorsignininfooptions_interface) | Options used for signing in with a second factor.                                                                                                                                                                                                                                                                                                                                                                                      |
| [PhoneSingleFactorInfoOptions](https://firebase.google.com/docs/reference/js/auth.phonesinglefactorinfooptions.md#phonesinglefactorinfooptions_interface)                | Options used for single-factor sign-in.                                                                                                                                                                                                                                                                                                                                                                                                |
| [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface)                                     | A resolver used for handling DOM specific operations like[signInWithPopup()](https://firebase.google.com/docs/reference/js/auth.md#signinwithpopup_770f816)or[signInWithRedirect()](https://firebase.google.com/docs/reference/js/auth.md#signinwithredirect_770f816).                                                                                                                                                                 |
| [ReactNativeAsyncStorage](https://firebase.google.com/docs/reference/js/auth.reactnativeasyncstorage.md#reactnativeasyncstorage_interface)                               | Interface for a supplied`AsyncStorage`.                                                                                                                                                                                                                                                                                                                                                                                                |
| [RecaptchaParameters](https://firebase.google.com/docs/reference/js/auth.recaptchaparameters.md#recaptchaparameters_interface)                                           | Interface representing reCAPTCHA parameters.See the[reCAPTCHA docs](https://developers.google.com/recaptcha/docs/display#render_param)for the list of accepted parameters. All parameters are accepted except for`sitekey`: Firebase Auth provisions a reCAPTCHA for each project and will configure the site key upon rendering.For an invisible reCAPTCHA, set the`size`key to`invisible`.                                           |
| [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface)                            | The class for asserting ownership of a TOTP second factor. Provided by[TotpMultiFactorGenerator.assertionForEnrollment()](https://firebase.google.com/docs/reference/js/auth.totpmultifactorgenerator.md#totpmultifactorgeneratorassertionforenrollment)and[TotpMultiFactorGenerator.assertionForSignIn()](https://firebase.google.com/docs/reference/js/auth.totpmultifactorgenerator.md#totpmultifactorgeneratorassertionforsignin). |
| [TotpMultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.totpmultifactorinfo.md#totpmultifactorinfo_interface)                                           | The subclass of the[MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface)interface for TOTP second factors. The`factorId`of this second factor is[FactorId](https://firebase.google.com/docs/reference/js/auth.md#factorid).TOTP.                                                                                                                                          |
| [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                                                                        | A user account.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)                                                          | A structure containing a[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface), the[OperationType](https://firebase.google.com/docs/reference/js/auth.md#operationtype), and the provider ID.                                                                                                                                                                                                               |
| [UserInfo](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfo_interface)                                                                            | User profile information, visible only to the Firebase project's apps.                                                                                                                                                                                                                                                                                                                                                                 |
| [UserMetadata](https://firebase.google.com/docs/reference/js/auth.usermetadata.md#usermetadata_interface)                                                                | Interface representing a user's metadata.                                                                                                                                                                                                                                                                                                                                                                                              |

## Variables

|                                                      Variable                                                      |                                                                                                                       Description                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActionCodeOperation](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation)                   | An enumeration of the possible email action types.                                                                                                                                                                                                       |
| [AuthErrorCodes](https://firebase.google.com/docs/reference/js/auth.md#autherrorcodes)                             | A map of potential`Auth`error codes, for easier comparison with errors thrown by the SDK.                                                                                                                                                                |
| [browserCookiePersistence](https://firebase.google.com/docs/reference/js/auth.md#browsercookiepersistence)         | ***(Public Preview)*** An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of type`COOKIE`, for use on the client side in applications leveraging hybrid rendering and middleware. |
| [browserLocalPersistence](https://firebase.google.com/docs/reference/js/auth.md#browserlocalpersistence)           | An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of type`LOCAL`using`localStorage`for the underlying storage.                                                                   |
| [browserPopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.md#browserpopupredirectresolver) | An implementation of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface)suitable for browser based applications.                                                         |
| [browserSessionPersistence](https://firebase.google.com/docs/reference/js/auth.md#browsersessionpersistence)       | An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of`SESSION`using`sessionStorage`for the underlying storage.                                                                    |
| [cordovaPopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.md#cordovapopupredirectresolver) | An implementation of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface)suitable for Cordova based applications.                                                         |
| [debugErrorMap](https://firebase.google.com/docs/reference/js/auth.md#debugerrormap)                               | A verbose error map with detailed descriptions for most error codes.See discussion at[AuthErrorMap](https://firebase.google.com/docs/reference/js/auth.autherrormap.md#autherrormap_interface)                                                           |
| [FactorId](https://firebase.google.com/docs/reference/js/auth.md#factorid)                                         | An enum of factors that may be used for multifactor authentication.                                                                                                                                                                                      |
| [indexedDBLocalPersistence](https://firebase.google.com/docs/reference/js/auth.md#indexeddblocalpersistence)       | An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of type`LOCAL`using`indexedDB`for the underlying storage.                                                                      |
| [inMemoryPersistence](https://firebase.google.com/docs/reference/js/auth.md#inmemorypersistence)                   | An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of type 'NONE'.                                                                                                                |
| [OperationType](https://firebase.google.com/docs/reference/js/auth.md#operationtype)                               | Enumeration of supported operation types.                                                                                                                                                                                                                |
| [prodErrorMap](https://firebase.google.com/docs/reference/js/auth.md#proderrormap)                                 | A minimal error map with all verbose error messages stripped.See discussion at[AuthErrorMap](https://firebase.google.com/docs/reference/js/auth.autherrormap.md#autherrormap_interface)                                                                  |
| [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid)                                     | Enumeration of supported providers.                                                                                                                                                                                                                      |
| [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod)                                 | Enumeration of supported sign-in methods.                                                                                                                                                                                                                |

## Type Aliases

|                                         Type Alias                                         |                                                                   Description                                                                    |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomParameters](https://firebase.google.com/docs/reference/js/auth.md#customparameters) | Map of OAuth Custom Parameters.                                                                                                                  |
| [NextOrObserver](https://firebase.google.com/docs/reference/js/auth.md#nextorobserver)     | Type definition for an event callback.                                                                                                           |
| [PhoneInfoOptions](https://firebase.google.com/docs/reference/js/auth.md#phoneinfooptions) | The information required to verify the ownership of a phone number.                                                                              |
| [UserProfile](https://firebase.google.com/docs/reference/js/auth.md#userprofile)           | User profile used in[AdditionalUserInfo](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfo_interface). |

## function(app, ...)

### getAuth(app)

Returns the Auth instance associated with the provided[FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes an Auth instance with platform-specific default dependencies.

**Signature:**  

    export declare function getAuth(app?: FirebaseApp): Auth;

#### Parameters

| Parameter |                                                 Type                                                  |    Description    |
|-----------|-------------------------------------------------------------------------------------------------------|-------------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The Firebase App. |

**Returns:**

[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)

### initializeAuth(app, deps)

Initializes an[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance with fine-grained control over[Dependencies](https://firebase.google.com/docs/reference/js/auth.dependencies.md#dependencies_interface).

This function allows more control over the[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance than[getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1).`getAuth`uses platform-specific defaults to supply the[Dependencies](https://firebase.google.com/docs/reference/js/auth.dependencies.md#dependencies_interface). In general,`getAuth`is the easiest way to initialize Auth and works for most use cases. Use`initializeAuth`if you need control over which persistence layer is used, or to minimize bundle size if you're not using either`signInWithPopup`or`signInWithRedirect`.

For example, if your app only uses anonymous accounts and you only want accounts saved for the current session, initialize`Auth`with:  

    const auth = initializeAuth(app, {
      persistence: browserSessionPersistence,
      popupRedirectResolver: undefined,
    });

**Signature:**  

    export declare function initializeAuth(app: FirebaseApp, deps?: Dependencies): Auth;

#### Parameters

| Parameter |                                                   Type                                                    | Description |
|-----------|-----------------------------------------------------------------------------------------------------------|-------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)     |             |
| deps      | [Dependencies](https://firebase.google.com/docs/reference/js/auth.dependencies.md#dependencies_interface) |             |

**Returns:**

[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)

## function(storage, ...)

### getReactNativePersistence(storage)

Returns a persistence object that wraps`AsyncStorage`imported from`react-native`or`@react-native-community/async-storage`, and can be used in the persistence dependency field in[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b).

**Signature:**  

    export declare function getReactNativePersistence(storage: ReactNativeAsyncStorage): Persistence;

#### Parameters

| Parameter |                                                                    Type                                                                    | Description |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| storage   | [ReactNativeAsyncStorage](https://firebase.google.com/docs/reference/js/auth.reactnativeasyncstorage.md#reactnativeasyncstorage_interface) |             |

**Returns:**

[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)

## function(auth, ...)

### applyActionCode(auth, oobCode)

Applies a verification code sent to the user by email or other out-of-band mechanism.

**Signature:**  

    export declare function applyActionCode(auth: Auth, oobCode: string): Promise<void>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| oobCode   | string                                                                            | A verification code sent to the user.                                                         |

**Returns:**

Promise\<void\>

### beforeAuthStateChanged(auth, callback, onAbort)

Adds a blocking callback that runs before an auth state change sets a new user.

**Signature:**  

    export declare function beforeAuthStateChanged(auth: Auth, callback: (user: User | null) => void | Promise<void>, onAbort?: () => void): Unsubscribe;

#### Parameters

| Parameter |                                                            Type                                                             |                                                  Description                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                           | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                  |
| callback  | (user:[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)\| null) =\> void \| Promise\<void\> | callback triggered before new user value is set. If this throws, it blocks the user from being set.            |
| onAbort   | () =\> void                                                                                                                 | callback triggered if a later`beforeAuthStateChanged()`callback throws, allowing you to undo any side effects. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

### checkActionCode(auth, oobCode)

Checks a verification code sent to the user by email or other out-of-band mechanism.

**Signature:**  

    export declare function checkActionCode(auth: Auth, oobCode: string): Promise<ActionCodeInfo>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| oobCode   | string                                                                            | A verification code sent to the user.                                                         |

**Returns:**

Promise\<[ActionCodeInfo](https://firebase.google.com/docs/reference/js/auth.actioncodeinfo.md#actioncodeinfo_interface)\>

metadata about the code.

### confirmPasswordReset(auth, oobCode, newPassword)

Completes the password reset process, given a confirmation code and new password.

**Signature:**  

    export declare function confirmPasswordReset(auth: Auth, oobCode: string, newPassword: string): Promise<void>;

#### Parameters

|  Parameter  |                                       Type                                        |                                          Description                                          |
|-------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth        | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| oobCode     | string                                                                            | A confirmation code sent to the user.                                                         |
| newPassword | string                                                                            | The new password.                                                                             |

**Returns:**

Promise\<void\>

### connectAuthEmulator(auth, url, options)

Changes the[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance to communicate with the Firebase Auth Emulator, instead of production Firebase Auth services.

This must be called synchronously immediately following the first call to[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b). Do not use with production credentials as emulator traffic is not encrypted.

**Signature:**  

    export declare function connectAuthEmulator(auth: Auth, url: string, options?: {
        disableWarnings: boolean;
    }): void;

#### Parameters

| Parameter |                                       Type                                        |                                                       Description                                                       |
|-----------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                           |
| url       | string                                                                            | The URL at which the emulator is running (eg, 'http://localhost:9099').                                                 |
| options   | { disableWarnings: boolean; }                                                     | Optional.`options.disableWarnings`defaults to`false`. Set it to`true`to disable the warning banner attached to the DOM. |

**Returns:**

void

### Example

    connectAuthEmulator(auth, 'http://127.0.0.1:9099', { disableWarnings: true });

### createUserWithEmailAndPassword(auth, email, password)

Creates a new user account associated with the specified email address and password.

On successful creation of the user account, this user will also be signed in to your application.

User account creation can fail if the account already exists or the password is invalid.

This method is not supported on[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).
| **Note:** The email address acts as a unique identifier for the user and enables an email-based password reset. This function will create a new user account and set the initial user password.

**Signature:**  

    export declare function createUserWithEmailAndPassword(auth: Auth, email: string, password: string): Promise<UserCredential>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| email     | string                                                                            | The user's email address.                                                                     |
| password  | string                                                                            | The user's chosen password.                                                                   |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### fetchSignInMethodsForEmail(auth, email)

Gets the list of possible sign in methods for the given email address. This method returns an empty list when[Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)is enabled, irrespective of the number of authentication methods available for the given email.

This is useful to differentiate methods of sign-in for the same provider, eg.[EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)which has 2 methods of sign-in,[SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_PASSWORD and[SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_LINK.

**Signature:**  

    export declare function fetchSignInMethodsForEmail(auth: Auth, email: string): Promise<string[]>;

#### Parameters

| Parameter |                                       Type                                        |                                                                                                                                      Description                                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                                                                                                                                                                          |
| email     | string                                                                            | The user's email address.Deprecated. Migrating off of this method is recommended as a security best-practice. Learn more in the Identity Platform documentation for[Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection). |

**Returns:**

Promise\<string\[\]\>

### getMultiFactorResolver(auth, error)

Provides a[MultiFactorResolver](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolver_interface)suitable for completion of a multi-factor flow.

**Signature:**  

    export declare function getMultiFactorResolver(auth: Auth, error: MultiFactorError): MultiFactorResolver;

#### Parameters

| Parameter |                                                         Type                                                          |                                                                                   Description                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                     | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                                                                   |
| error     | [MultiFactorError](https://firebase.google.com/docs/reference/js/auth.multifactorerror.md#multifactorerror_interface) | The[MultiFactorError](https://firebase.google.com/docs/reference/js/auth.multifactorerror.md#multifactorerror_interface)raised during a sign-in, or reauthentication operation. |

**Returns:**

[MultiFactorResolver](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolver_interface)

### getRedirectResult(auth, resolver)

Returns a[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)from the redirect-based sign-in flow.

If sign-in succeeded, returns the signed in user. If sign-in was unsuccessful, fails with an error. If no redirect operation was called, returns`null`.

This method does not work in a Node.js environment or with[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function getRedirectResult(auth: Auth, resolver?: PopupRedirectResolver): Promise<UserCredential | null>;

#### Parameters

| Parameter |                                                                 Type                                                                 |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                                    | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                                                                                                                                                                                                                                                                        |
| resolver  | [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) | An instance of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface), optional if already supplied to[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b)or provided by[getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1). |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\| null\>

### Example

    // Sign in using a redirect.
    const provider = new FacebookAuthProvider();
    // You can add additional scopes to the provider:
    provider.addScope('user_birthday');
    // Start a sign in process for an unauthenticated user.
    await signInWithRedirect(auth, provider);
    // This will trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);
    if (result) {
      // This is the signed-in user
      const user = result.user;
      // This gives you a Facebook Access Token.
      const credential = provider.credentialFromResult(auth, result);
      const token = credential.accessToken;
    }
    // As this API can be used for sign-in, linking and reauthentication,
    // check the operationType to determine what triggered this redirect
    // operation.
    const operationType = result.operationType;

### initializeRecaptchaConfig(auth)

Loads the reCAPTCHA configuration into the`Auth`instance.

This will load the reCAPTCHA config, which indicates whether the reCAPTCHA verification flow should be triggered for each auth provider, into the current Auth session.

If initializeRecaptchaConfig() is not invoked, the auth flow will always start without reCAPTCHA verification. If the provider is configured to require reCAPTCHA verification, the SDK will transparently load the reCAPTCHA config and restart the auth flows.

Thus, by calling this optional method, you will reduce the latency of future auth flows. Loading the reCAPTCHA config early will also enhance the signal collected by reCAPTCHA.

This method does not work in a Node.js environment.

**Signature:**  

    export declare function initializeRecaptchaConfig(auth: Auth): Promise<void>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |

**Returns:**

Promise\<void\>

### Example

    initializeRecaptchaConfig(auth);

### isSignInWithEmailLink(auth, emailLink)

Checks if an incoming link is a sign-in with email link suitable for[signInWithEmailLink()](https://firebase.google.com/docs/reference/js/auth.md#signinwithemaillink_ed14c53).

**Signature:**  

    export declare function isSignInWithEmailLink(auth: Auth, emailLink: string): boolean;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| emailLink | string                                                                            | The link sent to the user's email address.                                                    |

**Returns:**

boolean

### onAuthStateChanged(auth, nextOrObserver, error, completed)

Adds an observer for changes to the user's sign-in state.

To keep the old behavior, see[onIdTokenChanged()](https://firebase.google.com/docs/reference/js/auth.md#onidtokenchanged_b0d07ab).

**Signature:**  

    export declare function onAuthStateChanged(auth: Auth, nextOrObserver: NextOrObserver<User>, error?: ErrorFn, completed?: CompleteFn): Unsubscribe;

#### Parameters

|   Parameter    |                                                                                    Type                                                                                     |                                                                Description                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| auth           | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                                                                           | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                              |
| nextOrObserver | [NextOrObserver](https://firebase.google.com/docs/reference/js/auth.md#nextorobserver)\<[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)\> | callback triggered on change.                                                                                                              |
| error          | [ErrorFn](https://firebase.google.com/docs/reference/js/util.md#errorfn)                                                                                                    | Deprecated. This callback is never triggered. Errors on signing in/out can be caught in promises returned from sign-in/sign-out functions. |
| completed      | [CompleteFn](https://firebase.google.com/docs/reference/js/util.md#completefn)                                                                                              | Deprecated. This callback is never triggered.                                                                                              |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

### onIdTokenChanged(auth, nextOrObserver, error, completed)

Adds an observer for changes to the signed-in user's ID token.

This includes sign-in, sign-out, and token refresh events. This will not be triggered automatically upon ID token expiration. Use[User.getIdToken()](https://firebase.google.com/docs/reference/js/auth.user.md#usergetidtoken)to refresh the ID token.

**Signature:**  

    export declare function onIdTokenChanged(auth: Auth, nextOrObserver: NextOrObserver<User>, error?: ErrorFn, completed?: CompleteFn): Unsubscribe;

#### Parameters

|   Parameter    |                                                                                    Type                                                                                     |                                                                Description                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| auth           | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                                                                           | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                              |
| nextOrObserver | [NextOrObserver](https://firebase.google.com/docs/reference/js/auth.md#nextorobserver)\<[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)\> | callback triggered on change.                                                                                                              |
| error          | [ErrorFn](https://firebase.google.com/docs/reference/js/util.md#errorfn)                                                                                                    | Deprecated. This callback is never triggered. Errors on signing in/out can be caught in promises returned from sign-in/sign-out functions. |
| completed      | [CompleteFn](https://firebase.google.com/docs/reference/js/util.md#completefn)                                                                                              | Deprecated. This callback is never triggered.                                                                                              |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

### revokeAccessToken(auth, token)

Revokes the given access token. Currently only supports Apple OAuth access tokens.

**Signature:**  

    export declare function revokeAccessToken(auth: Auth, token: string): Promise<void>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| token     | string                                                                            | The Apple OAuth access token.                                                                 |

**Returns:**

Promise\<void\>

### sendPasswordResetEmail(auth, email, actionCodeSettings)

Sends a password reset email to the given email address. This method does not throw an error when there's no user account with the given email address and[Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)is enabled.

To complete the password reset, call[confirmPasswordReset()](https://firebase.google.com/docs/reference/js/auth.md#confirmpasswordreset_749dad8)with the code supplied in the email sent to the user, along with the new password specified by the user.

**Signature:**  

    export declare function sendPasswordResetEmail(auth: Auth, email: string, actionCodeSettings?: ActionCodeSettings): Promise<void>;

#### Parameters

|     Parameter      |                                                            Type                                                             |                                                           Description                                                           |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| auth               | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                           | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                   |
| email              | string                                                                                                                      | The user's email address.                                                                                                       |
| actionCodeSettings | [ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface) | The[ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface). |

**Returns:**

Promise\<void\>

### Example

    const actionCodeSettings = {
      url: 'https://www.example.com/?email=user@example.com',
      iOS: {
         bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true
    };
    await sendPasswordResetEmail(auth, 'user@example.com', actionCodeSettings);
    // Obtain code from user.
    await confirmPasswordReset('user@example.com', code);

### sendSignInLinkToEmail(auth, email, actionCodeSettings)

Sends a sign-in email link to the user with the specified email.

The sign-in operation has to always be completed in the app unlike other out of band email actions (password reset and email verifications). This is because, at the end of the flow, the user is expected to be signed in and their Auth state persisted within the app.

To complete sign in with the email link, call[signInWithEmailLink()](https://firebase.google.com/docs/reference/js/auth.md#signinwithemaillink_ed14c53)with the email address and the email link supplied in the email sent to the user.

**Signature:**  

    export declare function sendSignInLinkToEmail(auth: Auth, email: string, actionCodeSettings: ActionCodeSettings): Promise<void>;

#### Parameters

|     Parameter      |                                                            Type                                                             |                                                           Description                                                           |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| auth               | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                           |                                                                                                                                 |
| email              | string                                                                                                                      | The user's email address.                                                                                                       |
| actionCodeSettings | [ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface) | The[ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface). |

**Returns:**

Promise\<void\>

### Example

    const actionCodeSettings = {
      url: 'https://www.example.com/?email=user@example.com',
      iOS: {
         bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true
    };
    await sendSignInLinkToEmail(auth, 'user@example.com', actionCodeSettings);
    // Obtain emailLink from the user.
    if(isSignInWithEmailLink(auth, emailLink)) {
      await signInWithEmailLink(auth, 'user@example.com', emailLink);
    }

### setPersistence(auth, persistence)

Changes the type of persistence on the[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance for the currently saved`Auth`session and applies this type of persistence for future sign-in requests, including sign-in with redirect requests.

This makes it easy for a user signing in to specify whether their session should be remembered or not. It also makes it easier to never persist the`Auth`state for applications that are shared by other users or have sensitive data.

This method does not work in a Node.js environment or with[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function setPersistence(auth: Auth, persistence: Persistence): Promise<void>;

#### Parameters

|  Parameter  |                                                  Type                                                  |                                                   Description                                                    |
|-------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| auth        | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                      | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                    |
| persistence | [Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface) | The[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)to use. |

**Returns:**

Promise\<void\>

A`Promise`that resolves once the persistence change has completed

### Example

    setPersistence(auth, browserSessionPersistence);

### signInAnonymously(auth)

Asynchronously signs in as an anonymous user.

If there is already an anonymous user signed in, that user will be returned; otherwise, a new anonymous user identity will be created and returned.

This method is not supported by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function signInAnonymously(auth: Auth): Promise<UserCredential>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### signInWithCredential(auth, credential)

Asynchronously signs in with the given credentials.

An[AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)can be used to generate the credential.

This method is not supported by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function signInWithCredential(auth: Auth, credential: AuthCredential): Promise<UserCredential>;

#### Parameters

| Parameter  |                                                    Type                                                     |                                          Description                                          |
|------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth       | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                           | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| credential | [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) | The auth credential.                                                                          |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### signInWithCustomToken(auth, customToken)

Asynchronously signs in using a custom token.

Custom tokens are used to integrate Firebase Auth with existing auth systems, and must be generated by an auth backend using the[createCustomToken](https://firebase.google.com/docs/reference/admin/node/admin.auth.Auth#createcustomtoken)method in the[Admin SDK](https://firebase.google.com/docs/auth/admin).

Fails with an error if the token is invalid, expired, or not accepted by the Firebase Auth service.

This method is not supported by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function signInWithCustomToken(auth: Auth, customToken: string): Promise<UserCredential>;

#### Parameters

|  Parameter  |                                       Type                                        |                                          Description                                          |
|-------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth        | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| customToken | string                                                                            | The custom token to sign in with.                                                             |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### signInWithEmailAndPassword(auth, email, password)

Asynchronously signs in using an email and password.

Fails with an error if the email address and password do not match. When[Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)is enabled, this method fails with "auth/invalid-credential" in case of an invalid email/password.

This method is not supported on[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).
| **Note:** The user's password is NOT the password used to access the user's email account. The email address serves as a unique identifier for the user, and the password is used to access the user's account in your Firebase project. See also:[createUserWithEmailAndPassword()](https://firebase.google.com/docs/reference/js/auth.md#createuserwithemailandpassword_21ad33b).

**Signature:**  

    export declare function signInWithEmailAndPassword(auth: Auth, email: string, password: string): Promise<UserCredential>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| email     | string                                                                            | The users email address.                                                                      |
| password  | string                                                                            | The users password.                                                                           |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### signInWithEmailLink(auth, email, emailLink)

Asynchronously signs in using an email and sign-in email link.

If no link is passed, the link is inferred from the current URL.

Fails with an error if the email address is invalid or OTP in email link expires.

This method is not supported by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).
| **Note:** Confirm the link is a sign-in email link before calling this method firebase.auth.Auth.isSignInWithEmailLink.

**Signature:**  

    export declare function signInWithEmailLink(auth: Auth, email: string, emailLink?: string): Promise<UserCredential>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| email     | string                                                                            | The user's email address.                                                                     |
| emailLink | string                                                                            | The link sent to the user's email address.                                                    |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### Example

    const actionCodeSettings = {
      url: 'https://www.example.com/?email=user@example.com',
      iOS: {
         bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true
    };
    await sendSignInLinkToEmail(auth, 'user@example.com', actionCodeSettings);
    // Obtain emailLink from the user.
    if(isSignInWithEmailLink(auth, emailLink)) {
      await signInWithEmailLink(auth, 'user@example.com', emailLink);
    }

### signInWithPhoneNumber(auth, phoneNumber, appVerifier)

Asynchronously signs in using a phone number.

This method sends a code via SMS to the given phone number, and returns a[ConfirmationResult](https://firebase.google.com/docs/reference/js/auth.confirmationresult.md#confirmationresult_interface). After the user provides the code sent to their phone, call[ConfirmationResult.confirm()](https://firebase.google.com/docs/reference/js/auth.confirmationresult.md#confirmationresultconfirm)with the code to sign the user in.

For abuse prevention, this method requires a[ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface). This SDK includes an implementation based on reCAPTCHA v2,[RecaptchaVerifier](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifier_class). This function can work on other platforms that do not support the[RecaptchaVerifier](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifier_class)(like React Native), but you need to use a third-party[ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface)implementation.

If you've enabled project-level reCAPTCHA Enterprise bot protection in Enforce mode, you can omit the[ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface).

This method does not work in a Node.js environment or with[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function signInWithPhoneNumber(auth: Auth, phoneNumber: string, appVerifier?: ApplicationVerifier): Promise<ConfirmationResult>;

#### Parameters

|  Parameter  |                                                              Type                                                              |                                                            Description                                                             |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| auth        | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                              | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                      |
| phoneNumber | string                                                                                                                         | The user's phone number in E.164 format (e.g. +16505550101).                                                                       |
| appVerifier | [ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface) | The[ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface). |

**Returns:**

Promise\<[ConfirmationResult](https://firebase.google.com/docs/reference/js/auth.confirmationresult.md#confirmationresult_interface)\>

### Example

    // 'recaptcha-container' is the ID of an element in the DOM.
    const applicationVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container');
    const confirmationResult = await signInWithPhoneNumber(auth, phoneNumber, applicationVerifier);
    // Obtain a verificationCode from the user.
    const credential = await confirmationResult.confirm(verificationCode);

### signInWithPopup(auth, provider, resolver)

Authenticates a Firebase client using a popup-based OAuth authentication flow.

If succeeds, returns the signed in user along with the provider's credential. If sign in was unsuccessful, returns an error object containing additional information about the error.

This method does not work in a Node.js environment or with[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function signInWithPopup(auth: Auth, provider: AuthProvider, resolver?: PopupRedirectResolver): Promise<UserCredential>;

#### Parameters

| Parameter |                                                                 Type                                                                 |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                                    | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                                                                                                                                                                                                                                                                        |
| provider  | [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)                            | The provider to authenticate. The provider has to be an[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class). Non-OAuth providers like[EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)will throw an error.                                                    |
| resolver  | [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) | An instance of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface), optional if already supplied to[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b)or provided by[getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1). |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### Example

    // Sign in using a popup.
    const provider = new FacebookAuthProvider();
    const result = await signInWithPopup(auth, provider);

    // The signed-in user info.
    const user = result.user;
    // This gives you a Facebook Access Token.
    const credential = provider.credentialFromResult(auth, result);
    const token = credential.accessToken;

### signInWithRedirect(auth, provider, resolver)

Authenticates a Firebase client using a full-page redirect flow.

To handle the results and errors for this operation, refer to[getRedirectResult()](https://firebase.google.com/docs/reference/js/auth.md#getredirectresult_c35dc1f). Follow the[best practices](https://firebase.google.com/docs/auth/web/redirect-best-practices)when using[signInWithRedirect()](https://firebase.google.com/docs/reference/js/auth.md#signinwithredirect_770f816).

This method does not work in a Node.js environment or with[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function signInWithRedirect(auth: Auth, provider: AuthProvider, resolver?: PopupRedirectResolver): Promise<never>;

#### Parameters

| Parameter |                                                                 Type                                                                 |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                                    | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.                                                                                                                                                                                                                                                                                        |
| provider  | [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)                            | The provider to authenticate. The provider has to be an[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class). Non-OAuth providers like[EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)will throw an error.                                                    |
| resolver  | [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) | An instance of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface), optional if already supplied to[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b)or provided by[getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1). |

**Returns:**

Promise\<never\>

### Example

    // Sign in using a redirect.
    const provider = new FacebookAuthProvider();
    // You can add additional scopes to the provider:
    provider.addScope('user_birthday');
    // Start a sign in process for an unauthenticated user.
    await signInWithRedirect(auth, provider);
    // This will trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);
    if (result) {
      // This is the signed-in user
      const user = result.user;
      // This gives you a Facebook Access Token.
      const credential = provider.credentialFromResult(auth, result);
      const token = credential.accessToken;
    }
    // As this API can be used for sign-in, linking and reauthentication,
    // check the operationType to determine what triggered this redirect
    // operation.
    const operationType = result.operationType;

### signOut(auth)

Signs out the current user.

This method is not supported by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function signOut(auth: Auth): Promise<void>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |

**Returns:**

Promise\<void\>

### updateCurrentUser(auth, user)

Asynchronously sets the provided user as[Auth.currentUser](https://firebase.google.com/docs/reference/js/auth.auth.md#authcurrentuser)on the[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance.

A new instance copy of the user provided will be made and set as currentUser.

This will trigger[onAuthStateChanged()](https://firebase.google.com/docs/reference/js/auth.md#onauthstatechanged_b0d07ab)and[onIdTokenChanged()](https://firebase.google.com/docs/reference/js/auth.md#onidtokenchanged_b0d07ab)listeners like other sign in methods.

The operation fails with an error if the user to be updated belongs to a different Firebase project.

This method is not supported by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function updateCurrentUser(auth: Auth, user: User | null): Promise<void>;

#### Parameters

| Parameter |                                           Type                                           |                                          Description                                          |
|-----------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)        | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)\| null | The new[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface).     |

**Returns:**

Promise\<void\>

### useDeviceLanguage(auth)

Sets the current language to the default device/browser preference.

**Signature:**  

    export declare function useDeviceLanguage(auth: Auth): void;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |

**Returns:**

void

### validatePassword(auth, password)

Validates the password against the password policy configured for the project or tenant.

If no tenant ID is set on the`Auth`instance, then this method will use the password policy configured for the project. Otherwise, this method will use the policy configured for the tenant. If a password policy has not been configured, then the default policy configured for all projects will be used.

If an auth flow fails because a submitted password does not meet the password policy requirements and this method has previously been called, then this method will use the most recent policy available when called again.

**Signature:**  

    export declare function validatePassword(auth: Auth, password: string): Promise<PasswordValidationStatus>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| password  | string                                                                            | The password to validate.                                                                     |

**Returns:**

Promise\<[PasswordValidationStatus](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatus_interface)\>

### Example

    validatePassword(auth, 'some-password');

### verifyPasswordResetCode(auth, code)

Checks a password reset code sent to the user by email or other out-of-band mechanism.

**Signature:**  

    export declare function verifyPasswordResetCode(auth: Auth, code: string): Promise<string>;

#### Parameters

| Parameter |                                       Type                                        |                                          Description                                          |
|-----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| auth      | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) | The[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instance. |
| code      | string                                                                            | A verification code sent to the user.                                                         |

**Returns:**

Promise\<string\>

the user's email address if valid.

## function(link, ...)

### parseActionCodeURL(link)

Parses the email action link string and returns an[ActionCodeURL](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurl_class)if the link is valid, otherwise returns null.

**Signature:**  

    export declare function parseActionCodeURL(link: string): ActionCodeURL | null;

#### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| link      | string |             |

**Returns:**

[ActionCodeURL](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurl_class)\| null

## function(user, ...)

### deleteUser(user)

Deletes and signs out the user.
| **Important:** this is a security-sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and then call[reauthenticateWithCredential()](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithcredential_60f8043).

**Signature:**  

    export declare function deleteUser(user: User): Promise<void>;

#### Parameters

| Parameter |                                       Type                                        | Description |
|-----------|-----------------------------------------------------------------------------------|-------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.   |

**Returns:**

Promise\<void\>

### getIdToken(user, forceRefresh)

Returns a JSON Web Token (JWT) used to identify the user to a Firebase service.

Returns the current token if it has not expired or if it will not expire in the next five minutes. Otherwise, this will refresh the token and return a new one.

**Signature:**  

    export declare function getIdToken(user: User, forceRefresh?: boolean): Promise<string>;

#### Parameters

|  Parameter   |                                       Type                                        |                  Description                  |
|--------------|-----------------------------------------------------------------------------------|-----------------------------------------------|
| user         | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.                                     |
| forceRefresh | boolean                                                                           | Force refresh regardless of token expiration. |

**Returns:**

Promise\<string\>

### getIdTokenResult(user, forceRefresh)

Returns a deserialized JSON Web Token (JWT) used to identify the user to a Firebase service.

Returns the current token if it has not expired or if it will not expire in the next five minutes. Otherwise, this will refresh the token and return a new one.

**Signature:**  

    export declare function getIdTokenResult(user: User, forceRefresh?: boolean): Promise<IdTokenResult>;

#### Parameters

|  Parameter   |                                       Type                                        |                  Description                  |
|--------------|-----------------------------------------------------------------------------------|-----------------------------------------------|
| user         | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.                                     |
| forceRefresh | boolean                                                                           | Force refresh regardless of token expiration. |

**Returns:**

Promise\<[IdTokenResult](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresult_interface)\>

### linkWithCredential(user, credential)

Links the user account with the given credentials.

An[AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)can be used to generate the credential.

**Signature:**  

    export declare function linkWithCredential(user: User, credential: AuthCredential): Promise<UserCredential>;

#### Parameters

| Parameter  |                                                    Type                                                     |     Description      |
|------------|-------------------------------------------------------------------------------------------------------------|----------------------|
| user       | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                           | The user.            |
| credential | [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) | The auth credential. |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### linkWithPhoneNumber(user, phoneNumber, appVerifier)

Links the user account with the given phone number.

This method does not work in a Node.js environment.

**Signature:**  

    export declare function linkWithPhoneNumber(user: User, phoneNumber: string, appVerifier?: ApplicationVerifier): Promise<ConfirmationResult>;

#### Parameters

|  Parameter  |                                                              Type                                                              |                                                            Description                                                             |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| user        | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                              | The user.                                                                                                                          |
| phoneNumber | string                                                                                                                         | The user's phone number in E.164 format (e.g. +16505550101).                                                                       |
| appVerifier | [ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface) | The[ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface). |

**Returns:**

Promise\<[ConfirmationResult](https://firebase.google.com/docs/reference/js/auth.confirmationresult.md#confirmationresult_interface)\>

### linkWithPopup(user, provider, resolver)

Links the authenticated provider to the user account using a pop-up based OAuth flow.

If the linking is successful, the returned result will contain the user and the provider's credential.

This method does not work in a Node.js environment.

**Signature:**  

    export declare function linkWithPopup(user: User, provider: AuthProvider, resolver?: PopupRedirectResolver): Promise<UserCredential>;

#### Parameters

| Parameter |                                                                 Type                                                                 |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                                    | The user.                                                                                                                                                                                                                                                                                                                                                                            |
| provider  | [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)                            | The provider to authenticate. The provider has to be an[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class). Non-OAuth providers like[EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)will throw an error.                                                    |
| resolver  | [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) | An instance of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface), optional if already supplied to[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b)or provided by[getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1). |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### Example

    // Sign in using some other provider.
    const result = await signInWithEmailAndPassword(auth, email, password);
    // Link using a popup.
    const provider = new FacebookAuthProvider();
    await linkWithPopup(result.user, provider);

### linkWithRedirect(user, provider, resolver)

Links the[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class)to the user account using a full-page redirect flow.

To handle the results and errors for this operation, refer to[getRedirectResult()](https://firebase.google.com/docs/reference/js/auth.md#getredirectresult_c35dc1f). Follow the[best practices](https://firebase.google.com/docs/auth/web/redirect-best-practices)when using[linkWithRedirect()](https://firebase.google.com/docs/reference/js/auth.md#linkwithredirect_41c0b31).

This method does not work in a Node.js environment or with[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function linkWithRedirect(user: User, provider: AuthProvider, resolver?: PopupRedirectResolver): Promise<never>;

#### Parameters

| Parameter |                                                                 Type                                                                 |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                                    | The user.                                                                                                                                                                                                                                                                                                                                                                            |
| provider  | [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)                            | The provider to authenticate. The provider has to be an[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class). Non-OAuth providers like[EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)will throw an error.                                                    |
| resolver  | [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) | An instance of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface), optional if already supplied to[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b)or provided by[getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1). |

**Returns:**

Promise\<never\>

### Example

    // Sign in using some other provider.
    const result = await signInWithEmailAndPassword(auth, email, password);
    // Link using a redirect.
    const provider = new FacebookAuthProvider();
    await linkWithRedirect(result.user, provider);
    // This will trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);

### multiFactor(user)

The[MultiFactorUser](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruser_interface)corresponding to the user.

This is used to access all multi-factor properties and operations related to the user.

**Signature:**  

    export declare function multiFactor(user: User): MultiFactorUser;

#### Parameters

| Parameter |                                       Type                                        | Description |
|-----------|-----------------------------------------------------------------------------------|-------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.   |

**Returns:**

[MultiFactorUser](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruser_interface)

### reauthenticateWithCredential(user, credential)

Re-authenticates a user using a fresh credential.

Use before operations such as[updatePassword()](https://firebase.google.com/docs/reference/js/auth.md#updatepassword_6df673e)that require tokens from recent sign-in attempts. This method can be used to recover from a`CREDENTIAL_TOO_OLD_LOGIN_AGAIN`error or a`TOKEN_EXPIRED`error.

This method is not supported on any[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)signed in by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function reauthenticateWithCredential(user: User, credential: AuthCredential): Promise<UserCredential>;

#### Parameters

| Parameter  |                                                    Type                                                     |     Description      |
|------------|-------------------------------------------------------------------------------------------------------------|----------------------|
| user       | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                           | The user.            |
| credential | [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) | The auth credential. |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### reauthenticateWithPhoneNumber(user, phoneNumber, appVerifier)

Re-authenticates a user using a fresh phone credential.

Use before operations such as[updatePassword()](https://firebase.google.com/docs/reference/js/auth.md#updatepassword_6df673e)that require tokens from recent sign-in attempts.

This method does not work in a Node.js environment or on any[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)signed in by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function reauthenticateWithPhoneNumber(user: User, phoneNumber: string, appVerifier?: ApplicationVerifier): Promise<ConfirmationResult>;

#### Parameters

|  Parameter  |                                                              Type                                                              |                                                            Description                                                             |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| user        | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                              | The user.                                                                                                                          |
| phoneNumber | string                                                                                                                         | The user's phone number in E.164 format (e.g. +16505550101).                                                                       |
| appVerifier | [ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface) | The[ApplicationVerifier](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifier_interface). |

**Returns:**

Promise\<[ConfirmationResult](https://firebase.google.com/docs/reference/js/auth.confirmationresult.md#confirmationresult_interface)\>

### reauthenticateWithPopup(user, provider, resolver)

Reauthenticates the current user with the specified[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class)using a pop-up based OAuth flow.

If the reauthentication is successful, the returned result will contain the user and the provider's credential.

This method does not work in a Node.js environment or on any[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)signed in by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function reauthenticateWithPopup(user: User, provider: AuthProvider, resolver?: PopupRedirectResolver): Promise<UserCredential>;

#### Parameters

| Parameter |                                                                 Type                                                                 |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                                    | The user.                                                                                                                                                                                                                                                                                                                                                                            |
| provider  | [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)                            | The provider to authenticate. The provider has to be an[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class). Non-OAuth providers like[EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)will throw an error.                                                    |
| resolver  | [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) | An instance of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface), optional if already supplied to[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b)or provided by[getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1). |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### Example

    // Sign in using a popup.
    const provider = new FacebookAuthProvider();
    const result = await signInWithPopup(auth, provider);
    // Reauthenticate using a popup.
    await reauthenticateWithPopup(result.user, provider);

### reauthenticateWithRedirect(user, provider, resolver)

Reauthenticates the current user with the specified[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class)using a full-page redirect flow.

To handle the results and errors for this operation, refer to[getRedirectResult()](https://firebase.google.com/docs/reference/js/auth.md#getredirectresult_c35dc1f). Follow the[best practices](https://firebase.google.com/docs/auth/web/redirect-best-practices)when using[reauthenticateWithRedirect()](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithredirect_41c0b31).

This method does not work in a Node.js environment or with[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function reauthenticateWithRedirect(user: User, provider: AuthProvider, resolver?: PopupRedirectResolver): Promise<never>;

#### Parameters

| Parameter |                                                                 Type                                                                 |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                                    | The user.                                                                                                                                                                                                                                                                                                                                                                            |
| provider  | [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface)                            | The provider to authenticate. The provider has to be an[OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class). Non-OAuth providers like[EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class)will throw an error.                                                    |
| resolver  | [PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface) | An instance of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface), optional if already supplied to[initializeAuth()](https://firebase.google.com/docs/reference/js/auth.md#initializeauth_ca77c9b)or provided by[getAuth()](https://firebase.google.com/docs/reference/js/auth.md#getauth_cf608e1). |

**Returns:**

Promise\<never\>

### Example

    // Sign in using a redirect.
    const provider = new FacebookAuthProvider();
    const result = await signInWithRedirect(auth, provider);
    // This will trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);
    // Reauthenticate using a redirect.
    await reauthenticateWithRedirect(result.user, provider);
    // This will again trigger a full page redirect away from your app

    // After returning from the redirect when your app initializes you can obtain the result
    const result = await getRedirectResult(auth);

### reload(user)

Reloads user account data, if signed in.

**Signature:**  

    export declare function reload(user: User): Promise<void>;

#### Parameters

| Parameter |                                       Type                                        | Description |
|-----------|-----------------------------------------------------------------------------------|-------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.   |

**Returns:**

Promise\<void\>

### sendEmailVerification(user, actionCodeSettings)

Sends a verification email to a user.

The verification process is completed by calling[applyActionCode()](https://firebase.google.com/docs/reference/js/auth.md#applyactioncode_d2ae15a).

**Signature:**  

    export declare function sendEmailVerification(user: User, actionCodeSettings?: ActionCodeSettings | null): Promise<void>;

#### Parameters

|     Parameter      |                                                                Type                                                                |                                                           Description                                                           |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| user               | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                                  | The user.                                                                                                                       |
| actionCodeSettings | [ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface)\| null | The[ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface). |

**Returns:**

Promise\<void\>

### Example

    const actionCodeSettings = {
      url: 'https://www.example.com/?email=user@example.com',
      iOS: {
         bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true
    };
    await sendEmailVerification(user, actionCodeSettings);
    // Obtain code from the user.
    await applyActionCode(auth, code);

### unlink(user, providerId)

Unlinks a provider from a user account.

**Signature:**  

    export declare function unlink(user: User, providerId: string): Promise<User>;

#### Parameters

| Parameter  |                                       Type                                        |       Description       |
|------------|-----------------------------------------------------------------------------------|-------------------------|
| user       | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.               |
| providerId | string                                                                            | The provider to unlink. |

**Returns:**

Promise\<[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)\>

### updateEmail(user, newEmail)

Updates the user's email address.

An email will be sent to the original email address (if it was set) that allows to revoke the email address change, in order to protect them from account hijacking.

This method is not supported on any[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)signed in by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).
| **Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and then call[reauthenticateWithCredential()](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithcredential_60f8043).

**Signature:**  

    export declare function updateEmail(user: User, newEmail: string): Promise<void>;

#### Parameters

| Parameter |                                       Type                                        |                                                                                                                                                                 Description                                                                                                                                                                  |
|-----------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user      | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.                                                                                                                                                                                                                                                                                                                                    |
| newEmail  | string                                                                            | The new email address.Throws "auth/operation-not-allowed" error when[Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)is enabled. Deprecated - Use[verifyBeforeUpdateEmail()](https://firebase.google.com/docs/reference/js/auth.md#verifybeforeupdateemail_09d6f11)instead. |

**Returns:**

Promise\<void\>

### updatePassword(user, newPassword)

Updates the user's password.
| **Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and then call[reauthenticateWithCredential()](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithcredential_60f8043).

**Signature:**  

    export declare function updatePassword(user: User, newPassword: string): Promise<void>;

#### Parameters

|  Parameter  |                                       Type                                        |    Description    |
|-------------|-----------------------------------------------------------------------------------|-------------------|
| user        | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.         |
| newPassword | string                                                                            | The new password. |

**Returns:**

Promise\<void\>

### updatePhoneNumber(user, credential)

Updates the user's phone number.

This method does not work in a Node.js environment or on any[User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)signed in by[Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)instances created with a[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    export declare function updatePhoneNumber(user: User, credential: PhoneAuthCredential): Promise<void>;

#### Parameters

| Parameter  |                                                            Type                                                            |                    Description                    |
|------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| user       | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                          | The user.                                         |
| credential | [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredential_class) | A credential authenticating the new phone number. |

**Returns:**

Promise\<void\>

### Example

    // 'recaptcha-container' is the ID of an element in the DOM.
    const applicationVerifier = new RecaptchaVerifier('recaptcha-container');
    const provider = new PhoneAuthProvider(auth);
    const verificationId = await provider.verifyPhoneNumber('+16505550101', applicationVerifier);
    // Obtain the verificationCode from the user.
    const phoneCredential = PhoneAuthProvider.credential(verificationId, verificationCode);
    await updatePhoneNumber(user, phoneCredential);

### updateProfile(user, { displayName, photoURL: photoUrl })

Updates a user's profile data.

**Signature:**  

    export declare function updateProfile(user: User, { displayName, photoURL: photoUrl }: {
        displayName?: string | null;
        photoURL?: string | null;
    }): Promise<void>;

#### Parameters

|              Parameter              |                                       Type                                        | Description |
|-------------------------------------|-----------------------------------------------------------------------------------|-------------|
| user                                | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) | The user.   |
| { displayName, photoURL: photoUrl } | { displayName?: string \| null; photoURL?: string \| null; }                      |             |

**Returns:**

Promise\<void\>

### verifyBeforeUpdateEmail(user, newEmail, actionCodeSettings)

Sends a verification email to a new email address.

The user's email will be updated to the new one after being verified.

If you have a custom email action handler, you can complete the verification process by calling[applyActionCode()](https://firebase.google.com/docs/reference/js/auth.md#applyactioncode_d2ae15a).

**Signature:**  

    export declare function verifyBeforeUpdateEmail(user: User, newEmail: string, actionCodeSettings?: ActionCodeSettings | null): Promise<void>;

#### Parameters

|     Parameter      |                                                                Type                                                                |                                                           Description                                                           |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| user               | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                                  | The user.                                                                                                                       |
| newEmail           | string                                                                                                                             | The new email address to be verified before update.                                                                             |
| actionCodeSettings | [ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface)\| null | The[ActionCodeSettings](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettings_interface). |

**Returns:**

Promise\<void\>

### Example

    const actionCodeSettings = {
      url: 'https://www.example.com/?email=user@example.com',
      iOS: {
         bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true
    };
    await verifyBeforeUpdateEmail(user, 'newemail@example.com', actionCodeSettings);
    // Obtain code from the user.
    await applyActionCode(auth, code);

## function(userCredential, ...)

### getAdditionalUserInfo(userCredential)

Extracts provider specific[AdditionalUserInfo](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfo_interface)for the given credential.

**Signature:**  

    export declare function getAdditionalUserInfo(userCredential: UserCredential): AdditionalUserInfo | null;

#### Parameters

|   Parameter    |                                                      Type                                                       |     Description      |
|----------------|-----------------------------------------------------------------------------------------------------------------|----------------------|
| userCredential | [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface) | The user credential. |

**Returns:**

[AdditionalUserInfo](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfo_interface)\| null

## ActionCodeOperation

An enumeration of the possible email action types.

**Signature:**  

    ActionCodeOperation: {
        readonly EMAIL_SIGNIN: "EMAIL_SIGNIN";
        readonly PASSWORD_RESET: "PASSWORD_RESET";
        readonly RECOVER_EMAIL: "RECOVER_EMAIL";
        readonly REVERT_SECOND_FACTOR_ADDITION: "REVERT_SECOND_FACTOR_ADDITION";
        readonly VERIFY_AND_CHANGE_EMAIL: "VERIFY_AND_CHANGE_EMAIL";
        readonly VERIFY_EMAIL: "VERIFY_EMAIL";
    }

## AuthErrorCodes

A map of potential`Auth`error codes, for easier comparison with errors thrown by the SDK.

Note that you can't tree-shake individual keys in the map, so by using the map you might substantially increase your bundle size.

**Signature:**  

    AUTH_ERROR_CODES_MAP_DO_NOT_USE_INTERNALLY: {
        readonly ADMIN_ONLY_OPERATION: "auth/admin-restricted-operation";
        readonly ARGUMENT_ERROR: "auth/argument-error";
        readonly APP_NOT_AUTHORIZED: "auth/app-not-authorized";
        readonly APP_NOT_INSTALLED: "auth/app-not-installed";
        readonly CAPTCHA_CHECK_FAILED: "auth/captcha-check-failed";
        readonly CODE_EXPIRED: "auth/code-expired";
        readonly CORDOVA_NOT_READY: "auth/cordova-not-ready";
        readonly CORS_UNSUPPORTED: "auth/cors-unsupported";
        readonly CREDENTIAL_ALREADY_IN_USE: "auth/credential-already-in-use";
        readonly CREDENTIAL_MISMATCH: "auth/custom-token-mismatch";
        readonly CREDENTIAL_TOO_OLD_LOGIN_AGAIN: "auth/requires-recent-login";
        readonly DEPENDENT_SDK_INIT_BEFORE_AUTH: "auth/dependent-sdk-initialized-before-auth";
        readonly DYNAMIC_LINK_NOT_ACTIVATED: "auth/dynamic-link-not-activated";
        readonly EMAIL_CHANGE_NEEDS_VERIFICATION: "auth/email-change-needs-verification";
        readonly EMAIL_EXISTS: "auth/email-already-in-use";
        readonly EMULATOR_CONFIG_FAILED: "auth/emulator-config-failed";
        readonly EXPIRED_OOB_CODE: "auth/expired-action-code";
        readonly EXPIRED_POPUP_REQUEST: "auth/cancelled-popup-request";
        readonly INTERNAL_ERROR: "auth/internal-error";
        readonly INVALID_API_KEY: "auth/invalid-api-key";
        readonly INVALID_APP_CREDENTIAL: "auth/invalid-app-credential";
        readonly INVALID_APP_ID: "auth/invalid-app-id";
        readonly INVALID_AUTH: "auth/invalid-user-token";
        readonly INVALID_AUTH_EVENT: "auth/invalid-auth-event";
        readonly INVALID_CERT_HASH: "auth/invalid-cert-hash";
        readonly INVALID_CODE: "auth/invalid-verification-code";
        readonly INVALID_CONTINUE_URI: "auth/invalid-continue-uri";
        readonly INVALID_CORDOVA_CONFIGURATION: "auth/invalid-cordova-configuration";
        readonly INVALID_CUSTOM_TOKEN: "auth/invalid-custom-token";
        readonly INVALID_DYNAMIC_LINK_DOMAIN: "auth/invalid-dynamic-link-domain";
        readonly INVALID_EMAIL: "auth/invalid-email";
        readonly INVALID_EMULATOR_SCHEME: "auth/invalid-emulator-scheme";
        readonly INVALID_IDP_RESPONSE: "auth/invalid-credential";
        readonly INVALID_LOGIN_CREDENTIALS: "auth/invalid-credential";
        readonly INVALID_MESSAGE_PAYLOAD: "auth/invalid-message-payload";
        readonly INVALID_MFA_SESSION: "auth/invalid-multi-factor-session";
        readonly INVALID_OAUTH_CLIENT_ID: "auth/invalid-oauth-client-id";
        readonly INVALID_OAUTH_PROVIDER: "auth/invalid-oauth-provider";
        readonly INVALID_OOB_CODE: "auth/invalid-action-code";
        readonly INVALID_ORIGIN: "auth/unauthorized-domain";
        readonly INVALID_PASSWORD: "auth/wrong-password";
        readonly INVALID_PERSISTENCE: "auth/invalid-persistence-type";
        readonly INVALID_PHONE_NUMBER: "auth/invalid-phone-number";
        readonly INVALID_PROVIDER_ID: "auth/invalid-provider-id";
        readonly INVALID_RECIPIENT_EMAIL: "auth/invalid-recipient-email";
        readonly INVALID_SENDER: "auth/invalid-sender";
        readonly INVALID_SESSION_INFO: "auth/invalid-verification-id";
        readonly INVALID_TENANT_ID: "auth/invalid-tenant-id";
        readonly MFA_INFO_NOT_FOUND: "auth/multi-factor-info-not-found";
        readonly MFA_REQUIRED: "auth/multi-factor-auth-required";
        readonly MISSING_ANDROID_PACKAGE_NAME: "auth/missing-android-pkg-name";
        readonly MISSING_APP_CREDENTIAL: "auth/missing-app-credential";
        readonly MISSING_AUTH_DOMAIN: "auth/auth-domain-config-required";
        readonly MISSING_CODE: "auth/missing-verification-code";
        readonly MISSING_CONTINUE_URI: "auth/missing-continue-uri";
        readonly MISSING_IFRAME_START: "auth/missing-iframe-start";
        readonly MISSING_IOS_BUNDLE_ID: "auth/missing-ios-bundle-id";
        readonly MISSING_OR_INVALID_NONCE: "auth/missing-or-invalid-nonce";
        readonly MISSING_MFA_INFO: "auth/missing-multi-factor-info";
        readonly MISSING_MFA_SESSION: "auth/missing-multi-factor-session";
        readonly MISSING_PHONE_NUMBER: "auth/missing-phone-number";
        readonly MISSING_PASSWORD: "auth/missing-password";
        readonly MISSING_SESSION_INFO: "auth/missing-verification-id";
        readonly MODULE_DESTROYED: "auth/app-deleted";
        readonly NEED_CONFIRMATION: "auth/account-exists-with-different-credential";
        readonly NETWORK_REQUEST_FAILED: "auth/network-request-failed";
        readonly NULL_USER: "auth/null-user";
        readonly NO_AUTH_EVENT: "auth/no-auth-event";
        readonly NO_SUCH_PROVIDER: "auth/no-such-provider";
        readonly OPERATION_NOT_ALLOWED: "auth/operation-not-allowed";
        readonly OPERATION_NOT_SUPPORTED: "auth/operation-not-supported-in-this-environment";
        readonly POPUP_BLOCKED: "auth/popup-blocked";
        readonly POPUP_CLOSED_BY_USER: "auth/popup-closed-by-user";
        readonly PROVIDER_ALREADY_LINKED: "auth/provider-already-linked";
        readonly QUOTA_EXCEEDED: "auth/quota-exceeded";
        readonly REDIRECT_CANCELLED_BY_USER: "auth/redirect-cancelled-by-user";
        readonly REDIRECT_OPERATION_PENDING: "auth/redirect-operation-pending";
        readonly REJECTED_CREDENTIAL: "auth/rejected-credential";
        readonly SECOND_FACTOR_ALREADY_ENROLLED: "auth/second-factor-already-in-use";
        readonly SECOND_FACTOR_LIMIT_EXCEEDED: "auth/maximum-second-factor-count-exceeded";
        readonly TENANT_ID_MISMATCH: "auth/tenant-id-mismatch";
        readonly TIMEOUT: "auth/timeout";
        readonly TOKEN_EXPIRED: "auth/user-token-expired";
        readonly TOO_MANY_ATTEMPTS_TRY_LATER: "auth/too-many-requests";
        readonly UNAUTHORIZED_DOMAIN: "auth/unauthorized-continue-uri";
        readonly UNSUPPORTED_FIRST_FACTOR: "auth/unsupported-first-factor";
        readonly UNSUPPORTED_PERSISTENCE: "auth/unsupported-persistence-type";
        readonly UNSUPPORTED_TENANT_OPERATION: "auth/unsupported-tenant-operation";
        readonly UNVERIFIED_EMAIL: "auth/unverified-email";
        readonly USER_CANCELLED: "auth/user-cancelled";
        readonly USER_DELETED: "auth/user-not-found";
        readonly USER_DISABLED: "auth/user-disabled";
        readonly USER_MISMATCH: "auth/user-mismatch";
        readonly USER_SIGNED_OUT: "auth/user-signed-out";
        readonly WEAK_PASSWORD: "auth/weak-password";
        readonly WEB_STORAGE_UNSUPPORTED: "auth/web-storage-unsupported";
        readonly ALREADY_INITIALIZED: "auth/already-initialized";
        readonly RECAPTCHA_NOT_ENABLED: "auth/recaptcha-not-enabled";
        readonly MISSING_RECAPTCHA_TOKEN: "auth/missing-recaptcha-token";
        readonly INVALID_RECAPTCHA_TOKEN: "auth/invalid-recaptcha-token";
        readonly INVALID_RECAPTCHA_ACTION: "auth/invalid-recaptcha-action";
        readonly MISSING_CLIENT_TYPE: "auth/missing-client-type";
        readonly MISSING_RECAPTCHA_VERSION: "auth/missing-recaptcha-version";
        readonly INVALID_RECAPTCHA_VERSION: "auth/invalid-recaptcha-version";
        readonly INVALID_REQ_TYPE: "auth/invalid-req-type";
        readonly INVALID_HOSTING_LINK_DOMAIN: "auth/invalid-hosting-link-domain";
    }

## browserCookiePersistence

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of type`COOKIE`, for use on the client side in applications leveraging hybrid rendering and middleware.

This persistence method requires companion middleware to function, such as that provided by[ReactFire](https://firebaseopensource.com/projects/firebaseextended/reactfire/)for NextJS.

**Signature:**  

    browserCookiePersistence: Persistence

## browserLocalPersistence

An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of type`LOCAL`using`localStorage`for the underlying storage.

**Signature:**  

    browserLocalPersistence: Persistence

## browserPopupRedirectResolver

An implementation of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface)suitable for browser based applications.

This method does not work in a Node.js environment.

**Signature:**  

    browserPopupRedirectResolver: PopupRedirectResolver

## browserSessionPersistence

An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of`SESSION`using`sessionStorage`for the underlying storage.

**Signature:**  

    browserSessionPersistence: Persistence

## cordovaPopupRedirectResolver

An implementation of[PopupRedirectResolver](https://firebase.google.com/docs/reference/js/auth.popupredirectresolver.md#popupredirectresolver_interface)suitable for Cordova based applications.

**Signature:**  

    cordovaPopupRedirectResolver: PopupRedirectResolver

## debugErrorMap

A verbose error map with detailed descriptions for most error codes.

See discussion at[AuthErrorMap](https://firebase.google.com/docs/reference/js/auth.autherrormap.md#autherrormap_interface)

**Signature:**  

    debugErrorMap: AuthErrorMap

## FactorId

An enum of factors that may be used for multifactor authentication.

**Signature:**  

    FactorId: {
        readonly PHONE: "phone";
        readonly TOTP: "totp";
    }

## indexedDBLocalPersistence

An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of type`LOCAL`using`indexedDB`for the underlying storage.

**Signature:**  

    indexedDBLocalPersistence: Persistence

## inMemoryPersistence

An implementation of[Persistence](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistence_interface)of type 'NONE'.

**Signature:**  

    inMemoryPersistence: Persistence

## OperationType

Enumeration of supported operation types.

**Signature:**  

    OperationType: {
        readonly LINK: "link";
        readonly REAUTHENTICATE: "reauthenticate";
        readonly SIGN_IN: "signIn";
    }

## prodErrorMap

A minimal error map with all verbose error messages stripped.

See discussion at[AuthErrorMap](https://firebase.google.com/docs/reference/js/auth.autherrormap.md#autherrormap_interface)

**Signature:**  

    prodErrorMap: AuthErrorMap

## ProviderId

Enumeration of supported providers.

**Signature:**  

    ProviderId: {
        readonly FACEBOOK: "facebook.com";
        readonly GITHUB: "github.com";
        readonly GOOGLE: "google.com";
        readonly PASSWORD: "password";
        readonly PHONE: "phone";
        readonly TWITTER: "twitter.com";
    }

## SignInMethod

Enumeration of supported sign-in methods.

**Signature:**  

    SignInMethod: {
        readonly EMAIL_LINK: "emailLink";
        readonly EMAIL_PASSWORD: "password";
        readonly FACEBOOK: "facebook.com";
        readonly GITHUB: "github.com";
        readonly GOOGLE: "google.com";
        readonly PHONE: "phone";
        readonly TWITTER: "twitter.com";
    }

## CustomParameters

Map of OAuth Custom Parameters.

**Signature:**  

    export type CustomParameters = Record<string, string>;

## NextOrObserver

Type definition for an event callback.

**Signature:**  

    export type NextOrObserver<T> = NextFn<T | null> | Observer<T | null>;

## PhoneInfoOptions

The information required to verify the ownership of a phone number.

The information that's required depends on whether you are doing single-factor sign-in, multi-factor enrollment or multi-factor sign-in.

**Signature:**  

    export type PhoneInfoOptions = PhoneSingleFactorInfoOptions | PhoneMultiFactorEnrollInfoOptions | PhoneMultiFactorSignInInfoOptions;

## UserProfile

User profile used in[AdditionalUserInfo](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfo_interface).

**Signature:**  

    export type UserProfile = Record<string, unknown>;