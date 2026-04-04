# Source: https://docs.api7.ai/apisix/how-to-guide/authentication/implement-hmac-auth.md

# Implement HMAC Authentication

HMAC Authentication is a robust method of securing API requests by generating a cryptographic signature using a shared secret key and hashing algorithm. The client calculates the signature by hashing the request payload or specific request components, such as headers or parameters, and sends it along with the request. The server then recalculates the signature using the same shared key and verifies its validity. This approach ensures the authenticity and integrity of the request, protecting it from tampering or replay attacks. HMAC Authentication is particularly well-suited for securing sensitive data exchanges, such as in financial services or applications requiring strong non-repudiation. However, securely sharing and managing the secret key is critical to its effectiveness.

In this guide, you will implement a scenario where there are two consumers using [HMAC authentication](https://docs.api7.ai/hub/hmac-auth.md) to authenticate with APISIX, each with a different rate limiting quota. Once implemented, consumers should have access to the upstream service and forward consumer IDs to the upstream service, opening up options for additional business logic.

## Create Consumers[â](#create-consumers "Direct link to Create Consumers")

A consumer is an application or a developer who consumes the API. You should always create consumers when using APISIX built-in authentication methods.

* Admin API

Create a consumer `johndoe` with an optional custom ID and a rate limiting quota of one request in a 30-second window:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "johndoe",
    "labels": {
      "custom_id": "john-doe-junior"
    },
    "plugins": {
      "limit-count": {
        "count": 1,
        "time_window": 30,
        "rejected_code": 429
      }
    }
  }'
```

The custom ID will be forwarded to the upstream service, should you wish to implement additional business logic.

Create another consumer `janedoe` with an optional custom ID and a rate limiting quota of two requests in a 30-second window:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "janedoe",
    "labels": {
      "custom_id": "jane-doe-senior"
    },
    "plugins": {
      "limit-count": {
        "count": 2,
        "time_window": 30,
        "rejected_code": 429
      }
    }
  }'
```

## Create Consumer Credentials[â](#create-consumer-credentials "Direct link to Create Consumer Credentials")

Credentials are used to configure authentication credentials associated with consumers.

* Admin API

Create `hmac-auth` credential for `johndoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/johndoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-hmac-auth",
    "plugins": {
      "hmac-auth": {
        "key_id": "john-key",
        "secret_key": "john-secret-key"
      }
    }
  }'
```

Create `hmac-auth` credential for `janedoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/janedoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-hmac-auth",
    "plugins": {
      "hmac-auth": {
        "key_id": "jane-key",
        "secret_key": "jane-secret-key"
      }
    }
  }'
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route and enable `hmac-auth`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "hmac-auth-route",
    "uri": "/anything",
    "methods": ["GET"],
    "plugins": {
      "hmac-auth": {}
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

## Create a Signature[â](#create-a-signature "Direct link to Create a Signature")

Generate a signature. You can use the below Python snippet or other stack of your choice:

hmac-sig-header-gen.py

```
import hmac
import hashlib
import base64
from datetime import datetime, timezone

key_id = "john-key"                # key id
secret_key = b"john-secret-key"    # secret key
request_method = "GET"             # HTTP method
request_path = "/get"              # route URI
algorithm= "hmac-sha256"           # can use other algorithms in allowed_algorithms

# get current datetime in GMT
# note: the signature will become invalid after the clock skew (default 300s)
# you can regenerate the signature after it becomes invalid, or increase the clock
# skew to prolong the validity within the advised security boundary
gmt_time = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')

# construct the signing string (ordered)
# the date and any subsequent custom headers should be lowercased and separated by a
# single space character, i.e. `<key>:<space><value>`
# https://datatracker.ietf.org/doc/html/draft-cavage-http-signatures-12#section-2.1.6
signing_string = (
  f"{key_id}\n"
  f"{request_method} {request_path}\n"
  f"date: {gmt_time}\n"
)

# create signature
signature = hmac.new(secret_key, signing_string.encode('utf-8'), hashlib.sha256).digest()
signature_base64 = base64.b64encode(signature).decode('utf-8')

# construct the request headers
headers = {
  "Date": gmt_time,
  "Authorization": (
    f'Signature keyId="{key_id}",algorithm="{algorithm}",'
    f'headers="@request-target date",'
    f'signature="{signature_base64}"'
  )
}

# print headers
print(headers)
```

Run the script:

```
python3 hmac-sig-header-gen.py
```

You should see the request headers printed:

```
{'Date': 'Fri, 13 Dec 2024 10:52:03 GMT', 'Authorization': 'Signature keyId="john-key",algorithm="hmac-sha256",headers="@request-target date",signature="xt4MHsraC7C6E6jGUD9wlwEbdLWlQS561yoixekboCs="'}
```

Repeat the same step for `janedoe`. You should see the request headers printed:

```
{'Date': 'Fri, 13 Dec 2024 10:52:04 GMT', 'Authorization': 'Signature keyId="jane-key",algorithm="hmac-sha256",headers="@request-target date",signature="5KKPz7tk1+YVpoVqtNBxS6xHzRE9Bu3CUqhmhXPxGUE="'}
```

## Verify[â](#verify "Direct link to Verify")

Using the headers generated, send a request to the route using `johndoe`'s credential:

```
curl -X GET "http://127.0.0.1:9080/anything" \
  -H "Fri, 13 Dec 2024 10:52:03 GMT" \
  -H 'Authorization: Signature keyId="john-key",algorithm="hmac-sha256",headers="@request-target date",signature="xt4MHsraC7C6E6jGUD9wlwEbdLWlQS561yoixekboCs="'
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {},
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    ...
    "X-Consumer-Username": "johndoe",
    "X-Credential-Identifier": "cred-john-basic-auth",
    "X-Consumer-Custom-Id": "john-doe-junior",
    "X-Forwarded-Host": "127.0.0.1"
  }, 
  ...
}
```

Generate three requests to the route with `john`'s key:

```
resp=$(seq 3 | xargs -I{} curl -X GET "http://127.0.0.1:9080/anything" \
  -H "Date: Fri, 13 Dec 2024 10:52:03 GMT" \
  -H 'Authorization: Signature keyId="john-key",algorithm="hmac-sha256",headers="@request-target date",signature="xt4MHsraC7C6E6jGUD9wlwEbdLWlQS561yoixekboCs="' \
  -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200": $count_200, "429": $count_429
```

You should see the following response, showing that out of the 3 requests, 1 request was successful while the others were rejected:

```
200:    1, 429:    2
```

Generate three requests to the route with `jane`'s credential:

```
resp=$(seq 3 | xargs -I{} curl -X GET "http://127.0.0.1:9080/anything" \
  -H "Date: Fri, 13 Dec 2024 10:52:04 GMT" \
  -H 'Authorization: Signature keyId="jane-key",algorithm="hmac-sha256",headers="@request-target date",signature="5KKPz7tk1+YVpoVqtNBxS6xHzRE9Bu3CUqhmhXPxGUE="' \
  -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200": $count_200, "429": $count_429
```

You should see the following response, showing that out of the 3 requests, 2 requests were successful while the other was rejected:

```
200:    2, 429:    1
```

Finally, send a request with an invalid key:

```
curl -X GET "http://127.0.0.1:9080/anything" \
  -H "Fri, 13 Dec 2024 10:52:03 GMT" \
  -H 'Authorization: Signature keyId="john-key",algorithm="hmac-sha256",headers="@request-target date",signature="randomrandomalwEbdLWlQS561yoixekboCs="'
```

You should see an `HTTP/1.1 401 Unauthorized` response with a message similar to the following:

```
{"message":"client request can't be validated"}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to implement HMAC authentication. APISIX supports other built-in authentication methods, such as [key authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-key-auth.md), [basic authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-basic-auth.md), and [JWT authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-hmac-auth.md).
