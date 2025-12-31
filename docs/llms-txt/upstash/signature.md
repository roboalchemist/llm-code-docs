# Source: https://upstash.com/docs/qstash/howto/signature.md

# Verify Signatures

We send a JWT with each request. This JWT is signed by your individual secret
signing key and sent in the `Upstash-Signature` HTTP header.

You can use this signature to verify the request is coming from QStash.

<img src="https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/signing-key-logic.png?fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=4f2a27e3244e694dce6b3c3f9b64f9d7" alt="" data-og-width="1178" width="1178" data-og-height="419" height="419" data-path="img/qstash/signing-key-logic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/signing-key-logic.png?w=280&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=01630c1e0e7b17b0829d83390698fa66 280w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/signing-key-logic.png?w=560&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=bae37f3a791b85e8c21b57ad6ee99102 560w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/signing-key-logic.png?w=840&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=aaf8f0b21b736d320e546db3be730053 840w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/signing-key-logic.png?w=1100&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=216221b2c4f005976ede5e6571bd0812 1100w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/signing-key-logic.png?w=1650&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=44720ddcf414f81ba22a68dc11f26f7a 1650w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/signing-key-logic.png?w=2500&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=1cdfc23987612a6ad3d648e509ed1e14 2500w" />

<Warning>
  You need to keep your signing keys in a secure location.
  Otherwise some malicious actor could use them to send requests to your API as if they were coming from QStash.
</Warning>

## Verifying

You can use the official QStash SDKs or implement a custom verifier either by using [an open source library](https://jwt.io/libraries) or by processing the JWT manually.

### Via SDK (Recommended)

QStash SDKs provide a `Receiver` type that simplifies signature verification.

<CodeGroup>
  ```typescript Typescript theme={"system"}
  import { Receiver } from "@upstash/qstash";

  const receiver = new Receiver({
    currentSigningKey: "YOUR_CURRENT_SIGNING_KEY",
    nextSigningKey: "YOUR_NEXT_SIGNING_KEY",
  });

  // ... in your request handler

  const signature = req.headers["Upstash-Signature"];
  const body = req.body;

  const isValid = await receiver.verify({
    body,
    signature,
    url: "YOUR-SITE-URL",
  });
  ```

  ```python Python theme={"system"}
  from qstash import Receiver

  receiver = Receiver(
      current_signing_key="YOUR_CURRENT_SIGNING_KEY",
      next_signing_key="YOUR_NEXT_SIGNING_KEY",
  )

  # ... in your request handler

  signature, body = req.headers["Upstash-Signature"], req.body

  receiver.verify(
      body=body,
      signature=signature,
      url="YOUR-SITE-URL",
  )
  ```

  ```go Golang theme={"system"}
  import "github.com/qstash/qstash-go"

  receiver := qstash.NewReceiver("<CURRENT_SIGNING_KEY>", "NEXT_SIGNING_KEY")

  // ... in your request handler

  signature := req.Header.Get("Upstash-Signature")
  body, err := io.ReadAll(req.Body)
  // handle err

  err := receiver.Verify(qstash.VerifyOptions{
      Signature: signature,
      Body:      string(body),
      Url:       "YOUR-SITE-URL", // optional
  })
  // handle err
  ```
</CodeGroup>

<Warning>Depending on the environment, the body might be parsed into an object by the HTTP handler if it is JSON.
Ensure you use the raw body string as is. For example, converting the parsed object back to a string (e.g., JSON.stringify(object)) may cause inconsistencies and result in verification failure.</Warning>

### Manual verification

If you don't want to use the SDKs, you can implement your own verifier either by using an open-source library or by manually processing the JWT.

The exact implementation depends on the language of your choice and the library if you use one.
Instead here are the steps you need to follow:

1. Split the JWT into its header, payload and signature
2. Verify the signature
3. Decode the payload and verify the claims
   * `iss`: The issuer must be`Upstash`.
   * `sub`: The subject must the url of your API.
   * `exp`: Verify the token has not expired yet.
   * `nbf`: Verify the token is already valid.
   * `body`: Hash the raw request body using `SHA-256` and compare it with the
     `body` claim.

You can also reference the implementation in our
[Typescript SDK](https://github.com/upstash/sdk-qstash-ts/blob/main/src/receiver.ts#L82).

After you have verified the signature and the claims, you can be sure the
request came from Upstash and process it accordingly.

## Claims

All claims in the JWT are listed [here](/qstash/features/security#claims)
