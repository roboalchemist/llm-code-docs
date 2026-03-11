# Source: https://www.mux.com/docs/guides/show-live-stream-health-stats.md

# Show live stream health stats to your streamer
Learn how to get the live stream health stats using the Live Stream Stats API.
In this guide you will learn how to use the Live Stream Health Stats<BetaTag /> API in order to embed the live stream health stats for a particular live stream ID into your applications. A common use case is when you want to show the live stream stats to your streamer during a live event, so that the streamer can monitor the status and take actions when issues occur.

<Callout type="info">
  The Live Stream Stats API is not a 1:1 mapping of what you see on the [Live Stream Health page in the Mux dashboard](/docs/guides/debug-live-stream-issues).
</Callout>

You will use JSON Web Tokens to authenticate to this API.

## 1. Understand Live Stream Stats

The Live Stream Stats API returns **Stream Drift Session Average**, **Stream Drift Deviation From Rolling Average**, and **Status**. Before we dive into each of them, understanding a couple of terms here might be helpful:

* **Wallclock time**: Also called the real-world time.
* **Stream drift**: The difference between elapsed media time and elapsed wallclock time. For example, if your encoder has been connected for 10 seconds and it has sent 5 seconds of media during that time, then your current stream drift would be 5s.

Now keep reading below for the metrics the API returns and their definitions.

### Stream Drift Session Average

**Stream Drift Session Average** is the running average of **stream drift** for the lifetime of an ingest connection. It applies a smoothing function to the potentially jagged, fluctuating raw metric. Use this metric as an indication of the average offset between the elapsed wallclock time and media time throughout the whole session.

The value we return from the API is measured in miliseconds and is continuously updated with each measurement taken. It is reset whenever the encoder disconnects.

### Stream Drift Deviation From Rolling Average

To get an indication of whether the current drift is consistent (good) or growing (bad), use **Deviation From Rolling Average**. It is the difference between current **stream drift** and current **stream drift rolling average**. The rolling average only takes the last ~30s of data into account, so it represents the recent drift, rather than measurements taken potentially long time ago. Disparities between current drift and the rolling average can be a good indicator because session average moves slower and may not reflect the latest status.

Use this metric to understand whether the stream is experiencing issues at the moment. When it is, the **Deviation From Rolling Average** will likely be high.

### Status

The `status` returned from the Live Stream Health API could be any of the following values: `excellent`, `good`, `poor`, or `unknown`.

* `excellent`: The Stream Drift Deviation From Rolling Average is less than or equal to 500ms
* `good`: The Stream Drift Deviation From Rolling Average is less than or equal to 1s but greater than 500ms
* `poor`: The Stream Drift Deviation From Rolling Average is greater than 1s
* `unknown`: We are unable to calculate the stream drift. This is usually because the live stream is inactive and/or we have not received any data about it for a few minutes.

Use `status` as an indicator of the latest health status of the live stream ingest. A common use case is to render color coded UI for your streamer's ease-of-use based on the status information, such as green, yellow, or red. You can also check out our pre-built UI to monitor the status by going to the Mux Dashboard for the specific live stream.

## 2. Create a Signing Key

Signing keys can be managed (created, deleted, listed) from the [Signing Keys settings](https://dashboard.mux.com/settings/signing-keys) of the Mux dashboard or via the Mux System API.

<Callout type="warning">
  When making a request to the System API to generate a signing key, the access
  token being used must have the System permission. You can confirm whether your
  access token has this permission by going to Settings > API Access Token. If
  your token doesn't have the System permission listed, you'll need to generate
  another access token with all of the permissions you need, including the
  System permission.
</Callout>

When creating a new signing key, the API will generate a 2048-bit RSA key pair and return the private key and a generated key ID; the public key will be stored at Mux to validate signed tokens. Store the private key in a secure manner.

You probably only need one signing key active at a time and can use the same signing key when requesting live stream stats for multiple live streams. However, you can create multiple signing keys to enable key rotation, creating a new key and deleting the old only after any existing signed URLs have expired.

### Example request

```bash
curl -X POST \
-H "Content-Type: application/json" \
-u ${MUX_TOKEN_ID}:${MUX_TOKEN_SECRET} \
'https://api.mux.com/system/v1/signing-keys'
```

### Example response

```json
// POST https://api.mux.com/system/v1/signing-keys
{
  "data": {
    "private_key": "(base64-encoded PEM file with private key)",
    "id": "(unique signing-key identifier)",
    "created_at": "(UNIX Epoch seconds)”
  }
}
```

<Callout type="warning">
  Be sure that the signing key's environment (Staging, Production, etc.) matches
  the environment of the live streams you would like to call for! When creating a signing
  key via API, the environment of the access token used for authentication will
  be used.
</Callout>

This can also be done manually via the UI. If you choose to create and download your signing key as a PEM file from UI, you will need to base64 encode it before using it with (most) libraries.

```bash
❯ cat /path/to/file/my_signing_key.pem | base64
LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktL...
```

## 3. Generate a JSON Web Token

The following JWT claims are required:

| Claim Code | Description                | Value                                                                                                                                                              |
| :--------- | :------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sub`      | Subject of the JWT         | The ID for which counts will be returned                                                                                                                           |
| `aud`      | Audience (identifier type) | `live_stream_id` (Mux Video Live Stream ID) |
| `exp`      | Expiration time            | UNIX Epoch seconds when the token expires. Use this to ensure any tokens that are distributed become invalid after a period of time.                               |
| `kid`      | Key Identifier             | Key ID returned when signing key was created                                                                                                                       |

<Callout type="warning">
  Live Stream ID is available to Mux
  Video customers only and is generated by Mux. Be sure to double check both
  the query ID type and value!
</Callout>

### Expiration time

Expiration time should be at least the duration of the live stream. When the signed URL expires, you will no longer be able to receive live stream stats data from the API.

<Callout type="info">
  [See the related video documentation](/docs/guides/secure-video-playback#expiration-time)
</Callout>

## 4. Signing the JWT

The steps can be summarized as:

1. Load the private key used for signing
2. Assemble the claims (`sub`, `aud`, `exp`, `kid` etc) in a map
3. Encode and sign the JWT using the claims map and private key and the RS256 algorithm.

There are dozens of software libraries for creating and reading JWTs. Whether you’re writing in Go, Elixir, Ruby, or a dozen other languages, don’t fret, there’s probably a JWT library that you can rely on. For a list of open source libraries to use, check out [jwt.io](https://jwt.io/libraries).

<Callout type="warning">
  The following examples assume you're working with either a private key
  returned from the API, or copy & pasted from the Dashboard, **not** when
  downloaded as a PEM file. If you've downloaded it as a PEM file, you will need
  to base64 encode the file contents.
</Callout>

```go

package main

import (
    "encoding/base64"
    "fmt"
    "log"
    "time"
    "github.com/golang-jwt/jwt/v4"
)

func main() {

    myId := ""       // Enter the id for which you would like to get counts here
    myIdType := ""   // Enter the type of ID provided in my_id; one of video_id | asset_id | playback_id | live_stream_id
    keyId := ""      // Enter your signing key id here
    key := ""        // Enter your base64 encoded private key here

    decodedKey, err := base64.StdEncoding.DecodeString(key)
    if err != nil {
        log.Fatalf("Could not base64 decode private key: %v", err)
    }

    signKey, err := jwt.ParseRSAPrivateKeyFromPEM(decodedKey)
    if err != nil {
        log.Fatalf("Could not parse RSA private key: %v", err)
    }

    token := jwt.NewWithClaims(jwt.SigningMethodRS256, jwt.MapClaims{
        "sub": myId,
        "aud": myIdType,
        "exp": time.Now().Add(time.Minute * 15).Unix(),
        "kid": keyId,
    })

    tokenString, err := token.SignedString(signKey)
    if err != nil {
        log.Fatalf("Could not generate token: %v", err)
    }

    fmt.Println(tokenString)
}

```

```node

// using @mux/mux-node@8

import Mux from '@mux/mux-node';
const mux = new Mux();
const myId = ''; // Enter the id for which you would like to get counts here
const myIdType = ''; // Enter the type of ID provided in myId; one of video_id | asset_id | playback_id | live_stream_id
const signingKeyId = ''; // Enter your Mux signing key id here
const privateKeyBase64 = ''; // Enter your Mux base64 encoded private key here

const getViewerCountsToken = async () => {
    return await mux.jwt.signViewerCounts(myId, {
        expiration: '1 day',
        type: myIdType,
        keyId: signingKeyId,
        keySecret: privateKeyBase64,
    });
};

const sign = async () => {
    const token = await getViewerCountsToken();
    console.log(token);
};

sign();

```

```php

<?php

  // Using https://github.com/firebase/php-jwt

  use \Firebase\JWT\JWT;

  $myId = "";       // Enter the id for which you would like to get counts here
  $myIdType = "";   // Enter the type of ID provided in my_id; one of video_id | asset_id | playback_id | live_stream_id
  $keyId = "";      // Enter your signing key id here
  $keySecret = "";  // Enter your base64 encoded private key here

  $payload = array(
  "sub" => $myId,
  "aud" => $myIdType,
  "exp" => time() + 600, // Expiry time in epoch - in this case now + 10 mins
  "kid" => $keyId
  );

  $jwt = JWT::encode($payload, base64_decode($keySecret), 'RS256');

  print "$jwt\n";

?>

```

```python

# This example uses pyjwt / cryptography:
# pip install pyjwt
# pip install cryptography

import jwt
import base64
import time

my_id = ''              # Enter the id for which you would like to get counts here
my_id_type = ''         # Enter the type of ID provided in my_id; one of video_id | asset_id | playback_id | live_stream_id
signing_key_id = ''     # Enter your signing key id here
private_key_base64 = '' # Enter your base64 encoded private key here

private_key = base64.b64decode(private_key_base64)

payload = {
    'sub': my_id,
    'aud': my_id_type,
    'exp': int(time.time()) + 3600, # 1 hour
}
headers = {
    'kid': signing_key_id
}

encoded = jwt.encode(payload, private_key, algorithm="RS256", headers=headers)
print(encoded)

```

```ruby

require 'base64'
require 'jwt'

def sign_url(subject, audience, expires, signing_key_id, private_key, params = {})
    rsa_private = OpenSSL::PKey::RSA.new(Base64.decode64(private_key))
    payload = {sub: subject, aud: audience, exp: expires.to_i, kid: signing_key_id}
    payload.merge!(params)
    JWT.encode(payload, rsa_private, 'RS256')
end

my_id = ''                 # Enter the id for which you would like to get counts here
my_id_type = ''            # Enter the type of ID provided in my_id; one of video_id | asset_id | playback_id | live_stream_id
signing_key_id = ''        # Enter your signing key id here
private_key_base64 = ''    # Enter your base64 encoded private key here

token = sign_url(my_id, my_id_type, Time.now + 3600, signing_key_id, private_key_base64)

```



## 5. Making a Request

Supply the JWT in the resource URL using the `token` query parameter. The API will inspect and validate the JWT to make sure the request is allowed.

Example:

```bash
curl 'https://stats.mux.com/live-stream-health?token={JWT}'
```

Response:

```json
{
  "data": [
    {
      "ingest_health": {
        "updated_at": "2022-11-14T17:32:23",
        "stream_drift_session_avg": 384,
        "stream_drift_deviation_from_rolling_avg": 12,
        "status": "excellent",
        },
    },
  ],
}
```

* `stream_drift_session_avg` is the session average of stream drift. Use this to represent the overall health of the stream.
* `stream_drift_deviation_from_rolling_avg` is the delta between the current stream drift and the rolling average. Use this to represent the latest stream health.
