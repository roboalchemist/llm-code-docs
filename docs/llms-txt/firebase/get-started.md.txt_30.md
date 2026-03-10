# Source: https://firebase.google.com/docs/phone-number-verification/android/get-started.md.txt

<br />

This page describes how to use Firebase Phone Number Verification in an Android app. See the
[overview](https://firebase.google.com/docs/phone-number-verification) for a general description of this
feature.

This page details how to integrate with Firebase PNV using the unified, single-call
API. Calling a single method handles the entire Firebase PNV user flow, from
obtaining user consent to making the necessary network calls to the Firebase PNV
backend. By using this method, you reduce the integration steps to a single
method call.

This API is recommended for most developers; however, if you have specific
requirements not met by the library, see the
[Customize the Firebase Phone Number Verification flow](https://firebase.google.com/docs/phone-number-verification/android/custom-flow) page for information on
implementing a custom flow.

## Before you begin

1. Project owner rights are required to complete onboarding steps, including
   OAuth brand verification.

2. You must have a publicly accessible privacy policy to complete OAuth brand
   verification. You can use Firebase Hosting to create a basic web app to
   host your test privacy policy.

3. Ensure you have a SIM from one of the [supported carriers](https://firebase.google.com/docs/phone-number-verification/pricing#supported-carriers) to test.

## 1. Set up your Firebase project

1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup) if you haven't
   already done so.

2. If you haven't yet specified your app's SHA-256 fingerprint in the
   Firebase console, do so
   from the [*Project settings*](https://console.firebase.google.com/project/_/settings/general/).
   Refer to
   [Authenticating Your Client](https://developers.google.com/android/guides/client-auth)
   for details on how to get your app's SHA-256 fingerprint.

3. You will need to complete the first time onboarding process in the [Firebase console](https://console.firebase.google.com/project/_/phoneverification/sites/?useAutoProject=true).
   This includes [OAuth brand verification](https://support.google.com/cloud/answer/13464321?sjid=16326092754406046967-NC),
   and a privacy policy review. If you are preparing a non-production testing
   app, you can use Firebase Hosting to create a basic web app to host your
   test privacy policy.

4. Firebase PNV requires the Blaze plan. If you have not already upgraded your
   project to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), you will be prompted to during
   onboarding.

   Although Firebase PNV requires a billing account to be attached to your Firebase
   project, during the preview phase, you won't be billed for the service.
5. On the [Credentials](https://console.cloud.google.com/apis/credentials?project=_)
   page of the console, open your Android API key and add the Firebase Phone Number Verification
   API to the list of selected APIs.

## 2. Add the Firebase PNV library to your app

In your **module (app-level) Gradle file** (usually
`<project>/<app-module>/build.gradle.kts` or
`<project>/<app-module>/build.gradle`), add the dependency for the
Firebase Phone Number Verification library for Android.

    dependencies {
        // Add the dependency for the Firebase Phone Number Verification library
        implementation("com.google.firebase:firebase-pnv:16.0.0-beta01")
    }

## 3. Recommended: Check for Firebase PNV support

To help you determine when to show number entry UI or explainer UI, on app
launch it is recommended to check if the device and its SIM card support
Firebase PNV. This is a pre-check that doesn't require user consent. You can
use the result of this test to decide whether to initiate the Firebase PNV flow or
to use an alternative method of phone number verification, such as SMS.

To check the device for compatibility, call the `getVerificationSupportInfo()`
method:

### Kotlin

    import com.google.firebase.pnv.FirebasePhoneNumberVerification

    // Get an instance of the SDK.
    val fpnv = FirebasePhoneNumberVerification.getInstance()

    // Check all SIMs for support.
    fpnv.getVerificationSupportInfo()
      .addOnSuccessListener { results ->
        if (results.any { it.isSupported() }) {
          // At least one SIM is supported; proceed with FPNV flow
        } else {
          // No SIMs are supported, so fall back to SMS verification.
        }
      }
      .addOnFailureListener { e ->
        // Handle error.
      }

The `getVerificationSupportInfo()` returns a list of `VerificationSupportResult`
objects, one for each SIM slot. If at least one SIM card is supported, you can
proceed with the Firebase PNV flow.

## 4. Initiate the verification flow

To initiate the Firebase PNV flow, create a new instance of
`FirebasePhoneNumberVerification`, passing in an `Activity` context. An
`Activity` context is necessary for the SDK to present a consent screen to the
user. Then, call the object's `getVerifiedPhoneNumber()` method:

### Kotlin

    import com.google.firebase.pnv.FirebasePhoneNumberVerification

    // Get an instance of the SDK _with an Activity context_:
    val fpnv = FirebasePhoneNumberVerification.getInstance(this@MainActivity)

    // Call getVerifiedPhoneNumber
    fpnv.getVerifiedPhoneNumber()
      .addOnSuccessListener { result ->
        val phoneNumber = result.getPhoneNumber()
        val token = result.getToken()
        // Verification successful. Send token to your backend.
      }
      .addOnFailureListener { e ->
        // Handle failures, such as the user declining consent or a network error.
      }

The `getVerifiedPhoneNumber()` method carries out the entire phone number
verification flow, including:

- Using the Android Credential Manager to acquire user consent to share their phone number.
- Making the request to the Firebase PNV backend.
- Returning a verified phone number for the device (this is when billing happens).

> [!TIP]
> **Tip:** As a UI refinement, you should display a loading spinner before calling `getVerifiedPhoneNumber`, and dismiss the spinner after the operation completes, either successfully or with an error. Design the loading spinner to be smaller than the consent screen so that it is completely obscured by it when the screen is visible.

## 5. Using the Firebase PNV token

If the flow succeeds, the `getVerifiedPhoneNumber()` method returns the verified
phone number and a signed token containing it. You can use this data in your app
as documented by your privacy policy.

If you use the verified phone number outside the app client, you should pass
around the token instead of the phone number itself so you can verify its
integrity when you use it. To verify the token, you can use any JWT verification
library. Use the library to verify all of the following:

- The `typ` header is set to `JWT`.

- The token is signed using one of the keys published at the Firebase PNV JWKS
  endpoint with `ES256` algorithm:

      https://fpnv.googleapis.com/v1beta/jwks

- The issuer claims contains your Firebase project number and is in
  the following format:

      https://fpnv.googleapis.com/projects/FIREBASE_PROJECT_NUMBER

  You can find your Firebase project number on the
  [Project settings](https://console.firebase.google.com/project/_/settings/general/)
  page of the Firebase console.
- The audience claim is a list that contains your Firebase project number and
  project ID and is in the following format:

      [
        https://fpnv.googleapis.com/projects/FIREBASE_PROJECT_NUMBER,
        https://fpnv.googleapis.com/projects/FIREBASE_PROJECT_ID,
      ]

- The token has not expired.

### Example

As a brief example, the following Express.js app receives an Firebase PNV token from
an HTTP `POST` request and uses a JWT verification library to check the
signature and claims of the token:

### Node.js

    import express from "express";
    import { JwtVerifier } from "aws-jwt-verify";

    // Find your Firebase project number in the Firebase console.
    const FIREBASE_PROJECT_NUMBER = "123456789";

    // The issuer and audience claims of the FPNV token are specific to your
    // project.
    const issuer = `https://fpnv.googleapis.com/projects/${FIREBASE_PROJECT_NUMBER}`;
    const audience = `https://fpnv.googleapis.com/projects/${FIREBASE_PROJECT_NUMBER}`;

    // The JWKS URL contains the current public signing keys for FPNV tokens.
    const jwksUri = "https://fpnv.googleapis.com/v1beta/jwks";

    // Configure a JWT verifier to check the following:
    // - The token is signed by Google
    // - The issuer and audience claims match your project
    // - The token has not yet expired (default behavior)
    const fpnvVerifier = JwtVerifier.create({ issuer, audience, jwksUri });

    const app = express();

    app.post('/verifiedPhoneNumber', async (req, res) => {
        if (!req.body) return res.sendStatus(400);
        // Get the token from the body of the request.
        const fpnvToken = req.body;
        try {
            // Attempt to verify the token using the verifier configured
            previously.
            const verifiedPayload = await fpnvVerifier.verify(fpnvToken);

            // If verification succeeds, the subject claim of the token contains the
            // verified phone number. You can use this value however it's needed by
            // your app.
            const verifiedPhoneNumber = verifiedPayload.sub;
            // (Do something with it...)

            return res.sendStatus(200);
        } catch {
            // If verification fails, reject the token.
            return res.sendStatus(400);
        }
    });

    app.listen(3000);

### Sign in to a Firebase app

For an example of using the Firebase PNV token in a Firebase Authentication sign-in flow,
see the [Authenticate with Firebase using Firebase Phone Number Verification](https://firebase.google.com/docs/phone-number-verification/android/sign-in) page.