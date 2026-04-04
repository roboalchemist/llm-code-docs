# Source: https://firebase.google.com/docs/phone-number-verification/android/sign-in.md.txt

<br />

In the Firebase PNV public preview, Firebase Authentication cannot directly accept an
Firebase PNV token for sign-in; however, you can enable users to sign in with
Firebase PNV by using Firebase Authentication's custom authentication feature.

## Create a token exchange endpoint

The key step in implementing a custom authentication solution in Firebase is to
create an endpoint that can receive a Firebase PNV token, validate it, and then
issue a Firebase custom authentication token. Your application can then use this
custom token to sign in the user.

This endpoint can be hosted on any platform, but in the following example, the
endpoint is hosted using Cloud Functions for Firebase:

### Node.js

    import { JwtVerifier } from "aws-jwt-verify";
    import { getApp } from "firebase-admin/app";
    import { getAuth, UserRecord } from "firebase-admin/auth";
    import { onRequest } from "firebase-functions/https";

    // Because we're deploying to Cloud Functions for Firebase, admin credentials
    // are automatically available.
    const app = getApp();
    const authAdmin = getAuth(app);

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
    // - The token has not yet expired (default begavior)
    const fpnvVerifier = JwtVerifier.create({ issuer, audience, jwksUri });

    // This Cloud Function is your token exchange endpoint. You pass the endpoint an
    // FPNV token, and the Cloud Function verifies it and exchanges it for a
    // Firebase Auth token corresponding to the same user.
    export const signInWithFpnv = onRequest(async (req, res) => {
        // Get the FPNV token from the request body.
        const fpnvToken = req.body?;
        if (!fpnvToken) {
            res.sendStatus(400);
            return;
        }

        let verifiedPhoneNumber;
        try {
            // Attempt to verify the token using the verifier configured above.
            const verifiedPayload = await fpnvVerifier.verify(fpnvToken);

            // If verification succeeds, the subject claim of the token contains the
            // verified phone number.
            verifiedPhoneNumber = verifiedPayload.sub;
        } catch {
            // If verification fails, reject the token.
            res.sendStatus(403);
            return;
        }

        // Now that you have a verified phone number, look it up in your Firebase
        // project's user database.
        let user: UserRecord;
        try {
            // If a user account already exists with the phone number, retrieve it.
            user = await authAdmin.getUserByPhoneNumber(verifiedPhoneNumber);
        } catch {
            // Otherwise, create a new user account using the phone number.
            user = await authAdmin.createUser({phoneNumber: verifiedPhoneNumber});
        }

        // Finally, mint a Firebase custom auth token containing the UID of the user
        // you looked up or created. Return this token to the caller.
        const authToken = await authAdmin.createCustomToken(user.uid);
        res.status(200).send(authToken);
        return;
    });

## Sign in with the custom auth token

Once the endpoint is deployed, sign users into Firebase by following these
steps:

1. Get an Firebase PNV token using the flow described on the
   [Get started with Firebase Phone Number Verification](https://firebase.google.com/docs/phone-number-verification/android/get-started) page.

2. Pass this token to the Cloud Functions endpoint. The endpoint will return to
   your app a custom authentication token, which you can pass to
   [`signInWithCustomToken()`](https://firebase.google.com/docs/auth/android/custom-auth).

   For example, you could use Retrofit to write a method,
   `signInWithFpnvToken()`, that has a similar interface to one of Firebase's
   `signin`- methods:

   ### Kotlin

       class FpnvSigninExample {
           interface FPNVTokenExchangeService {
               @POST("signInWithFpnv")
               suspend fun signInWithFpnv(@Body fpnvToken: String): String
           }

           val retrofit = Retrofit.Builder()
               .baseUrl("https://example-project.cloudfunctions.net/")
               .build()
           val service: FPNVTokenExchangeService = retrofit.create(FPNVTokenExchangeService::class.java)

           suspend fun signInWithFpnvToken(fpnvToken: String): Task<AuthResult?> = coroutineScope {
               val authToken = service.signInWithFpnv(fpnvToken)
               return@coroutineScope Firebase.auth.signInWithCustomToken(authToken)
           }
       }