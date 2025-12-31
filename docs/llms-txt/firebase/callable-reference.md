# Source: https://firebase.google.com/docs/functions/callable-reference.md.txt

<br />

An`https.onCall`trigger for Cloud Functions is an HTTPS trigger with a specific format for the request and response. This section provides a specification for the HTTPS request and response formats used by the client SDKs to implement the API. This information may be useful to you if your requirements can't be met using the Android, Apple platforms, or web SDKs.
| **Note:** If you*are* able to use the Android, Apple, or web SDKs, you're recommended to do that instead of directly implementing this protocol. The SDKs provide features to save coding time and effort, as detailed in[Call Functions from Your App](https://firebase.google.com/docs/functions/callable).

## Request format: headers

The HTTP request to a callable trigger endpoint must be a`POST`with the following headers:

- Required:`Content-Type: application/json`
  - An optional`; charset=utf-8`is allowed.
- Optional:`Authorization: Bearer <token>`
  - AFirebase Authenticationuser ID token for the logged-in user making the request. The backend automatically[verifies](https://firebase.google.com/docs/auth/admin/verify-id-tokens)this token and makes it available in the handler's`context`. If the token is not valid, the request is rejected.
- Optional:`Firebase-Instance-ID-Token: <iid>`
  - The FCM registration token from the Firebase client SDK. This must be a string. This is available in the handler's`context`. It is used for targeting push notifications.
- Optional:`X-Firebase-AppCheck: <token>`
  - The Firebase App Check token provided by the client app making the request. The backend automatically verifies this token and decodes it, injecting the`appId`in the handler's`context`. If the token cannot be verified, the request is rejected. (Available for SDK \>=3.14.0)

If any other headers are included, the request is rejected, as described in the response documentation below.

**Note:** In JavaScript clients, these requests trigger a CORS`OPTIONS`preflight, because:

- `application/json`is not allowed. It must be`text/plain`or`application/x-www-form-urlencoded`.
- The`Authorization`header is not a[CORS-safelisted request-header](https://fetch.spec.whatwg.org/#cors-safelisted-request-header).
- Other headers are similarly not allowed.

The callable trigger automatically handles these`OPTIONS`requests.

## Request body

The body of the HTTP request should be a JSON object with any of the following fields:

- Required:`data`- The argument passed to the function. This can be any valid JSON value. This is automatically decoded into native JavaScript types according to the serialization format described below.

If there are any other fields present in the request, the backend considers the request malformed, and it is rejected.

### Response format: status codes

There are several cases that could result in different HTTP status codes and string status codes for[errors](https://cloud.google.com/apis/design/errors)in the response.

1. In the case of an HTTP error before the`client`trigger is invoked, the response is not handled as a client function. For example, if a client tries to invoke a non-existent function, it receives a`404 Not Found`response.

2. If the client trigger is invoked, but the request is in the wrong format, such as not being JSON, having invalid fields, or missing the`data`field, the request is rejected with`400 Bad Request`, with an error code of`INVALID_ARGUMENT`.

3. If the auth token supplied in the request is invalid, the request is rejected with`401 Unauthorized`, with an error code of`UNAUTHENTICATED`.

4. If the FCM registration token supplied in the request is invalid, the behavior is undefined. The token is not checked on every request, except when it is used to send a push notification with FCM.

5. If the callable trigger is invoked, but fails with an unhandled exception or returns a failed promise, the request is rejected with`500 Internal Server Error`, with an error code of`INTERNAL`. This prevents coding errors from accidentally being exposed to end users.

6. If the callable is invoked and returns an explicit error condition using the API provided for callable functions, then the request fails. The HTTP status code returned is based on the official mapping of error status to HTTP status, as defined in[code.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto). The specific error code, message, and details returned are encoded in the response body as detailed below. This means that if the function returns an explicit error with status`OK`, then the response has status`200 OK`, but the`error`field is set in the response.

7. If the client trigger is successful, the response status is`200 OK`.

### Response format: headers

The response has the following headers:

- `Content-Type: application/json`
- An optional`; charset=utf-8`is allowed.

## Response body

The response from a client endpoint is always a JSON object. At a minimum it contains either`result`or`error`, along with any optional fields. If the response is not a JSON object, or does not contain`data`or`error`, the client SDK should treat the request as failed with Google error code`INTERNAL (13)`.

- `error`- If this field is present, then the request is considered failed, regardless of the HTTP status code or whether`data`is also present. The value of this field should be a JSON object in the standard[Google Cloud HTTP Mapping](https://cloud.google.com/apis/design/errors#http_mapping)format for errors, with fields for`status`,`message`, and (optionally)`details`. The`code`field shall not be included. If the`status`field is unset, or is an invalid value, the client should treat the status as`INTERNAL`, in accordance with[code.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto#L33). If`details`is present, it is included in any user info attached to the error in the client SDK, if applicable.  
  **Note:** The`details`field here is a user-supplied value. It is not necessarily a list of values keyed by proto type as in the Google`Status`format.
- `result`- The value returned by the function. This can be any valid JSON value. The firebase-functions SDK automatically encodes the value returned by the user into this JSON format. The client SDKs automatically decode these params into native types according to the serialization format described below.

If other fields are present, they should be ignored.

## Serialization

The serialization format for arbitrary data payloads is the same for both the request and the response.

For platform consistency, these are encoded in JSON as though they are the value of an`Any`field in a proto3 protocol buffer, using the[standard JSON mapping](https://developers.google.com/protocol-buffers/docs/proto3#json). Values of simple types such as`null`,`int`,`double`, or`string`are encoded directly, and do not include their explicit type. So, a`float`and`double`are encoded the same way, and you may not know which is received on the other end of the call. For types that are not native to JSON, the typed proto3 encoding for the value is used. For more information, see the[documentation for Any JSON encoding](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any).

The following types are allowed:

- null -`null`
- int (signed or unsigned, up to 32 bit) - e.g.`3`or`-30`.
- float - e.g.`3.14`
- double - e.g.`3.14`
- boolean -`true`or`false`
- string - e.g.`"hello world"`
- map- e.g.`{"x": 3}`
- list- e.g.`[1, 2, 3]`
- long (signed or unsigned, up to 64 bits) - \[see below for details\]

`NaN`and`Infinity`values for`float`and`double`are not supported.

Note that`long`is a special type not normally allowed in JSON, but is covered by the proto3 specification. For example, these are encoded as:

long  

    {
        '@type': 'type.googleapis.com/google.protobuf.Int64Value',
        'value': '-123456789123456'
    }

unsigned long  

    {
        '@type': 'type.googleapis.com/google.protobuf.UInt64Value',
        'value': '123456789123456'
    }

In general, the`@type`key should be considered reserved, and not used for maps passed in.

Because the type is not specified for simple types, some values will change type after passing over the wire. A`float`passed in becomes a`double`. A`short`becomes an`int`, and so on. In Android, both`List`and`JSONArray`are supported for list values. In those cases, passing in a JSONArray will yield a`List`.

If a map with an unknown`@type`field is deserialized, it is left as a map. This allows developers to add fields with new types to their return values without breaking older clients.

## Code samples

The samples in this section illustrate how to encode the following:

- A callable.call example in Swift
- A success response for the call
- A failure response for the call

### Callable.call example in Swift to encode

    callable.call([
        "aString": "some string",
        "anInt": 57,
        "aFloat": 1.23,
        "aLong": -123456789123456 as Int64
    ])

Request header:  

    Method: POST
    Content-Type: application/json; charset=utf-8
    Authorization: Bearer some-auth-token
    Firebase-Instance-ID-Token: some-iid-token

Request body:  

    {
        "data": {
            "aString": "some string",
            "anInt": 57,
            "aFloat": 1.23,
            "aLong": {
                "@type": "type.googleapis.com/google.protobuf.Int64Value",
                "value": "-123456789123456"
            }
        }
    }

### Response to encode

    return {
        "aString": "some string",
        "anInt": 57,
        "aFloat": 1.23
    };

Successful response header:  

    200 OK
    Content-Type: application/json; charset=utf-8

Successful response body:  

    {
        "response": {
            "aString": "some string",
            "anInt": 57,
            "aFloat": 1.23
        }
    }

### Failure response to encode

    throw new HttpsError("unauthenticated", "Request had invalid credentials.", {
      "some-key": "some-value"
    });

Failed response header:  

    401 UNAUTHENTICATED
    Content-Type: application/json; charset=utf-8

Failed response body:  

    {
        "error": {
            "message": "Request had invalid credentials.",
            "status": "UNAUTHENTICATED",
            "details": {
                "some-key": "some-value"
            }
        }
    }