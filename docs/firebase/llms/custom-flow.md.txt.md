# Source: https://firebase.google.com/docs/phone-number-verification/android/custom-flow.md.txt

<br />

The [Get started with Firebase Phone Number Verification](https://firebase.google.com/docs/phone-number-verification/android/get-started) page details how to integrate
with Firebase PNV using the `getVerifiedPhoneNumber()` method, which handles
the entire Firebase PNV flow, from obtaining user consent to making the
necessary network calls to the Firebase PNV backend.

The single-method API (`getVerifiedPhoneNumber()`) is recommended for most
developers. However, if you need finer-grained control over the interaction with
Android Credential Manager--for example, to request other credentials along with
the phone number--the
Firebase PNV library also provides the following two methods, each of which handles
a different interaction with the Firebase PNV backend:

- `getDigitalCredentialPayload()` gets a server-signed request that you will use to invoke Credential Manager.
- `exchangeCredentialResponseForPhoneNumber()` exchanges the response from Credential Manager for a signed token containing the verified phone number. Billing will occur at this step.

Between calling each of those methods, you are responsible for handling the
interaction with Android's Credential Manager APIs. This page gives an overview
of how you implement this three-part flow.

## Before you begin

Set up your Firebase project and import the Firebase PNV dependencies as described
on the [Get started](https://firebase.google.com/docs/phone-number-verification/android/get-started) page.

## 1. Get the Digital Credential request payload

Call the `getDigitalCredentialPayload()` method to generate a request for the
device's phone number. In the next step, this request will be the payload of
your interaction with the Credential Manager API.

    // This instance does not require an Activity context.
    val fpnv = FirebasePhoneNumberVerification.getInstance()

    // Your request should include a nonce, which will propagate through the flow
    // and be present in the final response from FPNV. See the section "Verifying
    // the Firebase PNV token" for details on generating and verifying this.
    val nonce = fetchNonceFromYourServer()

    fpnv.getDigitalCredentialPayload(nonce, "https://example.com/privacy-policy")
      .addOnSuccessListener { fpnvDigitalCredentialPayload ->
        // Use the payload in the next step.
        // ...
      }
      .addOnFailureListener { e -> /* Handle payload fetch failure */ }

## 2. Make a digital credential request using the Credential Manager

Next, pass the request to the Credential Manager.

To do so, you need to wrap the request payload in a DigitalCredential API
request. This request must include the same nonce you passed to
`getDigitalCredentialPayload()`.

    // This example uses string interpolation for clarity, but you should use some kind of type-safe
    // serialization method.
    fun buildDigitalCredentialRequestJson(nonce: String, fpnvDigitalCredentialPayload: String) = """
        {
          "requests": [
            {
              "protocol": "openid4vp-v1-unsigned",
              "data": {
                "response_type": "vp_token",
                "response_mode": "dc_api",
                "nonce": "$nonce",
                "dcql_query": { "credentials": [$fpnvDigitalCredentialPayload] }
              }
            }
          ]
        }
    """.trimIndent()

Having done so, you can make the request using the Credential Manager API:

    suspend fun makeFpnvRequest(
      context: Activity, nonce: String, fpnvDigitalCredentialPayload: String): GetCredentialResponse {
      // Helper function to build the digital credential request (defined above).
      // Pass the same nonce you passed to getDigitalCredentialPayload().
      val digitalCredentialRequestJson =
        buildDigitalCredentialRequestJson(nonce, fpnvDigitalCredentialPayload)

      // CredentialManager requires an Activity context.
      val credentialManager = CredentialManager.create(context)

      // Build a Credential Manager request that includes the Firebase PNV option. Note that
      // you can't combine the digital credential option with other options.
      val request = GetCredentialRequest.Builder()
        .addCredentialOption(GetDigitalCredentialOption(digitalCredentialRequestJson))
        .build()

      // getCredential is a suspend function, so it must run in a coroutine scope,
      val cmResponse: GetCredentialResponse = try {
        credentialManager.getCredential(context, request)
      } catch (e: GetCredentialException) {
        // If the user cancels the operation, the feature isn't available, or the
        // SIM doesn't support the feature, a GetCredentialCancellationException
        // will be returned. Otherwise, a GetCredentialUnsupportedException will
        // be returned with details in the exception message.
        throw e
      }
      return cmResponse
    }

If the Credential Manager call succeeds, its response will contain a digital
credential, which you can extract using code like the following example:

    val dcApiResponse = extractApiResponse(cmResponse)

    fun extractApiResponse(response: GetCredentialResponse): String {
      val credential = response.credential
      when (credential) {
        is DigitalCredential -> {
          val json = JSONObject(credential.credentialJson)
          val firebaseJwtArray =
              json.getJSONObject("data").getJSONObject("vp_token").getJSONArray("firebase")
          return firebaseJwtArray.getString(0)

        }
        else -> {
          // Handle any unrecognized credential type here.
          Log.e(TAG, "Unexpected type of credential ${credential.type}")
        }
      }
    }

## 3. Exchange the digital credential response for a Firebase PNV token

Finally, call the `exchangeCredentialResponseForPhoneNumber()` method to
exchange the digital credential response for the verified phone number and an
Firebase PNV token:

    fpnv.exchangeCredentialResponseForPhoneNumber(dcApiResponse)
      .addOnSuccessListener { result ->
        val phoneNumber = result.getPhoneNumber()
        // Verification successful
      }
      .addOnFailureListener { e -> /* Handle exchange failure */ }

This step will trigger billing when it successfully completes and the verified
phone number is returned to your app.

## 4. Verifying the Firebase PNV token

If the flow succeeds, the `getVerifiedPhoneNumber()` method returns the verified
phone number and a signed token containing it. You can use this data in your app
as documented by your privacy policy.

If you use the verified phone number outside the app client, you should pass
around the token instead of the phone number itself so you can verify its
integrity when you use it. To verify tokens, you need to implement two
endpoints:

- A nonce generation endpoint
- A token verification endpoint

The implementation of these endpoints is up to you; the following examples show
how you might implement them using Node.js and Express.

### Generating nonces

This endpoint is responsible for generating and temporarily storing single-use
values called nonces, which are used to prevent replay attacks against your
endpoints. As an example, you might have an Express route defined like this:

    app.get('/fpnvNonce', async (req, res) => {
        const nonce = crypto.randomUUID();

        // TODO: Save the nonce to a database, key store, etc.
        // You should also assign the nonce an expiration time and periodically
        // clear expired nonces from your database.
        await persistNonce({
            nonce,
            expiresAt: Date.now() + 180000, // Give it a short duration.
        });

        // Return the nonce to the caller.
        res.send({ nonce });
    });

This is the endpoint that the placeholder function,
`fetchNonceFromYourServer()`, in Step 1 would call. The nonce will propagate
through the various network calls that the client performs and eventually make
its way back to your server in the Firebase PNV token. In the next step, you verify
that the token contains a nonce that you generated.

### Verifying tokens

This endpoint receives Firebase PNV tokens from your client and verifies their
authenticity. To verify a token, you need to check:

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

- The token contains a valid nonce. A nonce is valid if:

  - You generated it (that is, it can be found in whatever persistence mechanism you're using)
  - It hasn't already been used
  - It hasn't expired

For example, the Express implementation might look something like the following:

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
    // - The token has not yet expired (default begavior)
    const fpnvVerifier = JwtVerifier.create({ issuer, audience, jwksUri });

    app.post('/verifiedPhoneNumber', async (req, res) => {
        if (!req.body) return res.sendStatus(400);
        // Get the token from the body of the request.
        const fpnvToken = req.body;
        try {
            // Attempt to verify the token using the verifier configured above.
            const verifiedPayload = await fpnvVerifier.verify(fpnvToken);

            // Now that you've verified the signature and claims, verify the nonce.
            // TODO: Try to look up the nonce in your database and remove it if it's
            // found; if it's not found or it's expired, throw an error.
            await testAndRemoveNonce(verifiedPayload.nonce);

            // Only after verifying the JWT signature, claims, and nonce, get the
            // verified phone number from the subject claim.
            // You can use this value however it's needed by your app.
            const verifiedPhoneNumber = verifiedPayload.sub;
            // (Do something with it...)

            return res.sendStatus(200);
        } catch {
            // If verification fails, reject the token.
            return res.sendStatus(400);
        }
    });