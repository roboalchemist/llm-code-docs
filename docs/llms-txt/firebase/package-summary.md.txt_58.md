# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary.md.txt

# com.google.firebase.auth

# com.google.firebase.auth

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey` | Keys to access the account information related to an out of band code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` | Holds the possible operations that an out of band code can perform, which are password reset, verify email, and recover email. |

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult` | Interface for holding the information related to an out of band code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo` | Object that contains additional user information as a result of a successful sign-in, link, or re-authentication operation. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult` | Result object obtained from operations that can affect the authentication state. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener` | Listener called when there is a change in the authentication state. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener` | Listener called when the id token is changed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthProvider` | Represents the Firebase Authentication provider type. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata` | Holds the user metadata for the current `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/SignInMethodQueryResult` | Result object of a call to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String)`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpSecret` | Represents a TOTP secret that is used for enrolling a TOTP second factor. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo` | Represents a collection of standard profile information for a user. |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeEmailInfo` | Holds information regarding out-of-band operations that involve an email change. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo` | Holds information regarding different out of band operations. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeMultiFactorInfo` | Holds information regarding out of band operations that involve an multi-factor authentication. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` | Structure that contains the required continue/state URL with optional Android and iOS bundle identifiers. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` | A Builder class for `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeUrl` | A utility class to parse parameters in action code URLs from out of band email flows. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | Represents a credential that the Firebase Authentication server can use to authenticate a user. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential` | Wraps an email and password tuple for authentication purposes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider` | Represents the email and password authentication mechanism. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthCredential` | Wraps a Facebook Login access token for authentication purposes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider` | Represents the Facebook Login authentication provider. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider` | Abstract representation of an arbitrary federated authentication provider. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` | The entry point of the Firebase Authentication SDK. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings` | Enables the configuration of FirebaseAuth related settings. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` | Represents a user's profile information in your Firebase project's user database. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult` | Result object that contains a Firebase Auth ID Token. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GithubAuthCredential` | Wraps a Github OAuth access token for authentication purposes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GithubAuthProvider` | Represents the Github authentication provider. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthCredential` | Wraps a Google Sign-In ID token and/or access token, for authentication purposes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthProvider` | Represents the Google Sign-In authentication provider. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor` | Defines multi-factor related properties and operations pertaining to a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion` | Represents an assertion that the Firebase Authentication server can use to authenticate a user as part of a multi-factor flow. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` | Represents a single second factor meant for the user. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorResolver` | Utility class that contains methods to resolve second factor requirements on users that have opted into two-factor authentication. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession` | Identifies the current session to enroll a second factor or to complete sign in when previously enrolled. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthCredential` | Holds credentials generated by a sign-in with a credential to an IDP that uses OAuth |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` | Represents the login authentication provider for a generic OAuth2 provider. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` | Class used to create instances of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder` | Builder class to initialize `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential`'s. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential` | Wraps phone number and verification information for authentication purposes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions` | Options object for configuring phone validation flows in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | A Builder class for `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider` | Represents the phone number authentication mechanism. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken` | A 'token' that can be used to force re-sending an SMS verification code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks` | Registered callbacks for the different phone auth events. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion` | Asserts ownership of a phone number second factor. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator` | Helper class used to generate `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion`s. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo` | Represents the information for a phone second factor. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthCredential` | Wraps a Google Play Games Server Auth Code, for authentication purposes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthProvider` | Represents the Google Play Games authentication provider. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorAssertion` | Asserts ownership of a TOTP second factor. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator` | Helper class used to generate a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorAssertion`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo` | Represents the information for a TOTP (time-based one-time password) second factor. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthCredential` | Wraps a Log in with Twitter token and secret tuple for authentication purposes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider` | Represents the Twitter authentication provider. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest` | Request used to update user profile information. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest.Builder` | The request builder. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthActionCodeException` | Represents the exception which is a result of an expired or an invalid out of band code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthEmailException` | Represents the exception which is a result of an attempt to send an email via Firebase Auth (e.g. a password reset email) |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException` | Generic exception related to Firebase Authentication. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` | Thrown when one or more of the credentials passed to a method fail to identify and/or authenticate the user subject of that operation. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException` | Thrown when performing an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance that is no longer valid. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException` | Thrown when the auth request attempted to fetch a reCAPTCHA token, but the activity is missing or null. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthMultiFactorException` | This exception is returned when a user that previously enrolled a second factor tries to sign in and passes the first factor successfully. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException` | Thrown on security sensitive operations on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance that require the user to have signed in recently, when the requirement isn't met. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException` | Thrown when an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance couldn't be completed due to a conflict with another existing user. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException` | Thrown when using a weak password (less than 6 chars) to create a new account or to update an existing account's password. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWebException` | Thrown when a web operation couldn't be completed. |