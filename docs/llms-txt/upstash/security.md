# Source: https://upstash.com/docs/workflow/howto/security.md

# Source: https://upstash.com/docs/redis/features/security.md

# Source: https://upstash.com/docs/qstash/features/security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Security

### Request Authorization

When interacting with the QStash API, you will need an authorization token. You
can get your token from the [Console](https://console.upstash.com/qstash).

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b0bda5d8c30d60c36bcaaf49accce9b1" data-og-width="1090" width="1090" data-og-height="402" height="402" data-path="img/qstash/rest_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ad32156275de5c4b5c17f8351d03dfd7 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2b05f661b26af08e75cb7bd29b94530a 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c7b6ff4e398e7adff1f6901c991f4c92 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c8b639fac03f93107b378b3699c55803 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=18008b9741588917fd62e0efe903be95 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=245f6b9806e7b523b8a4a2ace3dad5c2 2500w" />
</Frame>

Send this token along with every request made to `QStash` inside the
`Authorization` header like this:

```
"Authorization": "Bearer <QSTASH_TOKEN>"
```

### Request Signing (optional)

Because your endpoint needs to be publicly available, we recommend you verify
the authenticity of each incoming request.

#### The `Upstash-Signature` header

With each request we are sending a JWT inside the `Upstash-Signature` header.
You can learn more about them [here](https://jwt.io).

An example token would be:

**Header**

```json  theme={"system"}
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload**

```json  theme={"system"}
{
  "iss": "Upstash",
  "sub": "https://qstash-remote.requestcatcher.com/test",
  "exp": 1656580612,
  "nbf": 1656580312,
  "iat": 1656580312,
  "jti": "jwt_67kxXD6UBAk7DqU6hzuHMDdXFXfP",
  "body": "qK78N0k3pNKI8zN62Fq2Gm-_LtWkJk1z9ykio3zZvY4="
}
```

The JWT is signed using `HMAC SHA256` algorithm with your current signing key
and includes the following claims:

#### Claims

##### `iss`

The issuer field is always `Upstash`.

##### `sub`

The url of your endpoint, where this request is sent to.

For example when you are using a nextjs app on vercel, this would look something
like `https://my-app.vercel.app/api/endpoint`

##### `exp`

A unix timestamp in seconds after which you should no longer accept this
request. Our JWTs have a lifetime of 5 minutes by default.

##### `iat`

A unix timestamp in seconds when this JWT was created.

##### `nbf`

A unix timestamp in seconds before which you should not accept this request.

##### `jti`

A unique id for this token.

##### `body`

The body field is a base64 encoded sha256 hash of the request body. We use url
encoding as specified in
[RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-5).

#### Verifying the signature

See [how to verify the signature](/qstash/howto/signature).
