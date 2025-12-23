# Source: https://fastapi.tiangolo.com/reference/status/

# Status Codes[&para;](#status-codes)

You can import the `status` module from `fastapi`:

`from fastapi import status
`

`status` is provided directly by Starlette.

It contains a group of named constants (variables) with integer status codes.

For example:

- 200: `status.HTTP_200_OK`

- 403: `status.HTTP_403_FORBIDDEN`

- etc.

It can be convenient to quickly access HTTP (and WebSocket) status codes in your app, using autocompletion for the name without having to remember the integer status codes by memory.

Read more about it in the [FastAPI docs about Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/).

## Example[&para;](#example)

`from fastapi import FastAPI, status

app = FastAPI()

@app.get("/items/", status_code=status.HTTP_418_IM_A_TEAPOT)
def read_items():
    return [{"name": "Plumbus"}, {"name": "Portal Gun"}]
`

## 
``            fastapi.status

[&para;](#fastapi.status)

        HTTP codes
See HTTP Status Code Registry:
https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

And RFC 9110 - https://www.rfc-editor.org/rfc/rfc9110

### 
``            HTTP_100_CONTINUE

      `module-attribute`

[&para;](#fastapi.status.HTTP_100_CONTINUE)

`HTTP_100_CONTINUE = 100
`

### 
``            HTTP_101_SWITCHING_PROTOCOLS

      `module-attribute`

[&para;](#fastapi.status.HTTP_101_SWITCHING_PROTOCOLS)

`HTTP_101_SWITCHING_PROTOCOLS = 101
`

### 
``            HTTP_102_PROCESSING

      `module-attribute`

[&para;](#fastapi.status.HTTP_102_PROCESSING)

`HTTP_102_PROCESSING = 102
`

### 
``            HTTP_103_EARLY_HINTS

      `module-attribute`

[&para;](#fastapi.status.HTTP_103_EARLY_HINTS)

`HTTP_103_EARLY_HINTS = 103
`

### 
``            HTTP_200_OK

      `module-attribute`

[&para;](#fastapi.status.HTTP_200_OK)

`HTTP_200_OK = 200
`

### 
``            HTTP_201_CREATED

      `module-attribute`

[&para;](#fastapi.status.HTTP_201_CREATED)

`HTTP_201_CREATED = 201
`

### 
``            HTTP_202_ACCEPTED

      `module-attribute`

[&para;](#fastapi.status.HTTP_202_ACCEPTED)

`HTTP_202_ACCEPTED = 202
`

### 
``            HTTP_203_NON_AUTHORITATIVE_INFORMATION

      `module-attribute`

[&para;](#fastapi.status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

`HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
`

### 
``            HTTP_204_NO_CONTENT

      `module-attribute`

[&para;](#fastapi.status.HTTP_204_NO_CONTENT)

`HTTP_204_NO_CONTENT = 204
`

### 
``            HTTP_205_RESET_CONTENT

      `module-attribute`

[&para;](#fastapi.status.HTTP_205_RESET_CONTENT)

`HTTP_205_RESET_CONTENT = 205
`

### 
``            HTTP_206_PARTIAL_CONTENT

      `module-attribute`

[&para;](#fastapi.status.HTTP_206_PARTIAL_CONTENT)

`HTTP_206_PARTIAL_CONTENT = 206
`

### 
``            HTTP_207_MULTI_STATUS

      `module-attribute`

[&para;](#fastapi.status.HTTP_207_MULTI_STATUS)

`HTTP_207_MULTI_STATUS = 207
`

### 
``            HTTP_208_ALREADY_REPORTED

      `module-attribute`

[&para;](#fastapi.status.HTTP_208_ALREADY_REPORTED)

`HTTP_208_ALREADY_REPORTED = 208
`

### 
``            HTTP_226_IM_USED

      `module-attribute`

[&para;](#fastapi.status.HTTP_226_IM_USED)

`HTTP_226_IM_USED = 226
`

### 
``            HTTP_300_MULTIPLE_CHOICES

      `module-attribute`

[&para;](#fastapi.status.HTTP_300_MULTIPLE_CHOICES)

`HTTP_300_MULTIPLE_CHOICES = 300
`

### 
``            HTTP_301_MOVED_PERMANENTLY

      `module-attribute`

[&para;](#fastapi.status.HTTP_301_MOVED_PERMANENTLY)

`HTTP_301_MOVED_PERMANENTLY = 301
`

### 
``            HTTP_302_FOUND

      `module-attribute`

[&para;](#fastapi.status.HTTP_302_FOUND)

`HTTP_302_FOUND = 302
`

### 
``            HTTP_303_SEE_OTHER

      `module-attribute`

[&para;](#fastapi.status.HTTP_303_SEE_OTHER)

`HTTP_303_SEE_OTHER = 303
`

### 
``            HTTP_304_NOT_MODIFIED

      `module-attribute`

[&para;](#fastapi.status.HTTP_304_NOT_MODIFIED)

`HTTP_304_NOT_MODIFIED = 304
`

### 
``            HTTP_305_USE_PROXY

      `module-attribute`

[&para;](#fastapi.status.HTTP_305_USE_PROXY)

`HTTP_305_USE_PROXY = 305
`

### 
``            HTTP_306_RESERVED

      `module-attribute`

[&para;](#fastapi.status.HTTP_306_RESERVED)

`HTTP_306_RESERVED = 306
`

### 
``            HTTP_307_TEMPORARY_REDIRECT

      `module-attribute`

[&para;](#fastapi.status.HTTP_307_TEMPORARY_REDIRECT)

`HTTP_307_TEMPORARY_REDIRECT = 307
`

### 
``            HTTP_308_PERMANENT_REDIRECT

      `module-attribute`

[&para;](#fastapi.status.HTTP_308_PERMANENT_REDIRECT)

`HTTP_308_PERMANENT_REDIRECT = 308
`

### 
``            HTTP_400_BAD_REQUEST

      `module-attribute`

[&para;](#fastapi.status.HTTP_400_BAD_REQUEST)

`HTTP_400_BAD_REQUEST = 400
`

### 
``            HTTP_401_UNAUTHORIZED

      `module-attribute`

[&para;](#fastapi.status.HTTP_401_UNAUTHORIZED)

`HTTP_401_UNAUTHORIZED = 401
`

### 
``            HTTP_402_PAYMENT_REQUIRED

      `module-attribute`

[&para;](#fastapi.status.HTTP_402_PAYMENT_REQUIRED)

`HTTP_402_PAYMENT_REQUIRED = 402
`

### 
``            HTTP_403_FORBIDDEN

      `module-attribute`

[&para;](#fastapi.status.HTTP_403_FORBIDDEN)

`HTTP_403_FORBIDDEN = 403
`

### 
``            HTTP_404_NOT_FOUND

      `module-attribute`

[&para;](#fastapi.status.HTTP_404_NOT_FOUND)

`HTTP_404_NOT_FOUND = 404
`

### 
``            HTTP_405_METHOD_NOT_ALLOWED

      `module-attribute`

[&para;](#fastapi.status.HTTP_405_METHOD_NOT_ALLOWED)

`HTTP_405_METHOD_NOT_ALLOWED = 405
`

### 
``            HTTP_406_NOT_ACCEPTABLE

      `module-attribute`

[&para;](#fastapi.status.HTTP_406_NOT_ACCEPTABLE)

`HTTP_406_NOT_ACCEPTABLE = 406
`

### 
``            HTTP_407_PROXY_AUTHENTICATION_REQUIRED

      `module-attribute`

[&para;](#fastapi.status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

`HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
`

### 
``            HTTP_408_REQUEST_TIMEOUT

      `module-attribute`

[&para;](#fastapi.status.HTTP_408_REQUEST_TIMEOUT)

`HTTP_408_REQUEST_TIMEOUT = 408
`

### 
``            HTTP_409_CONFLICT

      `module-attribute`

[&para;](#fastapi.status.HTTP_409_CONFLICT)

`HTTP_409_CONFLICT = 409
`

### 
``            HTTP_410_GONE

      `module-attribute`

[&para;](#fastapi.status.HTTP_410_GONE)

`HTTP_410_GONE = 410
`

### 
``            HTTP_411_LENGTH_REQUIRED

      `module-attribute`

[&para;](#fastapi.status.HTTP_411_LENGTH_REQUIRED)

`HTTP_411_LENGTH_REQUIRED = 411
`

### 
``            HTTP_412_PRECONDITION_FAILED

      `module-attribute`

[&para;](#fastapi.status.HTTP_412_PRECONDITION_FAILED)

`HTTP_412_PRECONDITION_FAILED = 412
`

### 
``            HTTP_413_CONTENT_TOO_LARGE

      `module-attribute`

[&para;](#fastapi.status.HTTP_413_CONTENT_TOO_LARGE)

`HTTP_413_CONTENT_TOO_LARGE = 413
`

### 
``            HTTP_414_URI_TOO_LONG

      `module-attribute`

[&para;](#fastapi.status.HTTP_414_URI_TOO_LONG)

`HTTP_414_URI_TOO_LONG = 414
`

### 
``            HTTP_415_UNSUPPORTED_MEDIA_TYPE

      `module-attribute`

[&para;](#fastapi.status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

`HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
`

### 
``            HTTP_416_RANGE_NOT_SATISFIABLE

      `module-attribute`

[&para;](#fastapi.status.HTTP_416_RANGE_NOT_SATISFIABLE)

`HTTP_416_RANGE_NOT_SATISFIABLE = 416
`

### 
``            HTTP_417_EXPECTATION_FAILED

      `module-attribute`

[&para;](#fastapi.status.HTTP_417_EXPECTATION_FAILED)

`HTTP_417_EXPECTATION_FAILED = 417
`

### 
``            HTTP_418_IM_A_TEAPOT

      `module-attribute`

[&para;](#fastapi.status.HTTP_418_IM_A_TEAPOT)

`HTTP_418_IM_A_TEAPOT = 418
`

### 
``            HTTP_421_MISDIRECTED_REQUEST

      `module-attribute`

[&para;](#fastapi.status.HTTP_421_MISDIRECTED_REQUEST)

`HTTP_421_MISDIRECTED_REQUEST = 421
`

### 
``            HTTP_422_UNPROCESSABLE_CONTENT

      `module-attribute`

[&para;](#fastapi.status.HTTP_422_UNPROCESSABLE_CONTENT)

`HTTP_422_UNPROCESSABLE_CONTENT = 422
`

### 
``            HTTP_423_LOCKED

      `module-attribute`

[&para;](#fastapi.status.HTTP_423_LOCKED)

`HTTP_423_LOCKED = 423
`

### 
``            HTTP_424_FAILED_DEPENDENCY

      `module-attribute`

[&para;](#fastapi.status.HTTP_424_FAILED_DEPENDENCY)

`HTTP_424_FAILED_DEPENDENCY = 424
`

### 
``            HTTP_425_TOO_EARLY

      `module-attribute`

[&para;](#fastapi.status.HTTP_425_TOO_EARLY)

`HTTP_425_TOO_EARLY = 425
`

### 
``            HTTP_426_UPGRADE_REQUIRED

      `module-attribute`

[&para;](#fastapi.status.HTTP_426_UPGRADE_REQUIRED)

`HTTP_426_UPGRADE_REQUIRED = 426
`

### 
``            HTTP_428_PRECONDITION_REQUIRED

      `module-attribute`

[&para;](#fastapi.status.HTTP_428_PRECONDITION_REQUIRED)

`HTTP_428_PRECONDITION_REQUIRED = 428
`

### 
``            HTTP_429_TOO_MANY_REQUESTS

      `module-attribute`

[&para;](#fastapi.status.HTTP_429_TOO_MANY_REQUESTS)

`HTTP_429_TOO_MANY_REQUESTS = 429
`

### 
``            HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE

      `module-attribute`

[&para;](#fastapi.status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE)

`HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
`

### 
``            HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS

      `module-attribute`

[&para;](#fastapi.status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)

`HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451
`

### 
``            HTTP_500_INTERNAL_SERVER_ERROR

      `module-attribute`

[&para;](#fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR)

`HTTP_500_INTERNAL_SERVER_ERROR = 500
`

### 
``            HTTP_501_NOT_IMPLEMENTED

      `module-attribute`

[&para;](#fastapi.status.HTTP_501_NOT_IMPLEMENTED)

`HTTP_501_NOT_IMPLEMENTED = 501
`

### 
``            HTTP_502_BAD_GATEWAY

      `module-attribute`

[&para;](#fastapi.status.HTTP_502_BAD_GATEWAY)

`HTTP_502_BAD_GATEWAY = 502
`

### 
``            HTTP_503_SERVICE_UNAVAILABLE

      `module-attribute`

[&para;](#fastapi.status.HTTP_503_SERVICE_UNAVAILABLE)

`HTTP_503_SERVICE_UNAVAILABLE = 503
`

### 
``            HTTP_504_GATEWAY_TIMEOUT

      `module-attribute`

[&para;](#fastapi.status.HTTP_504_GATEWAY_TIMEOUT)

`HTTP_504_GATEWAY_TIMEOUT = 504
`

### 
``            HTTP_505_HTTP_VERSION_NOT_SUPPORTED

      `module-attribute`

[&para;](#fastapi.status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED)

`HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
`

### 
``            HTTP_506_VARIANT_ALSO_NEGOTIATES

      `module-attribute`

[&para;](#fastapi.status.HTTP_506_VARIANT_ALSO_NEGOTIATES)

`HTTP_506_VARIANT_ALSO_NEGOTIATES = 506
`

### 
``            HTTP_507_INSUFFICIENT_STORAGE

      `module-attribute`

[&para;](#fastapi.status.HTTP_507_INSUFFICIENT_STORAGE)

`HTTP_507_INSUFFICIENT_STORAGE = 507
`

### 
``            HTTP_508_LOOP_DETECTED

      `module-attribute`

[&para;](#fastapi.status.HTTP_508_LOOP_DETECTED)

`HTTP_508_LOOP_DETECTED = 508
`

### 
``            HTTP_510_NOT_EXTENDED

      `module-attribute`

[&para;](#fastapi.status.HTTP_510_NOT_EXTENDED)

`HTTP_510_NOT_EXTENDED = 510
`

### 
``            HTTP_511_NETWORK_AUTHENTICATION_REQUIRED

      `module-attribute`

[&para;](#fastapi.status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)

`HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511
`

        WebSocket codes
https://www.iana.org/assignments/websocket/websocket.xml#close-code-number
https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent

### 
``            WS_1000_NORMAL_CLOSURE

      `module-attribute`

[&para;](#fastapi.status.WS_1000_NORMAL_CLOSURE)

`WS_1000_NORMAL_CLOSURE = 1000
`

### 
``            WS_1001_GOING_AWAY

      `module-attribute`

[&para;](#fastapi.status.WS_1001_GOING_AWAY)

`WS_1001_GOING_AWAY = 1001
`

### 
``            WS_1002_PROTOCOL_ERROR

      `module-attribute`

[&para;](#fastapi.status.WS_1002_PROTOCOL_ERROR)

`WS_1002_PROTOCOL_ERROR = 1002
`

### 
``            WS_1003_UNSUPPORTED_DATA

      `module-attribute`

[&para;](#fastapi.status.WS_1003_UNSUPPORTED_DATA)

`WS_1003_UNSUPPORTED_DATA = 1003
`

### 
``            WS_1005_NO_STATUS_RCVD

      `module-attribute`

[&para;](#fastapi.status.WS_1005_NO_STATUS_RCVD)

`WS_1005_NO_STATUS_RCVD = 1005
`

### 
``            WS_1006_ABNORMAL_CLOSURE

      `module-attribute`

[&para;](#fastapi.status.WS_1006_ABNORMAL_CLOSURE)

`WS_1006_ABNORMAL_CLOSURE = 1006
`

### 
``            WS_1007_INVALID_FRAME_PAYLOAD_DATA

      `module-attribute`

[&para;](#fastapi.status.WS_1007_INVALID_FRAME_PAYLOAD_DATA)

`WS_1007_INVALID_FRAME_PAYLOAD_DATA = 1007
`

### 
``            WS_1008_POLICY_VIOLATION

      `module-attribute`

[&para;](#fastapi.status.WS_1008_POLICY_VIOLATION)

`WS_1008_POLICY_VIOLATION = 1008
`

### 
``            WS_1009_MESSAGE_TOO_BIG

      `module-attribute`

[&para;](#fastapi.status.WS_1009_MESSAGE_TOO_BIG)

`WS_1009_MESSAGE_TOO_BIG = 1009
`

### 
``            WS_1010_MANDATORY_EXT

      `module-attribute`

[&para;](#fastapi.status.WS_1010_MANDATORY_EXT)

`WS_1010_MANDATORY_EXT = 1010
`

### 
``            WS_1011_INTERNAL_ERROR

      `module-attribute`

[&para;](#fastapi.status.WS_1011_INTERNAL_ERROR)

`WS_1011_INTERNAL_ERROR = 1011
`

### 
``            WS_1012_SERVICE_RESTART

      `module-attribute`

[&para;](#fastapi.status.WS_1012_SERVICE_RESTART)

`WS_1012_SERVICE_RESTART = 1012
`

### 
``            WS_1013_TRY_AGAIN_LATER

      `module-attribute`

[&para;](#fastapi.status.WS_1013_TRY_AGAIN_LATER)

`WS_1013_TRY_AGAIN_LATER = 1013
`

### 
``            WS_1014_BAD_GATEWAY

      `module-attribute`

[&para;](#fastapi.status.WS_1014_BAD_GATEWAY)

`WS_1014_BAD_GATEWAY = 1014
`

### 
``            WS_1015_TLS_HANDSHAKE

      `module-attribute`

[&para;](#fastapi.status.WS_1015_TLS_HANDSHAKE)

`WS_1015_TLS_HANDSHAKE = 1015
`