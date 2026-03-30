# Source: https://www.mux.com/docs/core/verify-webhook-signatures.md

# Verify webhook signatures
You have the option to verify webhook requests that Mux sends to your endpoints. Mux will include a signature in the request's header. You can use this signature in your code to make sure the request was sent by Mux and not a third party.
## Obtain your signing secret

Before you get started, you will need your signing secret for your webhook. You can find that where you configure webhooks on the [webhooks settings page](https://dashboard.mux.com/settings/webhooks). Please note that the signing secret is different for each webhook endpoint that we notify.

<Image src="/docs/images/webhook-security.png" width={1181} height={479} />

Webhooks contain a header called `mux-signature` with the timestamp and a signature. The timestamp is prefixed by `t=` and the signature is prefixed by a scheme. Schemes start with `v`, followed by an integer. Currently, the only valid signature scheme is `v1`. Mux generates signatures using [HMAC](https://en.wikipedia.org/wiki/HMAC) with [SHA-256](https://en.wikipedia.org/wiki/SHA-2).

```text
Mux-Signature: t=1565220904,v1=20c75c1180c701ee8a796e81507cfd5c932fc17cf63a4a55566fd38da3a2d3d2`
```

## How to verify webhook signatures

### Step 1: Extract the timestamp and signature

Split the header at the `,` character and get the values for `t` (timestamp) and `v1` (the signature)

### Step 2: Prepare the `signed_payload` string

You will need:

* the timestamp from Step 1 as a string (for example: "1565220904")
* the dot character `.`
* the raw request body (this will be JSON in a string format)

### Step 3: Determine the expected signature

Use the 3 components from Step 2 to compute an HMAC with the SHA256 hash function. Depending on the language that you are using this will look something like the following:

```js
secret = 'my secret' // your signing secret
payload = timestamp + "." + request_body
expected_signature = createHmacSha256(payload, secret)
```

### Step 4: Compare signature

Compare the signature in the header to the expected signature. If the signature matches, compute the difference between the current timestamp and the received timestamp, then check to make sure that the timestamp is within our tolerance. By default, our SDKs allow a tolerance of 5 minutes.

## Examples

Our official SDKs for [Node](https://github.com/muxinc/mux-node-sdk) and [Elixir](https://github.com/muxinc/mux-elixir) contain helper methods for verifying Mux webhooks. If you're using one of these languages it's best to use our available helper methods. Note that the helper methods use the raw request body instead of a payload including the timestamp.

```elixir

# check the mux-elixr docs for details and a full example using Phoenix
# https://github.com/muxinc/mux-elixir#verifying-webhook-signatures-in-phoenix
Mux.Webhooks.verify_header(raw_body, signature_header, secret)

```

```go

func generateHmacSignature(webhookSecret, payload string) string {
    h := hmac.New(sha256.New, []byte(webhookSecret))
    h.Write([]byte(payload))
    return hex.EncodeToString(h.Sum(nil))
}

func IsValidMuxSignature(req *http.Request, body []byte) error {
    muxSignature := req.Header.Get("Mux-Signature")

    if muxSignature == "" {
        return errors.New("no Mux-Signature in request header")
    }

    muxSignatureArr := strings.Split(muxSignature, ",")

    if len(muxSignatureArr) != 2 {
        return errors.New(fmt.Sprintf("Mux-Signature in request header should be 2 values long: %s", muxSignatureArr))
    }

    timestampArr := strings.Split(muxSignatureArr[0], "=")
    v1SignatureArr := strings.Split(muxSignatureArr[1], "=")

    if len(timestampArr) != 2 || len(v1SignatureArr) != 2 {
        return errors.New(fmt.Sprintf("missing timestamp: %s or missing v1Signature: %s", timestampArr, v1SignatureArr))
    }

    timestamp := timestampArr[1]
    v1Signature := v1SignatureArr[1]

    webhookSecret := "" //insert secret here or load from config file.
    payload := fmt.Sprintf("%s.%s", timestamp, string(body))
    sha := generateHmacSignature(webhookSecret, payload)

    if sha != v1Signature {
        return errors.New("not a valid mux webhook signature")
    }

    fmt.Println("timestamp sha:", sha)
    fmt.Println("v1Signature:", v1Signature)
    return nil
}

```

```laravel

/**
 * Verify the signature (laravel)
 *
 * @param Request $request
 * @return boolean
 */
protected function verifySignature(Request $request)
{
    // Get the signature from the request header
    $muxSig = $request->header('Mux-Signature');

    if(empty($muxSig)) {
        return false;
    }

    // Split the signature based on ','.
    // Format is 't=[timestamp],v1=[hash]'
    $muxSigArray = explode(',', $muxSig);

    if(empty($muxSigArray) || empty($muxSigArray[0]) || empty($muxSigArray[1])) {
        return false;
    }

    // Strip the first occurence of 't=' and 'v1=' from both strings
    $muxTimestamp = Str::replaceFirst('t=', '', $muxSigArray[0]);
    $muxHash = Str::replaceFirst('v1=', '', $muxSigArray[1]);

    // Create a payload of the timestamp from the Mux signature and the request body with a '.' in-between
    $payload = $muxTimestamp . "." . $request->getContent();

    // Build a HMAC hash using SHA256 algo, using our webhook secret
    $ourSignature = hash_hmac('sha256', $payload, config('mux.webhook_secret'));

    // `hash_equals` performs a timing-safe crypto comparison
    return hash_equals($ourSignature, $muxHash);
}

```

```node

import Mux from '@mux/mux-node';

// check the mux-node-sdk docs for details
// https://github.com/muxinc/mux-node-sdk/blob/master/api.md#webhooks
const mux = new Mux();
mux.webhooks.verifySignature(body, headers, secret);

```

