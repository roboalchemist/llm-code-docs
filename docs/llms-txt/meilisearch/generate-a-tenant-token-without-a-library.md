# Generate a tenant token without a library
Source: https://www.meilisearch.com/docs/learn/security/generate_tenant_token_scratch

This guide shows you the main steps when creating tenant tokens without using any libraries.

Generating tenant tokens without a library is possible, but not recommended. This guide summarizes the necessary steps.

The full process requires you to create a token header, prepare the data payload with at least one set of search rules, and then sign the token with an API key.

## Prepare token header

The token header must specify a `JWT` type and an encryption algorithm. Supported tenant token encryption algorithms are `HS256`, `HS384`, and `HS512`.

```json theme={null}
{
  "alg": "HS256",
  "typ": "JWT"
}
```

## Build token payload

First, create a set of search rules:

```json theme={null}
{
  "INDEX_NAME": {
    "filter": "ATTRIBUTE = VALUE"
  }
}
```

Next, find your default search API key. Query the [get an API key endpoint](/reference/api/keys#get-one-key) and inspect the `uid`  field to obtain your API key's UID:

```sh theme={null}
curl \
  -X GET 'MEILISEARCH_URL/keys/API_KEY' \
  -H 'Authorization: Bearer MASTER_KEY'
```

For maximum security, you should also set an expiry date for your tenant tokens. The following Node.js example configures the token to expire 20 minutes after its creation:

```js theme={null}
parseInt(Date.now() / 1000) + 20 * 60
```

Lastly, assemble all parts of the payload in a single object:

```json theme={null}
{
  "exp": UNIX_TIMESTAMP,
  "apiKeyUid": "API_KEY_UID",
  "searchRules": {
    "INDEX_NAME": {
      "filter": "ATTRIBUTE = VALUE"
    }
  }
}
```

Consult the [token payload reference](/learn/security/tenant_token_reference) for more information on the requirements for each payload field.

## Encode header and payload

You must then encode both the header and the payload into `base64`, concatenate them, and generate the token by signing it using your chosen encryption algorithm.

## Make a search request using a tenant token

After signing the token, you can use it to make search queries in the same way you would use an API key.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/patient_medical_records/search' \
    -H 'Authorization: Bearer TENANT_TOKEN'
  ```
</CodeGroup>