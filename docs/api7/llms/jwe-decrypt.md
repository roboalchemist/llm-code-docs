# Source: https://docs.api7.ai/hub/jwe-decrypt.md

# jwe-decrypt

The `jwe-decrypt` plugin decrypts [JWE](https://datatracker.ietf.org/doc/html/rfc7516) authorization headers in requests sent to APISIX [routes](https://docs.api7.ai/apisix/key-concepts/routes.md) or [services](https://docs.api7.ai/apisix/key-concepts/services.md).

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can work with the `jwe-decrypt` plugin for different scenarios.

### Expose JWE Encryption Endpoint and Generate JWE Token[â](#expose-jwe-encryption-endpoint-and-generate-jwe-token "Direct link to Expose JWE Encryption Endpoint and Generate JWE Token")

The following example demonstrates how to expose the JWE encryption endpoint and generate a JWE token.

The plugin `jwe-decrypt` plugin creates an internal endpoint at `/apisix/plugin/jwe/encrypt` to encrypt JWE. Expose the endpoint with the `public-api` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/jwe-encrypt-api" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "uri": "/apisix/plugin/jwe/encrypt",
    "plugins": {
      "public-api": {}
    }
  }'
```

Create a consumer with `jwe-decrypt` and configure the decryption key:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "jack",
    "plugins": {
      "jwe-decrypt": {
        "key": "jack-key",
        "secret": "key-length-should-be-32-chars123"
      }
    }
  }'
```

Send a request to the encryption endpoint with consumer key to encrypt some sample data in the payload:

```
curl "http://127.0.0.1:9080/apisix/plugin/jwe/encrypt?key=jack-key" \
  -d 'payload={"uid":10000,"uname":"test"}' -G
```

You should see a response similar to the following, with the JWE encrypted data in the response body:

```
eyJraWQiOiJqYWNrLWtleSIsImFsZyI6ImRpciIsImVuYyI6IkEyNTZHQ00ifQ..MTIzNDU2Nzg5MDEy.IUFW_q4igO_wvf63i-3VwV0MEetPL9C20tlgcQ.fveViMUi0ijJlQ19D7kDrg
```

### Decrypt Data with JWE[â](#decrypt-data-with-jwe "Direct link to Decrypt Data with JWE")

The following example demonstrates how to decrypt the previously generated JWE token.

Create a route with `jwe-decrypt` to decrypt the authorization header:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "jwe-decrypt-route",
    "uri": "/anything/jwe",
    "plugins": {
      "jwe-decrypt": {
        "header": "Authorization",
        "forward_header": "Authorization"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

Send a request to the route with the JWE encrypted data in the `Authorization` header:

```
curl "http://127.0.0.1:9080/anything/jwe" -H 'Authorization: eyJraWQiOiJqYWNrLWtleSIsImFsZyI6ImRpciIsImVuYyI6IkEyNTZHQ00ifQ..MTIzNDU2Nzg5MDEy.IUFW_q4igO_wvf63i-3VwV0MEetPL9C20tlgcQ.fveViMUi0ijJlQ19D7kDrg'
```

You should see a response similar to the following, where the `Authorization` header shows the plaintext of the payload:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Authorization": "{\"uid\":10000,\"uname\":\"test\"}",
    "Host": "127.0.0.1",
    "User-Agent": "curl/8.1.2",
    "X-Amzn-Trace-Id": "Root=1-6510f2c3-1586ec011a22b5094dbe1896",
    "X-Forwarded-Host": "127.0.0.1"
  },
  "json": null,
  "method": "GET",
  "origin": "127.0.0.1, 119.143.79.94",
  "url": "http://127.0.0.1/anything/jwe"
}
```
