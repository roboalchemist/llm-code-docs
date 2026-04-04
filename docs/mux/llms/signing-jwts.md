# Source: https://www.mux.com/docs/guides/signing-jwts.md

# Signing JWTs
JSON Web Tokens are an open, industry standard method for representing claims securely between two parties. Mux APIs leverage JWTs to authenticate requests.
## What is a JWT?

JWTs are made up of a header, a payload, and a signature. The header contains metadata useful for decrypting the rest of the token. The payload contains configuration options. And the signature is generated from a signing key-pair. More information can be found at [jwt.io](https://jwt.io/).

In order to sign the JWT you must create a signing key. Signing keys can be created from the [Signing Keys section](https://dashboard.mux.com/settings/signing-keys) of the Mux Dashboard or via the <ApiRefLink href="/docs/api-reference/system/signing-keys">Mux System API</ApiRefLink>. This key-pair will be used by a cryptographic function to sign JWTs.

## Signing JWTs during Development

While developing an app, you may want an easy way to generate JWTs locally because you're not yet ready to set up a full blown production system that signs JWTs for client-side applications. There are a few different options for generating these JWTs.

### Web Based JWT Signer

<Callout type="warning">
  Pasting credentials into a web browser is generally a bad practice. This web-based tool signs JWTs on the client which means your credentials never leave your machine. This is a tool designed by Mux, intended to be used with Mux credentials, and will always be hosted on a Mux domain. **Never use a tool like this if it is hosted on a non-Mux domain.**
</Callout>

Mux provides a web based JWT Signer at https://jwt.mux.dev. Simply input the Signing key-pair and configure the claims you wish to test your app with. Then, copy the JWT into your application code and run it.

<Image src="/docs/images/jwt-signer.gif" width={600} height={440} alt="Mux's JWT Signer" />

### Node based CLI

Mux provides a [Node.js based CLI](https://github.com/muxinc/cli) for performing common tasks including signing JWTs for [playback IDs](https://github.com/muxinc/cli#mux-sign-playback-id).

After [installing Node.js](https://nodejs.org/), the Mux CLI must be initialized with an Access Token. Follow [this guide](/docs/core/make-api-requests#http-basic-auth) to create an Access Token. With your newly created Access Token, initialize the Mux CLI.

```
npx @mux/cli init
```

Now that the Mux CLI is initialized with your credentials, you can sign a JWT for [Video Playback](https://github.com/muxinc/cli#mux-sign-playback-id).

```
npx @mux/cli sign PLAYBACK-ID
```

For more details, refer to https://github.com/muxinc/cli.

<Callout type="warning">
  You should only sign a JWT on the server, where you can keep your signing key secret. You should not put your signing key in the client itself.
</Callout>

<Callout type="success">
  Setup a REST endpoint behind your own authentication system that provides your client-side code with signed JWTs. That way, the sensitive secret from the signing key-pair stays on the server instead of being included in the client.
</Callout>

## Signing JWTs for Production

Once you're ready for customers to start using your app, you need a way to sign JWTs securely at-scale. Use the code examples below depending on which Mux product you would like to sign JWTs for.

### Sign Video Playback JWTs

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

    playbackId := "" // Enter your signed playback id here
    keyId      := "" // Enter your signing key id here
    key        := "" // Enter your base64 encoded private key here

    decodedKey, err := base64.StdEncoding.DecodeString(key)
    if err != nil {
        log.Fatalf("Could not base64 decode private key: %v", err)
    }

    signKey, err := jwt.ParseRSAPrivateKeyFromPEM(decodedKey)
    if err != nil {
        log.Fatalf("Could not parse RSA private key: %v", err)
    }

    token := jwt.NewWithClaims(jwt.SigningMethodRS256, jwt.MapClaims{
        "sub": playbackId,
        "aud": "v",
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

// We've created some helper functions for Node to make your signing-life easier
const Mux = require('@mux/mux-node');
const mux = new Mux();

async function createTokens () {
  const playbackId = ''; // Enter your signed playback id here

  // Set some base options we can use for a few different signing types
  // Type can be either video, thumbnail, gif, or storyboard
  let baseOptions = {
    keyId: '', // Enter your signing key id here
    keySecret: '', // Enter your base64 encoded private key here
    expiration: '7d', // E.g 60, "2 days", "10h", "7d", numeric value interpreted as seconds
  };

  const token = await mux.jwt.signPlaybackId(playbackId, { ...baseOptions, type: 'video' });
  console.log('video token', token);

  // Now the signed playback url should look like this:
  // https://stream.mux.com/${playbackId}.m3u8?token=${token}

  // If you wanted to pass in params for something like a gif, use the
  // params key in the options object
  const gifToken = await mux.jwt.signPlaybackId(playbackId, {
    ...baseOptions,
    type: 'gif',
    params: { time: '10' },
  });
  console.log('gif token', gifToken);

  // Then, use this token in a URL like this:
  // https://image.mux.com/${playbackId}/animated.gif?token=${gifToken}

  // A final example, if you wanted to sign a thumbnail url with a playback restriction
  const thumbnailToken = await mux.jwt.signPlaybackId(playbackId, {
    ...baseOptions,
    type: 'thumbnail',
    params: { playback_restriction_id: YOUR_PLAYBACK_RESTRICTION_ID },
  });
  console.log('thumbnail token', thumbnailToken);

  // When used in a URL, it should look like this:
  // https://image.mux.com/${playbackId}/thumbnail.png?token=${thumbnailToken}
}

```

```php

<?php
  // Using Composer and https://github.com/firebase/php-jwt
  require __DIR__ . '/vendor/autoload.php';
  use \Firebase\JWT\JWT;

  $playbackId = ""; // Enter your signed playback id here
  $keyId = "";      // Enter your signing key id here
  $keySecret = "";  // Enter your base64 encoded private key here

  $payload = array(
    "sub" => $playbackId,
    "aud" => "t",          // v = video, t = thumbnail, g = gif.
    "exp" => time() + 600, // Expiry time in epoch - in this case now + 10 mins
    "kid" => $keyId,

    // Optional, include any additional manipulations
    "time"     => 10,
    "width"    => 640,
    "fit_mode" => "smartcrop"
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

playback_id = ''        # Enter your signed playback id here
signing_key_id = ''     # Enter your signing key id here
private_key_base64 = '' # Enter your base64 encoded private key here

private_key = base64.b64decode(private_key_base64)

token = {
    'sub': playback_id,
    'exp': int(time.time()) + 3600, # 1 hour
    'aud': 'v'
}
headers = {
    'kid': signing_key_id
}

json_web_token = jwt.encode(
    token, private_key, algorithm="RS256", headers=headers)

print(json_web_token)

```

```ruby

require 'base64'
require 'jwt'

def sign_url(playback_id, audience, expires, signing_key_id, private_key, params = {})
    rsa_private = OpenSSL::PKey::RSA.new(Base64.decode64(private_key))
    payload = {sub: playback_id, exp: expires.to_i, kid: signing_key_id, aud: audience}
    payload.merge!(params)
    JWT.encode(payload, rsa_private, 'RS256')
end

playback_id = ''        # Enter your signed playback id here
signing_key_id = ''     # Enter your signing key id here
private_key_base64 = '' # Enter your base64 encoded private key here

token = sign_url(playback_id, 'v', Time.now + 3600, signing_key_id, private_key_base64)

```



### Sign Data JWTs

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

