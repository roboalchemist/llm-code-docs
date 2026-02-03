# Source: https://docs.solidfi.com/v2/api-reference/getting-started/idempotency.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Idempotency

> Solid Platform supports idempotency

The Solid Platform supports idempotency to help prevent you from accidentally calling the same API call twice.

An idempotency key uniquely identifies each API request. You must pass the idempotency key in the header (idempotency-key) so that the Solid platform can identify the API request. This key should be unique, preferably an internal UUID you store on your database.

```bash Example theme={null}
curl --request POST \ 
--url https://api.sandbox.solidfi.com/v2/accounts/sub_account_holder \ 
--header 'Content-Type: application/json' \ 
--header 'api-key: <api-key>' \ 
--header 'idempotency-key: 9c91bbca-67a0-11ec-90d6-0242ac120003' \
```

Idempotent requests are optional, as in, you can make API calls without an idempotency key. All Solid API  POST (Create calls) and PATCH (Update calls) support idempotency. An idempotency key sent for any other requests (GET, DELETE, etc.) will be ignored and not be saved.

Idempotency can be helpful if you instruct Solid to move money or issue a card.

#### Please note:

* All API responses are cached with the idempotency key (if sent in the header) irrespective of status code, and reuse of the same key will return the cached response (only exception here is rate limit error)
* When the program gets 409 status code: EC\_QLDB\_OCC\_ERROR\_RETRY" and sysMessage": "qldb occ error please retry", try with a new idempotency key
* Solid platform will respond with the original response object if you issue a new request with the same idempotency key
* In case of a 429 rate limit error, you can reuse the idempotency key. For other error codes, reusing the idempotency key will get the response of the previous request
* Idempotency keys expire after 24 hours
