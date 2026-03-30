# Source: https://docs.salad.com/reference/api-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the API

> Start integrating directly with SaladCloud's robust API

*Last Updated: October 10, 2024*

The SaladCloud API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded
request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

You can find OpenAPI specifications for all of our public APIs
[here](https://github.com/SaladTechnologies/salad-cloud-docs/tree/main/api-specs).

## Authentication

Each API request is authenticated with an API access token that can be accessed via the Web Portal. Each user has a
unique API token that grants API access to any Organization, Project, or Container group that the user has access to. If
you need to get a new API Token, you are able to refresh API tokens directly from the Web Portal.

This API token should be included in the `Salad-Api-Key` header of each request.

```http  theme={null}
Salad-Api-Key: YOUR_API_KEY
```

This authentication scheme is also used to access container groups (when authentication is enabled) and inference
endpoints.

## Get your SaladCloud API Key

Navigate to the `API Access` section under the account drop down

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/reference/images/account-dropdown.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=31d157e700518548281f5bf653efbfe6" alt="Account Drop Down Menu" data-og-width="254" width="254" data-og-height="219" height="219" data-path="reference/images/account-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/reference/images/account-dropdown.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=4a3da06583f4b0022255388bbb655776 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/reference/images/account-dropdown.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=c4dc4aec4d7f9aea5ec2c4b9d4d92e10 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/reference/images/account-dropdown.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a12c04cd3fedc91d764feb8d57ee744f 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/reference/images/account-dropdown.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d6efb6cc870193168a7fc5dbab895b0f 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/reference/images/account-dropdown.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=ae3988a1e87cf9fcf70dc9f23f396295 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/reference/images/account-dropdown.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=12b7243c8da604becc4b6111a4c6cfb5 2500w" />

Copy your API key from the `API Access` page. Be sure to store this key securely, as it is the only way to access the
SaladCloud APIs.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/reference/images/api-access-key.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=aed48b93a401ce11c1ac70acbdecd18e" alt="API Key Retrieval Screen" data-og-width="1056" width="1056" data-og-height="370" height="370" data-path="reference/images/api-access-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/reference/images/api-access-key.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=bdd35121c2da219887a06cb0d6369bc6 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/reference/images/api-access-key.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=6fa6716306ddc9548393cbdedc0f9997 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/reference/images/api-access-key.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=ea0c9e9bea9bfffeb4a1138357ba77a7 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/reference/images/api-access-key.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=bbc83bc481c591593a3a9f5b013a2d0b 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/reference/images/api-access-key.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=9fc01af604fcc606303cdabad9b3f25b 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/reference/images/api-access-key.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=cca675d338852f9b61e3a136e35b13fe 2500w" />

## Refreshing API Keys

If you need to update your API key for any reason, you can refresh the API key from the `API Access` page.

<Note>
  When you refresh an API token, the previous token is immediately invalidated and will not longer grant API access.
</Note>

## Rate Limits

SaladCloud's servers enforce rate limits to ensure our APIs are responsive as we grow. The rate limit is tied to an
individual API key and set to 240 requests per minute. If your team would like a higher rate limit, please
[reach out to our team](/support/contact).

## Errors

<Note>Errors from the SaladCloud API may come as HTML documents. Be sure to handle this case in your application.</Note>

SaladCloud uses conventional HTTP response codes to indicate the success or failure of an API request. In general:

* Codes in the 2xx range indicate success.
* Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was
  omitted, a change failed, etc.).
* Codes in the 5xx range indicate an error with SaladCloud's servers (these are rare).
