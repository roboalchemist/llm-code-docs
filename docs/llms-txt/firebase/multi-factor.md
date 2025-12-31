# Source: https://firebase.google.com/docs/auth/web/multi-factor.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/multi-factor.md.txt

# Source: https://firebase.google.com/docs/auth/ios/multi-factor.md.txt

# Source: https://firebase.google.com/docs/auth/android/multi-factor.md.txt

# Source: https://firebase.google.com/docs/auth/ios/multi-factor.md.txt

# Source: https://firebase.google.com/docs/auth/android/multi-factor.md.txt

If you've upgraded toFirebase Authenticationwith Identity Platform, you can add SMS multi-factor authentication to your Android app.

Multi-factor authentication increases the security of your app. While attackers often compromise passwords and social accounts, intercepting a text message is more difficult.

## Before you begin

| **Note:** Using multi-factor authentication with[multiple tenants](https://cloud.google.com/identity-platform/docs/multi-tenancy)is not supported on Android.

1. Enable at least one provider that supports multi-factor authentication. Every provider supports MFA,**except**phone auth, anonymous auth, and Apple Game Center.

2. Ensure your app is verifying user emails. MFA requires email verification. This prevents malicious actors from registering for a service with an email they don't own, and then locking out the real owner by adding a second factor.

3. Register your app's SHA-1 hash in the Firebase Console (your changes will automatically carry over toGoogle CloudFirebase).

   1. Follow the steps in[Authenticating your client](https://developers.google.com/android/guides/client-auth)to obtain your app's SHA-1 hash.

   2. Open the[Firebase Console](https://console.firebase.google.com).

   3. Navigate to**Project Settings**.

   4. Under**Your apps**, click the Android icon.

   5. Follow the guided steps to add your SHA-1 hash.

## Enabling multi-factor authentication

1. Open the[**Authentication \> Sign-in method**](https://console.firebase.google.com/project/_/authentication/providers)page of theFirebaseconsole.

2. In the**Advanced** section, enable**SMS Multi-factor Authentication**.

   You should also enter the phone numbers you'll be testing your app with. While optional, registering test phone numbers is strongly recommended to avoid throttling during development.
3. If you haven't already authorized your app's domain, add it to the allow list on the[**Authentication \> Settings**](https://console.firebase.google.com/project/_/authentication/settings)page of theFirebaseconsole.

4. **Optional** : On the**Authentication \> Settings**page, set a policy on the regions to which you want to allow or deny SMS messages to be sent. Setting an SMS region policy can help protect your apps from SMS abuse.

## Choosing an enrollment pattern

You can choose whether your app requires multi-factor authentication, and how and when to enroll your users. Some common patterns include:

- Enroll the user's second factor as part of registration. Use this method if your app requires multi-factor authentication for all users.

- Offer a skippable option to enroll a second factor during registration. Apps that want to encourage, but not require, multi-factor authentication might prefer this approach.

- Provide the ability to add a second factor from the user's account or profile management page, instead of the sign up screen. This minimizes friction during the registration process, while still making multi-factor authentication available for security-sensitive users.

- Require adding a second factor incrementally when the user wants to access features with increased security requirements.

## Enrolling a second factor

To enroll a new secondary factor for a user:

1. Re-authenticate the user.

2. Ask the user enter their phone number.

   | **Note:** Google stores and uses phone numbers to improve spam and abuse prevention across all Google services. Ensure you obtain appropriate consent from your users before sending their phone numbers toFirebase.
3. Get a multi-factor session for the user:

   ### Kotlin

       user.multiFactor.session.addOnCompleteListener { task ->
           if (task.isSuccessful) {
               val multiFactorSession: MultiFactorSession? = task.result
           }
       }

   ### Java

       user.getMultiFactor().getSession()
         .addOnCompleteListener(
             new OnCompleteListener<MultiFactorSession>() {
             @Override
             public void onComplete(@NonNull Task<MultiFactorSession> task) {
               if (task.isSuccessful()) {
                 MultiFactorSession multiFactorSession = task.getResult();
               }
             }
             });

4. Build an`OnVerificationStateChangedCallbacks`object to handle different events in the verification process:

   ### Kotlin

       val callbacks = object : OnVerificationStateChangedCallbacks() {
           override fun onVerificationCompleted(credential: PhoneAuthCredential) {
               // This callback will be invoked in two situations:
               // 1) Instant verification. In some cases, the phone number can be
               //    instantly verified without needing to send or enter a verification
               //    code. You can disable this feature by calling
               //    PhoneAuthOptions.builder#requireSmsValidation(true) when building
               //    the options to pass to PhoneAuthProvider#verifyPhoneNumber().
               // 2) Auto-retrieval. On some devices, Google Play services can
               //    automatically detect the incoming verification SMS and perform
               //    verification without user action.
               this@MainActivity.credential = credential
           }

           override fun onVerificationFailed(e: FirebaseException) {
               // This callback is invoked in response to invalid requests for
               // verification, like an incorrect phone number.
               if (e is FirebaseAuthInvalidCredentialsException) {
                   // Invalid request
                   // ...
               } else if (e is FirebaseTooManyRequestsException) {
                   // The SMS quota for the project has been exceeded
                   // ...
               }
               // Show a message and update the UI
               // ...
           }

           override fun onCodeSent(
               verificationId: String, forceResendingToken: ForceResendingToken
           ) {
               // The SMS verification code has been sent to the provided phone number.
               // We now need to ask the user to enter the code and then construct a
               // credential by combining the code with a verification ID.
               // Save the verification ID and resending token for later use.
               this@MainActivity.verificationId = verificationId
               this@MainActivity.forceResendingToken = forceResendingToken
               // ...
           }
       }

   ### Java

       OnVerificationStateChangedCallbacks callbacks =
       new OnVerificationStateChangedCallbacks() {
         @Override
         public void onVerificationCompleted(PhoneAuthCredential credential) {
           // This callback will be invoked in two situations:
           // 1) Instant verification. In some cases, the phone number can be
           //    instantly verified without needing to send or enter a verification
           //    code. You can disable this feature by calling
           //    PhoneAuthOptions.builder#requireSmsValidation(true) when building
           //    the options to pass to PhoneAuthProvider#verifyPhoneNumber().
           // 2) Auto-retrieval. On some devices, Google Play services can
           //    automatically detect the incoming verification SMS and perform
           //    verification without user action.
           this.credential = credential;
         }
         @Override
         public void onVerificationFailed(FirebaseException e) {
           // This callback is invoked in response to invalid requests for
           // verification, like an incorrect phone number.
           if (e instanceof FirebaseAuthInvalidCredentialsException) {
           // Invalid request
           // ...
           } else if (e instanceof FirebaseTooManyRequestsException) {
           // The SMS quota for the project has been exceeded
           // ...
           }
           // Show a message and update the UI
           // ...
         }
         @Override
         public void onCodeSent(
           String verificationId, PhoneAuthProvider.ForceResendingToken token) {
           // The SMS verification code has been sent to the provided phone number.
           // We now need to ask the user to enter the code and then construct a
           // credential by combining the code with a verification ID.
           // Save the verification ID and resending token for later use.
           this.verificationId = verificationId;
           this.forceResendingToken = token;
           // ...
         }
       };

5. Initialize a`PhoneInfoOptions`object with the user's phone number, the multi-factor session, and your callbacks:

   ### Kotlin

       val phoneAuthOptions = PhoneAuthOptions.newBuilder()
           .setPhoneNumber(phoneNumber)
           .setTimeout(30L, TimeUnit.SECONDS)
           .setMultiFactorSession(MultiFactorSession)
           .setCallbacks(callbacks)
           .build()

   ### Java

       PhoneAuthOptions phoneAuthOptions =
         PhoneAuthOptions.newBuilder()
             .setPhoneNumber(phoneNumber)
             .setTimeout(30L, TimeUnit.SECONDS)
             .setMultiFactorSession(multiFactorSession)
             .setCallbacks(callbacks)
             .build();

   By default, instant verification is enabled. To disable it, add a call to`requireSmsValidation(true)`.
6. Send a verification message to the user's phone:

   ### Kotlin

       PhoneAuthProvider.verifyPhoneNumber(phoneAuthOptions)

   ### Java

       PhoneAuthProvider.verifyPhoneNumber(phoneAuthOptions);

   While not required, it's a best practice to inform users beforehand that they will receive an SMS message, and that standard rates apply.
7. Once the SMS code is sent, ask the user to verify the code:

   ### Kotlin

       // Ask user for the verification code.
       val credential = PhoneAuthProvider.getCredential(verificationId, verificationCode)

   ### Java

       // Ask user for the verification code.
       PhoneAuthCredential credential
         = PhoneAuthProvider.getCredential(verificationId, verificationCode);

8. Initialize a`MultiFactorAssertion`object with the`PhoneAuthCredential`:

   ### Kotlin

       val multiFactorAssertion
         = PhoneMultiFactorGenerator.getAssertion(credential)

   ### Java

       MultiFactorAssertion multiFactorAssertion
         = PhoneMultiFactorGenerator.getAssertion(credential);

9. Complete the enrollment. Optionally, you can specify a display name for the second factor. This is useful for users with multiple second factors, since the phone number is masked during the authentication flow (for example, +1\*\*\*\*\*\*1234).

   ### Kotlin

       // Complete enrollment. This will update the underlying tokens
       // and trigger ID token change listener.
       FirebaseAuth.getInstance()
           .currentUser
           ?.multiFactor
           ?.enroll(multiFactorAssertion, "My personal phone number")
           ?.addOnCompleteListener {
               // ...
           }

   ### Java

       // Complete enrollment. This will update the underlying tokens
       // and trigger ID token change listener.
       FirebaseAuth.getInstance()
         .getCurrentUser()
         .getMultiFactor()
         .enroll(multiFactorAssertion, "My personal phone number")
         .addOnCompleteListener(
             new OnCompleteListener<Void>() {
             @Override
             public void onComplete(@NonNull Task<Void> task) {
               // ...
             }
             });

The code below shows a complete example of enrolling a second factor:  

### Kotlin

    val multiFactorAssertion = PhoneMultiFactorGenerator.getAssertion(credential)
    user.multiFactor.session
        .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                val multiFactorSession = task.result
                val phoneAuthOptions = PhoneAuthOptions.newBuilder()
                    .setPhoneNumber(phoneNumber)
                    .setTimeout(30L, TimeUnit.SECONDS)
                    .setMultiFactorSession(multiFactorSession)
                    .setCallbacks(callbacks)
                    .build()
                // Send SMS verification code.
                PhoneAuthProvider.verifyPhoneNumber(phoneAuthOptions)
            }
        }

    // Ask user for the verification code.
    val credential = PhoneAuthProvider.getCredential(verificationId, verificationCode)

    val multiFactorAssertion = PhoneMultiFactorGenerator.getAssertion(credential)

    // Complete enrollment.
    FirebaseAuth.getInstance()
        .currentUser
        ?.multiFactor
        ?.enroll(multiFactorAssertion, "My personal phone number")
        ?.addOnCompleteListener {
            // ...
        }

### Java

    MultiFactorAssertion multiFactorAssertion = PhoneMultiFactorGenerator.getAssertion(credential);
    user.getMultiFactor().getSession()
      .addOnCompleteListener(
          new OnCompleteListener<MultiFactorSession>() {
          @Override
          public void onComplete(@NonNull Task<MultiFactorSession> task) {
            if (task.isSuccessful()) {
              MultiFactorSession multiFactorSession = task.getResult();
              PhoneAuthOptions phoneAuthOptions =
                PhoneAuthOptions.newBuilder()
                    .setPhoneNumber(phoneNumber)
                    .setTimeout(30L, TimeUnit.SECONDS)
                    .setMultiFactorSession(multiFactorSession)
                    .setCallbacks(callbacks)
                    .build();
              // Send SMS verification code.
              PhoneAuthProvider.verifyPhoneNumber(phoneAuthOptions);
            }
          }
          });

    // Ask user for the verification code.
    PhoneAuthCredential credential =
      PhoneAuthProvider.getCredential(verificationId, verificationCode);

    MultiFactorAssertion multiFactorAssertion = PhoneMultiFactorGenerator.getAssertion(credential);
    // Complete enrollment.
    FirebaseAuth.getInstance()
      .getCurrentUser()
      .getMultiFactor()
      .enroll(multiFactorAssertion, "My personal phone number")
      .addOnCompleteListener(
          new OnCompleteListener<Void>() {
          @Override
          public void onComplete(@NonNull Task<Void> task) {
            // ...
          }
          });

Congratulations! You successfully registered a second authentication factor for a user.
| **Important:** You should strongly encourage your users to register more than one second factor for account recovery purposes. If a user only registers a single second factor and later loses access to it, they will be locked out of their account.

## Signing users in with a second factor

To sign in a user with two-factor SMS verification:

1. Sign the user in with their first factor, then catch the`FirebaseAuthMultiFactorException`exception. This error contains a resolver, which you can use to obtain the user's enrolled second factors. It also contains an underlying session proving the user successfully authenticated with their first factor.

   For example, if the user's first factor was an email and password:  

   ### Kotlin

       FirebaseAuth.getInstance()
           .signInWithEmailAndPassword(email, password)
           .addOnCompleteListener(
               OnCompleteListener { task ->
                   if (task.isSuccessful) {
                       // User is not enrolled with a second factor and is successfully
                       // signed in.
                       // ...
                       return@OnCompleteListener
                   }
                   if (task.exception is FirebaseAuthMultiFactorException) {
                       // The user is a multi-factor user. Second factor challenge is
                       // required.
                       val multiFactorResolver =
                           (task.exception as FirebaseAuthMultiFactorException).resolver
                       // ...
                   } else {
                       // Handle other errors, such as wrong password.
                   }
               })

   ### Java

       FirebaseAuth.getInstance()
         .signInWithEmailAndPassword(email, password)
         .addOnCompleteListener(
             new OnCompleteListener<AuthResult>() {
             @Override
             public void onComplete(@NonNull Task<AuthResult> task) {
               if (task.isSuccessful()) {
                 // User is not enrolled with a second factor and is successfully
                 // signed in.
                 // ...
                 return;
               }
               if (task.getException() instanceof FirebaseAuthMultiFactorException) {
                 // The user is a multi-factor user. Second factor challenge is
                 // required.
                 MultiFactorResolver multiFactorResolver = task.getException().getResolver();
                 // ...
               } else {
                 // Handle other errors such as wrong password.
               }
             }
             });

   If the user's first factor is a federated provider, such as OAuth, catch the error after calling`startActivityForSignInWithProvider()`.
2. If the user has multiple secondary factors enrolled, ask them which one to use:

   ### Kotlin

       // Ask user which second factor to use.
       // You can get the list of enrolled second factors using
       //   multiFactorResolver.hints

       // Check the selected factor:
       if (multiFactorResolver.hints[selectedIndex].factorId
           === PhoneMultiFactorGenerator.FACTOR_ID
       ) {
           // User selected a phone second factor.
           val selectedHint =
               multiFactorResolver.hints[selectedIndex] as PhoneMultiFactorInfo
       } else if (multiFactorResolver.hints[selectedIndex].factorId
           === TotpMultiFactorGenerator.FACTOR_ID) {
           // User selected a TOTP second factor.
       } else {
           // Unsupported second factor.
       }

   ### Java

       // Ask user which second factor to use.
       // You can get the masked phone number using
       // resolver.getHints().get(selectedIndex).getPhoneNumber()
       // You can get the display name using
       // resolver.getHints().get(selectedIndex).getDisplayName()
       if ( resolver.getHints()
                      .get(selectedIndex)
                      .getFactorId()
                      .equals( PhoneMultiFactorGenerator.FACTOR_ID ) ) {
       // User selected a phone second factor.
       MultiFactorInfo selectedHint =
         multiFactorResolver.getHints().get(selectedIndex);
       } else if ( resolver
                     .getHints()
                     .get(selectedIndex)
                     .getFactorId()
                     .equals(TotpMultiFactorGenerator.FACTOR_ID ) ) {
         // User selected a TOTP second factor.
       } else {
       // Unsupported second factor.
       }

3. Initialize a`PhoneAuthOptions`object with the hint and multi-factor session. These values are contained in the resolver attached to the`FirebaseAuthMultiFactorException`.

   ### Kotlin

       val phoneAuthOptions = PhoneAuthOptions.newBuilder()
           .setMultiFactorHint(selectedHint)
           .setTimeout(30L, TimeUnit.SECONDS)
           .setMultiFactorSession(multiFactorResolver.session)
           .setCallbacks(callbacks) // Optionally disable instant verification.
           // .requireSmsValidation(true)
           .build()

   ### Java

       PhoneAuthOptions phoneAuthOptions =
         PhoneAuthOptions.newBuilder()
             .setMultiFactorHint(selectedHint)
             .setTimeout(30L, TimeUnit.SECONDS)
             .setMultiFactorSession(multiFactorResolver.getSession())
             .setCallbacks(callbacks)
             // Optionally disable instant verification.
             // .requireSmsValidation(true)
             .build();

4. Send a verification message to the user's phone:

   ### Kotlin

       // Send SMS verification code
       PhoneAuthProvider.verifyPhoneNumber(phoneAuthOptions)

   ### Java

       // Send SMS verification code
       PhoneAuthProvider.verifyPhoneNumber(phoneAuthOptions);

5. Once the SMS code is sent, ask the user to verify the code:

   ### Kotlin

       // Ask user for the verification code. Then, pass it to getCredential:
       val credential =
           PhoneAuthProvider.getCredential(verificationId, verificationCode)

   ### Java

       // Ask user for the verification code. Then, pass it to getCredential:
       PhoneAuthCredential credential
           = PhoneAuthProvider.getCredential(verificationId, verificationCode);

6. Initialize a`MultiFactorAssertion`object with the`PhoneAuthCredential`:

   ### Kotlin

       val multiFactorAssertion = PhoneMultiFactorGenerator.getAssertion(credential)

   ### Java

       MultiFactorAssertion multiFactorAssertion
           = PhoneMultiFactorGenerator.getAssertion(credential);

7. Call`resolver.resolveSignIn()`to complete secondary authentication. You can then access the original sign-in result, which includes the standard provider-specific data and authentication credentials:

   ### Kotlin

       multiFactorResolver
           .resolveSignIn(multiFactorAssertion)
           .addOnCompleteListener { task ->
               if (task.isSuccessful) {
                   val authResult = task.result
                   // AuthResult will also contain the user, additionalUserInfo,
                   // and an optional credential (null for email/password)
                   // associated with the first factor sign-in.

                   // For example, if the user signed in with Google as a first
                   // factor, authResult.getAdditionalUserInfo() will contain data
                   // related to Google provider that the user signed in with;
                   // authResult.getCredential() will contain the Google OAuth
                   //   credential;
                   // authResult.getCredential().getAccessToken() will contain the
                   //   Google OAuth access token;
                   // authResult.getCredential().getIdToken() contains the Google
                   //   OAuth ID token.
               }
           }

   ### Java

       multiFactorResolver
         .resolveSignIn(multiFactorAssertion)
         .addOnCompleteListener(
             new OnCompleteListener<AuthResult>() {
             @Override
             public void onComplete(@NonNull Task<AuthResult> task) {
               if (task.isSuccessful()) {
                 AuthResult authResult = task.getResult();
                 // AuthResult will also contain the user, additionalUserInfo,
                 // and an optional credential (null for email/password)
                 // associated with the first factor sign-in.
                 // For example, if the user signed in with Google as a first
                 // factor, authResult.getAdditionalUserInfo() will contain data
                 // related to Google provider that the user signed in with.
                 // authResult.getCredential() will contain the Google OAuth
                 // credential.
                 // authResult.getCredential().getAccessToken() will contain the
                 // Google OAuth access token.
                 // authResult.getCredential().getIdToken() contains the Google
                 // OAuth ID token.
               }
             }
             });

The code below shows a complete example of signing in a multi-factor user:  

### Kotlin

    FirebaseAuth.getInstance()
        .signInWithEmailAndPassword(email, password)
        .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                // User is not enrolled with a second factor and is successfully
                // signed in.
                // ...
                return@addOnCompleteListener
            }
            if (task.exception is FirebaseAuthMultiFactorException) {
                val multiFactorResolver =
                    (task.exception as FirebaseAuthMultiFactorException).resolver

                // Ask user which second factor to use. Then, get
                // the selected hint:
                val selectedHint =
                    multiFactorResolver.hints[selectedIndex] as PhoneMultiFactorInfo

                // Send the SMS verification code.
                PhoneAuthProvider.verifyPhoneNumber(
                    PhoneAuthOptions.newBuilder()
                        .setActivity(this)
                        .setMultiFactorSession(multiFactorResolver.session)
                        .setMultiFactorHint(selectedHint)
                        .setCallbacks(generateCallbacks())
                        .setTimeout(30L, TimeUnit.SECONDS)
                        .build()
                )

                // Ask user for the SMS verification code, then use it to get
                // a PhoneAuthCredential:
                val credential =
                    PhoneAuthProvider.getCredential(verificationId, verificationCode)

                // Initialize a MultiFactorAssertion object with the
                // PhoneAuthCredential.
                val multiFactorAssertion: MultiFactorAssertion =
                    PhoneMultiFactorGenerator.getAssertion(credential)

                // Complete sign-in.
                multiFactorResolver
                    .resolveSignIn(multiFactorAssertion)
                    .addOnCompleteListener { task ->
                        if (task.isSuccessful) {
                            // User successfully signed in with the
                            // second factor phone number.
                        }
                        // ...
                    }
            } else {
                // Handle other errors such as wrong password.
            }
        }

### Java

    FirebaseAuth.getInstance()
      .signInWithEmailAndPassword(email, password)
      .addOnCompleteListener(
          new OnCompleteListener<AuthResult>() {
          @Override
          public void onComplete(@NonNull Task<AuthResult> task) {
            if (task.isSuccessful()) {
              // User is not enrolled with a second factor and is successfully
              // signed in.
              // ...
              return;
            }
            if (task.getException() instanceof FirebaseAuthMultiFactorException) {
              FirebaseAuthMultiFactorException e =
                (FirebaseAuthMultiFactorException) task.getException();

              MultiFactorResolver multiFactorResolver = e.getResolver();

              // Ask user which second factor to use.
              MultiFactorInfo selectedHint =
                multiFactorResolver.getHints().get(selectedIndex);

              // Send the SMS verification code.
              PhoneAuthProvider.verifyPhoneNumber(
                PhoneAuthOptions.newBuilder()
                    .setActivity(this)
                    .setMultiFactorSession(multiFactorResolver.getSession())
                    .setMultiFactorHint(selectedHint)
                    .setCallbacks(generateCallbacks())
                    .setTimeout(30L, TimeUnit.SECONDS)
                    .build());

              // Ask user for the SMS verification code.
              PhoneAuthCredential credential =
                PhoneAuthProvider.getCredential(verificationId, verificationCode);

              // Initialize a MultiFactorAssertion object with the
              // PhoneAuthCredential.
              MultiFactorAssertion multiFactorAssertion =
                PhoneMultiFactorGenerator.getAssertion(credential);

              // Complete sign-in.
              multiFactorResolver
                .resolveSignIn(multiFactorAssertion)
                .addOnCompleteListener(
                    new OnCompleteListener<AuthResult>() {
                      @Override
                      public void onComplete(@NonNull Task<AuthResult> task) {
                      if (task.isSuccessful()) {
                        // User successfully signed in with the
                        // second factor phone number.
                      }
                      // ...
                      }
                    });
            } else {
              // Handle other errors such as wrong password.
            }
          }
          });

Congratulations! You successfully signed in a user using multi-factor authentication.

## What's next

- [Manage multi-factor users](https://firebase.google.com/docs/auth/admin/manage-mfa-users)programmatically with theAdmin SDK.