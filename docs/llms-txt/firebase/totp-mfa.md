# Source: https://firebase.google.com/docs/auth/web/totp-mfa.md.txt

# Source: https://firebase.google.com/docs/auth/ios/totp-mfa.md.txt

# Source: https://firebase.google.com/docs/auth/android/totp-mfa.md.txt

# Source: https://firebase.google.com/docs/auth/web/totp-mfa.md.txt

# Source: https://firebase.google.com/docs/auth/ios/totp-mfa.md.txt

# Source: https://firebase.google.com/docs/auth/android/totp-mfa.md.txt

If you've upgraded toFirebase Authenticationwith Identity Platform, you can add time-based one-time password (TOTP) multi-factor authentication (MFA) to your app.

Firebase Authenticationwith Identity Platformlets you use a TOTP as an additional factor for MFA. When you enable this feature, users attempting to sign in to your app see a request for a TOTP. To generate it, they must use an authenticator app capable of generating valid TOTP codes, such as[Google Authenticator](https://support.google.com/accounts/answer/1066447).

## Before you begin

1. Enable at least one provider that supports MFA. Note that all providers*except*the following support MFA:

   - Phone auth
   - Anonymous auth
   - Custom auth tokens
   - Apple Game Center
2. Ensure your app verifies user email addresses. MFA requires email verification. This prevents malicious actors from registering for a service with an email address that they don't own, and then locking out the actual owner of the email address by adding a second factor.

3. If you haven't done so already, install the[Firebase Android SDK](https://firebase.google.com/docs/android/setup).

   TOTP MFA is only supported on the[Android SDK version v22.1.0](https://firebase.google.com/support/release-notes/android#auth_v22-1-0)and above.

## Enable TOTP MFA

To enable TOTP as a second factor, use theAdmin SDKor call the project configuration REST endpoint.

To use theAdmin SDK, do the following:

1. If you haven't done so already, install the[Firebase Admin Node.js SDK](https://firebase.google.com/docs/admin/setup).

   TOTP MFA is only supported on Firebase Admin Node.js SDK versions 11.6.0 and above.
2. Run the following:

       import { getAuth } from 'firebase-admin/auth';

       getAuth().projectConfigManager().updateProjectConfig(
       {
             multiFactorConfig: {
                 providerConfigs: [{
                     state: "ENABLED",
                     totpProviderConfig: {
                         adjacentIntervals: <var translate="no"><span class="devsite-syntax-nx">NUM_ADJ_INTERVALS</span></var>
                     }
                 }]
             }
       })

   Replace the following:
   - <var translate="no">NUM_ADJ_INTERVALS</var>: The number of adjacent time-window intervals from which to accept TOTPs, from zero to ten. The default is five.

     TOTPs work by ensuring that when two parties (the prover and the validator) generate OTPs within the same time window (typically 30 seconds long), they generate the same password. However, to accommodate clock drift between parties and human response time, you can configure the TOTP service to also accept TOTPs from adjacent windows.

To enable TOTP MFA using the REST API, run the following:  

    curl -X PATCH "https://identitytoolkit.googleapis.com/admin/v2/projects/<var translate="no">PROJECT_ID</var>/config?updateMask=mfa" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -H "X-Goog-User-Project: <var translate="no">PROJECT_ID</var>" \
        -d \
        '{
            "mfa": {
              "providerConfigs": [{
                "state": "ENABLED",
                "totpProviderConfig": {
                  "adjacentIntervals": <var translate="no">NUM_ADJ_INTERVALS</var>
                }
              }]
           }
        }'

Replace the following:

- <var translate="no">PROJECT_ID</var>: The project ID.
- <var translate="no">NUM_ADJ_INTERVALS</var>: The number of time-window intervals, from zero to ten. The default is five.

  TOTPs work by ensuring that when two parties (the prover and the validator) generate OTPs within the same time window (typically 30 seconds long), they generate the same password. However, to accommodate clock drift between parties and human response time, you can configure the TOTP service to also accept TOTPs from adjacent windows.

## Choose an enrollment pattern

You can choose whether your app requires multi-factor authentication, and how and when to enroll your users. Some common patterns include the following:

- Enroll the user's second factor as part of registration. Use this method if your app requires multi-factor authentication for all users.

- Offer a skippable option to enroll a second factor during registration. If you want to encourage but not require multi-factor authentication in your app, you might use this approach.

- Provide the ability to add a second factor from the user's account or profile management page, instead of the sign-up screen. This minimizes friction during the registration process, while still making multi-factor authentication available for security-sensitive users.

- Require adding a second factor incrementally when the user wants to access features with increased security requirements.

## Enroll users in TOTP MFA

After you enable TOTP MFA as a second factor for your app, implement client-side logic to enroll users in TOTP MFA:

1. Re-authenticate the user.

2. Generate a TOTP secret for the authenticated user:

       // Generate a TOTP secret.
       Firebase.auth.currentUser.multiFactor.session
           .addOnSuccessListener { multiFactorSession ->
               TotpMultiFactorGenerator.generateSecret(multiFactorSession)
                   .addOnSuccessListener { totpSecret ->
                       // Display the secret to the user and prompt them to
                       // enter it into their authenticator app. (See the next
                       // step.)
                   }
           }

3. Display the secret to the user and prompt them to enter it into their authenticator app:

       // Display this key:
       val secret = totpSecret.sharedSecretKey

   In addition to displaying the secret key, you can attempt to automatically add it to the device's default authenticator app. To do so, generate a[Google Authenticator-compatible key URI](https://github.com/google/google-authenticator/wiki/Key-Uri-Format), and pass it to`openInOtpApp()`:  

       val qrCodeUri = totpSecret.generateQrCodeUrl(
           currentUser.email ?: "default account",
           "Your App Name")
       totpSecret.openInOtpApp(qrCodeUri)

   After the user adds their secret to their authenticator app, it will start generating TOTPs.
4. Prompt the user to type the TOTP displayed by their authenticator app and use it to finalize MFA enrollment:

       // Ask the user for a verification code from the authenticator app.
       val verificationCode = // Code from user input.

       // Finalize the enrollment.
       val multiFactorAssertion = TotpMultiFactorGenerator
           .getAssertionForEnrollment(totpSecret, verificationCode)
       Firebase.auth.currentUser.multiFactor.enroll(multiFactorAssertion, "TOTP")
           .addOnSuccessListener {
               // Enrollment complete.
           }

## Sign in users with a second factor

To sign in users with TOTP MFA, use the following code:

1. Call one of the`signInWith`- methods as you would if you weren't using MFA. (For example,`signInWithEmailAndPassword()`.) If the method throws an`FirebaseAuthMultiFactorException`, start your app's MFA flow.

       Firebase.auth.signInWithEmailAndPassword(email, password)
           .addOnSuccessListener { result ->
               // If the user is not enrolled with a second factor and provided valid
               // credentials, sign-in succeeds.

               // (If your app requires MFA, this could be considered an error
               // condition, which you would resolve by forcing the user to enroll a
               // second factor.)

               // ...
           }
           .addOnFailureListener { exception ->
               when (exception) {
                   is FirebaseAuthMultiFactorException -> {
                       // Initiate your second factor sign-in flow. (See next step.)
                       // ...
                   }
               }
           }

2. Your app's MFA flow should first prompt the user to choose the second factor they want to use. You can get a list of supported second factors by examining the`hints`property of a`MultiFactorResolver`instance:

       val enrolledFactors = exception.resolver.hints.map { it.displayName }

3. If the user chooses to use TOTP, prompt them to type the TOTP displayed on their authenticator app and use it to sign in:

       when (exception.resolver.hints[selectedIndex].factorId) {
           TotpMultiFactorGenerator.FACTOR_ID -> {
               val otpFromAuthenticator = // OTP typed by the user.
               val assertion = TotpMultiFactorGenerator.getAssertionForSignIn(
                   exception.resolver.hints[selectedIndex].uid,
                   otpFromAuthenticator
               )
               exception.resolver.resolveSignIn(assertion)
                   .addOnSuccessListener { result ->
                       // Successfully signed in!
                   }
                   .addOnFailureListener { resolveError ->
                       // Invalid or expired OTP.
                   }
           }
           PhoneMultiFactorGenerator.FACTOR_ID -> {
               // Handle SMS second factor.
           }
       }

## Unenroll from TOTP MFA

This section describes how to handle a user unenrolling from TOTP MFA.

If a user has signed up for multiple MFA options, and if they unenroll from the most recently enabled option, they receive an`auth/user-token-expired`and are logged out. The user must sign in again and verify their existing credentials---for example, an email address and password.

To unenroll the user, handle the error, and trigger reauthentication, use the following code:  

    Firebase.auth.currentUser.multiFactor.unenroll(mfaEnrollmentId)
        .addOnSuccessListener {
            // Second factor unenrolled.
        }
        .addOnFailureListener { exception ->
            when (exception) {
                is FirebaseAuthInvalidUserException -> {
                    // Second factor unenrolled. If the user was signed out, re-authenticate
                    // them.

                    // For example, if they signed in with a password, prompt them to
                    // provide it again, then call `reauthenticateWithCredential()` as shown
                    // below.
                    val credential = EmailAuthProvider.getCredential(email, password)
                    currentUser.reauthenticate(credential)
                        .addOnSuccessListener { 
                            // Success!
                        }
                        .addOnFailureListener { 
                            // Bad email address and password combination.
                        }
                }
            }
        }

## What's next

- [Manage multi-factor users](https://firebase.google.com/docs/auth/admin/manage-mfa-users)programmatically with theAdmin SDK.