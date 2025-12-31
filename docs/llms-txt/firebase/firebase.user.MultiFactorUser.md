# Source: https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser.md.txt

# MultiFactorUser | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [User](https://firebase.google.com/docs/reference/js/v8/firebase.User).
- MultiFactorUser

This is the interface that defines the multi-factor related properties and
operations pertaining to a [firebase.User](https://firebase.google.com/docs/reference/js/v8/firebase.User).

## Index

### Properties

- [enrolledFactors](https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser#enrolledfactors)

### Methods

- [enroll](https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser#enroll)
- [getSession](https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser#getsession)
- [unenroll](https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser#unenroll)

## Properties

### enrolledFactors

enrolledFactors: [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo)\[\]  
Returns a list of the user's enrolled second factors.

## Methods

### enroll

- enroll ( assertion : [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorAssertion) , displayName ? : string \| null ) : Promise \< void \>
- Enrolls a second factor as identified by the
  [firebase.auth.MultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorAssertion) for the current user.
  On resolution, the user tokens are updated to reflect the change in the
  JWT payload.
  Accepts an additional display name parameter used to identify the second
  factor to the end user.
  Recent re-authentication is required for this operation to succeed.
  On successful enrollment, existing Firebase sessions (refresh tokens) are
  revoked. When a new factor is enrolled, an email notification is sent
  to the user's email.

  #### Error Codes

  auth/invalid-verification-code
  :   Thrown if the verification code is not valid.

  auth/missing-verification-code
  :   Thrown if the verification code is missing.

  auth/invalid-verification-id
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      ID of the credential is not valid.

  auth/missing-verification-id
  :   Thrown if the verification ID is missing.

  auth/code-expired
  :   Thrown if the verification code has expired.

  auth/maximum-second-factor-count-exceeded
  :   Thrown if The maximum allowed number of second factors on a user
      has been exceeded.

  auth/second-factor-already-in-use
  :   Thrown if the second factor is already enrolled on this account.

  auth/unsupported-first-factor
  :   Thrown if the first factor being used to sign in is not supported.

  auth/unverified-email
  :   Thrown if the email of the account is not verified.

  auth/requires-recent-login
  :   Thrown if the user's last sign-in time does not meet the security
      threshold. Use [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential) to
      resolve.

  example
  :

          firebase.auth().currentUser.multiFactor.getSession()
              .then(function(multiFactorSession) {
                // Send verification code
              var phoneAuthProvider = new firebase.auth.PhoneAuthProvider();
              var phoneInfoOptions = {
                phoneNumber: phoneNumber,
                session: multiFactorSession
              };
              return phoneAuthProvider.verifyPhoneNumber(
                  phoneInfoOptions, appVerifier);
              }).then(function(verificationId) {
                // Store verificationID and show UI to let user enter verification code.
              });

          var phoneAuthCredential =
              firebase.auth.PhoneAuthProvider.credential(verificationId, verificationCode);
          var multiFactorAssertion =
              firebase.auth.PhoneMultiFactorGenerator.assertion(phoneAuthCredential);
          firebase.auth().currentUser.multiFactor.enroll(multiFactorAssertion)
              .then(function() {
                // Second factor enrolled.
              });


  #### Parameters

  -

    ##### assertion: [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorAssertion)

    The multi-factor assertion to enroll with.
  -

    ##### Optional displayName: string \| null

    The display name of the second factor.

  #### Returns Promise\<void\>

### getSession

- getSession ( ) : Promise \< [MultiFactorSession](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorSession) \>
- Returns the session identifier for a second factor enrollment operation.
  This is used to identify the current user trying to enroll a second factor.

  #### Returns Promise\<[MultiFactorSession](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorSession)\>

  The promise that resolves with the
  [firebase.auth.MultiFactorSession](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorSession).

  #### Error Codes

  auth/user-token-expired
  :   Thrown if the token of the user is expired.

### unenroll

- unenroll ( option : [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo) \| string ) : Promise \< void \>
- Unenrolls the specified second factor. To specify the factor to remove, pass
  a [firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo) object
  (retrieved from `enrolledFactors()`)
  or the factor's UID string.
  Sessions are not revoked when the account is downgraded. An email
  notification is likely to be sent to the user notifying them of the change.
  Recent re-authentication is required for this operation to succeed.
  When an existing factor is unenrolled, an email notification is sent to the
  user's email.

  #### Error Codes

  auth/multi-factor-info-not-found
  :   Thrown if the user does not have a second factor matching the
      identifier provided.

  auth/requires-recent-login
  :   Thrown if the user's last sign-in time does not meet the security
      threshold. Use [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential) to
      resolve.

  example
  :

          var options = firebase.auth().currentUser.multiFactor.enrolledFactors;
          // Present user the option to unenroll.
          return firebase.auth().currentUser.multiFactor.unenroll(options[i])
            .then(function() {
              // User successfully unenrolled selected factor.
            }).catch(function(error) {
              // Handler error.
            });


  #### Parameters

  -

    ##### option: [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo) \| string

    The multi-factor option to unenroll.

  #### Returns Promise\<void\>